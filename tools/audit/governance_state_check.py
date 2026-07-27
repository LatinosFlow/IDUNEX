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
from pathlib import Path, PurePosixPath, PureWindowsPath
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
CURRENT_ENGINE_TREE_SHA256 = "87c0e9e681a3a4995d4f096eaaa73cd5c7a889e9c10a5f0f4b3c9897e80c2346"
CURRENT_ENGINE_FILE_COUNT = 981
CURRENT_ENGINE_BYTE_COUNT = 47_370_003
AUD037_BASE_COMMIT = "f9a2b84415ef53a8602911e39835617575ff3864"
PREVIOUS_ENGINE_TREE_SHA256 = "ff6a3a6d376206bd052d124031a72ca55c90827f5f69e3d3c851033128028ea3"
PREVIOUS_ENGINE_BYTE_COUNT = 47_361_805
M02_EVIDENCE_ENGINE_TREE_SHA256 = "c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e"
M02_EVIDENCE_ENGINE_BYTE_COUNT = 47_324_981

M02_RECOMPUTATION_EVIDENCE = {
    "run_id": 30194513740,
    "job_id": 89773509632,
    "artifact_id": 8629888949,
    "artifact_name": "idunex-m02-max-30194513740-attempt-1",
    "artifact_sha256": "797d705d9e75317f0cb8dacebcee22e1376369bfadae05ad453943988ad14dde",
    "repository_commit": "f9a2b84415ef53a8602911e39835617575ff3864",
    "engine_tree_sha256": M02_EVIDENCE_ENGINE_TREE_SHA256,
    "engine_file_count": 981,
    "engine_byte_count": M02_EVIDENCE_ENGINE_BYTE_COUNT,
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
M02_RE = re.compile(r"^(?:NOT_RECOMPUTED_POST_AUD[0-9]{3}|M02_PASS)$")
M03_RE = re.compile(r"^(?:NOT_RECOMPUTED_POST_AUD[0-9]{3}|M03_PASS)$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
FORMALIZED_EVIDENCE_VALUES = {
    "technical_result": "PASS",
    "independent_audit_result": "VALIDADO_PASS",
    "evidence_class": "VALIDATED_CURRENT_TREE_EVIDENCE",
    "governance_formalization_status": "VALIDADO",
    "workflow_decision": "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY",
}
OFFICIAL_GATE_RESULTS = {
    "motor_audit": {"PASS"},
    "project_demo_generation": {"PASS"},
    "project_demo_audit": {"PASS"},
    "chatgpt_runtime": {"PASS"},
    "copilot_runtime": {"PASS", "VENDOR_LIMITATION_NOT_ENGINE_FAIL"},
    "agent_runtime_audit": {"PASS"},
    "productive_formalization": {"VALIDADO"},
}
OFFICIAL_GATE_FAIL_CODES = {
    "motor_audit": "FAIL_OFFICIAL_MOTOR_AUDIT_REQUIRED",
    "project_demo_generation": "FAIL_OFFICIAL_DEMO_GENERATION_REQUIRED",
    "project_demo_audit": "FAIL_OFFICIAL_DEMO_AUDIT_REQUIRED",
    "chatgpt_runtime": "FAIL_OFFICIAL_CHATGPT_RUNTIME_REQUIRED",
    "copilot_runtime": "FAIL_OFFICIAL_COPILOT_RUNTIME_REQUIRED",
    "agent_runtime_audit": "FAIL_OFFICIAL_AGENT_RUNTIME_AUDIT_REQUIRED",
    "productive_formalization": "FAIL_OFFICIAL_PRODUCTIVE_FORMALIZATION_REQUIRED",
}
OFFICIAL_EVIDENCE_ROOT = "governance/evidence/official/"
OFFICIAL_EVIDENCE_REQUIRED_VALUES = {
    "independent_audit_result": "VALIDADO_PASS",
    "evidence_class": "VALIDATED_EXTERNAL_EVIDENCE",
    "governance_formalization_status": "VALIDADO",
}
OFFICIAL_GATE_REQUIRED_FIELDS = (
    "evidence_id",
    "evidence_path",
    "evidence_sha256",
    "result",
    "independent_audit_result",
    "evidence_class",
    "governance_formalization_status",
    "engine_tree_sha256",
    "engine_file_count",
    "engine_byte_count",
)
OFFICIAL_EVIDENCE_DOCUMENT_REQUIRED_FIELDS = (
    "schema_version",
    "evidence_id",
    "gate_name",
    "result",
    "independent_audit_result",
    "evidence_class",
    "governance_formalization_status",
    "engine_tree_sha256",
    "engine_file_count",
    "engine_byte_count",
)


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
    for field, expected in FORMALIZED_EVIDENCE_VALUES.items():
        if evidence.get(field) != expected:
            findings.append(
                f"{STATE_AUTHORITY}: FAIL_{phase.upper()}_EVIDENCE_{field.upper()} "
                f"{prefix}_evidence.{field} must be {expected!r}"
            )
    if (
        evidence.get("workflow_decision") == "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY"
        and evidence.get("governance_formalization_status") != "VALIDADO"
    ):
        findings.append(
            f"{STATE_AUTHORITY}: FAIL_{phase.upper()}_WORKFLOW_EVIDENCE_NOT_FORMALIZED "
            "workflow evidence is not governance authority without VALIDADO formalization"
        )
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


def _resolve_official_evidence_path(evidence_path: Any, gate_name: str, repo_root: Path) -> tuple[Path | None, list[str]]:
    prefix = f"{STATE_AUTHORITY}: official_transition_evidence.gates.{gate_name}"
    if not isinstance(evidence_path, str) or not evidence_path.strip():
        return None, [f"{prefix} FAIL_OFFICIAL_EVIDENCE_PATH_MISSING"]
    normalized = evidence_path.replace("\\", "/")
    pure_path = PurePosixPath(normalized)
    if pure_path.is_absolute() or PureWindowsPath(evidence_path).is_absolute():
        return None, [f"{prefix} FAIL_OFFICIAL_EVIDENCE_PATH_ABSOLUTE"]
    if ".." in pure_path.parts:
        return None, [f"{prefix} FAIL_OFFICIAL_EVIDENCE_PATH_TRAVERSAL"]
    normalized = pure_path.as_posix()
    if normalized == "engine/IDUNEX" or normalized.startswith("engine/IDUNEX/"):
        return None, [f"{prefix} FAIL_OFFICIAL_EVIDENCE_PATH_ENGINE_FORBIDDEN"]
    if not normalized.startswith(OFFICIAL_EVIDENCE_ROOT):
        return None, [f"{prefix} FAIL_OFFICIAL_EVIDENCE_PATH_OUTSIDE_AUTHORIZED_ROOT"]
    if pure_path.suffix != ".json":
        return None, [f"{prefix} FAIL_OFFICIAL_EVIDENCE_EXTENSION"]
    evidence_root = (repo_root / OFFICIAL_EVIDENCE_ROOT).resolve()
    resolved = (repo_root / Path(*pure_path.parts)).resolve()
    try:
        resolved.relative_to(evidence_root)
    except ValueError:
        return None, [f"{prefix} FAIL_OFFICIAL_EVIDENCE_PATH_OUTSIDE_AUTHORIZED_ROOT"]
    return resolved, []


def _validate_official_evidence_file(
    gate_name: str,
    gate: dict[str, Any],
    identity: dict[str, Any],
    repo_root: Path,
) -> list[str]:
    prefix = f"{STATE_AUTHORITY}: official_transition_evidence.gates.{gate_name}"
    evidence_file, findings = _resolve_official_evidence_path(gate.get("evidence_path"), gate_name, repo_root)
    if evidence_file is None:
        return findings
    if not evidence_file.is_file():
        return findings + [f"{prefix} FAIL_OFFICIAL_EVIDENCE_FILE_MISSING"]
    evidence_bytes = evidence_file.read_bytes()
    evidence_sha256 = gate.get("evidence_sha256")
    if not isinstance(evidence_sha256, str) or not SHA256_RE.fullmatch(evidence_sha256):
        findings.append(f"{prefix} FAIL_OFFICIAL_EVIDENCE_SHA256_INVALID")
    elif hashlib.sha256(evidence_bytes).hexdigest() != evidence_sha256:
        findings.append(f"{prefix} FAIL_OFFICIAL_EVIDENCE_SHA256_MISMATCH")
    try:
        document = json.loads(evidence_bytes.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return findings + [f"{prefix} FAIL_OFFICIAL_EVIDENCE_JSON_INVALID"]
    if not isinstance(document, dict):
        return findings + [f"{prefix} FAIL_OFFICIAL_EVIDENCE_JSON_INVALID"]
    missing_fields = [field for field in OFFICIAL_EVIDENCE_DOCUMENT_REQUIRED_FIELDS if field not in document]
    if missing_fields:
        findings.append(f"{prefix} FAIL_OFFICIAL_EVIDENCE_DOCUMENT_SCHEMA")
    if document.get("schema_version") != 1:
        findings.append(f"{prefix} FAIL_OFFICIAL_EVIDENCE_SCHEMA_VERSION")
    if document.get("evidence_id") != gate.get("evidence_id"):
        findings.append(f"{prefix} FAIL_OFFICIAL_EVIDENCE_ID_MISMATCH")
    if document.get("gate_name") != gate_name:
        findings.append(f"{prefix} FAIL_OFFICIAL_EVIDENCE_GATE_NAME_MISMATCH")
    if document.get("result") != gate.get("result"):
        findings.append(f"{prefix} FAIL_OFFICIAL_EVIDENCE_RESULT_MISMATCH")
    fail_codes = {
        "independent_audit_result": "FAIL_OFFICIAL_EVIDENCE_INDEPENDENT_AUDIT_RESULT",
        "evidence_class": "FAIL_OFFICIAL_EVIDENCE_CLASS",
        "governance_formalization_status": "FAIL_OFFICIAL_EVIDENCE_GOVERNANCE_FORMALIZATION_STATUS",
    }
    for field, expected in OFFICIAL_EVIDENCE_REQUIRED_VALUES.items():
        if document.get(field) != expected or gate.get(field) != expected or document.get(field) != gate.get(field):
            findings.append(f"{prefix} {fail_codes[field]}")
    for field, identity_field, fail_code in (
        ("engine_tree_sha256", "tree_sha256", "FAIL_OFFICIAL_EVIDENCE_ENGINE_TREE_SHA256_MISMATCH"),
        ("engine_file_count", "file_count", "FAIL_OFFICIAL_EVIDENCE_ENGINE_FILE_COUNT_MISMATCH"),
        ("engine_byte_count", "byte_count", "FAIL_OFFICIAL_EVIDENCE_ENGINE_BYTE_COUNT_MISMATCH"),
    ):
        expected = identity[identity_field]
        if gate.get(field) != expected or document.get(field) != expected or document.get(field) != gate.get(field):
            findings.append(f"{prefix} {fail_code}")
    return findings


def _validate_official_transition(
    data: dict[str, Any],
    identity: dict[str, Any],
    repo_root: Path,
) -> list[str]:
    findings: list[str] = []
    if data.get("m02_result") != "M02_PASS":
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_REQUIRES_M02_PASS")
    if data.get("m03_result") != "M03_PASS":
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_REQUIRES_M03_PASS")
    envelope = data.get("official_transition_evidence")
    if not isinstance(envelope, dict):
        return findings + [f"{STATE_AUTHORITY}: FAIL_OFFICIAL_TRANSITION_EVIDENCE_MISSING"]

    allowed_envelope_fields = {
        "schema_version",
        "formalization_status",
        "state_authority",
        "engine_tree_sha256",
        "engine_file_count",
        "engine_byte_count",
        "gates",
    }
    if set(envelope) - allowed_envelope_fields:
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_TRANSITION_AUTHORIZATION_INVALID")
    if envelope.get("schema_version") != 1 or envelope.get("state_authority") != STATE_AUTHORITY:
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_TRANSITION_SCHEMA")
    if envelope.get("formalization_status") != "VALIDADO":
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_PRODUCTIVE_FORMALIZATION_REQUIRED")
    if any(
        envelope.get(field) != identity[identity_field]
        for field, identity_field in (
            ("engine_tree_sha256", "tree_sha256"),
            ("engine_file_count", "file_count"),
            ("engine_byte_count", "byte_count"),
        )
    ):
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_EVIDENCE_CURRENT_TREE_MISMATCH")

    gates = envelope.get("gates") if isinstance(envelope.get("gates"), dict) else {}
    evidence_ids: list[str] = []
    evidence_paths: list[str] = []
    allowed_gate_fields = set(OFFICIAL_GATE_REQUIRED_FIELDS)
    for gate_name, allowed_results in OFFICIAL_GATE_RESULTS.items():
        gate = gates.get(gate_name)
        if not isinstance(gate, dict) or gate.get("result") not in allowed_results:
            findings.append(f"{STATE_AUTHORITY}: {OFFICIAL_GATE_FAIL_CODES[gate_name]}")
            continue
        if set(gate) - allowed_gate_fields:
            findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_TRANSITION_AUTHORIZATION_INVALID")
        evidence_id = gate.get("evidence_id")
        if not isinstance(evidence_id, str) or not evidence_id.strip():
            findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_EVIDENCE_ID_MISSING")
        else:
            evidence_ids.append(evidence_id)
        evidence_path = gate.get("evidence_path")
        if isinstance(evidence_path, str) and evidence_path.strip():
            evidence_paths.append(PurePosixPath(evidence_path.replace("\\", "/")).as_posix())
        findings.extend(_validate_official_evidence_file(gate_name, gate, identity, repo_root))
    if len(evidence_ids) != len(set(evidence_ids)):
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_EVIDENCE_ID_DUPLICATE")
    if len(evidence_paths) != len(set(evidence_paths)):
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_EVIDENCE_PATH_DUPLICATE")
    required_state_flags = {
        "ready_for_project_demo_generation": True,
        "release_authorized": True,
        "tag_authorized": True,
        "productive_closure_authorized": True,
        "oficial_authorized": True,
        "agent_load_authorized": True,
        "creative_output_certified": False,
    }
    for field, expected in required_state_flags.items():
        if data.get(field) is not expected:
            findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_PRODUCTIVE_FORMALIZATION_REQUIRED {field}")
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


def validate_current_state_data(data: dict[str, Any], repo_root: Path | None = None) -> list[str]:
    repo_root = (repo_root or Path(__file__).resolve().parents[2]).resolve()
    findings: list[str] = []
    if data.get("authority") != STATE_AUTHORITY:
        findings.append(f"{STATE_AUTHORITY}: authority must be {STATE_AUTHORITY!r}")
    issue = data.get("issue")
    if not isinstance(issue, str) or not ISSUE_RE.fullmatch(issue):
        findings.append(f"{STATE_AUTHORITY}: issue token is invalid")
    if data.get("motor_status") not in {"EN_REVISION", "OFICIAL"}:
        findings.append(f"{STATE_AUTHORITY}: motor_status is invalid")
    if data.get("creative_output_certified") is not False:
        findings.append(f"{STATE_AUTHORITY}: FAIL_MOTOR_CREATIVE_OUTPUT_CERTIFICATION_FORBIDDEN")
    m02_result = data.get("m02_result")
    m03_result = data.get("m03_result")
    if not isinstance(m02_result, str) or not M02_RE.fullmatch(m02_result):
        findings.append(f"{STATE_AUTHORITY}: FAIL_M02_RESULT_SCHEMA m02_result is outside the stable schema")
    if not isinstance(m03_result, str) or not M03_RE.fullmatch(m03_result):
        findings.append(f"{STATE_AUTHORITY}: FAIL_M03_RESULT_SCHEMA m03_result is outside the stable schema")
    if isinstance(issue, str) and ISSUE_RE.fullmatch(issue):
        suffix = issue.replace("-", "")
        if isinstance(m02_result, str) and m02_result.startswith("NOT_RECOMPUTED") and m02_result != f"NOT_RECOMPUTED_POST_{suffix}":
            findings.append(f"{STATE_AUTHORITY}: FAIL_M02_NOT_RECOMPUTED_ISSUE_BINDING m02_result must bind the current issue")
        if isinstance(m03_result, str) and m03_result.startswith("NOT_RECOMPUTED") and m03_result != f"NOT_RECOMPUTED_POST_{suffix}":
            findings.append(f"{STATE_AUTHORITY}: FAIL_M03_NOT_RECOMPUTED_ISSUE_BINDING m03_result must bind the current issue")

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

    official_evidence = data.get("official_transition_evidence")
    if not isinstance(official_evidence, dict):
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_TRANSITION_EVIDENCE_MISSING")
    elif official_evidence.get("schema_version") != 1:
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_TRANSITION_SCHEMA")
    elif data.get("motor_status") != "OFICIAL" and official_evidence != {
        "schema_version": 1,
        "formalization_status": "NOT_FORMALIZED",
        "gates": {},
    }:
        findings.append(f"{STATE_AUTHORITY}: FAIL_OFFICIAL_TRANSITION_PREMATURE_EVIDENCE")

    if data.get("motor_status") == "OFICIAL":
        findings.extend(_validate_official_transition(data, identity, repo_root))

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
    findings.extend(validate_controlled_external_demo_execution(data.get("controlled_external_demo_execution")))
    engine_change = data.get("engine_change_control")
    engine_expected = {
        "issue": "AUD-037",
        "base_commit": AUD037_BASE_COMMIT,
        "previous_engine_tree_sha256": PREVIOUS_ENGINE_TREE_SHA256,
        "previous_engine_byte_count": PREVIOUS_ENGINE_BYTE_COUNT,
        "previous_engine_tree_classification": "AUD037_INTERMEDIATE_STABLE_SCHEMA_TREE_SUPERSEDED_BY_EXTERNAL_OFFICIAL_EVIDENCE_VERIFIABILITY",
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
    schema = contract.get("mutable_state_schema", {})
    if not (
        isinstance(schema, dict)
        and schema.get("m02_result", {}).get("not_recomputed_pattern") == "^NOT_RECOMPUTED_POST_AUD[0-9]{3}$"
        and schema.get("m02_result", {}).get("pass_token") == "M02_PASS"
        and schema.get("m03_result", {}).get("not_recomputed_pattern") == "^NOT_RECOMPUTED_POST_AUD[0-9]{3}$"
        and schema.get("m03_result", {}).get("pass_token") == "M03_PASS"
    ):
        findings.append(f"{MASTER_CONTRACT_PATH.as_posix()}: FAIL_MASTER_GOVERNANCE_MUTABLE_STATE_SCHEMA")
    evidence_rules = contract.get("evidence_binding_rules", {})
    if not (
        isinstance(evidence_rules, dict)
        and evidence_rules.get("required_formalization_fields") == list(FORMALIZED_EVIDENCE_VALUES)
        and evidence_rules.get("required_formalization_values") == FORMALIZED_EVIDENCE_VALUES
        and evidence_rules.get("workflow_decision_is_not_governance_authority") is True
    ):
        findings.append(f"{MASTER_CONTRACT_PATH.as_posix()}: FAIL_MASTER_GOVERNANCE_EVIDENCE_BINDING_RULES")
    official = contract.get("official_transition_contract", {})
    expected_official_gates = {gate: sorted(results) for gate, results in OFFICIAL_GATE_RESULTS.items()}
    actual_official_gates = (
        {
            gate: sorted(results) if isinstance(results, list) else results
            for gate, results in official.get("required_gates", {}).items()
        }
        if isinstance(official, dict)
        else {}
    )
    if not (
        isinstance(official, dict)
        and official.get("schema_version") == 1
        and official.get("external_evidence_block") == "official_transition_evidence"
        and official.get("external_evidence_root") == OFFICIAL_EVIDENCE_ROOT
        and official.get("external_evidence_extension") == ".json"
        and official.get("state_authority") == STATE_AUTHORITY
        and official.get("formalization_status_required") == "VALIDADO"
        and official.get("required_phase_results") == {"m02_result": "M02_PASS", "m03_result": "M03_PASS"}
        and official.get("authorization_override_allowed") is False
        and official.get("every_gate_must_bind_physical_tree") is True
        and actual_official_gates == expected_official_gates
        and official.get("gate_required_fields") == list(OFFICIAL_GATE_REQUIRED_FIELDS)
        and official.get("external_evidence_document_required_fields") == list(OFFICIAL_EVIDENCE_DOCUMENT_REQUIRED_FIELDS)
        and official.get("external_evidence_required_values") == {
            "schema_version": 1,
            **OFFICIAL_EVIDENCE_REQUIRED_VALUES,
        }
        and official.get("external_evidence_path_rules") == {
            "repository_relative_only": True,
            "traversal_forbidden": True,
            "outside_authorized_root_forbidden": True,
            "engine_paths_forbidden": True,
            "file_must_exist": True,
            "sha256_must_match_file": True,
            "json_content_must_match_gate_link": True,
        }
        and official.get("gate_evidence_ids_must_be_unique") is True
        and official.get("gate_evidence_paths_must_be_unique") is True
        and official.get("required_state_flags") == {
            "ready_for_project_demo_generation": True,
            "release_authorized": True,
            "tag_authorized": True,
            "productive_closure_authorized": True,
            "oficial_authorized": True,
            "agent_load_authorized": True,
            "creative_output_certified": False,
        }
    ):
        findings.append(f"{MASTER_CONTRACT_PATH.as_posix()}: FAIL_MASTER_GOVERNANCE_OFFICIAL_TRANSITION_CONTRACT")
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
        findings.extend(validate_current_state_data(state, root))
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
