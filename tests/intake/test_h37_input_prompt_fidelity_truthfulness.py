import json
import tempfile
import unittest
from pathlib import Path

from tests.intake.post_demo_support import control_spec, load_factory, read_json


class H37TruthfulnessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = load_factory("idunex_h37_truthfulness")

    def test_alias_rows_require_operational_resolution(self):
        with tempfile.TemporaryDirectory(prefix="idunex_h37_") as td:
            project = self.factory.make_project(control_spec(), Path(td))
            ledger = read_json(project / "01_CANON/INPUT_PROMPT_FIDELITY_LEDGER.json")
            rows = [r for r in ledger["rows"] if r["input_field_path"].endswith((".aliases", ".pseudonym"))]
            self.assertEqual(ledger["result"], "PASS")
            self.assertTrue(rows)
            self.assertTrue(all(r["operational_resolution_status"] == "PASS" for r in rows))

    def test_false_pass_is_detected_when_resolver_loses_original_alias(self):
        with tempfile.TemporaryDirectory(prefix="idunex_h37_mutation_") as td:
            project = self.factory.make_project(control_spec(), Path(td))
            resolver_path = project / "00_PROJECT_INDEX/PROJECT_ALIAS_RESOLVER.json"
            resolver = read_json(resolver_path)
            resolver["aliases"].pop("vale")
            resolver_path.write_text(json.dumps(resolver, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            index = read_json(project / "00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json")
            codes = {x["fail_code"] for x in self.factory.validate_post_demo_required_surfaces(project, index)}
            self.assertIn("FAIL_ALIAS_SELECTOR_NOT_OPERATIONAL", codes)


if __name__ == "__main__":
    unittest.main()
