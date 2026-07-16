import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.windows_path_remap_check import (
    H62_SAFE,
    audit_repository,
    h62_original_path,
    load_remap_table,
    scan_stale_references,
    validate_table,
)


REPO_ROOT = Path(__file__).resolve().parents[2]


class WindowsPathRemapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = load_remap_table(REPO_ROOT)
        cls.h62_original = h62_original_path(cls.table)

    def test_canonical_table_is_bijective_and_materialised(self):
        self.assertEqual(self.table.declared_count, 487)
        self.assertEqual(len(self.table.entries), 487)
        self.assertEqual(validate_table(REPO_ROOT, self.table), [])

    def test_resolver_supports_repository_and_engine_relative_paths(self):
        self.assertEqual(self.table.resolve(self.h62_original), H62_SAFE)
        self.assertEqual(
            self.table.resolve(self.h62_original.removeprefix("engine/IDUNEX/")),
            H62_SAFE.removeprefix("engine/IDUNEX/"),
        )

    def test_stale_reference_scanner_rejects_original_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rogue = root / "engine" / "IDUNEX" / "ROGUE.json"
            rogue.parent.mkdir(parents=True)
            rogue.write_text(json.dumps({"path": self.h62_original}), encoding="utf-8")
            findings = scan_stale_references(root, self.table)
        self.assertEqual([item["path"] for item in findings], ["engine/IDUNEX/ROGUE.json"])

    def test_repository_remap_integrity(self):
        report = audit_repository(REPO_ROOT)
        self.assertEqual(report["result"], "PASS", json.dumps(report, indent=2))
        self.assertEqual(report["engine_mapping_count"], 475)
        self.assertEqual(report["materialised_original_path_count"], 0)
        self.assertEqual(report["missing_indexed_path_count"], 0)
        self.assertEqual(report["stale_reference_count"], 0)
        self.assertTrue(report["h62_safe_path_exists"])
        self.assertTrue(all(report["h62_consumers_windows_safe"].values()))

    def test_cli_returns_machine_readable_pass(self):
        result = subprocess.run(
            [
                sys.executable,
                "tools/audit/windows_path_remap_check.py",
                "--repo-root",
                ".",
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["result"], "PASS")


if __name__ == "__main__":
    unittest.main()
