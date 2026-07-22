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
CONTROLLED_EXTERNAL_DEMO_STATUS=PENDING_AUTHORIZATION
CONTROLLED_EXTERNAL_DEMO_AUTHORIZED=FALSE
```

| Superficie | Estado | Decisión |
|---|---|---|
| Motor extraído | EN_REVISION | Árbol técnico reauditorado, todavía no oficial/productivo |
| ZIP candidato del motor | VALIDADO | Preservar externo; no versionar como release activo |
| Certificado recibido | REFERENCIA | Contrastar contra recomputación independiente |
| Informe Maestro | REFERENCIA / autoridad de trabajo | Debe permanecer fuera de cambios destructivos |
| Proyecto 000 Demo general | BLOQUEADO | `ready_for_project_demo_generation=false` |
| Excepción externa única | PENDING_AUTHORIZATION | Schema implementado; ejecución todavía no autorizada |
| ChatGPT/Copilot runtime | BLOQUEADO | Solo después de Demo auditado |
| Proyectos futuros | BLOQUEADO | Solo después de Demo 100% y motor productivo |

## Máquina de estados de ejecución externa

La capacidad general de generación continúa bloqueada. AUD-029 define exclusivamente una máquina de estados para una futura ejecución externa, única y trazable:

| Estado | Authorized | Consumed | Generate permitido | Decisión |
|---|---:|---:|---:|---|
| `PENDING_AUTHORIZATION` | false | false | 0 | Preparación documental y técnica solamente |
| `AUTHORIZED_NOT_CONSUMED` | true | false | 1 | Una ejecución externa identificada por SHA y autorización |
| `CONSUMED` | false | true | 0 | Autorización agotada; no repetir |

La transición futura a `AUTHORIZED_NOT_CONSUMED` exige autorización ID, commit, tree SHA, package SHA, Informe Maestro SHA, prompt activo y prompt SHA. No puede habilitar release, tag, `OFICIAL`, cierre productivo, carga de agentes ni certificación creativa.

Los certificados, reportes y resultados internos anteriores quedan como `REFERENCIA_SUSTITUIDA`. Pueden conservar resultados históricos o declarativos para lineage, pero no son autoridad vigente y no habilitan por sí mismos la siguiente fase.

## Estados documentales permitidos

- OFICIAL
- VALIDADO
- BORRADOR
- EN_REVISION
- SUSTITUIDO
- ARCHIVADO
- REFERENCIA

## Regla de cierre

No se declara motor productivo si existe cualquier falla, workaround manual, timeout, PASS declarativo o evidencia incompleta.

Mientras `MOTOR_STATUS=EN_REVISION`, ningún certificado interno ni evidencia derivada puede habilitar generación general del Proyecto Demo, release, tag o cierre productivo. La futura excepción externa solo será válida a través del objeto machine-readable `controlled_external_demo_execution` y sus gates completos.
