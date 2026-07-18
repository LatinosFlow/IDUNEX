#!/usr/bin/env python3
"""AUD-006 governance-state consistency check.

This check validates global repository state only. It does not execute or
certify engine functionality and it never enables Demo, release, or closure.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


STATE_PATH = Path("governance/CURRENT_STATE.json")

JSON_STATE_SURFACES = (
    STATE_PATH,
    # Historical non-authority JSON surfaces (14_HISTORICAL_NON_AUTHORITY/**)
    # are intentionally excluded to keep this scanner scoped to active authority.
    Path("engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/VERSION_MANIFEST.json"),
    Path("engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/PRODUCTIVE_BASE_ENGINE_STATUS.json"),
    Path("engine/IDUNEX/00_INDEX/MASTER_GOVERNANCE_MAP.json"),
    Path("engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/FINAL_RELEASE_STATUS.json"),
)

TEXT_STATE_SURFACES = (
    Path("README.md"),
    Path("GOVERNANCE_STATUS.md"),
    Path("REPOSITORY_MANIFEST.yml"),
    Path("engine/IDUNEX/00_INDEX/ACTIVE_VERSION.txt"),
    Path("engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/ACTIVE_VERSION.md"),
    Path("engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/STATUS.md"),
    Path("engine/IDUNEX/00_INDEX/RELEASE_CERTIFICATE.txt"),
)

SCAN_SUFFIXES = {".json", ".md", ".txt", ".yml", ".yaml"}

EXCLUDED_PREFIXES = (
    Path("governance/authority/REFERENCIA"),
    Path("docs/audits"),
    Path("engine/IDUNEX/14_HISTORICAL_NON_AUTHORITY"),
)

DANGEROUS_PATTERNS = (
    re.compile(r"READY_FOR_PROJECT_DEMO_GENERATION[\"\s]*[:=]\s*(?:TRUE|true)"),
    re.compile(r'"ready_for_project_demo_generation"\s*:\s*true'),
    re.compile(r"ENGINE_TECHNICAL_CLOSURE_PASS"),
    re.compile(r"MOTOR_ACTIVE_STATUS[\"\s]*[:=]\s*READY\b"),
    re.compile(r"TECHNICAL_CLOSURE_AUTHORIZED[\"\s]*[:=]\s*(?:TRUE|true)"),
    re.compile(r"RELEASE_AUTHORIZED[\"\s]*[:=]\s*(?:TRUE|true)"),
    re.compile(r'"release_authorized"\s*:\s*true'),
    re.compile(r"TAG_AUTHORIZED[\"\s]*[:=]\s*(?:TRUE|true)"),
    re.compile(r'"tag_authorized"\s*:\s*true'),
    re.compile(r"PRODUCTIVE_CLOSURE(?:_AUTHORIZED)?[\"\s]*[:=]\s*(?:TRUE|true)"),
    re.compile(r'"productive_closure_authorized"\s*:\s*true'),
    re.compile(r"DEMO_READY[\"\s]*[:=]\s*(?:TRUE|true)"),
    re.compile(r"SCORE=10/10"),
    re.compile(r'"SCORE"\s*:\s*"10/10"'),
    re.compile(r"31/31 PASS"),
    re.compile(r"PRODUCTIVE_BASE_ENGINE_READY"),
)

REFERENCE_MARKERS = (
    "REFERENCIA_SUSTITUIDA",
    "REFERENCIA_HISTORICA_SUSTITUIDA",
)


def _is_under(path: Path, prefix: Path) -> bool:
    try:
        path.relative_to(prefix)
    except ValueError:
        return False
    return True


def _is_excluded(relative: Path) -> bool:
    return any(_is_under(relative, prefix) for prefix in EXCLUDED_PREFIXES)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _value(data: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in data:
            return data[key]
    return None


def validate_current_state_data(data: dict[str, Any]) -> list[str]:
    """Return violations of the fail-closed AUD-006 root state."""
    expected = {
        "motor_status": "EN_REVISION",
        "m02_result": "M02_PASS",
        "ready_for_project_demo_generation": False,
        "release_authorized": False,
        "tag_authorized": False,
        "productive_closure_authorized": False,
        "creative_output_certified": False,
    }
    findings: list[str] = []
    for key, expected_value in expected.items():
        if data.get(key) != expected_value:
            findings.append(
                f"governance/CURRENT_STATE.json: {key} must be {expected_value!r}, "
                f"got {data.get(key)!r}"
            )

    interlock = data.get("interlock")
    if not isinstance(interlock, dict):
        findings.append("governance/CURRENT_STATE.json: interlock must be an object")
    else:
        denied = set(interlock.get("denied_capabilities", []))
        required = {"PROJECT_DEMO_GENERATION", "RELEASE", "TAG", "PRODUCTIVE_CLOSURE"}
        missing = sorted(required - denied)
        if missing:
            findings.append(
                "governance/CURRENT_STATE.json: interlock missing denied capabilities: "
                + ", ".join(missing)
            )
    return findings


def scan_contradictions(root: Path) -> tuple[list[str], int]:
    """Find active enabling claims; allow only explicitly superseded evidence."""
    findings: list[str] = []
    historical_reference_matches = 0

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if _is_excluded(relative):
            continue

        text = _read_text(path)
        matches = [pattern.pattern for pattern in DANGEROUS_PATTERNS if pattern.search(text)]
        if not matches:
            continue

        marked_reference = any(marker in text for marker in REFERENCE_MARKERS)
        has_m02_marker = bool(re.search(r"M02_(?:FAIL|PASS)", text))
        has_demo_false = bool(
            re.search(
                r"READY_FOR_PROJECT_DEMO_GENERATION[\"\s]*[:=]\s*(?:FALSE|false)",
                text,
            )
            or re.search(r'"ready_for_project_demo_generation"\s*:\s*false', text)
        )

        if marked_reference and has_m02_marker and has_demo_false:
            historical_reference_matches += len(matches)
            continue

        findings.append(
            f"{relative.as_posix()}: active or unclassified contradictory state token(s): "
            + ", ".join(matches)
        )

    return findings, historical_reference_matches


def _validate_json_surface(path: Path, data: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    expected = (
        (("motor_status", "MOTOR_STATUS"), "EN_REVISION"),
        (("m02_result", "M02_RESULT"), "M02_PASS"),
        (("ready_for_project_demo_generation", "READY_FOR_PROJECT_DEMO_GENERATION"), False),
        (("release_authorized", "RELEASE_AUTHORIZED"), False),
        (("productive_closure_authorized", "PRODUCTIVE_CLOSURE_AUTHORIZED"), False),
        (("creative_output_certified", "CREATIVE_OUTPUT_CERTIFIED"), False),
    )
    for keys, expected_value in expected:
        observed = _value(data, *keys)
        if observed != expected_value:
            findings.append(
                f"{path.as_posix()}: {'/'.join(keys)} must be {expected_value!r}, got {observed!r}"
            )
    return findings


def audit_repository(root: Path) -> dict[str, Any]:
    root = root.resolve()
    findings: list[str] = []

    state_file = root / STATE_PATH
    state: dict[str, Any] = {}
    if not state_file.is_file():
        findings.append(f"Missing state authority: {STATE_PATH.as_posix()}")
    else:
        try:
            state = json.loads(_read_text(state_file))
            findings.extend(validate_current_state_data(state))
        except json.JSONDecodeError as exc:
            findings.append(f"{STATE_PATH.as_posix()}: invalid JSON: {exc}")

    for relative in JSON_STATE_SURFACES:
        path = root / relative
        if not path.is_file():
            findings.append(f"Missing state surface: {relative.as_posix()}")
            continue
        try:
            data = json.loads(_read_text(path))
        except json.JSONDecodeError as exc:
            findings.append(f"{relative.as_posix()}: invalid JSON: {exc}")
            continue
        findings.extend(_validate_json_surface(relative, data))

    required_text_patterns = (
        ("M02_PASS", re.compile(r"M02_PASS")),
        ("EN_REVISION", re.compile(r"EN_REVISION")),
        (
            "READY_FOR_PROJECT_DEMO_GENERATION=false",
            re.compile(
                r"ready_for_project_demo_generation[\"\s]*[:=]\s*false",
                re.IGNORECASE,
            ),
        ),
        (
            "CREATIVE_OUTPUT_CERTIFIED=false",
            re.compile(r"creative_output_certified[\"\s]*[:=]\s*false", re.IGNORECASE),
        ),
    )
    for relative in TEXT_STATE_SURFACES:
        path = root / relative
        if not path.is_file():
            findings.append(f"Missing state surface: {relative.as_posix()}")
            continue
        text = _read_text(path)
        for label, pattern in required_text_patterns:
            if not pattern.search(text):
                findings.append(f"{relative.as_posix()}: missing required token {label}")

    contradiction_findings, historical_reference_matches = scan_contradictions(root)
    findings.extend(contradiction_findings)

    return {
        "result": "CONSISTENT" if not findings else "INCONSISTENT",
        "scope": "AUD-006_governance_state_only",
        "motor_status": state.get("motor_status"),
        "m02_result": state.get("m02_result"),
        "ready_for_project_demo_generation": state.get(
            "ready_for_project_demo_generation"
        ),
        "release_authorized": state.get("release_authorized"),
        "tag_authorized": state.get("tag_authorized"),
        "productive_closure_authorized": state.get("productive_closure_authorized"),
        "creative_output_certified": state.get("creative_output_certified"),
        "active_contradiction_count": len(contradiction_findings),
        "historical_reference_match_count": historical_reference_matches,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    report = audit_repository(Path(args.repo_root))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["result"] == "CONSISTENT" else 1


if __name__ == "__main__":
    sys.exit(main())
