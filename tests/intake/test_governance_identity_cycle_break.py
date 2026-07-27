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
    "byte_count": 47_370_003,
    "tree_sha256": "87c0e9e681a3a4995d4f096eaaa73cd5c7a889e9c10a5f0f4b3c9897e80c2346",
}
OFFICIAL_GATE_RESULTS = {
    "motor_audit": "PASS",
    "project_demo_generation": "PASS",
    "project_demo_audit": "PASS",
    "chatgpt_runtime": "PASS",
    "copilot_runtime": "VENDOR_LIMITATION_NOT_ENGINE_FAIL",
    "agent_runtime_audit": "PASS",
    "productive_formalization": "VALIDADO",
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
        cls.official_evidence_root = cls.root / "governance/evidence/official"
        cls.base_state = cls.state_path.read_bytes()
        cls.base_contract = cls.contract_path.read_bytes()

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temporary.cleanup()

    def setUp(self) -> None:
        self.state_path.write_bytes(self.base_state)
        self.contract_path.write_bytes(self.base_contract)
        if self.official_evidence_root.exists():
            shutil.rmtree(self.official_evidence_root)

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

    def write_official_evidence(self, gate_name: str, result: str, index: int) -> dict:
        evidence_id = f"synthetic-{gate_name}-{index}"
        relative_path = f"governance/evidence/official/{gate_name}-{index}.json"
        document = {
            "schema_version": 1,
            "evidence_id": evidence_id,
            "gate_name": gate_name,
            "result": result,
            "independent_audit_result": "VALIDADO_PASS",
            "evidence_class": "VALIDATED_EXTERNAL_EVIDENCE",
            "governance_formalization_status": "VALIDADO",
            "engine_tree_sha256": EXPECTED_IDENTITY["tree_sha256"],
            "engine_file_count": EXPECTED_IDENTITY["file_count"],
            "engine_byte_count": EXPECTED_IDENTITY["byte_count"],
        }
        evidence_file = self.root / relative_path
        evidence_file.parent.mkdir(parents=True, exist_ok=True)
        evidence_bytes = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        evidence_file.write_bytes(evidence_bytes)
        return {
            "evidence_id": evidence_id,
            "evidence_path": relative_path,
            "evidence_sha256": hashlib.sha256(evidence_bytes).hexdigest(),
            "result": result,
            "independent_audit_result": "VALIDADO_PASS",
            "evidence_class": "VALIDATED_EXTERNAL_EVIDENCE",
            "governance_formalization_status": "VALIDADO",
            "engine_tree_sha256": EXPECTED_IDENTITY["tree_sha256"],
            "engine_file_count": EXPECTED_IDENTITY["file_count"],
            "engine_byte_count": EXPECTED_IDENTITY["byte_count"],
        }

    def mutate_official_document(self, state: dict, gate_name: str, mutator: Callable[[dict], None]) -> None:
        gate = state["official_transition_evidence"]["gates"][gate_name]
        evidence_file = self.root / gate["evidence_path"]
        document = json.loads(evidence_file.read_text(encoding="utf-8"))
        mutator(document)
        evidence_bytes = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        evidence_file.write_bytes(evidence_bytes)
        gate["evidence_sha256"] = hashlib.sha256(evidence_bytes).hexdigest()

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
        ):
            state[field] = True
        state["creative_output_certified"] = False
        gates = {}
        for index, (gate, result) in enumerate(OFFICIAL_GATE_RESULTS.items(), start=1):
            gates[gate] = self.write_official_evidence(gate, result, index)
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
            ("other_tree", lambda state: state["official_transition_evidence"]["gates"]["motor_audit"].update({"engine_tree_sha256": "0" * 64}), "FAIL_OFFICIAL_EVIDENCE_ENGINE_TREE_SHA256_MISMATCH"),
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

    def test_06_official_evidence_path_guards_have_specific_failcodes(self):
        def missing_file(state: dict) -> None:
            gate = state["official_transition_evidence"]["gates"]["motor_audit"]
            (self.root / gate["evidence_path"]).unlink()

        def absolute_path(state: dict) -> None:
            gate = state["official_transition_evidence"]["gates"]["motor_audit"]
            gate["evidence_path"] = str((self.root / gate["evidence_path"]).resolve())

        def non_json_extension(state: dict) -> None:
            gate = state["official_transition_evidence"]["gates"]["motor_audit"]
            source = self.root / gate["evidence_path"]
            target = source.with_suffix(".txt")
            shutil.copyfile(source, target)
            gate["evidence_path"] = target.relative_to(self.root).as_posix()

        cases: tuple[tuple[str, Callable[[dict], None], str], ...] = (
            ("missing_file", missing_file, "FAIL_OFFICIAL_EVIDENCE_FILE_MISSING"),
            ("absolute_path", absolute_path, "FAIL_OFFICIAL_EVIDENCE_PATH_ABSOLUTE"),
            ("path_traversal", lambda state: state["official_transition_evidence"]["gates"]["motor_audit"].update({"evidence_path": "governance/evidence/official/../escape.json"}), "FAIL_OFFICIAL_EVIDENCE_PATH_TRAVERSAL"),
            ("outside_root", lambda state: state["official_transition_evidence"]["gates"]["motor_audit"].update({"evidence_path": "governance/evidence/outside.json"}), "FAIL_OFFICIAL_EVIDENCE_PATH_OUTSIDE_AUTHORIZED_ROOT"),
            ("engine_path", lambda state: state["official_transition_evidence"]["gates"]["motor_audit"].update({"evidence_path": "engine/IDUNEX/evidence.json"}), "FAIL_OFFICIAL_EVIDENCE_PATH_ENGINE_FORBIDDEN"),
            ("non_json_extension", non_json_extension, "FAIL_OFFICIAL_EVIDENCE_EXTENSION"),
        )
        for label, mutate, failcode in cases:
            with self.subTest(label=label):
                self.setUp()
                state = self.valid_official_state()
                mutate(state)
                self.write_state(state)
                self.assert_failcode(failcode)

    def test_07_official_evidence_integrity_and_content_mutations_have_specific_failcodes(self):
        def invalid_json(state: dict) -> None:
            gate = state["official_transition_evidence"]["gates"]["motor_audit"]
            evidence_bytes = b"{invalid-json\n"
            (self.root / gate["evidence_path"]).write_bytes(evidence_bytes)
            gate["evidence_sha256"] = hashlib.sha256(evidence_bytes).hexdigest()

        document_cases: tuple[tuple[str, Callable[[dict], None], str], ...] = (
            ("wrong_gate_name", lambda document: document.update({"gate_name": "wrong_gate"}), "FAIL_OFFICIAL_EVIDENCE_GATE_NAME_MISMATCH"),
            ("divergent_result", lambda document: document.update({"result": "FAIL"}), "FAIL_OFFICIAL_EVIDENCE_RESULT_MISMATCH"),
            ("divergent_tree", lambda document: document.update({"engine_tree_sha256": "0" * 64}), "FAIL_OFFICIAL_EVIDENCE_ENGINE_TREE_SHA256_MISMATCH"),
            ("divergent_bytes", lambda document: document.update({"engine_byte_count": 1}), "FAIL_OFFICIAL_EVIDENCE_ENGINE_BYTE_COUNT_MISMATCH"),
            ("audit_missing", lambda document: document.pop("independent_audit_result"), "FAIL_OFFICIAL_EVIDENCE_INDEPENDENT_AUDIT_RESULT"),
            ("class_invalid", lambda document: document.update({"evidence_class": "DECLARED_ONLY"}), "FAIL_OFFICIAL_EVIDENCE_CLASS"),
            ("formalization_missing", lambda document: document.pop("governance_formalization_status"), "FAIL_OFFICIAL_EVIDENCE_GOVERNANCE_FORMALIZATION_STATUS"),
        )
        for label, mutate, failcode in document_cases:
            with self.subTest(label=label):
                self.setUp()
                state = self.valid_official_state()
                self.mutate_official_document(state, "motor_audit", mutate)
                self.write_state(state)
                self.assert_failcode(failcode)

        direct_cases: tuple[tuple[str, Callable[[dict], None], str], ...] = (
            ("wrong_sha", lambda state: state["official_transition_evidence"]["gates"]["motor_audit"].update({"evidence_sha256": "0" * 64}), "FAIL_OFFICIAL_EVIDENCE_SHA256_MISMATCH"),
            ("invalid_json", invalid_json, "FAIL_OFFICIAL_EVIDENCE_JSON_INVALID"),
        )
        for label, mutate, failcode in direct_cases:
            with self.subTest(label=label):
                self.setUp()
                state = self.valid_official_state()
                mutate(state)
                self.write_state(state)
                self.assert_failcode(failcode)

    def test_08_official_evidence_uniqueness_and_creative_false_are_enforced(self):
        def duplicate_id(state: dict) -> None:
            gates = state["official_transition_evidence"]["gates"]
            duplicate = gates["motor_audit"]["evidence_id"]
            gates["project_demo_generation"]["evidence_id"] = duplicate
            self.mutate_official_document(
                state,
                "project_demo_generation",
                lambda document: document.update({"evidence_id": duplicate}),
            )

        def duplicate_path(state: dict) -> None:
            gates = state["official_transition_evidence"]["gates"]
            gates["project_demo_generation"]["evidence_path"] = gates["motor_audit"]["evidence_path"].replace(
                "governance/evidence/official/",
                "governance/evidence/official/./",
            )
            gates["project_demo_generation"]["evidence_sha256"] = gates["motor_audit"]["evidence_sha256"]

        cases: tuple[tuple[str, Callable[[dict], None], str], ...] = (
            ("duplicate_id", duplicate_id, "FAIL_OFFICIAL_EVIDENCE_ID_DUPLICATE"),
            ("duplicate_path", duplicate_path, "FAIL_OFFICIAL_EVIDENCE_PATH_DUPLICATE"),
            ("creative_true_official", lambda state: state.update({"creative_output_certified": True}), "FAIL_MOTOR_CREATIVE_OUTPUT_CERTIFICATION_FORBIDDEN"),
        )
        for label, mutate, failcode in cases:
            with self.subTest(label=label):
                self.setUp()
                state = self.valid_official_state()
                mutate(state)
                self.write_state(state)
                self.assert_failcode(failcode)

        self.setUp()
        state = self.read_state()
        state["creative_output_certified"] = True
        self.write_state(state)
        self.assert_failcode("FAIL_MOTOR_CREATIVE_OUTPUT_CERTIFICATION_FORBIDDEN")

    def test_09_required_negative_mutations_have_specific_failcodes(self):
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
            ("creative_enabled", lambda: state_case(lambda state: state.update({"creative_output_certified": True})), "FAIL_MOTOR_CREATIVE_OUTPUT_CERTIFICATION_FORBIDDEN"),
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
