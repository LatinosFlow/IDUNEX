# CHANGE_REMOVAL_AND_DOWNGRADE_PROTOCOL

## Objetivo

Permitir downgrade o remoción quirúrgica de cambios sin degradar el motor, sin dejar rastros activos contradictorios y sin romper lineage histórico.

## Registro obligatorio por cambio

Todo cambio removido debe tener:

- CHANGE_ID
- Archivos tocados
- Campos agregados
- Validators agregados
- Sidecar fields agregados
- Source mappings afectados
- Documentación afectada
- Manifests afectados
- Hash/certificate reissue
- Retest obligatorio
- ZERO_ACTIVE_TRACE_AFTER_REMOVAL
- Anti-regression después de downgrade

## Proceso

1. Abrir CHANGE_ID y congelar snapshot pre-remoción.
2. Identificar todos los archivos activos afectados.
3. Remover o marcar como `HISTORICAL_ONLY_NOT_RUNTIME_AUTHORITY` según corresponda.
4. Ejecutar búsqueda de símbolos para confirmar `ZERO_ACTIVE_TRACE_AFTER_REMOVAL`.
5. Regenerar manifests SHA, file manifests y companion externo.
6. Reemitir certificado y manuales si el ZIP fue reempaquetado.
7. Ejecutar auditoría anti-regression completa.

## Bloqueos

- No declarar PASS si queda referencia activa a la capacidad removida.
- No remover lineage histórico salvo purga permitida por política.
- No tocar SRC_001-SRC_049 sin nueva fuente documentada.
- No cerrar si la remoción degrada Profile360 FULL60, TechExt FULL10, Agent Runtime Governance FULL10, QA, source cards, claims, mappings o fallbacks.
