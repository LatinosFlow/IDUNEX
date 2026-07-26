# IA-IDUNEX — Recomputación M02 post-AUD-033

**Estado documental:** `EN_REVISION`
**Control:** `AUD-034` / Issue #67
**Autoridad vigente:** `governance/CURRENT_STATE.json`

## Propósito

Formalizar en la gobernanza vigente el resultado técnico M02 recomputado y validado para el árbol actual de `engine/IDUNEX`, sin modificar ese árbol ni ejecutar M03, Demo, generate o refresh-external-artifacts.

## Evidencia M02 autorizada

```text
M02_RUN_ID=29941393366
M02_JOB_ID=88995880545
M02_ARTIFACT_ID=8539029665
M02_ARTIFACT_NAME=idunex-m02-max-29941393366-attempt-1
M02_ARTIFACT_SHA256=fd5c9334b96989c714300607dadf742ff63783b8090d90fc3d404b3a22355270
M02_REPOSITORY_COMMIT=1fc082bfcae5b590066309727c120500de976378
M02_ENGINE_TREE_SHA256=58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7
M02_ENGINE_FILE_COUNT=981
M02_ENGINE_BYTE_COUNT=47323574
M02_RUNTIME_VALIDATOR=PASS
M02_MATRIX=30/30_PASS
M02_MUTATION=506/506_PASS
M02_POSITIVE_FIXTURE=PASS
M02_RESTORATION_RETEST=PASS
M02_TECHNICAL_SCORE=10/10
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

La recomputación fue independiente. La matriz obtuvo `30/30_PASS`, mutation `506/506_PASS`, el retest de restauración fue `PASS` y el score técnico fue `10/10`.

El `audit_id` interno heredado `AUD-026-M02-POST-PR44` se clasifica únicamente como `METADATA_HEREDADA_NO_AUTORIDAD_NOMINAL`; no es autoridad actual.

## Estado e interlocks

El resultado vigente es `M02_PASS_RECOMPUTED_POST_AUD033`. M03 continúa `NOT_RECOMPUTED_POST_AUD030` y bloqueado por AUD-032. Un PASS de M02 por sí solo no habilita Demo general.

AUD-028 permanece `CONSUMED` y no puede reutilizarse. Agentes, release, tag, OFICIAL y cierre productivo siguen bloqueados. `CREATIVE_OUTPUT_CERTIFIED=FALSE`.

## Alcance, pruebas y reversa

Archivos modificados: `governance/CURRENT_STATE.json`, `tools/audit/governance_state_check.py`, `tests/intake/test_governance_state.py`, `README.md`, `GOVERNANCE_STATUS.md` y `REPOSITORY_MANIFEST.yml`; este documento completa el séptimo archivo autorizado. No se modificó `engine/IDUNEX`.

Las pruebas de gobernanza, intake, seguridad ligera y consistencia de diff se ejecutan antes de la entrega. La reversa consiste en revertir el commit de AUD-034, lo que restituye el estado canónico anterior sin alterar el árbol del motor.
