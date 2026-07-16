# Acting, pose, FACS, caminada, biomecánica y video

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.



## 1. Mandato de cobertura 10/10
Este core es obligatorio para cualquier proyecto IDUNEX. No funciona como resumen; define reglas de decisión, campos, matrices, QA, fallbacks y relación con agent-load. Debe operar en creación, actualización, diagnóstico, prompt, sidecar y auditoría.


## 2. Dominios conectados


### Acting, FACS, microgestos, pose, caminada y continuidad de video
Gobierna actuación, subtexto, gesto, respiración, peso, caminata, danza, continuidad frame-to-frame y repair de video.

**Fuentes aterrizadas:**
- **SRC_003_Antropometr_a_corporal_avanzada** | Dominio: body_age_anthropometry | Palabras: 4644 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: corporal, grasa, mujeres, hombros, muscular, ejemplo, altura, hombres, estatura, cuerpo.
- **SRC_016_Lencer_abodywear_editorial_adulto_no_expl_cito** | Dominio: body_age_anthropometry | Palabras: 1429 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: lencería, modelos, explícito, ejemplo, encaje, contenido, prenda, editorial, cualquier, poses.
- **SRC_019_Motion_bible_y_caminada** | Dominio: body_age_anthropometry | Palabras: 6732 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: movimiento, marcha, movimientos, pasos, puede, vídeo, ejemplo, hacia, cuerpo, brazos.
- **SRC_020_Acting_bible** | Dominio: body_age_anthropometry | Palabras: 7223 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: actuación, personaje, avatar, plano, mirada, escena, emoción, ejemplo, gestos, emociones.
- **SRC_034_Wardrobe_premium_por_modelo_y_cuerpo** | Dominio: body_age_anthropometry | Palabras: 7399 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: imagen, cuerpo, arrugas, prenda, contenido, poses, vestuario, ejemplo, calidad, evitar.
- **SRC_035_Acting_poses_y_microgestos_por_personalidad** | Dominio: body_age_anthropometry | Palabras: 12962 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: poses, gestos, mirada, sonrisa, manos, personalidad, corporal, guías, puede, creativas.
- **SRC_039_BODY_BEAUTY_FITNESS_EDITORIAL_NON_EXPLICIT** | Dominio: body_age_anthropometry | Palabras: 6577 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: persona, sección, personaje, idunex, texto, imagen, generación, estilo, modelos, personas.


#### Matriz runtime

### Grupo operativo: face_acting

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
| `rigid_pose_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fake_expression_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `morphing_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `video_identity_jump_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hands_warp_video_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `emotion_mismatch_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `motion_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `video_regression_test` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

#### Reglas invariantes
**Regla 01 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 02 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 03 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 04 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 05 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 06 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 07 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 08 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 09 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 10 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 11 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 12 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 13 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 14 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 15 — Acting, FACS, microgestos, pose, caminada y continuidad de video**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

#### Casos operativos
#### Caso operativo 1: face_acting
**Entrada coloquial:** el usuario pide un output que afecta face_acting.  
**Acción del motor:** cargar Perfil360, filtrar campos `facs_base, smile_types, microgesture_set, eye_emotion_map, brow_micro_movement`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 2: body_motion
**Entrada coloquial:** el usuario pide un output que afecta body_motion.  
**Acción del motor:** cargar Perfil360, filtrar campos `walking_rhythm, walking_weight, hip_movement, shoulder_countermotion, arm_swing`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 3: video
**Entrada coloquial:** el usuario pide un output que afecta video.  
**Acción del motor:** cargar Perfil360, filtrar campos `video_continuity_lock, frame_to_frame_identity, shot_transition_rule, motion_blur_rule, hair_motion_continuity`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 4: qa
**Entrada coloquial:** el usuario pide un output que afecta qa.  
**Acción del motor:** cargar Perfil360, filtrar campos `rigid_pose_blocker, fake_expression_blocker, morphing_blocker, video_identity_jump_blocker, hands_warp_video_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

### Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal
Define cuerpo adulto, proporción, postura, manos, pies, edad corporal, balance y movimiento coherente. Bloquea same-body, infantilización, exageración y pose imposible.

**Fuentes aterrizadas:**
- **SRC_003_Antropometr_a_corporal_avanzada** | Dominio: body_age_anthropometry | Palabras: 4644 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: corporal, grasa, mujeres, hombros, muscular, ejemplo, altura, hombres, estatura, cuerpo.
- **SRC_016_Lencer_abodywear_editorial_adulto_no_expl_cito** | Dominio: body_age_anthropometry | Palabras: 1429 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: lencería, modelos, explícito, ejemplo, encaje, contenido, prenda, editorial, cualquier, poses.
- **SRC_019_Motion_bible_y_caminada** | Dominio: body_age_anthropometry | Palabras: 6732 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: movimiento, marcha, movimientos, pasos, puede, vídeo, ejemplo, hacia, cuerpo, brazos.
- **SRC_020_Acting_bible** | Dominio: body_age_anthropometry | Palabras: 7223 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: actuación, personaje, avatar, plano, mirada, escena, emoción, ejemplo, gestos, emociones.
- **SRC_034_Wardrobe_premium_por_modelo_y_cuerpo** | Dominio: body_age_anthropometry | Palabras: 7399 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: imagen, cuerpo, arrugas, prenda, contenido, poses, vestuario, ejemplo, calidad, evitar.
- **SRC_035_Acting_poses_y_microgestos_por_personalidad** | Dominio: body_age_anthropometry | Palabras: 12962 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: poses, gestos, mirada, sonrisa, manos, personalidad, corporal, guías, puede, creativas.
- **SRC_039_BODY_BEAUTY_FITNESS_EDITORIAL_NON_EXPLICIT** | Dominio: body_age_anthropometry | Palabras: 6577 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: persona, sección, personaje, idunex, texto, imagen, generación, estilo, modelos, personas.


#### Matriz runtime

### Grupo operativo: structure

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
| `same_body_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wrong_age_body_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `impossible_pose_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `body_lens_distortion_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `proportion_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hands_feet_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `adult_body_safety_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

#### Reglas invariantes
**Regla 01 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 02 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 03 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 04 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 05 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 06 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 07 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 08 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 09 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 10 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 11 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 12 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 13 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 14 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 15 — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

#### Casos operativos
#### Caso operativo 1: structure
**Entrada coloquial:** el usuario pide un output que afecta structure.  
**Acción del motor:** cargar Perfil360, filtrar campos `height_range, body_build, visual_mass, shoulder_width, neck_length`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 2: hands_feet
**Entrada coloquial:** el usuario pide un output que afecta hands_feet.  
**Acción del motor:** cargar Perfil360, filtrar campos `hand_shape, finger_length, finger_taper, knuckle_visibility, nail_style`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 3: posture
**Entrada coloquial:** el usuario pide un output que afecta posture.  
**Acción del motor:** cargar Perfil360, filtrar campos `center_of_gravity, posture_base, spine_curve, shoulder_behavior, hip_alignment`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 4: qa
**Entrada coloquial:** el usuario pide un output que afecta qa.  
**Acción del motor:** cargar Perfil360, filtrar campos `same_body_blocker, wrong_age_body_blocker, impossible_pose_blocker, body_lens_distortion_rule, proportion_repair_rule`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

### Voz hablada, lenguaje, acento, escritura, canto y música
Crea identidad vocal y textual propia: timbre, prosodia, edad vocal, acento controlado, voz escrita, Suno y no imitación.

**Fuentes aterrizadas:**
- **SRC_007_Biograf_a_familiar_y_migratoria** | Dominio: phenotype_culture_safe | Palabras: 5710 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: ejemplo, personaje, elena, familia, estilo, puede, actual, forma, universidad, personalidad.
- **SRC_008_Moral_valores_y_tica_personal** | Dominio: phenotype_culture_safe | Palabras: 7838 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: moral, agente, matriz, ejemplo, valores, virtudes, podría, puede, límites, contexto.
- **SRC_012_Lenguaje_acento_y_voz_escrita** | Dominio: phenotype_culture_safe | Palabras: 7758 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: humor, muletillas, ejemplo, project-declared, español, formal, registro, frases, casual, vocabulario.
- **SRC_022_Voz_hablada_para_ElevenLabs** | Dominio: language_voice_text | Palabras: 7641 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: ejemplo, elevenlabs, puede, entonación, acento, pausas, español, voces, parámetros, sintética.
- **SRC_023_Voz_cantada_y_Suno** | Dominio: language_voice_text | Palabras: 7630 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: estilo, ejemplo, letra, idunex, canciones, género, puede, vocal, canción, timbre.
- **SRC_026_Gobernanza_legal_Per_PROJECT_BRAND_ENTITY** | Dominio: phenotype_culture_safe | Palabras: 7241 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: datos, contenido, project_brand_entity, legal, derechos, imagen, entrenamiento, ejemplo, modelos, personales.
- **SRC_028_Optimizaci_n_ChatGPT_JSONTXT** | Dominio: language_voice_text | Palabras: 6733 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: archivos, conocimiento, agente, instrucciones, ejemplo, información, puede, contenido, respuesta, contexto.
- **SRC_036_Identidad_musical_Suno_por_modelo** | Dominio: phenotype_culture_safe | Palabras: 14551 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: musical, estilo, música, vocal, estilos, letra, rango, audio, género, aspecto.
- **SRC_041_PERUVIAN_SPANISH_ACCENT_SOCIOLECT** | Dominio: phenotype_culture_safe | Palabras: 5737 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: personaje, acento, voces, limeño, idunex, ejemplo, popular, español, estilo, contenido.
- **SRC_044_SUNO_CHARACTER_SONGWRITING** | Dominio: phenotype_culture_safe | Palabras: 7121 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: personaje, persona, musical, estilo, género, canción, ejemplo, contenido, canciones, puede.
- **SRC_048_COPILOT_DOCX_GROUNDING_LARGE_CANON** | Dominio: phenotype_culture_safe | Palabras: 6932 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: personaje, copilot, documento, sección, contenido, ejemplo, estilo, idunex, personalidad, respuestas.


#### Matriz runtime

### Grupo operativo: voice

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
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

| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
| `wrong_voice_age_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `accent_caricature_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `generic_caption_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `artist_imitation_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `song_identity_drift_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `voice_text_mismatch_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `music_output_repair` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

#### Reglas invariantes
**Regla 01 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 02 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 03 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 04 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 05 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 06 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 07 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 08 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 09 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 10 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 11 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 12 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 13 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 14 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 15 — Voz hablada, lenguaje, acento, escritura, canto y música**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

#### Casos operativos
#### Caso operativo 1: voice
**Entrada coloquial:** el usuario pide un output que afecta voice.  
**Acción del motor:** cargar Perfil360, filtrar campos `vocal_age, timbre, pitch_range, resonance_place, breath_pattern`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 2: language
**Entrada coloquial:** el usuario pide un output que afecta language.  
**Acción del motor:** cargar Perfil360, filtrar campos `accent_profile, peruvian_spanish_level, latam_neutrality_rule, sociolect_rules, slang_limit`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 3: music
**Entrada coloquial:** el usuario pide un output que afecta music.  
**Acción del motor:** cargar Perfil360, filtrar campos `song_vocal_texture, singing_range, suno_genre_range, rhythm_preference, instrumentation_palette`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

#### Caso operativo 4: qa
**Entrada coloquial:** el usuario pide un output que afecta qa.  
**Acción del motor:** cargar Perfil360, filtrar campos `wrong_voice_age_blocker, accent_caricature_blocker, generic_caption_blocker, artist_imitation_blocker, song_identity_drift_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  
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


### Extractos transformados — Acting, FACS, microgestos, pose, caminada y continuidad de video


- **Regla derivada 001:** --- SOURCE: Antropometr a corporal avanzada ---
Canon corporal realista para modelos
de IA adultos en Latinoamérica
(IDUNEX – PROJECT_BRAND_ENTITY)
Nota: No se encontraron referencias internas especíﬁcas sobre IDUNEX o
PROJECT_BRAND_ENTITY en las búsquedas, por lo que esta investigación se basa en fuentes
públicas ﬁables y estudios relevantes.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 002:** Crear modelos de IA con cuerpos humanos realistas requiere fundamentar
sus proporciones y características en datos antropométricos y principios
cientíﬁcos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 003:** Para un entorno latinoamericano (tomando a PROJECT_DECLARED_COUNTRY como
referencia central y comparando con variaciones regionales), se deﬁnen a
continuación los parámetros corporales clave, variaciones demográﬁcas
por edad, sexo y estilo de vida, la metodología de modelado para traducir
datos físicos a modelos digitales (con poses, movimiento, ropa y cámara),
normas para evitar fallos de realismo físico y pruebas de validación
(“golde. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 004:** Parámetros antropométricos completos para
adultos
Altura y peso: Los adultos latinoamericanos suelen tener estaturas
promedio algo menores que las de poblaciones europeas o norteamericanas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 005:** En PROJECT_DECLARED_COUNTRY, estudios recientes (2019) reportan una estatura media de ~1.65 m
en hombres y 1.53 m en mujeres, mientras los promedios para
Latinoamérica (8 países) rondan los 1.71 m en varones y 1.58 m en
mujeres 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 006:** Estas medidas reﬂejan inﬂuencias genéticas (fuerte ascendencia
indígena andina en PROJECT_DECLARED_COUNTRY) y factores socioeconómicos (nutrición infantil, salud
pública) 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 007:** En comparación, la media global de estatura es cercana a 1.71 m
en hombres y 1.59 m en mujeres, situando a la población latina ligeramente
por debajo de la media mundial.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 008:** Rangos realistas: La distribución de estaturas en Latinoamérica es amplia;
un 90% de los hombres latinoamericanos miden aproximadamente entre ~158
cm (5° percentil) y ~183 cm (95° percentil), y las mujeres entre ~146 cm y
~170 cm (5° y 95° percentil, respectivamente) 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 009:** En diseño antropométrico se
suelen usar estos percentiles extremos (5° y 95°) para dimensionar
productos y espacios socavando el 90% central de la población 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 010:** Alturas más
allá de estos rangos son raras y normalmente asociadas a condiciones
especíﬁcas (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 011:** desórdenes de crecimiento, deportistas extremos) y por tanto
servirían para modelos particulares, no para un “canon” general.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 012:** Figura 1: Estatura promedio de hombres y mujeres en PROJECT_DECLARED_COUNTRY, Latinoamérica y
globalmente (cm).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 013:** Los project-declareds son en promedio más bajos, con ~165 cm los
hombres y ~153 cm las mujeres, frente a ~171/158 cm en Latinoamérica 1 y
~171/159 cm a nivel mundial.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 014:** Masa corporal y BMI: El peso corporal adulto depende de la altura y
composición (músculo/grasa).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 015:** El Índice de Masa Corporal (IMC) proporciona
un indicador integrado de constitución: en Latinoamérica se ubica típicamente
en rango de sobrepeso para un adulto medio (25 ≤ IMC < 30).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 016:** PROJECT_DECLARED_COUNTRY registra un
IMC promedio ~27.8 kg/m² en adultos, con una desviación estándar ~4.8 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 017:** En
efecto, cerca de el 42% de la población project-declared adulta tiene sobrepeso (IMC
≥ 25 pero < 30) y alrededor de 22% sufre obesidad (IMC ≥ 30) 4 , cifras
acordes con el promedio latinoamericano (obesidad ~25% en la región según
estudio ELANS de 8 países) 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 018:** Estos datos de alto peso relativo reﬂejan
condiciones nutricionales y estilos de vida urbanos cambiantes en las últimas
décadas, con dietas más calóricas e inactividad física creciente 5 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 019:** No obstante,
al deﬁnir un canon realista típicamente se opta por representar un cuerpo en
normopeso (IMC ~22–24), con variantes ajustables hacia contextos de ﬁguras. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 020:** más corpulentas (IMC ~27) o más esbeltas (IMC ~20) según se requieran
ejempliﬁcaciones de diferentes perﬁles.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 021:** Composición corporal (músculo y grasa): La composición (% de músculo y
grasa) varía por sexo, edad y entrenamiento.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 022:** De media, el hombre adulto
tiene aproximadamente 38% de su peso en masa muscular (músculo
esquelético) y las mujeres ~31% 6 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 023:** En ambos sexos, la masa muscular alcanza
su cenit a ﬁn de la juventud (veintitantos años) y declina con la edad, más
aceleradamente en hombres 6 (véase sección 2).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 024:** Simultáneamente, el
porcentaje de grasa corporal suele crecer: un varón adulto en peso normal
suele tener ~15–20% de grasa corporal; en la mujer es más elevado, ~20–30%
(parte del dimorﬁsmo sexual humano).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 025:** En individuos deportistas
(especialmente atletas de rendimiento), la proporción de grasa puede bajar
hasta ~10–12% en varones o ~18–22% en mujeres, con la masa muscular
incrementándose en consecuencia.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 026:** La diferencia sexual en la composición
corporal es ﬁsiológica: los hombres tienen mayor masa magra y densidad
ósea (inﬂuencia de testosterona) mientras las mujeres tienden a acumular
tejido adiposo en caderas, muslos y mamas por efecto estrogénico.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 027:** Somatotipos (tipologías corporales): La población real presenta
variabilidad en la forma corporal que suele clasiﬁcarse en tres somatotipos
principales: (1) Ectomorfo: delgado, extremidades largas, poca masa
muscular/grasa; (2) Mesomorfo: atlético, musculoso y proporcionado; (3)
Endomorfo: tendencia a mayor adiposidad, constitución más robusta.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 028:** ej., a partir de un modelo base mesomorfo
promedio, se podrá ajustar hacia un fenotipo más ectomorfo (reduciendo
circunferencias musculares y peso) o más endomorfo (aumentando depósitos
adiposos y formas redondeadas) según la aplicación.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 029:** Dimensiones corporales (proporciones relativas): Para un realismo
convincente, es crucial preservar relaciones proporcionales humanas típicas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 030:** Reglas clásicas como la ﬁgura de “7.5–8 cabezas” de altura por persona
adulta proporcionan un punto de partida: un modelo idealizado mide unas 8
veces la longitud de su propia cabeza 7 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 031:** Ancho de hombros: un varón adulto
de estatura media (~170 cm) presenta hombros de ~45 cm (≈ 26% de su
altura), en tanto una mujer de ~160 cm tiene hombros de ~39 cm (≈ 24% de. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 032:** La cadera femenina suele ser notablemente más ancha en proporción
(similar o mayor que los hombros), mientras la cadera masculina es más
estrecha (≈ 80% de la anchura de hombros, aportando la silueta en forma de
“V”) 7 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 033:** La relación cintura-cadera es un índice clave: típicamente ~0.85–0.95
en hombres y ~0.70–0.80 en mujeres, reﬂejando un tronco más rectilíneo en
varones y una forma de “reloj de arena” en mujeres.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 034:** Otras relaciones
prototípicas: piernas ~ 50% de la estatura total (longitud de pierna medida
desde cadera hasta pie), torso ~ 30% de la altura, pies ~ 15% de la altura, y
manos ~ 10% de la altura (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 035:** La
circunferencia de cuello adulta oscila en ~35–38 cm en varones y ~30–34 cm
en mujeres, valores que correlacionan con la composición corporal (un cuello
>39 cm en varón se asocia a obesidad central) 6 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 036:** Estas proporciones servirán
de guía para calibrar cada segmento corporal en los modelos de IA,
asegurando que su físico tenga una coherencia interna: por ejemplo, si
aumentamos la anchura de hombros para un somatotipo mesomorfo, debe
mantenerse en equilibrio con la circunferencia de pecho y brazos, para no
crear una morfología inverosímil.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 037:** Variaciones por edad, sexo/género,
entrenamiento y estilo de vida
Ciclos de edad adulta: El aspecto corporal varía notablemente a lo largo de
la vida adulta.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 038:** En el adulto joven (20–35 años), se alcanza la cúspide física:
los músculos están plenamente desarrollados (pudiendo constituir ~40% del
peso en varones jóvenes; ~30% en mujeres 6 8 ) y la grasa corporal se
mantiene en niveles bajos (10–20% en hombres; 18–28% en mujeres).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 039:** La
fuerza y densidad ósea son máximas alrededor de los 30 años y la piel es
uniforme y ﬁrme, con alta elasticidad y sin pérdida de tono visible.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 040:** Hacia la
franja de 36–55 años, surgen cambios graduales: descenso lento de masa
muscular (en hombres ~1–2% por año tras los 50; en mujeres ~0.5–1%
anual) 6 , y un aumento progresivo en grasa corporal central (grasa visceral
en abdomen y perivisceral).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 041:** Por ejemplo, a los 50 años un hombre puede
haber perdido ~4–5 kg de músculo en comparación con sus 20s 6 , y acumulado
grasa abdominal, aumentando su perímetro de cintura unos centímetros.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 042:** En la
madurez tardía (más de 55–60 años), se aceleran la sarcopenia (pérdida
muscular, ~1% anual de masa muscular en la sexta década) y la reducción de. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 043:** estatura (por cambios en columna y discos intervertebrales, ~1–2 cm por
década tras los 40–50 años).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 044:** Los hombres mayores pueden perder peso
corporal total ligeramente tras los 60 (por disminución hormonal, densidad
ósea y masa magra), y las mujeres mayores tras la menopausia experimentan
cambios en la densidad ósea y distribución de grasa (más acumulación central
al disminuir estrógenos).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 045:** Diferencias por sexo (biológicas): Los hombres y mujeres exhiben rasgos
corporales distintos desde la pubertad: los varones son por lo general más
altos y de complexión más musculosa (particularmente tronco superior),
con espalda y hombros más anchos y pelvis estrecha 7 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 046:** Tienen huesos más
densos y metabolismo basal más alto (debido mayor masa magra), lo que
facilita menor porcentaje de grasa.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 047:** Las mujeres, en promedio, son más bajas
y de contextura menos muscular; presentan hombros más estrechos y una
pelvis más ancha (adaptada a la gestación) 7 , acumulando más grasa
subcutánea en ca. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 048:** --- SOURCE: Lencer abodywear editorial adulto no expl cito ---
Lineamientos para la representación
de lencería mediante modelos de IA
sintéticos adultos (Guía Integral)
La representación de lencería, ropa interior, bikinis y bodywear con
modelos sintéticos generados por IA es un campo emergente que requiere
un enfoque 360 grados para garantizar que el contenido sea editorial,
elegante, no explícito y comercialmente s. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 049:** En esta guía abordamos los
aspectos creativos, técnicos, legales-comerciales y de control de calidad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 050:** Cada sección contiene directrices detalladas, tablas y ejemplos prácticos, con
un lenguaje técnico enfocado en moda y publicidad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 051:** Nota: Esta guía se enfoca explícitamente en modelos sintéticos adultos, no
en personas reales.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 052:** Respalda el cumplimiento de estándares profesionales de
la industria de la moda y la publicidad, incluyendo políticas de plataformas
como Amazon, Google Ads e Instagram.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 053:** Límites visuales y de contenido
Objetivo: Establecer qué se considera “editorial, elegante, no explícito y
seguro” y reclasiﬁcar visualmente qué está estrictamente prohibido.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 054:** Garantizar que las representaciones de lencería con IA se mantengan dentro
de límites claros de decoro.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 055:** La publicidad en plataformas exige prácticas prudentes para evitar la
restricción de contenido.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 056:** anuncios con contenido sexual explícito o modelos semidesnudos en
posiciones sugerentes.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 057:** Amazon, en sus directrices, exige que las poses no sean
sugerentes: modelos sin abrir demasiado las piernas, ojos abiertos, boca
cerrada, brazos relajados y sin cubrir estratégicamente partes íntimas 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 058:** Diseño y realismo de las prendas
Objetivo: Asegurar que las prendas generadas por IA (sujetadores, panties,
bikinis, bodies) sean visualmente realistas, en términos de diseño, ajuste,
materiales, comportamiento de telas, costuras, elasticidad, compresión,
así como transparencias manejadas de forma segura (sheerness controlada).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 059:** Esto garantizará que, aunque el modelo sea sintético, la prenda se perciba real
y bien confeccionada, tal como lo haría en una sesión fotográﬁca profesional.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 060:** Aj{"error":"InvalidReq
uest: This model's
maximum context
length is 8192 tokens.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 061:** --- SOURCE: Motion bible y caminada ---
Control de pasos y equilibrio          Personalidad en el
En una marcha realista, el cuerpo      movimiento
alterna soportando peso en cada        La forma de caminar revela
pie.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 062:** Cada paso debe mostrar un         personalidad: movimientos
apoyo ﬁrme del pie con el suelo,       amplios y rítmicos indican
seguido de un despegue, mientras       conﬁanza; pasos suaves y lentos
el centro de gravedad se desplaza      reﬂejan calma; gestos ﬂuidos y
suavemente de un lado a otro.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 063:** El       miradas sutiles sugieren seducción;
cuerpo desciende ligeramente al        postura erguida y controlada
recibir el peso (pose down) y luego    transmite profesionalidad; un
asciende al impulsarse con la punta    andar suelto con cambios de ritmo
del pie (pose up), evitando que el     parece casual y urbano; una
personaje parezca ﬂotar sin peso.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 064:** Ropa y calzado inﬂuyen en la           Prompts detallados para
marcha                                 capturar el movimiento
Tacones altos obligan a acortar la     Para guiar un modelo de vídeo IA,
zancada e inclinar el cuerpo           describe el sujeto, la acción y el
ligeramente hacia adelante,            entorno de forma narrativa y
requiriendo equilibrio extra en        precisa.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 065:** “camina
ajustada puede restringir el área de   lentamente”) y detalles de postura y
paso.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 066:** Usa prompts negativos
ralentiza y reduce la amplitud del     para vetar efectos no deseados (ej.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 067:** movimiento, mientras que ropa          “sin jitter ni extremidades
suelta y calzado deportivo permiten    deformes”).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

### Extractos transformados — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal


- **Regla derivada 001:** --- SOURCE: Antropometr a corporal avanzada ---
Canon corporal realista para modelos
de IA adultos en Latinoamérica
(IDUNEX – PROJECT_BRAND_ENTITY)
Nota: No se encontraron referencias internas especíﬁcas sobre IDUNEX o
PROJECT_BRAND_ENTITY en las búsquedas, por lo que esta investigación se basa en fuentes
públicas ﬁables y estudios relevantes.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 002:** Crear modelos de IA con cuerpos humanos realistas requiere fundamentar
sus proporciones y características en datos antropométricos y principios
cientíﬁcos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 003:** Para un entorno latinoamericano (tomando a PROJECT_DECLARED_COUNTRY como
referencia central y comparando con variaciones regionales), se deﬁnen a
continuación los parámetros corporales clave, variaciones demográﬁcas
por edad, sexo y estilo de vida, la metodología de modelado para traducir
datos físicos a modelos digitales (con poses, movimiento, ropa y cámara),
normas para evitar fallos de realismo físico y pruebas de validación
(“golde. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 004:** Parámetros antropométricos completos para
adultos
Altura y peso: Los adultos latinoamericanos suelen tener estaturas
promedio algo menores que las de poblaciones europeas o norteamericanas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 005:** En PROJECT_DECLARED_COUNTRY, estudios recientes (2019) reportan una estatura media de ~1.65 m
en hombres y 1.53 m en mujeres, mientras los promedios para
Latinoamérica (8 países) rondan los 1.71 m en varones y 1.58 m en
mujeres 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 006:** Estas medidas reﬂejan inﬂuencias genéticas (fuerte ascendencia
indígena andina en PROJECT_DECLARED_COUNTRY) y factores socioeconómicos (nutrición infantil, salud
pública) 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 007:** En comparación, la media global de estatura es cercana a 1.71 m
en hombres y 1.59 m en mujeres, situando a la población latina ligeramente
por debajo de la media mundial.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 008:** Rangos realistas: La distribución de estaturas en Latinoamérica es amplia;
un 90% de los hombres latinoamericanos miden aproximadamente entre ~158
cm (5° percentil) y ~183 cm (95° percentil), y las mujeres entre ~146 cm y
~170 cm (5° y 95° percentil, respectivamente) 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 009:** En diseño antropométrico se
suelen usar estos percentiles extremos (5° y 95°) para dimensionar
productos y espacios socavando el 90% central de la población 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 010:** Alturas más
allá de estos rangos son raras y normalmente asociadas a condiciones
especíﬁcas (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 011:** desórdenes de crecimiento, deportistas extremos) y por tanto
servirían para modelos particulares, no para un “canon” general.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 012:** Figura 1: Estatura promedio de hombres y mujeres en PROJECT_DECLARED_COUNTRY, Latinoamérica y
globalmente (cm).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 013:** Los project-declareds son en promedio más bajos, con ~165 cm los
hombres y ~153 cm las mujeres, frente a ~171/158 cm en Latinoamérica 1 y
~171/159 cm a nivel mundial.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 014:** Masa corporal y BMI: El peso corporal adulto depende de la altura y
composición (músculo/grasa).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 015:** El Índice de Masa Corporal (IMC) proporciona
un indicador integrado de constitución: en Latinoamérica se ubica típicamente
en rango de sobrepeso para un adulto medio (25 ≤ IMC < 30).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 016:** PROJECT_DECLARED_COUNTRY registra un
IMC promedio ~27.8 kg/m² en adultos, con una desviación estándar ~4.8 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 017:** En
efecto, cerca de el 42% de la población project-declared adulta tiene sobrepeso (IMC
≥ 25 pero < 30) y alrededor de 22% sufre obesidad (IMC ≥ 30) 4 , cifras
acordes con el promedio latinoamericano (obesidad ~25% en la región según
estudio ELANS de 8 países) 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 018:** Estos datos de alto peso relativo reﬂejan
condiciones nutricionales y estilos de vida urbanos cambiantes en las últimas
décadas, con dietas más calóricas e inactividad física creciente 5 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 019:** No obstante,
al deﬁnir un canon realista típicamente se opta por representar un cuerpo en
normopeso (IMC ~22–24), con variantes ajustables hacia contextos de ﬁguras. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 020:** más corpulentas (IMC ~27) o más esbeltas (IMC ~20) según se requieran
ejempliﬁcaciones de diferentes perﬁles.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 021:** Composición corporal (músculo y grasa): La composición (% de músculo y
grasa) varía por sexo, edad y entrenamiento.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 022:** De media, el hombre adulto
tiene aproximadamente 38% de su peso en masa muscular (músculo
esquelético) y las mujeres ~31% 6 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 023:** En ambos sexos, la masa muscular alcanza
su cenit a ﬁn de la juventud (veintitantos años) y declina con la edad, más
aceleradamente en hombres 6 (véase sección 2).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 024:** Simultáneamente, el
porcentaje de grasa corporal suele crecer: un varón adulto en peso normal
suele tener ~15–20% de grasa corporal; en la mujer es más elevado, ~20–30%
(parte del dimorﬁsmo sexual humano).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 025:** En individuos deportistas
(especialmente atletas de rendimiento), la proporción de grasa puede bajar
hasta ~10–12% en varones o ~18–22% en mujeres, con la masa muscular
incrementándose en consecuencia.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 026:** La diferencia sexual en la composición
corporal es ﬁsiológica: los hombres tienen mayor masa magra y densidad
ósea (inﬂuencia de testosterona) mientras las mujeres tienden a acumular
tejido adiposo en caderas, muslos y mamas por efecto estrogénico.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 027:** Somatotipos (tipologías corporales): La población real presenta
variabilidad en la forma corporal que suele clasiﬁcarse en tres somatotipos
principales: (1) Ectomorfo: delgado, extremidades largas, poca masa
muscular/grasa; (2) Mesomorfo: atlético, musculoso y proporcionado; (3)
Endomorfo: tendencia a mayor adiposidad, constitución más robusta.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 028:** ej., a partir de un modelo base mesomorfo
promedio, se podrá ajustar hacia un fenotipo más ectomorfo (reduciendo
circunferencias musculares y peso) o más endomorfo (aumentando depósitos
adiposos y formas redondeadas) según la aplicación.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 029:** Dimensiones corporales (proporciones relativas): Para un realismo
convincente, es crucial preservar relaciones proporcionales humanas típicas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 030:** Reglas clásicas como la ﬁgura de “7.5–8 cabezas” de altura por persona
adulta proporcionan un punto de partida: un modelo idealizado mide unas 8
veces la longitud de su propia cabeza 7 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 031:** Ancho de hombros: un varón adulto
de estatura media (~170 cm) presenta hombros de ~45 cm (≈ 26% de su
altura), en tanto una mujer de ~160 cm tiene hombros de ~39 cm (≈ 24% de. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 032:** La cadera femenina suele ser notablemente más ancha en proporción
(similar o mayor que los hombros), mientras la cadera masculina es más
estrecha (≈ 80% de la anchura de hombros, aportando la silueta en forma de
“V”) 7 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 033:** La relación cintura-cadera es un índice clave: típicamente ~0.85–0.95
en hombres y ~0.70–0.80 en mujeres, reﬂejando un tronco más rectilíneo en
varones y una forma de “reloj de arena” en mujeres.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 034:** Otras relaciones
prototípicas: piernas ~ 50% de la estatura total (longitud de pierna medida
desde cadera hasta pie), torso ~ 30% de la altura, pies ~ 15% de la altura, y
manos ~ 10% de la altura (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 035:** La
circunferencia de cuello adulta oscila en ~35–38 cm en varones y ~30–34 cm
en mujeres, valores que correlacionan con la composición corporal (un cuello
>39 cm en varón se asocia a obesidad central) 6 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 036:** Estas proporciones servirán
de guía para calibrar cada segmento corporal en los modelos de IA,
asegurando que su físico tenga una coherencia interna: por ejemplo, si
aumentamos la anchura de hombros para un somatotipo mesomorfo, debe
mantenerse en equilibrio con la circunferencia de pecho y brazos, para no
crear una morfología inverosímil.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 037:** Variaciones por edad, sexo/género,
entrenamiento y estilo de vida
Ciclos de edad adulta: El aspecto corporal varía notablemente a lo largo de
la vida adulta.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 038:** En el adulto joven (20–35 años), se alcanza la cúspide física:
los músculos están plenamente desarrollados (pudiendo constituir ~40% del
peso en varones jóvenes; ~30% en mujeres 6 8 ) y la grasa corporal se
mantiene en niveles bajos (10–20% en hombres; 18–28% en mujeres).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 039:** La
fuerza y densidad ósea son máximas alrededor de los 30 años y la piel es
uniforme y ﬁrme, con alta elasticidad y sin pérdida de tono visible.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 040:** Hacia la
franja de 36–55 años, surgen cambios graduales: descenso lento de masa
muscular (en hombres ~1–2% por año tras los 50; en mujeres ~0.5–1%
anual) 6 , y un aumento progresivo en grasa corporal central (grasa visceral
en abdomen y perivisceral).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 041:** Por ejemplo, a los 50 años un hombre puede
haber perdido ~4–5 kg de músculo en comparación con sus 20s 6 , y acumulado
grasa abdominal, aumentando su perímetro de cintura unos centímetros.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 042:** En la
madurez tardía (más de 55–60 años), se aceleran la sarcopenia (pérdida
muscular, ~1% anual de masa muscular en la sexta década) y la reducción de. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 043:** estatura (por cambios en columna y discos intervertebrales, ~1–2 cm por
década tras los 40–50 años).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 044:** Los hombres mayores pueden perder peso
corporal total ligeramente tras los 60 (por disminución hormonal, densidad
ósea y masa magra), y las mujeres mayores tras la menopausia experimentan
cambios en la densidad ósea y distribución de grasa (más acumulación central
al disminuir estrógenos).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 045:** Diferencias por sexo (biológicas): Los hombres y mujeres exhiben rasgos
corporales distintos desde la pubertad: los varones son por lo general más
altos y de complexión más musculosa (particularmente tronco superior),
con espalda y hombros más anchos y pelvis estrecha 7 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 046:** Tienen huesos más
densos y metabolismo basal más alto (debido mayor masa magra), lo que
facilita menor porcentaje de grasa.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 047:** Las mujeres, en promedio, son más bajas
y de contextura menos muscular; presentan hombros más estrechos y una
pelvis más ancha (adaptada a la gestación) 7 , acumulando más grasa
subcutánea en ca. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 048:** --- SOURCE: Lencer abodywear editorial adulto no expl cito ---
Lineamientos para la representación
de lencería mediante modelos de IA
sintéticos adultos (Guía Integral)
La representación de lencería, ropa interior, bikinis y bodywear con
modelos sintéticos generados por IA es un campo emergente que requiere
un enfoque 360 grados para garantizar que el contenido sea editorial,
elegante, no explícito y comercialmente s. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 049:** En esta guía abordamos los
aspectos creativos, técnicos, legales-comerciales y de control de calidad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 050:** Cada sección contiene directrices detalladas, tablas y ejemplos prácticos, con
un lenguaje técnico enfocado en moda y publicidad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 051:** Nota: Esta guía se enfoca explícitamente en modelos sintéticos adultos, no
en personas reales.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 052:** Respalda el cumplimiento de estándares profesionales de
la industria de la moda y la publicidad, incluyendo políticas de plataformas
como Amazon, Google Ads e Instagram.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 053:** Límites visuales y de contenido
Objetivo: Establecer qué se considera “editorial, elegante, no explícito y
seguro” y reclasiﬁcar visualmente qué está estrictamente prohibido.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 054:** Garantizar que las representaciones de lencería con IA se mantengan dentro
de límites claros de decoro.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 055:** La publicidad en plataformas exige prácticas prudentes para evitar la
restricción de contenido.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 056:** anuncios con contenido sexual explícito o modelos semidesnudos en
posiciones sugerentes.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 057:** Amazon, en sus directrices, exige que las poses no sean
sugerentes: modelos sin abrir demasiado las piernas, ojos abiertos, boca
cerrada, brazos relajados y sin cubrir estratégicamente partes íntimas 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 058:** Diseño y realismo de las prendas
Objetivo: Asegurar que las prendas generadas por IA (sujetadores, panties,
bikinis, bodies) sean visualmente realistas, en términos de diseño, ajuste,
materiales, comportamiento de telas, costuras, elasticidad, compresión,
así como transparencias manejadas de forma segura (sheerness controlada).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 059:** Esto garantizará que, aunque el modelo sea sintético, la prenda se perciba real
y bien confeccionada, tal como lo haría en una sesión fotográﬁca profesional.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 060:** Aj{"error":"InvalidReq
uest: This model's
maximum context
length is 8192 tokens.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 061:** --- SOURCE: Motion bible y caminada ---
Control de pasos y equilibrio          Personalidad en el
En una marcha realista, el cuerpo      movimiento
alterna soportando peso en cada        La forma de caminar revela
pie.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 062:** Cada paso debe mostrar un         personalidad: movimientos
apoyo ﬁrme del pie con el suelo,       amplios y rítmicos indican
seguido de un despegue, mientras       conﬁanza; pasos suaves y lentos
el centro de gravedad se desplaza      reﬂejan calma; gestos ﬂuidos y
suavemente de un lado a otro.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 063:** El       miradas sutiles sugieren seducción;
cuerpo desciende ligeramente al        postura erguida y controlada
recibir el peso (pose down) y luego    transmite profesionalidad; un
asciende al impulsarse con la punta    andar suelto con cambios de ritmo
del pie (pose up), evitando que el     parece casual y urbano; una
personaje parezca ﬂotar sin peso.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 064:** Ropa y calzado inﬂuyen en la           Prompts detallados para
marcha                                 capturar el movimiento
Tacones altos obligan a acortar la     Para guiar un modelo de vídeo IA,
zancada e inclinar el cuerpo           describe el sujeto, la acción y el
ligeramente hacia adelante,            entorno de forma narrativa y
requiriendo equilibrio extra en        precisa.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 065:** “camina
ajustada puede restringir el área de   lentamente”) y detalles de postura y
paso.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 066:** Usa prompts negativos
ralentiza y reduce la amplitud del     para vetar efectos no deseados (ej.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 067:** movimiento, mientras que ropa          “sin jitter ni extremidades
suelta y calzado deportivo permiten    deformes”).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

### Extractos transformados — Voz hablada, lenguaje, acento, escritura, canto y música


- **Regla derivada 001:** --- SOURCE: Voz hablada para ElevenLabs ---
Guía completa para crear la ﬁcha
técnica de una voz sintética (adulto,
español latino/project-declared)
Introducción:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 002:** El diseño de una voz sintética adulta en español (orientada al español
latinoamericano neutro y sus variaciones regionales, como el acento
project-declared) requiere un enfoque detallado tanto técnico como perceptual.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 003:** ElevenLabs, como plataforma avanzada de text-to-speech (TTS), ofrece
herramientas para ajustar parámetros de voz clonada o sintética que
permiten lograr voces realistas, estables y personalizadas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 004:** El español es uno de los idiomas más difundidos, hablado por cerca de 500
millones de personas en el mundo 1 ; sin embargo, presenta numerosas
variaciones de acento, entonación y léxico según cada país y región 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 005:** Por
ello, crear una ﬁcha técnica de voz implica especiﬁcar con claridad las
características acústicas (como tono, timbre, ritmo, etc.), los usos previstos
(narración, publicidad, diálogos, etc.) y las preferencias de conﬁguración en
la plataforma elegida.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 006:** Además, es fundamental considerar prácticas éticas: el
respeto a la identidad vocal original, el consentimiento para clonación y evitar
la suplantación de voces reales 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 007:** En esta guía práctica repasaremos los parámetros clave de la voz hablada en
adultos, diferencias entre estilos de locución, recomendaciones de scripts de
entrenamiento, ajustes especíﬁcos en ElevenLabs, limitaciones actuales (como
la diﬁcultad para cantar o gritar), campos para documentar la ﬁcha técnica, y
una lista de control (QA) para evaluar la calidad de la voz resultante.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 008:** Parámetros vocales recomendados para voces
adultas en español
Al crear la ﬁcha técnica de una voz sintética, se deben deﬁnir parámetros de
voz que reﬂejen la cualidad de un adulto hispanohablante.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 009:** A continuación,
detallamos los principales parámetros acústicos y articulatorios a considerar:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 010:** Diferencias entre estilos de voz: narración,
conversación, publicidad, actuación, susurro y
entrevista
No todas las aplicaciones requieren el mismo estilo de habla.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 011:** Es vital ajustar la
voz según el caso de uso, ya que varían los objetivos comunicativos, la
entonación y la energía.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 012:** A continuación, comparamos seis estilos comunes
de locución y sus características principales, junto con algunas
recomendaciones y precauciones:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 013:** --- SOURCE: Voz cantada y Suno ---
Guía integral: creación y gestión de
perﬁles musicales diferenciados en
Suno para modelos vocales IDUNEX
Resumen ejecutivo: Para diseñar perﬁles vocales completamente
diferenciados para la colección IDUNEX en Suno, es fundamental deﬁnir las
características musicales y vocales de cada modelo, controlar la distinción
entre voz cantada vs.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 014:** hablada, y dominar las herramientas de Suno (campos
de estilo, exclusión de estilos, estructuración de letras, performance tags, etc.)
al máximo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 015:** Solo entonces se puede lograr que cada modelo tenga una
personalidad única reconocible, consistente en varias canciones y contextos
(desde prototipos internos hasta producciones comerciales).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 016:** Los puntos
críticos incluyen: deﬁnir géneros, tempo y rango vocal de cada perﬁl para
delimitar su identidad; usar etiquetas y prompts adecuados para guiar la voz
(cantada/hablada), la estructura (introducción, verso, coro, etc.) y la
interpretación (volumen y matices); y establecer un proceso sistemático de
pruebas con un riguroso framework de QA para asegurar que cada perﬁl
cumpla con su descripción target.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 017:** También se deben abordar proactivamente
los riesgos de la generación de voz (falta de identidad, acentos erróneos, etc.),
con mitigaciones desde el diseño y la ejecución.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 018:** En este documento se detallan
prácticas recomendadas y ejemplos, con fuentes tanto públicas como de
conocimiento especíﬁco de la plataforma, para cada uno de estos aspectos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 019:** Nota: IDUNEX se considera una colección de modelos vocales propietarios sin
referencias públicas.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 020:** Este informe propondrá un marco general para crear
identidades vocálicas personalizadas con Suno, adaptable a cualquier
conjunto de modelos (arquetipos de voces) en español latino (acentuación
project-declared) e inglés.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 021:** Explicaremos qué decisiones tomar, así como por qué,
incluyendo enfoques alternativos si no se dispone de información concreta.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 022:** Deﬁnición de un perﬁl musical por modelo
IDUNEX
Por qué es importante el perﬁl: Cada modelo vocal IDUNEX debe contar con
una ﬁcha técnica detallada que recoja todos los atributos musicales y vocales
que deﬁnen su personalidad sonora.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 023:** Esto servirá de guía para conﬁgurar los
prompts de Suno y garantizar que cada modelo suene único y consistente.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 024:** Los componentes mínimos de un perﬁl musical incluyen: género principal,
subgéneros relacionados, tempo (BPM) típico, tonalidades habituales
(mayor/menor, escalas preferidas), rango vocal accesible, color o timbre
vocal, nivel de energía habitual, y los parámetros avanzados de Suno: rareza
(weirdness), Style Inﬂuence e Audio Inﬂuence.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 025:** En proyectos reales, estos
campos permiten diseñar “voces virtuales” con la misma precisión que un
productor deﬁne la identidad de un cantante real.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 026:** El género deﬁne la estética general del modelo; conviene escoger uno o dos
pilares que sirvan de base.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 027:** Por ejemplo: IDUNEX A puede ser un cantante pop
latino, IDUNEX B un rapero urbano, etc.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 028:** Los subgéneros aportan matices
adicionales (balada romántica, trap melódico, future house, etc.), delimitando
mejor la paleta de sonidos y arreglos esperados 1 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 029:** Este atributo orienta
directamente la instrumentación y grooves de la pista; Suno responde muy
bien a géneros especíﬁcos, sobre todo si se combinan con referencias de era. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 030:** “rock” a secas, guiará la generación hacia un
sonido más enfocado y coherente con Nirvana, y con la estética grunge
asociada.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 031:** La velocidad rítmica de las canciones preferidas por cada modelo es otro
diferenciador.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 032:** ~60–80 BPM), mientras uno electrónico de música bailable estará cómodo
en tempos rápidos (120–130 BMP).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 033:** Suno permite especiﬁcar el tempo tanto
mediante un número (por ejemplo, “120 BPM”) como con términos italianos
(e.g.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 034:** Importancia: describir un BPM
guía la energía: velocidades altas producen canciones enérgicas y bailables,
mientras que tempos lentos dan toques melancólicos o relajantes 3 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 035:** En el perﬁl
IDUNEX, deﬁnir un rango de BPM y un valor típico permite al equipo saber
cómo calibrar el prompt para obtener la vivacidad deseada.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 036:** Deﬁnir una o dos tonalidades preferidas (por ejemplo, Do mayor, La menor)
es útil para encauzar la atmósfera y la tesitura del modelo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 037:** Las tonalidades
mayores tienden a sonar alegres y brillantes, mientras las tonalidades
menores evocan una emoción más melancólica e intensa 3 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 038:** “en La menor” o “C major”) puede inﬂuir en las
notas y acordes que usará Suno 3 , ayudando a deﬁnir la zona cómoda de la
voz del modelo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 039:** Además, ﬁjar tonalidades relacionadas con su rango vocal (ver
abajo) asegurará que las melodías generadas se ajusten a su tesitura: por
ejemplo, un modelo con voz soprano lucirá en tonalidades como Sol mayor (G)
o La mayor (A), mientras que uno barítono puede favorecer Re menor (D
minor) o Fa mayor.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 040:** Esto no es completamente determinístico (Suno no siempre
ﬁja exactamente la escala marcada, pero inﬂuye fuertemente en la elección
de melodías y acordes 3 ).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 041:** Una recomendación es deﬁnir también la edad aparente de la voz (joven,
madura, infantil, etc.) y el género del cantante (femenina, masculina,
andrógina).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 042:** Esto no tiene un campo especíﬁco, pero Suno inferirá por las
descripciones y las etiquetas de género en la letra (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 043:** Si un modelo IDUNEX
tiene un personaje claro (por ejemplo, un cantante masculino de mediana
edad con voz ronca), esta información debe ﬁgurar en su perﬁl para que los
creadores la incluyan en los prompts, asegurando la coherencia de la voz.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 044:** Este factor se relaciona tanto con el género (p.ej., rock suele ser +enérgico;
ambient más calmo) como con la entrega.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 045:** En el perﬁl conviene describir si la
voz suele ser suave y contenida o potente y explosiva, y en qué contextos.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 046:** Por ejemplo, un modelo orientado a música indie íntima se caracterizará por
interpretaciones apacibles y emotivas; por otro lado, uno enfocado en EDM
festivalero tendrá una presencia más dinámica y energizante.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 047:** En la práctica
con Suno, esta característica se integra mediante tags de mood: palabras como
“calmado, etéreo, suave” vs “powerful, energetic” en el campo Estilo, o
directivas por sección (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 048:** La energía deﬁne la atmósfera general y, junto con el tempo y la
instrumentación, dará cohesión a lo que se espera de cada modelo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 049:** La rareza (Weirdness) es un control deslizante de 0 a 100 que ajusta cuánto
se desvía Suno de las normas típicas del género 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 050:** En valores bajos (0–20%)
es muy conservador: produce canciones seguras, genéricas, casi como clichés
del género deﬁnido (útil para pop comercial o jingles publicitarios) 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 051:** Con
valores medios (40–60%) –considerados óptimos para 90% de los casos–, la
canción será creativa pero coherente, combinando familiaridad y novedad 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 052:** Si se sube a 60–80%, se obtienen combinaciones experimentales en la
música, aptas para exploraciones artísticas o fusiones arriesgadas de estilos 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 053:** Por último, por encima de 81% entra en “modo glitch”, generando resultados
muy fragmentados, útiles solo para pedazos de audio abstracto pero
impracticables en canciones completas 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 054:** Consejo: mantén la rareza ≤60%
para producciones que requieran estructura estable, y aumenta a >60% solo si
buscas texturas raras intencionalmente 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 055:** Este slider** (0–100%) decide qué tan ﬁelmente sigue Suno las descripciones
del campo de Estilo en el prompt 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 056:** En - interpretaciones sueltas (0–30%):
Suno toma tus tags solo como sugerencias y se permite licencias (podría
desviarse a subestilos cercanos o instrumentaciones inesperadas) 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 057:** En
valores medios (40–70%) se obtiene un equilibrio: la canción respeta en
general el género y los instrumentos indicados, pero sin volverse rígida 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 058:** Con valores altos (70–100%), cada indicación se sigue al pie de la letra: la
generación tiende a estar encorsetada en tu descripción, con menos espacio
para que la IA improvise 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 059:** Esto es ideal cuando se tiene una visión muy clara
(y minimalista) de lo deseado (p.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 060:** ej., “acústico con solo de piano”); sin embargo,
hay que tener cuidado de no saturar el campo Estilo con muchísimos tags si la
inﬂuencia de estilo es 100%, porque la IA tratará de cumplirlos todos y podría
saturar el arreglo 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 061:** Regla práctica: si usas Style Inﬂuence >70%, mantén tu
prompt de Estilo conciso (≤5-8 términos) 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 062:** Para la mayoría de casos creativos,
40-60% es seguro y ﬂexible, combinando ﬁdelidad y creatividad a la vez 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 063:** Este parámetro de 0–100% aparece cuando subes un audio propio de
referencia en Suno (función Sample mode) 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 064:** Recomendación general: la comunidad ha descubierto que ~55% en Audio
Inﬂuence es un punto dulce para preservar la melodía pero permitiendo que
el contexto sonoro sea reimaginado 4 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 065:** --- SOURCE: Optimizaci n ChatGPT JSONTXT ---
Estructuración Óptima de Archivos
JSON y TXT para Conocimiento en
Agentes de IA Humanizados
Resumen: En esta guía describimos cómo estructurar archivos 💾 JSON y TXT
para maximizar su efectividad como fuentes de conocimiento y directrices en
agentes de IA conversacionales tipo ChatGPT.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 066:** Abordamos la diferencia entre
instrucciones del sistema (prompts de rol) y archivos de conocimiento, luego
proponemos una estructura canónica para un archivo JSON de conocimiento/
instrucciones (incluyendo campos como “tarjeta de tiempo de ejecución”,
“bloqueo de identidad”, “resumen activo”, “restricciones negativas”,
“comportamiento de respaldo” y “pares de Pregunta/Respuesta”).. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 067:** También
explicamos cómo diseñar un archivo de texto (PromptPack) con secciones
claras, así como técnicas para reducir la deriva de la información cuando
se recupera el conocimiento, métodos para evita. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 068:** --- SOURCE: Biografía familiar y migratoria ---
Guía Integral para Crear Biografías
Familiares Ficticias Realistas para
Modelos IA (IDUNEX)
Diseñar biografías familiares ﬁcticias altamente realistas – con profundidad
identitaria y plena plausibilidad – permite dotar a modelos de IA (adultos) de
una personalidad consistente y creíble.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 069:** Este informe brinda un marco
escalable y accionable para crear decenas o centenares de perﬁles
sintéticos con diversidad sociocultural (contexto PROJECT_DECLARED_LOCALITY) y en alineación
con el ecosistema PROJECT_BRAND_ENTITY.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 070:** Se abordan recomendaciones detalladas para
un uso tanto interno (entrenamiento de modelos) como externo
(marketing de contenido), salvaguardando los aspectos éticos y legales.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 071:** Estructura Biográﬁca Completa y Verosímil
Una biografía familiar ﬁcticia realista debe abarcar todas las etapas vitales
y relaciones esenciales de la persona artiﬁcial.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 072:** Esto conﬁere profundidad al
personaje y proporciona material coherente para entrenar su
comportamiento y comunicación como modelo IA.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 073:** una estructura recomendada, asegurando que cada elemento de la ruta de vida
se integre de forma lógica y rica en contexto local:. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 074:** Pautas de implementación: Presenta la biografía de forma cronológica
(infancia → adolescencia → formación → vida adulta actual) para mayor. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 075:** Evita saturar con datos irrelevantes: cada detalle debe aportar a la
caracterización del modelo, ya sea en su personalidad, valores o
habilidades 2 .. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 076:** Antes de ﬁnalizar, comprueba que la edad actual del personaje
concuerda con los eventos narrados (nacimiento, graduaciones, trabajos)
para no generar inconsistencias.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 077:** Mapeo Causal: De la Historia Familiar a la
Identidad del Modelo
Una biografía bien conectada con la personalidad actual del modelo es
esencial para su credibilidad.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 078:** Esto signiﬁca establecer cómo el recorrido vital y
familiar del personaje inﬂuye en sus valores, forma de hablar, profesión y
estilo.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 079:** Este mapa causal garantiza una coherencia psicológica: las vivencias
pasadas justiﬁcan el comportamiento presente.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

- **Regla derivada 080:** --- SOURCE: Moral valores y tica personal ---
Matriz moral realista para IA
humanizada: Desarrollo y aplicación
Desarrollar una matriz de moral convincente y realista para modelos de IA
con personalidad humana implica dotar a la IA de un perﬁl ético complejo,
creíble y consistente.. **Runtime:** convertir en campo verificable, test QA y fallback. **Bloqueo:** no usar como adorno ni como resumen.

## H71-H80 SAFE_APPAREL_WATERMARK_AGENT10N
H71_H80_AGENT10N=SAFE_APPAREL_TAXONOMY; ADULT_REVEALING_APPAREL_NOT_NUDITY; VENDOR_PROMPT_SANITIZATION_SAFE_APPAREL; WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED; ALLOW adult editorial beachwear/swimwear/intimate apparel/catalog/corset/body/performance wardrobe when covered non-explicit; BLOCK nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded or school-coded sexualization and real-person copying.
ALLOW_ADULT_EDITORIAL: moda de playa, traje de bano, ropa de bano, bikini editorial, swimwear campaign, beachwear, resortwear, moda intima editorial/catalog, ropa interior de catalogo, corset/body/bodysuit, vestuario de show adulto, vestuario de videoclip adulto y outfit de performance adulta cuando el modelo es adulto, cubierto y no explicito.
CONDITIONAL_REWRITE: convertir styling glam/provocativo, boudoir editorial, fantasia adulta y vestuario de alto impacto a lenguaje adulto, editorial, comercial, non-explicit, covered intimate areas.
BLOCK_ALWAYS: nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded styling, school-coded sexualization, real-person copying y cualquier intento de saltar locks de edad o identidad.
WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED.
