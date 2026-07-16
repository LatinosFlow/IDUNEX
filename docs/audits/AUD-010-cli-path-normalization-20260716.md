# AUD-010 - Ledger de normalización de rutas CLI

**Issue vinculada:** `#11`
**Rama:** `fix/AUD-010-cli-path-normalization`
**Base apilada:** `fix/AUD-006-governance-state-machine` (`45456bd`)
**Fecha:** `2026-07-16`
**MOTOR_STATUS:** `EN_REVISION`
**M02_RESULT:** `M02_FAIL`

## 1. Alcance

Este ledger registra exclusivamente la corrección de `B-08/AUD-010`: normalización temprana y determinista de rutas en `update-project`, `migrate-project` y `update-project-by-engine`.

No se corrigieron el watchdog Windows, el remapeo Windows-safe, bloat/no-history, el validator único ni la lógica Demo. No se generó Proyecto Demo, no se creó release o tag, no se cerró la issue y no se declara ni acepta `M02_PASS`.

## 2. Autoridad aplicada

1. `governance/authority/REFERENCIA/Informe_Maestro_Go_07d4ad84.pdf`, en particular la matriz máxima de migraciones de la sección 12.4.
2. `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`, hallazgo `B-08`.
3. `docs/audits/IA-IDUNEX-PlanCorreccionM02-20260716-v1-EN_REVISION.md`, criterio `AUD-010`.
4. `governance/CURRENT_STATE.json`, que conserva `EN_REVISION / M02_FAIL` y el interlock de Demo/release/tag.

## 3. Causa raíz reproducida

`_apply_semantic_replacements_limited` resolvía las raíces de búsqueda y, por tanto, enumeraba archivos absolutos, pero calculaba `relative_to(project_root)` contra el `project_root` recibido desde CLI sin resolver. Con `--project` relativo, Python comparaba una ruta absoluta con una relativa y lanzaba `ValueError`; con `--project` absoluto, la misma operación funcionaba.

## 4. Corrección quirúrgica

- Los argumentos filesystem de los tres comandos relacionados se convierten una sola vez a `Path` absoluto y resuelto inmediatamente después de `argparse`.
- La copia del proyecto normaliza de forma idempotente `source`, `output`, la raíz extraída y `dst`, de modo que las llamadas internas directas mantienen la misma representación.
- Las rutas de evidencia y manifiesto se emiten como rutas POSIX relativas únicamente después de comprobar que su ruta absoluta resuelta pertenece al `project_root` absoluto resuelto.
- Una raíz de reemplazo semántico fuera del proyecto se bloquea con `FAIL_CLI_PATH_OUTSIDE_PROJECT_ROOT`.
- La semántica del update, el contrato no-drift y la certificación creativa no cambian.

## 5. Regresión automatizada

Comando:

```text
python -m unittest tests.intake.test_cli_path_normalization -v
```

Resultado en Windows: `6/6 OK`.

Cobertura:

- equivalencia de rutas relativas y absolutas para `--project`, `--update`, `--output` y `--output-json`;
- normalización de `migrate-project` y `update-project-by-engine`;
- separadores Windows `\`;
- reproducción corregida de `project_root` relativo frente a archivos resueltos;
- rechazo de raíz fuera de `project_root`;
- copia con fuente y salida relativas normalizada a destino absoluto.

Controles complementarios:

- `python -m unittest discover -s tests/intake -p 'test_*.py' -v`: `9/9 OK`;
- llamada directa de `tests.intake.test_repo_intake.test_intake_audit_passes`: `PASS`;
- `tools/audit/governance_state_check.py --repo-root .`: `CONSISTENT`, 0 contradicciones activas;
- compilación in-memory del factory: `PASS`;
- `git diff --check`: `PASS`.

El runtime local no incluyó el paquete `pytest` (`No module named pytest`); la cobertura disponible se ejecutó mediante `unittest` y la función pytest-style de intake se invocó directamente.

## 6. Evidencia funcional CLI

Se reutilizó el proyecto N1 existente `IDUNEX_PROJECT_AUDIT_SINGLE_N1_v1.0.0` de la auditoría M02. No se invocó `generate` y no se creó un Proyecto Demo. Para reproducir el contexto auditado se definió `IDUNEX_ENGINE_ZIP_SHA256=bbef200d6f0d7bf116853e0d763b90dc0b6454efee831e6dee1b040c78fce0d6`.

| Caso | Forma de paths | rc | Resultado operativo | Validadores | Fail codes |
|---|---|---:|---|---:|---|
| `update-project` | relativa | 0 | `PASS / DELIVERY_ALLOWED` | 0 | `[]` |
| `update-project` | absoluta | 0 | `PASS / DELIVERY_ALLOWED` | 0 | `[]` |
| `migrate-project` | relativa | 0 | `PASS / MIGRATION_REAL_OUTPUT_PASS` | 0 | `[]` |
| `update-project-by-engine` | absoluta | 0 | `PASS / MIGRATION_REAL_OUTPUT_PASS` | 0 | `[]` |

En ambos updates:

- `model_count=1`;
- `runtime_upload_count=11`;
- `profile360_join=61/61 per model`;
- `techext_join=284/284 per model`;
- `creative_output_certified=false`;
- 246 rutas de manifest y 11 rutas de superficies escaneadas quedaron relativas, contenidas y sin `..`.

Los valores `PASS` de esta sección describen exclusivamente ejecuciones técnicas de los comandos enumerados. No alteran el estado global ni sustituyen una re-auditoría M02 independiente.

## 7. Archivos del cambio

- `engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py`
- `tests/intake/test_cli_path_normalization.py`
- `docs/audits/AUD-010-cli-path-normalization-20260716.md`

## 8. Estado de gobierno posterior

`governance/CURRENT_STATE.json` no fue modificado. Permanecen vigentes:

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=M02_FAIL
READY_FOR_PROJECT_DEMO_GENERATION=false
RELEASE_AUTHORIZED=false
TAG_AUTHORIZED=false
```
