# AUD-005 - Ledger de propagación de referencias Windows-safe

**Issue:** `AUD-005` / `#6`
**Fecha:** 2026-07-16
**Alcance:** propagación del remapeo Windows-safe a código, registries, manifiestos y self-tests
**MOTOR_STATUS vigente:** `EN_REVISION`
**M02_RESULT vigente:** `M02_FAIL`

## Autoridad aplicada

- Informe Maestro bajo `governance/authority/REFERENCIA/`.
- `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`.
- `docs/audits/IA-IDUNEX-PlanCorreccionM02-20260716-v1-EN_REVISION.md`.
- `governance/CURRENT_STATE.json`.
- `governance/baseline/WINDOWS_PATH_SAFE_REMAP.json`.
- Issue `AUD-005` / `#6`.

## Causa raíz

El rename Windows-safe se había aplicado al árbol físico, pero no al grafo de referencias. El mapa contenía 487 equivalencias y sus targets existían, mientras que código, registries y los seis manifiestos canónicos todavía conservaban rutas originales inexistentes. El factory y el runtime validator buscaban específicamente el nombre largo anterior de H62, por lo que los casos 452-454 observaban `H62_MATRIX_PROOF_MISSING`.

## Corrección aplicada

- Se reutilizó `WINDOWS_PATH_SAFE_REMAP.json` como única tabla original→segura; no se creó una autoridad paralela.
- `WINDOWS_PATH_SAFE_REMAP.md` documenta el resolver, el comando de lint y las exclusiones históricas/forenses.
- Se agregó `tools/audit/windows_path_remap_check.py`, que resuelve las variantes repo-relative, `IDUNEX/` y engine-relative desde la tabla canónica.
- El lint valida conteo declarado, unicidad, cero colisiones, existencia de los 487 targets, ausencia física de originales, existencia de toda ruta de los seis manifiestos canónicos y cero literales stale en superficies activas gobernadas.
- Se propagaron 3,684 reemplazos mecánicos en 60 archivos activos: factory, runtime validator, validadores auxiliares, registries, contratos, allowlists, evidence pointers y manifiestos.
- `FILE_MANIFEST.json`, `FINAL_TREE_MANIFEST.json`, `HASH_MANIFEST.json`, `MANIFEST.json`, `MANIFEST.txt` y `SHA256SUMS.txt` ahora indexan las 475 rutas físicas remapeadas del motor.
- `FILE_CONNECTEDNESS_LEDGER.json` recibió 419 correcciones de referencias cubiertas por el mapa.
- Factory y runtime validator consumen H62 mediante `99_MANIFESTS_SHA_LINEAGE/H62_CLI_N1_N10_CLEAN_EXIT.json`.
- Se agregó `tests/intake/test_windows_path_remap.py` con pruebas positivas y una mutación negativa que reintroduce una ruta original.
- `.github/workflows/intake.yml` ejecuta el lint y las mutaciones AUD-005 en cada PR a `main`.

Las exclusiones del scanner son autoridad de referencia, documentos forenses de auditoría, el baseline que contiene la propia tabla y `14_HISTORICAL_NON_AUTHORITY`. Esas superficies conservan historia o equivalencias por diseño y no son referencias runtime activas. No se ejecutó limpieza no-history.

## Evidencia de integridad referencial

```text
python -B tools/audit/windows_path_remap_check.py --repo-root .
result=PASS
mapping_count=487
engine_mapping_count=475
mapping_collision_count=0
materialised_original_path_count=0
missing_remapped_target_count=0
indexed_path_count=5826
missing_indexed_path_count=0
stale_reference_surface_count=0
stale_reference_count=0
h62_safe_path_exists=true
h62_consumers_windows_safe=true (factory y runtime validator)
```

Los 5,826 checks corresponden a 971 entradas por cada uno de los cuatro manifiestos JSON y los dos manifiestos de hashes/texto.

## Evidencia H62 y mutation/self-test

Se ejecutó el único entrypoint disponible; no existe selector focal para H18/H19/H20:

```text
python engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py \
  mutation-self-test --work <temp>/aud005-mutation --output-json <temp>/aud005-mutation-result.json --summary

452_H18_PROFILE360_GENERIC_INPUT_FULL_DECOLLISION=PASS
453_H19_PRECHECK_LATE_GENERIC_CLONING_PREVENTED=PASS
454_H20_ADVERSARIAL_N10_GENERIC_COMPLETE_CLI_PROOF=PASS
h20_adversarial_n10_generic_complete.source_proof=99_MANIFESTS_SHA_LINEAGE/H62_CLI_N1_N10_CLEAN_EXIT.json
```

El self-test global permanece **FAIL** (`465/506`, 41 fallos). La causa observada es previa y ajena al remapeo: el fixture positivo queda bloqueado por `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`, y por ello no se ejecutan como PASS los grupos posteriores H69/H71/H90/H113. Este ledger no convierte ese resultado en PASS, no afirma `506/506` y no declara cierre M02.

## Pruebas adicionales

Entorno: Windows, Python del runtime de Codex.

```text
python -B -m unittest tests.intake.test_windows_path_remap -v
Ran 5 tests - OK

python -B -m unittest tests.intake.test_governance_state -v
Ran 3 tests - OK

python -B -m unittest discover -s tests/intake -p 'test_*.py' -v
Ran 11 tests - OK (1 skipped por capacidad Unix no disponible en Windows)

python -B tools/audit/governance_state_check.py --repo-root .
result=CONSISTENT
active_contradiction_count=0
motor_status=EN_REVISION
m02_result=M02_FAIL

JSON parse de los archivos JSON modificados
changed_json_valid=36
```

## Controles de no expansión

- El self-test materializó únicamente `FIXTURE_ONLY_MUTATION_BASE` en un directorio temporal; no generó Proyecto Demo.
- No hay archivos Demo en el diff ni en el workspace temporal de la prueba.
- `governance/CURRENT_STATE.json` no fue modificado.
- No se creó release ni tag; `git tag --points-at HEAD` permanece vacío.
- No se cerró ningún issue y el PR se vincula a `#6` sin palabras de cierre automático.
- No se limpió bloat/no-history y no se consolidó validator único.
- No se modificó lógica Demo.

## Sello de hashes diferido

Este cambio corrige rutas indexadas y referencias, pero no presenta los hashes internos como sello final del árbol modificado. Conforme al plan maestro, la regeneración determinista y el sello criptográfico de manifiestos quedan reservados para `AUD-003`, después de integrar los cambios técnicos. No se crea release/tag ni se declara `M02_PASS`.
