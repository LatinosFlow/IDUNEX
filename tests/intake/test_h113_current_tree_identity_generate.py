from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FACTORY = REPO_ROOT / "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py"
BASELINE = REPO_ROOT / "governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json"
STATE = REPO_ROOT / "governance/CURRENT_STATE.json"
REPOSITORY_MANIFEST = REPO_ROOT / "REPOSITORY_MANIFEST.yml"
SENTINEL = "ENGINE_ZIP_SHA256_EXTERNAL_COMPANION_REQUIRED"


class H113CurrentTreeIdentityGenerateTest(unittest.TestCase):
    def test_non_release_current_tree_identity_generates_n1_without_circular_m02_dependency(self):
        baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        state = json.loads(STATE.read_text(encoding="utf-8"))
        repository_manifest = REPOSITORY_MANIFEST.read_text(encoding="utf-8")
        self.assertEqual(state["issue"], "AUD-035")
        self.assertEqual(state["motor_status"], "EN_REVISION")
        self.assertEqual(state["m02_result"], "NOT_RECOMPUTED_POST_AUD035")
        self.assertEqual(state["m03_result"], "NOT_RECOMPUTED_POST_AUD035")
        self.assertFalse(state["release_authorized"])
        self.assertFalse(state["tag_authorized"])
        self.assertFalse(state["oficial_authorized"])
        self.assertFalse(state["agent_load_authorized"])
        self.assertFalse(state["creative_output_certified"])
        self.assertEqual(state["engine_change_control"]["current_engine_tree_sha256"], baseline["tree_sha256"])
        self.assertEqual(state["engine_change_control"]["current_engine_file_count"], baseline["file_count"])
        self.assertEqual(state["engine_change_control"]["current_engine_byte_count"], baseline["byte_count"])

        historical = re.search(
            r"historical_received_baseline:\n(?:.*\n)*?  bytes: (\d+)\n",
            repository_manifest,
        )
        current = re.search(
            r"current_corrected_tree:\n(?:.*\n)*?  file_count: (\d+)\n"
            r"  bytes: (\d+)\n  tree_sha256: ([0-9a-f]{64})\n",
            repository_manifest,
        )
        self.assertIsNotNone(historical)
        self.assertIsNotNone(current)
        self.assertEqual(int(historical.group(1)), 4_277_381)
        self.assertEqual(int(current.group(1)), baseline["file_count"])
        self.assertEqual(int(current.group(2)), baseline["byte_count"])
        self.assertEqual(current.group(3), baseline["tree_sha256"])

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "input.json"
            output_dir = root / "output"
            result_path = root / "generate.json"
            input_path.write_text(json.dumps({
                "project_id": "IDUNEX_PROJECT_AUD035_H113_N1_v1.0.0",
                "models": [{}],
            }), encoding="utf-8")
            completed = subprocess.run([
                sys.executable, "-B", str(FACTORY), "generate",
                "--input", str(input_path),
                "--output", str(output_dir),
                "--summary",
                "--output-json", str(result_path),
            ], cwd=REPO_ROOT, check=False, capture_output=True, text=True, timeout=180)
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            result = json.loads(result_path.read_text(encoding="utf-8"))
            self.assertEqual(result["result"], "PASS", result)
            self.assertEqual(result.get("fail_codes"), [])
            project_zip = Path(result["project_zip"])
            companion = Path(result["companion"])
            self.assertTrue(project_zip.is_file())
            self.assertTrue(companion.is_file())
            self.assertEqual(companion.read_text(encoding="utf-8").split()[0], hashlib.sha256(project_zip.read_bytes()).hexdigest())
            external_certificate = Path(result["external_artifacts"]["release_certificate"])
            external_certificate_text = external_certificate.read_text(encoding="utf-8")
            self.assertEqual(len(re.findall(r"(?m)^VALIDATORS_FAIL=\d+$", external_certificate_text)), 1)
            self.assertEqual(len(re.findall(r"(?m)^BLOCKING_WARNINGS=\d+$", external_certificate_text)), 1)
            self.assertIn("VALIDATORS_FAIL=0", external_certificate_text)
            self.assertIn("BLOCKING_WARNINGS=0", external_certificate_text)
            with zipfile.ZipFile(project_zip) as archive:
                self.assertIsNone(archive.testzip())
                cert_name = next(name for name in archive.namelist() if name.endswith("10_RELEASE/IDUNEX_PROJECT_CERTIFICATE.json"))
                certificate = json.loads(archive.read(cert_name))
            self.assertEqual(certificate["engine_zip_sha"], baseline["tree_sha256"])
            self.assertEqual(certificate["engine_zip_sha256"], baseline["tree_sha256"])
            self.assertNotEqual(certificate["engine_zip_sha"], SENTINEL)
            self.assertEqual(certificate["H113_POST_EXPORT_FINALIZER_SHA_PROOF_CERTIFICATE"], "PASS")
            self.assertFalse(certificate["CREATIVE_OUTPUT_CERTIFIED"])


if __name__ == "__main__":
    unittest.main()
