#!/usr/bin/env python3
"""AUD-006/AUD-030 governance-state consistency check.

This check validates global repository state only. It does not execute or
certify engine functionality. General Demo generation, release, tag and
productive closure remain fail-closed while the motor is EN_REVISION.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


STATE_PATH = Path("governance/CURRENT_STATE.json")
ENGINE_TREE_MANIFEST_PATH = Path("governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json")
AUD030_RECOMPUTATION_STATE = "NOT_RECOMPUTED_POST_AUD030"

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

CONTROLLED_EXTERNAL_DEMO_STATUSES = {
    "PENDING_AUTHORIZATION",
    "AUTHORIZED_NOT_CONSUMED",
    "CONSUMED",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")


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


def _finding(field: str, expected: Any, actual: Any) -> str:
    return (
        "governance/CURRENT_STATE.json: controlled_external_demo_execution."
        f"{field} must be {expected!r}, got {actual!r}"
    )


def _require_exact(
    controlled: dict[str, Any], field: str, expected: Any, findings: list[str]
) -> None:
    actual = controlled.get(field)
    if actual != expected:
        findings.append(_finding(field, expected, actual))


def _require_nonempty_string(
    controlled: dict[str, Any], field: str, findings: list[str]
) -> None:
    value = controlled.get(field)
    if not isinstance(value, str) or not value.strip():
        findings.append(_finding(field, "non-empty string", value))


def _require_sha256(
    controlled: dict[str, Any], field: str, findings: list[str]
) -> None:
    value = controlled.get(field)
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        findings.append(_finding(field, "64 lowercase hexadecimal characters", value))


def validate_controlled_external_demo_execution(data: Any) -> list[str]:
    """Validate the fail-closed single external Demo execution state machine."""
    if not isinstance(data, dict):
        return [
            "governance/CURRENT_STATE.json: controlled_external_demo_execution must be an object"
        ]

    findings: list[str] = []
    status = data.get("status")

    _require_exact(data, "schema_version", 1, findings)
    if status not in CONTROLLED_EXTERNAL_DEMO_STATUSES:
        findings.append(
            _finding("status", sorted(CONTROLLED_EXTERNAL_DEMO_STATUSES), status)
        )

    _require_exact(data, "execution_limit", 1, findings)
    _require_exact(data, "allowed_environment", "CHATGPT_NORMAL_EXTERNAL", findings)
    _require_exact(data, "general_project_generation_enabled", False, findings)
    _require_exact(data, "allows_release", False, findings)
    _require_exact(data, "allows_tag", False, findings)
    _require_exact(data, "allows_oficial", False, findings)
    _require_exact(data, "allows_productive_closure", False, findings)
    _require_exact(data, "allows_agent_load", False, findings)
    _require_exact(data, "creative_output_certified", False, findings)

    execution_count = data.get("execution_count")
    if not isinstance(execution_count, int) or isinstance(execution_count, bool):
        findings.append(_finding("execution_count", "integer 0 or 1", execution_count))
    elif execution_count not in {0, 1}:
        findings.append(_finding("execution_count", "0 or 1", execution_count))

    repository_commit = data.get("repository_commit")
    if not isinstance(repository_commit, str) or not GIT_SHA_RE.fullmatch(repository_commit):
        findings.append(
            _finding("repository_commit", "40 lowercase hexadecimal characters", repository_commit)
        )
    _require_sha256(data, "engine_tree_sha256", findings)
    _require_sha256(data, "engine_package_sha256", findings)
    _require_sha256(data, "master_report_sha256", findings)
    _require_nonempty_string(data, "engine_package_filename", findings)
    _require_nonempty_string(data, "master_report_filename", findings)

    authorized = data.get("authorized")
    consumed = data.get("consumed")
    if authorized is True and consumed is True:
        findings.append(
            "governance/CURRENT_STATE.json: controlled_external_demo_execution cannot be authorized and consumed simultaneously"
        )

    if status == "PENDING_AUTHORIZATION":
        _require_exact(data, "authorized", False, findings)
        _require_exact(data, "consumed", False, findings)
        _require_exact(data, "execution_count", 0, findings)
        _require_exact(data, "generate_executions_allowed", 0, findings)
        _require_exact(data, "validate_executions_allowed", 0, findings)
        _require_exact(data, "authorization_id", None, findings)
        _require_exact(data, "prompt_path", None, findings)
        _require_exact(data, "prompt_sha256", None, findings)

    elif status == "AUTHORIZED_NOT_CONSUMED":
        _require_exact(data, "authorized", True, findings)
        _require_exact(data, "consumed", False, findings)
        _require_exact(data, "execution_count", 0, findings)
        _require_exact(data, "generate_executions_allowed", 1, findings)
        validate_allowed = data.get("validate_executions_allowed")
        if validate_allowed not in {0, 1} or isinstance(validate_allowed, bool):
            findings.append(
                _finding("validate_executions_allowed", "integer 0 or 1", validate_allowed)
            )
        _require_nonempty_string(data, "authorization_id", findings)
        _require_nonempty_string(data, "prompt_path", findings)
        _require_sha256(data, "prompt_sha256", findings)

    elif status == "CONSUMED":
        _require_exact(data, "authorized", False, findings)
        _require_exact(data, "consumed", True, findings)
        _require_exact(data, "execution_count", 1, findings)
        _require_exact(data, "generate_executions_allowed", 0, findings)
        _require_exact(data, "validate_executions_allowed", 0, findings)
        _require_nonempty_string(data, "authorization_id", findings)
        _require_nonempty_string(data, "prompt_path", findings)
        _require_sha256(data, "prompt_sha256", findings)

    return findings


def validate_current_state_data(data: dict[str, Any]) -> list[str]:
    """Return violations of the fail-closed post-AUD-030 root state."""
    expected = {
        "issue": "AUD-030",
        "motor_status": "EN_REVISION",
        "m02_result": AUD030_RECOMPUTATION_STATE,
        "m03_result": AUD030_RECOMPUTATION_STATE,
        "ready_for_project_demo_generation": False,
        "release_authorized": False,
        "tag_authorized": False,
        "productive_closure_authorized": False,
        "oficial_authorized": False,
        "agent_load_authorized": False,
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
        required = {
            "PROJECT_DEMO_GENERATION", "RELEASE", "TAG", "PRODUCTIVE_CLOSURE",
            "OFICIAL", "AGENT_LOAD",
        }
        missing = sorted(required - denied)
        if missing:
            findings.append(
                "governance/CURRENT_STATE.json: interlock missing denied capabilities: "
                + ", ".join(missing)
            )

    controlled=data.get("controlled_external_demo_execution")
    findings.extend(validate_controlled_external_demo_execution(controlled))
    if isinstance(controlled, dict):
        post_aud030_expected={
            "status":"CONSUMED",
            "authorized":False,
            "consumed":True,
            "execution_count":1,
            "generate_executions_allowed":0,
            "validate_executions_allowed":0,
            "authorization_id":"AUD-028",
            "project_audit_status":"PROJECT_AUDIT_FAIL_EXTERNAL_SURFACE_DESYNC",
            "project_agent_load_pass":False,
            "project_ready_for_production":False,
            "allows_release":False,
            "allows_tag":False,
            "allows_oficial":False,
            "allows_productive_closure":False,
            "allows_agent_load":False,
            "creative_output_certified":False,
        }
        for field,expected_value in post_aud030_expected.items():
            if controlled.get(field)!=expected_value:
                findings.append(_finding(field, expected_value, controlled.get(field)))
    engine_change=data.get("engine_change_control")
    if not isinstance(engine_change, dict):
        findings.append("governance/CURRENT_STATE.json: engine_change_control must be an object")
    else:
        engine_expected={
            "issue":"AUD-030",
            "base_commit":"fb13a4f5d4bd559b4f1268103630a735b53c8999",
            "previous_engine_tree_sha256":"628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9",
            "current_engine_file_count":981,
            "manifests_recomputed_with_canonical_scanner":True,
            "m02_result":AUD030_RECOMPUTATION_STATE,
            "m03_result":AUD030_RECOMPUTATION_STATE,
        }
        for field,expected_value in engine_expected.items():
            if engine_change.get(field)!=expected_value:
                findings.append(
                    f"governance/CURRENT_STATE.json: engine_change_control.{field} must be {expected_value!r}, got {engine_change.get(field)!r}"
                )
        current_sha=engine_change.get("current_engine_tree_sha256")
        if not isinstance(current_sha, str) or not SHA256_RE.fullmatch(current_sha):
            findings.append("governance/CURRENT_STATE.json: engine_change_control.current_engine_tree_sha256 must be 64 lowercase hexadecimal characters")
        byte_count=engine_change.get("current_engine_byte_count")
        if not isinstance(byte_count, int) or isinstance(byte_count, bool) or byte_count<=0:
            findings.append("governance/CURRENT_STATE.json: engine_change_control.current_engine_byte_count must be a positive integer")
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
        has_m02_marker = bool(
            re.search(r"M02_(?:FAIL|PASS)|NOT_RECOMPUTED_POST_AUD030", text)
        )
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
        (("m02_result", "M02_RESULT"), AUD030_RECOMPUTATION_STATE),
        (("m03_result", "M03_RESULT"), AUD030_RECOMPUTATION_STATE),
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

    engine_manifest={}
    engine_manifest_path=root/ENGINE_TREE_MANIFEST_PATH
    if not engine_manifest_path.is_file():
        findings.append(f"Missing engine tree manifest: {ENGINE_TREE_MANIFEST_PATH.as_posix()}")
    else:
        try:
            engine_manifest=json.loads(_read_text(engine_manifest_path))
        except json.JSONDecodeError as exc:
            findings.append(f"{ENGINE_TREE_MANIFEST_PATH.as_posix()}: invalid JSON: {exc}")
    engine_change=state.get("engine_change_control", {}) if isinstance(state, dict) else {}
    if isinstance(engine_change, dict) and engine_manifest:
        parity=(
            engine_change.get("current_engine_tree_sha256")==engine_manifest.get("tree_sha256")
            and engine_change.get("current_engine_file_count")==engine_manifest.get("file_count")
            and engine_change.get("current_engine_byte_count")==engine_manifest.get("byte_count")
        )
        if not parity:
            findings.append("governance/CURRENT_STATE.json: engine_change_control does not match canonical engine tree manifest")

    required_text_patterns = (
        (
            "M02_RESULT=NOT_RECOMPUTED_POST_AUD030",
            re.compile(r"M02_(?:RESULT)?[\"\s]*[:=]\s*NOT_RECOMPUTED_POST_AUD030", re.IGNORECASE),
        ),
        (
            "M03_RESULT=NOT_RECOMPUTED_POST_AUD030",
            re.compile(r"M03_(?:RESULT)?[\"\s]*[:=]\s*NOT_RECOMPUTED_POST_AUD030", re.IGNORECASE),
        ),
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

    controlled = state.get("controlled_external_demo_execution", {})
    return {
        "result": "CONSISTENT" if not findings else "INCONSISTENT",
        "scope": "AUD-006_AUD-030_governance_state_only",
        "motor_status": state.get("motor_status"),
        "m02_result": state.get("m02_result"),
        "m03_result": state.get("m03_result"),
        "ready_for_project_demo_generation": state.get(
            "ready_for_project_demo_generation"
        ),
        "release_authorized": state.get("release_authorized"),
        "tag_authorized": state.get("tag_authorized"),
        "productive_closure_authorized": state.get("productive_closure_authorized"),
        "creative_output_certified": state.get("creative_output_certified"),
        "controlled_external_demo_status": controlled.get("status"),
        "controlled_external_demo_authorized": controlled.get("authorized"),
        "controlled_external_demo_consumed": controlled.get("consumed"),
        "current_engine_tree_sha256": engine_change.get("current_engine_tree_sha256") if isinstance(engine_change, dict) else None,
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
