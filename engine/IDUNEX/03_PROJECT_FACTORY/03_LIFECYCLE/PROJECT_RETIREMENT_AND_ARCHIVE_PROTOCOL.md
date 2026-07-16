# PROJECT_RETIREMENT_AND_ARCHIVE_PROTOCOL

## Estados obligatorios

| Estado | Outputs nuevos | Consulta | Recomendación para nuevos outputs |
|---|---:|---:|---:|
| PROJECT_ACTIVE | Permitido con QA | Sí | Sí |
| PROJECT_LOCKED | Bloqueado | Sí | No |
| PROJECT_DEPRECATED | Bloqueado salvo excepción aprobada | Sí | No |
| PROJECT_RETIRED | Bloqueado | Sí | No |
| PROJECT_ARCHIVED_READONLY | Bloqueado | Solo lectura | No |
| PROJECT_PURGED_POLICY_ALLOWED | Bloqueado | Según política de purga | No |

## Reglas

- Un proyecto retirado no puede generar outputs nuevos.
- Un proyecto archivado queda solo lectura.
- Un proyecto deprecated puede consultarse, pero no recomendarse para nuevos outputs.
- Todo retiro conserva lineage histórico salvo purga permitida por contrato/legal.
- El estado debe propagarse a manifests, certificados, scorecards, dashboards y agent configs exportados.

## Bloqueos

- `BLOCKED_PROJECT_RETIRED_OUTPUT_REQUEST` para cualquier output nuevo en PROJECT_RETIRED.
- `BLOCKED_PROJECT_ARCHIVED_READONLY_OUTPUT_REQUEST` para cualquier output nuevo en PROJECT_ARCHIVED_READONLY.
- `BLOCKED_PROJECT_PURGED_NO_RUNTIME_AUTHORITY` cuando la purga elimina autoridad runtime.
