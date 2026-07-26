#!/usr/bin/env python3
"""AUD-003 physical-tree manifest generator and verifier.

The received ZIP declaration is historical evidence.  This scanner establishes
and verifies a separate, current physical baseline for ``engine/IDUNEX``.  It
does not create a ZIP, release, tag, Demo project, or global M02 decision.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ENGINE_REL = Path("engine/IDUNEX")
MANIFEST_DIR_REL = ENGINE_REL / "99_MANIFESTS_SHA_LINEAGE"
CURRENT_MANIFEST_REL = Path("governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json")
CURRENT_SHA_REL = Path("governance/baseline/IDUNEX_CURRENT_TREE_SHA256.txt")
DIFF_REL = Path("governance/baseline/IDUNEX_BASELINE_DIFF_RECEIVED_TO_CURRENT.json")
RECEIVED_LEDGER_REL = Path(
    "governance/baseline/historical_received/"
    "IDUNEX_MOTOR_v1.0.0_RECEIVED_SHA256SUMS.txt"
)
RECEIPT_REL = Path("governance/baseline/IDUNEX_MOTOR_v1.0.0_BASELINE_RECEIPT.json")
REMAP_REL = Path("governance/baseline/WINDOWS_PATH_SAFE_REMAP.json")
MOVEMENT_REL = Path("docs/audits/AUD-008-movement-reversal-manifest.json")
STATE_REL = Path("governance/CURRENT_STATE.json")
ROOT_ISSUE = "AUD-035"
ROOT_M02_RESULT = "NOT_RECOMPUTED_POST_AUD035"
ROOT_M03_RESULT = "NOT_RECOMPUTED_POST_AUD035"
PHYSICAL_MANIFEST_M02_SNAPSHOT = "NOT_RECOMPUTED_POST_AUD035"
PHYSICAL_MANIFEST_M03_SNAPSHOT = "NOT_RECOMPUTED_POST_AUD035"
PHYSICAL_MANIFEST_STATE_CLASSIFICATION = (
    "PHYSICAL_TREE_SNAPSHOT_NON_AUTHORITY_FOR_CURRENT_M02"
)
CURRENT_TREE_SHA256 = "22d64b639ed7657605787051d936bffc736cfa3d45b8799475adc28ef7ea0aeb"
CURRENT_TREE_FILE_COUNT = 981
CURRENT_TREE_BYTE_COUNT = 47324957

INTERNAL_JSON_MANIFESTS = (
    "99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json",
    "99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json",
    "99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json",
    "99_MANIFESTS_SHA_LINEAGE/MANIFEST.json",
)
INTERNAL_TEXT_MANIFESTS = (
    "99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt",
    "99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt",
)
INTERNAL_MANIFESTS = INTERNAL_JSON_MANIFESTS + INTERNAL_TEXT_MANIFESTS
INTERNAL_EXCLUSIONS = frozenset(INTERNAL_MANIFESTS)

HASH_LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")
TYPE_BY_SUFFIX = {
    ".csv": "csv",
    ".docx": "docx",
    ".json": "json",
    ".md": "markdown",
    ".pdf": "pdf",
    ".py": "python",
    ".txt": "text",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".zip": "zip",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _extension(path: Path) -> str:
    return path.suffix.lower() or "<none>"


def _file_type(path: Path) -> str:
    extension = _extension(path)
    return TYPE_BY_SUFFIX.get(extension, "no_extension" if extension == "<none>" else "binary_or_other")


def snapshot_tree(engine_root: Path, *, exclude_internal: bool = False) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    physical_files = (item for item in engine_root.rglob("*") if item.is_file())
    for path in sorted(
        physical_files,
        key=lambda item: item.relative_to(engine_root).as_posix(),
    ):
        relative = path.relative_to(engine_root).as_posix()
        if exclude_internal and relative in INTERNAL_EXCLUSIONS:
            continue
        records.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "extension": _extension(path),
                "type": _file_type(path),
            }
        )
    return records


def aggregate_sha256(records: list[dict[str, Any]]) -> str:
    """Hash canonical path/NUL/bytes/NUL/file-sha/newline records."""
    digest = hashlib.sha256()
    for record in sorted(records, key=lambda item: item["path"]):
        line = (
            f"{record['path']}\0{record['bytes']}\0{record['sha256']}\n"
        ).encode("utf-8")
        digest.update(line)
    return digest.hexdigest()


def _counts(records: list[dict[str, Any]], key: str) -> dict[str, int]:
    return dict(sorted(Counter(str(item[key]) for item in records).items()))


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _internal_payload(records: list[dict[str, Any]], m02_result: str, m03_result: str) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "manifest_class": "CURRENT_PHYSICAL_ENGINE_INTERNAL_NON_SELF_REFERENTIAL",
        "semantic_version": "v1.0.0",
        "version_bump": "NO",
        "correction_mode": "DIRECT_CANONICAL_NO_PATCH",
        "correction_scope": "AUD-030_EXTERNAL_ARTIFACTS_POST_H410",
        "motor_status": "EN_REVISION",
        "m02_result": m02_result,
        "m03_result": m03_result,
        "release_authorized": False,
        "file_count": len(records),
        "byte_count": sum(item["bytes"] for item in records),
        "tree_sha256": aggregate_sha256(records),
        "tree_sha256_algorithm": "SHA256(path_utf8 + NUL + decimal_bytes + NUL + file_sha256 + LF), sorted by path",
        "counts_by_extension": _counts(records, "extension"),
        "counts_by_type": _counts(records, "type"),
        "SELF_HASH_EXCLUDED_WITH_REASON": "NON_SELF_REFERENTIAL_INTERNAL_MANIFEST_POLICY",
        "self_excluded_manifest_paths": sorted(INTERNAL_EXCLUSIONS),
        "files": records,
    }


def _external_payload(records: list[dict[str, Any]], m02_result: str, m03_result: str) -> dict[str, Any]:
    repository_records = [dict(item, path=f"engine/IDUNEX/{item['path']}") for item in records]
    return {
        "schema_version": 1,
        "manifest_id": "IDUNEX_CURRENT_PHYSICAL_TREE",
        "baseline_class": "CURRENT_CORRECTED_REPOSITORY_TREE_NOT_RELEASE",
        "scope": "engine/IDUNEX",
        "semantic_version": "v1.0.0",
        "motor_status": "EN_REVISION",
        "m02_result": m02_result,
        "m03_result": m03_result,
        "release_authorized": False,
        "coverage": "ALL_PHYSICAL_FILES_IN_SCOPE",
        "file_count": len(repository_records),
        "byte_count": sum(item["bytes"] for item in repository_records),
        "tree_sha256": aggregate_sha256(repository_records),
        "tree_sha256_algorithm": "SHA256(repo_path_utf8 + NUL + decimal_bytes + NUL + file_sha256 + LF), sorted by path",
        "counts_by_extension": _counts(repository_records, "extension"),
        "counts_by_type": _counts(repository_records, "type"),
        "exclusions": [],
        "files": repository_records,
    }


def _internal_text(records: list[dict[str, Any]], m02_result: str, m03_result: str) -> str:
    header = (
        "# manifest_class=CURRENT_PHYSICAL_ENGINE_INTERNAL_NON_SELF_REFERENTIAL\n"
        "# semantic_version=v1.0.0\n"
        "# correction_scope=AUD-030_EXTERNAL_ARTIFACTS_POST_H410\n"
        "# motor_status=EN_REVISION\n"
        f"# m02_result={m02_result}\n"
        f"# m03_result={m03_result}\n"
        "# release_authorized=false\n"
        "# exclusions=99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json,"
        "99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json,"
        "99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json,"
        "99_MANIFESTS_SHA_LINEAGE/MANIFEST.json,"
        "99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt,"
        "99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt\n"
    )
    return header + "".join(
        f"{item['sha256']}  {item['path']}\n" for item in records
    )


def parse_received_ledger(path: Path) -> dict[str, str]:
    records: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HASH_LINE.match(line)
        if match:
            records[match.group(2)] = match.group(1)
    return records


def _historical_resolver(root: Path) -> tuple[dict[str, str], int]:
    remap = json.loads((root / REMAP_REL).read_text(encoding="utf-8"))
    engine_map = {
        row["original_path"].removeprefix("engine/IDUNEX/"): row[
            "windows_safe_path"
        ].removeprefix("engine/IDUNEX/")
        for row in remap.get("mappings", [])
        if row.get("original_path", "").startswith("engine/IDUNEX/")
    }
    movement = json.loads((root / MOVEMENT_REL).read_text(encoding="utf-8"))
    post_movement = {
        row["origin"].replace("\\", "/"): row["destination"].replace("\\", "/")
        for row in movement.get("movements", [])
    }
    resolved = dict(post_movement)
    resolved.update({
        original: post_movement.get(safe, safe) for original, safe in engine_map.items()
    })
    return resolved, len(engine_map)


def build_diff(root: Path, current_indexable: list[dict[str, Any]]) -> dict[str, Any]:
    received = parse_received_ledger(root / RECEIVED_LEDGER_REL)
    resolver, engine_mapping_count = _historical_resolver(root)
    current = {item["path"]: item for item in current_indexable}
    resolved_targets: set[str] = set()
    modified: list[dict[str, Any]] = []
    missing: list[dict[str, str]] = []
    unchanged_count = 0
    resolved_path_change_count = 0

    for received_path, received_sha in sorted(received.items()):
        current_path = resolver.get(received_path, received_path)
        resolved_targets.add(current_path)
        if current_path != received_path:
            resolved_path_change_count += 1
        record = current.get(current_path)
        if record is None:
            missing.append({"received_path": received_path, "resolved_current_path": current_path})
        elif record["sha256"] == received_sha:
            unchanged_count += 1
        else:
            modified.append(
                {
                    "received_path": received_path,
                    "current_path": current_path,
                    "received_sha256": received_sha,
                    "current_sha256": record["sha256"],
                    "current_bytes": record["bytes"],
                }
            )

    added = [current[path] for path in sorted(set(current) - resolved_targets)]
    receipt = json.loads((root / RECEIPT_REL).read_text(encoding="utf-8"))
    return {
        "schema_version": 1,
        "comparison": "HISTORICAL_RECEIVED_DECLARATION_TO_CURRENT_CORRECTED_TREE",
        "historical_received": {
            "classification": "HISTORICAL_DECLARED_BASELINE_NOT_CURRENT_AUTHORITY",
            "source_zip_filename": receipt.get("source_zip_filename"),
            "source_zip_declared_sha256": receipt.get("source_zip_sha256"),
            "source_zip_declared_entry_count": receipt.get("source_zip_entry_count"),
            "source_zip_physical_status_in_repo": "ABSENT_BY_STORAGE_POLICY_NOT_RECOMPUTED_IN_AUD003",
            "received_indexed_file_count": len(received),
            "received_self_excluded_manifest_count": len(INTERNAL_EXCLUSIONS),
            "received_ledger": RECEIVED_LEDGER_REL.as_posix(),
        },
        "current_corrected": {
            "classification": "CURRENT_REPRODUCIBLE_REPOSITORY_TREE_NOT_RELEASE",
            "physical_file_count": len(current_indexable) + len(INTERNAL_EXCLUSIONS),
            "internal_indexed_file_count": len(current_indexable),
            "external_manifest": CURRENT_MANIFEST_REL.as_posix(),
        },
        "resolution": {
            "windows_safe_engine_mapping_count": engine_mapping_count,
            "received_paths_changed_after_remap_or_movement": resolved_path_change_count,
            "mapping_authority": REMAP_REL.as_posix(),
            "post_remap_movement_ledger": MOVEMENT_REL.as_posix(),
        },
        "summary": {
            "unchanged_content_count": unchanged_count,
            "modified_content_count": len(modified),
            "missing_after_resolution_count": len(missing),
            "added_current_count": len(added),
        },
        "modified": modified,
        "missing_after_resolution": missing,
        "added_current": added,
        "global_conclusion": "AUD030_ENGINE_TREE_REBUILT_M02_M03_NOT_RECOMPUTED_EN_REVISION",
    }


def write_artifacts(root: Path) -> dict[str, Any]:
    root = root.resolve()
    state = json.loads((root / STATE_REL).read_text(encoding="utf-8"))
    if not (root / RECEIVED_LEDGER_REL).is_file():
        raise FileNotFoundError(
            f"Historical received ledger must be preserved before regeneration: {RECEIVED_LEDGER_REL}"
        )
    engine_root = root / ENGINE_REL
    m02_result=state.get("m02_result")
    m03_result=state.get("m03_result")
    if (
        state.get("issue")!=ROOT_ISSUE
        or m02_result!=PHYSICAL_MANIFEST_M02_SNAPSHOT
        or m03_result!=PHYSICAL_MANIFEST_M03_SNAPSHOT
    ):
        raise ValueError("AUD035_BLOCKED_INCOHERENT_RECOMPUTATION_STATE")
    indexable = snapshot_tree(engine_root, exclude_internal=True)
    internal_payload = _internal_payload(indexable, m02_result, m03_result)
    for relative in INTERNAL_JSON_MANIFESTS:
        _write_json(engine_root / relative, internal_payload)

    text = _internal_text(indexable, m02_result, m03_result)
    for relative in INTERNAL_TEXT_MANIFESTS:
        (engine_root / relative).write_text(text, encoding="utf-8", newline="\n")

    complete = snapshot_tree(engine_root)
    external_payload = _external_payload(complete, m02_result, m03_result)
    _write_json(root / CURRENT_MANIFEST_REL, external_payload)
    (root / CURRENT_SHA_REL).write_text(
        "# AUD-003 current physical engine tree aggregate; not a ZIP or release SHA256\n"
        f"{external_payload['tree_sha256']}  engine/IDUNEX\n",
        encoding="utf-8",
        newline="\n",
    )
    _write_json(root / DIFF_REL, build_diff(root, indexable))
    return external_payload


def verify_manifest_records(
    engine_root: Path, records: list[dict[str, Any]], *, repository_paths: bool
) -> dict[str, Any]:
    actual = snapshot_tree(engine_root)
    expected_by_path: dict[str, dict[str, Any]] = {}
    malformed: list[str] = []
    for row in records:
        path = str(row.get("path", "")).replace("\\", "/")
        if repository_paths:
            prefix = "engine/IDUNEX/"
            if not path.startswith(prefix):
                malformed.append(path or "<empty>")
                continue
            path = path.removeprefix(prefix)
        expected_by_path[path] = row

    actual_by_path = {row["path"]: row for row in actual}
    duplicate_path_count = len(records) - len(expected_by_path) - len(malformed)
    missing_indexed = sorted(set(expected_by_path) - set(actual_by_path))
    unmanifested = sorted(set(actual_by_path) - set(expected_by_path))
    hash_mismatches: list[dict[str, Any]] = []
    metadata_mismatches: list[dict[str, Any]] = []
    for path in sorted(set(expected_by_path) & set(actual_by_path)):
        expected = expected_by_path[path]
        observed = actual_by_path[path]
        if expected.get("sha256") != observed["sha256"]:
            hash_mismatches.append(
                {"path": path, "expected": expected.get("sha256"), "actual": observed["sha256"]}
            )
        for key in ("bytes", "extension", "type"):
            if expected.get(key) != observed[key]:
                metadata_mismatches.append(
                    {"path": path, "field": key, "expected": expected.get(key), "actual": observed[key]}
                )
    return {
        "indexed_missing_count": len(missing_indexed),
        "physical_unmanifested_count": len(unmanifested),
        "hash_mismatch_count": len(hash_mismatches),
        "metadata_mismatch_count": len(metadata_mismatches),
        "malformed_path_count": len(malformed),
        "duplicate_path_count": duplicate_path_count,
        "indexed_missing": missing_indexed,
        "physical_unmanifested": unmanifested,
        "hash_mismatches": hash_mismatches,
        "metadata_mismatches": metadata_mismatches,
        "malformed_paths": malformed,
    }


def _verify_internal_manifest(root: Path, relative: str) -> dict[str, Any]:
    payload = json.loads((root / ENGINE_REL / relative).read_text(encoding="utf-8"))
    engine_root = root / ENGINE_REL
    actual_indexable = snapshot_tree(engine_root, exclude_internal=True)
    observed = payload.get("files", [])
    expected_paths = {item["path"] for item in actual_indexable}
    observed_paths = {str(item.get("path", "")) for item in observed}
    hash_mismatches = []
    expected_by_path = {item["path"]: item for item in actual_indexable}
    for row in observed:
        path = str(row.get("path", ""))
        expected = expected_by_path.get(path)
        if expected and any(row.get(key) != expected[key] for key in ("sha256", "bytes", "extension", "type")):
            hash_mismatches.append(path)
    stale_exclusion_entries = sorted(observed_paths & INTERNAL_EXCLUSIONS)
    return {
        "path": f"engine/IDUNEX/{relative}",
        "indexed_missing_count": len(expected_paths - observed_paths),
        "physical_unmanifested_count": len(observed_paths - expected_paths),
        "hash_or_metadata_mismatch_count": len(hash_mismatches),
        "self_exclusion_violation_count": len(stale_exclusion_entries),
        "duplicate_path_count": len(observed) - len(observed_paths),
        "declared_file_count_matches": payload.get("file_count") == len(observed),
        "declared_tree_sha256_matches": payload.get("tree_sha256") == aggregate_sha256(observed),
        "m02_result": payload.get("m02_result"),
        "m03_result": payload.get("m03_result"),
    }


def _stale_manifest_paths(root: Path) -> list[dict[str, str]]:
    remap = json.loads((root / REMAP_REL).read_text(encoding="utf-8"))
    original_engine_paths = {
        row["original_path"].removeprefix("engine/IDUNEX/")
        for row in remap.get("mappings", [])
        if row.get("original_path", "").startswith("engine/IDUNEX/")
        and row.get("original_path") != row.get("windows_safe_path")
    }
    findings: list[dict[str, str]] = []
    for relative in INTERNAL_JSON_MANIFESTS:
        payload = json.loads((root / ENGINE_REL / relative).read_text(encoding="utf-8"))
        for row in payload.get("files", []):
            if row.get("path") in original_engine_paths:
                findings.append({"manifest": relative, "path": row["path"]})
    for relative in INTERNAL_TEXT_MANIFESTS:
        for line in (root / ENGINE_REL / relative).read_text(encoding="utf-8").splitlines():
            match = HASH_LINE.match(line)
            if match and match.group(2) in original_engine_paths:
                findings.append({"manifest": relative, "path": match.group(2)})
    return findings


def audit_repository(root: Path) -> dict[str, Any]:
    root = root.resolve()
    findings: list[str] = []
    state = json.loads((root / STATE_REL).read_text(encoding="utf-8"))
    current = json.loads((root / CURRENT_MANIFEST_REL).read_text(encoding="utf-8"))
    external = verify_manifest_records(
        root / ENGINE_REL, current.get("files", []), repository_paths=True
    )
    if any(external[key] for key in (
        "indexed_missing_count",
        "physical_unmanifested_count",
        "hash_mismatch_count",
        "metadata_mismatch_count",
        "malformed_path_count",
        "duplicate_path_count",
    )):
        findings.append("CURRENT_EXTERNAL_MANIFEST_MISMATCH")

    external_records = current.get("files", [])
    declared_tree_ok = current.get("tree_sha256") == aggregate_sha256(external_records)
    declared_count_ok = current.get("file_count") == len(external_records)
    if not declared_tree_ok or not declared_count_ok:
        findings.append("CURRENT_EXTERNAL_SUMMARY_MISMATCH")
    if (
        current.get("m02_result") != PHYSICAL_MANIFEST_M02_SNAPSHOT
        or current.get("m03_result") != PHYSICAL_MANIFEST_M03_SNAPSHOT
    ):
        findings.append("CURRENT_EXTERNAL_PHYSICAL_SNAPSHOT_MISMATCH")

    sha_lines = (root / CURRENT_SHA_REL).read_text(encoding="utf-8").splitlines()
    sha_matches = [HASH_LINE.match(line) for line in sha_lines]
    sha_values = [match.group(1) for match in sha_matches if match]
    companion_ok = sha_values == [current.get("tree_sha256")]
    if not companion_ok:
        findings.append("CURRENT_TREE_SHA_COMPANION_MISMATCH")

    internal = [_verify_internal_manifest(root, path) for path in INTERNAL_JSON_MANIFESTS]
    for result in internal:
        if (
            result["indexed_missing_count"]
            or result["physical_unmanifested_count"]
            or result["hash_or_metadata_mismatch_count"]
            or result["self_exclusion_violation_count"]
            or result["duplicate_path_count"]
            or not result["declared_file_count_matches"]
            or not result["declared_tree_sha256_matches"]
            or result["m02_result"] != PHYSICAL_MANIFEST_M02_SNAPSHOT
            or result["m03_result"] != PHYSICAL_MANIFEST_M03_SNAPSHOT
        ):
            findings.append(f"INTERNAL_MANIFEST_MISMATCH:{result['path']}")

    actual_indexable = snapshot_tree(root / ENGINE_REL, exclude_internal=True)
    expected_text = _internal_text(
        actual_indexable,
        PHYSICAL_MANIFEST_M02_SNAPSHOT,
        PHYSICAL_MANIFEST_M03_SNAPSHOT,
    ).encode("utf-8")
    text_manifest_sync = all(
        (root / ENGINE_REL / path).read_bytes() == expected_text
        for path in INTERNAL_TEXT_MANIFESTS
    )
    text_entries = sum(1 for line in expected_text.decode("utf-8").splitlines() if HASH_LINE.match(line))
    expected_internal_count = len(actual_indexable)
    if not text_manifest_sync or text_entries != expected_internal_count:
        findings.append("INTERNAL_TEXT_MANIFEST_MISMATCH")

    stale = _stale_manifest_paths(root)
    if stale:
        findings.append("STALE_REMAP_PATH_IN_ACTIVE_MANIFEST")

    diff = json.loads((root / DIFF_REL).read_text(encoding="utf-8"))
    if diff.get("summary", {}).get("missing_after_resolution_count") != 0:
        findings.append("RECEIVED_LEDGER_PATH_UNRESOLVED")

    engine_change=state.get("engine_change_control", {})
    state_ok = (
        state.get("issue") == ROOT_ISSUE
        and state.get("motor_status") == "EN_REVISION"
        and state.get("m02_result") == ROOT_M02_RESULT
        and state.get("m03_result") == ROOT_M03_RESULT
        and state.get("ready_for_project_demo_generation") is False
        and state.get("release_authorized") is False
        and state.get("tag_authorized") is False
        and state.get("productive_closure_authorized") is False
        and state.get("oficial_authorized") is False
        and state.get("agent_load_authorized") is False
        and state.get("creative_output_certified") is False
        and isinstance(engine_change, dict)
        and engine_change.get("current_engine_tree_sha256") == CURRENT_TREE_SHA256
        and engine_change.get("current_engine_file_count") == CURRENT_TREE_FILE_COUNT
        and engine_change.get("current_engine_byte_count") == CURRENT_TREE_BYTE_COUNT
        and current.get("tree_sha256") == CURRENT_TREE_SHA256
        and current.get("file_count") == CURRENT_TREE_FILE_COUNT
        and current.get("byte_count") == CURRENT_TREE_BYTE_COUNT
    )
    if not state_ok:
        findings.append("GLOBAL_STATE_INTERLOCK_CHANGED")

    return {
        "audit": "AUD-003_PHYSICAL_BASELINE_SCANNER",
        "result": "PASS" if not findings else "FAIL",
        "aud003_scope_result": "PARTIAL_PASS" if not findings else "FAIL",
        "root_issue": state.get("issue"),
        "root_m02_result": state.get("m02_result"),
        "root_m03_result": state.get("m03_result"),
        "physical_manifest_m02_snapshot": current.get("m02_result"),
        "physical_manifest_m03_snapshot": current.get("m03_result"),
        "physical_manifest_state_classification": PHYSICAL_MANIFEST_STATE_CLASSIFICATION,
        "motor_status": state.get("motor_status"),
        "m02_result": state.get("m02_result"),
        "m03_result": state.get("m03_result"),
        "release_authorized": state.get("release_authorized"),
        "current_tree_manifest": CURRENT_MANIFEST_REL.as_posix(),
        "current_tree_sha256": current.get("tree_sha256"),
        "current_tree_file_count": current.get("file_count"),
        "current_tree_byte_count": current.get("byte_count"),
        "indexed_missing_path_count": external["indexed_missing_count"],
        "physical_unmanifested_path_count": external["physical_unmanifested_count"],
        "stale_active_manifest_path_count": len(stale),
        "obsolete_hash_count": external["hash_mismatch_count"],
        "metadata_mismatch_count": external["metadata_mismatch_count"],
        "external_manifest_summary_matches": declared_tree_ok and declared_count_ok,
        "tree_sha_companion_matches": companion_ok,
        "internal_json_manifests": internal,
        "internal_text_manifest_sync": text_manifest_sync,
        "received_to_current_diff_summary": diff.get("summary"),
        "state_interlock_consistent": state_ok,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Regenerate current manifests and received-to-current difference evidence before verification.",
    )
    args = parser.parse_args()
    root = Path(args.repo_root)
    if args.write:
        write_artifacts(root)
    report = audit_repository(root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["result"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
