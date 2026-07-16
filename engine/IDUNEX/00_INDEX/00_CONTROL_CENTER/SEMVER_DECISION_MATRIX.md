# SEMVER_DECISION_MATRIX - IDUNEX Motor y Proyectos

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Fecha:** NEUTRALIZED_ACTIVE_SCOPE  
**Tipo de cambio:** P0 quirúrgico pre-cierre  
**Dictamen:** mantener exactamente `IDUNEX_MOTOR_v1.0.0` porque la release aún no fue cerrada como línea posterior.

## Regla principal

Durante fase pre-cierre, una corrección P0 obligatoria puede reemitir el mismo nombre semántico siempre que:

1. No se cree `v1.0.1`, `v1.0.0-final`, `v1.0.0-fixed`, `v1.0.0-new`, `RC`, fork ni variante alternativa.
2. Se preserve todo lo correcto.
3. Se regenere companion SHA256 externo, certificado, manuales y manifests afectados.
4. El ZIP no embeba su propio SHA final real como autoridad.
5. La auditoría final no declare PASS con `actual_value` vacío.

## Matriz de decisión

| Caso | Decisión | Versión resultante | Gate obligatorio |
|---|---|---|---|
| Pre-cierre quirúrgico P0 | Mantener versión | IDUNEX_MOTOR_v1.0.0 | Reissue SHA/certificado/manuales/manifests |
| Patch/micro compatible | Patch | 1.0.1, 1.0.2 | No breaking change + full regression |
| Minor/intermedio | Minor | 1.1.0, 1.2.0 | Backward compatible + migration notes |
| Major/breaking | Major | 2.0.0 | Breaking contract + migration plan |
| Downgrade/remoción | Protocolo de remoción | Misma versión si pre-cierre; patch formal si post-cierre | ZERO_ACTIVE_TRACE_AFTER_REMOVAL |
| Update de motor | Engine update | Según impacto | Project impact analysis |
| Update de proyecto por motor | Project migration | Versión de proyecto, no motor | Project Factory gate |
| Update solo proyecto | Project-only | Versión de proyecto | No alterar motor |
| Baja/retiro de proyecto | Lifecycle state | Estado de proyecto | Output block si retired/archived |

## Árbol de decisión operativo

1. ¿El cambio rompe schema, runtime, sidecar, manifests, Project Factory o Agent Factory?  
   - Sí: `MAJOR_BREAKING` salvo que aún sea pre-cierre y se documente como corrección P0 interna.  
   - No: continuar.
2. ¿Agrega capacidad compatible sin obligar a migrar proyectos existentes?  
   - Sí: `MINOR_INTERMEDIATE` post-cierre o mismo `v1.0.0` si es P0 pre-cierre.
3. ¿Corrige error compatible ya cerrado?  
   - Sí: `PATCH_MICRO` post-cierre.
4. ¿Remueve o revierte una capacidad?  
   - Sí: ejecutar `CHANGE_REMOVAL_AND_DOWNGRADE_PROTOCOL`.
5. ¿Afecta solo un proyecto?  
   - Sí: modificar versión/estado del proyecto; no tocar motor.

## Bloqueos

- Bloquear cierre si companion SHA no coincide.
- Bloquear cierre si JSON inválido.
- Bloquear cierre si un config agente no mide 8000 caracteres exactos.
- Bloquear cierre si se pierde Profile360 FULL60, TechExt FULL10, Agent Runtime Governance FULL10, SRC_001-SRC_049, source cards, claims, mappings, QA o fallbacks.
