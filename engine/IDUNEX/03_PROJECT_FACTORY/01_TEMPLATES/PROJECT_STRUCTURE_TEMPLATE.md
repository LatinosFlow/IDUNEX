# Project Structure Template

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


IDUNEX_PROJECT_<NOMBRE>_vX.Y.Z_YYYYMMDD/
├─ 00_PROJECT_CONTROL/
├─ 01_PROJECT_CORE_10_CHATGPT/
├─ 02_PROJECT_CORE_10_COPILOT_DOCX/
├─ 03_MODELS_PROFILE360/
├─ 04_AGENT_LOADS/
├─ 05_PROMPT_PACKS/
├─ 06_VENDOR_ADAPTERS/
├─ 07_QA_GOLDEN_TESTS/
├─ 08_OUTPUT_SIDECAR_WATERMARK/
├─ 09_PROJECT_DOCUMENTATION/
└─ 99_MANIFESTS_SHA_LINEAGE/
# Project Factory Full 10/10

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


Este módulo gobierna creación y actualización de proyectos. Un proyecto IDUNEX nunca es copia del motor: es una instancia con canon, 10 core adaptados, perfiles Perfil360 por modelo, agent-load ChatGPT, Copilot DOCX, adapters, QA, manifests y lineage.

## Load order de creación
1. Leer motor y políticas.
2. Leer brief de proyecto.
3. Definir nombre `IDUNEX_PROJECT_<NOMBRE>_vX.Y.Z_YYYYMMDD`.
4. Crear control de proyecto.
5. Generar 10 core de proyecto derivados del motor.
6. Crear Perfil360 por modelo.
7. Crear agent-load ChatGPT.
8. Crear Copilot DOCX agent-load.
9. Crear prompt packs, adapters, sidecar y QA.
10. Auditar N ciclos hasta PASS.

## Load order de actualización
1. Leer motor vigente.
2. Leer proyecto anterior.
3. Crear migration map KEEP/CHANGE/ADD/MIGRATE/DEPRECATE/REMOVE.
4. Migrar canon útil sin arrastrar legacy activo.
5. Recalcular compatibilidad.
6. Rehacer agent-load completo.
7. Revalidar modelos, pairwise uniqueness, sidecar y QA.

### Caso factory 01
**Escenario:** creación/actualización de proyecto con 2 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 02
**Escenario:** creación/actualización de proyecto con 3 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 03
**Escenario:** creación/actualización de proyecto con 4 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 04
**Escenario:** creación/actualización de proyecto con 5 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 05
**Escenario:** creación/actualización de proyecto con 6 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 06
**Escenario:** creación/actualización de proyecto con 7 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 07
**Escenario:** creación/actualización de proyecto con 8 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 08
**Escenario:** creación/actualización de proyecto con 9 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 09
**Escenario:** creación/actualización de proyecto con 10 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 10
**Escenario:** creación/actualización de proyecto con 1 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 11
**Escenario:** creación/actualización de proyecto con 2 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 12
**Escenario:** creación/actualización de proyecto con 3 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 13
**Escenario:** creación/actualización de proyecto con 4 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 14
**Escenario:** creación/actualización de proyecto con 5 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 15
**Escenario:** creación/actualización de proyecto con 6 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 16
**Escenario:** creación/actualización de proyecto con 7 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 17
**Escenario:** creación/actualización de proyecto con 8 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 18
**Escenario:** creación/actualización de proyecto con 9 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 19
**Escenario:** creación/actualización de proyecto con 10 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 20
**Escenario:** creación/actualización de proyecto con 1 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 21
**Escenario:** creación/actualización de proyecto con 2 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 22
**Escenario:** creación/actualización de proyecto con 3 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 23
**Escenario:** creación/actualización de proyecto con 4 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar, ejecutar QA y reparar fallas sin inventar canon.


### Caso factory 24
**Escenario:** creación/actualización de proyecto con 5 modelo(s), requerimiento multimodal y compatibilidad con IDUNEX_MOTOR_v1.0.0.  
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estándar.  
**PASS:** proyecto puede responder readback, crear prompts con sidecar
