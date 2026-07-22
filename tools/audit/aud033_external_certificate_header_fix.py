#!/usr/bin/env python3
"""Temporary AUD-033 second-stage repair. Remove before merge."""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FACTORY = ROOT / "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py"
TEST = ROOT / "tests/intake/test_h113_current_tree_identity_generate.py"
AUDIT = ROOT / "docs/audits/GOV-IDUNEX-CorreccionResolucionIdentidadH113-20260722-v1-EN_REVISION.md"
STATE = ROOT / "governance/CURRENT_STATE.json"
REPO_MANIFEST = ROOT / "REPOSITORY_MANIFEST.yml"


def replace_idempotent(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if text.count(old) != 1:
        raise RuntimeError(f"AUD033_CERT_HEADER_REPLACEMENT_BLOCKED:{path}:{text.count(old)}")
    path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")


def patch_factory() -> None:
    replace_idempotent(
        FACTORY,
        '''    internal_cert=sources["release_certificate"]\n    internal_report=sources["final_audit_report"]\n    internal_readme=sources["readme_for_human_operator"]\n''',
        '''    internal_cert=sources["release_certificate"]\n    # AUD-033: the external envelope is the sole authority for these two\n    # validation counters. The internal certificate is still preserved, but\n    # duplicate counter lines are removed before embedding so the validator's\n    # exact-one-header contract remains satisfiable.\n    internal_cert_for_external="\\n".join(\n        line for line in internal_cert.splitlines()\n        if not re.fullmatch(r"(?:VALIDATORS_FAIL|BLOCKING_WARNINGS)=\\d+", line)\n    )\n    internal_report=sources["final_audit_report"]\n    internal_readme=sources["readme_for_human_operator"]\n''',
    )
    replace_idempotent(
        FACTORY,
        '''            "CREATIVE_OUTPUT_CERTIFIED=FALSE","NO_RELEASE_TAG_OR_OFICIAL_AUTHORIZED=TRUE","",internal_cert,\n''',
        '''            "CREATIVE_OUTPUT_CERTIFIED=FALSE","NO_RELEASE_TAG_OR_OFICIAL_AUTHORIZED=TRUE","",internal_cert_for_external,\n''',
    )


def patch_test() -> None:
    replace_idempotent(
        TEST,
        '''            self.assertEqual(companion.read_text(encoding="utf-8").split()[0], hashlib.sha256(project_zip.read_bytes()).hexdigest())\n            with zipfile.ZipFile(project_zip) as archive:\n''',
        '''            self.assertEqual(companion.read_text(encoding="utf-8").split()[0], hashlib.sha256(project_zip.read_bytes()).hexdigest())\n            external_certificate = Path(result["external_artifacts"]["release_certificate"])\n            external_certificate_text = external_certificate.read_text(encoding="utf-8")\n            self.assertEqual(len(re.findall(r"(?m)^VALIDATORS_FAIL=\\d+$", external_certificate_text)), 1)\n            self.assertEqual(len(re.findall(r"(?m)^BLOCKING_WARNINGS=\\d+$", external_certificate_text)), 1)\n            self.assertIn("VALIDATORS_FAIL=0", external_certificate_text)\n            self.assertIn("BLOCKING_WARNINGS=0", external_certificate_text)\n            with zipfile.ZipFile(project_zip) as archive:\n''',
    )
    text = TEST.read_text(encoding="utf-8")
    if "import re\n" not in text:
        text = text.replace("import json\n", "import json\nimport re\n", 1)
        TEST.write_text(text, encoding="utf-8", newline="\n")


def update_audit() -> None:
    text = AUDIT.read_text(encoding="utf-8")
    marker = '''\n## Hallazgo secuencial de contrato externo\n\nDespués de resolver H113, la prueba integral alcanzó la emisión externa y detectó `FAIL_EXTERNAL_ARTIFACT_CONTENT` con detalle `release_certificate:validation headers`. La causa era duplicación de `VALIDATORS_FAIL` y `BLOCKING_WARNINGS`: una vez en el envelope externo y otra dentro del certificado interno embebido.\n\nLa corrección conserva íntegra la autoridad interna salvo esas dos líneas de contador, que se emiten una sola vez en el envelope externo. El validator sigue exigiendo exactamente una ocurrencia de cada header y derivación byte-exacta desde el ZIP reabierto.\n'''
    if "## Hallazgo secuencial de contrato externo" not in text:
        AUDIT.write_text(text.rstrip() + marker + "\n", encoding="utf-8", newline="\n")


def regenerate_and_sync() -> dict:
    scanner_path = ROOT / "tools/audit/baseline_scanner.py"
    spec = importlib.util.spec_from_file_location("aud033_baseline_scanner_stage2", scanner_path)
    scanner = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(scanner)
    payload = scanner.write_artifacts(ROOT)

    state = json.loads(STATE.read_text(encoding="utf-8"))
    engine_change = state.setdefault("engine_change_control", {})
    engine_change.update({
        "current_engine_tree_sha256": payload["tree_sha256"],
        "current_engine_file_count": payload["file_count"],
        "current_engine_byte_count": payload["byte_count"],
        "manifests_recomputed_with_canonical_scanner": True,
        "subsequent_correction_issue": "AUD-033",
        "subsequent_correction_reason": "H113_IDENTITY_AND_EXTERNAL_CERTIFICATE_HEADER_PARITY",
        "m02_result": state.get("m02_result"),
        "m03_result": state.get("m03_result"),
    })
    state["last_external_certificate_contract_fix"] = "AUD-033_EXACT_ONE_VALIDATION_HEADER"
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    text = REPO_MANIFEST.read_text(encoding="utf-8")
    text = re.sub(r"(?m)^  file_count: \d+$", f"  file_count: {payload['file_count']}", text, count=1)
    text = re.sub(r"(?m)^  bytes: \d+$", f"  bytes: {payload['byte_count']}", text, count=1)
    text = re.sub(r"(?m)^  tree_sha256: [0-9a-f]{64}$", f"  tree_sha256: {payload['tree_sha256']}", text, count=1)
    text = re.sub(
        r"(?ms)(aud033_h113_current_tree_identity:.*?^  current_engine_tree_sha256: )[0-9a-f]{64}$",
        rf"\g<1>{payload['tree_sha256']}",
        text,
        count=1,
    )
    text = re.sub(
        r"(?ms)(aud033_h113_current_tree_identity:.*?^  current_engine_file_count: )\d+$",
        rf"\g<1>{payload['file_count']}",
        text,
        count=1,
    )
    text = re.sub(
        r"(?ms)(aud033_h113_current_tree_identity:.*?^  current_engine_bytes: )\d+$",
        rf"\g<1>{payload['byte_count']}",
        text,
        count=1,
    )
    if "external_certificate_validation_headers:" not in text:
        text = text.rstrip() + '''\n\nexternal_certificate_validation_headers:\n  controlling_issue: 64\n  source_failure: FAIL_EXTERNAL_ARTIFACT_CONTENT\n  source_detail: release_certificate_validation_headers\n  validators_fail_header_count: 1\n  blocking_warnings_header_count: 1\n  internal_certificate_preserved: true\n  duplicate_counter_lines_removed_before_external_embedding: true\n  status: IMPLEMENTED_PENDING_PR_REVIEW\n'''
    REPO_MANIFEST.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    return payload


def main() -> int:
    patch_factory()
    patch_test()
    update_audit()
    payload = regenerate_and_sync()
    evidence = ROOT / ".aud033-evidence"
    evidence.mkdir(exist_ok=True)
    (evidence / "new-engine-identity-stage2.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "result": "PASS",
        "engine_tree_sha256": payload["tree_sha256"],
        "engine_file_count": payload["file_count"],
        "engine_byte_count": payload["byte_count"],
        "external_certificate_validation_header_contract": "EXACTLY_ONE_EACH",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
