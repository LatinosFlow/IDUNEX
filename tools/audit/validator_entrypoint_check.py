#!/usr/bin/env python3
"""AUD-009 scanner for the single authoritative validator entrypoint.

This is a repository consistency check, not a motor closure validator.  It
never declares M02_PASS and cannot authorize Demo, release, tag, or closure.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REGISTRY_PATH = Path(
    "engine/IDUNEX/07_VALIDATION_QA_GAUNTLET/"
    "22_QA_GAUNTLET_C_a85c6f84/VALIDATOR_SURFACE_REGISTRY.json"
)
HISTORICAL_DIRS = {
    "12_HISTORICAL_NON_AUTHORITY",
    "14_HISTORICAL_NON_AUTHORITY",
}
SUBCHECK_GUARD_MARKER = "_enforce_subcheck_invocation(__file__, __name__)"


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _active_engine_python(engine_root: Path) -> set[str]:
    paths: set[str] = set()
    for path in engine_root.rglob("*.py"):
        relative = path.relative_to(engine_root)
        if any(part in HISTORICAL_DIRS for part in relative.parts):
            continue
        paths.add(relative.as_posix())
    return paths


def _surface_groups(registry: dict[str, Any]) -> list[tuple[str, list[dict[str, Any]]]]:
    engine = registry.get("engine_surfaces", {})
    return [
        ("authoritative_entrypoints", engine.get("authoritative_entrypoints", [])),
        ("subvalidators", engine.get("subvalidators", [])),
        ("internal_support_modules", engine.get("internal_support_modules", [])),
        ("scoped_domain_commands", engine.get("scoped_domain_commands", [])),
    ]


def check_repository(
    repo_root: Path, registry_path: Path | None = None
) -> tuple[list[str], dict[str, Any]]:
    repo_root = repo_root.resolve()
    engine_root = repo_root / "engine" / "IDUNEX"
    registry_file = (registry_path or (repo_root / REGISTRY_PATH)).resolve()
    findings: list[str] = []

    if not registry_file.is_file():
        return [f"missing validator surface registry: {registry_file}"], {}
    try:
        registry = _read_json(registry_file)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid validator surface registry: {exc}"], {}

    groups = _surface_groups(registry)
    entrypoints = groups[0][1]
    if len(entrypoints) != 1:
        findings.append(
            f"expected exactly one authoritative entrypoint, found {len(entrypoints)}"
        )
    if registry.get("global_closure_entrypoint_count") != 1:
        findings.append("global_closure_entrypoint_count must equal 1")

    all_surfaces: list[tuple[str, dict[str, Any]]] = []
    for group_name, items in groups:
        if not isinstance(items, list):
            findings.append(f"{group_name} must be a list")
            continue
        all_surfaces.extend((group_name, item) for item in items)

    classified_paths: list[str] = []
    for group_name, surface in all_surfaces:
        path = surface.get("path")
        if not isinstance(path, str) or not path:
            findings.append(f"{group_name} contains a surface without a path")
            continue
        classified_paths.append(path)
        if not (engine_root / path).is_file():
            findings.append(f"classified engine surface is missing: {path}")
        allowed_global = group_name == "authoritative_entrypoints"
        if surface.get("global_closure_capable") is not allowed_global:
            findings.append(
                f"{path}: global_closure_capable must be {allowed_global} for {group_name}"
            )

    duplicates = sorted(
        {path for path in classified_paths if classified_paths.count(path) > 1}
    )
    if duplicates:
        findings.append("engine surface paths classified more than once: " + ", ".join(duplicates))

    actual_engine_paths = _active_engine_python(engine_root)
    classified_engine_paths = set(classified_paths)
    unclassified = sorted(actual_engine_paths - classified_engine_paths)
    stale = sorted(classified_engine_paths - actual_engine_paths)
    if unclassified:
        findings.append("unclassified active engine Python: " + ", ".join(unclassified))
    if stale:
        findings.append("registry paths not active engine Python: " + ", ".join(stale))

    subvalidators = groups[1][1]
    entrypoint_paths = {
        item.get("path") for item in entrypoints if isinstance(item.get("path"), str)
    }
    subvalidator_paths = {
        item.get("path")
        for item in subvalidators
        if isinstance(item.get("path"), str)
    }
    active_validator_scripts = {
        path
        for path in actual_engine_paths
        if Path(path).name.startswith("VALIDATE")
    }
    expected_validator_scripts = entrypoint_paths | subvalidator_paths
    if active_validator_scripts != expected_validator_scripts:
        findings.append(
            "VALIDATE*.py classification must be entrypoint or subvalidator only; "
            f"unclassified={sorted(active_validator_scripts - expected_validator_scripts)}, "
            f"misclassified={sorted(expected_validator_scripts - active_validator_scripts)}"
        )
    for surface in subvalidators:
        path = surface.get("path")
        if not isinstance(path, str):
            continue
        if surface.get("direct_cli") != "BLOCKED":
            findings.append(f"{path}: subvalidator direct_cli must be BLOCKED")
        source_path = engine_root / path
        if source_path.is_file():
            source = source_path.read_text(encoding="utf-8", errors="replace")
            if SUBCHECK_GUARD_MARKER not in source:
                findings.append(f"{path}: delegated subcheck guard is missing")

    repository_tools = registry.get("repository_validation_tools", [])
    registered_tools: set[str] = set()
    for item in repository_tools:
        path = item.get("path")
        if not isinstance(path, str):
            findings.append("repository_validation_tools contains an invalid path")
            continue
        registered_tools.add(path)
        if item.get("global_closure_capable") is not False:
            findings.append(f"{path}: repository check cannot emit global closure")
        if not (repo_root / path).is_file():
            findings.append(f"registered repository check is missing: {path}")

    actual_tools = {
        path.relative_to(repo_root).as_posix()
        for path in (repo_root / "tools" / "audit").glob("*.py")
    }
    missing_tool_classification = sorted(actual_tools - registered_tools)
    stale_tool_classification = sorted(registered_tools - actual_tools)
    if missing_tool_classification:
        findings.append(
            "unclassified repository validation tool: "
            + ", ".join(missing_tool_classification)
        )
    if stale_tool_classification:
        findings.append(
            "registered repository validation tool is not active: "
            + ", ".join(stale_tool_classification)
        )

    summary = {
        "entrypoint_count": len(entrypoints),
        "subvalidator_count": len(subvalidators),
        "active_validator_script_count": len(active_validator_scripts),
        "engine_python_surface_count": len(actual_engine_paths),
        "repository_validation_tool_count": len(actual_tools),
        "classified_engine_surface_count": len(classified_engine_paths),
    }
    return findings, summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--registry")
    args = parser.parse_args()

    repo_root = Path(args.repo_root)
    registry = Path(args.registry) if args.registry else None
    findings, summary = check_repository(repo_root, registry)
    report = {
        "result": "CONSISTENT" if not findings else "INCONSISTENT",
        "scope": "AUD-009_VALIDATOR_ENTRYPOINT_CONSISTENCY_ONLY",
        "motor_status": "EN_REVISION",
        "m02_result": "M02_PASS",
        "global_closure_authorized": False,
        "m02_decision_authority": False,
        **summary,
        "findings": findings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
