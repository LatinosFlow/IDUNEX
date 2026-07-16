# GOV — Estado de Gobernanza del Repositorio

`governance/CURRENT_STATE.json` es la única fuente legible por máquina para el estado global vigente.

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=M02_FAIL
READY_FOR_PROJECT_DEMO_GENERATION=FALSE
RELEASE_AUTHORIZED=FALSE
TAG_AUTHORIZED=FALSE
PRODUCTIVE_CLOSURE_AUTHORIZED=FALSE
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

| Superficie | Estado | Decisión |
|---|---|---|
| Motor extraído | EN_REVISION | Base técnica importable, no oficial funcional |
| ZIP fuente | VALIDADO integridad física | Preservar externo, no versionar como release activo |
| Certificado recibido | REFERENCIA | Contrastar contra recomputación independiente |
| Informe Maestro | REFERENCIA / autoridad de trabajo | Debe permanecer fuera de cambios destructivos |
| Proyecto 000 Demo | BLOQUEADO | Solo después de cierre técnico del motor |
| ChatGPT/Copilot runtime | BLOQUEADO | Solo después de Demo auditado |
| Proyectos futuros | BLOQUEADO | Solo después de Demo 100% y motor productivo |

Los certificados, reportes y resultados internos anteriores quedan como `REFERENCIA_SUSTITUIDA`. Pueden conservar resultados históricos o declarativos para lineage, pero no son autoridad vigente y no habilitan la siguiente fase.

## Estados permitidos

- OFICIAL
- VALIDADO
- BORRADOR
- EN_REVISION
- SUSTITUIDO
- ARCHIVADO
- REFERENCIA

## Regla de cierre

No se declara motor productivo si existe cualquier falla, workaround manual, timeout, PASS declarativo o evidencia incompleta.

Si `M02_RESULT=M02_FAIL`, ningún certificado interno ni evidencia derivada puede habilitar Proyecto Demo, release, tag o cierre productivo.
