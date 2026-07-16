import argparse
import importlib.util
import os
import tempfile
import unittest
from contextlib import contextmanager
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


@contextmanager
def working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


class CliPathNormalizationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("idunex_factory_aud010", FACTORY_PATH)
        cls.factory = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.factory)

    def test_update_cli_relative_and_absolute_paths_have_one_representation(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            project = root / "project input"
            update = root / "contracts" / "update.json"
            output = root / "output"
            evidence = root / "evidence" / "result.json"
            project.mkdir()
            update.parent.mkdir()
            update.write_text("{}", encoding="utf-8")

            with working_directory(root):
                relative_args = argparse.Namespace(
                    cmd="update-project",
                    project=Path("project input"),
                    update=Path("contracts") / "update.json",
                    output=Path("output"),
                    output_json=Path("evidence") / "result.json",
                )
                self.factory._normalize_related_cli_paths(relative_args)

            absolute_args = argparse.Namespace(
                cmd="update-project",
                project=project.resolve(),
                update=update.resolve(),
                output=output.resolve(),
                output_json=evidence.resolve(),
            )
            self.factory._normalize_related_cli_paths(absolute_args)

            for attribute in ("project", "update", "output", "output_json"):
                relative_value = getattr(relative_args, attribute)
                absolute_value = getattr(absolute_args, attribute)
                self.assertIsInstance(relative_value, Path)
                self.assertTrue(relative_value.is_absolute())
                self.assertEqual(relative_value, absolute_value)

    def test_migrate_commands_normalize_project_output_and_evidence_paths(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            with working_directory(root):
                for command in ("migrate-project", "update-project-by-engine"):
                    with self.subTest(command=command):
                        args = argparse.Namespace(
                            cmd=command,
                            project="project",
                            output="output",
                            output_json=str(Path("evidence") / f"{command}.json"),
                        )
                        self.factory._normalize_related_cli_paths(args)
                        self.assertEqual(args.project, (root / "project").resolve())
                        self.assertEqual(args.output, (root / "output").resolve())
                        self.assertEqual(
                            args.output_json,
                            (root / "evidence" / f"{command}.json").resolve(),
                        )

    @unittest.skipUnless(os.name == "nt", "Windows separator behavior is platform-specific")
    def test_windows_separators_are_resolved_at_the_cli_boundary(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            expected = root / "nested" / "project"
            expected.mkdir(parents=True)
            with working_directory(root):
                args = argparse.Namespace(
                    cmd="migrate-project",
                    project=r"nested\project",
                    output=r"nested\output",
                    output_json=None,
                )
                self.factory._normalize_related_cli_paths(args)
            self.assertEqual(args.project, expected.resolve())
            self.assertEqual(args.output, (root / "nested" / "output").resolve())

    def test_relative_project_root_can_emit_internal_evidence_paths(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            model_dir = root / "project" / "02_MODELS" / "MODEL_001"
            model_dir.mkdir(parents=True)
            marker = model_dir / "marker.txt"
            marker.write_text("old value", encoding="utf-8")

            with working_directory(root):
                touched, scanned = self.factory._apply_semantic_replacements_limited(
                    Path("project"),
                    [("old value", "new value")],
                    [Path("project") / "02_MODELS" / "MODEL_001"],
                )

            relative_marker = "02_MODELS/MODEL_001/marker.txt"
            self.assertEqual(touched, [relative_marker])
            self.assertEqual(scanned, [relative_marker])
            self.assertEqual(marker.read_text(encoding="utf-8").strip(), "new value")

    def test_semantic_replacement_rejects_escape_outside_project_root(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            project = root / "project"
            outside = root / "outside"
            project.mkdir()
            outside.mkdir()
            (outside / "marker.txt").write_text("old value", encoding="utf-8")

            with self.assertRaises(self.factory.InputContractError) as caught:
                self.factory._apply_semantic_replacements_limited(
                    project,
                    [("old value", "new value")],
                    [project / ".." / "outside"],
                )
            self.assertEqual(caught.exception.fail_code, "FAIL_CLI_PATH_OUTSIDE_PROJECT_ROOT")

    def test_project_copy_normalizes_relative_source_and_output(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            project = root / "project"
            project.mkdir()
            (project / "manifest.json").write_text("{}", encoding="utf-8")

            with working_directory(root):
                destination, temporary_directories = self.factory._copy_project_source(
                    Path("project"), Path("relative output")
                )

            self.assertEqual(temporary_directories, [])
            self.assertTrue(destination.is_absolute())
            self.assertEqual(destination, (root / "relative output" / "project").resolve())
            self.assertTrue((destination / "manifest.json").is_file())


if __name__ == "__main__":
    unittest.main()
