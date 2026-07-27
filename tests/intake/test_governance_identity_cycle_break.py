from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Callable


REPO_ROOT = Path(__file__).resolve().parents[2]
EXPECTED_IDENTITY = {
    "file_count": 981,
    "byte_count": 47_361_805,
    "tree_sha256": "ff6a3a6d376206bd052d124031a72ca55c90827f5f69e3d3c851033128028ea3",
}


def engine_identity(engine: Path) -> dict[str, object]:
    rows: list[tuple[str, int, str]] = []
    for path in engine.rglob("*"):
        if path.is_file():
            data = path.read_bytes()
            relative = "engine/IDUNEX/" + path.relative_to(engine).as_posix()
            rows.append((relative, len(data), hashlib.sha256(data).hexdigest()))
    rows.sort()
    aggregate = hashlib.sha256()
    for relative, size, digest in rows:
        aggregate.update(f"{relative}\0{size}\0{digest}\n".encode("utf-8"))
    return {
        "file_count": len(rows),
        "byte_count": sum(row[1] for row in rows),
        "tree_sha256": aggregate.hexdigest(),
    }


class GovernanceIdentityCycleBreakTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._temporary = tempfile.TemporaryDirectory(prefix="aud037-cycle-break-")
        cls.root = Path(cls._temporary.name)
        shutil.copytree(REPO_ROOT / "engine", cls.root / "engine")
        shutil.copytree(REPO_ROOT / "governance", cls.root / "governance")
        cls.engine = cls.root / "engine/IDUNEX"
        cls.validator = cls.engine / "99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py"
        cls.state_path = cls.root / "governance/CURRENT_STATE.json"
        cls.contract_path = cls.engine / (
            "07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/"
            "MASTER_GOVERNANCE_VALIDATION_CONTRACT.json"
        )
        cls.base_state = cls.state_path.read_bytes()
        cls.base_contract = cls.contract_path.read_bytes()

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temporary.cleanup()

    def setUp(self) -> None:
        self.state_path.write_bytes(self.base_state)
        self.contract_path.write_bytes(self.base_contract)

    def write_state(self, state: dict) -> None:
        self.state_path.write_text(
            json.dumps(state, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def read_state(self) -> dict:
        return json.loads(self.state_path.read_text(encoding="utf-8"))

    def valid_evidence(self, seed: int = 1) -> dict:
        return {
            "run_id": seed,
            "job_id": seed + 1,
            "artifact_id": seed + 2,
            "artifact_name": f"synthetic-aud037-{seed}",
            "artifact_sha256": f"{seed % 16:x}" * 64,
            "repository_commit": f"{seed % 16:x}" * 40,
            "engine_tree_sha256": EXPECTED_IDENTITY["tree_sha256"],
            "engine_file_count": EXPECTED_IDENTITY["file_count"],
            "engine_byte_count": EXPECTED_IDENTITY["byte_count"],
            "technical_result": "PASS",
            "independent_audit_result": "VALIDADO_PASS",
            "evidence_class": "VALIDATED_CURRENT_TREE_EVIDENCE",
            "governance_formalization_status": "VALIDADO",
            "workflow_decision": "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY",
        }

    def valid_official_state(self) -> dict:
        state = self.read_state()
        state["m02_result"] = "M02_PASS"
        state["m03_result"] = "M03_PASS"
        state["m02_evidence"] = self.valid_evidence(1)
        state["m03_evidence"] = self.valid_evidence(4)
        state["motor_status"] = "OFICIAL"
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
        results = {
            "motor_audit": "PASS",
            "project_demo_generation": "PASS",
            "project_demo_audit": "PASS",
            "chatgpt_runtime": "PASS",
            "copilot_runtime": "VENDOR_LIMITATION_NOT_ENGINE_FAIL",
            "agent_runtime_audit": "PASS",
            "productive_formalization": "VALIDADO",
        }
        gates = {}
        for index, (gate, result) in enumerate(results.items(), start=1):
            gates[gate] = {
                "evidence_id": f"synthetic-{gate}-{index}",
                "result": result,
                "engine_tree_sha256": EXPECTED_IDENTITY["tree_sha256"],
                "engine_file_count": EXPECTED_IDENTITY["file_count"],
                "engine_byte_count": EXPECTED_IDENTITY["byte_count"],
            }
        state["official_transition_evidence"] = {
            "schema_version": 1,
            "formalization_status": "VALIDADO",
            "state_authority": "governance/CURRENT_STATE.json",
            "engine_tree_sha256": EXPECTED_IDENTITY["tree_sha256"],
            "engine_file_count": EXPECTED_IDENTITY["file_count"],
            "engine_byte_count": EXPECTED_IDENTITY["byte_count"],
            "gates": gates,
        }
        return state

    def run_validator(self, *, governance_only: bool = False) -> tuple[subprocess.CompletedProcess[str], dict]:
        command = [sys.executable, "-B", str(self.validator), str(self.engine)]
        if governance_only:
            command.append("--governance-state-contract-only")
        completed = subprocess.run(
            command,
            cwd=self.root,
            check=False,
            capture_output=True,
            text=True,
            timeout=180,
        )
        try:
            payload = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            self.fail(f"validator did not emit JSON: {exc}\n{completed.stdout}\n{completed.stderr}")
        return completed, payload

    def assert_failcode(self, expected: str) -> None:
        completed, payload = self.run_validator(governance_only=True)
        self.assertNotEqual(completed.returncode, 0, payload)
        self.assertEqual(payload["result"], "FAIL")
        self.assertIn(expected, payload["fail_codes"], payload)

    def test_01_external_m02_transition_passes_without_engine_identity_change(self):
        before = engine_identity(self.engine)
        self.assertEqual(before, EXPECTED_IDENTITY)

        baseline_completed, baseline_payload = self.run_validator()
        self.assertEqual(baseline_completed.returncode, 0, baseline_payload)
        self.assertEqual(baseline_payload["result"], "PASS")

        state = self.read_state()
        state["m02_result"] = "M02_PASS"
        state["m02_evidence"] = self.valid_evidence()
        self.write_state(state)
        transitioned_completed, transitioned_payload = self.run_validator()
        self.assertEqual(transitioned_completed.returncode, 0, transitioned_payload)
        self.assertEqual(transitioned_payload["result"], "PASS")
        self.assertEqual(transitioned_payload["fail_codes"], [])

        after = engine_identity(self.engine)
        self.assertEqual(after, before)

    def test_02_not_recomputed_is_issue_bound_and_pass_tokens_are_exact(self):
        cases = (
            ("m02_bare", "m02_result", "NOT_RECOMPUTED", "FAIL_M02_NOT_RECOMPUTED_ISSUE_BINDING"),
            ("m03_bare", "m03_result", "NOT_RECOMPUTED", "FAIL_M03_NOT_RECOMPUTED_ISSUE_BINDING"),
            ("m02_other_issue", "m02_result", "NOT_RECOMPUTED_POST_AUD036", "FAIL_M02_NOT_RECOMPUTED_ISSUE_BINDING"),
            ("m03_other_issue", "m03_result", "NOT_RECOMPUTED_POST_AUD036", "FAIL_M03_NOT_RECOMPUTED_ISSUE_BINDING"),
            ("m02_partial_pass", "m02_result", "M02_PASS_UNVERIFIED", "FAIL_M02_RESULT_SCHEMA"),
            ("m03_partial_pass", "m03_result", "M03_PASS_SUFFIX", "FAIL_M03_RESULT_SCHEMA"),
        )
        for label, field, value, failcode in cases:
            with self.subTest(label=label):
                self.setUp()
                state = self.read_state()
                state[field] = value
                self.write_state(state)
                self.assert_failcode(failcode)

    def test_03_pass_evidence_requires_audit_and_governance_formalization(self):
        cases = (
            ("technical_fail", "technical_result", "FAIL", "FAIL_M02_EVIDENCE_TECHNICAL_RESULT"),
            ("audit_missing", "independent_audit_result", None, "FAIL_M02_EVIDENCE_INDEPENDENT_AUDIT_RESULT"),
            ("class_invalid", "evidence_class", "WORKFLOW_ONLY", "FAIL_M02_EVIDENCE_CLASS"),
            ("formalization_missing", "governance_formalization_status", None, "FAIL_M02_EVIDENCE_GOVERNANCE_FORMALIZATION_STATUS"),
            ("artifact_sha_malformed", "artifact_sha256", "not-a-sha", "FAIL_M02_EVIDENCE_ARTIFACT_SHA256_INVALID"),
            ("other_tree", "engine_tree_sha256", "0" * 64, "FAIL_M02_EVIDENCE_ENGINE_TREE_SHA256_MISMATCH"),
            ("workflow_not_formalized", "governance_formalization_status", "NOT_DECLARED", "FAIL_M02_WORKFLOW_EVIDENCE_NOT_FORMALIZED"),
        )
        for label, field, value, failcode in cases:
            with self.subTest(label=label):
                self.setUp()
                state = self.read_state()
                state["m02_result"] = "M02_PASS"
                state["m02_evidence"] = self.valid_evidence()
                if value is None:
                    state["m02_evidence"].pop(field)
                else:
                    state["m02_evidence"][field] = value
                self.write_state(state)
                self.assert_failcode(failcode)

    def test_04_official_transition_is_fail_closed_per_independent_gate(self):
        def mutate_without_m02(state):
            state["m02_result"] = "NOT_RECOMPUTED_POST_AUD037"
            state.pop("m02_evidence")

        def mutate_without_m03(state):
            state["m03_result"] = "NOT_RECOMPUTED_POST_AUD037"
            state.pop("m03_evidence")

        cases: tuple[tuple[str, Callable[[dict], None], str], ...] = (
            ("without_m02", mutate_without_m02, "FAIL_OFFICIAL_REQUIRES_M02_PASS"),
            ("without_m03", mutate_without_m03, "FAIL_OFFICIAL_REQUIRES_M03_PASS"),
            ("without_motor_audit", lambda state: state["official_transition_evidence"]["gates"].pop("motor_audit"), "FAIL_OFFICIAL_MOTOR_AUDIT_REQUIRED"),
            ("without_demo", lambda state: state["official_transition_evidence"]["gates"].pop("project_demo_generation"), "FAIL_OFFICIAL_DEMO_GENERATION_REQUIRED"),
            ("without_demo_audit", lambda state: state["official_transition_evidence"]["gates"].pop("project_demo_audit"), "FAIL_OFFICIAL_DEMO_AUDIT_REQUIRED"),
            ("without_chatgpt", lambda state: state["official_transition_evidence"]["gates"].pop("chatgpt_runtime"), "FAIL_OFFICIAL_CHATGPT_RUNTIME_REQUIRED"),
            ("invalid_copilot", lambda state: state["official_transition_evidence"]["gates"]["copilot_runtime"].update({"result": "UNAVAILABLE"}), "FAIL_OFFICIAL_COPILOT_RUNTIME_REQUIRED"),
            ("without_agent_runtime_audit", lambda state: state["official_transition_evidence"]["gates"].pop("agent_runtime_audit"), "FAIL_OFFICIAL_AGENT_RUNTIME_AUDIT_REQUIRED"),
            ("other_tree", lambda state: state["official_transition_evidence"]["gates"]["motor_audit"].update({"engine_tree_sha256": "0" * 64}), "FAIL_OFFICIAL_EVIDENCE_CURRENT_TREE_MISMATCH"),
            ("invented_authorization", lambda state: state["official_transition_evidence"].update({"authorization_override": "INVENTED"}), "FAIL_OFFICIAL_TRANSITION_AUTHORIZATION_INVALID"),
        )
        for label, mutate, failcode in cases:
            with self.subTest(label=label):
                self.setUp()
                state = self.valid_official_state()
                mutate(state)
                self.write_state(state)
                self.assert_failcode(failcode)

    def test_05_external_official_transition_passes_without_engine_identity_change(self):
        before = engine_identity(self.engine)
        self.assertEqual(before, EXPECTED_IDENTITY)
        self.write_state(self.valid_official_state())
        completed, payload = self.run_validator()
        self.assertEqual(completed.returncode, 0, payload)
        self.assertEqual(payload["result"], "PASS")
        self.assertEqual(payload["fail_codes"], [])
        self.assertEqual(engine_identity(self.engine), before)

    def test_06_required_negative_mutations_have_specific_failcodes(self):
        cases: list[tuple[str, Callable[[], None], str]] = []

        def state_case(mutator):
            state = self.read_state()
            mutator(state)
            self.write_state(state)

        def m02_pass(state):
            state["m02_result"] = "M02_PASS"
            state["m02_evidence"] = self.valid_evidence()

        cases.extend([
            ("m02_wrong_sha", lambda: state_case(lambda state: (m02_pass(state), state["m02_evidence"].__setitem__("engine_tree_sha256", "0" * 64))), "FAIL_M02_EVIDENCE_ENGINE_TREE_SHA256_MISMATCH"),
            ("m02_wrong_bytes", lambda: state_case(lambda state: (m02_pass(state), state["m02_evidence"].__setitem__("engine_byte_count", 1))), "FAIL_M02_EVIDENCE_ENGINE_BYTE_COUNT_MISMATCH"),
            ("m03_without_m02", lambda: state_case(lambda state: (state.__setitem__("m03_result", "M03_PASS"), state.__setitem__("m03_evidence", self.valid_evidence(4)))), "FAIL_M03_PASS_REQUIRES_M02_PASS"),
            ("m02_without_artifact", lambda: state_case(lambda state: (m02_pass(state), state["m02_evidence"].pop("artifact_id"))), "FAIL_M02_EVIDENCE_ARTIFACT_ID_MISSING"),
            ("aud028_reauthorized", lambda: state_case(lambda state: state["controlled_external_demo_execution"].update({"authorized": True})), "FAIL_AUD028_CONSUMED_INTERLOCK"),
            ("aud028_generate_nonzero", lambda: state_case(lambda state: state["controlled_external_demo_execution"].update({"generate_executions_allowed": 1})), "FAIL_AUD028_GENERATE_EXECUTIONS_ALLOWED_NONZERO"),
            ("aud028_validate_nonzero", lambda: state_case(lambda state: state["controlled_external_demo_execution"].update({"validate_executions_allowed": 1})), "FAIL_AUD028_VALIDATE_EXECUTIONS_ALLOWED_NONZERO"),
            ("demo_enabled", lambda: state_case(lambda state: state.update({"ready_for_project_demo_generation": True})), "FAIL_EN_REVISION_DEMO_INTERLOCK"),
            ("release_enabled", lambda: state_case(lambda state: state.update({"release_authorized": True})), "FAIL_EN_REVISION_RELEASE_INTERLOCK"),
            ("tag_enabled", lambda: state_case(lambda state: state.update({"tag_authorized": True})), "FAIL_EN_REVISION_TAG_INTERLOCK"),
            ("oficial_enabled", lambda: state_case(lambda state: state.update({"oficial_authorized": True})), "FAIL_EN_REVISION_OFICIAL_INTERLOCK"),
            ("agents_enabled", lambda: state_case(lambda state: state.update({"agent_load_authorized": True})), "FAIL_EN_REVISION_AGENT_LOAD_INTERLOCK"),
            ("creative_enabled", lambda: state_case(lambda state: state.update({"creative_output_certified": True})), "FAIL_CREATIVE_OUTPUT_FALSE_INTERLOCK"),
        ])

        def snapshot_authority():
            contract = json.loads(self.contract_path.read_text(encoding="utf-8"))
            contract["build_state_snapshot_authority"] = True
            self.contract_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")

        def exact_equality():
            contract = json.loads(self.contract_path.read_text(encoding="utf-8"))
            contract["expected_current_state"] = {"M02_RESULT": "NOT_RECOMPUTED_POST_AUD037"}
            self.contract_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")

        cases.extend([
            ("snapshot_authority", snapshot_authority, "FAIL_INTERNAL_BUILD_SNAPSHOT_AUTHORITY"),
            ("audit_specific_exact_equality", exact_equality, "FAIL_MASTER_GOVERNANCE_AUDIT_SPECIFIC_STATE_EQUALITY"),
        ])

        for label, mutate, failcode in cases:
            with self.subTest(label=label):
                self.setUp()
                mutate()
                self.assert_failcode(failcode)


if __name__ == "__main__":
    unittest.main()
