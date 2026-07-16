# RESEARCH_RUNTIME_GLOBAL_RULES — IDUNEX MOTOR v1.0.0

## COMMON_RESEARCH_LANDING_RULE
**Aterrizaje IDUNEX:** convertir a campo Perfil360 o regla de core, definir allowed/forbidden, aplicar QA, crear fail code y fallback.
**No usar como:** resumen decorativo o conocimiento no cargable.

## COMMON_RUNTIME_QA_BLOCK
| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

## Regla no-loss
Los extractos transformados de investigación no se eliminan. Se centraliza solo la regla de aterrizaje repetida para reducir padding y mantener trazabilidad investigativa.
