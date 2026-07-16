# PROJECT_FACTORY_GLOBAL_PROTOCOL_RULES — IDUNEX MOTOR v1.0.0

## COMMON_PROJECT_FACTORY_EXECUTION_BLOCK
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.

## Regla de delta por protocolo
Cada protocolo debe conservar su caso diferencial: creación, actualización, migración, readiness demo o readiness multi-sujeto, y declarar cómo cambia inputs, outputs, riesgos y retest.

## MODEL_COUNT_MATRIX_1_TO_10
Aplica model_count_min=1 y model_count_max=10. Cada protocolo hereda la matriz de conteo 1..10; el delta local solo debe declarar creación, actualización, migración, demo readiness o multi-subject readiness.
