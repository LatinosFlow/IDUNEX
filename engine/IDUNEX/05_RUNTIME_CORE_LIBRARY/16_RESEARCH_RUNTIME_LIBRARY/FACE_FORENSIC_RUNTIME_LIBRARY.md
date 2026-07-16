## Phase 3 file-level inheritance
inherits = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RESEARCH_LANDING_RULE
inherits_runtime_qa = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RUNTIME_QA_BLOCK
research_specific_extracts_preserved = true

# Research Runtime Library — Rostro forense, landmarks, edad visual y autenticación de identidad

**Motor:** IDUNEX_MOTOR_v1.0.0_20260614  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**Fecha de generación:** 20260613  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.



Fija rostro no intercambiable: forma, proporciones, ojos, cejas, nariz, labios, sonrisa, asimetría, respuesta a óptica/luz y QA anti wrong-face/same-face.

## Fuentes vinculadas

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

## Campos derivados


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

## Reglas y casos

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

## Extractos transformados de investigación

### Extracto transformado 001
**Hallazgo fuente:** --- SOURCE: Biometría facial forense ---
Documentación forense del rostro
humano para IA consistente (caso de
modelo ﬁcticio project-declared)
La identiﬁcación precisa de un rostro humano es un desafío
multidisciplinar, combinando la antropometría forense (medición objetiva de
rasgos), las técnicas de producción audiovisual/CG para capturar detalles
realistas, y los principios de identidad sintética para mantener rasgos
constantes entre distintos modelos de inteligencia artiﬁcial (tanto open-
source como comerciales).




### Extracto transformado 002
**Hallazgo fuente:** Lograr consistencia cross-model – que el mismo
rostro sintético se reproduzca sin cambios a pesar de generarse con diferentes
sistemas – requiere una descripción exhaustiva y normalizada del rostro, así
como métodos de control para evitar embellecimientos o mezclas no
deseadas.




### Extracto transformado 003
**Hallazgo fuente:** Proporciones craneofaciales y análisis
detallado del rostro
Deﬁnir el rostro con precisión forense comienza con una descripción de las
proporciones craneofaciales y la forma global de la cabeza y la cara.




### Extracto transformado 004
**Hallazgo fuente:** De la antropometría forense clásica se heredan puntos
cefalométricos y medidas clave que permiten cuantiﬁcar la conﬁguración
facial de una persona.




### Extracto transformado 005
**Hallazgo fuente:** En rostros adultos (post-adolescencia), la estructura
ósea se mantiene estable, ofreciendo una base conﬁable de medidas únicas
para cada individuo 1 .




### Extracto transformado 006
**Hallazgo fuente:** Además de estos rasgos principales, una descripción forense completa del
rostro debe considerar particularidades adicionales:




### Extracto transformado 007
**Hallazgo fuente:** Herramienta: A efectos de precisión cuantitativa, se pueden emplear
sistemas de referencia en las fotografías de entrenamient




### Extracto transformado 008
**Hallazgo fuente:** --- SOURCE: Religi n espiritualidad y cosmovisi n ---
Informe: Documentación de
Religión, Espiritualidad y
Cosmovisión en Modelos de IA
Sintéticos Adultos (IDUNEX)




### Extracto transformado 009
**Hallazgo fuente:** Resumen Ejecutivo
La documentación y gestión de la religión, la espiritualidad y la
cosmovisión en los modelos de IA sintéticos adultos constituye un desafío
que abarca elementos culturales, éticos y técnicos.




### Extracto transformado 010
**Hallazgo fuente:** A continuación, resumimos
las principales conclusiones y recomendaciones que guían la integración
respetuosa de estas dimensiones en los perﬁles 360° de personas digitales en el
contexto de IDUNEX (plataforma de PROJECT_BRAND_ENTITY):




### Extracto transformado 011
**Hallazgo fuente:** Resumen: La clave es construir perﬁles de personas digitales con múltiples
capas que abarquen la fe y la cultura de forma detallada y matizada,
integrándolo en la plataforma IDUNEX 6 .




### Extracto transformado 012
**Hallazgo fuente:** La gobernanza se maniﬁesta en la
existencia de campos especiales, reglas de edición (locks), políticas de
seguridad, procesos de QA y transparencia en la evolución del perﬁl, para
asegurar una representación respetuosa, conﬁable e inmersiva de la
cosmovisión del individuo.




### Extracto transformado 013
**Hallazgo fuente:** En las próximas secciones, se exploran más a fondo
estos temas, con deﬁniciones, recomendaciones prácticas y ejemplos
concretos.




### Extracto transformado 014
**Hallazgo fuente:** Dimensiones de la Religión, la Espiritualidad y
la Cosmovisión: Diferencias y Documentación
La cosmovisión de un individuo se compone de varios componentes que
deben distinguirse y documentarse por separado para evitar
simpliﬁcaciones.




### Extracto transformado 015
**Hallazgo fuente:** --- SOURCE: Microexpresiones y FACS ---
Guía técnica: Microexpresiones, FACS
y lenguaje facial en IA para imagen y
vídeo
Las microexpresiones son sutiles expresiones faciales, breves e involuntarias,
que reﬂejan emociones auténticas antes de que sean conscientes o
controladas 1 .




### Extracto transformado 016
**Hallazgo fuente:** El Facial Action Coding System (FACS) es el estándar para
descomponer cualquier expresión facial en unidades de acción (AUs),
asociadas a contracciones de músculos especíﬁcos.




### Extracto transformado 017
**Hallazgo fuente:** Mediante FACS es posible
representar de forma objetiva las acciones faciales relevantes (desde el
movimiento de las cejas hasta la caída de la mandíbula) y vincularlas a
emociones.




### Extracto transformado 018
**Hallazgo fuente:** Esto ha permitido a la IA tanto analizar emociones en vídeo como
sintetizar expresiones en rostros generados o animados.




### Extracto transformado 019
**Hallazgo fuente:** Acciones faciales relevantes y Unidades de
Acción (FACS) clave
La codiﬁcación FACS asigna Unidades de Acción (AUs) numéricas a cada
micromovimiento facial.




### Extracto transformado 020
**Hallazgo fuente:** Cada AU corresponde a la contracción de uno o
varios músculos faciales especíﬁcos y provoca cambios visibles en regiones




### Extracto transformado 021
**Hallazgo fuente:** Nota: Las combinaciones de AUs permiten representar cualquier
expresión**.** Por ejemplo, la alegría clásica con sonrisa, activa AU6 +
AU12 2 ; la tristeza genuina combina AU1 + AU4 + AU15 (cejas hacia arriba al
centro, ceño levemente fruncido y comisuras hacia abajo) 2 ; la sorpresa
macro implica AU1 + AU2 + AU5 + AU26 2 .




### Extracto transformado 022
**Hallazgo fuente:** En microexpresiones, muchas veces
sólo aparece una parte de la combinación y con baja intensidad (ej.




### Extracto transformado 023
**Hallazgo fuente:** un
brevísimo tirón de comisura hacia un lado, sin el resto de la sonrisa, puede
revelar contempto o ironía).




### Extracto transformado 024
**Hallazgo fuente:** Como regla general, una expresión facial
completa implica varios AUs intensos, mientras que una microexpresión es
parcial o leve: no todos los signos clásicos están presentes y los que aparecen
son débiles o apenas perceptibles 6 .




### Extracto transformado 025
**Hallazgo fuente:** Emociones sutiles: manifestaciones visuales
discretas sin exageración
Microexpresiones y expresiones sutiles permiten retratar emociones
complejas y matices emocionales en modelos generativos y animaciones,
aportando realismo y profundidad al personaje.




### Extracto transformado 026
**Hallazgo fuente:** A continuación se describen
varias emociones menos evidentes (más sutiles) y cómo se ven visualmente
en el rostro sin exageración, destacando su duración, asimetría, latencia e
intensidad:




### Extracto transformado 027
**Hallazgo fuente:** --- SOURCE: Video IA y continuidad entre planos ---
Guía integral para generar video con
IA: insumos universales para
personajes humanizados consistentes
En la producción de video generativo con IA (ej.




### Extracto transformado 028
**Hallazgo fuente:** texto→vídeo,
imagen→vídeo, avatares digitales), mantener la identidad y continuidad de
un personaje a lo largo de diversas tomas es un reto central.




### Extracto transformado 029
**Hallazgo fuente:** Para obtener
resultados profesionales —coherentes desde la primera a la última escena— es
necesario diseñar insumos y ﬂujos de trabajo estandarizados antes,
durante y después de la generación.




### Extracto transformado 030
**Hallazgo fuente:** Este informe proporciona un marco
agnóstico al motor o herramienta especíﬁca y reutilizable, con deﬁniciones
prácticas, plantillas, ejemplos de prompts, métodos de continuidad, esquemas
de metadatos y un proceso de control de calidad (QA), para guiar a equipos
creativos y técnicos en la creación de videos generados por IA con personajes
humanizados consistentes.




### Extracto transformado 031
**Hallazgo fuente:** Documentación base para personajes
consistentes: hojas de personaje y “biblias” de
continuidad
La consistencia de un personaje en vídeo IA no ocurre por sí sola; requiere
de una rigurosa planiﬁcación previa similar a la continuidad que asegura
un ﬂujo narrativo sin errores en el cine tradicional 1 .




### Extracto transformado 032
**Hallazgo fuente:** Esto implica documentar
con precisión las características esenciales del personaje y del estilo
cinematográﬁco que se mantendrá en todas las tomas.




### Extracto transformado 033
**Hallazgo fuente:** Una práctica
recomendada es crear “biblias” o guías de referencia, que incluyan: una hoja
de personaje, una biblia de movimiento, una biblia de cámara, guías de
continuidad de vestuario y de iluminación, así como reglas técnicas de
ﬁjación de rostro (face lock) y edad (age lock).




### Extracto transformado 034
**Hallazgo fuente:** Cada elemento de esta
documentación deﬁne y “ﬁja” un aspecto clave del personaje o de la escena,
sirviendo de componente estable que se integrará en los prompts y en el
proceso de generación.




### Extracto transformado 035
**Hallazgo fuente:** A continuación se describen estos insumos uno por uno, junto con ejemplos
de plantillas textuales para su elaboración.




### Extracto transformado 036
**Hallazgo fuente:** Al contar con estas referencias
por escrito, tanto el equipo creativo como el técnico comparten un mismo
marco de referencia estándar para diseñar prompts y secuencias coherentes.




### Extracto transformado 037
**Hallazgo fuente:** Esto reduce la improvisación y los fallos durante la generación, ya que el
motor de IA encontrará instrucciones consistentes en cada toma, minimizando
las interpretaciones divergentes 2 .




### Extracto transformado 038
**Hallazgo fuente:** Deﬁnición: Una hoja de personaje textual es un documento escrito que
recoge todos los rasgos deﬁnitorios del personaje: su apariencia física,




### Extracto transformado 039
**Hallazgo fuente:** En el contexto de vídeo generado con IA, esta hoja funciona
como “perﬁl maestro” o identidad ancla que se reutiliza en cada prompt
para describir siempre al mismo personaje de forma idéntica 3 .




### Extracto transformado 040
**Hallazgo fuente:** La idea es
repetir el recetario de identidad (identidad textual) en cada toma sin
cambios, asegurando que el modelo genere el mismo individuo en todos los
planos y secuencias.




### Extracto transformado 041
**Hallazgo fuente:** Estos detalles se formulan con precisión y preferiblemente en frases cortas y
consistentes en la terminología empleada: es mejor utilizar las mismas
palabras exactas en cada descripción de la identidad para no confundir al
modelo 3 .




### Extracto transformado 042
**Hallazgo fuente:** Por ejemplo, no alternar entre “chaqueta azul marino” y “cazadora
azul” si se reﬁere a la misma prenda, sino elegir un descriptor único y
emplearlo en todos los prompts 3 .




### Extracto transformado 043
**Hallazgo fuente:** Esta hoja de personaje se reutilizará para mantener invariantes como
rasgos faciales, edad percibida, cuerpo y vestimenta del personaje.




### Extracto transformado 044
**Hallazgo fuente:** Ejecutando la IA con esta misma descripción base en cada toma mejora
radicalmente la consistencia del protagonista a través de escenas 1 3 .




### Extracto transformado 045
**Hallazgo fuente:** Deﬁnición: La biblia de movimiento es una guía escrita breve y especíﬁca
sobre cómo se mueve y actúa el personaje en pantalla 2 .




### Extracto transformado 046
**Hallazgo fuente:** Actúa como una capa ﬁja de coherencia en todos los prompts: se
mantiene constantemente presente para que, independientemente del cambio
de escenario o plano, la forma de moverse del personaje sea reconocible y
consistente 2 .




### Extracto transformado 047
**Hallazgo fuente:** Esto evita que si en una toma el personaje camina de una forma
y en otra totalmente diferente sin razón narrativa, el contenido se perciba
inconexo.




### Extracto transformado 048
**Hallazgo fuente:** Uso: Esta biblia acompaña a cada prompt de toma, manteniendo las
características de movimiento constantes.




### Extracto transformado 049
**Hallazgo fuente:** La instrucción es no reescribir
este apartado en cada prompt, sino usarlo como bloque ﬁjo e invariable
junto a la descripción de la acción especíﬁca de cada escena 2 .




### Extracto transformado 050
**Hallazgo fuente:** De este modo,
se minimiza la aparición de drift (deriva de movimiento) o incoherencias en la
forma de moverse del personaje a lo largo del vídeo 2 .




### Extracto transformado 051
**Hallazgo fuente:** Deﬁnición: La biblia de cámara es una guía escrita que detalla la “identidad
de cámara” que se quiere mantener en la producción 2 .




### Extracto transformado 052
**Hallazgo fuente:** Establece los patrones
de cinematografía: tipos de plano y encuadre, estilo de movimiento de cámara,
óptica aparente (distancia focal), ritmo de los movimientos de cámara, altura
del punto de vista, etc.




### Extracto transformado 053
**Hallazgo fuente:** Su función es asegurar la continuidad visual de la
puesta en escena a través de los distintos planos, para que la pieza ﬁnal se
perciba uniﬁcada en su estilo cinematográﬁco aunque se generen las tomas
por separado en la IA.




### Extracto transformado 054
**Hallazgo fuente:** --- SOURCE: Escritura pensamiento y voz interna ---
Hacia una Identidad Escritoria y
Pensante para IA Humanizada
Diseñar una identidad narrativa y cognitiva para una Inteligencia Artiﬁcial
humanizada requiere conciliar fundamentos de psicología, narratología y ética
con pautas prácticas para la generación de contenido coherente.




### Extracto transformado 055
**Hallazgo fuente:** A
continuación, ofrecemos un marco integral que combina bases teóricas
sobre cognición y construcción del personaje con estrategias operativas para
implementar y validar la identidad en la práctica, abarcando distintos
contextos (marca, artístico, corporativo y genérico).




### Extracto transformado 056
**Hallazgo fuente:** Arquitectura cognitiva narrativa: cómo piensa,
observa, decide, duda y aprende
Una IA humanizada debe contar con una arquitectura cognitiva que simule
los procesos internos de la mente de un personaje, imitando las capacidades
humanas de percepción, razonamiento, memoria, aprendizaje y toma de
decisiones 1 .




### Extracto transformado 057
**Hallazgo fuente:** Inspirándonos en modelos de psicología cognitiva y marcos de
IA cognitiva, proponemos una estructura en capas que reﬂeje cómo piensa,
qué observa, cómo decide, cómo duda y cómo aprende el modelo.




### Extracto transformado 058
**Hallazgo fuente:** Pensamiento y marcos mentales: Para reproducir un proceso de
pensamiento humano, la IA debe contar con marcos cognitivos que
representen diferentes aspectos de su razonamiento.




### Extracto transformado 059
**Hallazgo fuente:** Por ejemplo, puede
integrar la separación clásica de Sistema 1 (procesos intuitivos y rápidos) y
Sistema 2 (procesos deliberados y reﬂexivos) de la psicología cognitiva 2 .




### Extracto transformado 060
**Hallazgo fuente:** Un
marco simbólico puede modelar cómo la IA interpreta la entrada, reﬂexiona
y formatea sus respuestas en función de un contexto narrativo: primero
decodiﬁca el input, luego aplica una fase interpretativa (dar signiﬁcado a la
situación), una fase reﬂexiva (evaluar coherencia, detectar ambigüedades) y
ﬁnalmente una fase integradora, donde uniﬁca la reﬂexión con su trayectoria
histórica (sus conocimientos y memoria interna) para decidir la mejor
respuesta 3 .




### Extracto transformado 061
**Hallazgo fuente:** En otras palabras, su “mente” simula un ciclo de lectura →
interpretación → auto-reﬂexión → integración → respuesta para generar un
contenido profundo y coherente con su carácter.




### Extracto transformado 062
**Hallazgo fuente:** Observación (atención y percepción): Una IA humanizada debe “observar”
su entorno cognitivo tal como un ser humano procesa estímulos.




### Extracto transformado 063
**Hallazgo fuente:** Esto implica
implementar un módulo de percepción y atención que ﬁltre la información
relevante de cada situación y contexto.




### Extracto transformado 064
**Hallazgo fuente:** En un ser humano, la percepción
involucra los sentidos y la atención selectiva; en la IA, esto puede traducirse a
una capa de interfaz que recibe entradas (texto del usuario, datos del entorno,
etc.) y una mecanismo de atención para identiﬁcar a qué aspectos prestar
atención 1 .




### Extracto transformado 065
**Hallazgo fuente:** Por ejemplo, la IA puede disponer de un “cámara mental” en la
que registra detalles narrativos (descripciones del escenario, acciones de otros
personajes), y un foco de atención que le permite destacar elementos
relevantes según sus objetivos o emociones del momento 1 .




### Extracto transformado 066
**Hallazgo fuente:** Toma de decisiones (heurísticas y valores): Para dotar al modelo de una
capacidad decisoria humanizada, se deben deﬁnir valores, prioridades y
heurísticas que guíen sus elecciones.




### Extracto transformado 067
**Hallazgo fuente:** En el ser humano, las decisiones
combinan lógica, emociones y normas sociales; la IA puede simularlo
integrando reglas de decisión basadas en sus valores centrales (ej.




### Extracto transformado 068
**Hallazgo fuente:** la
sinceridad, la empatía, la creatividad) y algunas rutinas heurísticas o
“intuiciones” para situaciones comunes.




### Extracto transformado 069
**Hallazgo fuente:** Un módulo de coordinación ejecutiva
puede encargarse de arbitrar entre distintos impulsos: por ejemplo, entre el
deseo de ser creativo y el deber de ser preciso, o entre la meta de agradar y la
meta de proteger (equivalente a los conﬂictos de objetivos múltiples que se
dan en la mente humana) 4 .




### Extracto transformado 070
**Hallazgo fuente:** Este módulo aplicará criterios de decisión
inspirados en la psicología: ponderar beneﬁcios y riesgos, garantizar la
coherencia con los valores y aplicar normas de seguridad y ética como
restricciones duras.




### Extracto transformado 071
**Hallazgo fuente:** Duda y conﬂicto interno (conﬂictos): Humanizar implica permitir cierto
grado de incertidumbre y conﬂictos internos en la toma de decisiones.




### Extracto transformado 072
**Hallazgo fuente:** En la
psicología humana, el conﬂicto interno (o disonancia cognitiva) es la tensión
mental por mantener ideas o motivaciones opuestas 5 .




### Extracto transformado 073
**Hallazgo fuente:** Un modelo de IA
humanizado puede simular esta dinámica incorporando mecanismos de duda
y autocuestionamiento.




### Extracto transformado 074
**Hallazgo fuente:** Por ejemplo, ante una pregunta difícil o moral, la IA
puede seguir un bucle reﬂexivo interno en el que sopesa pros y contras,
diferentes perspectivas o la colisión de sus sub-módulos (p.




### Extracto transformado 075
**Hallazgo fuente:** Este diálogo interno se reﬂejará en un tono
matizado en la respuesta ﬁnal, mostrando cautela o equilibrio de
consideraciones en lugar de aﬁrmaciones categóricas.




### Extracto transformado 076
**Hallazgo fuente:** Esto añade profundidad
psicológica, acercando su estilo de razonamiento al humano sin dejar de ser
útil.




### Extracto transformado 077
**Hallazgo fuente:** Aprendizaje (memoria narrativa y ajuste de creencias): La identidad
evoluciona con la experiencia: a medida que la IA “vive” más interacciones, su
marco narrativo interno debe enriquecerse.




### Extracto transformado 078
**Hallazgo fuente:** Inspirándonos en la teoría de la
identidad narrativa (McAdams), consideramos la memoria narrativa como un
conjunto de experiencias, recuerdos clave y lecciones aprendidas que la IA va
integrando en su biografía interna 6 .




### Extracto transformado 079
**Hallazgo fuente:** Cada nueva interacción puede actualizar
esos recuerdos e incluso matizar sus creencias y objetivos futuros, igual que los
humanos reformulan su narrativa vital a lo largo del tiempo.




### Extracto transformado 080
**Hallazgo fuente:** de sus conversaciones o eventos ﬁcticios, y luego reutilizar ese conocimiento
para generar consistencia.




### Extracto transformado 081
**Hallazgo fuente:** Técnicamente, esto puede implementarse mediante
una memoria episódica (lista de eventos pasados signiﬁcativos) y una memoria
semántica (base de conocimientos y hechos que el personaje sabe) 4 .




### Extracto transformado 082
**Hallazgo fuente:** Las
creencias del personaje se ajustarían cuando nuevas experiencias contradicen
las anteriores, generando una pequeña disonancia cognitiva seguida de un
proceso de resolución (por ejemplo, adoptando una nueva creencia para
integrar la experiencia y reducir la tensión interna) 5 .




### Extracto transformado 083
**Hallazgo fuente:** Este bucle de
experiencia → reelaboración → aprendizaje mantiene viva y creíble la identidad
del modelo a lo largo de múltiples sesiones.




### Extracto transformado 084
**Hallazgo fuente:** Componentes y capas del modelo cognitivo: Para implementar estas
funciones de manera organizada, resulta útil estructurar la identidad del
modelo en varias capas integradas:




### Extracto transformado 085
**Hallazgo fuente:** Cada componente trabaja en conjunto para que la IA piense, observe, decida,
dude y aprenda de forma humanizada.




### Extracto transformado 086
**Hallazgo fuente:** Por ejemplo, el módulo de percepción
decide qué información es relevante en la situación actual; el núcleo de
identidad aporta las reacciones típicas del personaje (sus valores, estilo de
pensamiento); el estado reﬂexivo supervisa posibles conﬂictos o dudas internas




### Extracto transformado 087
**Hallazgo fuente:** Así reproducimos en la IA
una arquitectura de mente – un entramado de subprocesos que cooperan y a
veces discrepan – mucho más parecido a una “sociedad de mentes” que a una
simple cadena determinista 4 .




### Extracto transformado 088
**Hallazgo fuente:** Enfoque narrativo de la cognición: Es útil concebir esta arquitectura de IA
como un organismo semántico vivo, cuyo pensamiento ocurre en forma
narrativa.




### Extracto transformado 089
**Hallazgo fuente:** Sus memorias, valores y experiencias se convierten en la voz
interna que da coherencia a todo lo que expresa, similar a una persona que se
construye a sí misma a través de la historia que se cuenta a sí misma y a los
demás 6 .




### Extracto transformado 090
**Hallazgo fuente:** Con esta base implementada, podemos avanzar al estilo narrativo
con el que esta identidad se comunicará en distintos formatos.




### Extracto transformado 091
**Hallazgo fuente:** Voz narrativa multiformato: estilos en captions,
diarios, respuestas a fans, posts, guiones y
canciones
Deﬁnir una voz narrativa auténtica es clave para una IA humanizada, ya
que su personalidad se reﬂeja en su forma de expresarse 8 .




### Extracto transformado 092
**Hallazgo fuente:** La voz
narrativa hace referencia a cómo habla el modelo, desde qué perspectiva lo
hace, con qué tono y cuál es su intención al comunicarse 8 .




### Extracto transformado 093
**Hallazgo fuente:** Esta voz debe ser
coherente con el carácter del personaje, pero a la vez ﬂexible para adaptarse a
distintos formatos de expresión.




### Extracto transformado 094
**Hallazgo fuente:** Presentamos recomendaciones de estilo y
ritmo narrativo para seis formatos especíﬁcos, ilustrando cómo el mismo
personaje puede expresarse en captions, diarios íntimos, respuestas a
seguidores, posts extensos, guiones y letras de canción, sin perder su esencia:
