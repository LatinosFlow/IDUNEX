# RESEARCH_ABSORPTION_PIPELINE

## Objetivo

Absorber nuevas investigaciones, documentos, informes, GENERIC_VISUAL_SYSTEM_TOKEN y documentación IDUNEX sin pérdida, sin reemplazar canon válido y sin tocar investigaciones cerradas SRC_001-SRC_049 salvo que exista fuente nueva documentada y justificada.

## Entrada aceptada

- ZIP agrupado de soporte.
- PDF/DOCX/TXT/MD/JSON/CSV auditables.
- Informe de auditoría o matriz de requisitos.
- Paquete GENERIC_VISUAL_SYSTEM_TOKEN o documentación IDUNEX.

## Pipeline obligatorio

1. `SOURCE_PACKAGE_INTAKE`: registrar nombre, SHA, fecha, autoridad y alcance.
2. `SOURCE_IDENTIFICATION`: separar fuente nueva, parche, auditoría, manual o evidencia.
3. `SOURCE_CARD_CREATION`: crear source card con claims, límites, owner y hash.
4. `CLAIM_EXTRACTION`: extraer claims operativos, no opiniones sueltas.
5. `SOURCE_TO_RUNTIME_MAPPING`: mapear a Profile360, TechExt, Agent Runtime, GENERIC_VISUAL_SYSTEM_TOKEN, QA, Project Factory y Agent Factory.
6. `IMPACT_ANALYSIS`: declarar campos, validators, fallbacks, sidecar fields y docs afectados.
7. `NOLOSS_APPLICATION`: aplicar cambios de forma quirúrgica y aditiva.
8. `MANIFESTS_HASH_REGENERATION`: regenerar ledgers internos y companion externo.
9. `INDEPENDENT_AUDIT`: ejecutar auditoría independiente con evidencia no vacía.
10. `CLOSURE_DECISION`: cerrar solo con 0 FAIL.

## Regla de investigaciones cerradas

SRC_001-SRC_049 son baseline bloqueado. No se editan ni se reemplazan sin nueva fuente documentada, hash, changelog, mapping y auditoría.

## Salidas

- Source card.
- Claim map.
- Source-to-runtime map.
- Validators nuevos.
- Fallbacks nuevos.
- Sidecar fields nuevos.
- Changelog.
- Manifests y hash.
- Informe de auditoría independiente.
