## Phase 3 file-level inheritance
inherits = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RESEARCH_LANDING_RULE
inherits_runtime_qa = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RUNTIME_QA_BLOCK
research_specific_extracts_preserved = true

# Research Runtime Library — Cámara, lente, iluminación, color, escena y física espacial

**Motor:** IDUNEX_MOTOR_v1.0.0_20260614  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**Fecha de generación:** 20260613  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.



Aterriza fotografía y video en óptica, sensor, focal, luz, sombras, composición, grading, entorno, contacto, escala y coherencia espacial.

## Fuentes vinculadas

- **SRC_004_Dermatolog_a_visual_realista** | Dominio: skin_hair_realism | Palabras: 5638 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: textura, poros, puede, arrugas, imagen, prompts, iluminación, detalles, natural, vídeo.
- **SRC_005_Cabello_peinados_y_f_sica_capilar** | Dominio: skin_hair_realism | Palabras: 13582 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: cabello, video, hebras, puede, movimiento, peinado, estilo, ejemplo, imagen, mechones.
- **SRC_017_C_mara_sensor_lente_y_fotograf_a_premium** | Dominio: skin_hair_realism | Palabras: 6096 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: iluminación, ejemplo, color, imagen, prompts, fondo, fotográ, medio, cámara, formato.

## Campos derivados


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

## Reglas y casos

**Regla 01 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 02 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 03 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 04 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 05 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 06 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 07 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 08 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 09 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 10 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 11 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 12 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 13 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 14 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 15 — Cámara, lente, iluminación, color, escena y física espacial**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

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
**Entrada coloquial:** el usuario pide un output que afecta qa.  
**Acción del motor:** cargar Perfil360, filtrar campos `lens_face_distortion_blocker, impossible_light_blocker, shadow_mismatch_blocker, scale_error_blocker, cgi_grading_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

## Extractos transformados de investigación

### Extracto transformado 001
**Hallazgo fuente:** --- SOURCE: Dermatolog a visual realista ---
Piel humana realista en IA: Guía
integral visual y textual
La ﬁdelidad de la piel humana en la inteligencia artiﬁcial (IA) requiere
capturar y describir con detalle las características auténticas de la piel, ya sea
en fotografías y vídeos reales o en los prompts y anotaciones para modelos
generativos.




### Extracto transformado 002
**Hallazgo fuente:** Los microdetalles (poros, arrugas, vello, brillos naturales, etc.)
marcan la diferencia entre un resultado convincente y la temida piel
“plástica”.




### Extracto transformado 003
**Hallazgo fuente:** En esta guía práctica exploramos cómo documentar visualmente
estos rasgos en sesiones de foto/vídeo realistas, y cómo describirlos
textualmente en prompts y metadatos de datasets, evitando estereotipos
étnicos y la falta de realismo.




### Extracto transformado 004
**Hallazgo fuente:** Se abordan también la inﬂuencia de edad,
iluminación, clima y equipos en la apariencia de la piel, técnicas para
prevenir la sobre-suavización no deseada, procedimientos de QA visual en
diversos contextos y estrategias de corrección cuando los resultados no son
los esperados.




### Extracto transformado 005
**Hallazgo fuente:** Presentamos ejemplos de prompts y esquemas de metadatos
útiles para un pipeline end-to-end abarcando fotografía, vídeo, modelado
generativo y veriﬁcación de calidad.




### Extracto transformado 006
**Hallazgo fuente:** Atributos esenciales de la piel a documentar y
describir
Los rasgos clave de una piel humana realista son aquellos detalles que
hacen que luzca natural y creíble, y deben ser capturados en la fotografía o
vídeo real y también descritos en los prompts y metadatos si se entrena o
utiliza un modelo generativo.




### Extracto transformado 007
**Hallazgo fuente:** Variaciones en la piel por edad, iluminación,
clima, actividad y cámara
Además de las características intrínsecas de la piel, su apariencia varía según
múltiples factores externos e internos como la edad de la persona, el tipo e
intensidad de la luz, las condiciones ambientales y la actividad física reciente.




### Extracto transformado 008
**Hallazgo fuente:** Comprender estas variaciones contextuales es fundamental
para documentar adecuadamente la piel y prever su representación
correcta en IA:




### Extracto transformado 009
**Hallazgo fuente:** Las pieles jóvenes (20-30 años) tienden a
tener una textura más tersa, mayor elasticidad y tono más uniforme, aunque
pueden presentar acné o poros más abiertos en pieles grasas.




### Extracto transformado 010
**Hallazgo fuente:** ej., >50 años) la piel pierde ﬁrmeza, se vuelve más ﬁna y
menos elástica, y suele presentar arrugas, pliegues marcados y manchas (p.




### Extracto transformado 011
**Hallazgo fuente:** También aumenta la sequedad: alrededor
del 85% de las personas mayores sufren sequedad de “invierno” por pérdida de
glándulas sebáceas y baja humedad 7 .




### Extracto transformado 012
**Hallazgo fuente:** Por tanto, en la fotografía editorial, se
deben respetar las huellas de la edad (no eliminarlas por completo en
posproducción) para reﬂejar la madurez del sujeto.




### Extracto transformado 013
**Hallazgo fuente:** Igualmente, en prompts
conviene especiﬁcar la edad aproximada o rango (“mujer de 45 años con
arrugas ﬁnas y manchas suaves”) para guiar al modelo a generar los signos de
edad correctos.




### Extracto transformado 014
**Hallazgo fuente:** Tipo e intensidad de la luz (iluminación): La iluminación inﬂuye
dramáticamente en la apariencia de la piel.




### Extracto transformado 015
**Hallazgo fuente:** ej., sol
directo o ﬂash sin difusor) acentúa cada irregularidad creando sombras
marcadas en arrugas y poros 8 .




### Extracto transformado 016
**Hallazgo fuente:** Esto realza la textura pero puede exagerar
defectos (útil para estilos dramáticos o retratos con grit).




### Extracto transformado 017
**Hallazgo fuente:** En cambio, la luz
suave (difusa, de ventana, de un softbox) envuelve la piel suavizando
arrugas y uniformando el tono 8 ; ideal para retratos de belleza o publicidad
donde se busca un look más ﬂaterring.




### Extracto transformado 018
**Hallazgo fuente:** La dirección de la luz también
importa: luz lateral o cenital proyecta sombras en surcos y poros (dando
profundidad y realce de textura), mientras que luz frontal o muy baja reduce
sombras y puede aplanar la textura 8 .




### Extracto transformado 019
**Hallazgo fuente:** En IA, es crucial describir la fuente y
estilo de luz en los prompts para controlar cómo se mostrará la piel (ejemplos:
“iluminación de atardecer lateral (golden hour) acentuando la textura de la
piel” 2 vs.




### Extracto transformado 020
**Hallazgo fuente:** Esto
constriñe la interpretación del modelo y puede marcar la diferencia entre
una piel detallada y otra plásticamente lisa 2 4 .




### Extracto transformado 021
**Hallazgo fuente:** Clima y ambiente: Las condiciones ambientales y el clima circundante
afectan tanto la ﬁsiología de la piel real como su aspecto en imágenes:




### Extracto transformado 022
**Hallazgo fuente:** --- SOURCE: Cabello peinados y física capilar ---
Informe: Cómo deﬁnir cabello
humano realista para modelos de IA
en imagen, video y 3D
El cabello es uno de los elementos más desaﬁantes en la generación de
contenido visual realista con Inteligencia Artiﬁcial (IA).




### Extracto transformado 023
**Hallazgo fuente:** Reproducirlo
ﬁelmente en imágenes 2D generadas por IA, en videos o en modelos 3D/
avatares exige entender sus propiedades físicas y estéticas.




### Extracto transformado 024
**Hallazgo fuente:** A continuación se
presenta una guía completa y operativa, organizada en siete apartados,
abarcando desde la estructura del cabello hasta la validación de resultados.




### Extracto transformado 025
**Hallazgo fuente:** Está adaptada para todos los stacks (2D, video generativo, 3D) y considera
todas las diversidades capilares: cabello lacio, ondulado, rizado, afro
(también conocido como coily), con variaciones étnicas, y cómo afectan
factores como clima y humedad.




### Extracto transformado 026
**Hallazgo fuente:** También se incluyen ejemplos concretos,
recetas por escena y comparaciones en tablas para destacar diferencias entre
enfoques 2D, video y 3D, respaldado por fuentes autoritativas
(investigaciones académicas, documentos de la industria, manuales técnicos
oﬁciales).




### Extracto transformado 027
**Hallazgo fuente:** Cada sección comienza con los aspectos
cruciales, seguidos de explicaciones detalladas para dar un contexto completo.




### Extracto transformado 028
**Hallazgo fuente:** Estructura del cabello: propiedades físicas y
visuales fundamentales
Resumen: Para deﬁnir un cabello realista en IA, primero necesitamos
comprender las características físicas del cabello humano real.




### Extracto transformado 029
**Hallazgo fuente:** Las
propiedades clave incluyen tipo de cabello (forma del rizo o lacio), grosor y
diámetro de las hebras (ej.




### Extracto transformado 030
**Hallazgo fuente:** su rango en micrómetros), densidad por área
(cantidad de cabellos por cm²), volumen visual, patrón de rizo (grado u forma
del rizado), raya o división y nacimiento del cabello (línea de
implantación), presencia de baby hairs (pelos ﬁnos en la frente o sienes),
frizz (encrespamiento), nivel de brillo (reﬂejos especulares y componente
difuso), aspecto de puntas (condición, puntas abiertas), daño (sequedad,
quiebre), efectos de humedad o electrostática, presencia de canas, tintes y la
transición del cuero cabelludo a la hebra.




### Extracto transformado 031
**Hallazgo fuente:** Todos estos aspectos deberán ser
modelados o descritos en prompts/parametrizaciones para cada stack de IA.




### Extracto transformado 032
**Hallazgo fuente:** Tipo y patrón de rizo: Los cabellos se clasiﬁcan según su textura y forma
predominantemente en cuatro grupos: lacio (recto), ondulado, rizado y afro
(coily).




### Extracto transformado 033
**Hallazgo fuente:** Esta tipología, conocida como sistema 1A–4C, detalla subtipos por
grado de rizo: 1A–1C se reﬁere a lacio liso, 2A–2C a ondulado leve, 3A–3C a
rizado de bucles amplios a más apretados, y 4A–4C al cabello afro/ensortijado
de rizos muy apretados.




### Extracto transformado 034
**Hallazgo fuente:** Un cabello lacio es casi completamente recto; su
sección transversal suele ser circular, lo que le da mayor rigidez y brillo
uniforme 1 .




### Extracto transformado 035
**Hallazgo fuente:** El cabello ondulado forma curvas en “S” suaves; rizado tiene
espirales más deﬁnidas, con secciones transversales ovaladas; y el afro o coily
presenta rizos sumamente apretados y una sección transversal plana o
elíptica 1 .




### Extracto transformado 036
**Hallazgo fuente:** Esta forma de la sección transversal inﬂuye en cómo el cabello se
curva: las hebras planas u ovaladas tienden a enroscarse más (como en
cabellos afros), mientras que las cilíndricas se alinean rectas 1 .




### Extracto transformado 037
**Hallazgo fuente:** Grosor de las hebras (diámetro): El diámetro de un cabello humano típico
varía entre ~17 y 181 micrones (0.017 a 0.181 mm) 1 .




### Extracto transformado 038
**Hallazgo fuente:** En promedio es de unos
~70 μm 1 , aunque el rango es amplio: los cabellos ﬁnos suelen medir ~15–50
μm (translúcidos, frágiles), los medianos de 50–90 μm (estándar común) y los
gruesos o “coarse” pueden superar 90 μm (alcanzando 120–150 μm en casos
extremos) 1 .




### Extracto transformado 039
**Hallazgo fuente:** Variaciones étnicas: Los estudios muestran diferencias, con
el cabello asiático siendo el más grueso (muchos trazos de 80 a 120 μm,
superando el promedio global) 1 , caucásico con grosor intermedio
(típicamente 50–90 μm) 1 , y el cabello afro presentando la paradoja de verse
muy voluminoso por sus rizos cerrados, aunque sus hebras individuales
tienden a ser más ﬁnas que las asiáticas 1 .




### Extracto transformado 040
**Hallazgo fuente:** En cabelleras reales, el grosor
inﬂuye en la textura: pelos más gruesos son más rígidos y resistentes; los
ﬁnos, más ﬂexibles pero también más propensos a romperse 1 .




### Extracto transformado 041
**Hallazgo fuente:** Un adulto promedio tiene entre 100,000 y 150,000 cabellos
en unos 600 cm² de cuero cabelludo, es decir, entre ~100 y 150 cabellos/
cm² 2 .




### Extracto transformado 042
**Hallazgo fuente:** Menos de 100 cabellos/cm² se considera baja densidad (con el cuero
cabelludo visible en ciertas condiciones) 2 , mientras densidades mayores a 150
cabellos/cm² dan una melena muy tupida y de gran volumen 2 .




### Extracto transformado 043
**Hallazgo fuente:** La densidad y
el grosor conjuntamente determinan el volumen aparente: hebras gruesas
con baja densidad pueden lucir escasas, mientras hebras ﬁnas pero muy
numerosas se ven abundantes.




### Extracto transformado 044
**Hallazgo fuente:** En contextos de IA, para imágenes 2D se puede
“imitar” mayor densidad describiendo el cabello como “espeso, con mucha
cantidad” o incidiendo en el volumen (“melena abundante”), mientras en
modelos 3D se logra generando suﬁcientes strands o hair cards para cubrir el
cuero cabelludo (evitando “huecos” por donde la piel asome).




### Extracto transformado 045
**Hallazgo fuente:** Si el modelo 3D
permite simular densidades variables, puede calibrarse el número de hebras o
clumps por superﬁcie para diferentes densidades: por ejemplo, ~120 hebras
guía por cm² para densidad media, y quizás >150/cm² para una super
melena 2 .




### Extracto transformado 046
**Hallazgo fuente:** Raya y nacimiento (hairline) y baby hairs: La raya en el cabello es la línea
donde el cabello se divide (central, lateral, en zigzag, etc.), inﬂuyendo en la
distribución y caída del pelo.




### Extracto transformado 047
**Hallazgo fuente:** El nacimiento del
cabello (línea de implantación o hairline) determina la forma en que el pelo
enmarca el rostro: puede ser recto, con entradas, pico de viuda, etc., y es
fundamental para realismo en retratos de IA.




### Extracto transformado 048
**Hallazgo fuente:** Por ejemplo, las entradas
(retrocesos en las sienes) son comunes especialmente en hombres y su
ausencia puede volver un modelo facial inverosímil.




### Extracto transformado 049
**Hallazgo fuente:** Detalles como pequeños
cabellos (baby hairs) en la frente o sienes aportan realismo, por lo cual los
grooms 3D suelen incluir primitivas para estos pelitos, y en prompts conviene




### Extracto transformado 050
**Hallazgo fuente:** Cuidado con la simetría excesiva: En la naturaleza el cabello no es
perfectamente simétrico; para evitar apariencia plástica o de “peluca”, es
aconsejable introducir ligeras variaciones y asimetrías en la raya y contorno
capilar.




### Extracto transformado 051
**Hallazgo fuente:** En 3D, los diseñadores suelen romper la simetría deliberadamente en
los grooms, añadiendo baby hairs y mechones no simétricos 3 .




### Extracto transformado 052
**Hallazgo fuente:** Existen componentes especulares (reﬂejos brillantes a lo largo de las hebras)
y un componente difuso (la luz dispersa suavemente).




### Extracto transformado 053
**Hallazgo fuente:** El cabello totalmente
opaco y sin reﬂejos se ve mate o “muerto”, mientras que un brillo excesivo y
uniforme genera el efecto plástico o de muñeca. [TECHNICAL_LEGACY_TERM_NOT_CREATIVE_RUNTIME]




### Extracto transformado 054
**Hallazgo fuente:** Para un brillo realista, el
modelo debe simular la reﬂectancia anisotrópica de las ﬁbras capilares: por
ejemplo, usando shaders especializados como Kajiya-Kay (1989) o Marschner
(2003), que reproducen reﬂejos duales (un highlight principal y un glint
secundario en la melena) 4 .




### Extracto transformado 055
**Hallazgo fuente:** Si esto es muy técnico para un proyecto, se puede
imitar descriptivamente: en prompts de Stable Diﬀusion y similares, se logra
con frases como “cabello brillante y sedoso, reﬂejos sutiles bajo la luz, con brillo
natural”.




### Extracto transformado 056
**Hallazgo fuente:** Para modelos 3D, se ajustan parámetros del material capilar: por
ejemplo, en Blender puede usarse el shader Principled Hair de Cycles con un
valor apropiado de melanina (parámetro que controla tanto el color natural –
pigmento– como la cantidad de brillo y transparencia de cada hebra) 3 .




### Extracto transformado 057
**Hallazgo fuente:** Un
truco práctico es combinar brillos heterogéneos: algunas hebras más opacas
que otras, y añadir microvariaciones en rugosidad, para evitar una reﬂexión
de luz “de casco”.




### Extracto transformado 058
**Hallazgo fuente:** Frizz y puntas (acabado de hebras): El frizz es el encrespamiento o esos
mechones rebeldes que se alejan de la masa principal del cabello (cabellos
sueltos).




### Extracto transformado 059
**Hallazgo fuente:** Un cabello completamente “peinado” sin ningún frizz suele parecer
artiﬁcial; conviene incluir algo de frizz (p.




### Extracto transformado 060
**Hallazgo fuente:** ej., “con algunos pelitos sueltos
para un aspecto natural”) o en 3D usar parámetros de clumping y randomness
para que un porcentaje de hebras se separe ligeramente de los mechones
principales (p.




### Extracto transformado 061
**Hallazgo fuente:** Las puntas del cabello real casi nunca son
perfectamente uniformes: pueden estar aﬁnadas o abiertas en casos de
cabello dañado.




### Extracto transformado 062
**Hallazgo fuente:** Para replicar esto, en 3D se modula el grosor de la hebra de
raíz a punta (taper progresivo) y se puede dar color ligeramente más claro/
opaco a las puntas para simular resequedad o decoloración.




### Extracto transformado 063
**Hallazgo fuente:** similar, en un prompt se pueden agregar detalles como “puntas ligeramente
más claras” o “ligeramente abiertas” para sugerir ese acabado realista.




### Extracto transformado 064
**Hallazgo fuente:** Humedad y estática: El cabello es higroscópico; en ambientes húmedos
absorbe agua, aumentando su diámetro y relajando los enlaces de hidrógeno
en la queratina.




### Extracto transformado 065
**Hallazgo fuente:** En cambio, en ambientes secos (especialmente con aire frío y seco)
puede cargarse de electricidad estática, haciendo que algunos pelos se
separen y se ericen.




### Extracto transformado 066
**Hallazgo fuente:** Al modelar, se debe considerar la humedad como
parámetro: cabellos en escenas lluviosas o húmedas estarán más pesados y
apelmazados, con menos volúmen y más rizos ﬂojos o encrespados; en
entornos áridos podrían aparecer hebras sueltas por estática.




### Extracto transformado 067
**Hallazgo fuente:** Visualmente, el
cabello mojado pierde volumen y se agrupa en mechones más gruesos (por la
tensión superﬁcial del agua), con un brillo especular más intenso pero difuso.




### Extracto transformado 068
**Hallazgo fuente:** En un prompt, se puede indicar “cabello mojado, agrupado por el agua, con
mechones pegados a la frente” para generar este look; en 3D, la simulación de
cabello mojado puede lograrse aumentando la masa efectiva de las hebras y
disminuyendo su stiﬀness, además de aplicar un shader con reﬂejos más
intensos para simular la película de agua.




### Extracto transformado 069
**Hallazgo fuente:** Los cabellos oscuros tienen más melanina y tienden a absorber más
luz (menor brillo visible), mientras los rubios tienen menos pigmento y
maniﬁestan highlight más evidentes.




### Extracto transformado 070
**Hallazgo fuente:** Además, el número total de cabellos varía
por color natural: personas rubias suelen tener hasta ~150 mil cabellos,
mientras las pelirrojas promedian unos 90 mil 5 , como muestra la gráﬁca a
continuación.




### Extracto transformado 071
**Hallazgo fuente:** Este es un factor evolutivo: colores más claros compensan su
menor grosor con mayor densidad, y viceversa 5 .




### Extracto transformado 072
**Hallazgo fuente:** Las melenas rubias tienden
a tener mayor número de hebras, mientras que las pelirrojas suelen tener menos
cantidad pero con hebras más gruesas 5 .




### Extracto transformado 073
**Hallazgo fuente:** En aplicaciones de IA generativa, indicar correctamente el color base y
matices es clave: por ejemplo, “cabello castaño oscuro con reﬂejos dorados”
(incluyendo las palabras “tonos cálidos, mechas sutiles”, etc.).




### Extracto transformado 074
**Hallazgo fuente:** Canas: Cabellos
grises o blancos entremezclados suman realismo, pero pueden confundir al
modelo si no está entrenado en sus p




### Extracto transformado 075
**Hallazgo fuente:** --- SOURCE: Cámara sensor lente y fotograf a premium ---
Estándar técnico más alto en
fotografía profesional para IA:
Cámara, óptica, iluminación,
realismo y control de calidad
La fotografía profesional de alta gama marca la referencia para la generación
de imágenes realistas con modelos de IA.




### Extracto transformado 076
**Hallazgo fuente:** Alcanzar resultados que emulen
capturas fotográﬁcas profesionales requiere incorporar tanto conocimientos
técnicos (cámaras, lentes, parámetros de captura, iluminación) como
habilidades de prompt engineering y estrategias de entrenamiento, para
reproducir las cualidades ópticas y estéticas de la mejor fotografía tradicional.




### Extracto transformado 077
**Hallazgo fuente:** Cámaras y captura: sensores, óptica y
parámetros técnicos al más alto nivel
En la fotografía profesional de vanguardia se emplean cámaras de sensor
grande (full-frame y formato medio) y lentes de altísima calidad para
maximizar la resolución, rango dinámico y ﬁdelidad de color.




### Extracto transformado 078
**Hallazgo fuente:** Estas
cualidades – esenciales en imágenes de moda, publicidad o belleza – deben
trasladarse también a los modelos de IA para lograr resultados equiparables.




### Extracto transformado 079
**Hallazgo fuente:** En resumen, el estándar dorado del equipo fotográﬁco en la actualidad lo
marcan sensores full-frame y formato medio con decenas de megapíxeles y
amplia latitud tonal, combinados con ópticas de gran apertura y alta
resolución (preferiblemente ﬁjas, de marcas como Canon L, Nikon S, Zeiss,
etc.) para lograr imágenes “perfectas”.




### Extracto transformado 080
**Hallazgo fuente:** La IA puede beneﬁciarse de estas
referencias: al incorporar marcas y modelos de cámaras, focales y valores de
exposición en los prompts, estamos entregando al modelo semánticas de la
fotografía real que incrementan la credibilidad del resultado visual 5 6 .




### Extracto transformado 081
**Hallazgo fuente:** Adaptando la técnica según el tipo de toma:
retrato, cuerpo entero, editorial, beauty, campaña,
baja luz y backstage
La fotografía profesional abarca diferentes géneros – desde primeros planos
de belleza hasta escenas de moda en pasarela – cada uno con exigencias




### Extracto transformado 082
**Hallazgo fuente:** Para replicar con IA estos estilos, conviene entender qué
distingue a cada tipo de toma en la práctica fotográﬁca tradicional:
