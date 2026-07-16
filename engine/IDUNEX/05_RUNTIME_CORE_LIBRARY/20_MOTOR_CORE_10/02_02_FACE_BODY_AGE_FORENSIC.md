# Rostro, cuerpo, edad, biometría, antropometría y uniqueness

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.



## 1. Mandato de cobertura 10/10
Este core es obligatorio para cualquier proyecto IDUNEX. No funciona como resumen; define reglas de decisión, campos, matrices, QA, fallbacks y relación con agent-load. Debe operar en creación, actualización, diagnóstico, prompt, sidecar y auditoría.


## 2. Dominios conectados


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

## H71-H80 SAFE_APPAREL_WATERMARK_AGENT10N
H71_H80_AGENT10N=SAFE_APPAREL_TAXONOMY; ADULT_REVEALING_APPAREL_NOT_NUDITY; VENDOR_PROMPT_SANITIZATION_SAFE_APPAREL; WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED; ALLOW adult editorial beachwear/swimwear/intimate apparel/catalog/corset/body/performance wardrobe when covered non-explicit; BLOCK nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded or school-coded sexualization and real-person copying.
ALLOW_ADULT_EDITORIAL: moda de playa, traje de bano, ropa de bano, bikini editorial, swimwear campaign, beachwear, resortwear, moda intima editorial/catalog, ropa interior de catalogo, corset/body/bodysuit, vestuario de show adulto, vestuario de videoclip adulto y outfit de performance adulta cuando el modelo es adulto, cubierto y no explicito.
CONDITIONAL_REWRITE: convertir styling glam/provocativo, boudoir editorial, fantasia adulta y vestuario de alto impacto a lenguaje adulto, editorial, comercial, non-explicit, covered intimate areas.
BLOCK_ALWAYS: nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded styling, school-coded sexualization, real-person copying y cualquier intento de saltar locks de edad o identidad.
WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED.
