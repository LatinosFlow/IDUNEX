# Cámara, lente, iluminación, composición, color y look premium

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.



## 1. Mandato de cobertura 10/10
Este core es obligatorio para cualquier proyecto IDUNEX. No funciona como resumen; define reglas de decisión, campos, matrices, QA, fallbacks y relación con agent-load. Debe operar en creación, actualización, diagnóstico, prompt, sidecar y auditoría.


## 2. Dominios conectados


### Cámara, lente, iluminación, color, escena y física espacial
Aterriza fotografía y video en óptica, sensor, focal, luz, sombras, composición, grading, entorno, contacto, escala y coherencia espacial.

**Fuentes aterrizadas:**
- **SRC_004_Dermatolog_a_visual_realista** | Dominio: skin_hair_realism | Palabras: 5638 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: textura, poros, puede, arrugas, imagen, prompts, iluminación, detalles, natural, vídeo.
- **SRC_005_Cabello_peinados_y_f_sica_capilar** | Dominio: skin_hair_realism | Palabras: 13582 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: cabello, video, hebras, puede, movimiento, peinado, estilo, ejemplo, imagen, mechones.
- **SRC_017_C_mara_sensor_lente_y_fotograf_a_premium** | Dominio: skin_hair_realism | Palabras: 6096 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: iluminación, ejemplo, color, imagen, prompts, fondo, fotográ, medio, cámara, formato.


#### Matriz runtime

### Grupo operativo: camera

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
| `lens_face_distortion_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `impossible_light_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `shadow_mismatch_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `scale_error_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `cgi_grading_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `background_identity_conflict_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `scene_physics_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `environment_continuity_test` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

#### Reglas invariantes
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

#### Casos operativos
#### Caso operativo 1: camera
**Entrada coloquial:** el usuario pide un output que afecta camera.  
**Acción del motor:** cargar Perfil360, filtrar campos `shot_type, camera_distance, camera_height, camera_angle, lens_focal_range`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 2: lighting
**Entrada coloquial:** el usuario pide un output que afecta lighting.  
**Acción del motor:** cargar Perfil360, filtrar campos `key_light, fill_light, rim_light, catchlight_pattern, shadow_logic`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 3: scene
**Entrada coloquial:** el usuario pide un output que afecta scene.  
**Acción del motor:** cargar Perfil360, filtrar campos `scene_location, period_context, weather_rule, scale_contact, gravity_rules`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 4: qa
**Entrada coloquial:** el usuario pide un output que afecta qa.  
**Acción del motor:** cargar Perfil360, filtrar campos `lens_face_distortion_blocker, impossible_light_blocker, shadow_mismatch_blocker, scale_error_blocker, cgi_grading_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

### Piel, dermatología visual, cabello y materialidad humana
Controla textura, subtono, poros, brillo, marcas naturales, maquillaje, cabello, frizz, humedad y movimiento. Evita muñeco digital, piel plástica y pelo casco. [NEGATIVE_AVOID_ALLOWED_NOT_CREATIVE_IDENTITY_LABEL] [NEGATIVE_AVOID_ALLOWED_NOT_CREATIVE_IDENTITY]

**Fuentes aterrizadas:**
- **SRC_004_Dermatolog_a_visual_realista** | Dominio: skin_hair_realism | Palabras: 5638 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: textura, poros, puede, arrugas, imagen, prompts, iluminación, detalles, natural, vídeo.
- **SRC_005_Cabello_peinados_y_f_sica_capilar** | Dominio: skin_hair_realism | Palabras: 13582 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: cabello, video, hebras, puede, movimiento, peinado, estilo, ejemplo, imagen, mechones.
- **SRC_017_C_mara_sensor_lente_y_fotograf_a_premium** | Dominio: skin_hair_realism | Palabras: 6096 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: iluminación, ejemplo, color, imagen, prompts, fondo, fotográ, medio, cámara, formato.


#### Matriz runtime

### Grupo operativo: skin

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
| `eye_wetness` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `sclera_natural_variation` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lip_texture` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lip_specular_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `teeth_natural_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_hair_color_harmony` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_makeup_continuity` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_video_continuity` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
| `plastic_skin_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_helmet_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `overblur_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `dead_eyes_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `skin_tone_shift_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hair_length_drift_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `cgi_skin_repair` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

#### Reglas invariantes
**Regla 01 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 02 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 03 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 04 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 05 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 06 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 07 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 08 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 09 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 10 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 11 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 12 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 13 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 14 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 15 — Piel, dermatología visual, cabello y materialidad humana**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

#### Casos operativos
#### Caso operativo 1: skin
**Entrada coloquial:** el usuario pide un output que afecta skin.  
**Acción del motor:** cargar Perfil360, filtrar campos `skin_tone, skin_subtone, pore_density, texture_zone_map, natural_marks`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 2: hair
**Entrada coloquial:** el usuario pide un output que afecta hair.  
**Acción del motor:** cargar Perfil360, filtrar campos `hair_color_base, hair_subtone, hair_density, strand_thickness, hairline_shape`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 3: detail
**Entrada coloquial:** el usuario pide un output que afecta detail.  
**Acción del motor:** cargar Perfil360, filtrar campos `eye_wetness, sclera_natural_variation, lip_texture, lip_specular_rule, teeth_natural_rule`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 4: qa
**Entrada coloquial:** el usuario pide un output que afecta qa.  
**Acción del motor:** cargar Perfil360, filtrar campos `plastic_skin_blocker, hair_helmet_blocker, overblur_blocker, dead_eyes_blocker, skin_tone_shift_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

### Rostro forense, landmarks, edad visual y autenticación de identidad
Fija rostro no intercambiable: forma, proporciones, ojos, cejas, nariz, labios, sonrisa, asimetría, respuesta a óptica/luz y QA anti wrong-face/same-face.

**Fuentes aterrizadas:**
- **SRC_002_Biometr_a_facial_forense** | Dominio: face_forensics | Palabras: 7204 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: rostro, rasgos, ejemplo, forma, nariz, puede, imágenes, medidas, distancia, imagen.
- **SRC_009_Religi_n_espiritualidad_y_cosmovisi_n** | Dominio: face_forensics | Palabras: 8814 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: personaje, idunex, ejemplo, cosmovisión, cultural, religiosa, puede, religión, creencias, liación.
- **SRC_011_Microexpresiones_y_FACS** | Dominio: face_forensics | Palabras: 5086 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: sonrisa, expresión, puede, microexpresiones, mirada, ejemplo, facial, rostro, ligeramente, sutil.
- **SRC_021_Video_IA_y_continuidad_entre_planos** | Dominio: face_forensics | Palabras: 7888 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: personaje, cámara, movimiento, ejemplo, iluminación, plano, tomas, prompts, continuidad, referencia.
- **SRC_024_Escritura_pensamiento_y_voz_interna** | Dominio: face_forensics | Palabras: 5673 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: personaje, ejemplo, puede, narrativa, estilo, persona, coherencia, capas, personalidad, interno.
- **SRC_031_Proporciones_fitness_por_edad_adulta** | Dominio: face_forensics | Palabras: 5822 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: tness, postura, modelos, proporciones, ejemplo, puede, rasgos, adulto, muscular, musculatura.
- **SRC_032_Anti_same-face_anti_same-body_para_10_modelos** | Dominio: face_forensics | Palabras: 4043 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: {MODEL_TOKEN}, modelos, dimensión, acción, cabello, cualquier, pairwise, umbral, codes, confusión.
- **SRC_033_Causalidad_edad-origen-psicolog_a-voz** | Dominio: face_forensics | Palabras: 1175 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: origen, fenotipo, modelos, rasgos, project_brand_entity, personalidad, psicología, idunex, comportamiento, apariencia.
- **SRC_038_PAIRWISE_UNIQUENESS_METRICS** | Dominio: face_forensics | Palabras: 12378 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: persona, personaje, puede, ejemplo, imagen, rasgos, bloque, texto, estilo, forma.
- **SRC_042_VIDEO_BIOMECHANICS_ACTING_CONTINUITY** | Dominio: face_forensics | Palabras: 6214 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: personaje, movimiento, video, continuidad, cámara, respiración, evitar, contenido, ejemplo, gestos.


#### Matriz runtime

### Grupo operativo: shape

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
| `wrong_face_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `same_face_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `generic_beauty_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `over_symmetry_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `makeup_face_drift_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lens_face_distortion_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `anchor_face_match_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `face_regression_test` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

#### Reglas invariantes
**Regla 01 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 02 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 03 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 04 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 05 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 06 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 07 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 08 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 09 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 10 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 11 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 12 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 13 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 14 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 15 — Rostro forense, landmarks, edad visual y autenticación de identidad**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

#### Casos operativos
#### Caso operativo 1: shape
**Entrada coloquial:** el usuario pide un output que afecta shape.  
**Acción del motor:** cargar Perfil360, filtrar campos `face_shape, cranial_visual_volume, vertical_thirds, horizontal_fifths, forehead_height`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 2: eyes
**Entrada coloquial:** el usuario pide un output que afecta eyes.  
**Acción del motor:** cargar Perfil360, filtrar campos `eye_shape, eye_size, eye_spacing, eye_tilt, eyelid_fold`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 3: brows_nose_mouth
**Entrada coloquial:** el usuario pide un output que afecta brows_nose_mouth.  
**Acción del motor:** cargar Perfil360, filtrar campos `brow_density, brow_arc, brow_height, brow_eye_distance, nose_bridge`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 4: auth
**Entrada coloquial:** el usuario pide un output que afecta auth.  
**Acción del motor:** cargar Perfil360, filtrar campos `wrong_face_blocker, same_face_blocker, generic_beauty_blocker, over_symmetry_blocker, makeup_face_drift_rule`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

## 3. Checklist PASS/FAIL del core
| Check | PASS | FAIL | Repair |
|---|---|---|---|

| cobertura de campos | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| interconexión con Perfil360 | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| source-to-runtime | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| prompt creativo limpio | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| sidecar técnico | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| QA fail codes | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| fallback fixes | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| vendor-safe | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| no imaginación | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |

| compatibilidad proyecto | evidencia explícita en archivo, perfil o manifest | declaración general sin operación | reconstruir sección, añadir campo, test y fallback |


## 4. Extractos operativos derivados de investigaciones


### Extractos transformados — Cámara, lente, iluminación, color, escena y física espacial


- **Regla derivada 001:** --- SOURCE: Dermatolog a visual realista ---
Piel humana realista en IA: Guía
integral visual y textual
La ﬁdelidad de la piel humana en la inteligencia artiﬁcial (IA) requiere
capturar y describir con detalle las características auténticas de la piel, ya sea
en fotografías y vídeos reales o en los prompts y anotaciones para modelos
generativos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 002:** Los microdetalles (poros, arrugas, vello, brillos naturales, etc.)
marcan la diferencia entre un resultado convincente y la temida piel
“plástica”.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 003:** En esta guía práctica exploramos cómo documentar visualmente
estos rasgos en sesiones de foto/vídeo realistas, y cómo describirlos
textualmente en prompts y metadatos de datasets, evitando estereotipos
étnicos y la falta de realismo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 004:** Se abordan también la inﬂuencia de edad,
iluminación, clima y equipos en la apariencia de la piel, técnicas para
prevenir la sobre-suavización no deseada, procedimientos de QA visual en
diversos contextos y estrategias de corrección cuando los resultados no son
los esperados.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 005:** Presentamos ejemplos de prompts y esquemas de metadatos
útiles para un pipeline end-to-end abarcando fotografía, vídeo, modelado
generativo y veriﬁcación de calidad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 006:** Atributos esenciales de la piel a documentar y
describir
Los rasgos clave de una piel humana realista son aquellos detalles que
hacen que luzca natural y creíble, y deben ser capturados en la fotografía o
vídeo real y también descritos en los prompts y metadatos si se entrena o
utiliza un modelo generativo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 007:** Variaciones en la piel por edad, iluminación,
clima, actividad y cámara
Además de las características intrínsecas de la piel, su apariencia varía según
múltiples factores externos e internos como la edad de la persona, el tipo e
intensidad de la luz, las condiciones ambientales y la actividad física reciente.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 008:** También inﬂuyen aspectos técnicos de la captura (calidad de cámara, lente,
resolución, etc.).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 009:** Comprender estas variaciones contextuales es fundamental
para documentar adecuadamente la piel y prever su representación
correcta en IA:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 010:** Edad de la persona (adultos jóvenes vs maduros): Con la edad, la piel
experimenta cambios notables.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 011:** Las pieles jóvenes (20-30 años) tienden a
tener una textura más tersa, mayor elasticidad y tono más uniforme, aunque
pueden presentar acné o poros más abiertos en pieles grasas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 012:** ej., >50 años) la piel pierde ﬁrmeza, se vuelve más ﬁna y
menos elástica, y suele presentar arrugas, pliegues marcados y manchas (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 013:** También aumenta la sequedad: alrededor
del 85% de las personas mayores sufren sequedad de “invierno” por pérdida de
glándulas sebáceas y baja humedad 7 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 014:** Por tanto, en la fotografía editorial, se
deben respetar las huellas de la edad (no eliminarlas por completo en
posproducción) para reﬂejar la madurez del sujeto.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 015:** Igualmente, en prompts
conviene especiﬁcar la edad aproximada o rango (“mujer de 45 años con
arrugas ﬁnas y manchas suaves”) para guiar al modelo a generar los signos de
edad correctos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 016:** Tipo e intensidad de la luz (iluminación): La iluminación inﬂuye
dramáticamente en la apariencia de la piel.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 017:** ej., sol
directo o ﬂash sin difusor) acentúa cada irregularidad creando sombras
marcadas en arrugas y poros 8 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 018:** Esto realza la textura pero puede exagerar
defectos (útil para estilos dramáticos o retratos con grit).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 019:** En cambio, la luz
suave (difusa, de ventana, de un softbox) envuelve la piel suavizando
arrugas y uniformando el tono 8 ; ideal para retratos de belleza o publicidad
donde se busca un look más ﬂaterring.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 020:** La dirección de la luz también
importa: luz lateral o cenital proyecta sombras en surcos y poros (dando
profundidad y realce de textura), mientras que luz frontal o muy baja reduce
sombras y puede aplanar la textura 8 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 021:** En IA, es crucial describir la fuente y
estilo de luz en los prompts para controlar cómo se mostrará la piel (ejemplos:
“iluminación de atardecer lateral (golden hour) acentuando la textura de la
piel” 2 vs.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 022:** Esto
constriñe la interpretación del modelo y puede marcar la diferencia entre
una piel detallada y otra plásticamente lisa 2 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 023:** Clima y ambiente: Las condiciones ambientales y el clima circundante
afectan tanto la ﬁsiología de la piel real como su aspecto en imágenes:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 024:** --- SOURCE: Cabello peinados y física capilar ---
Informe: Cómo deﬁnir cabello
humano realista para modelos de IA
en imagen, video y 3D
El cabello es uno de los elementos más desaﬁantes en la generación de
contenido visual realista con Inteligencia Artiﬁcial (IA).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 025:** Reproducirlo
ﬁelmente en imágenes 2D generadas por IA, en videos o en modelos 3D/
avatares exige entender sus propiedades físicas y estéticas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 026:** A continuación se
presenta una guía completa y operativa, organizada en siete apartados,
abarcando desde la estructura del cabello hasta la validación de resultados.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 027:** Está adaptada para todos los stacks (2D, video generativo, 3D) y considera
todas las diversidades capilares: cabello lacio, ondulado, rizado, afro
(también conocido como coily), con variaciones étnicas, y cómo afectan
factores como clima y humedad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 028:** También se incluyen ejemplos concretos,
recetas por escena y comparaciones en tablas para destacar diferencias entre
enfoques 2D, video y 3D, respaldado por fuentes autoritativas
(investigaciones académicas, documentos de la industria, manuales técnicos
oﬁciales).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 029:** Al ﬁnal, se presentan recomendaciones prácticas y un resumen
ejecutivo con los puntos esenciales.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 030:** Cada sección comienza con los aspectos
cruciales, seguidos de explicaciones detalladas para dar un contexto completo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 031:** Estructura del cabello: propiedades físicas y
visuales fundamentales
Resumen: Para deﬁnir un cabello realista en IA, primero necesitamos
comprender las características físicas del cabello humano real.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 032:** Las
propiedades clave incluyen tipo de cabello (forma del rizo o lacio), grosor y
diámetro de las hebras (ej.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 033:** su rango en micrómetros), densidad por área
(cantidad de cabellos por cm²), volumen visual, patrón de rizo (grado u forma
del rizado), raya o división y nacimiento del cabello (línea de
implantación), presencia de baby hairs (pelos ﬁnos en la frente o sienes),
frizz (encrespamiento), nivel de brillo (reﬂejos especulares y componente
difuso), aspecto de puntas (condición, puntas abiertas), daño (sequedad,
quiebre), ef. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 034:** Todos estos aspectos deberán ser
modelados o descritos en prompts/parametrizaciones para cada stack de IA.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 035:** Tipo y patrón de rizo: Los cabellos se clasiﬁcan según su textura y forma
predominantemente en cuatro grupos: lacio (recto), ondulado, rizado y afro
(coily).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 036:** Esta tipología, conocida como sistema 1A–4C, detalla subtipos por
grado de rizo: 1A–1C se reﬁere a lacio liso, 2A–2C a ondulado leve, 3A–3C a
rizado de bucles amplios a más apretados, y 4A–4C al cabello afro/ensortijado
de rizos muy apretados.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 037:** Un cabello lacio es casi completamente recto; su
sección transversal suele ser circular, lo que le da mayor rigidez y brillo
uniforme 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 038:** El cabello ondulado forma curvas en “S” suaves; rizado tiene
espirales más deﬁnidas, con secciones transversales ovaladas; y el afro o coily
presenta rizos sumamente apretados y una sección transversal plana o
elíptica 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 039:** Esta forma de la sección transversal inﬂuye en cómo el cabello se
curva: las hebras planas u ovaladas tienden a enroscarse más (como en
cabellos afros), mientras que las cilíndricas se alinean rectas 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 040:** Grosor de las hebras (diámetro): El diámetro de un cabello humano típico
varía entre ~17 y 181 micrones (0.017 a 0.181 mm) 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 041:** En promedio es de unos
~70 μm 1 , aunque el rango es amplio: los cabellos ﬁnos suelen medir ~15–50
μm (translúcidos, frágiles), los medianos de 50–90 μm (estándar común) y los
gruesos o “coarse” pueden superar 90 μm (alcanzando 120–150 μm en casos
extremos) 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 042:** ej., la
alopecia androgenética “miniaturiza” los folículos, reduciendo el diámetro de. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 043:** Variaciones étnicas: Los estudios muestran diferencias, con
el cabello asiático siendo el más grueso (muchos trazos de 80 a 120 μm,
superando el promedio global) 1 , caucásico con grosor intermedio
(típicamente 50–90 μm) 1 , y el cabello afro presentando la paradoja de verse
muy voluminoso por sus rizos cerrados, aunque sus hebras individuales
tienden a ser más ﬁnas que las asiáticas 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 044:** En cabelleras reales, el grosor
inﬂuye en la textura: pelos más gruesos son más rígidos y resistentes; los
ﬁnos, más ﬂexibles pero también más propensos a romperse 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 045:** Densidad y volumen: La densidad es la cantidad de cabellos por superﬁcie de
cuero cabelludo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 046:** Un adulto promedio tiene entre 100,000 y 150,000 cabellos
en unos 600 cm² de cuero cabelludo, es decir, entre ~100 y 150 cabellos/
cm² 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 047:** Menos de 100 cabellos/cm² se considera baja densidad (con el cuero
cabelludo visible en ciertas condiciones) 2 , mientras densidades mayores a 150
cabellos/cm² dan una melena muy tupida y de gran volumen 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 048:** La densidad y
el grosor conjuntamente determinan el volumen aparente: hebras gruesas
con baja densidad pueden lucir escasas, mientras hebras ﬁnas pero muy
numerosas se ven abundantes.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 049:** En contextos de IA, para imágenes 2D se puede
“imitar” mayor densidad describiendo el cabello como “espeso, con mucha
cantidad” o incidiendo en el volumen (“melena abundante”), mientras en
modelos 3D se logra generando suﬁcientes strands o hair cards para cubrir el
cuero cabelludo (evitando “huecos” por donde la piel asome).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 050:** Si el modelo 3D
permite simular densidades variables, puede calibrarse el número de hebras o
clumps por superﬁcie para diferentes densidades: por ejemplo, ~120 hebras
guía por cm² para densidad media, y quizás >150/cm² para una super
melena 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 051:** Raya y nacimiento (hairline) y baby hairs: La raya en el cabello es la línea
donde el cabello se divide (central, lateral, en zigzag, etc.), inﬂuyendo en la
distribución y caída del pelo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 052:** El nacimiento del
cabello (línea de implantación o hairline) determina la forma en que el pelo
enmarca el rostro: puede ser recto, con entradas, pico de viuda, etc., y es
fundamental para realismo en retratos de IA.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 053:** Por ejemplo, las entradas
(retrocesos en las sienes) son comunes especialmente en hombres y su
ausencia puede volver un modelo facial inverosímil.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 054:** Detalles como pequeños
cabellos (baby hairs) en la frente o sienes aportan realismo, por lo cual los
grooms 3D suelen incluir primitivas para estos pelitos, y en prompts conviene. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 055:** mencionarlos explícitamente (“con pequeños mechones sueltos alrededor de la
frente”).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 056:** Cuidado con la simetría excesiva: En la naturaleza el cabello no es
perfectamente simétrico; para evitar apariencia plástica o de “peluca”, es
aconsejable introducir ligeras variaciones y asimetrías en la raya y contorno
capilar.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 057:** En 3D, los diseñadores suelen romper la simetría deliberadamente en
los grooms, añadiendo baby hairs y mechones no simétricos 3 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 058:** Brillo y textura superﬁcial: El pelo real reﬂeja la luz de forma característica.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 059:** Existen componentes especulares (reﬂejos brillantes a lo largo de las hebras)
y un componente difuso (la luz dispersa suavemente).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 060:** El cabello totalmente
opaco y sin reﬂejos se ve mate o “muerto”, mientras que un brillo excesivo y
uniforme genera el efecto plástico o de muñeca.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen. [TECHNICAL_LEGACY_TERM_NOT_CREATIVE_RUNTIME]

- **Regla derivada 061:** Para un brillo realista, el
modelo debe simular la reﬂectancia anisotrópica de las ﬁbras capilares: por
ejemplo, usando shaders especializados como Kajiya-Kay (1989) o Marschner
(2003), que reproducen reﬂejos duales (un highlight principal y un glint
secundario en la melena) 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 062:** Si esto es muy técnico para un proyecto, se puede
imitar descriptivamente: en prompts de Stable Diﬀusion y similares, se logra
con frases como “cabello brillante y sedoso, reﬂejos sutiles bajo la luz, con brillo
natural”.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 063:** Para modelos 3D, se ajustan parámetros del material capilar: por
ejemplo, en Blender puede usarse el shader Principled Hair de Cycles con un
valor apropiado de melanina (parámetro que controla tanto el color natural –
pigmento– como la cantidad de brillo y transparencia de cada hebra) 3 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 064:** Un
truco práctico es combinar brillos heterogéneos: algunas hebras más opacas
que otras, y añadir microvariaciones en rugosidad, para evitar una reﬂexión
de luz “de casco”.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 065:** Frizz y puntas (acabado de hebras): El frizz es el encrespamiento o esos
mechones rebeldes que se alejan de la masa principal del cabello (cabellos
sueltos).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 066:** Un cabello completamente “peinado” sin ningún frizz suele parecer
artiﬁcial; conviene incluir algo de frizz (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 067:** ej., “con algunos pelitos sueltos
para un aspecto natural”) o en 3D usar parámetros de clumping y randomness
para que un porcentaje de hebras se separe ligeramente de los mechones
principales (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 068:** ej., en XGen se puede usar el parámetro Noise para esa
irregularidad controlada).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 069:** Las puntas del cabello real casi nunca son
perfectamente uniformes: pueden estar aﬁnadas o abiertas en casos de
cabello dañado.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 070:** Para replicar esto, en 3D se modula el grosor de la hebra de
raíz a punta (taper progresivo) y se puede dar color ligeramente más claro/
opaco a las puntas para simular resequedad o decoloración.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 071:** similar, en un prompt se pueden agregar detalles como “puntas ligeramente
más claras” o “ligeramente abiertas” para sugerir ese acabado realista.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 072:** Humedad y estática: El cabello es higroscópico; en ambientes húmedos
absorbe agua, aumentando su diámetro y relajando los enlaces de hidrógeno
en la queratina.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 073:** En cambio, en ambientes secos (especialmente con aire frío y seco)
puede cargarse de electricidad estática, haciendo que algunos pelos se
separen y se ericen.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 074:** Al modelar, se debe considerar la humedad como
parámetro: cabellos en escenas lluviosas o húmedas estarán más pesados y
apelmazados, con menos volúmen y más rizos ﬂojos o encrespados; en
entornos áridos podrían aparecer hebras sueltas por estática.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 075:** Visualmente, el
cabello mojado pierde volumen y se agrupa en mechones más gruesos (por la
tensión superﬁcial del agua), con un brillo especular más intenso pero difuso.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 076:** En un prompt, se puede indicar “cabello mojado, agrupado por el agua, con
mechones pegados a la frente” para generar este look; en 3D, la simulación de
cabello mojado puede lograrse aumentando la masa efectiva de las hebras y
disminuyendo su stiﬀness, además de aplicar un shader con reﬂejos más
intensos para simular la película de agua.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 077:** Color, canas y tintes: El color del cabello (natural o teñido) inﬂuye en su
aspecto.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 078:** Los cabellos oscuros tienen más melanina y tienden a absorber más
luz (menor brillo visible), mientras los rubios tienen menos pigmento y
maniﬁestan highlight más evidentes.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 079:** Además, el número total de cabellos varía
por color natural: personas rubias suelen tener hasta ~150 mil cabellos,
mientras las pelirrojas promedian unos 90 mil 5 , como muestra la gráﬁca a
continuación.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 080:** Este es un factor evolutivo: colores más claros compensan su
menor grosor con mayor densidad, y viceversa 5 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

### Extractos transformados — Piel, dermatología visual, cabello y materialidad humana


- **Regla derivada 001:** --- SOURCE: Dermatolog a visual realista ---
Piel humana realista en IA: Guía
integral visual y textual
La ﬁdelidad de la piel humana en la inteligencia artiﬁcial (IA) requiere
capturar y describir con detalle las características auténticas de la piel, ya sea
en fotografías y vídeos reales o en los prompts y anotaciones para modelos
generativos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 002:** Los microdetalles (poros, arrugas, vello, brillos naturales, etc.)
marcan la diferencia entre un resultado convincente y la temida piel
“plástica”.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 003:** En esta guía práctica exploramos cómo documentar visualmente
estos rasgos en sesiones de foto/vídeo realistas, y cómo describirlos
textualmente en prompts y metadatos de datasets, evitando estereotipos
étnicos y la falta de realismo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 004:** Se abordan también la inﬂuencia de edad,
iluminación, clima y equipos en la apariencia de la piel, técnicas para
prevenir la sobre-suavización no deseada, procedimientos de QA visual en
diversos contextos y estrategias de corrección cuando los resultados no son
los esperados.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 005:** Presentamos ejemplos de prompts y esquemas de metadatos
útiles para un pipeline end-to-end abarcando fotografía, vídeo, modelado
generativo y veriﬁcación de calidad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 006:** Atributos esenciales de la piel a documentar y
describir
Los rasgos clave de una piel humana realista son aquellos detalles que
hacen que luzca natural y creíble, y deben ser capturados en la fotografía o
vídeo real y también descritos en los prompts y metadatos si se entrena o
utiliza un modelo generativo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 007:** Variaciones en la piel por edad, iluminación,
clima, actividad y cámara
Además de las características intrínsecas de la piel, su apariencia varía según
múltiples factores externos e internos como la edad de la persona, el tipo e
intensidad de la luz, las condiciones ambientales y la actividad física reciente.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 008:** También inﬂuyen aspectos técnicos de la captura (calidad de cámara, lente,
resolución, etc.).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 009:** Comprender estas variaciones contextuales es fundamental
para documentar adecuadamente la piel y prever su representación
correcta en IA:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 010:** Edad de la persona (adultos jóvenes vs maduros): Con la edad, la piel
experimenta cambios notables.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 011:** Las pieles jóvenes (20-30 años) tienden a
tener una textura más tersa, mayor elasticidad y tono más uniforme, aunque
pueden presentar acné o poros más abiertos en pieles grasas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 012:** ej., >50 años) la piel pierde ﬁrmeza, se vuelve más ﬁna y
menos elástica, y suele presentar arrugas, pliegues marcados y manchas (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 013:** También aumenta la sequedad: alrededor
del 85% de las personas mayores sufren sequedad de “invierno” por pérdida de
glándulas sebáceas y baja humedad 7 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 014:** Por tanto, en la fotografía editorial, se
deben respetar las huellas de la edad (no eliminarlas por completo en
posproducción) para reﬂejar la madurez del sujeto.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 015:** Igualmente, en prompts
conviene especiﬁcar la edad aproximada o rango (“mujer de 45 años con
arrugas ﬁnas y manchas suaves”) para guiar al modelo a generar los signos de
edad correctos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 016:** Tipo e intensidad de la luz (iluminación): La iluminación inﬂuye
dramáticamente en la apariencia de la piel.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 017:** ej., sol
directo o ﬂash sin difusor) acentúa cada irregularidad creando sombras
marcadas en arrugas y poros 8 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 018:** Esto realza la textura pero puede exagerar
defectos (útil para estilos dramáticos o retratos con grit).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 019:** En cambio, la luz
suave (difusa, de ventana, de un softbox) envuelve la piel suavizando
arrugas y uniformando el tono 8 ; ideal para retratos de belleza o publicidad
donde se busca un look más ﬂaterring.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 020:** La dirección de la luz también
importa: luz lateral o cenital proyecta sombras en surcos y poros (dando
profundidad y realce de textura), mientras que luz frontal o muy baja reduce
sombras y puede aplanar la textura 8 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 021:** En IA, es crucial describir la fuente y
estilo de luz en los prompts para controlar cómo se mostrará la piel (ejemplos:
“iluminación de atardecer lateral (golden hour) acentuando la textura de la
piel” 2 vs.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 022:** Esto
constriñe la interpretación del modelo y puede marcar la diferencia entre
una piel detallada y otra plásticamente lisa 2 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 023:** Clima y ambiente: Las condiciones ambientales y el clima circundante
afectan tanto la ﬁsiología de la piel real como su aspecto en imágenes:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 024:** --- SOURCE: Cabello peinados y física capilar ---
Informe: Cómo deﬁnir cabello
humano realista para modelos de IA
en imagen, video y 3D
El cabello es uno de los elementos más desaﬁantes en la generación de
contenido visual realista con Inteligencia Artiﬁcial (IA).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 025:** Reproducirlo
ﬁelmente en imágenes 2D generadas por IA, en videos o en modelos 3D/
avatares exige entender sus propiedades físicas y estéticas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 026:** A continuación se
presenta una guía completa y operativa, organizada en siete apartados,
abarcando desde la estructura del cabello hasta la validación de resultados.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 027:** Está adaptada para todos los stacks (2D, video generativo, 3D) y considera
todas las diversidades capilares: cabello lacio, ondulado, rizado, afro
(también conocido como coily), con variaciones étnicas, y cómo afectan
factores como clima y humedad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 028:** También se incluyen ejemplos concretos,
recetas por escena y comparaciones en tablas para destacar diferencias entre
enfoques 2D, video y 3D, respaldado por fuentes autoritativas
(investigaciones académicas, documentos de la industria, manuales técnicos
oﬁciales).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 029:** Al ﬁnal, se presentan recomendaciones prácticas y un resumen
ejecutivo con los puntos esenciales.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 030:** Cada sección comienza con los aspectos
cruciales, seguidos de explicaciones detalladas para dar un contexto completo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 031:** Estructura del cabello: propiedades físicas y
visuales fundamentales
Resumen: Para deﬁnir un cabello realista en IA, primero necesitamos
comprender las características físicas del cabello humano real.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 032:** Las
propiedades clave incluyen tipo de cabello (forma del rizo o lacio), grosor y
diámetro de las hebras (ej.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 033:** su rango en micrómetros), densidad por área
(cantidad de cabellos por cm²), volumen visual, patrón de rizo (grado u forma
del rizado), raya o división y nacimiento del cabello (línea de
implantación), presencia de baby hairs (pelos ﬁnos en la frente o sienes),
frizz (encrespamiento), nivel de brillo (reﬂejos especulares y componente
difuso), aspecto de puntas (condición, puntas abiertas), daño (sequedad,
quiebre), ef. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 034:** Todos estos aspectos deberán ser
modelados o descritos en prompts/parametrizaciones para cada stack de IA.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 035:** Tipo y patrón de rizo: Los cabellos se clasiﬁcan según su textura y forma
predominantemente en cuatro grupos: lacio (recto), ondulado, rizado y afro
(coily).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 036:** Esta tipología, conocida como sistema 1A–4C, detalla subtipos por
grado de rizo: 1A–1C se reﬁere a lacio liso, 2A–2C a ondulado leve, 3A–3C a
rizado de bucles amplios a más apretados, y 4A–4C al cabello afro/ensortijado
de rizos muy apretados.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 037:** Un cabello lacio es casi completamente recto; su
sección transversal suele ser circular, lo que le da mayor rigidez y brillo
uniforme 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 038:** El cabello ondulado forma curvas en “S” suaves; rizado tiene
espirales más deﬁnidas, con secciones transversales ovaladas; y el afro o coily
presenta rizos sumamente apretados y una sección transversal plana o
elíptica 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 039:** Esta forma de la sección transversal inﬂuye en cómo el cabello se
curva: las hebras planas u ovaladas tienden a enroscarse más (como en
cabellos afros), mientras que las cilíndricas se alinean rectas 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 040:** Grosor de las hebras (diámetro): El diámetro de un cabello humano típico
varía entre ~17 y 181 micrones (0.017 a 0.181 mm) 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 041:** En promedio es de unos
~70 μm 1 , aunque el rango es amplio: los cabellos ﬁnos suelen medir ~15–50
μm (translúcidos, frágiles), los medianos de 50–90 μm (estándar común) y los
gruesos o “coarse” pueden superar 90 μm (alcanzando 120–150 μm en casos
extremos) 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 042:** ej., la
alopecia androgenética “miniaturiza” los folículos, reduciendo el diámetro de. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 043:** Variaciones étnicas: Los estudios muestran diferencias, con
el cabello asiático siendo el más grueso (muchos trazos de 80 a 120 μm,
superando el promedio global) 1 , caucásico con grosor intermedio
(típicamente 50–90 μm) 1 , y el cabello afro presentando la paradoja de verse
muy voluminoso por sus rizos cerrados, aunque sus hebras individuales
tienden a ser más ﬁnas que las asiáticas 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 044:** En cabelleras reales, el grosor
inﬂuye en la textura: pelos más gruesos son más rígidos y resistentes; los
ﬁnos, más ﬂexibles pero también más propensos a romperse 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 045:** Densidad y volumen: La densidad es la cantidad de cabellos por superﬁcie de
cuero cabelludo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 046:** Un adulto promedio tiene entre 100,000 y 150,000 cabellos
en unos 600 cm² de cuero cabelludo, es decir, entre ~100 y 150 cabellos/
cm² 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 047:** Menos de 100 cabellos/cm² se considera baja densidad (con el cuero
cabelludo visible en ciertas condiciones) 2 , mientras densidades mayores a 150
cabellos/cm² dan una melena muy tupida y de gran volumen 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 048:** La densidad y
el grosor conjuntamente determinan el volumen aparente: hebras gruesas
con baja densidad pueden lucir escasas, mientras hebras ﬁnas pero muy
numerosas se ven abundantes.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 049:** En contextos de IA, para imágenes 2D se puede
“imitar” mayor densidad describiendo el cabello como “espeso, con mucha
cantidad” o incidiendo en el volumen (“melena abundante”), mientras en
modelos 3D se logra generando suﬁcientes strands o hair cards para cubrir el
cuero cabelludo (evitando “huecos” por donde la piel asome).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 050:** Si el modelo 3D
permite simular densidades variables, puede calibrarse el número de hebras o
clumps por superﬁcie para diferentes densidades: por ejemplo, ~120 hebras
guía por cm² para densidad media, y quizás >150/cm² para una super
melena 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 051:** Raya y nacimiento (hairline) y baby hairs: La raya en el cabello es la línea
donde el cabello se divide (central, lateral, en zigzag, etc.), inﬂuyendo en la
distribución y caída del pelo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 052:** El nacimiento del
cabello (línea de implantación o hairline) determina la forma en que el pelo
enmarca el rostro: puede ser recto, con entradas, pico de viuda, etc., y es
fundamental para realismo en retratos de IA.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 053:** Por ejemplo, las entradas
(retrocesos en las sienes) son comunes especialmente en hombres y su
ausencia puede volver un modelo facial inverosímil.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 054:** Detalles como pequeños
cabellos (baby hairs) en la frente o sienes aportan realismo, por lo cual los
grooms 3D suelen incluir primitivas para estos pelitos, y en prompts conviene. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 055:** mencionarlos explícitamente (“con pequeños mechones sueltos alrededor de la
frente”).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 056:** Cuidado con la simetría excesiva: En la naturaleza el cabello no es
perfectamente simétrico; para evitar apariencia plástica o de “peluca”, es
aconsejable introducir ligeras variaciones y asimetrías en la raya y contorno
capilar.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 057:** En 3D, los diseñadores suelen romper la simetría deliberadamente en
los grooms, añadiendo baby hairs y mechones no simétricos 3 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 058:** Brillo y textura superﬁcial: El pelo real reﬂeja la luz de forma característica.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 059:** Existen componentes especulares (reﬂejos brillantes a lo largo de las hebras)
y un componente difuso (la luz dispersa suavemente).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 060:** El cabello totalmente
opaco y sin reﬂejos se ve mate o “muerto”, mientras que un brillo excesivo y
uniforme genera el efecto plástico o de muñeca.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen. [TECHNICAL_LEGACY_TERM_NOT_CREATIVE_RUNTIME]

- **Regla derivada 061:** Para un brillo realista, el
modelo debe simular la reﬂectancia anisotrópica de las ﬁbras capilares: por
ejemplo, usando shaders especializados como Kajiya-Kay (1989) o Marschner
(2003), que reproducen reﬂejos duales (un highlight principal y un glint
secundario en la melena) 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 062:** Si esto es muy técnico para un proyecto, se puede
imitar descriptivamente: en prompts de Stable Diﬀusion y similares, se logra
con frases como “cabello brillante y sedoso, reﬂejos sutiles bajo la luz, con brillo
natural”.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 063:** Para modelos 3D, se ajustan parámetros del material capilar: por
ejemplo, en Blender puede usarse el shader Principled Hair de Cycles con un
valor apropiado de melanina (parámetro que controla tanto el color natural –
pigmento– como la cantidad de brillo y transparencia de cada hebra) 3 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 064:** Un
truco práctico es combinar brillos heterogéneos: algunas hebras más opacas
que otras, y añadir microvariaciones en rugosidad, para evitar una reﬂexión
de luz “de casco”.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 065:** Frizz y puntas (acabado de hebras): El frizz es el encrespamiento o esos
mechones rebeldes que se alejan de la masa principal del cabello (cabellos
sueltos).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 066:** Un cabello completamente “peinado” sin ningún frizz suele parecer
artiﬁcial; conviene incluir algo de frizz (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 067:** ej., “con algunos pelitos sueltos
para un aspecto natural”) o en 3D usar parámetros de clumping y randomness
para que un porcentaje de hebras se separe ligeramente de los mechones
principales (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 068:** ej., en XGen se puede usar el parámetro Noise para esa
irregularidad controlada).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 069:** Las puntas del cabello real casi nunca son
perfectamente uniformes: pueden estar aﬁnadas o abiertas en casos de
cabello dañado.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 070:** Para replicar esto, en 3D se modula el grosor de la hebra de
raíz a punta (taper progresivo) y se puede dar color ligeramente más claro/
opaco a las puntas para simular resequedad o decoloración.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 071:** similar, en un prompt se pueden agregar detalles como “puntas ligeramente
más claras” o “ligeramente abiertas” para sugerir ese acabado realista.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 072:** Humedad y estática: El cabello es higroscópico; en ambientes húmedos
absorbe agua, aumentando su diámetro y relajando los enlaces de hidrógeno
en la queratina.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 073:** En cambio, en ambientes secos (especialmente con aire frío y seco)
puede cargarse de electricidad estática, haciendo que algunos pelos se
separen y se ericen.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 074:** Al modelar, se debe considerar la humedad como
parámetro: cabellos en escenas lluviosas o húmedas estarán más pesados y
apelmazados, con menos volúmen y más rizos ﬂojos o encrespados; en
entornos áridos podrían aparecer hebras sueltas por estática.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 075:** Visualmente, el
cabello mojado pierde volumen y se agrupa en mechones más gruesos (por la
tensión superﬁcial del agua), con un brillo especular más intenso pero difuso.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 076:** En un prompt, se puede indicar “cabello mojado, agrupado por el agua, con
mechones pegados a la frente” para generar este look; en 3D, la simulación de
cabello mojado puede lograrse aumentando la masa efectiva de las hebras y
disminuyendo su stiﬀness, además de aplicar un shader con reﬂejos más
intensos para simular la película de agua.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 077:** Color, canas y tintes: El color del cabello (natural o teñido) inﬂuye en su
aspecto.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 078:** Los cabellos oscuros tienen más melanina y tienden a absorber más
luz (menor brillo visible), mientras los rubios tienen menos pigmento y
maniﬁestan highlight más evidentes.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 079:** Además, el número total de cabellos varía
por color natural: personas rubias suelen tener hasta ~150 mil cabellos,
mientras las pelirrojas promedian unos 90 mil 5 , como muestra la gráﬁca a
continuación.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 080:** Este es un factor evolutivo: colores más claros compensan su
menor grosor con mayor densidad, y viceversa 5 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

### Extractos transformados — Rostro forense, landmarks, edad visual y autenticación de identidad


- **Regla derivada 001:** --- SOURCE: Biometría facial forense ---
Documentación forense del rostro
humano para IA consistente (caso de
modelo ﬁcticio project-declared)
La identiﬁcación precisa de un rostro humano es un desafío
multidisciplinar, combinando la antropometría forense (medición objetiva de
rasgos), las técnicas de producción audiovisual/CG para capturar detalles
realistas, y los principios de identidad sintética para mantener rasgos
const. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 002:** Lograr consistencia cross-model – que el mismo
rostro sintético se reproduzca sin cambios a pesar de generarse con diferentes
sistemas – requiere una descripción exhaustiva y normalizada del rostro, así
como métodos de control para evitar embellecimientos o mezclas no
deseadas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 003:** La identiﬁcación facial forense se             En la creación de rostros digitales,. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 004:** permanecen estables tras la                    aumenta la credibilidad y conﬁanza.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 005:** Proporciones craneofaciales y análisis
detallado del rostro
Deﬁnir el rostro con precisión forense comienza con una descripción de las
proporciones craneofaciales y la forma global de la cabeza y la cara.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 006:** Esto
abarca las dimensiones absolutas y relativas de cada zona, desde la frente hasta
la mandíbula.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 007:** De la antropometría forense clásica se heredan puntos
cefalométricos y medidas clave que permiten cuantiﬁcar la conﬁguración
facial de una persona.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 008:** En rostros adultos (post-adolescencia), la estructura
ósea se mantiene estable, ofreciendo una base conﬁable de medidas únicas
para cada individuo 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 009:** A continuación, se detallan los principales componentes del rostro y sus
características medibles:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 010:** Además de estos rasgos principales, una descripción forense completa del
rostro debe considerar particularidades adicionales:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 011:** Herramienta: A efectos de precisión cuantitativa, se pueden emplear
sistemas de referencia en las fotografías de entrenamient. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 012:** --- SOURCE: Religi n espiritualidad y cosmovisi n ---
Informe: Documentación de
Religión, Espiritualidad y
Cosmovisión en Modelos de IA
Sintéticos Adultos (IDUNEX). **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 013:** Resumen Ejecutivo
La documentación y gestión de la religión, la espiritualidad y la
cosmovisión en los modelos de IA sintéticos adultos constituye un desafío
que abarca elementos culturales, éticos y técnicos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 014:** A continuación, resumimos
las principales conclusiones y recomendaciones que guían la integración
respetuosa de estas dimensiones en los perﬁles 360° de personas digitales en el
contexto de IDUNEX (plataforma de PROJECT_BRAND_ENTITY):. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 015:** Resumen: La clave es construir perﬁles de personas digitales con múltiples
capas que abarquen la fe y la cultura de forma detallada y matizada,
integrándolo en la plataforma IDUNEX 6 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 016:** La gobernanza se maniﬁesta en la
existencia de campos especiales, reglas de edición (locks), políticas de
seguridad, procesos de QA y transparencia en la evolución del perﬁl, para
asegurar una representación respetuosa, conﬁable e inmersiva de la
cosmovisión del individuo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 017:** En las próximas secciones, se exploran más a fondo
estos temas, con deﬁniciones, recomendaciones prácticas y ejemplos
concretos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 018:** Dimensiones de la Religión, la Espiritualidad y
la Cosmovisión: Diferencias y Documentación
La cosmovisión de un individuo se compone de varios componentes que
deben distinguirse y documentarse por separado para evitar
simpliﬁcaciones.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 019:** Un error común es reducir una persona a su etiqueta
religiosa, omitiendo matices.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 020:** --- SOURCE: Microexpresiones y FACS ---
Guía técnica: Microexpresiones, FACS
y lenguaje facial en IA para imagen y
vídeo
Las microexpresiones son sutiles expresiones faciales, breves e involuntarias,
que reﬂejan emociones auténticas antes de que sean conscientes o
controladas 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 021:** El Facial Action Coding System (FACS) es el estándar para
descomponer cualquier expresión facial en unidades de acción (AUs),
asociadas a contracciones de músculos especíﬁcos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 022:** Mediante FACS es posible
representar de forma objetiva las acciones faciales relevantes (desde el
movimiento de las cejas hasta la caída de la mandíbula) y vincularlas a
emociones.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 023:** Esto ha permitido a la IA tanto analizar emociones en vídeo como
sintetizar expresiones en rostros generados o animados.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

## H71-H80 SAFE_APPAREL_WATERMARK_AGENT10N
H71_H80_AGENT10N=SAFE_APPAREL_TAXONOMY; ADULT_REVEALING_APPAREL_NOT_NUDITY; VENDOR_PROMPT_SANITIZATION_SAFE_APPAREL; WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED; ALLOW adult editorial beachwear/swimwear/intimate apparel/catalog/corset/body/performance wardrobe when covered non-explicit; BLOCK nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded or school-coded sexualization and real-person copying.
ALLOW_ADULT_EDITORIAL: moda de playa, traje de bano, ropa de bano, bikini editorial, swimwear campaign, beachwear, resortwear, moda intima editorial/catalog, ropa interior de catalogo, corset/body/bodysuit, vestuario de show adulto, vestuario de videoclip adulto y outfit de performance adulta cuando el modelo es adulto, cubierto y no explicito.
CONDITIONAL_REWRITE: convertir styling glam/provocativo, boudoir editorial, fantasia adulta y vestuario de alto impacto a lenguaje adulto, editorial, comercial, non-explicit, covered intimate areas.
BLOCK_ALWAYS: nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded styling, school-coded sexualization, real-person copying y cualquier intento de saltar locks de edad o identidad.
WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED.
