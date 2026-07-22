# GOV — Estado de Gobernanza del Repositorio

`governance/CURRENT_STATE.json` es la única fuente legible por máquina para el estado global vigente.

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=M02_PASS
M03_RESULT=M03_PASS
READY_FOR_PROJECT_DEMO_GENERATION=FALSE
RELEASE_AUTHORIZED=FALSE
TAG_AUTHORIZED=FALSE
PRODUCTIVE_CLOSURE_AUTHORIZED=FALSE
CREATIVE_OUTPUT_CERTIFIED=FALSE
CONTROLLED_EXTERNAL_DEMO_STATUS=AUTHORIZED_NOT_CONSUMED
CONTROLLED_EXTERNAL_DEMO_AUTHORIZED=TRUE
CONTROLLED_EXTERNAL_DEMO_CONSUMED=FALSE
CONTROLLED_EXTERNAL_DEMO_EXECUTION_LIMIT=1
```

| Superficie | Estado | Decisión |
|---|---|---|
| Motor | EN_REVISION | Reauditorado; no oficial/productivo |
| ZIP candidato | VALIDADO | Paquete externo fijado por SHA |
| Informe Maestro | VALIDADO como autoridad operativa | Fijado por SHA externo |
| Prompt canónico | VALIDADO / ACTIVO | Autorizado para una ejecución |
| Proyecto 000 Demo general | BLOQUEADO | `ready_for_project_demo_generation=false` |
| Excepción externa AUD-028 | AUTHORIZED_NOT_CONSUMED | Una ejecución externa en ChatGPT normal |
| Release / tag / OFICIAL / cierre | BLOQUEADO | No autorizado |
| Carga de agentes | BLOQUEADO | Solo después de auditoría independiente del Demo |

## Máquina de estados

| Estado | Authorized | Consumed | Generate permitido | Decisión |
|---|---:|---:|---:|---|
| `PENDING_AUTHORIZATION` | false | false | 0 | Preparación |
| `AUTHORIZED_NOT_CONSUMED` | true | false | 1 | Una ejecución externa |
| `CONSUMED` | false | true | 0 | Autorización agotada |

La autorización AUD-028 se limita a los tres adjuntos fijados por SHA. El inicio de `generate`
consume la autorización. Un fallo posterior no permite reintento.

## Estados documentales permitidos

- OFICIAL
- VALIDADO
- BORRADOR
- EN_REVISION
- SUSTITUIDO
- ARCHIVADO
- REFERENCIA

## Regla de cierre

La excepción AUD-028 no promueve el motor ni el Demo. Solo una auditoría independiente posterior
puede declarar `PROJECT_AUDIT_PASS`.
