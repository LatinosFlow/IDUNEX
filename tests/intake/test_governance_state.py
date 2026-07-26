import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.governance_state_check import (
    AUD035_BASE_COMMIT,
    CURRENT_ENGINE_BYTE_COUNT,
    CURRENT_ENGINE_TREE_SHA256,
    M02_EVIDENCE_ENGINE_TREE_SHA256,
    M02_RECOMPUTATION_STATE,
    PREVIOUS_ENGINE_TREE_SHA256,
    scan_contradictions,
    validate_current_state_data,
)


FORBIDDEN_TRANSIENT_STATE_TOKENS = (
    "ESTADO_PROPUESTO_EN_REVISION_" + "HASTA" + "_MERGE",
    "HASTA" + "_MERGE",
    "until" + " merge",
)
ACTIVE_PERSISTENT_STATE_SURFACES = (
    Path("governance/CURRENT_STATE.json"),
    Path("REPOSITORY_MANIFEST.yml"),
    Path("engine/IDUNEX/00_INDEX/ACTIVE_VERSION.txt"),
    Path("engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/ACTIVE_VERSION.md"),
    Path("engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/STATUS.md"),
    Path("engine/IDUNEX/00_INDEX/CHANGELOG.md"),
    Path("docs/audits/IA-IDUNEX-SincronizacionGobernanzaInternaPostAUD034-20260726-v1-EN_REVISION.md"),
)
HISTORICAL_STATE_PREFIXES = (
    "engine/IDUNEX/12_HISTORICAL_NON_AUTHORITY/",
    "engine/IDUNEX/14_HISTORICAL_NON_AUTHORITY/",
    "governance/authority/REFERENCIA/",
)


def transient_state_findings(root: Path, surfaces: tuple[Path, ...]) -> list[str]:
    findings: list[str] = []
    for relative in surfaces:
        text = (root / relative).read_text(encoding="utf-8", errors="replace")
        matches = [token for token in FORBIDDEN_TRANSIENT_STATE_TOKENS if token.lower() in text.lower()]
        if not matches:
            continue
        rel = relative.as_posix()
        historical = any(rel.startswith(prefix) for prefix in HISTORICAL_STATE_PREFIXES)
        classified_reference = "REFERENCIA_SUSTITUIDA" in text or "REFERENCIA_HISTORICA_SUSTITUIDA" in text
        if historical and classified_reference:
            continue
        findings.append(f"{rel}: {matches}")
    return findings


def aud034_state() -> dict:
    return json.loads(Path("governance/CURRENT_STATE.json").read_text(encoding="utf-8"))


def aud034_m02_manifest_block() -> str:
    text = Path("REPOSITORY_MANIFEST.yml").read_text(encoding="utf-8")
    return text.split("aud034_m02_recomputation:\n", 1)[1].split("\ncurrent_motor_package_candidate:", 1)[0]


class GovernanceStateTest(unittest.TestCase):
    def test_01_current_aud035_state_passes_checker(self):
        result = subprocess.run(
            [sys.executable, "tools/audit/governance_state_check.py", "--repo-root", "."],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["result"], "CONSISTENT")
        self.assertEqual(report["m02_result"], M02_RECOMPUTATION_STATE)
        self.assertEqual(report["m03_result"], "NOT_RECOMPUTED_POST_AUD035")

    def test_02_generic_m02_pass_is_rejected(self):
        state = aud034_state()
        state["m02_result"] = "M02_PASS"
        self.assertTrue(any("m02_result" in finding for finding in validate_current_state_data(state)))

    def test_03_post_pr44_m02_pass_is_rejected(self):
        state = aud034_state()
        state["m02_result"] = "M02_PASS_RECOMPUTED_POST_PR44"
        self.assertTrue(any("m02_result" in finding for finding in validate_current_state_data(state)))

    def test_04_old_m02_not_recomputed_state_is_rejected(self):
        state = aud034_state()
        state["m02_result"] = "NOT_RECOMPUTED_POST_AUD030"
        self.assertTrue(any("m02_result" in finding for finding in validate_current_state_data(state)))

    def test_05_m03_pass_is_rejected(self):
        state = aud034_state()
        state["m03_result"] = "M03_PASS"
        self.assertTrue(any("m03_result" in finding for finding in validate_current_state_data(state)))

    def test_06_aud028_cannot_be_reauthorized(self):
        state = aud034_state()
        state["controlled_external_demo_execution"].update(
            {"status": "AUTHORIZED_NOT_CONSUMED", "authorized": True, "consumed": False}
        )
        findings = validate_current_state_data(state)
        self.assertTrue(any("status" in finding for finding in findings))
        self.assertTrue(any("authorized" in finding for finding in findings))
        self.assertTrue(any("consumed" in finding for finding in findings))

    def test_07_generate_execution_counter_must_remain_zero(self):
        state = aud034_state()
        state["controlled_external_demo_execution"]["generate_executions_allowed"] = 1
        self.assertTrue(any("generate_executions_allowed" in finding for finding in validate_current_state_data(state)))

    def test_08_artifact_sha_must_match_authorized_evidence(self):
        state = aud034_state()
        state["prior_m02_recomputation_evidence"]["artifact_sha256"] = "0" * 64
        self.assertTrue(any("artifact_sha256" in finding for finding in validate_current_state_data(state)))

    def test_09_engine_tree_sha_must_match_authorized_evidence(self):
        state = aud034_state()
        state["prior_m02_recomputation_evidence"]["engine_tree_sha256"] = "0" * 64
        self.assertTrue(any("engine_tree_sha256" in finding for finding in validate_current_state_data(state)))

    def test_10_release_oficial_and_agent_load_remain_disabled(self):
        state = aud034_state()
        state.update({"release_authorized": True, "oficial_authorized": True, "agent_load_authorized": True})
        findings = validate_current_state_data(state)
        self.assertTrue(any("release_authorized" in finding for finding in findings))
        self.assertTrue(any("oficial_authorized" in finding for finding in findings))
        self.assertTrue(any("agent_load_authorized" in finding for finding in findings))

    def test_11_creative_output_certification_must_remain_false(self):
        state = aud034_state()
        state["creative_output_certified"] = True
        self.assertTrue(any("creative_output_certified" in finding for finding in validate_current_state_data(state)))

    def test_12_intact_current_state_passes_direct_validation(self):
        self.assertEqual(validate_current_state_data(copy.deepcopy(aud034_state())), [])

    def test_13_scanner_rejects_unclassified_demo_enablement(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rogue = root / "engine" / "IDUNEX" / "00_INDEX" / "ROGUE_CERTIFICATE.txt"
            rogue.parent.mkdir(parents=True)
            rogue.write_text(
                "M02_RESULT=NOT_RECOMPUTED_POST_AUD030\nREADY_FOR_PROJECT_DEMO_GENERATION=TRUE\n",
                encoding="utf-8",
            )
            findings, historical_matches = scan_contradictions(root)
        self.assertTrue(findings)
        self.assertEqual(historical_matches, 0)

    def test_14_historical_m02_bytes_and_binding_are_immutable(self):
        state = aud034_state()
        evidence = state["prior_m02_recomputation_evidence"]
        self.assertEqual(evidence["engine_tree_sha256"], M02_EVIDENCE_ENGINE_TREE_SHA256)
        self.assertEqual(evidence["engine_byte_count"], 47_323_574)
        self.assertEqual(evidence["m02_result"], "M02_PASS_RECOMPUTED_POST_AUD033")
        self.assertEqual(evidence["evidence_class"], "REFERENCIA_SUSTITUIDA")
        self.assertFalse(evidence["current_tree_applicability"])
        self.assertEqual(evidence["superseded_by"], "AUD-035")
        mutated = copy.deepcopy(state)
        mutated["prior_m02_recomputation_evidence"]["engine_byte_count"] = CURRENT_ENGINE_BYTE_COUNT
        self.assertTrue(any("engine_byte_count" in finding for finding in validate_current_state_data(mutated)))
        mutated = copy.deepcopy(state)
        mutated["prior_m02_recomputation_evidence"]["engine_tree_sha256"] = CURRENT_ENGINE_TREE_SHA256
        mutated["prior_m02_recomputation_evidence"]["current_tree_applicability"] = True
        findings = validate_current_state_data(mutated)
        self.assertTrue(any("historical M02 evidence" in finding for finding in findings))

    def test_15_aud035_base_previous_tree_and_m03_failure_are_exact(self):
        state = aud034_state()
        control = state["engine_change_control"]
        self.assertEqual(control["base_commit"], AUD035_BASE_COMMIT)
        self.assertEqual(control["previous_engine_tree_sha256"], PREVIOUS_ENGINE_TREE_SHA256)
        self.assertEqual(control["previous_engine_byte_count"], 47_324_957)
        self.assertEqual(control["previous_engine_tree_classification"], "INTERMEDIATE_DRAFT_PR71_IDENTITY_SUPERSEDED_BY_FINAL_TRUTHFULNESS")
        self.assertEqual(state["last_failed_m03_run"], 30189604763)
        self.assertEqual(state["last_failed_m03_case"], "M03-19")
        self.assertEqual(state["last_failed_m03_result"], "VALIDATED_FAIL")
        self.assertNotIn("last_failed_m02_run", state)
        mutated = copy.deepcopy(state)
        mutated["engine_change_control"]["base_commit"] = "0" * 40
        self.assertTrue(any("base_commit" in finding for finding in validate_current_state_data(mutated)))
        mutated = copy.deepcopy(state)
        mutated["engine_change_control"]["previous_engine_tree_sha256"] = "0" * 64
        self.assertTrue(any("previous_engine_tree_sha256" in finding for finding in validate_current_state_data(mutated)))
        mutated = copy.deepcopy(state)
        mutated["last_failed_m02_run"] = 30189604763
        self.assertTrue(any("last_failed_m02_run" in finding for finding in validate_current_state_data(mutated)))

    def test_16_repository_manifest_preserves_aud034_m02_evidence(self):
        block = aud034_m02_manifest_block()
        for token in (
            "m02_result: M02_PASS_RECOMPUTED_POST_AUD033",
            "run_id: 29941393366",
            "job_id: 88995880545",
            "artifact_id: 8539029665",
            "artifact_sha256: fd5c9334b96989c714300607dadf742ff63783b8090d90fc3d404b3a22355270",
            "repository_commit: 1fc082bfcae5b590066309727c120500de976378",
            f"engine_tree_sha256: {M02_EVIDENCE_ENGINE_TREE_SHA256}",
            "engine_file_count: 981",
            "engine_byte_count: 47323574",
            "evidence_class: REFERENCIA_SUSTITUIDA",
            "current_tree_applicability: false",
            "superseded_by: AUD-035",
        ):
            with self.subTest(token=token):
                self.assertIn(token, block)
        self.assertNotIn(CURRENT_ENGINE_TREE_SHA256, block)

    def test_17_active_surfaces_use_persistent_post_merge_classification(self):
        self.assertEqual(transient_state_findings(Path("."), ACTIVE_PERSISTENT_STATE_SURFACES), [])
        expected = "EN_REVISION_M02_M03_NOT_RECOMPUTED_POST_AUD035"
        for relative in ACTIVE_PERSISTENT_STATE_SURFACES:
            text = relative.read_text(encoding="utf-8", errors="replace")
            if relative.name in {"ACTIVE_VERSION.txt", "ACTIVE_VERSION.md", "STATUS.md", "CHANGELOG.md"}:
                with self.subTest(relative=relative.as_posix()):
                    self.assertIn(expected, text)

    def test_18_only_clearly_classified_historical_zones_may_retain_transient_text(self):
        transient = FORBIDDEN_TRANSIENT_STATE_TOKENS[0]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            classified = Path("engine/IDUNEX/14_HISTORICAL_NON_AUTHORITY/old.md")
            unclassified = Path("engine/IDUNEX/14_HISTORICAL_NON_AUTHORITY/rogue.md")
            (root / classified).parent.mkdir(parents=True)
            (root / classified).write_text(f"REFERENCIA_SUSTITUIDA\n{transient}\n", encoding="utf-8")
            (root / unclassified).write_text(f"{transient}\n", encoding="utf-8")
            self.assertEqual(transient_state_findings(root, (classified,)), [])
            self.assertTrue(transient_state_findings(root, (unclassified,)))


if __name__ == "__main__":
    unittest.main()
