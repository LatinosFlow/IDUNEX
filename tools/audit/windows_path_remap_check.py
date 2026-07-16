#!/usr/bin/env python3
"""AUD-005 Windows-safe path resolver and referential-integrity lint.

The canonical original-to-safe table remains
``governance/baseline/WINDOWS_PATH_SAFE_REMAP.json``.  This module consumes
that table; it does not create a second mapping authority.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


MAP_PATH = Path("governance/baseline/WINDOWS_PATH_SAFE_REMAP.json")
ENGINE_ROOT = Path("engine/IDUNEX")

TEXT_SUFFIXES = {".csv", ".json", ".md", ".py", ".txt", ".yaml", ".yml"}
SCAN_ROOTS = (
    Path("engine/IDUNEX"),
    Path("tests"),
    Path("tools"),
    Path("governance"),
    Path("docs"),
)
EXCLUDED_PREFIXES = (
    Path("docs/audits"),
    Path("engine/IDUNEX/14_HISTORICAL_NON_AUTHORITY"),
    Path("governance/authority/REFERENCIA"),
    Path("governance/baseline"),
)

JSON_MANIFESTS = (
    Path("engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json"),
    Path("engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json"),
    Path("engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json"),
    Path("engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/MANIFEST.json"),
)
HASH_MANIFESTS = (
    Path("engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt"),
    Path("engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt"),
)
H62_SAFE = "engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/H62_CLI_N1_N10_CLEAN_EXIT.json"


def _normalise(value: str) -> str:
    return value.strip().replace("\\", "/").lstrip("./")


def _is_under(path: Path, prefix: Path) -> bool:
    try:
        path.relative_to(prefix)
    except ValueError:
        return False
    return True


def _reference_variants(original: str, safe: str) -> Iterable[tuple[str, str]]:
    """Yield repository-, IDUNEX-, and engine-root-relative equivalents."""
    yield original, safe
    if original.startswith("engine/") and safe.startswith("engine/"):
        yield original.removeprefix("engine/"), safe.removeprefix("engine/")
    if original.startswith("engine/IDUNEX/") and safe.startswith("engine/IDUNEX/"):
        yield (
            original.removeprefix("engine/IDUNEX/"),
            safe.removeprefix("engine/IDUNEX/"),
        )


@dataclass(frozen=True)
class RemapEntry:
    original: str
    safe: str
    reason: str


@dataclass
class RemapTable:
    declared_count: int
    entries: tuple[RemapEntry, ...]
    references: dict[str, str]
    conflicts: tuple[str, ...]

    def resolve(self, reference: str) -> str:
        """Resolve an original spelling while preserving its path-root style."""
        normalised = _normalise(reference)
        return self.references.get(normalised, normalised)


def load_remap_table(root: Path) -> RemapTable:
    data = json.loads((root / MAP_PATH).read_text(encoding="utf-8"))
    rows = data.get("mappings", [])
    entries = tuple(
        RemapEntry(
            original=_normalise(str(row.get("original_path", ""))),
            safe=_normalise(str(row.get("windows_safe_path", ""))),
            reason=str(row.get("reason", "")),
        )
        for row in rows
    )

    references: dict[str, str] = {}
    conflicts: list[str] = []
    for entry in entries:
        for original, safe in _reference_variants(entry.original, entry.safe):
            prior = references.get(original)
            if prior is not None and prior != safe:
                conflicts.append(f"{original}: {prior} != {safe}")
            references[original] = safe

    # Directory references are not separate authority rows.  They are inferred
    # only when an entry preserves depth and the corresponding safe directory
    # exists while the original directory does not.
    for entry in entries:
        original_parts = PurePosixPath(entry.original).parts
        safe_parts = PurePosixPath(entry.safe).parts
        if len(original_parts) != len(safe_parts):
            continue
        for depth in range(2, len(original_parts)):
            original_parent = "/".join(original_parts[:depth])
            safe_parent = "/".join(safe_parts[:depth])
            if original_parent == safe_parent:
                continue
            if (root / original_parent).exists() or not (root / safe_parent).is_dir():
                continue
            for original, safe in _reference_variants(original_parent, safe_parent):
                prior = references.get(original)
                if prior is not None and prior != safe:
                    continue
                references[original] = safe

    return RemapTable(
        declared_count=int(data.get("remap_count", -1)),
        entries=entries,
        references=references,
        conflicts=tuple(sorted(set(conflicts))),
    )


def h62_original_path(table: RemapTable) -> str:
    matches = [entry.original for entry in table.entries if entry.safe == H62_SAFE]
    if len(matches) != 1:
        raise ValueError(f"Expected one H62 mapping for {H62_SAFE}, got {len(matches)}")
    return matches[0]


def validate_table(root: Path, table: RemapTable) -> list[str]:
    findings: list[str] = []
    if table.declared_count != len(table.entries):
        findings.append(
            f"remap_count={table.declared_count} but mappings={len(table.entries)}"
        )

    originals = [entry.original for entry in table.entries]
    safe_paths = [entry.safe for entry in table.entries]
    if len(originals) != len(set(originals)):
        findings.append("duplicate original_path entries")
    if len(safe_paths) != len(set(safe_paths)):
        findings.append("windows_safe_path collision")
    findings.extend(f"ambiguous remap: {item}" for item in table.conflicts)

    for entry in table.entries:
        if not entry.original or not entry.safe:
            findings.append("mapping contains an empty path")
            continue
        if not (root / entry.safe).is_file():
            findings.append(f"missing remapped target: {entry.safe}")
        if entry.original != entry.safe and (root / entry.original).exists():
            findings.append(f"original path still materialised: {entry.original}")
    return findings


def _is_scan_excluded(relative: Path) -> bool:
    return any(_is_under(relative, prefix) for prefix in EXCLUDED_PREFIXES)


def _scan_files(root: Path) -> Iterable[Path]:
    seen: set[Path] = set()
    for relative_root in SCAN_ROOTS:
        scan_root = root / relative_root
        if not scan_root.exists():
            continue
        for path in scan_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            relative = path.relative_to(root)
            if relative in seen or _is_scan_excluded(relative):
                continue
            seen.add(relative)
            yield path

    for path in root.iterdir():
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def scan_stale_references(root: Path, table: RemapTable) -> list[dict[str, Any]]:
    """Return original path spellings used by active governed text surfaces."""
    stale_patterns = sorted(
        (
            (original, safe)
            for original, safe in table.references.items()
            if original != safe
        ),
        key=lambda item: len(item[0]),
        reverse=True,
    )
    findings: list[dict[str, Any]] = []
    for path in _scan_files(root):
        text = path.read_text(encoding="utf-8", errors="replace").replace("\\", "/")
        hits: list[dict[str, str]] = []
        consumed: list[str] = []
        for original, safe in stale_patterns:
            if any(original in longer for longer in consumed):
                continue
            if original in text:
                hits.append({"original": original, "safe": safe})
                consumed.append(original)
        if hits:
            findings.append(
                {"path": path.relative_to(root).as_posix(), "references": hits}
            )
    return findings


def _engine_index_target(root: Path, indexed: str) -> Path:
    normalised = _normalise(indexed)
    if normalised.startswith("engine/IDUNEX/"):
        return root / normalised
    if normalised.startswith("IDUNEX/"):
        return root / "engine" / normalised
    return root / ENGINE_ROOT / normalised


def validate_indexed_paths(root: Path) -> tuple[int, list[str]]:
    checked = 0
    missing: list[str] = []

    for relative in JSON_MANIFESTS:
        data = json.loads((root / relative).read_text(encoding="utf-8"))
        for row in data.get("files", []):
            indexed = str(row.get("path", ""))
            checked += 1
            if not _engine_index_target(root, indexed).is_file():
                missing.append(f"{relative.as_posix()}: {indexed}")

    hash_line = re.compile(r"^[0-9a-fA-F]{64}\s{2}(.+)$")
    for relative in HASH_MANIFESTS:
        for line in (root / relative).read_text(encoding="utf-8").splitlines():
            match = hash_line.match(line)
            if not match:
                continue
            indexed = match.group(1)
            checked += 1
            if not _engine_index_target(root, indexed).is_file():
                missing.append(f"{relative.as_posix()}: {indexed}")

    return checked, missing


def audit_repository(root: Path) -> dict[str, Any]:
    root = root.resolve()
    table = load_remap_table(root)
    table_findings = validate_table(root, table)
    stale = scan_stale_references(root, table)
    indexed_path_count, missing_indexed = validate_indexed_paths(root)

    safe_h62 = root / H62_SAFE
    factory = root / (
        "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/"
        "IDUNEX_PROJECT_FACTORY_v1.0.0.py"
    )
    runtime_validator = root / "engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py"
    safe_engine_relative = H62_SAFE.removeprefix("engine/IDUNEX/")
    original_engine_relative = h62_original_path(table).removeprefix("engine/IDUNEX/")
    h62_consumers: dict[str, bool] = {}
    for path in (factory, runtime_validator):
        text = path.read_text(encoding="utf-8", errors="replace")
        h62_consumers[path.relative_to(root).as_posix()] = (
            safe_engine_relative in text and original_engine_relative not in text
        )

    findings = list(table_findings)
    findings.extend(f"stale reference surface: {item['path']}" for item in stale)
    findings.extend(f"missing indexed path: {item}" for item in missing_indexed)
    if not safe_h62.is_file():
        findings.append(f"missing safe H62 evidence: {H62_SAFE}")
    for path, valid in h62_consumers.items():
        if not valid:
            findings.append(f"H62 consumer is not Windows-safe: {path}")

    return {
        "result": "PASS" if not findings else "FAIL",
        "scope": "AUD-005_windows_safe_referential_integrity",
        "mapping_count": len(table.entries),
        "declared_mapping_count": table.declared_count,
        "engine_mapping_count": sum(
            1 for entry in table.entries if entry.original.startswith("engine/IDUNEX/")
        ),
        "mapping_collision_count": len(
            table.entries
        ) - len({entry.safe for entry in table.entries}),
        "materialised_original_path_count": sum(
            1
            for entry in table.entries
            if entry.original != entry.safe and (root / entry.original).exists()
        ),
        "missing_remapped_target_count": sum(
            1 for entry in table.entries if not (root / entry.safe).is_file()
        ),
        "indexed_path_count": indexed_path_count,
        "missing_indexed_path_count": len(missing_indexed),
        "stale_reference_surface_count": len(stale),
        "stale_reference_count": sum(len(item["references"]) for item in stale),
        "stale_references": stale,
        "h62_safe_path": H62_SAFE,
        "h62_safe_path_exists": safe_h62.is_file(),
        "h62_consumers_windows_safe": h62_consumers,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    report = audit_repository(Path(args.repo_root))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["result"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
