#!/usr/bin/env python3
"""Recomputed AUD-008 no-bloat/no-history scanner.

The scanner never trusts declared PASS surfaces. It hashes the current active
tree, detects milestone paths, verifies the movement/reversal ledger, and
confirms the global motor state remains EN_REVISION / M02_FAIL.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


ENGINE_REL = Path("engine/IDUNEX")
HISTORICAL_REL = Path("14_HISTORICAL_NON_AUTHORITY")
MANIFEST_REL = Path("docs/audits/AUD-008-movement-reversal-manifest.json")
STATE_REL = Path("governance/CURRENT_STATE.json")
H_ROUTE = re.compile(r"(^|[_/.-])H\d", re.IGNORECASE)
SHA256 = re.compile(r"^[0-9a-f]{64}$")
CLASSIFICATIONS = {
    "ACTIVE_AUTHORITY",
    "EVIDENCE_REQUIRED",
    "HISTORICAL_NON_AUTHORITY",
    "DUPLICATE_EXACT",
    "REFERENCE_SUPERSEDED",
}

FROZEN_DUPLICATE_PATH_SETS = {
    frozenset({
        "99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json",
        "99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json",
        "99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json",
        "99_MANIFESTS_SHA_LINEAGE/MANIFEST.json",
    }),
    frozenset({
        "99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt",
        "99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt",
    }),
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def active_files(engine_root: Path) -> list[Path]:
    historical = engine_root / HISTORICAL_REL
    return sorted(
        path for path in engine_root.rglob("*")
        if path.is_file() and historical not in path.parents
    )


def scan_active_tree(engine_root: Path) -> dict:
    hashes: dict[str, list[dict]] = defaultdict(list)
    h_routes: list[str] = []
    files = active_files(engine_root)
    for path in files:
        relative = path.relative_to(engine_root).as_posix()
        size = path.stat().st_size
        hashes[_sha256(path)].append({"path": relative, "bytes": size})
        if H_ROUTE.search(relative):
            h_routes.append(relative)

    exact_groups = []
    justified_groups = []
    unjustified_groups = []
    for digest, entries in sorted(hashes.items()):
        if len(entries) < 2:
            continue
        paths = frozenset(item["path"] for item in entries)
        group = {
            "sha256": digest,
            "paths": sorted(paths),
            "file_count": len(entries),
            "bytes_each": entries[0]["bytes"],
            "redundant_bytes": (len(entries) - 1) * entries[0]["bytes"],
        }
        exact_groups.append(group)
        if paths in FROZEN_DUPLICATE_PATH_SETS:
            group["justification"] = "AUD008_FINAL_MANIFESTS_FROZEN_OUT_OF_SCOPE"
            justified_groups.append(group)
        else:
            unjustified_groups.append(group)

    return {
        "active_file_count": len(files),
        "active_bytes": sum(path.stat().st_size for path in files),
        "exact_duplicate_group_count": len(exact_groups),
        "exact_duplicate_file_count": sum(group["file_count"] for group in exact_groups),
        "exact_duplicate_redundant_bytes": sum(group["redundant_bytes"] for group in exact_groups),
        "justified_duplicate_group_count": len(justified_groups),
        "unjustified_duplicate_group_count": len(unjustified_groups),
        "unjustified_duplicate_groups": unjustified_groups,
        "justified_duplicate_groups": justified_groups,
        "active_h_route_count": len(h_routes),
        "active_h_routes": sorted(h_routes),
    }


def movement_conflicts(engine_root: Path, payload: dict) -> list[dict]:
    conflicts = []
    historical_prefix = HISTORICAL_REL.as_posix() + "/"
    movements = payload.get("movements")
    if not isinstance(movements, list) or not movements:
        return [{"code": "MOVEMENT_LEDGER_EMPTY_OR_INVALID"}]
    for index, movement in enumerate(movements):
        origin = movement.get("origin", "")
        destination = movement.get("destination", "")
        operation = movement.get("operation")
        classification = movement.get("classification")
        authority_after = movement.get("authority_after")
        before_sha = movement.get("sha256_before")
        expected_sha = movement.get("sha256_after")
        reverse = movement.get("reverse", {})
        if classification not in CLASSIFICATIONS:
            conflicts.append({
                "code": "UNKNOWN_CLASSIFICATION",
                "index": index,
                "classification": classification,
            })
        if not isinstance(before_sha, str) or not SHA256.fullmatch(before_sha):
            conflicts.append({"code": "INVALID_SHA256_BEFORE", "index": index})
        if not isinstance(expected_sha, str) or not SHA256.fullmatch(expected_sha):
            conflicts.append({"code": "INVALID_SHA256_AFTER", "index": index})
        if not movement.get("reason") or not movement.get("impact"):
            conflicts.append({"code": "REASON_OR_IMPACT_MISSING", "index": index})
        if (
            not isinstance(reverse, dict)
            or reverse.get("from") != destination
            or reverse.get("to") != origin
            or reverse.get("expected_sha256") != expected_sha
        ):
            conflicts.append({"code": "REVERSE_INSTRUCTION_INVALID", "index": index})
        source = engine_root / origin
        target = engine_root / destination
        if source.exists():
            conflicts.append({"code": "ORIGIN_STILL_ACTIVE", "index": index, "origin": origin})
        if not target.is_file():
            conflicts.append({"code": "DESTINATION_MISSING", "index": index, "destination": destination})
            continue
        actual_sha = _sha256(target)
        if actual_sha != expected_sha:
            conflicts.append({
                "code": "DESTINATION_SHA_MISMATCH",
                "index": index,
                "destination": destination,
                "expected": expected_sha,
                "actual": actual_sha,
            })
        if operation == "MOVE_TO_HISTORICAL":
            if not destination.startswith(historical_prefix):
                conflicts.append({
                    "code": "HISTORICAL_MOVE_OUTSIDE_ZONE",
                    "index": index,
                    "destination": destination,
                })
            if authority_after != "NON_AUTHORITY":
                conflicts.append({
                    "code": "HISTORICAL_EVIDENCE_HAS_ACTIVE_AUTHORITY",
                    "index": index,
                    "destination": destination,
                    "authority_after": authority_after,
                })
        elif operation == "RENAME_TO_STABLE":
            if destination.startswith(historical_prefix):
                conflicts.append({
                    "code": "STABLE_AUTHORITY_RENAMED_INTO_HISTORY",
                    "index": index,
                    "destination": destination,
                })
        else:
            conflicts.append({"code": "UNKNOWN_MOVEMENT_OPERATION", "index": index, "operation": operation})
    return conflicts


def summary_conflicts(tree: dict, manifest: dict, movement_conflict_count: int) -> list[dict]:
    """Reject a stale declared after-summary; recomputation remains authoritative."""
    declared = manifest.get("tree_summary", {}).get("after", {})
    declared_duplicates = declared.get("duplicates", {})
    declared_h = declared.get("h_routes", {})
    expected = {
        "active_file_count": tree["active_file_count"],
        "active_bytes": tree["active_bytes"],
        "duplicate_group_count": tree["exact_duplicate_group_count"],
        "duplicate_file_count": tree["exact_duplicate_file_count"],
        "duplicate_redundant_bytes": tree["exact_duplicate_redundant_bytes"],
        "justified_duplicate_group_count": tree["justified_duplicate_group_count"],
        "unjustified_duplicate_group_count": tree["unjustified_duplicate_group_count"],
        "active_h_route_count": tree["active_h_route_count"],
        "movement_conflict_count": movement_conflict_count,
    }
    actual = {
        "active_file_count": declared.get("active_file_count"),
        "active_bytes": declared.get("active_bytes"),
        "duplicate_group_count": declared_duplicates.get("group_count"),
        "duplicate_file_count": declared_duplicates.get("file_count"),
        "duplicate_redundant_bytes": declared_duplicates.get("redundant_bytes"),
        "justified_duplicate_group_count": declared_duplicates.get("justified_group_count"),
        "unjustified_duplicate_group_count": declared_duplicates.get("unjustified_group_count"),
        "active_h_route_count": declared_h.get("path_count"),
        "movement_conflict_count": declared.get("historical_authority_conflict_count"),
    }
    return [] if actual == expected else [{
        "code": "DECLARED_AFTER_SUMMARY_MISMATCH",
        "declared": actual,
        "recomputed": expected,
    }]


def audit_repo(repo_root: Path) -> dict:
    repo_root = repo_root.resolve()
    engine_root = repo_root / ENGINE_REL
    tree = scan_active_tree(engine_root)
    failures = []
    if tree["unjustified_duplicate_group_count"]:
        failures.append("UNJUSTIFIED_ACTIVE_EXACT_DUPLICATES")
    if tree["active_h_route_count"]:
        failures.append("ACTIVE_H_MILESTONE_ROUTES_OUTSIDE_HISTORY")

    try:
        manifest = json.loads((repo_root / MANIFEST_REL).read_text(encoding="utf-8"))
        conflicts = movement_conflicts(engine_root, manifest)
        conflicts.extend(summary_conflicts(tree, manifest, len(conflicts)))
    except Exception as exc:
        manifest = {}
        conflicts = [{"code": "MOVEMENT_LEDGER_UNREADABLE", "error": str(exc)}]
    if conflicts:
        failures.append("MOVEMENT_OR_AUTHORITY_CONFLICT")

    release_surface = engine_root / "11_RELEASE_INTERNAL"
    unexpected_release_files = sorted(
        path.relative_to(engine_root).as_posix()
        for path in release_surface.rglob("*")
        if path.is_file() and path.name != "README.md"
    ) if release_surface.exists() else []
    if unexpected_release_files:
        failures.append("SUPERSEDED_RELEASE_HISTORY_STILL_ACTIVE")

    try:
        state = json.loads((repo_root / STATE_REL).read_text(encoding="utf-8"))
    except Exception as exc:
        state = {"error": str(exc)}
    state_ok = (
        state.get("motor_status") == "EN_REVISION"
        and state.get("m02_result") == "M02_FAIL"
        and state.get("ready_for_project_demo_generation") is False
        and state.get("release_authorized") is False
        and state.get("tag_authorized") is False
    )
    if not state_ok:
        failures.append("GLOBAL_STATE_INTERLOCK_CHANGED")

    authority_conflicts = [
        item for item in conflicts
        if item.get("code") == "HISTORICAL_EVIDENCE_HAS_ACTIVE_AUTHORITY"
    ]
    return {
        "audit": "AUD-008_NO_BLOAT_NO_HISTORY",
        "result": "PASS" if not failures else "FAIL",
        "motor_status": state.get("motor_status"),
        "m02_result": state.get("m02_result"),
        "active_tree": tree,
        "movement_manifest_conflict_count": len(conflicts),
        "movement_manifest_conflicts": conflicts,
        "historical_authority_conflict_count": len(authority_conflicts),
        "historical_authority_conflicts": authority_conflicts,
        "unexpected_release_history_count": len(unexpected_release_files),
        "unexpected_release_history": unexpected_release_files,
        "movement_count": len(manifest.get("movements", [])) if isinstance(manifest, dict) else 0,
        "state_interlock_consistent": state_ok,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    result = audit_repo(Path(args.repo_root))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
