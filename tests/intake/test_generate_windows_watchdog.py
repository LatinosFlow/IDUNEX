import importlib.util
import json
import os
import signal
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FACTORY_PATH = (
    REPO_ROOT
    / "engine"
    / "IDUNEX"
    / "03_PROJECT_FACTORY"
    / "02_PROTOCOLS"
    / "IDUNEX_PROJECT_FACTORY_v1.0.0.py"
)


def _load_factory():
    spec = importlib.util.spec_from_file_location("idunex_project_factory_aud004", FACTORY_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class GenerateWindowsWatchdogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.dont_write_bytecode = True
        cls.factory = _load_factory()

    def test_generate_handles_platform_without_sigalrm(self):
        original_signal = self.factory.signal
        self.factory.signal = types.SimpleNamespace(SIG_IGN=object())
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                output = Path(temp_dir) / "output"
                result = self.factory.generate_end_to_end(
                    {"project_name": "TODO"}, output
                )

                self.assertEqual(result["result"], "PASS")
                self.assertTrue(result["expected_block"])
                self.assertTrue(result["delivery_status"].startswith("BLOCKED_EARLY_EXPECTED"))
                self.assertFalse(any(output.rglob("*.zip")))
                self.assertFalse(any("PROYECTO_000_DEMO" in path.name.upper() for path in output.rglob("*")))
        finally:
            self.factory.signal = original_signal

    def test_h113_resolves_current_aud003_tree_identity_without_release_zip(self):
        manifest = json.loads(
            (
                REPO_ROOT
                / "governance"
                / "baseline"
                / "IDUNEX_CURRENT_TREE_MANIFEST.json"
            ).read_text(encoding="utf-8")
        )
        previous = os.environ.pop("IDUNEX_ENGINE_ZIP_SHA256", None)
        try:
            self.assertEqual(
                self.factory.resolve_engine_zip_sha256(), manifest["tree_sha256"]
            )
            self.assertEqual(
                manifest["baseline_class"],
                "CURRENT_CORRECTED_REPOSITORY_TREE_NOT_RELEASE",
            )
            self.assertFalse(manifest["release_authorized"])
        finally:
            if previous is not None:
                os.environ["IDUNEX_ENGINE_ZIP_SHA256"] = previous

    @unittest.skipUnless(hasattr(signal, "SIGALRM"), "Unix alarm primitives are unavailable")
    def test_sigalrm_timer_remains_enabled_when_supported(self):
        self.assertEqual(
            self.factory._h197_signal_alarm_primitives(),
            (signal.SIGALRM, signal.ITIMER_REAL),
        )

    @unittest.skipIf(hasattr(signal, "SIGALRM"), "native no-SIGALRM smoke is Windows-specific")
    def test_generate_command_returns_controlled_rc_without_sigalrm(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "blocked_input.json"
            output = root / "output"
            output_json = root / "generate_result.json"
            input_path.write_text(
                json.dumps({"project_name": "TODO"}), encoding="utf-8"
            )
            env = os.environ.copy()
            env["PYTHONDONTWRITEBYTECODE"] = "1"

            completed = subprocess.run(
                [
                    sys.executable,
                    str(FACTORY_PATH),
                    "generate",
                    "--input",
                    str(input_path),
                    "--output",
                    str(output),
                    "--output-json",
                    str(output_json),
                ],
                cwd=REPO_ROOT,
                env=env,
                check=False,
                capture_output=True,
                text=True,
                timeout=30,
            )

            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertNotIn("AttributeError", completed.stdout + completed.stderr)
            payload = json.loads(output_json.read_text(encoding="utf-8"))
            self.assertEqual(payload["result"], "PASS")
            self.assertTrue(payload["expected_block"])
            self.assertFalse(any(output.rglob("*.zip")))
            self.assertFalse(any("PROYECTO_000_DEMO" in path.name.upper() for path in output.rglob("*")))


if __name__ == "__main__":
    unittest.main()
