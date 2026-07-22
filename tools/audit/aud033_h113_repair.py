#!/usr/bin/env python3
"""Temporary AUD-033 repair executor. Remove before merge."""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FACTORY = ROOT / "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py"
RUNNER = ROOT / "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py"
CHANGELOG = ROOT / "engine/IDUNEX/00_INDEX/CHANGELOG.md"
TEST = ROOT / "tests/intake/test_h113_current_tree_identity_generate.py"
AUDIT = ROOT / "docs/audits/GOV-IDUNEX-CorreccionResolucionIdentidadH113-20260722-v1-EN_REVISION.md"
STATE = ROOT / "governance/CURRENT_STATE.json"
REPO_MANIFEST = ROOT / "REPOSITORY_MANIFEST.yml"
BASE_COMMIT = "7852cea334d3e94d6c3821e2db516ae6bc8b8cd8"


def replace_idempotent(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"AUD033_EXACT_REPLACEMENT_BLOCKED:{path}:{count}")
    path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")


def patch_sources() -> None:
    replace_idempotent(
        FACTORY,
        '''            and state.get("motor_status")=="EN_REVISION"\n            and state.get("m02_result")=="M02_PASS"\n            and state.get("release_authorized") is False\n''',
        '''            and state.get("motor_status")=="EN_REVISION"\n            and isinstance(state.get("engine_change_control"), dict)\n            and state["engine_change_control"].get("current_engine_tree_sha256")==token\n            and state["engine_change_control"].get("current_engine_file_count")==manifest.get("file_count")\n            and state["engine_change_control"].get("current_engine_byte_count")==manifest.get("byte_count")\n            and state.get("release_authorized") is False\n''',
    )
    replace_idempotent(
        RUNNER,
        '''    row["generate_result"] = gen.get("result")\n    row["generated_zip"] = gen.get("project_zip")\n    row["generated_companion"] = gen.get("companion")\n''',
        '''    row["generate_result"] = gen.get("result")\n    row["generate_fail_codes"] = list(gen.get("fail_codes") or [])\n    row["generate_root_cause_fail_codes"] = list(gen.get("root_cause_fail_codes") or [])\n    row["generate_root_cause_phase"] = gen.get("root_cause_phase")\n    row["generate_root_cause_detail"] = gen.get("root_cause_detail")\n    row["generate_stdout_tail"] = (gen_stdout or "")[-4000:]\n    row["generate_stderr_tail"] = (gen_stderr or "")[-4000:]\n    if row["generate_result"] != "PASS" and row["generate_fail_codes"]:\n        row["fail_codes"].extend(code for code in row["generate_fail_codes"] if code not in row["fail_codes"])\n    row["generated_zip"] = gen.get("project_zip")\n    row["generated_companion"] = gen.get("companion")\n''',
    )
    marker = "- 2026-07-22 — AUD-033: H113 repository current-tree identity resolution decoupled from M02 approval; identity remains non-release and governance interlocks remain authoritative.\n"
    changelog = CHANGELOG.read_text(encoding="utf-8")
    if marker not in changelog:
        CHANGELOG.write_text(changelog.rstrip() + "\n" + marker, encoding="utf-8", newline="\n")


def write_test() -> None:
    TEST.write_text('''from __future__ import annotations

import hashlib
import json
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
SENTINEL = "ENGINE_ZIP_SHA256_EXTERNAL_COMPANION_REQUIRED"


class H113CurrentTreeIdentityGenerateTest(unittest.TestCase):
    def test_non_release_current_tree_identity_generates_n1_without_circular_m02_dependency(self):
        baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["motor_status"], "EN_REVISION")
        self.assertEqual(state["m02_result"], "NOT_RECOMPUTED_POST_AUD030")
        self.assertFalse(state["release_authorized"])
        self.assertFalse(state["tag_authorized"])
        self.assertEqual(state["engine_change_control"]["current_engine_tree_sha256"], baseline["tree_sha256"])
        self.assertEqual(state["engine_change_control"]["current_engine_file_count"], baseline["file_count"])
        self.assertEqual(state["engine_change_control"]["current_engine_byte_count"], baseline["byte_count"])

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "input.json"
            output_dir = root / "output"
            result_path = root / "generate.json"
            input_path.write_text(json.dumps({
                "project_id": "IDUNEX_PROJECT_AUD033_H113_N1_v1.0.0",
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
''', encoding="utf-8", newline="\n")


def write_audit() -> None:
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text('''# GOV-IDUNEX — Corrección de resolución de identidad H113

Fecha: 2026-07-22  
Versión documental: v1  
Estado: EN_REVISION  
Control: AUD-033 / issue #64

## Hallazgo validado

El run M02 `29936388876` obtuvo 0/30. El diagnóstico sintético `29937730988` aisló `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE` con detalle `certificate engine sha invalid`.

La causa fue una dependencia circular en `resolve_engine_zip_sha256()`: la identidad AUD-003 del repositorio solo se aceptaba cuando `M02_RESULT=M02_PASS`, aunque M02 necesita generar la matriz antes de recomputar ese resultado.

## Corrección

La identidad no-release se acepta únicamente cuando coinciden el companion AUD-003, el manifiesto físico y `engine_change_control` en SHA, conteo y bytes; además el motor debe permanecer `EN_REVISION` y release/tag deben seguir bloqueados.

Identidad criptográfica no equivale a autorización operativa. Demo, generación general, agentes, release, tag, OFICIAL y cierre productivo continúan bloqueados.

## Evidencia requerida

- prueba integral sintética N1;
- certificado sin sentinel diferido;
- ZIP y companion válidos;
- baseline, governance, intake, security y runtime validator PASS;
- M02 y M03 no recomputados hasta ejecuciones completas nuevas.

## Reversión

Revertir el commit correctivo completo. No se modifica el ZIP real del Proyecto 000 Demo.
''', encoding="utf-8", newline="\n")


def regenerate_and_sync() -> dict:
    scanner_path = ROOT / "tools/audit/baseline_scanner.py"
    spec = importlib.util.spec_from_file_location("aud033_baseline_scanner", scanner_path)
    scanner = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(scanner)
    payload = scanner.write_artifacts(ROOT)

    state = json.loads(STATE.read_text(encoding="utf-8"))
    engine_change = state.setdefault("engine_change_control", {})
    prior_tree = engine_change.get("current_engine_tree_sha256")
    engine_change.update({
        "previous_current_engine_tree_sha256": prior_tree,
        "current_engine_tree_sha256": payload["tree_sha256"],
        "current_engine_file_count": payload["file_count"],
        "current_engine_byte_count": payload["byte_count"],
        "manifests_recomputed_with_canonical_scanner": True,
        "subsequent_correction_issue": "AUD-033",
        "subsequent_correction_base_commit": BASE_COMMIT,
        "subsequent_correction_reason": "H113_CURRENT_TREE_IDENTITY_RESOLUTION",
        "m02_result": state.get("m02_result"),
        "m03_result": state.get("m03_result"),
    })
    state["last_correction_issue"] = "AUD-033"
    state["last_failed_m02_run"] = 29936388876
    state["last_diagnostic_run"] = 29937730988
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    text = REPO_MANIFEST.read_text(encoding="utf-8")
    if "current_repository_commit_at_aud033_base:" not in text:
        text = text.replace(
            "  current_repository_commit_at_aud031_base: 2790468f6b3bcc5286761def779276e8a77b6d20\n",
            "  current_repository_commit_at_aud031_base: 2790468f6b3bcc5286761def779276e8a77b6d20\n"
            f"  current_repository_commit_at_aud033_base: {BASE_COMMIT}\n",
        )
    text = re.sub(r"(?m)^  file_count: \d+$", f"  file_count: {payload['file_count']}", text, count=1)
    text = re.sub(r"(?m)^  bytes: \d+$", f"  bytes: {payload['byte_count']}", text, count=1)
    text = re.sub(r"(?m)^  tree_sha256: [0-9a-f]{64}$", f"  tree_sha256: {payload['tree_sha256']}", text, count=1)
    if "aud033_h113_current_tree_identity:" not in text:
        text = text.rstrip() + f'''\n\naud033_h113_current_tree_identity:
  controlling_issue: 64
  source_m02_run_id: 29936388876
  diagnostic_run_id: 29937730988
  base_commit: {BASE_COMMIT}
  previous_engine_tree_sha256: {prior_tree}
  current_engine_tree_sha256: {payload["tree_sha256"]}
  current_engine_file_count: {payload["file_count"]}
  current_engine_bytes: {payload["byte_count"]}
  status: IMPLEMENTED_PENDING_PR_REVIEW
  root_failcode: FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE
  m02_result: NOT_RECOMPUTED_POST_AUD030
  m03_result: NOT_RECOMPUTED_POST_AUD030
  demo_executed: false
  refresh_external_artifacts_executed: false
  release_authorized: false
  tag_authorized: false
  oficial_authorized: false
  agent_load_authorized: false
  creative_output_certified: false
'''
    REPO_MANIFEST.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    return payload


def main() -> int:
    patch_sources()
    write_test()
    write_audit()
    payload = regenerate_and_sync()
    evidence = ROOT / ".aud033-evidence"
    evidence.mkdir(exist_ok=True)
    (evidence / "new-engine-identity.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "result": "PASS",
        "engine_tree_sha256": payload["tree_sha256"],
        "engine_file_count": payload["file_count"],
        "engine_byte_count": payload["byte_count"],
        "m02_result": "NOT_RECOMPUTED_POST_AUD030",
        "m03_result": "NOT_RECOMPUTED_POST_AUD030",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
