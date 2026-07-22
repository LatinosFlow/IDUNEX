"""Focused mutation coverage for post-AUD024 truthfulness gates.

These fixtures are synthetic and never generate any named external Demo project.
"""
import importlib.util
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[2]
FACTORY = REPO_ROOT / "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py"
SPEC = importlib.util.spec_from_file_location("idunex_factory", FACTORY)
factory = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(factory)


class PostAuditTruthfulnessTests(unittest.TestCase):
    def _clean_fixture(self, root):
        (root / "09_MANIFESTS_SHA").mkdir()
        (root / "01_CANON").mkdir()
        (root / "10_RELEASE").mkdir()
        (root / "evidence_a.txt").write_text("evidence A", encoding="utf-8")
        (root / "evidence_b.txt").write_text("evidence B", encoding="utf-8")
        ledger = root / "09_MANIFESTS_SHA" / "PROJECT_PACKAGE_SHA256SUMS.txt"
        ledger.write_text("", encoding="utf-8")
        factory.write_json(root / "09_MANIFESTS_SHA" / "CONTENT_TREE_PROOF_NOT_FINAL_ZIP_SHA.json", {"content_tree_sha256": factory.hashlib.sha256(b"").hexdigest()})
        factory.write_json(root / "01_CANON" / "INPUT_PROMPT_FIDELITY_LEDGER.json", {"rows": [{"materialization_evidence_paths": ["evidence_a.txt", "evidence_b.txt"], "materialization_evidence_hashes": {"evidence_a.txt": factory.sha(root / "evidence_a.txt"), "evidence_b.txt": factory.sha(root / "evidence_b.txt")}}]})
        factory.write_json(root / "09_MANIFESTS_SHA" / "PROJECT_MATRIX_COMPLETION_PROOF.json", {"MATRIX_CASES_EXECUTED": 1, "MATRIX_CASES_TOTAL": 1, "MATRIX_CASES_FAIL": 0, "MATRIX_COMPLETION_SIGNAL": "COMPLETE_PASS"})
        factory.write_json(root / "09_MANIFESTS_SHA" / "CREATIVE_CERTIFICATION_TRUTHFULNESS.json", {"CREATIVE_OUTPUT_CERTIFIED": False, "PACKAGE_PASS_IMPLIES_CREATIVE_OUTPUT_PASS": False})
        (root / "10_RELEASE" / "FINAL_AUDIT_REPORT.md").write_text("## A\n\nunique A\n\n## B\n\nunique B\n", encoding="utf-8")
        factory._h274_write_project_exact_duplicate_allowlist(root)

    def test_forensic_report_has_no_exact_padding(self):
        report = factory.h116_forensic_report_text("IDUNEX_PROJECT_FIXTURE", 1, "tree", "engine", "sentinel", "sentinel", {})
        bodies = [section.strip() for section in report.split("## ")[1:]]
        self.assertEqual(len(bodies), len(set(bodies)))
        self.assertNotIn("for i in range(1,25)", report)
        for number in range(1, 17):
            self.assertIn(f"## {number}.", report)
        bodies = [part.split("\n\n", 1)[1].strip() for part in report.split("## ")[1:]]
        self.assertEqual(16, len(bodies))
        self.assertTrue(all(bodies))

    def test_duplicate_allowlist_mutation_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._clean_fixture(root)
            (root / "a.txt").write_text("same", encoding="utf-8")
            (root / "b.txt").write_text("same", encoding="utf-8")
            factory._h274_write_project_exact_duplicate_allowlist(root)
            (root / "b.txt").write_text("changed", encoding="utf-8")
            result = factory.validate_h269_h280_project_truthfulness(root)
            self.assertIn("FAIL_H274_DUPLICATE_GROUP_COUNT_OR_ALLOWLIST_STALE", result["fail_codes"])

    def test_fidelity_hash_mutation_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._clean_fixture(root)
            evidence = root / "evidence.txt"
            evidence.write_text("before", encoding="utf-8")
            factory.write_json(root / "01_CANON" / "INPUT_PROMPT_FIDELITY_LEDGER.json", {"rows": [{"materialization_evidence_hashes": {"evidence.txt": factory.sha(evidence)}}]})
            evidence.write_text("after", encoding="utf-8")
            result = factory.validate_h269_h280_project_truthfulness(root)
            self.assertIn("FAIL_H284_FIDELITY_LEDGER_HASH_STALE", result["fail_codes"])

    def test_content_tree_post_finalizer_mutation_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._clean_fixture(root)
            factory.write_json(root / "09_MANIFESTS_SHA" / "CONTENT_TREE_PROOF_NOT_FINAL_ZIP_SHA.json", {"content_tree_sha256": "0" * 64})
            result = factory.validate_h269_h280_project_truthfulness(root)
            self.assertIn("FAIL_H283_CONTENT_TREE_POST_FINALIZER_DESYNC", result["fail_codes"])

    def test_report_padding_mutation_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._clean_fixture(root)
            (root / "10_RELEASE" / "FINAL_AUDIT_REPORT.md").write_text("## A\n\nrepeated body\n\n## B\n\nrepeated body\n", encoding="utf-8")
            result = factory.validate_h269_h280_project_truthfulness(root)
            self.assertIn("FAIL_H285_FORENSIC_REPORT_REPEATED_SECTION", result["fail_codes"])

    def test_clean_fixture_passes_all_post_audit_gates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._clean_fixture(root)
            result = factory.validate_h269_h280_project_truthfulness(root)
            self.assertEqual("PASS", result["result"])

    def test_content_tree_scope_is_stable_after_two_recomputations(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "09_MANIFESTS_SHA").mkdir()
            (root / "payload.txt").write_text("stable payload", encoding="utf-8")
            factory.write_project_package_manifests(root, root.name)
            first = factory.compute_content_tree_sha256(root)
            factory.write_project_package_manifests(root, root.name)
            second = factory.compute_content_tree_sha256(root)
            self.assertEqual(first, second)

    def test_late_fifth_duplicate_is_reflected_in_final_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "09_MANIFESTS_SHA").mkdir()
            (root / "10_RELEASE").mkdir()
            for name in ("a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt", "g.txt", "h.txt", "i.txt", "j.txt"):
                (root / name).write_text(name[0], encoding="utf-8")
            # Five exact pairs are created after the initial tree exists.
            for left, right in (("a.txt", "b.txt"), ("c.txt", "d.txt"), ("e.txt", "f.txt"), ("g.txt", "h.txt"), ("i.txt", "j.txt")):
                (root / right).write_text((root / left).read_text(encoding="utf-8"), encoding="utf-8")
            factory._h274_write_project_exact_duplicate_allowlist(root)
            factory._h279_write_final_machine_audit_summary(root, 0, {}, {"validators_fail": 0})
            summary = factory.load_json(root / "10_RELEASE" / "FINAL_MACHINE_AUDIT_SUMMARY.json")
            self.assertEqual(5, summary["duplicate_allowlist_summary"]["duplicate_group_count"])

    def test_noncanonical_fixture_accepts_not_applicable_external_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            project_zip = Path(tmp) / "NON_DELIVERY_TEST_ONLY.zip"
            with zipfile.ZipFile(project_zip, "w", zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("NON_DELIVERY_TEST_ONLY/marker.txt", "synthetic fixture")
            companion = Path(f"{project_zip}.sha256")
            companion.write_text(
                f"{factory.sha(project_zip)}  {project_zip.name}\n", encoding="utf-8"
            )
            validation = factory.validate_external_project_artifacts(
                project_zip, companion
            )
        self.assertEqual("PASS", validation["result"])
        self.assertFalse(validation["required"])
        self.assertEqual(
            "NOT_APPLICABLE_NON_CANONICAL_TEMP_ZIP",
            validation["external_artifacts"],
        )

    def test_canonical_zip_without_external_artifacts_stays_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project_zip = root / "IDUNEX_PROJECT_SYNTHETIC_v1.0.0.zip"
            with zipfile.ZipFile(project_zip, "w", zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("IDUNEX_PROJECT_SYNTHETIC_v1.0.0/marker.txt", "non-delivery fixture")
            companion = project_zip.with_suffix(".zip.sha256")
            companion.write_text(f"{factory.sha(project_zip)}  {project_zip.name}\n", encoding="utf-8")
            result = factory.validate_reopened_zip(project_zip, companion)
        self.assertTrue(factory._canonical_external_artifacts_required(project_zip))
        self.assertEqual("FAIL", result["result"])
        self.assertIn("FAIL_EXTERNAL_ARTIFACT_SET_5_OF_5", result["fail_codes"])


if __name__ == "__main__":
    unittest.main()
