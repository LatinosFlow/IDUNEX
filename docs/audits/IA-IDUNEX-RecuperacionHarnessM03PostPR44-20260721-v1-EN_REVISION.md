# IA-IDUNEX — Recuperación del harness M03 post-PR44

**Expediente:** `AUD-027`
**Repositorio:** `LatinosFlow/IDUNEX`
**Fecha:** `2026-07-21`
**Estado:** `EN_REVISION`
**Tipo de entrega:** implementación controlada de Fase B
**Autoridad de control:** issue #50, comentarios `5038841885` y `5038887068`

## 1. Estado y límites de esta entrega

Esta entrega versiona una reconstrucción trazable del harness adversarial M03 fuera del motor. No cambia el estado de gobierno y no promueve la evidencia histórica al árbol actual.

- `M03_CURRENT_TREE=NOT_RECOMPUTED_POST_PR44`
- `DEMO=BLOCKED_PENDING_CURRENT_TREE_M03`
- `CREATIVE_OUTPUT_CERTIFIED=false`
- `M03_DECISION=NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY`
- Documento: `EN_REVISION`

La ejecución local descrita aquí valida la implementación y los 25 contratos individuales. La recomputación técnica completa requiere posteriormente el workflow manual y revisión independiente de su artifact. El workflow no fue ejecutado desde `main` durante esta fase.

## 2. Base sincronizada y congelada

La implementación partió de un checkout limpio y materializado en la autoridad aprobada:

| Control | Resultado |
|---|---:|
| Base commit | `b46929799f02ee686c6fbb0dc531f71e656914f0` |
| Scope | `engine/IDUNEX` |
| File count | `981` |
| Byte count | `47,302,063` |
| Engine tree SHA-256 | `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9` |
| Working tree antes de implementar | limpio |

No se implementó sobre el checkout anterior `66eb8a2...`.

## 3. Pérdida forense del harness original

La Fase A confirmó una brecha forense real:

- `22b-adversarial-harness-final.json` no está versionado;
- el archivo no aparece en refs o commits alcanzables ni en objetos Git inalcanzables;
- el PR histórico #32 fue documental y añadió únicamente el informe M03;
- no se recuperaron los inputs, mutaciones, resultados individuales o restauraciones byte a byte del harness original;
- sí se recuperaron los 25 IDs y las 25 descripciones históricas;
- solo los casos 18 y 19 conservan comando, salida agregada esperada y contrato operativo suficientes para recuperación exacta.

Fuentes históricas principales:

1. `docs/audits/IA-IDUNEX-AuditoriaAdversarialM03-20260717-v1-EN_REVISION.md`.
2. PR #32 y commits documentales `542b70b8...` / `60379240...`.
3. Comentario de descubrimiento `issuecomment-5038841885`.
4. Decisión de control `issuecomment-5038887068`.

## 4. Lineage 25/25

El archivo `tests/m03/m03_adversarial_lineage.json` conserva exactamente los IDs históricos `01`…`25` y propone los aliases de runtime `M03-01`…`M03-25`.

Clasificación aprobada y materializada:

| Clasificación | Conteo | IDs |
|---|---:|---|
| `RECUPERADO_EXACTO` | 2 | `18`, `19` |
| `RECONSTRUIDO_TRAZABLE` | 23 | `01`…`17`, `20`…`25` |
| `NO_RECUPERABLE` | 0 | ninguno |

Cada registro separa expresamente:

- `historical_input_status`;
- `historical_failcode`;
- `current_expected_failcodes`;
- contrato autoritativo vigente;
- comportamiento esperado actual;
- método de ejecución;
- restauración;
- evidencia y límites de equivalencia.

Los casos cuyo input histórico es `NO_DOCUMENTADO` no se presentan como recuperación exacta. Los failcodes actuales se identifican como señales vigentes y no se retroatribuyen a la ejecución histórica. Los casos 01 y 16 conservan el único failcode históricamente vinculado a sus IDs; sus inputs exactos continúan no documentados.

## 5. Casos exactos recuperados

### Caso 18 — Mutation/self-test adversarial

Evidencia exacta conservada:

- comando: factory canónico, subcomando `mutation-self-test`, con `--work`, `--summary` y `--output-json`;
- `result=PASS`;
- `mutation_count=506`;
- `cases_pass=506`;
- `cases_fail=0`;
- `positive_fixture=PASS`;
- `restoration_retest=PASS`.

La prueba local comprueba que el binding CLI canónico continúa existiendo. El workflow ejecutará el comando completo una sola vez y aplicará todos los gates anteriores.

### Caso 19 — Validator runtime adversarial

Evidencia exacta conservada:

- comando: `VALIDATE_IDUNEX_RUNTIME.py engine/IDUNEX`;
- `result=PASS`;
- `validators_fail=0`;
- `blocking_warnings=0`;
- `fail_codes=[]`.

El caso 19 ejecuta el validator global real. El workflow reutiliza su stdout, stderr y RC como evidencia del validator para evitar una segunda ejecución equivalente.

## 6. Límites de equivalencia

La reconstrucción no demuestra igualdad byte a byte con el harness perdido. La autoridad de cada resultado es:

`CURRENT_ENGINE_CONTRACT_NOT_HISTORICAL_BYTE_EQUIVALENCE`

En consecuencia:

- se preserva el frente histórico y su descripción;
- la ejecución reconstruida se enlaza a funciones, CLI y scanners vigentes;
- los 23 casos reconstruidos no se renombran como recuperados;
- no se inventan inputs o failcodes históricos;
- el resultado técnico actual no reescribe la evidencia del árbol histórico;
- el artifact futuro será evidencia del commit concreto que ejecute el workflow.

Los casos 17 y 18 enlazan localmente el runner y la CLI canónicos. Sus controles pesados 30/30 y 506/506 son gates independientes del workflow para cumplir la restricción de recursos local sin ocultar su obligatoriedad.

## 7. Arquitectura del nuevo harness

`tests/m03/test_adversarial_harness.py` implementa:

1. Carga y validación fail-closed del lineage.
2. Gates de conteo, IDs, campos obligatorios y clasificación 2/23/0.
3. Rechazo de una fila `NO_DOCUMENTADO` presentada como recuperación exacta.
4. Veinticinco métodos `unittest` explícitos, uno por ID histórico.
5. Un `tempfile.TemporaryDirectory` externo al repositorio por caso.
6. Copia exclusiva de la superficie mínima necesaria en mutaciones de archivo.
7. Restauración de la copia y comparación SHA pre/post cuando aplica.
8. Recomputación del tree SHA del engine antes y después de cada caso.
9. Resultado JSON, stdout, stderr y RC por caso.
10. Consolidado `M03_ADVERSARIAL_RESULT.json` con conteos, restauración, commit, tree SHA y regla de verdad.

El directorio de evidencia es obligatorio fuera del repositorio cuando se configura `M03_EVIDENCE_DIR`. Sin configuración explícita, el harness usa un temporal externo y lo elimina al terminar.

## 8. Uso exclusivo de autoridades vigentes

El harness orquesta, pero no reimplementa el factory ni el validator. Delega a:

- `engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py`;
- `engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py`;
- `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py`;
- `tools/audit/baseline_scanner.py`;
- `tools/audit/demo_hardcoding_check.py`;
- `tools/audit/governance_state_check.py`;
- `tools/audit/no_bloat_no_history_check.py`;
- `tools/audit/windows_path_remap_check.py`;
- `tools/audit/security_lite_scan.py`;
- `tools/audit/intake_audit.py`;
- funciones y CLI actuales expuestas por esas superficies.

No se creó factory paralelo, validator paralelo ni lógica productiva alternativa.

## 9. Workflow manual

`.github/workflows/m03-adversarial.yml` usa exclusivamente `workflow_dispatch`, Python 3.11 y `python-docx==1.2.0`, con permisos `contents: read` y `cancel-in-progress=false`.

El orden de evidencia es:

1. checkout y setup;
2. directorios externos aislados;
3. preflight de commit, conteos, SHA, manifests, limpieza, bytecode y gobierno no-release;
4. gate de lineage 25/25;
5. harness de 25 casos;
6. captura del validator ejecutado por el caso exacto 19;
7. matriz canónica N1..N10 x3;
8. mutation/self-test;
9. postflight de restauración;
10. consolidación Markdown/JSON;
11. upload del artifact con `if: always()`;
12. gate técnico final después del upload.

El gate exige 25/25 casos, 25 restauraciones, clasificación 2/23/0, validator sin fallos o warnings bloqueantes, matriz 30/30, mutation 506/506, fixture positivo, restoration retest, SHA coincidente y repositorio limpio.

## 10. Archivos creados

Únicamente se crean:

1. `tests/m03/__init__.py`.
2. `tests/m03/test_adversarial_harness.py`.
3. `tests/m03/m03_adversarial_lineage.json`.
4. `.github/workflows/m03-adversarial.yml`.
5. `docs/audits/IA-IDUNEX-RecuperacionHarnessM03PostPR44-20260721-v1-EN_REVISION.md`.

No se modifica `engine/IDUNEX`, `governance/CURRENT_STATE.json`, `REPOSITORY_MANIFEST.yml`, Proyecto 000 Demo, releases o tags.

## 11. Pruebas locales ejecutadas y resultados reales

### Harness y lineage

Comando:

```text
python -m unittest tests.m03.test_adversarial_harness -v
```

Resultado real:

- `Ran 26 tests in 52.590s`;
- `OK`;
- 1 test de contrato de lineage;
- 25 casos adversariales individuales;
- `case_count=25`;
- `executed_case_count=25`;
- `pass_count=25`;
- `fail_count=0`;
- `restoration_pass_count=25`;
- `exact_recovered_count=2`;
- `traceable_reconstructed_count=23`;
- `non_recoverable_count=0`;
- `historical_harness_recovered=false`;
- `reconstruction_truthfulness=PASS`;
- engine SHA pre/post `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9`;
- validator global del caso 19: PASS con cero fallos, cero warnings bloqueantes y lista de failcodes vacía.

La evidencia local se escribió fuera del repositorio en un directorio temporal de la sesión. No se versiona como sustituto del futuro artifact de Actions.

### Validaciones ligeras

- compilación sintáctica de `tests/m03/test_adversarial_harness.py`: PASS;
- parseo y gate semántico del lineage JSON: PASS;
- parseo sintáctico YAML de `.github/workflows/m03-adversarial.yml`: PASS;
- regresiones ligeras relacionadas de paths, gobierno, guard nominal, baseline, no-bloat, remap y alias: `Ran 13 tests in 24.751s`, `OK`;
- `git diff --check`: PASS en la iteración de implementación.

No se ejecutaron localmente la matriz completa 30/30 ni mutation 506/506. Se reservan para el workflow manual posterior, conforme a la restricción de recursos de la Fase B.

## 12. Restricciones preservadas

- Ninguna mutación directa en `engine/IDUNEX`.
- Ningún cambio en `governance/CURRENT_STATE.json`.
- Ningún cambio en `REPOSITORY_MANIFEST.yml`.
- Ninguna generación del Demo.
- Ninguna release o tag.
- Ningún cambio de estado productivo.
- Ninguna certificación de output creativo.
- Ninguna fusión del Draft PR durante esta fase.
- Ninguna ejecución del workflow M03 desde `main` durante esta fase.

## 13. Riesgos y limitaciones residuales

1. Los bytes del harness original y sus inputs exactos continúan perdidos.
2. Veintitrés casos prueban contratos actuales trazables, no equivalencia histórica byte a byte.
3. El caso 17 requiere el artifact 30/30 para completar su gate pesado actual.
4. El caso 18 requiere el artifact 506/506 para completar su gate pesado actual.
5. Un PASS local de implementación no sustituye la evidencia de Actions del commit del PR.
6. Cualquier divergencia de failcode, restauración, SHA o conteo en Actions fuerza `technical_result=FAIL` sin eliminar casos ni convertirlos en SKIP.

## 14. Plan de reversión

La reversión consiste en revertir los commits de esta Fase B o eliminar los cinco archivos creados. No requiere restaurar el motor, gobierno, Demo, releases o tags porque esas superficies no se modifican.

Después de revertir se debe confirmar:

- `engine/IDUNEX` mantiene `981` archivos y `47,302,063` bytes;
- tree SHA permanece `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9`;
- `governance/CURRENT_STATE.json` no tiene diff;
- el working tree queda limpio.

## 15. Determinación de esta Fase B

La implementación local del harness está completa y pendiente de revisión del Draft PR. La decisión técnica del árbol actual permanece no declarada hasta ejecutar y revisar la evidencia manual del workflow.

`M03_HARNESS_IMPLEMENTED_PENDING_PR_REVIEW`
