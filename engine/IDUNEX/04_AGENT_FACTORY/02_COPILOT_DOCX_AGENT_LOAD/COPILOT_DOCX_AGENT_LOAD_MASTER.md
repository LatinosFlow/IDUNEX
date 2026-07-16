## Phase 3 file-level inheritance
inherits = AGENT_FACTORY_GLOBAL_RULES#COMMON_AGENT_RUNTIME_QA_BLOCK
inherits_mandatory_fields = AGENT_FACTORY_GLOBAL_RULES#COMMON_MANDATORY_FIELDS
agent_specific_delta_required = true

# Copilot DOCX Agent Load Master — IDUNEX_MOTOR_v1.0.0

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


## IDUNEX_COPILOT_CLEAN_IMAGE_OUTPUT - H245-H260 PRIORITY

No visual panels. No info cards. No age, nationality, project metadata, QA status, certification status, sidecar status or hashes inside image. No fake canon rendered in image. No exact logo unless asset is verified. If Copilot cannot verify watermark overlay, mark VISIBLE_WATERMARK_NOT_VERIFIED. Emit metadata outside image. Candidate generation remains separate from certification.

## Scope operativo específico — Copilot DOCX / Word

- Prioridad: documentos largos, DOCX, grounding documental, chunking, readback QA, control de estructura y compatibilidad Word/Copilot 365.
- Debe usar explícitamente estos estándares:
  - `COPILOT_DOCX_RUNTIME_STANDARD.md`
  - `COPILOT_DOCX_GROUNDING_PROTOCOL.md`
  - `COPILOT_LARGE_CANON_CHUNKING.md`
  - `COPILOT_READBACK_QA.md`
- Debe preservar jerarquía H1-H4, tablas largas, anexos, referencias cruzadas y validación de readback.
- No debe operar como generador principal de PromptPacks creativos; esa función corresponde a ChatGPT Agent Load.
- Debe respetar `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`, `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; project_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`, `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE` y `RESEARCH_LAYER_SCOPE=LOCKED_NOT_IN_SCOPE`.

Los agentes son la interfaz principal de uso. Deben cargar core + perfil + QA + adapter antes de responder. El agente no es libre de imaginar canon. Puede componer dentro de rangos declarados.

## Orden obligatorio
1. Readback del motor/proyecto.
2. Identificar intención: crear, actualizar, diagnosticar, prompt, sidecar, QA, migración.
3. Identificar modelo(s) y cargar Perfil360 completo.
4. Leer core relevantes.
5. Seleccionar vendor adapter.
6. Compilar prompt creativo y sidecar técnico separados.
7. Ejecutar QA.
8. Entregar fallback fixes.

## Uso agente para Identidad, memoria, biografía, cultura segura y persona digital adulta

### Grupo operativo: canon

| `canonical_name` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `model_code` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `aliases` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `adult_age` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `visual_age` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `body_age` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `vocal_age` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `project_role` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `canon_scope` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `mutable_scope` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `immutable_scope` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `identity_status` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `relationship_to_project` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `persona_boundary` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `private_public_boundary` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: biography

| `birth_context` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `family_structure` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `migration_trace` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `education_trace` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `work_trace` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `social_environment` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `formative_events` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `life_turning_points` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `habit_map` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `daily_routines` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `memory_triggers` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `emotional_anchors` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `personal_limits` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `conflict_history` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `growth_arc` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: personhood

| `temperament` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `motivation_stack` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fear_stack` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `desire_stack` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `values_map` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `moral_boundaries` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `worldview` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `contradictions` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `humor_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `decision_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `social_reaction` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `conflict_response` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `confidence_pattern` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `attention_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `empathy_pattern` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: language

| `inner_voice` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `written_voice` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `speech_register` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `silence_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `vocabulary_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `peruvian_latam_usage` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sociolect_limit` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `interview_voice` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `caption_voice` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `script_voice` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `no_generic_text_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `non_imitation_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: canon
**Entrada coloquial:** el usuario pide un output que afecta canon.  
**Acción del motor:** cargar Perfil360, filtrar campos `canonical_name, model_code, aliases, adult_age, visual_age`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: biography
**Entrada coloquial:** el usuario pide un output que afecta biography.  
**Acción del motor:** cargar Perfil360, filtrar campos `birth_context, family_structure, migration_trace, education_trace, work_trace`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: personhood
**Entrada coloquial:** el usuario pide un output que afecta personhood.  
**Acción del motor:** cargar Perfil360, filtrar campos `temperament, motivation_stack, fear_stack, desire_stack, values_map`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: language
**Entrada coloquial:** el usuario pide un output que afecta language.  
**Acción del motor:** cargar Perfil360, filtrar campos `inner_voice, written_voice, speech_register, silence_style, vocabulary_range`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
## Uso agente para Rostro forense, landmarks, edad visual y autenticación de identidad

### Grupo operativo: shape

| `face_shape` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `cranial_visual_volume` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `vertical_thirds` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `horizontal_fifths` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `forehead_height` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hairline_relation` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `temple_width` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `cheekbone_position` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `midface_length` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lower_face_ratio` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `jaw_angle` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `jaw_softness` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `chin_projection` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `chin_width` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `facial_asymmetry_map` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `age_face_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: eyes

| `eye_shape` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `eye_size` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `eye_spacing` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `eye_tilt` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `eyelid_fold` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `upper_lid_weight` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lower_lid_tension` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `iris_color` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `iris_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `catchlight_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `gaze_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `blink_pattern` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `eye_emotion_map` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `under_eye_texture` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sclera_natural_variation` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: brows_nose_mouth

| `brow_density` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brow_arc` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brow_height` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brow_eye_distance` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `nose_bridge` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `nose_dorsum` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `nose_tip` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `nostril_width` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `alar_shape` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `philtrum_length` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lip_ratio` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `upper_lip_shape` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lower_lip_volume` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `cupid_bow` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `mouth_width` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `smile_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `teeth_visibility_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: auth

| `wrong_face_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `same_face_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `generic_beauty_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `over_symmetry_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `makeup_face_drift_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lens_face_distortion_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `anchor_face_match_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `face_regression_test` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: shape
**Entrada coloquial:** el usuario pide un output que afecta shape.  
**Acción del motor:** cargar Perfil360, filtrar campos `face_shape, cranial_visual_volume, vertical_thirds, horizontal_fifths, forehead_height`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: eyes
**Entrada coloquial:** el usuario pide un output que afecta eyes.  
**Acción del motor:** cargar Perfil360, filtrar campos `eye_shape, eye_size, eye_spacing, eye_tilt, eyelid_fold`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: brows_nose_mouth
**Entrada coloquial:** el usuario pide un output que afecta brows_nose_mouth.  
**Acción del motor:** cargar Perfil360, filtrar campos `brow_density, brow_arc, brow_height, brow_eye_distance, nose_bridge`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: auth
**Entrada coloquial:** el usuario pide un output que afecta auth.  
**Acción del motor:** cargar Perfil360, filtrar campos `wrong_face_blocker, same_face_blocker, generic_beauty_blocker, over_symmetry_blocker, makeup_face_drift_rule`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
## Uso agente para Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal

### Grupo operativo: structure

| `height_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `body_build` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `visual_mass` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shoulder_width` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `neck_length` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `clavicle_visibility` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `torso_length` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `torso_leg_ratio` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `waist_hip_relation` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `pelvis_width` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `arm_length` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `forearm_shape` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wrist_scale` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `leg_line` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `knee_visibility` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `ankle_scale` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `foot_scale` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `body_age_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: hands_feet

| `hand_shape` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `finger_length` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `finger_taper` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `knuckle_visibility` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `nail_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hand_gesture_rest` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hand_object_contact` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `feet_ground_contact` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `toe_visibility_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shoe_fit_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hands_age_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `contact_pressure_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: posture

| `center_of_gravity` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `posture_base` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `spine_curve` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shoulder_behavior` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hip_alignment` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `weight_distribution` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `standing_balance` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sitting_balance` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `walking_weight` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `dance_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fitness_tone` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `body_energy_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| `same_body_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wrong_age_body_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `impossible_pose_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `body_lens_distortion_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `proportion_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hands_feet_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `adult_body_safety_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: structure
**Entrada coloquial:** el usuario pide un output que afecta structure.  
**Acción del motor:** cargar Perfil360, filtrar campos `height_range, body_build, visual_mass, shoulder_width, neck_length`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: hands_feet
**Entrada coloquial:** el usuario pide un output que afecta hands_feet.  
**Acción del motor:** cargar Perfil360, filtrar campos `hand_shape, finger_length, finger_taper, knuckle_visibility, nail_style`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: posture
**Entrada coloquial:** el usuario pide un output que afecta posture.  
**Acción del motor:** cargar Perfil360, filtrar campos `center_of_gravity, posture_base, spine_curve, shoulder_behavior, hip_alignment`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: qa
**Entrada coloquial:** output afecta qa; aplicar delta específico del caso.  
**Acción del motor:** cargar Perfil360, filtrar campos `same_body_blocker, wrong_age_body_blocker, impossible_pose_blocker, body_lens_distortion_rule, proportion_repair_rule`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
## Uso agente para Piel, dermatología visual, cabello y materialidad humana

### Grupo operativo: skin

| `skin_tone` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_subtone` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `pore_density` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `texture_zone_map` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `natural_marks` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fine_lines` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `specular_zones` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `matte_zones` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `makeup_rules` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_light_response` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_climate_response` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_age_response` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `anti_doll_markers` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `no_airbrush_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_camera_distance_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: hair

| `hair_color_base` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_subtone` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_density` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `strand_thickness` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hairline_shape` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_length` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_parting` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `layering_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `volume_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `frizz_level` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `baby_hairs` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `flyaway_hairs` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `humidity_response` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wind_response` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `strand_motion` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_shadow_contact` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_face_occlusion_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: detail

| `eye_wetness` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sclera_natural_variation` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lip_texture` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lip_specular_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `teeth_natural_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_hair_color_harmony` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_makeup_continuity` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_video_continuity` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| `plastic_skin_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_helmet_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `overblur_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `dead_eyes_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_tone_shift_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_length_drift_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `cgi_skin_repair` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: skin
**Entrada coloquial:** el usuario pide un output que afecta skin.  
**Acción del motor:** cargar Perfil360, filtrar campos `skin_tone, skin_subtone, pore_density, texture_zone_map, natural_marks`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: hair
**Entrada coloquial:** el usuario pide un output que afecta hair.  
**Acción del motor:** cargar Perfil360, filtrar campos `hair_color_base, hair_subtone, hair_density, strand_thickness, hairline_shape`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: detail
**Entrada coloquial:** el usuario pide un output que afecta detail.  
**Acción del motor:** cargar Perfil360, filtrar campos `eye_wetness, sclera_natural_variation, lip_texture, lip_specular_rule, teeth_natural_rule`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: qa
**Entrada coloquial:** output afecta qa; aplicar delta específico del caso.  
**Acción del motor:** cargar Perfil360, filtrar campos `plastic_skin_blocker, hair_helmet_blocker, overblur_blocker, dead_eyes_blocker, skin_tone_shift_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
## Uso agente para Voz hablada, lenguaje, acento, escritura, canto y música

### Grupo operativo: voice

| `vocal_age` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `timbre` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `pitch_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `resonance_place` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `breath_pattern` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `speaking_speed` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prosody_curve` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `pause_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `diction_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `emotional_color` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `micro_laugh` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `vocal_fatigue_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `recording_context_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `voice_identity_lock` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `voice_scene_response` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: language

| `accent_profile` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `peruvian_spanish_level` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `latam_neutrality_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sociolect_rules` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `slang_limit` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `formality_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `written_voice` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `caption_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `interview_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `dm_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `script_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `narration_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `inner_monologue_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `translation_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: music

| `song_vocal_texture` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `singing_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `suno_genre_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `rhythm_preference` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `instrumentation_palette` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lyric_perspective` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hook_style` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `chorus_energy` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `spoken_word_option` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `no_artist_imitation_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `music_identity_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `negative_music_tags` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `suno_arrangement_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| `wrong_voice_age_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `accent_caricature_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `generic_caption_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `artist_imitation_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `song_identity_drift_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `voice_text_mismatch_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `music_output_repair` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: voice
**Entrada coloquial:** el usuario pide un output que afecta voice.  
**Acción del motor:** cargar Perfil360, filtrar campos `vocal_age, timbre, pitch_range, resonance_place, breath_pattern`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: language
**Entrada coloquial:** el usuario pide un output que afecta language.  
**Acción del motor:** cargar Perfil360, filtrar campos `accent_profile, peruvian_spanish_level, latam_neutrality_rule, sociolect_rules, slang_limit`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: music
**Entrada coloquial:** el usuario pide un output que afecta music.  
**Acción del motor:** cargar Perfil360, filtrar campos `song_vocal_texture, singing_range, suno_genre_range, rhythm_preference, instrumentation_palette`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: qa
**Entrada coloquial:** output afecta qa; aplicar delta específico del caso.  
**Acción del motor:** cargar Perfil360, filtrar campos `wrong_voice_age_blocker, accent_caricature_blocker, generic_caption_blocker, artist_imitation_blocker, song_identity_drift_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
## Uso agente para Acting, FACS, microgestos, pose, caminada y continuidad de video

### Grupo operativo: face_acting

| `facs_base` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `smile_types` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `microgesture_set` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `eye_emotion_map` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brow_micro_movement` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `jaw_tension` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `mouth_corner_behavior` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `neck_tension` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `subtext_state` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `emotion_transition_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `camera_reaction_pattern` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `emotion_to_pose_map` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: body_motion

| `walking_rhythm` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `walking_weight` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hip_movement` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shoulder_countermotion` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `arm_swing` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hand_gesture_library` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `breathing_visibility` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `pose_energy` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `pose_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `dance_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `runway_presence` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `camera_presence` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `micro_action_library` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: video

| `video_continuity_lock` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `frame_to_frame_identity` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shot_transition_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `motion_blur_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_motion_continuity` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wardrobe_motion_continuity` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `voice_body_sync` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `acting_intention_per_shot` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `clip_complexity_limit` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `video_prompt_timeline` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| `rigid_pose_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fake_expression_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `morphing_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `video_identity_jump_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hands_warp_video_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `emotion_mismatch_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `motion_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `video_regression_test` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: face_acting
**Entrada coloquial:** el usuario pide un output que afecta face_acting.  
**Acción del motor:** cargar Perfil360, filtrar campos `facs_base, smile_types, microgesture_set, eye_emotion_map, brow_micro_movement`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: body_motion
**Entrada coloquial:** el usuario pide un output que afecta body_motion.  
**Acción del motor:** cargar Perfil360, filtrar campos `walking_rhythm, walking_weight, hip_movement, shoulder_countermotion, arm_swing`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: video
**Entrada coloquial:** el usuario pide un output que afecta video.  
**Acción del motor:** cargar Perfil360, filtrar campos `video_continuity_lock, frame_to_frame_identity, shot_transition_rule, motion_blur_rule, hair_motion_continuity`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: qa
**Entrada coloquial:** output afecta qa; aplicar delta específico del caso.  
**Acción del motor:** cargar Perfil360, filtrar campos `rigid_pose_blocker, fake_expression_blocker, morphing_blocker, video_identity_jump_blocker, hands_warp_video_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
## Uso agente para Wardrobe, bodywear editorial adulto, props, materiales y física textil

### Grupo operativo: wardrobe

| `wardrobe_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `color_palette` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `silhouette_preference` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fabric_preferences` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fabric_weight` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fabric_texture` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fit_rules` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `seam_visibility` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `drape_behavior` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wrinkle_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `support_physics` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `layering_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `season_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `occasion_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `body_shape_fit_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wardrobe_story_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: bodywear

| `bodywear_editorial_limits` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `swimwear_editorial_limits` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lingerie_non_explicit_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `adult_context_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `no_exploitation_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `camera_angle_safety` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `pose_safety` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `styling_alternative_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `commercial_safe_rewrite` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: props

| `accessory_rules` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `jewelry_limit` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_material` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_weight` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_scale` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hand_object_contact` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `object_shadow_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brand_logo_restrictions` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_scene_coherence` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `object_continuity_video` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_lineage_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| `floating_cloth_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `texture_flat_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wrong_style_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brand_logo_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `unsupported_bodywear_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_physics_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wardrobe_identity_drift_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `material_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: wardrobe
**Entrada coloquial:** el usuario pide un output que afecta wardrobe.  
**Acción del motor:** cargar Perfil360, filtrar campos `wardrobe_signature, color_palette, silhouette_preference, fabric_preferences, fabric_weight`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: bodywear
**Entrada coloquial:** el usuario pide un output que afecta bodywear.  
**Acción del motor:** cargar Perfil360, filtrar campos `bodywear_editorial_limits, swimwear_editorial_limits, lingerie_non_explicit_rule, adult_context_rule, no_exploitation_rule`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: props
**Entrada coloquial:** el usuario pide un output que afecta props.  
**Acción del motor:** cargar Perfil360, filtrar campos `accessory_rules, jewelry_limit, prop_material, prop_weight, prop_scale`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: qa
**Entrada coloquial:** output afecta qa; aplicar delta específico del caso.  
**Acción del motor:** cargar Perfil360, filtrar campos `floating_cloth_blocker, texture_flat_blocker, wrong_style_blocker, brand_logo_blocker, unsupported_bodywear_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
## Uso agente para Cámara, lente, iluminación, color, escena y física espacial

### Grupo operativo: camera

| `shot_type` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `camera_distance` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `camera_height` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `camera_angle` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lens_focal_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `aperture_range` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shutter_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `iso_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `white_balance` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sensor_look` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `depth_of_field_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `distortion_control` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `crop_safe_area` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `composition_grid` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `negative_space_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `camera_body_relation` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: lighting

| `key_light` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fill_light` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `rim_light` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `catchlight_pattern` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shadow_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `softness_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `contrast_ratio` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `color_temperature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `ambient_light` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `practical_lights` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_highlight_control` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_rim_control` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `eye_light_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `night_scene_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lighting_mood_map` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: scene

| `scene_location` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `period_context` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `weather_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `scale_contact` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `gravity_rules` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `reflection_rules` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `floor_contact` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wall_contact` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `background_depth` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `object_scale` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `cultural_context_safe` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lima_peru_context_option` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `set_dressing_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `scene_story_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| `lens_face_distortion_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `impossible_light_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shadow_mismatch_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `scale_error_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `cgi_grading_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `background_identity_conflict_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `scene_physics_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `environment_continuity_test` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: camera
**Entrada coloquial:** el usuario pide un output que afecta camera.  
**Acción del motor:** cargar Perfil360, filtrar campos `shot_type, camera_distance, camera_height, camera_angle, lens_focal_range`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: lighting
**Entrada coloquial:** el usuario pide un output que afecta lighting.  
**Acción del motor:** cargar Perfil360, filtrar campos `key_light, fill_light, rim_light, catchlight_pattern, shadow_logic`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: scene
**Entrada coloquial:** el usuario pide un output que afecta scene.  
**Acción del motor:** cargar Perfil360, filtrar campos `scene_location, period_context, weather_rule, scale_contact, gravity_rules`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: qa
**Entrada coloquial:** output afecta qa; aplicar delta específico del caso.  
**Acción del motor:** cargar Perfil360, filtrar campos `lens_face_distortion_blocker, impossible_light_blocker, shadow_mismatch_blocker, scale_error_blocker, cgi_grading_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
## Uso agente para Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage

### Grupo operativo: governance

| `status_internal` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `policy_set` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `compatible_with` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `source_trace` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `source_classification` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sha_lock` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lineage_lock` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `version_semver` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `migration_state` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `no_loss_evidence` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `audit_cycle` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `final_only_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `readback_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `rebuild_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `acceptance_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: sidecar

| `sidecar_schema` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `watermark_state` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `clean_master_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `c2pa_conceptual_note` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prompt_hash` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `output_hash` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `vendor_parameters` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `model_profile_hash` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `project_hash` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `qa_snapshot` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fallback_history` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `regression_test_link` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sidecar_required_fields` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: legal

| `privacy_review` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `ley_29733_review` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `license_review` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `likeness_review` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brand_logo_review` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `adult_editorial_review` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `data_minimization_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `consent_trace` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `commercial_use_flag` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `vendor_terms_flag` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `peru_context_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| `fail_code_schema` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fallback_schema` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `golden_test_schema` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `regression_test_schema` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `padding_linter` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `naming_linter` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `source_runtime_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `profile_fullness_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `copilot_render_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `chatgpt_load_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `project_factory_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `generic_visual_system_gate` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
#### Caso operativo 1: governance
**Entrada coloquial:** el usuario pide un output que afecta governance.  
**Acción del motor:** cargar Perfil360, filtrar campos `status_internal, policy_set, compatible_with, source_trace, source_classification`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: sidecar
**Entrada coloquial:** el usuario pide un output que afecta sidecar.  
**Acción del motor:** cargar Perfil360, filtrar campos `sidecar_schema, watermark_state, clean_master_rule, c2pa_conceptual_note, prompt_hash`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: legal
**Entrada coloquial:** el usuario pide un output que afecta legal.  
**Acción del motor:** cargar Perfil360, filtrar campos `privacy_review, ley_29733_review, license_review, likeness_review, brand_logo_review`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: qa
**Entrada coloquial:** output afecta qa; aplicar delta específico del caso.  
**Acción del motor:** cargar Perfil360, filtrar campos `fail_code_schema, fallback_schema, golden_test_schema, regression_test_schema, padding_linter`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  


## Phase 3 agent inheritance

## LEGACY_NON_AUTHORITY - ACTIVE_BLOCKING
Engine: IDUNEX_MOTOR_v1.0.0. Internal label: LEGACY_NON_AUTHORITY; not a semantic version. This block is embedded inside the runtime core file loaded by ChatGPT/Copilot and is not a documentary-only external reference.

Closed runtime policy: one ChatGPT agent per project and one Copilot agent per project; max 20 files per agent; max 10 models per project/agent; runtime formula = 10 core IDUNEX + 1 MODEL_RUNTIME_PROFILE_FULL per model; 1 model = 11 files; 2 models = 12 files; 5 models = 15 files; 10 models = 20 files; 11+ models = BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT. No split agents. No destructive summary. Digest, coverage map and evidence never replace the FULL model file.

Embedded mandatory controls: 
01. Conversational Operation Router.
02. Startup Capability Menu.
03. Project Intake Decision Tree.
04. Auto / Basic Guided / Detailed creation modes.
05. Auto Model Synthesis Engine.
06. Field Ownership Policy.
07. Update/Migration Variable Decision Gate.
08. Full Runtime Evidence Policy.
09. Agent Runtime Fit Planner.
10. Runtime Coverage Map obligatorio.
11. Agent Export Parity Gate.
12. Project Evidence Bundle.
13. TechExt Materialization Gate.
14. Alias Resolver desde Profile360.
15. Legacy Contamination Linter.
16. Project Core Namespace Gate.
17. Colloquial Fuzz Suite.
18. Universal Pre-Delivery Audit + Retry Loop.
19. No Summary As Completeness Policy.
20. Project Package 10/10 vs Output Real 10/10 Separation.
21. Policy Harmonization / No Duplicate Authority Gate.
22. 20-file runtime policy.
23. MODEL_RUNTIME_PROFILE_FULL per model.
24. No split agent policy.
25. Max 10 models policy.

MODEL_RUNTIME_PROFILE_FULL per model is mandatory and must materialize Profile360 FULL60, TechExt FULL10, Master Visual Anchors, aliases, Face360, Body360, Skin360, Hair360, Wardrobe360, Voice360, Motion360, Scene/Environment affinity, camera/lighting rules, image/video reference rules, voice/audio/music/Suno/ElevenLabs rules, sidecar mapping, QA/fallbacks and source trace. No null, blank, placeholder or pending FACTORY_DEFINED_PROPOSED can remain in a final project delivery.

Runtime evidence gate: PROJECT_RUNTIME_COVERAGE_MAP required; Project Evidence Bundle required; Agent Export Parity Gate required; TechExt materialization required; alias resolver from Profile360 required; legacy contamination blocked; Project Core namespace gate required. PROJECT_PACKAGE_10_10 != OUTPUT_REAL_10_10. OUTPUT_REAL_10_10 requires asset + sidecar + prompt_hash + output_hash + QA + reviewer + lineage.

Truthfulness gate: if independent audit finds FAIL, delivery is blocked. No PASS with empty actual_value. Retry until 100% PASS. Policy harmonization/no duplicate authority gate blocks parallel authorities that conflict with LEGACY_NON_AUTHORITY.

Blocking fail codes: BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT, BLOCKED_TECH_EXT_NOT_MATERIALIZED, BLOCKED_TECH_EXT_NULL_INHERITANCE, BLOCKED_RUNTIME_COVERAGE_MAP_MISSING, BLOCKED_MODEL_ALIAS_NOT_RESOLVED, BLOCKED_LEGACY_MODEL_OUTSIDE_NAMESPACE, BLOCKED_PROJECT_CORE_PREFIX_DUPLICATE, BLOCKED_OUTPUT_REAL_10_10_WITHOUT_ASSET, BLOCKED_TRUTHFULNESS_INDEPENDENT_FAIL, BLOCKED_POLICY_DUPLICATE_AUTHORITY, BLOCKED_SUMMARY_AS_COMPLETENESS, BLOCKED_CONFIG_8000_REQUIRED_TOKEN_MISSING, BLOCKED_RUNTIME_CORE_LEGACY_NON_AUTHORITY.

## H71-H80 SAFE_APPAREL_WATERMARK_AGENT10N
H71_H80_AGENT10N=SAFE_APPAREL_TAXONOMY; ADULT_REVEALING_APPAREL_NOT_NUDITY; VENDOR_PROMPT_SANITIZATION_SAFE_APPAREL; WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED; ALLOW adult editorial beachwear/swimwear/intimate apparel/catalog/corset/body/performance wardrobe when covered non-explicit; BLOCK nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded or school-coded sexualization and real-person copying.
ALLOW_ADULT_EDITORIAL: moda de playa, traje de bano, ropa de bano, bikini editorial, swimwear campaign, beachwear, resortwear, moda intima editorial/catalog, ropa interior de catalogo, corset/body/bodysuit, vestuario de show adulto, vestuario de videoclip adulto y outfit de performance adulta cuando el modelo es adulto, cubierto y no explicito.
CONDITIONAL_REWRITE: convertir styling glam/provocativo, boudoir editorial, fantasia adulta y vestuario de alto impacto a lenguaje adulto, editorial, comercial, non-explicit, covered intimate areas.
BLOCK_ALWAYS: nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded styling, school-coded sexualization, real-person copying y cualquier intento de saltar locks de edad o identidad.
WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED.

## H165-H180 Creative Canon Safety Realism - active canonical block
Restricciones: Politica adulta editorial segura: permite ropa de bano, lenceria, glamour adulto y pose sensual con ropa para adultos ficticios; bloquea desnudez, sexo explicito, pornografia, exposicion intima, apariencia menor, school-coded sexualizado, coercion, copia real no autorizada y evasion de politicas.

- UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA=PASS; applies before every generative handoff across image, video, voice/audio, music/Suno, text/copy/doc, Copilot DOCX, ChatGPT runtime upload, AGPT prompt packs and sidecar instructions.
- CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS=PASS; technical identity tokens remain in JSON/lineage/QA/hashes only. Creative surfaces use humanized adult fictional descriptors.
- PROFILE360_TECHEXT_ALL_MEDIA_BINDING=PASS; Profile360 61/61 and TechExt 284/284 are read with locks before output.
- HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS=PASS; NEGATIVE / AVOID: plastic skin, wax skin, porcelain skin, doll-like face, mannequin body, toy-like proportions, generic stock model, dead eyes, glassy eyes, frozen expression, helmet hair, rubber skin, over-smoothed skin, AI plastic look, duplicated face, same-face syndrome, deformed hands, extra fingers, warped joints, fake fabric, logo artifacts, text artifacts. ES: evitar piel plástica, rostro de muñeco, cuerpo de maniquí, proporciones de juguete, modelo genérico de stock, ojos muertos, ojos vidriosos, expresión congelada, cabello tipo casco, piel encerada, piel demasiado suavizada, manos deformes, dedos extra, articulaciones deformes, tela falsa, artefactos de logos, artefactos de texto.
- BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK=PASS; PROJECT_BRAND_ENTITY verified own brand allows exact logo without legal disclaimer; verified third-party asset routes to sidecar/disclaimer; unverified third-party exact logo degrades safely instead of blocking whole output.
- LEGAL_WATERMARK_ROUTER_PASS=PASS; short visible disclaimer when required: Uso referencial. Sin afiliación oficial.
- CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT=PASS; default locality is PROJECT_DECLARED_LOCALITY contemporary unless a different place is declared.
- PROMPT_PACK_STRUCTURE_ALL_OUTPUTS=PASS; A_HEADER through J_FALLBACK_FIXES are mandatory for image/video prompt packs.
