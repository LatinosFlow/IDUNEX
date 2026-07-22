"""Synthetic coverage for AUD-030 external documentary refresh."""
import json
import io
import contextlib
import sys
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from unittest import mock

from tests.intake.post_demo_support import load_factory

sys.dont_write_bytecode = True

CONTENT_TREE = "8" * 64
STALE_TREE = "3" * 64
ROOT_NAME = "IDUNEX_PROJECT_SYNTHETIC_v1.0.0"


class ExternalArtifactRefreshTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = load_factory("idunex_external_artifact_refresh")

    def _create_zip(
        self,
        directory: Path,
        *,
        report_tree: str = CONTENT_TREE,
        certificate_tree: str = CONTENT_TREE,
        proof_tree: str = CONTENT_TREE,
        finalizer_tree: str = CONTENT_TREE,
        omitted: set[str] | None = None,
        filename: str = f"{ROOT_NAME}.zip",
    ) -> tuple[Path, Path]:
        omitted = omitted or set()
        members = {
            "10_RELEASE/FINAL_AUDIT_REPORT.md": (
                f"# Synthetic internal report\ncontent_tree_sha256={report_tree}\n"
            ),
            "10_RELEASE/RELEASE_CERTIFICATE.txt": (
                f"PROJECT_ID={ROOT_NAME}\nCONTENT_TREE_SHA256={certificate_tree}\n"
            ),
            "00_PROJECT_INDEX/README_FOR_HUMAN_OPERATOR.md": (
                "# Synthetic internal operator README\nUse only synthetic fixtures.\n"
            ),
            "09_MANIFESTS_SHA/POST_EXPORT_FINALIZER_REPORT.json": json.dumps(
                {"result": "PASS", "content_tree_sha256": finalizer_tree}
            ),
            "09_MANIFESTS_SHA/CONTENT_TREE_PROOF_NOT_FINAL_ZIP_SHA.json": json.dumps(
                {"result": "PASS", "content_tree_sha256": proof_tree}
            ),
        }
        project_zip = directory / filename
        with zipfile.ZipFile(project_zip, "w", zipfile.ZIP_DEFLATED) as archive:
            for relative, content in members.items():
                if relative not in omitted:
                    archive.writestr(f"{ROOT_NAME}/{relative}", content)
            archive.writestr(f"{ROOT_NAME}/synthetic_payload.txt", "fixture only")
        companion = Path(f"{project_zip}.sha256")
        companion.write_text(
            f"{self.factory.sha(project_zip)}  {project_zip.name}\n", encoding="utf-8"
        )
        return project_zip, companion

    def _synthetic_reopened_validation(self, project_zip: Path, companion: Path) -> dict:
        external = self.factory.validate_external_project_artifacts(project_zip, companion)
        return {
            "result": external["result"],
            "delivery_status": (
                "DELIVERY_ALLOWED" if external["result"] == "PASS" else "DELIVERY_BLOCKED"
            ),
            "validators_fail": external.get("validators_fail", 0),
            "blocking_warnings": 0,
            "fail_codes": external.get("fail_codes", []),
            "EXTERNAL_ARTIFACTS_5_OF_5": (
                "PASS" if external.get("required") and external["result"] == "PASS"
                else "NOT_APPLICABLE_TEMP_ZIP"
            ),
            "external_artifacts": external,
        }

    def _refresh(self, project_zip: Path) -> tuple[dict, mock.Mock]:
        validator = mock.Mock(side_effect=self._synthetic_reopened_validation)
        with mock.patch.object(self.factory, "validate_reopened_zip", validator):
            result = self.factory.refresh_external_project_artifacts(project_zip)
        return result, validator

    def test_01_refresh_derives_three_surfaces_from_final_zip(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, _ = self._create_zip(Path(td))
            result, validator = self._refresh(project_zip)
            paths = self.factory._external_project_artifact_paths(project_zip)
            sources = self.factory.read_external_project_artifact_sources_from_zip(project_zip)
            self.assertEqual("PASS", result["result"], result)
            self.assertTrue(
                paths["release_certificate"].read_text(encoding="utf-8").endswith(
                    sources["release_certificate"].rstrip() + "\n"
                )
            )
            self.assertTrue(
                paths["final_audit_report"].read_text(encoding="utf-8").endswith(
                    sources["final_audit_report"].rstrip() + "\n"
                )
            )
            self.assertTrue(
                paths["readme_for_human_operator"].read_text(encoding="utf-8").endswith(
                    sources["readme_for_human_operator"].rstrip() + "\n"
                )
            )
            validator.assert_called_once()

    def test_02_internal_report_certificate_tree_mismatch_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, _ = self._create_zip(
                Path(td), report_tree=CONTENT_TREE, certificate_tree=STALE_TREE
            )
            result = self.factory.refresh_external_project_artifacts(project_zip)
            self.assertEqual("FAIL", result["result"])
            self.assertIn(
                "FAIL_EXTERNAL_ARTIFACT_INTERNAL_CONTENT_TREE_MISMATCH",
                result["fail_codes"],
            )

    def test_03_stale_external_report_tree_blocks_validator(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, companion = self._create_zip(Path(td))
            result, _ = self._refresh(project_zip)
            self.assertEqual("PASS", result["result"], result)
            report = self.factory._external_project_artifact_paths(project_zip)[
                "final_audit_report"
            ]
            report.write_text(
                report.read_text(encoding="utf-8").replace(CONTENT_TREE, STALE_TREE),
                encoding="utf-8",
            )
            validation = self.factory.validate_external_project_artifacts(
                project_zip, companion
            )
            self.assertEqual("FAIL", validation["result"])
            self.assertIn(
                "FAIL_EXTERNAL_ARTIFACT_CONTENT_TREE_MISMATCH",
                validation["fail_codes"],
            )

    def test_04_missing_internal_source_blocks_refresh(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, _ = self._create_zip(
                Path(td), omitted={"00_PROJECT_INDEX/README_FOR_HUMAN_OPERATOR.md"}
            )
            result = self.factory.refresh_external_project_artifacts(project_zip)
            self.assertEqual("FAIL", result["result"])
            self.assertIn(
                "FAIL_EXTERNAL_ARTIFACT_INTERNAL_SOURCE_MISSING", result["fail_codes"]
            )

    def test_05_mismatching_companion_blocks_refresh(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, companion = self._create_zip(Path(td))
            companion.write_text(f"{'0' * 64}  {project_zip.name}\n", encoding="utf-8")
            result = self.factory.refresh_external_project_artifacts(project_zip)
            self.assertEqual("FAIL", result["result"])
            self.assertIn("FAIL_EXTERNAL_ARTIFACT_SHA_MISMATCH", result["fail_codes"])

    def test_06_zip_sha_and_size_are_unchanged(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, _ = self._create_zip(Path(td))
            before = (self.factory.sha(project_zip), project_zip.stat().st_size)
            result, _ = self._refresh(project_zip)
            after = (self.factory.sha(project_zip), project_zip.stat().st_size)
            self.assertEqual(before, after)
            self.assertTrue(result["ZIP_UNCHANGED"], result)
            self.assertEqual(
                result["project_zip_sha256_before"], result["project_zip_sha256_after"]
            )

    def test_07_companion_sha_and_size_are_unchanged(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, companion = self._create_zip(Path(td))
            before = (self.factory.sha(companion), companion.stat().st_size)
            result, _ = self._refresh(project_zip)
            after = (self.factory.sha(companion), companion.stat().st_size)
            self.assertEqual(before, after)
            self.assertTrue(result["COMPANION_UNCHANGED"], result)
            self.assertEqual(
                result["companion_sha256_before"], result["companion_sha256_after"]
            )

    def test_08_final_external_set_is_5_of_5(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, companion = self._create_zip(Path(td))
            result, _ = self._refresh(project_zip)
            validation = self.factory.validate_external_project_artifacts(
                project_zip, companion
            )
            self.assertEqual("PASS", result["EXTERNAL_ARTIFACTS_5_OF_5"], result)
            self.assertEqual("PASS", validation["result"], validation)
            self.assertEqual(5, validation["artifact_count"])

    def test_09_noncanonical_zip_remains_not_applicable(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, companion = self._create_zip(
                Path(td), filename="synthetic-noncanonical.zip"
            )
            validation = self.factory.validate_external_project_artifacts(
                project_zip, companion
            )
            self.assertEqual("PASS", validation["result"])
            self.assertFalse(validation["required"])
            self.assertEqual(
                "NOT_APPLICABLE_NON_CANONICAL_TEMP_ZIP",
                validation["external_artifacts"],
            )

    def test_10_duplicate_or_ambiguous_zip_member_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, _ = self._create_zip(Path(td))
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                with zipfile.ZipFile(project_zip, "a", zipfile.ZIP_DEFLATED) as archive:
                    archive.writestr(
                        f"{ROOT_NAME}/10_RELEASE/FINAL_AUDIT_REPORT.md",
                        f"content_tree_sha256={CONTENT_TREE}\n",
                    )
            Path(f"{project_zip}.sha256").write_text(
                f"{self.factory.sha(project_zip)}  {project_zip.name}\n", encoding="utf-8"
            )
            result = self.factory.refresh_external_project_artifacts(project_zip)
            self.assertEqual("FAIL", result["result"])
            self.assertIn("FAIL_EXTERNAL_ARTIFACT_ZIP_UNSAFE", result["fail_codes"])

    def test_11_cli_persists_required_result_json(self):
        with tempfile.TemporaryDirectory() as td:
            project_zip, _ = self._create_zip(Path(td))
            result_json = Path(td) / "refresh-result.json"
            validator = mock.Mock(side_effect=self._synthetic_reopened_validation)
            argv = [
                str(self.factory.__file__),
                "refresh-external-artifacts",
                str(project_zip),
                "--output-json",
                str(result_json),
            ]
            with (
                mock.patch.object(self.factory, "validate_reopened_zip", validator),
                mock.patch.object(sys, "argv", argv),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                return_code = self.factory.main()
            payload = json.loads(result_json.read_text(encoding="utf-8"))
            self.assertEqual(0, return_code)
            self.assertEqual("PASS", payload["result"])
            self.assertTrue(payload["ZIP_UNCHANGED"])
            self.assertTrue(payload["COMPANION_UNCHANGED"])
            self.assertFalse(payload["CREATIVE_OUTPUT_CERTIFIED"])


if __name__ == "__main__":
    unittest.main()
