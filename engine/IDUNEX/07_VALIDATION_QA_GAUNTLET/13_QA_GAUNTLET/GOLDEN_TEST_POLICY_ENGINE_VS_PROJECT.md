# GOLDEN_TEST_POLICY_ENGINE_VS_PROJECT

## Separación obligatoria

- El motor puede cerrar con `GOLDEN_TEST_FRAMEWORK_PASS` / `FRAMEWORK_PASS`.
- El motor NO debe declarar `GOLDEN_TEST_REAL_OUTPUT_EXECUTION_PASS`, porque no contiene outputs reales finales de proyectos.
- Project Factory debe exportar golden tests definidos por proyecto.
- Un proyecto técnico requiere `PROJECT_TESTS_DEFINED`.
- Un proyecto productivo 10/10 real requiere `EXECUTED_PASS` con evidencia, sidecar, prompt hash, output hash y lineage por modalidad aplicable.

## Estados permitidos

- FRAMEWORK_PASS
- PROJECT_TESTS_DEFINED
- NOT_EXECUTED
- EXECUTED_PASS
- EXECUTED_FAIL
- NOT_APPLICABLE

## Bloqueos

- `BLOCKED_PROJECT_CLOSE_WITHOUT_GOLDEN_TESTS_DEFINED` si se intenta cerrar proyecto técnico sin matriz.
- `BLOCKED_OUTPUT_GO_TRUE_WITHOUT_SIDECAR_HASH_LINEAGE` si se intenta cerrar output real sin evidencia.
- `BLOCKED_ENGINE_FALSE_REAL_OUTPUT_EXECUTION_PASS` si el motor declara ejecución real que no corresponde.
