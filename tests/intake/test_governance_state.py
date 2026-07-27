from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.governance_state_check import (
    AUD037_BASE_COMMIT,
    BUILD_STATE_SNAPSHOT_CLASSIFICATION,
    CURRENT_ENGINE_BYTE_COUNT,
    CURRENT_ENGINE_FILE_COUNT,
    CURRENT_ENGINE_TREE_SHA256,
    M02_EVIDENCE_ENGINE_TREE_SHA256,
    M02_RECOMPUTATION_EVIDENCE,
    M02_RECOMPUTATION_STATE,
    M03_RECOMPUTATION_STATE,
    PREVIOUS_ENGINE_TREE_SHA256,
    scan_contradictions,
    validate_current_state_data,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = REPO_ROOT / "governance/CURRENT_STATE.json"
CONTRACT_PATH = REPO_ROOT / (
    "engine/IDUNEX/07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/"
    "MASTER_GOVERNANCE_VALIDATION_CONTRACT.json"
)
INTERNAL_STATE_SURFACES = (
    REPO_ROOT / "engine/IDUNEX/00_INDEX/RELEASE_CERTIFICATE.txt",
    REPO_ROOT / "engine/IDUNEX/00_INDEX/CHANGELOG.md",
    REPO_ROOT / "engine/IDUNEX/00_INDEX/ACTIVE_VERSION.txt",
    REPO_ROOT / "engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/ACTIVE_VERSION.md",
    REPO_ROOT / "engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/STATUS.md",
)


def current_state() -> dict:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def current_evidence(seed: int = 1) -> dict:
    return {
        "run_id": seed,
        "job_id": seed + 1,
        "artifact_id": seed + 2,
        "artifact_name": f"synthetic-evidence-{seed}",
        "artifact_sha256": f"{seed % 16:x}" * 64,
        "repository_commit": f"{seed % 16:x}" * 40,
        "engine_tree_sha256": CURRENT_ENGINE_TREE_SHA256,
        "engine_file_count": CURRENT_ENGINE_FILE_COUNT,
        "engine_byte_count": CURRENT_ENGINE_BYTE_COUNT,
        "technical_result": "PASS",
        "independent_audit_result": "VALIDADO_PASS",
        "evidence_class": "VALIDATED_CURRENT_TREE_EVIDENCE",
        "governance_formalization_status": "VALIDADO",
        "workflow_decision": "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY",
    }


def official_state() -> dict:
    state = current_state()
    state["motor_status"] = "OFICIAL"
    state["m02_result"] = "M02_PASS"
    state["m03_result"] = "M03_PASS"
    state["m02_evidence"] = current_evidence(1)
    state["m03_evidence"] = current_evidence(4)
    for field in (
        "ready_for_project_demo_generation",
        "release_authorized",
        "tag_authorized",
        "productive_closure_authorized",
        "oficial_authorized",
        "agent_load_authorized",
        "creative_output_certified",
    ):
        state[field] = True
    gate_results = {
        "motor_audit": "PASS",
        "project_demo_generation": "PASS",
        "project_demo_audit": "PASS",
        "chatgpt_runtime": "PASS",
        "copilot_runtime": "PASS",
        "agent_runtime_audit": "PASS",
        "productive_formalization": "VALIDADO",
    }
    gates = {
        gate: {
            "evidence_id": f"synthetic-{gate}",
            "result": result,
            "engine_tree_sha256": CURRENT_ENGINE_TREE_SHA256,
            "engine_file_count": CURRENT_ENGINE_FILE_COUNT,
            "engine_byte_count": CURRENT_ENGINE_BYTE_COUNT,
        }
        for gate, result in gate_results.items()
    }
    state["official_transition_evidence"] = {
        "schema_version": 1,
        "formalization_status": "VALIDADO",
        "state_authority": "governance/CURRENT_STATE.json",
        "engine_tree_sha256": CURRENT_ENGINE_TREE_SHA256,
        "engine_file_count": CURRENT_ENGINE_FILE_COUNT,
        "engine_byte_count": CURRENT_ENGINE_BYTE_COUNT,
        "gates": gates,
    }
    return state


class GovernanceStateTest(unittest.TestCase):
    def test_01_current_aud037_state_passes_checker(self):
        result = subprocess.run(
            [sys.executable, "-B", "tools/audit/governance_state_check.py", "--repo-root", "."],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["result"], "CONSISTENT")
        self.assertEqual(report["m02_result"], M02_RECOMPUTATION_STATE)
        self.assertEqual(report["m03_result"], M03_RECOMPUTATION_STATE)

    def test_02_exact_m02_pass_with_current_tree_evidence_is_valid(self):
        state = current_state()
        state["m02_result"] = "M02_PASS"
        state["m02_evidence"] = current_evidence()
        self.assertEqual(validate_current_state_data(state), [])

    def test_03_pass_substrings_are_not_accepted(self):
        for token in ("PASS", "M02_PASS_UNVERIFIED", "SOMETHING_PASS", "M02_PASS_RECOMPUTED_POST_AUD037"):
            state = current_state()
            state["m02_result"] = token
            with self.subTest(token=token):
                self.assertTrue(any("m02_result" in finding for finding in validate_current_state_data(state)))

    def test_03a_bare_and_cross_issue_not_recomputed_tokens_are_rejected_per_phase(self):
        cases = (
            ("m02_result", "NOT_RECOMPUTED", "FAIL_M02_RESULT_SCHEMA"),
            ("m03_result", "NOT_RECOMPUTED", "FAIL_M03_RESULT_SCHEMA"),
            ("m02_result", "NOT_RECOMPUTED_POST_AUD036", "FAIL_M02_NOT_RECOMPUTED_ISSUE_BINDING"),
            ("m03_result", "NOT_RECOMPUTED_POST_AUD036", "FAIL_M03_NOT_RECOMPUTED_ISSUE_BINDING"),
        )
        for field, token, failcode in cases:
            state = current_state()
            state[field] = token
            with self.subTest(field=field, token=token):
                self.assertTrue(any(failcode in finding for finding in validate_current_state_data(state)))

    def test_04_m03_pass_requires_m02_pass_and_same_tree_evidence(self):
        state = current_state()
        state["m03_result"] = "M03_PASS"
        state["m03_evidence"] = current_evidence(4)
        self.assertTrue(any("requires exact M02_PASS" in finding for finding in validate_current_state_data(state)))
        state["m02_result"] = "M02_PASS"
        state["m02_evidence"] = current_evidence(1)
        self.assertEqual(validate_current_state_data(state), [])

    def test_05_m02_evidence_identity_mutations_are_rejected(self):
        cases = {
            "engine_tree_sha256": "0" * 64,
            "engine_file_count": 1,
            "engine_byte_count": 1,
            "artifact_id": None,
        }
        for field, value in cases.items():
            state = current_state()
            state["m02_result"] = "M02_PASS"
            state["m02_evidence"] = current_evidence()
            state["m02_evidence"][field] = value
            with self.subTest(field=field):
                self.assertTrue(any(field in finding for finding in validate_current_state_data(state)))

    def test_05a_m02_and_m03_pass_evidence_require_explicit_formalization(self):
        for phase in ("m02", "m03"):
            state = current_state()
            state["m02_result"] = "M02_PASS"
            state["m02_evidence"] = current_evidence(1)
            if phase == "m03":
                state["m03_result"] = "M03_PASS"
                state["m03_evidence"] = current_evidence(4)
            state[f"{phase}_evidence"].pop("governance_formalization_status")
            with self.subTest(phase=phase):
                self.assertTrue(
                    any(
                        f"FAIL_{phase.upper()}_EVIDENCE_GOVERNANCE_FORMALIZATION_STATUS" in finding
                        for finding in validate_current_state_data(state)
                    )
                )

    def test_05b_complete_official_transition_is_valid_and_each_gate_is_independent(self):
        state = official_state()
        self.assertEqual(validate_current_state_data(state), [])
        state["official_transition_evidence"]["gates"]["chatgpt_runtime"]["evidence_id"] = (
            state["official_transition_evidence"]["gates"]["motor_audit"]["evidence_id"]
        )
        self.assertTrue(
            any("FAIL_OFFICIAL_EVIDENCE_LAYER_INDEPENDENCE" in finding for finding in validate_current_state_data(state))
        )

    def test_06_aud028_cannot_be_reauthorized_or_recounted(self):
        for field, value in (
            ("status", "AUTHORIZED_NOT_CONSUMED"),
            ("authorized", True),
            ("consumed", False),
            ("generate_executions_allowed", 1),
            ("validate_executions_allowed", 1),
        ):
            state = current_state()
            state["controlled_external_demo_execution"][field] = value
            with self.subTest(field=field):
                self.assertTrue(any(field in finding for finding in validate_current_state_data(state)))

    def test_07_en_revision_interlocks_remain_false(self):
        for field in (
            "ready_for_project_demo_generation",
            "release_authorized",
            "tag_authorized",
            "productive_closure_authorized",
            "oficial_authorized",
            "agent_load_authorized",
            "creative_output_certified",
        ):
            state = current_state()
            state[field] = True
            with self.subTest(field=field):
                self.assertTrue(any(field in finding for finding in validate_current_state_data(state)))

    def test_08_superseded_m02_evidence_is_exact_and_not_rebound(self):
        state = current_state()
        evidence = state["prior_m02_recomputation_evidence"]
        self.assertEqual(evidence, M02_RECOMPUTATION_EVIDENCE)
        self.assertEqual(evidence["engine_tree_sha256"], M02_EVIDENCE_ENGINE_TREE_SHA256)
        self.assertEqual(evidence["engine_byte_count"], 47_324_981)
        self.assertEqual(evidence["evidence_class"], "REFERENCIA_SUSTITUIDA")
        self.assertFalse(evidence["current_tree_applicability"])
        self.assertEqual(evidence["superseded_by"], "AUD-037")
        self.assertNotEqual(evidence["engine_tree_sha256"], CURRENT_ENGINE_TREE_SHA256)

    def test_09_aud037_engine_change_control_is_exact(self):
        control = current_state()["engine_change_control"]
        self.assertEqual(control["base_commit"], AUD037_BASE_COMMIT)
        self.assertEqual(control["previous_engine_tree_sha256"], PREVIOUS_ENGINE_TREE_SHA256)
        self.assertEqual(control["previous_engine_byte_count"], 47_350_130)
        self.assertEqual(control["current_engine_tree_sha256"], CURRENT_ENGINE_TREE_SHA256)
        self.assertEqual(control["current_engine_file_count"], CURRENT_ENGINE_FILE_COUNT)
        self.assertEqual(control["current_engine_byte_count"], CURRENT_ENGINE_BYTE_COUNT)
        self.assertFalse(control["build_state_snapshot_authority"])
        self.assertEqual(control["build_state_snapshot_classification"], BUILD_STATE_SNAPSHOT_CLASSIFICATION)

    def test_10_master_contract_has_no_exact_current_state_equality(self):
        contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        self.assertNotIn("expected_current_state", contract)
        self.assertEqual(contract["state_authority"], "governance/CURRENT_STATE.json")
        self.assertFalse(contract["build_state_snapshot_authority"])
        self.assertTrue(contract["M02_before_M03"])
        self.assertTrue(contract["same_tree_evidence_requirement"])
        self.assertTrue(contract["creative_output_false_interlock"])
        self.assertEqual(
            contract["mutable_state_schema"]["m02_result"]["not_recomputed_pattern"],
            "^NOT_RECOMPUTED_POST_AUD[0-9]{3}$",
        )
        self.assertEqual(
            contract["mutable_state_schema"]["m03_result"]["not_recomputed_pattern"],
            "^NOT_RECOMPUTED_POST_AUD[0-9]{3}$",
        )
        self.assertEqual(contract["official_transition_contract"]["external_evidence_block"], "official_transition_evidence")

    def test_11_internal_surfaces_are_non_authority_snapshots(self):
        for surface in INTERNAL_STATE_SURFACES:
            text = surface.read_text(encoding="utf-8", errors="replace")
            with self.subTest(surface=surface.name):
                self.assertIn("STATE_AUTHORITY=governance/CURRENT_STATE.json", text)
                self.assertIn("BUILD_STATE_SNAPSHOT_AUTHORITY=FALSE", text)
                self.assertIn("BUILD_STATE_SNAPSHOT_CLASSIFICATION=NON_AUTHORITY_BUILD_SNAPSHOT", text)
                self.assertNotRegex(text, r"(?m)^(?:CURRENT_)?M0[23]_RESULT=")

    def test_12_scanner_rejects_unclassified_demo_enablement(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rogue = root / "engine/IDUNEX/00_INDEX/ROGUE_CERTIFICATE.txt"
            rogue.parent.mkdir(parents=True)
            rogue.write_text("READY_FOR_PROJECT_DEMO_GENERATION=TRUE\n", encoding="utf-8")
            findings, historical_matches = scan_contradictions(root)
        self.assertTrue(findings)
        self.assertEqual(historical_matches, 0)


if __name__ == "__main__":
    unittest.main()
