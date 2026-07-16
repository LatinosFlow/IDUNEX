# COPILOT DOCX RUNTIME STANDARD

## Authority hierarchy
Copilot debe leer primero estado de motor, control center, locks, source inventory, Profile360 registry, source-to-runtime map, adapters, QA, sidecar y manifest. La jerarquía H1-H4 es obligatoria para impedir que el canon crítico quede enterrado.

## H1-H4 standard
H1 = unidad de autoridad; H2 = sección operativa; H3 = tabla o matriz; H4 = reglas/fallbacks. Todo DOCX debe incluir portada técnica, resumen ejecutivo, producción state, lock table, canon crítico, Profile360 fields, source mapping, multimodal rules, QA/golden tests, fallback fixes, sidecar, changelog y audit.

## Large canon chunking
El canon grande se divide por autoridad: motor core, project factory, agent factory, Profile360, source-to-runtime, adapters, QA, sidecar, policies, documentation. Cada chunk debe repetir engine_version, state, source scope y no-loss rule.

## Source and field trace
Toda sección DOCX debe tener matriz source_id → field_id → adapter → QA → fallback. Copilot no puede responder si no puede hacer readback de esa matriz.

## No destructive summary
Copilot puede resumir para orientar, pero no puede eliminar locks, source_ids, fail codes, fallback fixes, sidecar requirements o production state. Si un resumen omite esos elementos, se dispara FAIL_BLOCKER_COPILOT_DOCX_TOO_THIN.

## Render validation
Cada DOCX operativo debe abrir, renderizar y permitir extracción de texto. Si falla render o clipping visual, la entrega queda en NO_GO.

## Readback QA
Antes de operar, Copilot debe devolver engine_version, production_state, active_project_id si existe, active_locks, source_ids_loaded, field_ids_loaded, adapter_targets_loaded, QA gates, sidecar requirement, known gaps y GO/NO_GO.

## Project package handoff
El DOCX no otorga GLOBAL_GO. Solo prepara el motor para prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE y exige prueba de proyecto.


## Archivo específico
Ruta operativa: `19_DOCUMENTATION/COPILOT_LARGE_CANON_CHUNKING.md`. Esta ruta mantiene autoridad documental y prueba no-loss DOCX export.


## Operational depth extension
Este estándar obliga a Copilot a operar como lector de canon grande, no como resumidor libre. Para cada documento debe construir una tabla de autoridad con: sección, propósito, source_ids, field_ids, adapter_targets, QA, fail_code, fallback y estado. Si una sección contiene locks o reglas de identidad, Copilot debe repetirlas en la respuesta de readback antes de cualquier transformación. La estrategia de chunking se basa en autoridad, no en longitud: primero motor/control, luego Profile360, luego source-to-runtime, luego adapters, luego QA, luego sidecar, luego documentación. Si el contexto excede límite, se divide por autoridad y se preservan las relaciones source_id → field_id → adapter → QA. 

El protocolo anti-hallucination bloquea inferencias no presentes; todo dato no cargado se marca como gap. El protocolo anti-destructive-summary prohíbe resumir eliminando locks, sidecar, fail codes, source trace, schema rules o estado GO/NO-GO. El no-loss DOCX export test exige abrir/renderizar el DOCX, extraer texto, validar headings H1-H4, comprobar tablas de locks y confirmar que SRC_029 y SRC_048 están referenciadas en grounding, chunking, readback y claim verification. Si Copilot no puede citar sección interna, debe devolver REVIEW_REQUIRED.

## HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3 Remediación final QA/Evidencia/Hash


### Grounding evidence HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3
- DOCX authority hierarchy: Control Center → Motor Core → Profile360 → Source-to-Runtime → Schemas → QA → Smoke Evidence → Sidecar.
- H1-H4 standard: every section must expose title, authority, source trace and QA gate.
- Source trace table: source_id, canonical id, runtime domains, fields impacted, primary/support counts, score and evidence.
- Field trace table: field_id, field_name, runtime_domain, adapter_domain, qa_rule_id, fail_code, fallback.
- Lock table: JSON_LOCK, ANCHOR_LOCK, AGE_LOCK, ID_LOCK, NO_LOSS_LOCK, NO_GLOBAL_GO_LOCK.
- Chunking strategy: split by authority, repeat locks at chunk boundary, no destructive summary.
- Readback protocol: engine_version, production_state, active_project_id, active_locks, source_ids_loaded, field_ids_loaded, adapter_targets_loaded, QA gates loaded, sidecar requirement, known gaps, GO/NO_GO state.
- Render gate: DOCX must be rendered; layout issues block Copilot-ready claim.
- Hallucination blocker: Copilot must not infer fields, projects, people, models or GLOBAL_GO absent from loaded package.
