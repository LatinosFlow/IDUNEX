import os
import tempfile
import unittest
from pathlib import Path

from tests.intake.post_demo_support import control_spec, load_factory


class ProjectExternalArtifactsMinimumSetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = load_factory("idunex_external_artifacts")

    def test_canonical_external_artifact_set_is_5_of_5_and_mutation_blocks(self):
        with tempfile.TemporaryDirectory(prefix="idunex_external_") as td:
            old = os.environ.get("IDUNEX_ENGINE_ZIP_SHA256")
            os.environ["IDUNEX_ENGINE_ZIP_SHA256"] = "a" * 64
            try:
                out = self.factory.generate_end_to_end(control_spec(), Path(td))
            finally:
                if old is None:
                    os.environ.pop("IDUNEX_ENGINE_ZIP_SHA256", None)
                else:
                    os.environ["IDUNEX_ENGINE_ZIP_SHA256"] = old
            self.assertEqual(out["result"], "PASS", out)
            project_zip = Path(out["project_zip"])
            companion = Path(out["companion"])
            validation = self.factory.validate_external_project_artifacts(project_zip, companion)
            self.assertEqual(validation["result"], "PASS", validation)
            self.assertEqual(validation["artifact_count"], 5)
            paths = self.factory._external_project_artifact_paths(project_zip)
            paths["readme_for_human_operator"].unlink()
            mutated = self.factory.validate_reopened_zip(project_zip, companion)
            self.assertEqual(mutated["result"], "FAIL")
            self.assertIn("FAIL_EXTERNAL_ARTIFACT_SET_5_OF_5", mutated["fail_codes"])


if __name__ == "__main__":
    unittest.main()
