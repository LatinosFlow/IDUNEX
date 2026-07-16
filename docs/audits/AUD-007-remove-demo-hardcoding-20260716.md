# AUD-007 - Ledger de eliminación de acoplamiento activo a Demo

**Issue:** `AUD-007` / `#8`

**Fecha:** 2026-07-16

**Alcance:** separación ENGINE_LEVEL/PROJECT_LEVEL y corrección del self-test de hardcoding

**MOTOR_STATUS vigente:** `EN_REVISION`

**M02_RESULT vigente:** `M02_FAIL`

## Autoridad aplicada

- Informe Maestro bajo `governance/authority/REFERENCIA/`.
- `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`.
- `docs/audits/IA-IDUNEX-PlanCorreccionM02-20260716-v1-EN_REVISION.md`.
- `governance/CURRENT_STATE.json`.
- Issue `AUD-007` / `#8`.

## Clasificación de referencias

| Clase | Tratamiento AUD-007 | Ejemplos |
|---|---|---|
| Documental o histórica permitida | Se conserva; no participa en decisiones runtime. | Informes M02, plan maestro, ADR, README y estado documental. |
| Fixture/input externo permitido | Se conserva fuera del canon activo; requiere una fase posterior y decisión M02 independiente. | Prompt bajo `governance/authority/REFERENCIA/` y documento bloqueado bajo `docs/project-demo/`. |
| Guardia negativa de prueba | Se conserva exclusivamente para inyectar/detectar la comparación prohibida. | `tools/audit/demo_hardcoding_check.py` y `tests/intake/test_demo_hardcoding.py`. |
| Lógica activa prohibida | Eliminada. | La condición `project_name == "Proyecto 000 Demo"` y equivalentes normalizados. |

`tools/audit/demo_hardcoding_check.py` aplica esta clasificación y falla ante cualquier referencia no permitida. El resultado final registra cero branches ejecutables por el nombre protegido y cero referencias literales activas prohibidas.

## Causa raíz

El factory derivaba `is_project_demo` comparando el nombre canónico del proyecto con un nombre propio. Esa decisión activaba un campo de status específico y mantenía gates/registries Demo dentro del canon ENGINE_LEVEL. El caso `463_H27_FACTORY_HARDCODED_DEMO_BRANCH_BLOCKED` declaraba PASS de forma fija y no inspeccionaba la condición real.

## Corrección aplicada

- Se eliminó la comparación por nombre del factory.
- La política especial se reemplazó por el input booleano neutral `external_validation_required`, válido para cualquier nombre de proyecto.
- Los estados y campos activos `PROJECT_DEMO_PASS*` se reemplazaron por `PROJECT_EXTERNAL_VALIDATION_REQUIRED` y `PROJECT_EXTERNAL_VALIDATION_PASS`.
- `PROJECT_DEMO_PASS_GATE` y `DEMO_TEMPLATE_READINESS` conservan sus rutas solo por compatibilidad, pero quedan clasificados como contratos externos posteriores, con `engine_runtime_active=false`, sin selección por nombre y bloqueados por `M02_FAIL`.
- Los rules Demo se retiraron de `required_rule_ids`, `STABLE_GOVERNANCE_RULE_IDS` y required paths/tokens activos. Sus entradas se conservan como trazabilidad externa, con `active_paths=[]` y `validator_or_factory_affected=NONE_ENGINE_LEVEL`.
- El runner con nombre legado `IDUNEX_PROJECT_MATRIX_31_RUNNER.py` conserva la ruta por compatibilidad, pero ejecuta exactamente 30 casos no-Demo: N1..N10 × basic/intermediate/complete. Los resúmenes activos usan contrato `N1_N10_X3` y filtran cualquier fila legado al reanudar.
- El self-test del factory ahora construye el caso 463 desde un scan AST real. Detecta comparaciones exactas, concatenadas y equivalentes por normalización; una reintroducción produce `result=FAIL`.
- El workflow de intake ejecuta el guard AUD-007 y sus mutaciones.

## Cambio contractual mínimo documentado

El cambio de `PROJECT_DEMO_PASS*` a `PROJECT_EXTERNAL_VALIDATION_*` es necesario para dejar de proyectar una instancia específica sobre todos los proyectos generados. No cambia naming, estructura N1, runtime 10+N, Profile360, TechExt, output ZIP ni contratos de update/migration. El nuevo flag es opcional, booleano y `false` por defecto.

## Evidencia ejecutada

```text
python -B tools/audit/demo_hardcoding_check.py --repo-root .
result=PASS
active_named_project_branch_count=0
prohibited_active_literal_reference_count=0
runner_case_count=30
runner_contains_demo_case=false
gate_findings=[]
registry_findings=[]

python -B -m unittest discover -s tests/intake -p 'test_*.py' -v
Ran 18 tests - OK (1 skipped por capacidad Unix ausente en Windows)

python -B tools/audit/intake_audit.py --repo-root .
result=PASS

python -B tools/audit/windows_path_remap_check.py --repo-root .
result=PASS; stale_reference_count=0; missing_remapped_target_count=0

python -B tools/audit/governance_state_check.py --repo-root .
result=CONSISTENT
motor_status=EN_REVISION
m02_result=M02_FAIL
ready_for_project_demo_generation=false

python -B engine/IDUNEX/07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/VALIDATE_PROMPTS_PROJECT_POLICY.py engine/IDUNEX
result=PASS; VALIDATORS_FAIL=0
```

La prueba N1 materializa temporalmente `Proyecto Control Alfa`, verifica el status genérico y ejecuta `validate_project`. La validación no presenta fallos Demo; conserva únicamente el bloqueante previo `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`, ya documentado por AUD-005. No se generó ZIP ni proyecto Demo.

El entrypoint real `mutation-self-test` se ejecutó sin selector focal:

```text
mutation_count=506
cases_pass=465
cases_fail=41
result=FAIL
463_H27_FACTORY_HARDCODED_DEMO_BRANCH_BLOCKED=PASS
observed=AST_CONDITIONAL_SCAN_NO_NAMED_PROJECT_BRANCH
```

El resultado global permanece FAIL por el fixture positivo/restauración bloqueados por causas previas ajenas a AUD-007. Este ledger no lo convierte en PASS ni afirma `506/506`.

`VALIDATE_MASTER_GOVERNANCE_NATIVE.py` también permanece FAIL, con tres controles fuera de alcance:

```text
FAIL_RELEASE_SURFACE_SCOPE_SYNC
FAIL_DUPLICATE_ALLOWLIST_REAL_COVERAGE
FAIL_DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY
```

No se repararon esos controles en esta rama.

## Controles de no expansión

- `governance/CURRENT_STATE.json` no fue modificado.
- No se generó Proyecto Demo.
- No se creó release ni tag.
- No se cerró ningún issue.
- No se declaró ni aceptó `M02_PASS`.
- No se limpió bloat/no-history.
- No se consolidó un validator único.
- No se regeneraron ni sellaron manifiestos/hashes; esa tarea continúa reservada para `AUD-003`.

Este ledger documenta una corrección técnica acotada y no certifica el motor.
