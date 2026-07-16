#!/usr/bin/env python3
"""IDUNEX intake audit.

Validates the repository scaffold and extracted engine baseline. This is not the
full M02/M03 audit; it only verifies that the GitHub import is structurally safe.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

REQUIRED_ENGINE_DIRS = [
    "00_INDEX",
    "01_CANON_REGISTRIES",
    "02_RESEARCH_CORPUS",
    "03_PROJECT_FACTORY",
    "04_AGENT_FACTORY",
    "05_RUNTIME_CORE_LIBRARY",
    "06_MULTIMODAL_CONTRACTS",
    "07_VALIDATION_QA_GAUNTLET",
    "08_EVIDENCE_LINEAGE",
    "09_TEMPLATES_FIXTURES",
    "10_INTERNAL_MANUALS",
    "11_RELEASE_INTERNAL",
    "12_OUTPUT_CONTRACTS",
    "13_UPDATE_MIGRATION",
    "14_HISTORICAL_NON_AUTHORITY",
    "99_MANIFESTS_SHA_LINEAGE",
]

FORBIDDEN_REPO_PATH_PARTS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "dist",
    "coverage",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    engine = root / "engine" / "IDUNEX"
    failures: list[str] = []
    warnings: list[str] = []

    if not engine.is_dir():
        failures.append("Missing engine/IDUNEX directory")
    else:
        for required in REQUIRED_ENGINE_DIRS:
            if not (engine / required).is_dir():
                failures.append(f"Missing engine directory: {required}")

    manifest_path = root / "governance" / "baseline" / "IDUNEX_MOTOR_v1.0.0_BASELINE_RECEIPT.json"
    if not manifest_path.is_file():
        failures.append("Missing baseline receipt manifest")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if manifest.get("status") != "EN_REVISION":
                warnings.append("Baseline manifest status is not EN_REVISION")
        except Exception as exc:  # noqa: BLE001
            failures.append(f"Cannot parse baseline manifest: {exc}")

    if not (root / ".github" / "workflows" / "intake.yml").is_file():
        failures.append("Missing .github/workflows/intake.yml")

    file_count = 0
    bytes_total = 0
    max_rel_len = 0
    longest_path = ""
    for path in root.rglob("*"):
        rel = path.relative_to(root).as_posix()
        if len(rel) > max_rel_len:
            max_rel_len = len(rel)
            longest_path = rel
        rel_parts = set(path.relative_to(root).parts)
        if rel_parts & FORBIDDEN_REPO_PATH_PARTS and path.is_file():
            warnings.append(f"Ignored/generated path present: {path.relative_to(root)}")
        if path.is_file():
            file_count += 1
            bytes_total += path.stat().st_size
    if max_rel_len > 125:
        warnings.append(f"Path length above Windows-safe target: {max_rel_len} chars: {longest_path}")

    report = {
        "result": "FAIL" if failures else "PASS",
        "scope": "repository_intake_only_not_full_motor_audit",
        "file_count": file_count,
        "bytes_total": bytes_total,
        "max_relative_path_length": max_rel_len,
        "longest_path": longest_path,
        "failures": failures,
        "warnings": warnings,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
