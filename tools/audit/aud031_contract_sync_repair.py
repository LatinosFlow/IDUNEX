#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OLD_SHA = "8a3c191c266647acd754a56c1e5555ca1a36ab807d2e04e72a5ff21edb3e92bd"
OLD_BYTES = 47_321_777
PENDING = "NOT_RECOMPUTED_POST_AUD030"
BASE_COMMIT = "2790468f6b3bcc5286761def779276e8a77b6d20"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    contract_path = ROOT / "engine/IDUNEX/07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json"
    contract = read_json(contract_path)
    expected = contract.get("expected_current_state")
    if not isinstance(expected, dict):
        raise SystemExit("AUD031_BLOCKED_EXPECTED_CURRENT_STATE_MISSING")
    if expected.get("M02_RESULT") not in {"M02_PASS", PENDING}:
        raise SystemExit(f"AUD031_BLOCKED_UNEXPECTED_M02_RESULT:{expected.get('M02_RESULT')!r}")
    expected["M02_RESULT"] = PENDING
    contract["last_sync_issue"] = "AUD-031"
    contract["last_sync_source_run"] = 29928852782
    contract["last_sync_reason"] = "MASTER_GOVERNANCE_VALIDATION_CONTRACT_POST_AUD030_PARITY"
    contract["interlock"] = (
        "M02_FAIL or NOT_RECOMPUTED_POST_AUD030 prevents any internal certificate "
        "from enabling Demo, release, tag, OFICIAL, agent loading or productive closure."
    )
    write_json(contract_path, contract)

    subprocess.run(
        [sys.executable, "tools/audit/baseline_scanner.py", "--repo-root", ".", "--write"],
        cwd=ROOT,
        check=True,
    )

    manifest_path = ROOT / "governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json"
    manifest = read_json(manifest_path)
    new_sha = manifest.get("tree_sha256")
    new_count = manifest.get("file_count")
    new_bytes = manifest.get("byte_count")
    if not isinstance(new_sha, str) or re.fullmatch(r"[0-9a-f]{64}", new_sha) is None:
        raise SystemExit("AUD031_BLOCKED_INVALID_NEW_TREE_SHA")
    if new_sha == OLD_SHA:
        raise SystemExit("AUD031_BLOCKED_TREE_IDENTITY_DID_NOT_CHANGE")
    if new_count != 981 or not isinstance(new_bytes, int) or new_bytes <= OLD_BYTES:
        raise SystemExit(f"AUD031_BLOCKED_INVALID_NEW_IDENTITY:{new_count}:{new_bytes}")

    state_path = ROOT / "governance/CURRENT_STATE.json"
    state = read_json(state_path)
    if state.get("issue") != "AUD-030":
        raise SystemExit("AUD031_BLOCKED_ROOT_STATE_AUTHORITY_CHANGED")
    if state.get("m02_result") != PENDING or state.get("m03_result") != PENDING:
        raise SystemExit("AUD031_BLOCKED_RECOMPUTATION_INTERLOCK_CHANGED")
    change = state.get("engine_change_control")
    if not isinstance(change, dict) or change.get("current_engine_tree_sha256") != OLD_SHA:
        raise SystemExit("AUD031_BLOCKED_PRIOR_ENGINE_IDENTITY_MISMATCH")
    change["previous_current_engine_tree_sha256"] = OLD_SHA
    change["current_engine_tree_sha256"] = new_sha
    change["current_engine_file_count"] = new_count
    change["current_engine_byte_count"] = new_bytes
    change["child_correction_issue"] = "AUD-031"
    change["child_correction_base_commit"] = BASE_COMMIT
    change["child_correction_reason"] = "MASTER_GOVERNANCE_VALIDATION_CONTRACT_SYNC"
    change["m02_result"] = PENDING
    change["m03_result"] = PENDING
    write_json(state_path, state)

    repository_manifest_path = ROOT / "REPOSITORY_MANIFEST.yml"
    repository_manifest = repository_manifest_path.read_text(encoding="utf-8")
    if "current_repository_commit_at_aud031_base:" not in repository_manifest:
        repository_manifest = repository_manifest.replace(
            "  current_repository_commit_at_aud030_base: fb13a4f5d4bd559b4f1268103630a735b53c8999\n",
            "  current_repository_commit_at_aud030_base: fb13a4f5d4bd559b4f1268103630a735b53c8999\n"
            f"  current_repository_commit_at_aud031_base: {BASE_COMMIT}\n",
            1,
        )
    pattern = re.compile(
        r"(current_corrected_tree:\n.*?  file_count: 981\n  bytes: )\d+(\n  tree_sha256: )[0-9a-f]{64}",
        re.DOTALL,
    )
    repository_manifest, replaced = pattern.subn(
        lambda match: f"{match.group(1)}{new_bytes}{match.group(2)}{new_sha}",
        repository_manifest,
        count=1,
    )
    if replaced != 1:
        raise SystemExit("AUD031_BLOCKED_REPOSITORY_MANIFEST_CURRENT_TREE_NOT_UPDATED")
    if "aud031_master_governance_contract_sync:" not in repository_manifest:
        repository_manifest += (
            "\naud031_master_governance_contract_sync:\n"
            "  controlling_issue: 61\n"
            "  source_workflow_run_id: 29928852782\n"
            "  source_workflow_artifact_id: 8533126155\n"
            f"  base_commit: {BASE_COMMIT}\n"
            f"  previous_engine_tree_sha256: {OLD_SHA}\n"
            f"  current_engine_tree_sha256: {new_sha}\n"
            f"  current_engine_file_count: {new_count}\n"
            f"  current_engine_bytes: {new_bytes}\n"
            "  status: IMPLEMENTED_PENDING_PR_REVIEW\n"
            f"  m02_result: {PENDING}\n"
            f"  m03_result: {PENDING}\n"
            "  demo_executed: false\n"
            "  refresh_external_artifacts_executed: false\n"
            "  release_authorized: false\n"
            "  tag_authorized: false\n"
            "  oficial_authorized: false\n"
            "  agent_load_authorized: false\n"
            "  creative_output_certified: false\n"
        )
    repository_manifest_path.write_text(repository_manifest, encoding="utf-8", newline="\n")

    replacements = {
        ROOT / ".github/workflows/m02-max.yml": [(OLD_SHA, new_sha), ("POST-PR44", "POST-AUD030")],
        ROOT / ".github/workflows/m03-adversarial.yml": [
            (OLD_SHA, new_sha),
            (f"{OLD_BYTES:_}", f"{new_bytes:_}"),
            (str(OLD_BYTES), str(new_bytes)),
            ("POST-PR44", "POST-AUD030"),
        ],
        ROOT / "tests/m03/test_adversarial_harness.py": [
            (OLD_SHA, new_sha),
            (f"{OLD_BYTES:_}", f"{new_bytes:_}"),
        ],
    }
    for path, pairs in replacements.items():
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in pairs:
            text = text.replace(old, new)
        if text == original:
            raise SystemExit(f"AUD031_BLOCKED_EXPECTED_REPLACEMENT_NOT_FOUND:{path}")
        path.write_text(text, encoding="utf-8", newline="\n")

    governance_status_path = ROOT / "GOVERNANCE_STATUS.md"
    governance_status = governance_status_path.read_text(encoding="utf-8")
    if "AUD-031" not in governance_status:
        governance_status += (
            "\n## Corrección AUD-031\n\n"
            "La primera recomputación M02 post-AUD030 quedó bloqueada antes de matriz y mutation "
            "por una expectativa heredada `M02_PASS` en el contrato activo de validación maestra. "
            "AUD-031 sincroniza esa superficie con `NOT_RECOMPUTED_POST_AUD030`, regenera los "
            "manifiestos canónicos y exige una nueva ejecución M02 completa.\n\n"
            f"- Run origen: `29928852782`;\n- árbol previo: `{OLD_SHA}`;\n"
            f"- árbol post-AUD031: `{new_sha}`;\n- M02/M03: `{PENDING}`;\n"
            "- Demo, refresh real, agentes, release, tag y OFICIAL: `BLOQUEADO`.\n"
        )
    governance_status_path.write_text(governance_status, encoding="utf-8", newline="\n")

    audit_doc = ROOT / "docs/audits/GOV-IDUNEX-SincronizacionContratoGobernanzaM02-20260722-v1-EN_REVISION.md"
    audit_doc.write_text(
        f"""# GOV-IDUNEX — Sincronización del contrato de gobernanza para M02

Fecha: 2026-07-22
Versión documental: v1
Estado: EN_REVISION
Control: AUD-031 / issue #61

## Hallazgo reproducido

El run `29928852782` reprodujo la identidad post-AUD030 y obtuvo RC 0 en los ocho controles previos. El runtime validator bloqueó con `FAIL_MASTER_GOVERNANCE_VALIDATION_CONTRACT_NOT_SYNCED` porque `MASTER_GOVERNANCE_VALIDATION_CONTRACT.json` todavía exigía `M02_PASS`. Matriz y mutation no se ejecutaron por fail-fast.

## Corrección

Se sincroniza únicamente la expectativa `M02_RESULT` del contrato activo con `{PENDING}` y se preservan todos los interlocks. No se ejecuta Demo, `generate`, validación del Demo ni refresco del artefacto real.

## Identidad

- árbol previo: `{OLD_SHA}` — 981 archivos / {OLD_BYTES:,} bytes;
- árbol post-AUD031: `{new_sha}` — {new_count} archivos / {new_bytes:,} bytes.

## Estado

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT={PENDING}
M03_RESULT={PENDING}
AUD-028=CONSUMED
PROJECT_AUDIT_STATUS=PROJECT_AUDIT_FAIL_EXTERNAL_SURFACE_DESYNC
RELEASE_AUTHORIZED=FALSE
TAG_AUTHORIZED=FALSE
OFICIAL_AUTHORIZED=FALSE
AGENT_LOAD_AUTHORIZED=FALSE
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

## Criterio de cierre

Este cambio no declara M02 PASS. Después del merge se debe ejecutar nuevamente M02 Maximum Reaudit sobre la identidad post-AUD031 y auditar su artifact.
""",
        encoding="utf-8",
        newline="\n",
    )

    result = {
        "issue": "AUD-031",
        "source_run_id": 29928852782,
        "previous_engine_tree_sha256": OLD_SHA,
        "current_engine_tree_sha256": new_sha,
        "current_engine_file_count": new_count,
        "current_engine_byte_count": new_bytes,
        "m02_result": PENDING,
        "m03_result": PENDING,
    }
    Path("/tmp/aud031_identity.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
