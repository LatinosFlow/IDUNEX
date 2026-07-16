## Phase 3 file-level inheritance
inherits = PROJECT_FACTORY_GLOBAL_PROTOCOL_RULES#COMMON_PROJECT_FACTORY_EXECUTION_BLOCK
protocol_specific_delta_required = true
inherits_model_count_matrix = PROJECT_FACTORY_GLOBAL_PROTOCOL_RULES#MODEL_COUNT_MATRIX_1_TO_10

# PROJECT_BRAND_ENTITY 10 Readiness

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.

Proyecto MULTI_SUBJECT_TEMPLATE debe ejecutarse después de plantilla demo no instanciada Demo PASS. Máximo 10 modelos por agente principal; cada modelo requiere Perfil360 full y uniqueness total.
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



### Caso factory 02



### Caso factory 03



### Caso factory 04



### Caso factory 05



### Caso factory 06



### Caso factory 07



### Caso factory 08



### Caso factory 09



### Caso factory 10



### Caso factory 11



### Caso factory 12



### Caso factory 13



### Caso factory 14



### Caso factory 15



### Caso factory 16



### Caso factory 17



### Caso factory 18



### Caso factory 19



### Caso factory 20



### Caso factory 21



### Caso factory 22



### Caso factory 23



### Caso factory 24



### Caso factory 25



### Caso factory 26



### Caso factory 27



### Caso factory 28



### Caso factory 29



### Caso factory 30



### Caso factory 31



### Caso factory 32



### Caso factory 33



### Caso factory 34



### Caso factory 35



### Caso factory 36



### Caso factory 37
**Entradas obligatorias:** brief, motor, políticas, source map, roster, constraints, anchors si existen, estado productivo y límites de vendor.  
**Ejecución:** generar 10 core de proyecto; por cada modelo crear Perfil360 completo; compilar ChatGPT Agent-Load; transformar a Copilot DOCX; generar QA; emitir manifest y SHA.  
**Bloqueos:** core delgado, perfil resumido, Copilot pobre, no-loss sin evidencia, same-face, same-body, vendor drift, sidecar incompleto, naming no estánd
