# IA-IDUNEX - Re-auditoría forense M02 post-reconciliación AUD-009/AUD-010

**Expediente:** `AUD-013`
**Repositorio:** `LatinosFlow/IDUNEX`
**Rama documental:** `audit/AUD-013-m02-reaudit-post-reconciliation`
**Base auditada:** `main`
**Commit auditado:** `128b5b61f26293da5bc04426c19bb345eb440835`
**Commit subject:** `Merge pull request #23 from LatinosFlow/fix/AUD-012-reconcile-aud009-aud010-main`
**Fecha del informe:** `2026-07-17`
**Versión declarada del motor:** `v1.0.0`
**Estado del informe:** `EN_REVISION`
**Decisión recomputada:** `M02_FAIL`

## 1. Resumen ejecutivo

La re-auditoría completa post-reconciliación **no habilita M03 adversarial**. La decisión independiente es **M02_FAIL**.

La reconciliación sí es efectiva: los commits originales de `AUD-009` y `AUD-010`, y sus commits de reaplicación, son ancestros de `main`. El árbol actual incorpora un único entrypoint global clasificado, bloqueo de los 20 subvalidators por invocación directa y normalización de paths CLI cubierta por seis pruebas. Todos los scanners de repositorio requeridos pasan en su alcance y el baseline corregido actual es reproducible.

Esas mejoras no cumplen el cierre M02. La evidencia recomputada decisiva es:

- validator global: `rc=1`, `VALIDATORS_FAIL=3`, `BLOCKING_WARNINGS=0`, tres fail codes;
- matriz N1..N10 por `basic/intermediate/complete`: **0/30 PASS, 30/30 FAIL**;
- los 30 `generate` retornaron `rc=1`, sin timeout, sin ZIP y sin companion;
- `mutation-self-test`: **465/506 PASS, 41 FAIL**, fixture positivo `FAIL` y restauración `FAIL`;
- `validate`, `update-project`, `migrate-project` y `update-project-by-engine` sobre la fixture técnica vigente retornaron `FAIL` por `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`; `update-project` además emitió un blocking warning;
- no existe evidencia de lifecycle completo sobre un proyecto fresco aceptado.

No se aceptó ningún PASS declarado. No se modificó `engine/IDUNEX/`, no se generó Proyecto Demo, no se creó release, no se creó tag y no se cerraron issues.

## 2. Autoridad y regla de decisión

### 2.1 Autoridad aplicada

- `governance/authority/REFERENCIA/Informe_Maestro_Go_07d4ad84.pdf` (34 páginas; extracción textual y revisión visual de páginas 15, 17, 25 y 31).
- `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`.
- `docs/audits/IA-IDUNEX-ReauditoriaMotorM02-20260717-v1-EN_REVISION.md`.
- `docs/audits/IA-IDUNEX-PlanCorreccionM02-20260716-v1-EN_REVISION.md`.
- Ledgers `AUD-003` a `AUD-010` presentes en `docs/audits/`.
- `governance/CURRENT_STATE.json`, autoridad del estado global vigente.

El Informe Maestro exige separación `ENGINE_LEVEL != PROJECT_LEVEL != AGENT_LEVEL`, matriz máxima de 30 generaciones, lifecycle `generate/validate/update/migrate`, mutation completo, factory único, validator único y cierre exclusivamente con:

```text
VALIDATORS_FAIL=0
BLOCKING_WARNINGS=0
FAIL_CODES=[]
SCORE=10/10
```

La autoridad también ordena no entregar si una prueba, simulación, auditoría o comando falla, y prohíbe aceptar un PASS no recomputado.

### 2.2 Estado vigente y evidencia histórica

`governance/CURRENT_STATE.json` conserva:

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=M02_FAIL
READY_FOR_PROJECT_DEMO_GENERATION=false
RELEASE_AUTHORIZED=false
TAG_AUTHORIZED=false
PRODUCTIVE_CLOSURE_AUTHORIZED=false
```

El certificado histórico extraído `governance/authority/REFERENCIA/IDUNEX_MOTOR_v1_0__29dfbebb.txt` contiene afirmaciones antiguas de readiness y un SHA de ZIP. Se clasifica como baseline histórico recibido, no como autoridad del árbol corregido actual. `governance_state_check` detectó dos coincidencias históricas y cero contradicciones activas.

## 3. Commit y ancestros efectivos

| Elemento | Commit | `merge-base --is-ancestor <commit> HEAD` |
|---|---|---:|
| `main` auditado | `128b5b61f26293da5bc04426c19bb345eb440835` | - |
| AUD-009 original | `e9a6b63111ca6e4240bdc8719693dca0a16ae82a` | `0` / sí |
| AUD-010 original | `44d5b769ac60eeb27afd53dfa24ab0398664c791` | `0` / sí |
| Reconciliación AUD-009 | `c04e136270933fe81b818dc676074b2a3955a86d` | `0` / sí |
| Reconciliación AUD-010 | `72f658f9d40bd0c0d50afa7600d6ad81218362b6` | `0` / sí |

El merge `128b5b6` corresponde al PR #23 de reconciliación. Por tanto, a diferencia de AUD-012, AUD-009 y AUD-010 sí son ancestros efectivos del `main` auditado.

## 4. Entorno e integridad física

| Dato | Valor |
|---|---|
| OS | `Microsoft Windows NT 10.0.26200.0` |
| Python | `3.12.13` |
| Git | `2.55.0.windows.3` |
| Archivos tracked | 1,067 |
| Archivos tracked bajo `engine/IDUNEX` | 981 |
| Archivos activos del motor, excluido histórico | 749 |
| Estado antes de crear este informe | worktree limpio, rama sobre `origin/main` |
| Tags del repositorio | 0; 0 apuntando a `HEAD` |

Los outputs de matriz, mutation y lifecycle se escribieron fuera del repositorio. No se usó `--keep-work` en la matriz y el runner retiró cada proyecto/ZIP temporal. El árbol físico del motor permaneció sin cambios.

## 5. Baselines y manifiestos AUD-003

### 5.1 Baseline histórico recibido

| Elemento | Clasificación | Uso en AUD-013 |
|---|---|---|
| `IDUNEX_MOTOR_v1.0.0.zip` | ZIP histórico ausente del árbol por política | No recomputado y no usado como árbol actual |
| SHA histórico | `bbef200d6f0d7bf116853e0d763b90dc0b6454efee831e6dee1b040c78fce0d6` | No inyectado en generate/matrix |
| Ledger recibido | `governance/baseline/historical_received/IDUNEX_MOTOR_v1.0.0_RECEIVED_SHA256SUMS.txt` | Lineage no autoritativo para el árbol actual |

### 5.2 Baseline corregido actual

Se ejecutó el scanner AUD-003 y, adicionalmente, una recomputación independiente por bytes sobre cada entrada de `governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json`.

| Métrica | Manifiesto actual | Recomputado AUD-013 |
|---|---:|---:|
| Archivos físicos del motor | 981 | 981 |
| Bytes | 47,257,559 | 47,257,559 |
| Mismatches por archivo | 0 | 0 |
| SHA agregado | `227f43f615af809c214b296a7df3c7faa210d1087d3ac82a713026f657541947` | mismo |
| Missing indexados | 0 | 0 |
| Unmanifested físicos | 0 | 0 |
| Hashes obsoletos | 0 | 0 |
| Metadata mismatch | 0 | 0 |

El SHA agregado se calculó sobre registros ordenados `path UTF-8 + NUL + bytes decimales + NUL + SHA256 del archivo + LF`. Coincide con el manifiesto y con `governance/baseline/IDUNEX_CURRENT_TREE_SHA256.txt`.

Los cuatro manifiestos JSON internos (`FILE_MANIFEST.json`, `FINAL_TREE_MANIFEST.json`, `HASH_MANIFEST.json`, `MANIFEST.json`) tienen cero missing, unmanifested, duplicados y mismatches. `MANIFEST.txt` y `SHA256SUMS.txt` están sincronizados. El scanner conserva `aud003_scope_result=PARTIAL_PASS` porque este baseline de árbol no es un ZIP/release y el estado global continúa bloqueado; esa etiqueta no invalida la reproducibilidad física aquí acreditada.

## 6. Tabla de controles M02

| # | Control | Estado | Evidencia recomputada |
|---:|---|---|---|
| 1 | Integridad física del árbol actual | **PASS** | Checkout limpio en `128b5b6`; 1,067 tracked, 981 del motor; outputs fuera del repo. |
| 2 | Baseline actual reproducible | **PASS** | 981 archivos, 47,257,559 bytes, 0 mismatch, SHA `227f43...1947`. |
| 3 | SHA agregado y manifiestos AUD-003 | **PASS** | Scanner rc=0; companion y cuatro JSON internos sincronizados. |
| 4 | Separación ENGINE/PROJECT/AGENT | **PASS** | Contratos raíz presentes; Demo externo inactivo; fixtures explícitas; scanner Demo PASS. |
| 5 | SemVer y gobierno | **PASS** | `v1.0.0`; `CURRENT_STATE=EN_REVISION/M02_FAIL`; sin bump activo. |
| 6 | No-bloat | **PASS** | 0 grupos duplicados injustificados; 2 grupos justificados de carriers de manifiesto. |
| 7 | No-history activo | **PASS** | 0 rutas H activas; 295 movimientos sin conflicto; histórico aislado. |
| 8 | No-staging | **PASS** | 0 segmentos tracked `staging/stage` en árbol activo. |
| 9 | No-temp | **PASS** | 0 `tmp/temp`, `.pyc` o `__pycache__` tracked activos. |
| 10 | No logs largos activos | **PASS** | 0 archivos `.log` o heartbeat activos; `CHANGELOG` y nombres de políticas no son logs runtime. |
| 11 | No default activo de LatinosFlow | **PASS** | `latinosflow_default_active=false`; menciones restantes son nombres de manuales o bloqueos negativos. |
| 12 | No Proyecto 000 Demo activo | **PASS** | 0 branches por nombre; contratos Demo declaran `engine_runtime_active=false` y `BLOCKED_BY_M02_FAIL`. |
| 13 | No nombres Demo como canon activo | **PASS** | Runner 30 casos con `contains_demo_case=false`; referencias restantes externas/históricas/negativas. |
| 14 | Factory único | **PASS** | Un único `IDUNEX_PROJECT_FACTORY_v1.0.0.py`. |
| 15 | Validator único autoritativo | **PASS** | Scanner: 1 entrypoint, 20 subvalidators, ejecución directa bloqueada, 25 superficies clasificadas. |
| 16 | Profile360 | **PASS** | Subcheck field-source `61/61`; validate de fixture N2 `61/61 per model`. |
| 17 | TechExt | **PASS** | Subcheck field-source `284/284`; validate de fixture N2 `284/284 per model`. |
| 18 | Research corpus conectado | **PASS** | `RES_POLICY_REGISTRY.json`: 24 dominios y 5 pointers activos; subcheck ledger PASS. |
| 19 | Runtime ChatGPT/Copilot 10+N | **EN_REVISION** | Contrato presente; fixture N2 reporta 12, pero 0/30 entregas finales materializadas. |
| 20 | Prompt packs A-J | **EN_REVISION** | Subcheck de template engine PASS/100%; no hay pack final validado en 30 entregas. |
| 21 | Output contracts | **PASS** | Contratos engine/project/agent presentes; su materialización final falla en lifecycle. |
| 22 | Update/migration contracts | **PASS** | 8 tipos, 3 shapes, 9 casos; `validate-update-contract` rc=0, fail codes vacíos. |
| 23 | CLI lifecycle | **FAIL** | 7 comandos expuestos; generate/validate/update/migrate no cierran en limpio. |
| 24 | Generate | **FAIL** | 30/30 rc=1; 30 sin ZIP/companion; 0 timeouts. |
| 25 | Validate | **FAIL** | Fixture N2: rc=1, validators_fail=1, `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`. |
| 26 | Update | **FAIL** | `update-project` rc=1, validators_fail=1, blocking_warnings=1, H113; no base fresca aceptada. |
| 27 | Migrate | **FAIL** | `migrate-project` y `update-project-by-engine` rc=1, validators_fail=1, H113. |
| 28 | Matriz N1..N10 x 3 | **FAIL** | 0/30 PASS, 30/30 FAIL, 1,711.984 s. |
| 29 | Mutation/self-test | **FAIL** | 465/506; 41 FAIL; fixture positivo y restauración FAIL. |
| 30 | PASS vs EN_REVISION | **PASS** | Gobierno consistente; 0 contradicciones activas; evidencia histórica no gobierna. |
| 31 | Windows-safe remap | **PASS** | 487 mappings, 0 colisiones/missing/stale; 5,850 paths indexados. |
| 32 | Security Lite | **PASS** | 0 secretos de alta confianza. |
| 33 | Intake Audit | **PASS** | 0 failures; warning de path histórico de 161 caracteres. |
| 34 | Demo hardcoding guard | **PASS** | 0 branches activos, 0 referencias prohibidas, 30 casos no-Demo. |
| 35 | Baseline scanner | **PASS** | Árbol actual y manifests íntegros; estado/release siguen bloqueados. |
| 36 | No-bloat/no-history scanner | **PASS** | 0 duplicados injustificados, 0 rutas H activas, 0 conflictos de movimiento. |
| 37 | Validator entrypoint scanner | **PASS** | `CONSISTENT`; 1 entrypoint, 20 subvalidators, 8 tools de repositorio. |
| 38 | Governance state check | **PASS** | `CONSISTENT`; `EN_REVISION/M02_FAIL`; 0 contradicciones activas. |

**Conteo:** 29 PASS, 7 FAIL, 2 EN_REVISION; 38 controles.

Un PASS de control individual acredita solo ese alcance y no compensa ningún bloqueante.

## 7. Scanners y pruebas de intake

| Comando/check | rc | Resultado | Evidencia principal |
|---|---:|---|---|
| `tools/audit/intake_audit.py --repo-root .` | 0 | PASS | 1,068 archivos físicos; 0 failures; 2 warnings no bloqueantes. |
| `tools/audit/security_lite_scan.py --repo-root .` | 0 | PASS | Sin secretos de alta confianza. |
| `tools/audit/governance_state_check.py --repo-root .` | 0 | CONSISTENT | 0 contradicciones activas. |
| `tools/audit/windows_path_remap_check.py --repo-root .` | 0 | PASS | 487 mappings; 0 missing/collisions/stale. |
| `tools/audit/no_bloat_no_history_check.py --repo-root .` | 0 | PASS | 0 duplicados injustificados; 0 H-route activo. |
| `tools/audit/demo_hardcoding_check.py --repo-root .` | 0 | PASS | 0 named branches; 30 casos no-Demo. |
| `tools/audit/baseline_scanner.py --repo-root .` | 0 | PASS | 981/981; SHA agregado coincide. |
| `tools/audit/validator_entrypoint_check.py --repo-root .` | 0 | CONSISTENT | 1 entrypoint; 20 subvalidators; 25 superficies clasificadas. |
| `python -B -m unittest discover -s tests/intake -p 'test_*.py' -v` | 0 | PASS | 36 tests OK; 1 skip de SIGALRM Unix en Windows. |

## 8. Validator global y subchecks

### 8.1 Subchecks delegados

AUD-009 obliga a ejecutar secundarios mediante:

```text
VALIDATE_IDUNEX_RUNTIME.py --subcheck <ID> -- <engine-root-absoluto>
```

| Subcheck | rc | Resultado local |
|---|---:|---|
| `VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL` | 0 | 299 JSON, 21 schemas, 0 invalid, 0 fail codes. |
| `VALIDATE_PROMPT_PACK_STRUCTURE` | 0 | A-J 100%, negative/QC/fallback PASS. |
| `VALIDATE_FIELD_SOURCE_TRACE_LEDGER` | 0 | Profile360 61/61, TechExt 284/284. |
| `VALIDATE_AGENT_RUNTIME_MARKDOWN_STRICT` | 0 | 46 clauses, 100%, 0 bad clauses. |

Estos resultados son `LOCAL_SUBCHECK_ONLY`; no tienen autoridad para cerrar M02.

### 8.2 Entrypoint global

```text
python -B engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py engine/IDUNEX
```

| Métrica | Resultado |
|---|---:|
| rc | 1 |
| result | FAIL |
| validators_fail | 3 |
| blocking_warnings | 0 |
| global_closure_authorized | false |
| m02_decision_authority | false |

Fail codes:

1. `ACTIVE_VALIDATORS_EXACT_SET`: el runtime conserva un set de nombres largos previo al remapeo, mientras los archivos físicos activos usan nombres Windows-safe como `VALIDATE_ACTIVE_AU_f3527139.py`.
2. `DOCUMENT_TRUTHFULNESS_PARITY_H245_H260`: las superficies de estado no contienen tokens de cierre `VALIDATORS_FAIL=0`, `FAIL_CODES=[]`, `SCORE=10/10`; bajo el estado actual no pueden declararlos, pero el validator los sigue exigiendo para cerrar.
3. `DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY`: `MASTER_GOVERNANCE_VALIDATION_CONTRACT.json` no está sincronizado con el gate de alcance activo.

La topología única AUD-009 pasa su scanner, pero el entrypoint global sigue fallando su propia validación de paridad. No existe base para sustituir ese resultado por un PASS arquitectónico parcial.

## 9. Matriz N1..N10 x tres niveles

Comando:

```text
python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py \
  --work <audit-work>/aud013_matrix_work \
  --output-dir <audit-work>/aud013_matrix_output \
  --timeout 300 --stream-progress
```

| Nivel | N1 | N2 | N3 | N4 | N5 | N6 | N7 | N8 | N9 | N10 |
|---|---|---|---|---|---|---|---|---|---|---|
| basic / low-info | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| intermediate-info | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| complete / full-info | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |

Resumen recomputado:

```text
case_count=30
pass_count=0
fail_count=30
PROJECT_N1_N10_X3_MATRIX_PASS_COUNT=0/30
elapsed_seconds=1711.984
generate_rc=1 en 30/30
generate_result=FAIL en 30/30
generate_timeout=false en 30/30
post_completion_process_kill=false en 30/30
FAIL_ZIP_OR_COMPANION_MISSING en 30/30
validate_rc=1 en 30/30
FAIL_ZIP_MISSING en 30/30
contains_demo_case=false
```

La fila compacta N1 registró `generate_seconds=17.328`; las filas de N superiores aumentaron de duración, pero ninguna agotó el timeout. El runner retiró las salidas por caso y declaró `no_test_output_zips_in_engine=true`.

No se usó el SHA histórico del ZIP como variable `IDUNEX_ENGINE_ZIP_SHA256`; hacerlo habría confundido el baseline histórico con el árbol corregido actual.

## 10. Mutation/self-test

Comando:

```text
python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py \
  mutation-self-test --work <audit-work>/aud013_mutation_work --summary \
  --output-json <audit-work>/aud013_mutation_result.json
```

| Métrica | Resultado |
|---|---:|
| Mutation count | 506 |
| Cases PASS | 465 |
| Cases FAIL | 41 |
| Positive fixture | FAIL |
| Restoration retest | FAIL |
| Resultado global | FAIL |
| Fail code global | `FAIL_UNCLASSIFIED_EXECUTABLE_FAILURE_MISSING_FAILCODE` |

Los casos 466-506 no observaron sus fail codes mutados: todos registraron `POSITIVE_FIXTURE_FAILED` antes de la mutación. Distribución:

| Rango | Familia | FAIL |
|---|---|---:|
| 466-475 | H69 pending/proof | 10 |
| 476-487 | H71-H79 safety/watermark | 12 |
| 488-497 | H90 semantic suite | 10 |
| 498-506 | H113-H118 SHA/sidecar/report | 9 |

La validación independiente de `FIXTURE_ONLY_MUTATION_BASE` produjo:

```text
result=FAIL
validators_fail=1
blocking_warnings=0
profile360_join=61/61 per model
techext_join=284/284 per model
runtime_upload_count=12
fail_codes=[FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE]
```

El conteo 465/506 no puede aceptarse como suficiente: la autoridad exige PASS total y restauración limpia.

## 11. CLI lifecycle, update y migración

La superficie CLI expone exactamente siete comandos:

```text
generate
validate
validate-update-contract
update-project
migrate-project
update-project-by-engine
mutation-self-test
```

El contrato nuevo `age_delta_years` normalizó con rc=0, `validators_fail=0`, `blocking_warnings=0` y `fail_codes=[]`. Esto acredita el borde de contrato y es coherente con las seis pruebas de AUD-010.

Las operaciones sobre la fixture técnica N2 no cerraron:

| Operación | rc | validators_fail | blocking_warnings | Fail codes |
|---|---:|---:|---:|---|
| `validate` | 1 | 1 | 0 | `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE` |
| `update-project` | 1 | 1 | 1 | `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE` |
| `migrate-project` | 1 | 1 | 0 | `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE` |
| `update-project-by-engine` | 1 | 1 | 0 | `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE` |

La fixture base ya es inválida y no sustituye un proyecto fresco aceptado. El resultado forense es más restrictivo, no menos: no existe evidencia actual de update/migration end-to-end exitoso sobre una entrega generada por este `main`.

## 12. Comparación con la M02 anterior

| Área | AUD-012 (`27a4961`) | AUD-013 (`128b5b6`) | Cambio |
|---|---|---|---|
| AUD-009 ancestro de main | No | Sí, original y reconciliación | Corregido |
| AUD-010 ancestro de main | No | Sí, original y reconciliación | Corregido |
| Validator entrypoint scanner | Ausente / EN_REVISION | PASS: 1 + 20 subvalidators | Corregido |
| CLI path normalization | No fusionado | 6 pruebas PASS | Corregido |
| Baseline actual | 979 archivos; `b44ce9...548e4` | 981 archivos; `227f43...1947` | Regenerado y reproducible |
| Validator global | 3 FAIL | 3 FAIL | Sin cierre |
| Matriz máxima | 0/30 | 0/30 | Sin mejora de decisión |
| Mutation/self-test | 465/506 | 465/506 | Sin mejora |
| Gobierno | EN_REVISION/M02_FAIL | EN_REVISION/M02_FAIL | Coherente |
| M02 | FAIL | FAIL | Sin cambio |

La reconciliación resuelve la presencia efectiva de AUD-009/AUD-010, pero no los bloqueantes funcionales de cierre que AUD-012 ya había observado.

## 13. Hallazgos bloqueantes

### B-01 - Validator global no cierra

`VALIDATORS_FAIL=3` y tres fail codes contradicen el umbral obligatorio `0/[]`. Incluye un set esperado de nombres de validators no actualizado al remapeo físico.

### B-02 - Matriz máxima 0/30

Ninguno de los 30 casos produjo ZIP/companion. `generate rc=1` en todos los casos. Incumple `30/30 PASS`.

### B-03 - Mutation/self-test incompleto

41 casos fallan porque el fixture positivo base falla; la restauración también falla. Incumple PASS total.

### B-04 - SHA de motor no resuelto para el árbol corregido

La fixture y el lifecycle reportan `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`. El companion histórico existe, pero no es autoridad del árbol corregido y no se reutilizó artificialmente.

### B-05 - Lifecycle update/migration sin evidencia aceptable

Los tres comandos de update/migration terminan rc=1 sobre la fixture técnica disponible; `update-project` además emite `blocking_warnings=1`. No existe base fresca aceptada.

## 14. Hallazgos no bloqueantes

- Intake advierte `.git` como ruta ignorada/generada y una ruta histórica de 161 caracteres; Windows remap acredita 0 stale/missing/collisions.
- La suite Windows omite una prueba Unix de `SIGALRM`; las otras 36 pruebas pasan.
- Los dos grupos de duplicados activos son carriers de manifiesto explícitamente justificados.
- Los tres archivos cuyo nombre contiene Demo permanecen solo por compatibilidad y declaran `ENGINE_LEVEL activo=false`; el scanner no detecta branch ejecutable por nombre.

## 15. Criterio de cierre

| Criterio para `M02_PASS` | Resultado AUD-013 | Cumple |
|---|---:|---|
| `VALIDATORS_FAIL=0` | 3 globales; 1 en lifecycle | No |
| `BLOCKING_WARNINGS=0` | 0 globales; 1 en update | No |
| `FAIL_CODES=[]` | No vacío | No |
| `SCORE=10/10` | No alcanzado; no se asigna score parcial | No |
| Matriz 30/30 | 0/30 | No |
| Mutation total | 465/506; fixture/restauración FAIL | No |
| Sin contradicciones de gobierno | 0 activas | Sí |
| Sin Demo activo | Scanner PASS | Sí |
| Sin release/tag generado | 0/0 por AUD-013 | Sí |
| Baseline actual reproducible | PASS | Sí |
| AUD-009/AUD-010 ancestros | Sí | Sí |

## 16. Decisión final y recomendación

```text
M02_RESULT=M02_FAIL
MOTOR_STATUS=EN_REVISION
M03_ADVERSARIAL=BLOCKED
READY_FOR_PROJECT_DEMO_GENERATION=false
RELEASE_AUTHORIZED=false
TAG_AUTHORIZED=false
```

**Decisión final: M02_FAIL.**

M03 adversarial permanece bloqueada. Se recomienda abrir issues derivados, sin cerrarlos automáticamente, para:

1. sincronizar el set físico Windows-safe con `ACTIVE_VALIDATORS_EXACT_SET` y los contratos de gobierno;
2. resolver una identidad SHA legítima del motor corregido sin reutilizar el ZIP histórico;
3. restaurar el fixture positivo y alcanzar mutation 506/506 con retest limpio;
4. recomputar generate/validate hasta 30/30 con ZIP, companion y `testzip` válidos;
5. repetir update/migration end-to-end sobre un proyecto fresco aceptado.

Solo una nueva M02 independiente que alcance todos los criterios podrá habilitar M03.

## 17. Comandos principales ejecutados

```text
git fetch --prune origin
git merge-base --is-ancestor <AUD-009/AUD-010 commits> HEAD
git ls-files

python -B tools/audit/intake_audit.py --repo-root .
python -B tools/audit/security_lite_scan.py --repo-root .
python -B tools/audit/governance_state_check.py --repo-root .
python -B tools/audit/windows_path_remap_check.py --repo-root .
python -B tools/audit/no_bloat_no_history_check.py --repo-root .
python -B tools/audit/demo_hardcoding_check.py --repo-root .
python -B tools/audit/baseline_scanner.py --repo-root .
python -B tools/audit/validator_entrypoint_check.py --repo-root .
python -B -m unittest discover -s tests/intake -p 'test_*.py' -v

python -B engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py engine/IDUNEX
python -B engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py --subcheck <ID> -- <absolute-engine-root>

python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py --work <audit-work> --output-dir <audit-output> --timeout 300 --stream-progress
python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py mutation-self-test --work <audit-work> --summary --output-json <result.json>
python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py validate-update-contract --input <input.json> --summary
python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py validate <fixture> --summary
python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py update-project ...
python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py migrate-project ...
python -B engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py update-project-by-engine ...
```

---

**Declaración de control:** este informe documenta evidencia recomputada sobre el commit indicado. No modifica el motor, no cambia `governance/CURRENT_STATE.json`, no autoriza Proyecto Demo, release, tag ni cierre productivo, y no convierte resultados internos o históricos en un PASS global.
