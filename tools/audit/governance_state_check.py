#!/usr/bin/env python3
"""AUD-037 mutable-governance and immutable-engine boundary check.

This existing repository check validates the sole external state authority,
evidence-to-tree binding, immutable interlocks, and non-authoritative internal
build snapshots. It does not execute M02, M03, Demo, refresh, or agent loading.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


STATE_PATH = Path("governance/CURRENT_STATE.json")
ENGINE_TREE_MANIFEST_PATH = Path("governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json")
MASTER_CONTRACT_PATH = Path(
    "engine/IDUNEX/07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/"
    "MASTER_GOVERNANCE_VALIDATION_CONTRACT.json"
)
STATE_AUTHORITY = STATE_PATH.as_posix()
BUILD_STATE_SNAPSHOT_CLASSIFICATION = "NON_AUTHORITY_BUILD_SNAPSHOT"
M02_RECOMPUTATION_STATE = "NOT_RECOMPUTED_POST_AUD037"
M03_RECOMPUTATION_STATE = "NOT_RECOMPUTED_POST_AUD037"
CURRENT_ENGINE_TREE_SHA256 = "b516c1f08682aba94ebb771578d727361ab71b406406d30fc442f27458b1fda4"
CURRENT_ENGINE_FILE_COUNT = 981
CURRENT_ENGINE_BYTE_COUNT = 47_350_130
AUD037_BASE_COMMIT = "f9a2b84415ef53a8602911e39835617575ff3864"
PREVIOUS_ENGINE_TREE_SHA256 = "c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e"
PREVIOUS_ENGINE_BYTE_COUNT = 47_324_981
M02_EVIDENCE_ENGINE_TREE_SHA256 = PREVIOUS_ENGINE_TREE_SHA256

M02_RECOMPUTATION_EVIDENCE = {
    "run_id": 30194513740,
    "job_id": 89773509632,
    "artifact_id": 8629888949,
    "artifact_name": "idunex-m02-max-30194513740-attempt-1",
    "artifact_sha256": "797d705d9e75317f0cb8dacebcee22e1376369bfadae05ad453943988ad14dde",
    "repository_commit": "f9a2b84415ef53a8602911e39835617575ff3864",
    "engine_tree_sha256": PREVIOUS_ENGINE_TREE_SHA256,
    "engine_file_count": 981,
    "engine_byte_count": PREVIOUS_ENGINE_BYTE_COUNT,
    "technical_result": "PASS",
    "matrix": "30/30",
    "mutation": "506/506",
    "score": "10/10",
    "m02_decision": "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY",
    "scoped_classification": "VALIDATED_SCOPED_EVIDENCE_FOR_C5CB2F4B_NOT_GOVERNANCE_AUTHORITY",
    "evidence_class": "REFERENCIA_SUSTITUIDA",
    "current_tree_applicability": False,
    "superseded_by": "AUD-037",
    "creative_output_certified": False,
}

ROOT_TEXT_STATE_SURFACES = (
    Path("README.md"),
    Path("GOVERNANCE_STATUS.md"),
    Path("REPOSITORY_MANIFEST.yml"),
)
INTERNAL_TEXT_STATE_SURFACES = (
    Path("engine/IDUNEX/00_INDEX/ACTIVE_VERSION.txt"),
    Path("engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/ACTIVE_VERSION.md"),
    Path("engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/STATUS.md"),
    Path("engine/IDUNEX/00_INDEX/RELEASE_CERTIFICATE.txt"),
    Path("engine/IDUNEX/00_INDEX/CHANGELOG.md"),
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
ISSUE_RE = re.compile(r"^AUD-[0-9]{3}$")
M02_RE = re.compile(r"^(?:NOT_RECOMPUTED(?:_POST_AUD[0-9]{3})?|M02_PASS)$")
M03_RE = re.compile(r"^(?:NOT_RECOMPUTED(?:_POST_AUD[0-9]{3})?|M03_PASS)$")
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


def physical_identity(root: Path) -> dict[str, Any]:
    rows: list[tuple[str, int, str]] = []
    engine = root / "engine/IDUNEX"
    for path in engine.rglob("*"):
        if path.is_file():
            data = path.read_bytes()
            rows.append((path.relative_to(root).as_posix(), len(data), hashlib.sha256(data).hexdigest()))
    rows.sort()
    aggregate = hashlib.sha256()
    for relative, size, digest in rows:
        aggregate.update(f"{relative}\0{size}\0{digest}\n".encode("utf-8"))
    return {
        "file_count": len(rows),
        "byte_count": sum(row[1] for row in rows),
        "tree_sha256": aggregate.hexdigest(),
    }


def _validate_evidence(phase: str, evidence: Any, identity: dict[str, Any]) -> list[str]:
    prefix = phase.lower()
    if not isinstance(evidence, dict):
        return [f"{STATE_AUTHORITY}: {prefix}_evidence must be an object"]
    findings: list[str] = []
    for field in ("run_id", "job_id", "artifact_id"):
        value = evidence.get(field)
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            findings.append(f"{STATE_AUTHORITY}: {prefix}_evidence.{field} must be a positive integer")
    if not isinstance(evidence.get("artifact_name"), str) or not evidence["artifact_name"].strip():
        findings.append(f"{STATE_AUTHORITY}: {prefix}_evidence.artifact_name must be present")
    if not isinstance(evidence.get("artifact_sha256"), str) or not SHA256_RE.fullmatch(evidence["artifact_sha256"]):
        findings.append(f"{STATE_AUTHORITY}: {prefix}_evidence.artifact_sha256 must be a lowercase SHA-256")
    if not isinstance(evidence.get("repository_commit"), str) or not GIT_SHA_RE.fullmatch(evidence["repository_commit"]):
        findings.append(f"{STATE_AUTHORITY}: {prefix}_evidence.repository_commit must be a lowercase Git SHA")
    for evidence_field, identity_field in (
        ("engine_tree_sha256", "tree_sha256"),
        ("engine_file_count", "file_count"),
        ("engine_byte_count", "byte_count"),
    ):
        if evidence.get(evidence_field) != identity[identity_field]:
            findings.append(
                f"{STATE_AUTHORITY}: {prefix}_evidence.{evidence_field} must match physical engine {identity_field}"
            )
    return findings


def validate_controlled_external_demo_execution(data: Any) -> list[str]:
    if not isinstance(data, dict):
        return [f"{STATE_AUTHORITY}: controlled_external_demo_execution must be an object"]
    findings: list[str] = []
    expected = {
        "schema_version": 1,
        "status": "CONSUMED",
        "authorized": False,
        "consumed": True,
        "execution_limit": 1,
        "execution_count": 1,
        "generate_executions_allowed": 0,
        "validate_executions_allowed": 0,
        "general_project_generation_enabled": False,
        "authorization_id": "AUD-028",
        "project_agent_load_pass": False,
        "project_ready_for_production": False,
        "allows_release": False,
        "allows_tag": False,
        "allows_oficial": False,
        "allows_productive_closure": False,
        "allows_agent_load": False,
        "creative_output_certified": False,
    }
    for field, value in expected.items():
        if data.get(field) != value:
            findings.append(
                f"{STATE_AUTHORITY}: controlled_external_demo_execution.{field} must be {value!r}, got {data.get(field)!r}"
            )
    return findings


def validate_current_state_data(data: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    if data.get("authority") != STATE_AUTHORITY:
        findings.append(f"{STATE_AUTHORITY}: authority must be {STATE_AUTHORITY!r}")
    issue = data.get("issue")
    if not isinstance(issue, str) or not ISSUE_RE.fullmatch(issue):
        findings.append(f"{STATE_AUTHORITY}: issue token is invalid")
    if data.get("motor_status") not in {"EN_REVISION", "OFICIAL"}:
        findings.append(f"{STATE_AUTHORITY}: motor_status is invalid")
    m02_result = data.get("m02_result")
    m03_result = data.get("m03_result")
    if not isinstance(m02_result, str) or not M02_RE.fullmatch(m02_result):
        findings.append(f"{STATE_AUTHORITY}: m02_result is outside the stable schema")
    if not isinstance(m03_result, str) or not M03_RE.fullmatch(m03_result):
        findings.append(f"{STATE_AUTHORITY}: m03_result is outside the stable schema")
    if isinstance(issue, str) and ISSUE_RE.fullmatch(issue):
        suffix = issue.replace("-", "")
        if isinstance(m02_result, str) and m02_result.startswith("NOT_RECOMPUTED_POST_") and m02_result != f"NOT_RECOMPUTED_POST_{suffix}":
            findings.append(f"{STATE_AUTHORITY}: m02_result must bind the current issue")
        if isinstance(m03_result, str) and m03_result.startswith("NOT_RECOMPUTED_POST_") and m03_result != f"NOT_RECOMPUTED_POST_{suffix}":
            findings.append(f"{STATE_AUTHORITY}: m03_result must bind the current issue")

    identity = {
        "tree_sha256": CURRENT_ENGINE_TREE_SHA256,
        "file_count": CURRENT_ENGINE_FILE_COUNT,
        "byte_count": CURRENT_ENGINE_BYTE_COUNT,
    }
    if m02_result == "M02_PASS":
        findings.extend(_validate_evidence("M02", data.get("m02_evidence"), identity))
    if m03_result == "M03_PASS":
        if m02_result != "M02_PASS":
            findings.append(f"{STATE_AUTHORITY}: M03_PASS requires exact M02_PASS")
        findings.extend(_validate_evidence("M03", data.get("m03_evidence"), identity))
        m02_evidence = data.get("m02_evidence")
        m03_evidence = data.get("m03_evidence")
        if isinstance(m02_evidence, dict) and isinstance(m03_evidence, dict):
            if any(m02_evidence.get(field) != m03_evidence.get(field) for field in ("engine_tree_sha256", "engine_file_count", "engine_byte_count")):
                findings.append(f"{STATE_AUTHORITY}: M02 and M03 evidence must bind the same engine tree")

    if data.get("motor_status") == "EN_REVISION":
        for field in (
            "ready_for_project_demo_generation",
            "release_authorized",
            "tag_authorized",
            "productive_closure_authorized",
            "oficial_authorized",
            "agent_load_authorized",
            "creative_output_certified",
        ):
            if data.get(field) is not False:
                findings.append(f"{STATE_AUTHORITY}: {field} must remain false while EN_REVISION")
    if data.get("creative_output_certified") is not False:
        findings.append(f"{STATE_AUTHORITY}: creative_output_certified must remain false")

    findings.extend(validate_controlled_external_demo_execution(data.get("controlled_external_demo_execution")))
    engine_change = data.get("engine_change_control")
    engine_expected = {
        "issue": "AUD-037",
        "base_commit": AUD037_BASE_COMMIT,
        "previous_engine_tree_sha256": PREVIOUS_ENGINE_TREE_SHA256,
        "previous_engine_byte_count": PREVIOUS_ENGINE_BYTE_COUNT,
        "previous_engine_tree_classification": "AUD035_TREE_SUPERSEDED_BY_AUD037_GOVERNANCE_IDENTITY_CYCLE_BREAK",
        "current_engine_tree_sha256": CURRENT_ENGINE_TREE_SHA256,
        "current_engine_file_count": CURRENT_ENGINE_FILE_COUNT,
        "current_engine_byte_count": CURRENT_ENGINE_BYTE_COUNT,
        "manifests_recomputed_with_canonical_scanner": True,
        "build_state_snapshot_authority": False,
        "build_state_snapshot_classification": BUILD_STATE_SNAPSHOT_CLASSIFICATION,
        "build_state_snapshot": {
            "m02_result": M02_RECOMPUTATION_STATE,
            "m03_result": M03_RECOMPUTATION_STATE,
        },
    }
    if not isinstance(engine_change, dict):
        findings.append(f"{STATE_AUTHORITY}: engine_change_control must be an object")
    else:
        for field, expected in engine_expected.items():
            if engine_change.get(field) != expected:
                findings.append(f"{STATE_AUTHORITY}: engine_change_control.{field} must be {expected!r}")

    prior = data.get("prior_m02_recomputation_evidence")
    if not isinstance(prior, dict):
        findings.append(f"{STATE_AUTHORITY}: prior_m02_recomputation_evidence must be an object")
    else:
        for field, expected in M02_RECOMPUTATION_EVIDENCE.items():
            if prior.get(field) != expected:
                findings.append(f"{STATE_AUTHORITY}: prior_m02_recomputation_evidence.{field} must be {expected!r}")
        if prior.get("engine_tree_sha256") == CURRENT_ENGINE_TREE_SHA256 or prior.get("current_tree_applicability") is not False:
            findings.append(f"{STATE_AUTHORITY}: superseded M02 evidence must not apply to the AUD-037 tree")
    return findings


def validate_master_contract(contract: Any) -> list[str]:
    if not isinstance(contract, dict):
        return [f"{MASTER_CONTRACT_PATH.as_posix()}: must be an object"]
    findings: list[str] = []
    if "expected_current_state" in contract:
        findings.append(f"{MASTER_CONTRACT_PATH.as_posix()}: audit-specific exact state equality is forbidden")
    expected = {
        "state_authority": STATE_AUTHORITY,
        "build_state_snapshot_authority": False,
        "build_state_snapshot_classification": BUILD_STATE_SNAPSHOT_CLASSIFICATION,
        "M02_before_M03": True,
        "same_tree_evidence_requirement": True,
        "creative_output_false_interlock": True,
    }
    for field, value in expected.items():
        if contract.get(field) != value:
            findings.append(f"{MASTER_CONTRACT_PATH.as_posix()}: {field} must be {value!r}")
    rules = contract.get("state_transition_rules", {})
    if not isinstance(rules, dict) or rules.get("state_changes_do_not_require_engine_changes") is not True:
        findings.append(f"{MASTER_CONTRACT_PATH.as_posix()}: stable state_transition_rules are missing")
    if re.search(r"AUD-?[0-9]{3}", json.dumps(rules, sort_keys=True)):
        findings.append(f"{MASTER_CONTRACT_PATH.as_posix()}: future transitions cannot be pinned to one audit")
    return findings


def scan_contradictions(root: Path) -> tuple[list[str], int]:
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
        has_fail_closed = bool(
            re.search(r"READY_FOR_PROJECT_DEMO_GENERATION[\"\s]*[:=]\s*(?:FALSE|false)", text)
            or re.search(r'"ready_for_project_demo_generation"\s*:\s*false', text)
        )
        has_non_authority_snapshot = bool(
            re.search(r"BUILD_STATE_SNAPSHOT_AUTHORITY[\"\s]*[:=]\s*(?:FALSE|false)", text)
            or re.search(r'"build_state_snapshot_authority"\s*:\s*false', text)
        )
        if marked_reference and (has_fail_closed or has_non_authority_snapshot):
            historical_matches += len(matches)
        else:
            findings.append(
                f"{relative.as_posix()}: active or unclassified contradictory state token(s): "
                + ", ".join(matches)
            )
    return findings, historical_matches


def _require_tokens(root: Path, surfaces: tuple[Path, ...], tokens: tuple[str, ...]) -> list[str]:
    findings: list[str] = []
    for relative in surfaces:
        path = root / relative
        if not path.is_file():
            findings.append(f"Missing state surface: {relative.as_posix()}")
            continue
        text = _read_text(path)
        for token in tokens:
            if token not in text:
                findings.append(f"{relative.as_posix()}: missing required token {token}")
    return findings


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

    baseline: dict[str, Any] = {}
    try:
        baseline = json.loads(_read_text(root / ENGINE_TREE_MANIFEST_PATH))
    except (FileNotFoundError, json.JSONDecodeError):
        findings.append(f"{ENGINE_TREE_MANIFEST_PATH.as_posix()}: missing or unreadable")
    identity = physical_identity(root)
    expected_identity = {
        "file_count": CURRENT_ENGINE_FILE_COUNT,
        "byte_count": CURRENT_ENGINE_BYTE_COUNT,
        "tree_sha256": CURRENT_ENGINE_TREE_SHA256,
    }
    if identity != expected_identity:
        findings.append("engine/IDUNEX: physical identity does not match AUD-037 constants")
    if {field: baseline.get(field) for field in expected_identity} != expected_identity:
        findings.append(f"{ENGINE_TREE_MANIFEST_PATH.as_posix()}: identity mismatch")
    engine_change = state.get("engine_change_control", {})
    if isinstance(engine_change, dict) and (
        engine_change.get("current_engine_tree_sha256") != identity["tree_sha256"]
        or engine_change.get("current_engine_file_count") != identity["file_count"]
        or engine_change.get("current_engine_byte_count") != identity["byte_count"]
    ):
        findings.append(f"{STATE_AUTHORITY}: engine_change_control does not match the physical tree")

    try:
        findings.extend(validate_master_contract(json.loads(_read_text(root / MASTER_CONTRACT_PATH))))
    except (FileNotFoundError, json.JSONDecodeError):
        findings.append(f"{MASTER_CONTRACT_PATH.as_posix()}: missing or unreadable")

    findings.extend(_require_tokens(root, ROOT_TEXT_STATE_SURFACES, (
        "STATE_AUTHORITY=governance/CURRENT_STATE.json",
        "READY_FOR_PROJECT_DEMO_GENERATION=FALSE",
        "CREATIVE_OUTPUT_CERTIFIED=FALSE",
    )))
    findings.extend(_require_tokens(root, INTERNAL_TEXT_STATE_SURFACES, (
        "STATE_AUTHORITY=governance/CURRENT_STATE.json",
        "BUILD_STATE_SNAPSHOT_AUTHORITY=FALSE",
        "BUILD_STATE_SNAPSHOT_CLASSIFICATION=NON_AUTHORITY_BUILD_SNAPSHOT",
    )))

    contradiction_findings, historical_matches = scan_contradictions(root)
    findings.extend(contradiction_findings)
    controlled = state.get("controlled_external_demo_execution", {})
    return {
        "result": "CONSISTENT" if not findings else "INCONSISTENT",
        "scope": "AUD-037_governance_identity_cycle_break",
        "motor_status": state.get("motor_status"),
        "m02_result": state.get("m02_result"),
        "m03_result": state.get("m03_result"),
        "current_engine_identity": identity,
        "ready_for_project_demo_generation": state.get("ready_for_project_demo_generation"),
        "release_authorized": state.get("release_authorized"),
        "tag_authorized": state.get("tag_authorized"),
        "productive_closure_authorized": state.get("productive_closure_authorized"),
        "creative_output_certified": state.get("creative_output_certified"),
        "controlled_external_demo_status": controlled.get("status") if isinstance(controlled, dict) else None,
        "controlled_external_demo_authorized": controlled.get("authorized") if isinstance(controlled, dict) else None,
        "historical_contradictory_tokens_classified": historical_matches,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    report = audit_repository(Path(args.repo_root))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["result"] == "CONSISTENT" else 1


if __name__ == "__main__":
    sys.exit(main())
