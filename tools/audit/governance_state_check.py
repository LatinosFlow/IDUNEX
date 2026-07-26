#!/usr/bin/env python3
"""AUD-035 governance-state consistency check.

This check validates governance only. It neither executes nor certifies engine
functionality. The engine-internal state snapshots remain deliberately
fail-closed because AUD-034 must not modify engine/IDUNEX.
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
M02_RECOMPUTATION_STATE = "NOT_RECOMPUTED_POST_AUD035"
M03_RECOMPUTATION_STATE = "NOT_RECOMPUTED_POST_AUD035"
CURRENT_ENGINE_TREE_SHA256 = "22d64b639ed7657605787051d936bffc736cfa3d45b8799475adc28ef7ea0aeb"
CURRENT_ENGINE_FILE_COUNT = 981
CURRENT_ENGINE_BYTE_COUNT = 47324957
AUD035_BASE_COMMIT = "2eb99d5c43bae4b2b077c38d0e40923ef7072857"
PREVIOUS_ENGINE_TREE_SHA256 = "58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7"

M02_RECOMPUTATION_EVIDENCE = {
    "run_id": 29941393366,
    "job_id": 88995880545,
    "artifact_id": 8539029665,
    "artifact_name": "idunex-m02-max-29941393366-attempt-1",
    "artifact_sha256": "fd5c9334b96989c714300607dadf742ff63783b8090d90fc3d404b3a22355270",
    "repository_commit": "1fc082bfcae5b590066309727c120500de976378",
    "engine_tree_sha256": "58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7",
    "engine_file_count": 981,
    "engine_byte_count": 47323574,
    "m02_result": "M02_PASS_RECOMPUTED_POST_AUD033",
    "evidence_class": "REFERENCIA_SUSTITUIDA",
    "current_tree_applicability": False,
    "superseded_by": "AUD-035",
    "runtime_validator": "HISTORICAL_REFERENCE_ONLY",
    "matrix": "HISTORICAL_REFERENCE_ONLY",
    "mutation": "HISTORICAL_REFERENCE_ONLY",
    "positive_fixture": "HISTORICAL_REFERENCE_ONLY",
    "restoration_retest": "HISTORICAL_REFERENCE_ONLY",
    "technical_score": "HISTORICAL_REFERENCE_ONLY",
    "creative_output_certified": False,
    "inherited_audit_id": "AUD-026-M02-POST-PR44",
    "inherited_audit_id_classification": "METADATA_HEREDADA_NO_AUTORIDAD_NOMINAL",
}

# AUD-034 establishes the root authority. Engine files are retained as
# explicitly fail-closed legacy snapshots and must not become enabling claims.
LEGACY_ENGINE_JSON_STATE_SURFACES = ()
ROOT_TEXT_STATE_SURFACES = (
    Path("README.md"),
    Path("GOVERNANCE_STATUS.md"),
    Path("REPOSITORY_MANIFEST.yml"),
)
LEGACY_ENGINE_TEXT_STATE_SURFACES = (
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
REFERENCE_MARKERS = ("REFERENCIA_SUSTITUIDA", "REFERENCIA_HISTORICA_SUSTITUIDA")
CONTROLLED_EXTERNAL_DEMO_STATUSES = {
    "PENDING_AUTHORIZATION", "AUTHORIZED_NOT_CONSUMED", "CONSUMED"
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _is_under(path: Path, prefix: Path) -> bool:
    try:
        path.relative_to(prefix)
    except ValueError:
        return False
    return True


def _finding(field: str, expected: Any, actual: Any) -> str:
    return (
        "governance/CURRENT_STATE.json: controlled_external_demo_execution."
        f"{field} must be {expected!r}, got {actual!r}"
    )


def _require_exact(data: dict[str, Any], field: str, expected: Any, findings: list[str]) -> None:
    if data.get(field) != expected:
        findings.append(_finding(field, expected, data.get(field)))


def _require_sha256(data: dict[str, Any], field: str, findings: list[str]) -> None:
    value = data.get(field)
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        findings.append(_finding(field, "64 lowercase hexadecimal characters", value))


def _require_nonempty_string(data: dict[str, Any], field: str, findings: list[str]) -> None:
    value = data.get(field)
    if not isinstance(value, str) or not value.strip():
        findings.append(_finding(field, "non-empty string", value))


def validate_controlled_external_demo_execution(data: Any) -> list[str]:
    """Validate the permanently consumed AUD-028 execution state machine."""
    if not isinstance(data, dict):
        return ["governance/CURRENT_STATE.json: controlled_external_demo_execution must be an object"]
    findings: list[str] = []
    _require_exact(data, "schema_version", 1, findings)
    _require_exact(data, "status", "CONSUMED", findings)
    for field, expected in {
        "authorized": False,
        "consumed": True,
        "execution_limit": 1,
        "execution_count": 1,
        "generate_executions_allowed": 0,
        "validate_executions_allowed": 0,
        "general_project_generation_enabled": False,
        "authorization_id": "AUD-028",
        "project_audit_status": "PROJECT_AUDIT_FAIL_EXTERNAL_SURFACE_DESYNC",
        "project_agent_load_pass": False,
        "project_ready_for_production": False,
        "allows_release": False,
        "allows_tag": False,
        "allows_oficial": False,
        "allows_productive_closure": False,
        "allows_agent_load": False,
        "creative_output_certified": False,
    }.items():
        _require_exact(data, field, expected, findings)
    if data.get("status") not in CONTROLLED_EXTERNAL_DEMO_STATUSES:
        findings.append(_finding("status", sorted(CONTROLLED_EXTERNAL_DEMO_STATUSES), data.get("status")))
    for field in ("engine_tree_sha256", "engine_package_sha256", "master_report_sha256", "prompt_sha256"):
        _require_sha256(data, field, findings)
    for field in ("allowed_environment", "engine_package_filename", "master_report_filename", "prompt_path"):
        _require_nonempty_string(data, field, findings)
    if data.get("allowed_environment") != "CHATGPT_NORMAL_EXTERNAL":
        findings.append(_finding("allowed_environment", "CHATGPT_NORMAL_EXTERNAL", data.get("allowed_environment")))
    repository_commit = data.get("repository_commit")
    if not isinstance(repository_commit, str) or not GIT_SHA_RE.fullmatch(repository_commit):
        findings.append(_finding("repository_commit", "40 lowercase hexadecimal characters", repository_commit))
    return findings


def validate_current_state_data(data: dict[str, Any]) -> list[str]:
    """Return all deviations from the sole AUD-035 governance authority."""
    findings: list[str] = []
    expected = {
        "issue": "AUD-035",
        "motor_status": "EN_REVISION",
        "m02_result": M02_RECOMPUTATION_STATE,
        "m03_result": M03_RECOMPUTATION_STATE,
        "ready_for_project_demo_generation": False,
        "release_authorized": False,
        "tag_authorized": False,
        "productive_closure_authorized": False,
        "oficial_authorized": False,
        "agent_load_authorized": False,
        "creative_output_certified": False,
        "last_failed_m03_run": 30189604763,
        "last_failed_m03_case": "M03-19",
        "last_failed_m03_result": "VALIDATED_FAIL",
    }
    for key, expected_value in expected.items():
        if data.get(key) != expected_value:
            findings.append(f"governance/CURRENT_STATE.json: {key} must be {expected_value!r}, got {data.get(key)!r}")

    interlock = data.get("interlock")
    required_denials = {"PROJECT_DEMO_GENERATION", "RELEASE", "TAG", "PRODUCTIVE_CLOSURE", "OFICIAL", "AGENT_LOAD"}
    if not isinstance(interlock, dict):
        findings.append("governance/CURRENT_STATE.json: interlock must be an object")
    elif missing := sorted(required_denials - set(interlock.get("denied_capabilities", []))):
        findings.append("governance/CURRENT_STATE.json: interlock missing denied capabilities: " + ", ".join(missing))

    findings.extend(validate_controlled_external_demo_execution(data.get("controlled_external_demo_execution")))
    engine_change = data.get("engine_change_control")
    if not isinstance(engine_change, dict):
        findings.append("governance/CURRENT_STATE.json: engine_change_control must be an object")
    else:
        engine_expected = {
            "issue": "AUD-035",
            "base_commit": AUD035_BASE_COMMIT,
            "previous_engine_tree_sha256": PREVIOUS_ENGINE_TREE_SHA256,
            "current_engine_tree_sha256": CURRENT_ENGINE_TREE_SHA256,
            "current_engine_file_count": CURRENT_ENGINE_FILE_COUNT,
            "current_engine_byte_count": CURRENT_ENGINE_BYTE_COUNT,
            "manifests_recomputed_with_canonical_scanner": True,
            "m02_result": M02_RECOMPUTATION_STATE,
            "m03_result": M03_RECOMPUTATION_STATE,
        }
        for field, expected_value in engine_expected.items():
            if engine_change.get(field) != expected_value:
                findings.append(f"governance/CURRENT_STATE.json: engine_change_control.{field} must be {expected_value!r}, got {engine_change.get(field)!r}")

    if "last_failed_m02_run" in data:
        findings.append("governance/CURRENT_STATE.json: last_failed_m02_run must be absent when no current verified M02 failure run exists")

    recomputation = data.get("prior_m02_recomputation_evidence")
    if not isinstance(recomputation, dict):
        findings.append("governance/CURRENT_STATE.json: prior_m02_recomputation_evidence must be an object")
    else:
        for field, expected_value in M02_RECOMPUTATION_EVIDENCE.items():
            if recomputation.get(field) != expected_value:
                findings.append(f"governance/CURRENT_STATE.json: prior_m02_recomputation_evidence.{field} must be {expected_value!r}, got {recomputation.get(field)!r}")
        if recomputation.get("engine_tree_sha256") == CURRENT_ENGINE_TREE_SHA256:
            findings.append("governance/CURRENT_STATE.json: historical M02 evidence must not be linked to the current AUD-035 tree")
    return findings


def _validate_legacy_engine_json_surface(path: Path, data: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    for keys, expected in (
        (("motor_status", "MOTOR_STATUS"), "EN_REVISION"),
        (("m02_result", "M02_RESULT"), M03_RECOMPUTATION_STATE),
        (("m03_result", "M03_RESULT"), M03_RECOMPUTATION_STATE),
        (("ready_for_project_demo_generation", "READY_FOR_PROJECT_DEMO_GENERATION"), False),
        (("release_authorized", "RELEASE_AUTHORIZED"), False),
        (("productive_closure_authorized", "PRODUCTIVE_CLOSURE_AUTHORIZED"), False),
        (("creative_output_certified", "CREATIVE_OUTPUT_CERTIFIED"), False),
    ):
        actual = next((data[key] for key in keys if key in data), None)
        if actual != expected:
            findings.append(f"{path.as_posix()}: {'/'.join(keys)} must remain {expected!r}, got {actual!r}")
    return findings


def scan_contradictions(root: Path) -> tuple[list[str], int]:
    """Find active enabling claims while preserving marked historical references."""
    findings: list[str] = []
    historical_matches = 0
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if any(_is_under(relative, prefix) for prefix in EXCLUDED_PREFIXES):
            continue
        text = _read_text(path)
        matches = [pattern.pattern for pattern in DANGEROUS_PATTERNS if pattern.search(text)]
        if not matches:
            continue
        marked_reference = any(marker in text for marker in REFERENCE_MARKERS)
        has_m02_marker = bool(re.search(r"M02_(?:FAIL|PASS)|NOT_RECOMPUTED_POST_AUD030", text))
        has_demo_false = bool(re.search(r"READY_FOR_PROJECT_DEMO_GENERATION[\"\s]*[:=]\s*(?:FALSE|false)", text) or re.search(r'"ready_for_project_demo_generation"\s*:\s*false', text))
        if marked_reference and has_m02_marker and has_demo_false:
            historical_matches += len(matches)
        else:
            findings.append(f"{relative.as_posix()}: active or unclassified contradictory state token(s): " + ", ".join(matches))
    return findings, historical_matches


def _require_text_tokens(root: Path, surfaces: tuple[Path, ...], patterns: tuple[tuple[str, re.Pattern[str]], ...], findings: list[str]) -> None:
    for relative in surfaces:
        path = root / relative
        if not path.is_file():
            findings.append(f"Missing state surface: {relative.as_posix()}")
            continue
        text = _read_text(path)
        for label, pattern in patterns:
            if not pattern.search(text):
                findings.append(f"{relative.as_posix()}: missing required token {label}")


def audit_repository(root: Path) -> dict[str, Any]:
    root = root.resolve()
    findings: list[str] = []
    state: dict[str, Any] = {}
    try:
        state = json.loads(_read_text(root / STATE_PATH))
        findings.extend(validate_current_state_data(state))
    except FileNotFoundError:
        findings.append(f"Missing state authority: {STATE_PATH.as_posix()}")
    except json.JSONDecodeError as exc:
        findings.append(f"{STATE_PATH.as_posix()}: invalid JSON: {exc}")

    for relative in LEGACY_ENGINE_JSON_STATE_SURFACES:
        path = root / relative
        if not path.is_file():
            findings.append(f"Missing legacy engine state surface: {relative.as_posix()}")
            continue
        try:
            findings.extend(_validate_legacy_engine_json_surface(relative, json.loads(_read_text(path))))
        except json.JSONDecodeError as exc:
            findings.append(f"{relative.as_posix()}: invalid JSON: {exc}")

    engine_manifest: dict[str, Any] = {}
    try:
        engine_manifest = json.loads(_read_text(root / ENGINE_TREE_MANIFEST_PATH))
    except FileNotFoundError:
        findings.append(f"Missing engine tree manifest: {ENGINE_TREE_MANIFEST_PATH.as_posix()}")
    except json.JSONDecodeError as exc:
        findings.append(f"{ENGINE_TREE_MANIFEST_PATH.as_posix()}: invalid JSON: {exc}")
    engine_change = state.get("engine_change_control", {})
    if isinstance(engine_change, dict) and engine_manifest:
        if any((engine_change.get("current_engine_tree_sha256") != engine_manifest.get("tree_sha256"), engine_change.get("current_engine_file_count") != engine_manifest.get("file_count"), engine_change.get("current_engine_byte_count") != engine_manifest.get("byte_count"))):
            findings.append("governance/CURRENT_STATE.json: engine_change_control does not match canonical engine tree manifest")

    _require_text_tokens(root, ROOT_TEXT_STATE_SURFACES, (
        ("M02_RESULT=NOT_RECOMPUTED_POST_AUD035", re.compile(r"M02_(?:RESULT)?[\"\s]*[:=]\s*NOT_RECOMPUTED_POST_AUD035", re.IGNORECASE)),
        ("M03_RESULT=NOT_RECOMPUTED_POST_AUD035", re.compile(r"M03_(?:RESULT)?[\"\s]*[:=]\s*NOT_RECOMPUTED_POST_AUD035", re.IGNORECASE)),
        ("EN_REVISION", re.compile(r"EN_REVISION")),
        ("READY_FOR_PROJECT_DEMO_GENERATION=false", re.compile(r"ready_for_project_demo_generation[\"\s]*[:=]\s*false", re.IGNORECASE)),
        ("CREATIVE_OUTPUT_CERTIFIED=false", re.compile(r"creative_output_certified[\"\s]*[:=]\s*false", re.IGNORECASE)),
    ), findings)
    _require_text_tokens(root, LEGACY_ENGINE_TEXT_STATE_SURFACES, (
        ("derived M02 not recomputed", re.compile(r"M02_(?:RESULT)?[\"\s]*[:=]\s*NOT_RECOMPUTED_POST_AUD035", re.IGNORECASE)),
        ("derived M03 not recomputed", re.compile(r"M03_(?:RESULT)?[\"\s]*[:=]\s*NOT_RECOMPUTED_POST_AUD035", re.IGNORECASE)),
        ("EN_REVISION", re.compile(r"EN_REVISION")),
    ), findings)

    contract_path = root / "engine/IDUNEX/07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json"
    try:
        contract = json.loads(_read_text(contract_path))
        expected_contract = {
            "MOTOR_STATUS": state.get("motor_status"),
            "M02_RESULT": state.get("m02_result"),
            "M03_RESULT": state.get("m03_result"),
            "READY_FOR_PROJECT_DEMO_GENERATION": state.get("ready_for_project_demo_generation"),
            "RELEASE_AUTHORIZED": state.get("release_authorized"),
            "PRODUCTIVE_CLOSURE_AUTHORIZED": state.get("productive_closure_authorized"),
            "TAG_AUTHORIZED": state.get("tag_authorized"),
            "OFICIAL_AUTHORIZED": state.get("oficial_authorized"),
            "AGENT_LOAD_AUTHORIZED": state.get("agent_load_authorized"),
            "CREATIVE_OUTPUT_CERTIFIED": state.get("creative_output_certified"),
        }
        if contract.get("state_authority") != "governance/CURRENT_STATE.json" or contract.get("expected_current_state") != expected_contract or contract.get("last_sync_issue") != "AUD-035":
            findings.append("MASTER_GOVERNANCE_VALIDATION_CONTRACT out of sync with CURRENT_STATE")
    except (FileNotFoundError, json.JSONDecodeError):
        findings.append("MASTER_GOVERNANCE_VALIDATION_CONTRACT missing or unreadable")

    contradiction_findings, historical_matches = scan_contradictions(root)
    findings.extend(contradiction_findings)
    controlled = state.get("controlled_external_demo_execution", {})
    return {
        "result": "CONSISTENT" if not findings else "INCONSISTENT",
        "scope": "AUD-035_internal_governance_surface_sync",
        "motor_status": state.get("motor_status"),
        "m02_result": state.get("m02_result"),
        "m03_result": state.get("m03_result"),
        "ready_for_project_demo_generation": state.get("ready_for_project_demo_generation"),
        "release_authorized": state.get("release_authorized"),
        "tag_authorized": state.get("tag_authorized"),
        "productive_closure_authorized": state.get("productive_closure_authorized"),
        "creative_output_certified": state.get("creative_output_certified"),
        "controlled_external_demo_status": controlled.get("status"),
        "controlled_external_demo_authorized": controlled.get("authorized"),
        "controlled_external_demo_consumed": controlled.get("consumed"),
        "current_engine_tree_sha256": engine_change.get("current_engine_tree_sha256") if isinstance(engine_change, dict) else None,
        "active_contradiction_count": len(contradiction_findings),
        "historical_reference_match_count": historical_matches,
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
