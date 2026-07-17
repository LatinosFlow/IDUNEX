# IA-IDUNEX - Re-auditoría forense independiente del motor M02 post-correcciones

**Expediente:** `AUD-012`
**Repositorio:** `LatinosFlow/IDUNEX`
**Rama de auditoría:** `audit/AUD-012-m02-reaudit-post-fixes`
**Base auditada:** `main`
**Commit auditado:** `27a49618db402a095b4ca5abcf37949ba4ba0a0d`
**Commit subject:** `Merge pull request #21 from LatinosFlow/fix/AUD-003-baseline-ledger-remap`
**Fecha del informe:** `2026-07-17`
**Versión declarada:** `v1.0.0`
**Estado del informe:** `EN_REVISION`
**Decisión recomputada:** `M02_FAIL`

## 1. Resumen ejecutivo

La re-auditoría completa no habilita el motor IDUNEX para M03 adversarial. La decisión independiente es **M02_FAIL**.

El árbol corregido actual sí mejora de forma material respecto de la M02 anterior: el baseline actual se reproduce byte a byte, los manifiestos AUD-003 están sincronizados, el remapeo Windows no presenta rutas stale, el hardcoding ejecutable de Demo fue retirado, el gobierno raíz es coherente y los scanners no-bloat/no-history pasan en su alcance activo.

Esas correcciones no satisfacen el cierre M02. La evidencia recomputada decisiva es:

- matriz N1..N10 por `basic/intermediate/complete`: **0/30 PASS, 30/30 FAIL**;
- los 30 `generate` retornaron `rc=1`, sin ZIP ni companion; el caso N1 aislado identificó `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE` y `FAIL_H160_ATOMIC_FINALIZE_NOT_REACHED`;
- `mutation-self-test`: **465/506 PASS, 41 FAIL**, fixture positivo `FAIL` y retest de restauración `FAIL`;
- el validator runtime autoritativo declarado retornó `rc=1`, `validators_fail=3`;
- el entrypoint único de AUD-009 y la normalización de rutas CLI de AUD-010 existen en commits/ramas separadas, pero **no son ancestros de `main` auditado**;
- update/migrate no pueden elevarse a PASS sobre un proyecto fresco aceptado porque `generate` no produce una entrega válida y AUD-010 no está fusionado.

No se aceptó ningún PASS declarado. No se modificó `engine/IDUNEX/`, no se generó Proyecto Demo, no se creó release, no se creó tag y no se cerraron issues.

## 2. Decisión y estado general

| Métrica de cierre | Resultado recomputado | Criterio M02_PASS | Cumple |
|---|---:|---:|---|
| Validator runtime | `VALIDATORS_FAIL=3` | `0` | No |
| Blocking warnings del validator runtime | `0` | `0` | Sí, pero insuficiente |
| Fail codes | 3 en validator runtime; adicionales en generate/mutation | `[]` | No |
| Score | `10/10 no alcanzado`; no se asigna score parcial | `10/10` | No |
| Matriz N1..N10 x 3 | `0/30 PASS` | `30/30 PASS` | No |
| Mutation/self-test | `465/506 PASS`; global FAIL | PASS total | No |
| Gobierno raíz | `EN_REVISION / M02_FAIL`, 0 contradicciones activas | Sin contradicciones | Sí |
| Demo activo | 0 branches por nombre; runner sin Demo | Ausente | Sí |
| Baseline actual | 979/979; SHA agregado reproducido | Reproducible | Sí |
| Release/tag creado por AUD-012 | 0/0 | 0/0 | Sí |

**Conteo de controles:** 27 PASS, 6 FAIL, 5 EN_REVISION; 38 controles totales.

Un PASS de control individual acredita solo ese alcance. No compensa ningún bloqueante.

## 3. Autoridad, baseline y clasificación de evidencia

### 3.1 Autoridad aplicada

- `governance/authority/REFERENCIA/Informe_Maestro_Go_07d4ad84.pdf` (34 páginas, inspección visual y extracción textual).
- `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`.
- `docs/audits/IA-IDUNEX-PlanCorreccionM02-20260716-v1-EN_REVISION.md`.
- Ledgers AUD-003 a AUD-010 disponibles en `main` o en sus commits de corrección, sin asumir que una rama no fusionada pertenece a `main`.
- `governance/CURRENT_STATE.json` como única autoridad del estado global vigente.

El Informe Maestro exige separación `ENGINE_LEVEL != PROJECT_LEVEL != AGENT_LEVEL`, matriz máxima 30/30, generate/validate/update/migrate, mutation total, factory único, validator único, no-bloat/no-history y cierre exclusivamente con `VALIDATORS_FAIL=0`, `BLOCKING_WARNINGS=0`, `FAIL_CODES=[]`, `SCORE=10/10`.

### 3.2 Baseline histórico recibido

| Elemento | Clasificación | Resultado |
|---|---|---|
| `IDUNEX_MOTOR_v1.0.0.zip` | Evidencia histórica declarada; ZIP ausente por política | No recomputado en AUD-012 |
| SHA histórico declarado | `bbef200d6f0d7bf116853e0d763b90dc0b6454efee831e6dee1b040c78fce0d6` | No es SHA del árbol corregido actual |
| Ledger recibido | `governance/baseline/historical_received/IDUNEX_MOTOR_v1.0.0_RECEIVED_SHA256SUMS.txt` | Preservado, no autoridad actual |

La ausencia del ZIP histórico no se usa para negar la reproducibilidad del baseline corregido actual y tampoco se reinterpreta como release actual.

### 3.3 Baseline corregido actual

| Métrica | Declarado AUD-003 | Recomputado AUD-012 |
|---|---:|---:|
| Archivos físicos `engine/IDUNEX` | 979 | 979 |
| Bytes | 47,227,994 | 47,227,994 |
| SHA agregado | `b44ce9c87249a5ab33c7cb25ef3aeb539a21ff03f481e2e6282238b2da5548e4` | mismo |
| Rutas indexadas faltantes | 0 | 0 |
| Archivos físicos sin manifest | 0 | 0 |
| Hashes obsoletos | 0 | 0 |
| Metadatos discordantes | 0 | 0 |

El SHA se recalculó independientemente con el algoritmo declarado: registros ordenados `repo_path UTF-8 + NUL + bytes decimales + NUL + SHA256 de archivo + LF`. El resultado coincide con `governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json` y `governance/baseline/IDUNEX_CURRENT_TREE_SHA256.txt`.

### 3.4 Manifiestos actuales y evidencia histórica no autoritativa

- Manifiesto externo actual: `governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json`.
- Companion agregado actual: `governance/baseline/IDUNEX_CURRENT_TREE_SHA256.txt`.
- Diferencia recibido -> actual: `governance/baseline/IDUNEX_BASELINE_DIFF_RECEIVED_TO_CURRENT.json`.
- Manifiestos internos actuales: cuatro JSON y dos carriers de texto bajo `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/`.
- Evidencia histórica: `engine/IDUNEX/14_HISTORICAL_NON_AUTHORITY/`; no se utilizó como autoridad para el resultado M02.

## 4. Entorno y método

| Componente | Valor |
|---|---|
| OS | Microsoft Windows NT 10.0.26200.0 |
| Python | 3.12.13 |
| Git | 2.53.0.windows.3 |
| Worktree forense limpio | detached en `27a49618db402a095b4ca5abcf37949ba4ba0a0d` |
| Archivos tracked del commit | 1,059 |
| Archivos tracked del motor | 979 |

Se creó un worktree nuevo en una ruta corta para evitar contaminación por archivos ignorados de checkouts previos. Todos los outputs de matriz y mutación quedaron fuera del repositorio. El árbol del motor permaneció read-only.

## 5. Tabla de controles M02

| # | Control | Estado | Evidencia recomputada |
|---:|---|---|---|
| 1 | Integridad física del árbol actual | **PASS** | Worktree limpio materializado en el commit; 1,059 archivos tracked, 979 bajo el motor. |
| 2 | Baseline actual reproducible | **PASS** | Recomputación independiente: 979 archivos, 47,227,994 bytes, SHA agregado `b44ce9...548e4`. |
| 3 | SHA agregado y manifiestos AUD-003 | **PASS** | Baseline scanner PASS; 0 missing, 0 unmanifested, 0 obsolete hash, 0 metadata mismatch. |
| 4 | Separación ENGINE/PROJECT/AGENT | **PASS** | Contratos JSON/MD presentes; dos fixtures activos están marcados `FIXTURE_ONLY`; hardcoding guard PASS. |
| 5 | SemVer y estado de gobierno | **PASS** | `VERSION=v1.0.0`; sin sufijo activo; `CURRENT_STATE.json=EN_REVISION/M02_FAIL`. |
| 6 | No-bloat | **PASS** | Scanner: 0 grupos duplicados injustificados; 2 grupos justificados de carriers de manifiesto. |
| 7 | No-history activo | **PASS** | Scanner: 0 rutas H activas; 295 movimientos sin conflicto; histórico aislado. |
| 8 | No-staging | **PASS** | 0 rutas tracked con segmento staging/stage. |
| 9 | No-temp | **PASS** | 0 rutas tracked `tmp/temp`, `.pyc` o `__pycache__`. |
| 10 | No logs largos activos | **PASS** | 0 rutas tracked log/heartbeat. |
| 11 | No default activo de LatinosFlow | **PASS** | Menciones limitadas al contrato de nombres de manuales exigido por autoridad o a reglas negativas; `latinosflow_default_active=false`. |
| 12 | No Proyecto 000 Demo activo en motor | **PASS** | 0 branch por nombre, 0 literal activo prohibido; contratos de compatibilidad declaran `engine_runtime_active=false`. |
| 13 | No nombres Demo como canon activo | **PASS** | Runner de 30 casos contiene 0 Demo; referencias restantes son contrato externo posterior, authority input o guardia negativa. |
| 14 | Factory único | **PASS** | Un `IDUNEX_PROJECT_FACTORY_v1.0.0.py`; runner y export packer no son factories paralelos. |
| 15 | Validator único autoritativo | **FAIL** | 17 `VALIDATE_*.py` en `99_MANIFESTS_SHA_LINEAGE`; set esperado no coincide; AUD-009 no está fusionado. |
| 16 | Profile360 | **PASS** | Registry declara 61 secciones; validate fresco reporta `61/61 per model`. |
| 17 | TechExt | **PASS** | Registry declara 284 campos; validate fresco reporta `284/284 per model`. |
| 18 | Research corpus conectado | **PASS** | 24 dominios, 5 pointers activos; validator de field-source contract PASS sobre engine. |
| 19 | Runtime ChatGPT/Copilot 10+N | **EN_REVISION** | Contrato existe y fixture N2 reporta 12, pero no hay ZIP final en ninguno de los 30 casos. |
| 20 | Prompt packs A-J | **EN_REVISION** | Validator de template engine PASS; no se materializaron/validaron packs finales en 30/30 entregas. |
| 21 | Output contracts | **PASS** | Contratos engine/project/agent presentes; la ejecución final falla en lifecycle. |
| 22 | Update/migration contracts | **PASS** | Contrato declara 8 tipos de update, 3 shapes y 9 casos de migración; `validate-update-contract` PASS. |
| 23 | CLI lifecycle | **FAIL** | Superficie de 7 comandos existe, pero `generate` y `validate` frescos fallan. |
| 24 | Generate | **FAIL** | 30/30 `rc=1`; N1: `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`, `FAIL_H160_ATOMIC_FINALIZE_NOT_REACHED`. |
| 25 | Validate | **FAIL** | Fixture fresco: `validators_fail=1`, `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`. |
| 26 | Update | **EN_REVISION** | Contrato normaliza; no hay proyecto fresco aceptado y AUD-010 no está fusionado. |
| 27 | Migrate | **EN_REVISION** | Comando existe; no hay proyecto fresco aceptado y AUD-010 no está fusionado. |
| 28 | Matriz N1..N10 x 3 | **FAIL** | 0/30 PASS, 30/30 FAIL, 1,472.844 s, 0 timeouts. |
| 29 | Mutation/self-test | **FAIL** | 465/506; 41 FAIL; positive fixture FAIL; restoration FAIL. |
| 30 | Estados PASS vs EN_REVISION | **PASS** | `governance_state_check`: CONSISTENT, 0 contradicciones activas; superficies internas superseded. |
| 31 | Windows-safe remap | **PASS** | 487 mappings, 475 del motor, 0 collisions/missing/stale; H62 y consumidores resueltos. |
| 32 | Security Lite | **PASS** | 0 secretos de alta confianza. |
| 33 | Intake Audit | **PASS** | 0 failures; 1,060 archivos físicos incluyendo `.git`; caveat de path histórico no bloqueante. |
| 34 | Demo hardcoding guard | **PASS** | 0 branches activos, 0 referencias prohibidas, 30 casos no-Demo. |
| 35 | Baseline scanner | **PASS** | AUD-003 scope PASS/PARTIAL_PASS; current tree íntegro. |
| 36 | No-bloat/no-history scanner | **PASS** | 0 duplicados injustificados y 0 conflictos de movimiento. |
| 37 | Validator entrypoint scanner | **EN_REVISION** | `validator_entrypoint_check.py` no existe en main; el commit AUD-009 no está fusionado. |
| 38 | Governance state check | **PASS** | `CONSISTENT`; `EN_REVISION/M02_FAIL`; 0 contradicciones activas. |

## 6. Resultado de scanners

| Scanner/check | rc | Resultado | Datos principales |
|---|---:|---|---|
| `tools/audit/intake_audit.py --repo-root .` | 0 | PASS | 0 failures; longest relative path 161, histórica |
| `tools/audit/security_lite_scan.py --repo-root .` | 0 | PASS | 0 patrones de secreto de alta confianza |
| `tools/audit/governance_state_check.py --repo-root .` | 0 | CONSISTENT | 0 contradicciones activas |
| `tools/audit/windows_path_remap_check.py --repo-root .` | 0 | PASS | 5,838 referencias; 0 stale/missing |
| `tools/audit/no_bloat_no_history_check.py --repo-root .` | 0 | PASS | 0 unjustified duplicates; 0 active H routes |
| `tools/audit/demo_hardcoding_check.py --repo-root .` | 0 | PASS | 0 named branches; 30 non-Demo cases |
| `tools/audit/baseline_scanner.py --repo-root .` | 0 | PASS | 979/979; aggregate match |
| `python -m unittest discover -s tests/intake -v` | 0 | PASS | 26 tests OK; 1 skip Unix SIGALRM |
| `VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL.py engine/IDUNEX` | 0 | PASS | validators_fail=0 |
| `VALIDATE_PROMPT_PACK_STRUCTURE.py engine/IDUNEX` | 0 | PASS | engine template A-J |
| `VALIDATE_FIELD_SOURCE_TRACE_LEDGER.py engine/IDUNEX` | 0 | PASS | engine ledger contract |
| `VALIDATE_AGENT_RUNTIME_MARKDOWN_STRICT.py engine/IDUNEX` | 0 | PASS | 46 clauses |
| `VALIDATE_IDUNEX_RUNTIME.py` | 1 | FAIL | validators_fail=3 |
| `validator_entrypoint_check.py` | - | EN_REVISION | ausente en main |

### 6.1 Fallos del validator runtime

```text
ACTIVE_VALIDATORS_EXACT_SET
DOCUMENT_TRUTHFULNESS_PARITY_H245_H260
DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY
```

Detalles:

- set actual: 17 scripts `VALIDATE_*.py`; set esperado: 18 nombres; 11 esperados faltan y 10 nombres remapeados aparecen como inesperados;
- paridad documental: faltan tokens de estado fail-closed en superficies `00_INDEX` y release histórica;
- `MASTER_GOVERNANCE_VALIDATION_CONTRACT.json` no está sincronizado.

## 7. Matriz N1..N10 x tres niveles

Comando:

```text
python IDUNEX_PROJECT_MATRIX_31_RUNNER.py \
  --work <audit-work>/matrix_work \
  --output-dir <audit-work>/matrix_output \
  --timeout 300 --stream-progress
```

El runner ejecutó exactamente 30 casos no-Demo. No se usó `--keep-work`; los directorios/ZIP temporales se retiraron. Los treinta casos terminaron sin timeout y con `generate_rc=1`.

| N | low/basic | intermediate | full/complete |
|---:|---|---|---|
| 1 | FAIL (10.094 s) | FAIL (14.344 s) | FAIL (13.500 s) |
| 2 | FAIL (14.016 s) | FAIL (25.688 s) | FAIL (24.296 s) |
| 3 | FAIL (18.297 s) | FAIL (24.844 s) | FAIL (28.891 s) |
| 4 | FAIL (22.437 s) | FAIL (31.766 s) | FAIL (40.015 s) |
| 5 | FAIL (28.609 s) | FAIL (36.547 s) | FAIL (63.437 s) |
| 6 | FAIL (31.516 s) | FAIL (46.906 s) | FAIL (67.266 s) |
| 7 | FAIL (36.907 s) | FAIL (54.937 s) | FAIL (90.437 s) |
| 8 | FAIL (40.844 s) | FAIL (59.640 s) | FAIL (117.218 s) |
| 9 | FAIL (46.500 s) | FAIL (63.281 s) | FAIL (136.641 s) |
| 10 | FAIL (51.984 s) | FAIL (72.234 s) | FAIL (159.235 s) |

Resumen:

```text
case_count=30
pass_count=0
fail_count=30
PROJECT_N1_N10_X3_MATRIX_PASS_COUNT=0/30
elapsed_seconds=1472.844
generate_rc=1 in 30/30
generate_timeout=false in 30/30
FAIL_ZIP_OR_COMPANION_MISSING in 30/30
```

La ejecución N1 aislada, con el mismo input básico del runner y sin inyectar un SHA falso, produjo:

```text
result=FAIL
fail_codes=[FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE, FAIL_H160_ATOMIC_FINALIZE_NOT_REACHED]
delivery_status=DELIVERY_BLOCKED
```

`resolve_engine_zip_sha256()` solo acepta `IDUNEX_ENGINE_ZIP_SHA256` o un companion localizado en rutas predefinidas. El baseline corregido actual es un SHA agregado de árbol, no un ZIP de release; no se sustituyó por el SHA histórico ni se inventó un valor.

## 8. Mutation/self-test

Comando:

```text
python IDUNEX_PROJECT_FACTORY_v1.0.0.py mutation-self-test \
  --work <audit-work>/mutation_work --summary \
  --output-json <audit-work>/mutation_result.json
```

| Métrica | Resultado |
|---|---:|
| Mutation count | 506 |
| PASS | 465 |
| FAIL | 41 |
| Positive fixture | FAIL |
| Restoration retest | FAIL |
| Bounded time | PASS |
| Resultado global | FAIL |

Los casos 466..506 no ejecutaron su mutación específica porque el fixture positivo ya estaba fallando. La revalidación directa del fixture mostró la causa:

```text
validators_fail=1
fail_codes=[FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE]
Profile360=61/61 per model
TechExt=284/284 per model
runtime_upload_count=12 for N2
```

El resumen CLI reemplaza esa causa específica por `FAIL_UNCLASSIFIED_EXECUTABLE_FAILURE_MISSING_FAILCODE`. Esta pérdida de diagnóstico no convierte la suite en PASS.

## 9. Comparación con M02 anterior

| Área | M02 anterior | Re-auditoría AUD-012 | Cambio |
|---|---|---|---|
| Baseline actual | FAIL/no reproducible | PASS, 979/979 y SHA agregado reproducido | Corregido |
| Windows remap | FAIL, rutas stale | PASS, 0 stale/missing/collision | Corregido |
| No-bloat/no-history | FAIL | PASS en scanner activo | Corregido |
| Demo hardcoding | FAIL | PASS, 0 branches por nombre | Corregido |
| Gobierno raíz | Contradicciones activas | CONSISTENT, 0 contradicciones activas | Corregido |
| Generate Windows | FAIL por `SIGALRM` | Ya no falla por SIGALRM; falla por H113/atomic finalize | Bloqueante cambiado |
| Matriz 30 casos | 0/30 | 0/30 | No corregido globalmente |
| Mutation | 503/506 | 465/506 | Regresión de cierre por fixture H113 |
| Validator único | FAIL | FAIL; AUD-009 no fusionado | No corregido en main |
| CLI paths update/migrate | FAIL relativo | EN_REVISION; AUD-010 no fusionado | No presente en main |

## 10. Hallazgos bloqueantes

### B-01 - Generate no puede publicar una entrega desde el baseline actual

**Evidencia:** 30/30 casos `rc=1`; N1 aislado con `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE` y `FAIL_H160_ATOMIC_FINALIZE_NOT_REACHED`.

**Impacto:** no hay ZIP, companion, testzip ni validate final. Bloquea CLI lifecycle, output contracts ejecutables, runtime/prompt packs de entrega y la matriz 30/30.

### B-02 - Mutation/self-test no cierra y pierde el fail code causal en el resumen

**Evidencia:** 465/506, positive fixture FAIL, restoration FAIL. Causa directa: `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`; resumen CLI: `FAIL_UNCLASSIFIED_EXECUTABLE_FAILURE_MISSING_FAILCODE`.

**Impacto:** incumple PASS total y debilita la trazabilidad forense del fallo.

### B-03 - Validator runtime autoritativo declarado falla

**Evidencia:** `VALIDATE_IDUNEX_RUNTIME.py` retorna rc=1, `validators_fail=3`, con los tres códigos enumerados en 6.1.

**Impacto:** incumple `VALIDATORS_FAIL=0` y `FAIL_CODES=[]`.

### B-04 - AUD-009 no está en main

**Evidencia Git:** commit `e9a6b63111ca` (`AUD-009 consolidate validator entrypoint`) no es ancestro de `27a4961`; `tools/audit/validator_entrypoint_check.py` está ausente.

**Impacto:** no existe enforcement del entrypoint único en el commit auditado; permanecen múltiples ejecutables de validación.

### B-05 - AUD-010 no está en main y update/migrate no son demostrables sobre un proyecto fresco aceptado

**Evidencia Git:** commit `70fa98facbb1` (`AUD-010: normalize related CLI paths`) no es ancestro de `27a4961`.

**Impacto:** la corrección documentada de rutas relativas no pertenece a la base auditada. Sin generate aceptado, no se completó una matriz fresca de update/migrate sin recurrir a evidencia histórica o a un SHA inyectado.

## 11. Hallazgos no bloqueantes y limitaciones

1. El worktree en una ruta profunda falló inicialmente por nombres absolutos demasiado largos dentro de `14_HISTORICAL_NON_AUTHORITY`; en ruta corta y con `core.longpaths=true` se materializó 100%. El scanner Windows-safe pasa y la ruta relativa de 161 caracteres está en histórico, por lo que se registra como caveat no bloqueante.
2. Los seis carriers de manifiesto incluyen dos grupos de duplicados exactos, ambos explícitamente justificados por AUD-008. No se reinterpreta esa allowlist como prueba del lifecycle.
3. El ZIP histórico recibido sigue ausente por política. No es el baseline actual ni se usó para simular un release.
4. `validate-update-contract` pasa para un contrato `set_wardrobe`, pero esto acredita la normalización del contrato, no una actualización completa de proyecto.

## 12. Comandos de evidencia principales

```text
git fetch origin main --prune
git switch -c audit/AUD-012-m02-reaudit-post-fixes origin/main
git -c core.longpaths=true worktree add --detach <short-path> origin/main

python tools/audit/intake_audit.py --repo-root .
python tools/audit/security_lite_scan.py --repo-root .
python tools/audit/governance_state_check.py --repo-root .
python tools/audit/windows_path_remap_check.py --repo-root .
python tools/audit/no_bloat_no_history_check.py --repo-root .
python tools/audit/demo_hardcoding_check.py --repo-root .
python tools/audit/baseline_scanner.py --repo-root .
python -m unittest discover -s tests/intake -v

python engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py
python engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL.py engine/IDUNEX
python engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_PROMPT_PACK_STRUCTURE.py engine/IDUNEX
python engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_FIELD_SOURCE_TRACE_LEDGER.py engine/IDUNEX
python engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_AGENT_RUNTIME_MARKDOWN_STRICT.py engine/IDUNEX

python engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py --work <audit-work>/matrix_work --output-dir <audit-work>/matrix_output --timeout 300 --stream-progress
python engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py mutation-self-test --work <audit-work>/mutation_work --summary --output-json <audit-work>/mutation_result.json
```

Todos los scanners de baseline se ejecutaron sin `--write`.

## 13. Control de cambios y no-expansión

- Archivos modificados bajo `engine/IDUNEX/`: **0**.
- Proyecto Demo generado: **no**.
- Release creado: **no**.
- Tag creado: **no**; 0 tags locales observados antes del commit documental.
- Issues cerradas: **0**.
- Estado convertido a OFICIAL: **no**.
- `governance/CURRENT_STATE.json` modificado: **no**.
- Único cambio previsto en el PR: este informe documental.

## 14. Decisión final y recomendación

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=M02_FAIL
M03_ADVERSARIAL=BLOCKED
READY_FOR_PROJECT_DEMO_GENERATION=FALSE
RELEASE_AUTHORIZED=FALSE
TAG_AUTHORIZED=FALSE
```

**Decisión:** `M02_FAIL`.

**M03 queda bloqueada.** No corresponde generar Proyecto Demo, release o tag.

Se recomienda abrir issues derivados, sin cerrar los existentes, para:

1. hacer resoluble y verificable la autoridad SHA del baseline corregido durante `generate`, sin usar el SHA histórico como sustituto;
2. corregir la suite mutation para que el fixture positivo y la restauración pasen y el fail code causal no se pierda;
3. fusionar o reaplicar AUD-009 sobre el `main` vigente y recomputar el validator único;
4. fusionar o reaplicar AUD-010 sobre el `main` vigente y ejecutar matriz update/migrate fresca;
5. repetir M02 desde un commit congelado solo cuando runtime validator, 30/30 y 506/506 pasen sin workaround.

---

**Declaración forense:** este informe no modifica el motor ni sustituye `governance/CURRENT_STATE.json`. Los PASS internos e históricos fueron tratados como afirmaciones a contrastar y no como decisión.
