# GOV — Estado de Gobernanza del Repositorio

| Superficie | Estado | Decisión |
|---|---|---|
| Motor extraído | EN_REVISION | Base técnica importable, no oficial funcional |
| ZIP fuente | VALIDADO integridad física | Preservar externo, no versionar como release activo |
| Certificado recibido | REFERENCIA | Contrastar contra recomputación independiente |
| Informe Maestro | REFERENCIA / autoridad de trabajo | Debe permanecer fuera de cambios destructivos |
| Proyecto 000 Demo | BLOQUEADO | Solo después de cierre técnico del motor |
| ChatGPT/Copilot runtime | BLOQUEADO | Solo después de Demo auditado |
| Proyectos futuros | BLOQUEADO | Solo después de Demo 100% y motor productivo |

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
