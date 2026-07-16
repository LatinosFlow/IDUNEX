# PATH_REFERENCE_REWRITE_AFTER_RENUMBERING - P0.2-009

Engine: IDUNEX_MOTOR_v1.0.0
Fecha: NEUTRALIZED_ACTIVE_SCOPE
Estado: APPLIED_AND_BLOCKING_FOR_FUTURE

## Protocolo
Despues de cualquier renumeracion se deben buscar y actualizar rutas en MD, TXT, JSON, CSV, manifests, sidecars, templates, configs, manuales generados, certificados, export paths de Project Factory, runtime paths de ChatGPT/Copilot, source-to-runtime mappings, QA/fallback references y documentation references.

## Evidencia permitida
Las rutas antiguas solo pueden permanecer como evidencia historica en este archivo, en `ROOT_DIRECTORY_CANONICAL_RENUMBERING.*` o en changelogs historicos. No pueden quedar como referencias operativas activas.
