import tempfile
import unittest
from pathlib import Path

from tests.intake.post_demo_support import control_spec, load_factory, read_json


class ProjectAliasResolverOperationalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = load_factory("idunex_alias_operational")

    def test_aliases_and_pseudonyms_resolve_in_registry_runtime_and_qa(self):
        with tempfile.TemporaryDirectory(prefix="idunex_alias_") as td:
            project = self.factory.make_project(control_spec(), Path(td))
            index = read_json(project / "00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json")
            resolver = read_json(project / "00_PROJECT_INDEX/PROJECT_ALIAS_RESOLVER.json")
            mids = {row["name"]: row["model_id"] for row in index["models"]}
            self.assertEqual(resolver["aliases"]["vale"], mids["Valeria Rios Andrade"])
            self.assertEqual(resolver["aliases"]["mateo"], mids["Mateo Vargas Salinas"])
            self.assertEqual(self.factory.validate_post_demo_required_surfaces(project, index), [])

    def test_unknown_and_ambiguous_policy_blocks(self):
        with tempfile.TemporaryDirectory(prefix="idunex_alias_policy_") as td:
            project = self.factory.make_project(control_spec(), Path(td))
            resolver = read_json(project / "00_PROJECT_INDEX/PROJECT_ALIAS_RESOLVER.json")
            self.assertEqual(resolver["unknown_alias_behavior"], "BLOCK_AND_REQUEST_PRECISION")
            self.assertEqual(resolver["ambiguous_alias_behavior"], "BLOCK_AND_REQUEST_PRECISION")


if __name__ == "__main__":
    unittest.main()
