# IA-IDUNEX-ReauditoriaAdversarialM03PostPR44-20260721-v1-EN_REVISION

**Tipo:** Informe de reauditoría adversarial M03 del árbol actual  
**ID de control:** `AUD-027-M03-POST-PR44`  
**Fecha:** `2026-07-21`  
**Versión:** `v1`  
**Estado documental:** `EN_REVISION`  
**Repositorio:** `LatinosFlow/IDUNEX`  
**Issue de control:** `#50`  
**Issue padre:** `#46`  
**Workflow:** `IDUNEX M03 Adversarial Reaudit`  
**Run:** `29870466999`  
**Job:** `88769080352`  
**Commit auditado:** `4357093167feea65799f295dfbb50295cfe84b91`  
**Motor:** `EN_REVISION`  
**CREATIVE_OUTPUT_CERTIFIED:** `false`

---

## 1. Resumen ejecutivo

Se recomputó la evidencia adversarial M03 sobre el árbol vigente posterior al PR #44 y posterior a la incorporación del harness reconstruido mediante PR #51.

El workflow terminó con todos los steps obligatorios en `success`, generó un artifact externo completo y cerró técnicamente con:

- `technical_result=PASS`;
- 25/25 casos M03 `PASS`;
- 25/25 restauraciones `PASS`;
- lineage 2 `RECUPERADO_EXACTO`, 23 `RECONSTRUIDO_TRAZABLE`, 0 `NO_RECUPERABLE`;
- validator global `PASS`;
- matriz N1..N10 x3: 30/30 `PASS`;
- mutation/self-test: 506/506 `PASS`;
- fixture positivo `PASS`;
- restauración mutacional `PASS`;
- identidad física del motor preservada antes y después;
- repositorio limpio después de la suite;
- gobernanza no-release preservada.

El harness histórico original `22b-adversarial-harness-final.json` no fue recuperado. Por tanto, esta reauditoría no declara equivalencia histórica byte a byte. Los 23 casos reconstruidos validan contratos vigentes trazables del motor actual.

La evidencia descargada fue revisada de forma independiente y mostró consistencia entre el digest publicado por GitHub, el ZIP descargado, los 132 archivos internos, los resultados individuales, los RC, el lineage, el validator, la matriz, mutation y los hashes pre/post.

**Determinación documental de este informe:**

`M03_PASS_RECOMPUTED_POST_PR44`

Esta determinación significa que el árbol actual superó la matriz M03 vigente y trazable. No significa que el harness histórico perdido haya sido recuperado.

La determinación aplica únicamente al motor identificado por el tree SHA y el commit auditados. No autoriza Proyecto 000 Demo, release, tag, estado `OFICIAL`, cierre productivo ni certificación creativa.

---

## 2. Autoridad técnica auditada

| Campo | Valor |
|---|---|
| Branch | `main` |
| Commit | `4357093167feea65799f295dfbb50295cfe84b91` |
| Scope | `engine/IDUNEX` |
| Archivos | `981` |
| Bytes | `47,302,063` |
| Engine tree SHA-256 | `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9` |
| M02 actual | `M02_PASS_RECOMPUTED_POST_PR44` |
| Estado global | `EN_REVISION` |
| Demo autorizado | `false` |
| Release autorizado | `false` |
| Tag autorizado | `false` |
| Cierre productivo autorizado | `false` |
| Certificación creativa | `false` |

El commit auditado es el HEAD de `main` usado por el workflow. El árbol físico del motor coincide con el tree SHA esperado y con los manifiestos vigentes.

---

## 3. Evidencia GitHub Actions

### 3.1 Ejecución

- Workflow run ID: `29870466999`
- Job ID: `88769080352`
- Job: `M03 adversarial technical evidence`
- Estado: `completed`
- Conclusión: `success`
- Attempt: `1`
- Head branch: `main`
- Head SHA: `4357093167feea65799f295dfbb50295cfe84b91`

Todos los steps obligatorios cerraron en `success`:

1. Checkout del ref congelado.
2. Python 3.11.
3. Instalación de dependencia fijada.
4. Inicialización de evidencia aislada.
5. Preflight de repositorio y motor.
6. Validación de lineage 25/25.
7. Harness adversarial completo.
8. Captura del validator global.
9. Matriz N1..N10 x3.
10. Mutation/self-test.
11. Postflight de identidad y restauración.
12. Consolidación de evidencia.
13. Upload del artifact.
14. Gate técnico final.

### 3.2 Artifact

| Campo | Valor |
|---|---|
| Artifact ID | `8511538539` |
| Nombre | `idunex-m03-adversarial-29870466999-attempt-1` |
| Tamaño | `136,824` bytes |
| Digest GitHub | `sha256:76df161607bc665c6d8a7bbbcbea0a88e6ef38fb0a86a80a9ac501417281343a` |
| Digest recomputado | `76df161607bc665c6d8a7bbbcbea0a88e6ef38fb0a86a80a9ac501417281343a` |
| Entradas internas | `132` |
| ZIP test | `PASS` |
| Duplicados de nombre | `0` |
| Rutas inseguras | `0` |
| Expiración GitHub | `2026-08-20T21:59:17Z` |

El digest recomputado coincide exactamente con el digest publicado por GitHub.

El artifact debe conservarse fuera del repositorio, junto con su companion SHA-256.

---

## 4. Preflight y postflight

### 4.1 Preflight

Fuente: `identity/PREFLIGHT.json`.

| Control | Resultado |
|---|---|
| Motor presente | `PASS` |
| File count | `981` |
| Byte count | `47,302,063` |
| Tree SHA esperado | Coincide |
| Baseline manifest | Coincide |
| Repository manifest | Coincide |
| Repositorio limpio | `true` |
| `.pyc` o `__pycache__` | Ninguno |
| Gobernanza no-release | `PASS` |
| Resultado | `PASS` |
| Fail codes | `[]` |

### 4.2 Postflight

Fuente: `identity/POSTFLIGHT.json`.

| Control | Resultado |
|---|---|
| File count | `981` |
| Byte count | `47,302,063` |
| Tree SHA | Igual al preflight |
| Repositorio limpio | `true` |
| `.pyc` o `__pycache__` | Ninguno |
| Restauración | `PASS` |
| Fail codes | `[]` |

No se detectó mutación persistente del motor ni del repositorio.

---

## 5. Lineage M03

Fuentes:

- `lineage/m03_adversarial_lineage.json`;
- `lineage/LINEAGE_VALIDATION.json`;
- informe histórico M03;
- informe de recuperación del harness;
- issue `#50`.

Resultado:

| Clasificación | Conteo |
|---|---:|
| `RECUPERADO_EXACTO` | 2 |
| `RECONSTRUIDO_TRAZABLE` | 23 |
| `NO_RECUPERABLE` | 0 |
| **TOTAL** | **25** |

Contratos verificados:

- IDs históricos exactos `01`…`25`;
- runtime IDs `M03-01`…`M03-25`;
- casos exactos únicamente `18` y `19`;
- `historical_harness_recovered=false`;
- autoridad de resultado:
  `CURRENT_ENGINE_CONTRACT_NOT_HISTORICAL_BYTE_EQUIVALENCE`;
- ninguna ausencia histórica fue presentada como evidencia exacta;
- ninguna prueba fue eliminada o convertida en skip silencioso.

---

## 6. Harness adversarial

Fuente principal: `M03_ADVERSARIAL_RESULT.json`.

Resultado consolidado:

- `case_count=25`;
- `executed_case_count=25`;
- `pass_count=25`;
- `fail_count=0`;
- `restoration_pass_count=25`;
- `exact_recovered_count=2`;
- `traceable_reconstructed_count=23`;
- `non_recoverable_count=0`;
- `reconstruction_truthfulness=PASS`;
- `result=PASS`;
- `fail_codes=[]`.

La revisión independiente confirmó:

- 25 JSON individuales presentes;
- 25 juegos de stdout, stderr y RC presentes;
- IDs únicos y completos;
- resultado `PASS` en los 25 casos;
- restauración `PASS` en los 25 casos;
- hash del motor idéntico antes y después de cada caso;
- expected failcodes iguales a actual failcodes;
- ningún failcode de harness;
- ningún caso omitido.

Los casos 24 y 25 retornaron `RC=1` en sus scanners adversariales, conforme a su contrato de bloqueo esperado. El resultado del caso permaneció `PASS` porque el rechazo era precisamente la conducta esperada.

---

## 7. Cobertura adversarial

Los 25 frentes preservados cubren:

1. Path traversal.
2. Rutas absolutas y relativas peligrosas.
3. Separación ENGINE/PROJECT/AGENT.
4. Demo sin autorización.
5. Release/tag sin autorización.
6. `MOTOR_STATUS=OFICIAL` forzado.
7. `M02_PASS` no sustentado.
8. Inputs low-info.
9. Inputs ambiguos.
10. Inputs contradictorios.
11. Payloads grandes.
12. Caracteres inusuales.
13. Paths Windows/POSIX.
14. Mutación de manifiesto.
15. Mutación de SHA companion.
16. Update/migrate fuera de project root.
17. Contrato N1..N10 x3.
18. Mutation/self-test.
19. Validator global.
20. Governance state adversarial.
21. No-bloat/no-history.
22. Hardcoding de Demo.
23. Baseline reproducible.
24. Security Lite adversarial.
25. Intake Audit adversarial.

Los casos 18 y 19 conservaron comando y resultado agregados exactos. Los demás casos fueron reconstruidos desde autoridades vigentes y trazabilidad documental.

---

## 8. Validator global

Fuentes:

- `cases/M03-19.stdout.log`;
- `checks/runtime-validator.stdout.log`;
- `checks/runtime-validator.rc`.

Resultado:

- `RC=0`;
- `result=PASS`;
- `validators_fail=0`;
- `blocking_warnings=0`;
- `fail_codes=[]`.

La captura de validator procede de la ejecución real del caso exacto 19 y fue reutilizada por el gate global sin ejecutar una segunda copia innecesaria.

---

## 9. Matriz N1..N10 x3

Fuentes:

- `matrix/H238_FULL_31_PROJECT_MATRIX_SUMMARY.json`;
- `matrix/H238_FULL_31_PROJECT_MATRIX_PARTIAL.json`;
- `matrix/H238_FULL_31_PROJECT_MATRIX.csv`.

Resultado:

- `case_count=30`;
- `pass_count=30`;
- `fail_count=0`;
- `PROJECT_N1_N10_X3_MATRIX_PASS_COUNT=30/30`;
- `result=PASS`.

Cobertura:

| Modalidad | Casos | PASS | FAIL |
|---|---:|---:|---:|
| BASIC | 10 | 10 | 0 |
| INTERMEDIATE | 10 | 10 | 0 |
| COMPLETE | 10 | 10 | 0 |
| **TOTAL** | **30** | **30** | **0** |

La revisión independiente confirmó:

- 30 case IDs únicos;
- 30 filas CSV;
- generate RC `0`;
- validate RC `0`;
- companion SHA `PASS`;
- ZIP test `PASS`;
- Profile360 `61/61` por modelo;
- TechExt `284/284` por modelo;
- runtime ChatGPT y Copilot `10+N`;
- field-source trace ledger por modelo;
- active runtime upload manifest presente;
- `CREATIVE_OUTPUT_CERTIFIED=false`;
- sin timeouts;
- sin process kill posterior a completion;
- sin fail codes.

---

## 10. Mutation/self-test

Fuente: `mutation/mutation-result.json`.

Resultado:

- `result=PASS`;
- `mutation_count=506`;
- `cases_pass=506`;
- `cases_fail=0`;
- `positive_fixture=PASS`;
- `restoration_retest=PASS`;
- `delivery_status=DELIVERY_PASS`;
- `validators_fail=0`;
- `blocking_warnings=0`;
- `fail_codes=[]`.

La evidencia concuerda con el RC `0` del comando y con el resumen consolidado.

---

## 11. Códigos de retorno de gates

| Gate | RC |
|---|---:|
| Harness M03 | `0` |
| Validator global | `0` |
| Matriz 30 casos | `0` |
| Mutation 506 casos | `0` |

No faltó ningún RC obligatorio.

---

## 12. Validación independiente del artifact

Resultado:

`INDEPENDENT_ARTIFACT_VALIDATION=PASS`

Controles realizados:

1. Recomputación SHA-256 del ZIP.
2. `ZipFile.testzip()` sin errores.
3. Conteo de 132 entradas.
4. Detección de nombres duplicados.
5. Detección de rutas absolutas o traversal.
6. Presencia de resultados y logs de 25 casos.
7. Paridad de RC individuales.
8. Paridad expected/actual failcodes.
9. Paridad de hash de motor pre/post por caso.
10. Paridad entre resultado M03 y resumen consolidado.
11. Validación de lineage 25/2/23/0.
12. Validación del validator global.
13. Validación JSON/CSV de la matriz 30/30.
14. Validación mutation 506/506.
15. Verificación de gobernanza no-release.
16. Verificación de `historical_harness_recovered=false`.
17. Verificación de `CREATIVE_OUTPUT_CERTIFIED=false`.

No se detectaron inconsistencias materiales.

---

## 13. Limitaciones y verdad forense

Esta auditoría conserva las siguientes limitaciones:

1. `22b-adversarial-harness-final.json` continúa no recuperado.
2. Los inputs exactos y resultados individuales históricos de 23 casos no existen.
3. Los 23 casos reconstruidos prueban contratos vigentes trazables.
4. No se afirma igualdad histórica byte a byte.
5. El PASS se limita al commit y engine tree SHA auditados.
6. Cualquier cambio posterior en `engine/IDUNEX` invalida la promoción automática de este PASS y exige recomputación.
7. El PASS técnico no habilita por sí solo el Proyecto 000 Demo.

---

## 14. Determinación

Con la evidencia técnica y la validación independiente disponibles:

`M03_PASS_RECOMPUTED_POST_PR44`

Calificación:

- 25/25 casos adversariales `PASS`;
- 25/25 restauraciones `PASS`;
- validator global `PASS`;
- matriz 30/30 `PASS`;
- mutation 506/506 `PASS`;
- identidad física preservada;
- truthfulness de reconstrucción `PASS`.

La determinación se vincula exclusivamente a:

- commit:
  `4357093167feea65799f295dfbb50295cfe84b91`;
- engine tree SHA-256:
  `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9`;
- artifact SHA-256:
  `76df161607bc665c6d8a7bbbcbea0a88e6ef38fb0a86a80a9ac501417281343a`.

---

## 15. Estado posterior propuesto

```text
M02_CURRENT_TREE=M02_PASS_RECOMPUTED_POST_PR44
M03_CURRENT_TREE=M03_PASS_RECOMPUTED_POST_PR44
CURRENT_TREE_AUDIT=PASS_PENDING_DEMO_AUTHORITY_RECONCILIATION
MOTOR_STATUS=EN_REVISION
DEMO_REGENERATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
TAG_AUTHORIZED=false
PRODUCTIVE_CLOSURE_AUTHORIZED=false
CREATIVE_OUTPUT_CERTIFIED=false
```

El siguiente gate no es técnico M02/M03. Es documental y procedural:

`NEW_CONTROLLED_DEMO_AUTHORIZATION_REQUIRED`

Debe emitirse una autorización nueva, no reutilizar AUD-025 v1.

---

## 16. Alcance y reversión

Este informe no modifica:

- `engine/IDUNEX`;
- `governance/CURRENT_STATE.json`;
- factory;
- validator;
- Proyecto 000 Demo;
- release;
- tag.

Reversión:

- cerrar el PR sin fusionar; o
- revertir el commit documental y la actualización del manifiesto.

La reversión no afecta el motor ni los artifacts externos.

---

## 17. Veredicto único

`M03_PASS_RECOMPUTED_POST_PR44`

Estado documental:

`EN_REVISION`

Estado del motor:

`EN_REVISION`

Proyecto 000 Demo:

`BLOQUEADO_HASTA_NUEVA_AUTORIZACION_CONTROLADA`
