# IA-IDUNEX — Ruptura de circularidad estado-identidad

**Fecha:** 2026-07-27
**Estado:** EN_REVISION
**Control:** Issue #73 — AUD-037
**Veredicto de implementación:** `AUD037_GOVERNANCE_IDENTITY_CYCLE_BREAK_IMPLEMENTED_PENDING_REVIEW`

## Alcance y restricciones

AUD-037 rediseña de forma atómica la frontera entre el estado externo mutable, los snapshots internos de build y el runtime validator global. Durante la implementación no se ejecutaron M02, M03, `workflow_dispatch`, Proyecto 000 Demo, `generate`/`validate` del Demo real, `refresh-external-artifacts`, carga de agentes, release, tag ni merge. El motor permanece `EN_REVISION` y `CREATIVE_OUTPUT_CERTIFIED=FALSE`.

## Base verificada

- Commit base obligatorio: `f9a2b84415ef53a8602911e39835617575ff3864`.
- Autoridad inicial: `issue=AUD-035`, `motor_status=EN_REVISION`.
- Estado inicial: `m02_result=NOT_RECOMPUTED_POST_AUD035`, `m03_result=NOT_RECOMPUTED_POST_AUD035`.
- Identidad inicial: `981` archivos, `47324981` bytes, SHA-256 `c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e`.
- AUD-028: `status=CONSUMED`, `authorized=false`, `consumed=true`, `generate_executions_allowed=0`, `validate_executions_allowed=0`.

## Evidencia M02 scoped preservada

- Run: `30194513740`.
- Job: `89773509632`.
- Artifact: `8629888949`.
- Artifact name: `idunex-m02-max-30194513740-attempt-1`.
- Artifact SHA-256: `797d705d9e75317f0cb8dacebcee22e1376369bfadae05ad453943988ad14dde`.
- Árbol: `981 / 47324981 / c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e`.
- Resultado técnico: `PASS`; matriz `30/30`; mutation `506/506`; score `10/10`.
- Decisión: `NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY`.
- Clasificación original: `VALIDATED_SCOPED_EVIDENCE_FOR_C5CB2F4B_NOT_GOVERNANCE_AUTHORITY`.

Como AUD-037 modifica el motor, esta evidencia queda `evidence_class=REFERENCIA_SUSTITUIDA`, `current_tree_applicability=false` y `superseded_by=AUD-037`. No se reasigna al árbol nuevo.

## Reproducción de la circularidad

La reproducción se realizó en `TemporaryDirectory`, copiando `engine/IDUNEX` y `governance` sin modificar el checkout. Se cambió únicamente `CURRENT_STATE.m02_result` a `M02_PASS` sintético y se ejecutó el runtime validator existente.

Resultado observado antes de la corrección:

```text
validator_result=FAIL
contract_failcode=FAIL_MASTER_GOVERNANCE_VALIDATION_CONTRACT_NOT_SYNCED
engine_before=981/47324981/c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e
engine_after=981/47324981/c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e
engine_unchanged=true
```

## Causa raíz

`MASTER_GOVERNANCE_VALIDATION_CONTRACT.json` contenía `expected_current_state` con valores M02/M03 audit-specific. El runtime validator exigía igualdad exacta entre ese snapshot interno y `governance/CURRENT_STATE.json`. Una transición externa legítima cambiaba el estado, rompía la igualdad y obligaba a editar el motor; esa edición cambiaba el SHA al que debía ligarse la evidencia, cerrando el ciclo estado-identidad.

## Arquitectura anterior

```text
CURRENT_STATE mutable
  == igualdad exacta ==
contrato/superficies internas
  -> cambio de engine/IDUNEX
  -> nuevo SHA
  -> evidencia anterior deja de aplicar
```

## Arquitectura nueva

```text
STATE_AUTHORITY=governance/CURRENT_STATE.json
BUILD_STATE_SNAPSHOT_AUTHORITY=FALSE
BUILD_STATE_SNAPSHOT_CLASSIFICATION=NON_AUTHORITY_BUILD_SNAPSHOT
```

El contrato interno ahora describe un esquema estable, interlocks inmutables, reglas de transición y reglas de binding de evidencia. No replica el valor mutable actual. Los documentos y los seis manifests internos sólo registran un snapshot de build trazable y no autoritativo.

El validator global existente valida:

- existencia, lectura, esquema y autoridad de `CURRENT_STATE`;
- tokens exactos M02/M03, sin coincidencias por subcadena `PASS`;
- `M02_PASS` antes de `M03_PASS`;
- run, job, artifact, artifact SHA, commit y la identidad física completa;
- evidencia M02/M03 para el mismo árbol;
- interlocks de Demo, release, tag, OFICIAL, cierre productivo, agentes y output creativo;
- AUD-028 consumido y con contadores cero;
- ausencia de autoridad en snapshots internos y ausencia de `expected_current_state`.

## Superficies modificadas

- Contrato maestro y `VALIDATE_IDUNEX_RUNTIME.py`.
- `RELEASE_CERTIFICATE.txt`, `CHANGELOG.md`, `ACTIVE_VERSION.txt`, Control Center `ACTIVE_VERSION.md` y `STATUS.md`.
- Los seis manifests internos canónicos.
- `CURRENT_STATE`, baseline manifest, companion SHA y diff recibido-a-actual.
- `REPOSITORY_MANIFEST.yml`, `README.md` y `GOVERNANCE_STATUS.md`.
- Workflows M02/M03, scanners de gobernanza/identidad y pruebas intake.

No se modificaron Project Factory funcional, canon, perfiles, prompts, agentes, reglas creativas ni schemas no relacionados.

## Prueba de transición externa sin cambio de SHA

La prueba obligatoria usa una copia temporal controlada:

1. Con `M02=NOT_RECOMPUTED_POST_AUD037` y `M03=NOT_RECOMPUTED_POST_AUD037`, el validator resulta `PASS`.
2. Se cambia únicamente `CURRENT_STATE` a `M02_PASS`, se añade evidencia sintética consistente con el árbol y se conserva M03 no recomputado.
3. El mismo validator resulta `PASS`.
4. La identidad física de `engine/IDUNEX` antes y después es exactamente igual.
5. Mutaciones de SHA, bytes, orden M02/M03, artifact, AUD-028, Demo, release, tag, OFICIAL, agentes, certificación creativa, autoridad del snapshot e igualdad audit-specific fallan con failcodes específicos.

## Nueva identidad calculada

Los seis manifests internos se regeneraron con `tools/audit/baseline_scanner.py`. La identidad se calculó dos veces y se exige igualdad exacta:

```text
ENGINE_FILE_COUNT=981
ENGINE_BYTES=47350130
ENGINE_TREE_SHA256=b516c1f08682aba94ebb771578d727361ab71b406406d30fc442f27458b1fda4
```

El file count permanece en `981`; el cambio de bytes está explicado por las superficies AUD-037 modificadas.

## Estado e interlocks resultantes

```text
issue=AUD-037
motor_status=EN_REVISION
m02_result=NOT_RECOMPUTED_POST_AUD037
m03_result=NOT_RECOMPUTED_POST_AUD037
AUD028=CONSUMED/authorized:false/consumed:true/generate:0/validate:0
Demo=false
release=false
tag=false
OFICIAL=false
productive_closure=false
agent_load=false
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

M02 queda listo para una única ejecución manual futura sobre la nueva identidad. M03 exige un M02 formalizado para el mismo árbol y permanece bloqueado.

## Reversa

La reversa consiste en revertir atómicamente el commit AUD-037 completo: contrato, validator, superficies internas, seis manifests, identidad externa, estado, workflows, scanners, pruebas y documentación. No debe revertirse sólo `CURRENT_STATE` o sólo el contrato, porque eso reintroduciría una frontera incoherente. Tras una reversa debe regenerarse canónicamente la identidad del árbol resultante y mantenerse M02/M03 no recomputados para ese árbol.

## Cierre

M02 y M03 no fueron ejecutados. No se creó release ni tag, no se declaró `MOTOR_STATUS=OFICIAL`, no se cargaron agentes y no se fusionó el PR. `CREATIVE_OUTPUT_CERTIFIED=FALSE`.
