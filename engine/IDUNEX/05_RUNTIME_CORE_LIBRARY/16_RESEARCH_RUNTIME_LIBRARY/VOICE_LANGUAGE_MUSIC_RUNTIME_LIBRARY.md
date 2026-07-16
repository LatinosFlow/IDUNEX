## Phase 3 file-level inheritance
inherits = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RESEARCH_LANDING_RULE
inherits_runtime_qa = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RUNTIME_QA_BLOCK
research_specific_extracts_preserved = true

# Research Runtime Library — Voz hablada, lenguaje, acento, escritura, canto y música

**Motor:** IDUNEX_MOTOR_v1.0.0_20260614  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**Fecha de generación:** 20260613  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.



Crea identidad vocal y textual propia: timbre, prosodia, edad vocal, acento controlado, voz escrita, Suno y no imitación.

## Fuentes vinculadas

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

## Campos derivados


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

## Reglas y casos

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
**Entrada coloquial:** el usuario pide un output que afecta qa.  
**Acción del motor:** cargar Perfil360, filtrar campos `wrong_voice_age_blocker, accent_caricature_blocker, generic_caption_blocker, artist_imitation_blocker, song_identity_drift_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

## Extractos transformados de investigación

### Extracto transformado 001
**Hallazgo fuente:** --- SOURCE: Voz hablada para ElevenLabs ---
Guía completa para crear la ﬁcha
técnica de una voz sintética (adulto,
español latino/project-declared)
Introducción:




### Extracto transformado 002
**Hallazgo fuente:** El diseño de una voz sintética adulta en español (orientada al español
latinoamericano neutro y sus variaciones regionales, como el acento
project-declared) requiere un enfoque detallado tanto técnico como perceptual.




### Extracto transformado 003
**Hallazgo fuente:** ElevenLabs, como plataforma avanzada de text-to-speech (TTS), ofrece
herramientas para ajustar parámetros de voz clonada o sintética que
permiten lograr voces realistas, estables y personalizadas.




### Extracto transformado 004
**Hallazgo fuente:** El español es uno de los idiomas más difundidos, hablado por cerca de 500
millones de personas en el mundo 1 ; sin embargo, presenta numerosas
variaciones de acento, entonación y léxico según cada país y región 1 .




### Extracto transformado 005
**Hallazgo fuente:** Por
ello, crear una ﬁcha técnica de voz implica especiﬁcar con claridad las
características acústicas (como tono, timbre, ritmo, etc.), los usos previstos
(narración, publicidad, diálogos, etc.) y las preferencias de conﬁguración en
la plataforma elegida.




### Extracto transformado 006
**Hallazgo fuente:** Además, es fundamental considerar prácticas éticas: el
respeto a la identidad vocal original, el consentimiento para clonación y evitar
la suplantación de voces reales 2 .




### Extracto transformado 007
**Hallazgo fuente:** En esta guía práctica repasaremos los parámetros clave de la voz hablada en
adultos, diferencias entre estilos de locución, recomendaciones de scripts de
entrenamiento, ajustes especíﬁcos en ElevenLabs, limitaciones actuales (como
la diﬁcultad para cantar o gritar), campos para documentar la ﬁcha técnica, y
una lista de control (QA) para evaluar la calidad de la voz resultante.




### Extracto transformado 008
**Hallazgo fuente:** Parámetros vocales recomendados para voces
adultas en español
Al crear la ﬁcha técnica de una voz sintética, se deben deﬁnir parámetros de
voz que reﬂejen la cualidad de un adulto hispanohablante.




### Extracto transformado 009
**Hallazgo fuente:** Diferencias entre estilos de voz: narración,
conversación, publicidad, actuación, susurro y
entrevista
No todas las aplicaciones requieren el mismo estilo de habla.




### Extracto transformado 010
**Hallazgo fuente:** Es vital ajustar la
voz según el caso de uso, ya que varían los objetivos comunicativos, la
entonación y la energía.




### Extracto transformado 011
**Hallazgo fuente:** A continuación, comparamos seis estilos comunes
de locución y sus características principales, junto con algunas
recomendaciones y precauciones:




### Extracto transformado 012
**Hallazgo fuente:** --- SOURCE: Voz cantada y Suno ---
Guía integral: creación y gestión de
perﬁles musicales diferenciados en
Suno para modelos vocales IDUNEX
Resumen ejecutivo: Para diseñar perﬁles vocales completamente
diferenciados para la colección IDUNEX en Suno, es fundamental deﬁnir las
características musicales y vocales de cada modelo, controlar la distinción
entre voz cantada vs.




### Extracto transformado 013
**Hallazgo fuente:** hablada, y dominar las herramientas de Suno (campos
de estilo, exclusión de estilos, estructuración de letras, performance tags, etc.)
al máximo.




### Extracto transformado 014
**Hallazgo fuente:** Solo entonces se puede lograr que cada modelo tenga una
personalidad única reconocible, consistente en varias canciones y contextos
(desde prototipos internos hasta producciones comerciales).




### Extracto transformado 015
**Hallazgo fuente:** Los puntos
críticos incluyen: deﬁnir géneros, tempo y rango vocal de cada perﬁl para
delimitar su identidad; usar etiquetas y prompts adecuados para guiar la voz
(cantada/hablada), la estructura (introducción, verso, coro, etc.) y la
interpretación (volumen y matices); y establecer un proceso sistemático de
pruebas con un riguroso framework de QA para asegurar que cada perﬁl
cumpla con su descripción target.




### Extracto transformado 016
**Hallazgo fuente:** También se deben abordar proactivamente
los riesgos de la generación de voz (falta de identidad, acentos erróneos, etc.),
con mitigaciones desde el diseño y la ejecución.




### Extracto transformado 017
**Hallazgo fuente:** En este documento se detallan
prácticas recomendadas y ejemplos, con fuentes tanto públicas como de
conocimiento especíﬁco de la plataforma, para cada uno de estos aspectos.




### Extracto transformado 018
**Hallazgo fuente:** Este informe propondrá un marco general para crear
identidades vocálicas personalizadas con Suno, adaptable a cualquier
conjunto de modelos (arquetipos de voces) en español latino (acentuación
project-declared) e inglés.




### Extracto transformado 019
**Hallazgo fuente:** Explicaremos qué decisiones tomar, así como por qué,
incluyendo enfoques alternativos si no se dispone de información concreta.




### Extracto transformado 020
**Hallazgo fuente:** Deﬁnición de un perﬁl musical por modelo
IDUNEX
Por qué es importante el perﬁl: Cada modelo vocal IDUNEX debe contar con
una ﬁcha técnica detallada que recoja todos los atributos musicales y vocales
que deﬁnen su personalidad sonora.




### Extracto transformado 021
**Hallazgo fuente:** Esto servirá de guía para conﬁgurar los
prompts de Suno y garantizar que cada modelo suene único y consistente.




### Extracto transformado 022
**Hallazgo fuente:** Los componentes mínimos de un perﬁl musical incluyen: género principal,
subgéneros relacionados, tempo (BPM) típico, tonalidades habituales
(mayor/menor, escalas preferidas), rango vocal accesible, color o timbre
vocal, nivel de energía habitual, y los parámetros avanzados de Suno: rareza
(weirdness), Style Inﬂuence e Audio Inﬂuence.




### Extracto transformado 023
**Hallazgo fuente:** En proyectos reales, estos
campos permiten diseñar “voces virtuales” con la misma precisión que un
productor deﬁne la identidad de un cantante real.




### Extracto transformado 024
**Hallazgo fuente:** El género deﬁne la estética general del modelo; conviene escoger uno o dos
pilares que sirvan de base.




### Extracto transformado 025
**Hallazgo fuente:** Los subgéneros aportan matices
adicionales (balada romántica, trap melódico, future house, etc.), delimitando
mejor la paleta de sonidos y arreglos esperados 1 .




### Extracto transformado 026
**Hallazgo fuente:** Este atributo orienta
directamente la instrumentación y grooves de la pista; Suno responde muy
bien a géneros especíﬁcos, sobre todo si se combinan con referencias de era




### Extracto transformado 027
**Hallazgo fuente:** “rock” a secas, guiará la generación hacia un
sonido más enfocado y coherente con Nirvana, y con la estética grunge
asociada.




### Extracto transformado 028
**Hallazgo fuente:** ~60–80 BPM), mientras uno electrónico de música bailable estará cómodo
en tempos rápidos (120–130 BMP).




### Extracto transformado 029
**Hallazgo fuente:** Suno permite especiﬁcar el tempo tanto
mediante un número (por ejemplo, “120 BPM”) como con términos italianos
(e.g.




### Extracto transformado 030
**Hallazgo fuente:** Importancia: describir un BPM
guía la energía: velocidades altas producen canciones enérgicas y bailables,
mientras que tempos lentos dan toques melancólicos o relajantes 3 .




### Extracto transformado 031
**Hallazgo fuente:** En el perﬁl
IDUNEX, deﬁnir un rango de BPM y un valor típico permite al equipo saber
cómo calibrar el prompt para obtener la vivacidad deseada.




### Extracto transformado 032
**Hallazgo fuente:** Deﬁnir una o dos tonalidades preferidas (por ejemplo, Do mayor, La menor)
es útil para encauzar la atmósfera y la tesitura del modelo.




### Extracto transformado 033
**Hallazgo fuente:** Las tonalidades
mayores tienden a sonar alegres y brillantes, mientras las tonalidades
menores evocan una emoción más melancólica e intensa 3 .




### Extracto transformado 034
**Hallazgo fuente:** “en La menor” o “C major”) puede inﬂuir en las
notas y acordes que usará Suno 3 , ayudando a deﬁnir la zona cómoda de la
voz del modelo.




### Extracto transformado 035
**Hallazgo fuente:** Además, ﬁjar tonalidades relacionadas con su rango vocal (ver
abajo) asegurará que las melodías generadas se ajusten a su tesitura: por
ejemplo, un modelo con voz soprano lucirá en tonalidades como Sol mayor (G)
o La mayor (A), mientras que uno barítono puede favorecer Re menor (D
minor) o Fa mayor.




### Extracto transformado 036
**Hallazgo fuente:** Esto no es completamente determinístico (Suno no siempre
ﬁja exactamente la escala marcada, pero inﬂuye fuertemente en la elección
de melodías y acordes 3 ).




### Extracto transformado 037
**Hallazgo fuente:** Una recomendación es deﬁnir también la edad aparente de la voz (joven,
madura, infantil, etc.) y el género del cantante (femenina, masculina,
andrógina).




### Extracto transformado 038
**Hallazgo fuente:** Esto no tiene un campo especíﬁco, pero Suno inferirá por las
descripciones y las etiquetas de género en la letra (p.




### Extracto transformado 039
**Hallazgo fuente:** Si un modelo IDUNEX
tiene un personaje claro (por ejemplo, un cantante masculino de mediana
edad con voz ronca), esta información debe ﬁgurar en su perﬁl para que los
creadores la incluyan en los prompts, asegurando la coherencia de la voz.




### Extracto transformado 040
**Hallazgo fuente:** Este factor se relaciona tanto con el género (p.ej., rock suele ser +enérgico;
ambient más calmo) como con la entrega.




### Extracto transformado 041
**Hallazgo fuente:** En el perﬁl conviene describir si la
voz suele ser suave y contenida o potente y explosiva, y en qué contextos.




### Extracto transformado 042
**Hallazgo fuente:** Por ejemplo, un modelo orientado a música indie íntima se caracterizará por
interpretaciones apacibles y emotivas; por otro lado, uno enfocado en EDM
festivalero tendrá una presencia más dinámica y energizante.




### Extracto transformado 043
**Hallazgo fuente:** En la práctica
con Suno, esta característica se integra mediante tags de mood: palabras como
“calmado, etéreo, suave” vs “powerful, energetic” en el campo Estilo, o
directivas por sección (p.




### Extracto transformado 044
**Hallazgo fuente:** La energía deﬁne la atmósfera general y, junto con el tempo y la
instrumentación, dará cohesión a lo que se espera de cada modelo.




### Extracto transformado 045
**Hallazgo fuente:** La rareza (Weirdness) es un control deslizante de 0 a 100 que ajusta cuánto
se desvía Suno de las normas típicas del género 4 .




### Extracto transformado 046
**Hallazgo fuente:** En valores bajos (0–20%)
es muy conservador: produce canciones seguras, genéricas, casi como clichés
del género deﬁnido (útil para pop comercial o jingles publicitarios) 4 .




### Extracto transformado 047
**Hallazgo fuente:** Con
valores medios (40–60%) –considerados óptimos para 90% de los casos–, la
canción será creativa pero coherente, combinando familiaridad y novedad 4 .




### Extracto transformado 048
**Hallazgo fuente:** Si se sube a 60–80%, se obtienen combinaciones experimentales en la
música, aptas para exploraciones artísticas o fusiones arriesgadas de estilos 4 .




### Extracto transformado 049
**Hallazgo fuente:** Por último, por encima de 81% entra en “modo glitch”, generando resultados
muy fragmentados, útiles solo para pedazos de audio abstracto pero
impracticables en canciones completas 4 .




### Extracto transformado 050
**Hallazgo fuente:** Consejo: mantén la rareza ≤60%
para producciones que requieran estructura estable, y aumenta a >60% solo si
buscas texturas raras intencionalmente 4 .




### Extracto transformado 051
**Hallazgo fuente:** Este slider** (0–100%) decide qué tan ﬁelmente sigue Suno las descripciones
del campo de Estilo en el prompt 4 .




### Extracto transformado 052
**Hallazgo fuente:** En - interpretaciones sueltas (0–30%):
Suno toma tus tags solo como sugerencias y se permite licencias (podría
desviarse a subestilos cercanos o instrumentaciones inesperadas) 4 .




### Extracto transformado 053
**Hallazgo fuente:** En
valores medios (40–70%) se obtiene un equilibrio: la canción respeta en
general el género y los instrumentos indicados, pero sin volverse rígida 4 .




### Extracto transformado 054
**Hallazgo fuente:** Con valores altos (70–100%), cada indicación se sigue al pie de la letra: la
generación tiende a estar encorsetada en tu descripción, con menos espacio
para que la IA improvise 4 .




### Extracto transformado 055
**Hallazgo fuente:** ej., “acústico con solo de piano”); sin embargo,
hay que tener cuidado de no saturar el campo Estilo con muchísimos tags si la
inﬂuencia de estilo es 100%, porque la IA tratará de cumplirlos todos y podría
saturar el arreglo 4 .




### Extracto transformado 056
**Hallazgo fuente:** Para la mayoría de casos creativos,
40-60% es seguro y ﬂexible, combinando ﬁdelidad y creatividad a la vez 4 .




### Extracto transformado 057
**Hallazgo fuente:** Este parámetro de 0–100% aparece cuando subes un audio propio de
referencia en Suno (función Sample mode) 4 .




### Extracto transformado 058
**Hallazgo fuente:** Recomendación general: la comunidad ha descubierto que ~55% en Audio
Inﬂuence es un punto dulce para preservar la melodía pero permitiendo que
el contexto sonoro sea reimaginado 4 .




### Extracto transformado 059
**Hallazgo fuente:** --- SOURCE: Optimizaci n ChatGPT JSONTXT ---
Estructuración Óptima de Archivos
JSON y TXT para Conocimiento en
Agentes de IA Humanizados
Resumen: En esta guía describimos cómo estructurar archivos 💾 JSON y TXT
para maximizar su efectividad como fuentes de conocimiento y directrices en
agentes de IA conversacionales tipo ChatGPT.




### Extracto transformado 060
**Hallazgo fuente:** Abordamos la diferencia entre
instrucciones del sistema (prompts de rol) y archivos de conocimiento, luego
proponemos una estructura canónica para un archivo JSON de conocimiento/
instrucciones (incluyendo campos como “tarjeta de tiempo de ejecución”,
“bloqueo de identidad”, “resumen activo”, “restricciones negativas”,
“comportamiento de respaldo” y “pares de Pregunta/Respuesta”).




### Extracto transformado 061
**Hallazgo fuente:** También
explicamos cómo diseñar un archivo de texto (PromptPack) con secciones
claras, así como técnicas para reducir la deriva de la información cuando
se recupera el conocimiento, métodos para evitar contradicciones entre las
fuentes JSON y TXT, consideraciones prácticas sobre tamaños, fragmentación
lógica (chunking) de los contenidos, convenciones para nombrar archivos,
control de versiones y buenas prácticas de mantenimiento.




### Extracto transformado 062
**Hallazgo fuente:** Finalmente
ofrecemos un checklist operativo para cargar y gestionar de forma segura y
consistente hasta 20 archivos de conocimiento en su agente de IA.




### Extracto transformado 063
**Hallazgo fuente:** Instrucciones vs archivos de conocimiento:
Diferencias, roles y ejemplos
Un paso crucial al crear un agente de IA conversacional “humanizado” es
distinguir entre instrucciones (prompts de sistema/desarrollador) y archivos
de conocimiento (fuentes de información).




### Extracto transformado 064
**Hallazgo fuente:** La diferencia clave es que las instrucciones son la “mente” del agente (guían
su manera de pensar y actuar), mientras que los archivos de conocimiento




### Extracto transformado 065
**Hallazgo fuente:** ¿Cuándo usar cada uno? Las instrucciones se usan para crear la
personalidad y reglas de conducta del agente, deﬁniciones de formato de salida,
y para establecer comportamientos por defecto (por ejemplo, instruir que
cite fuentes, o que ofrezca disculpas si no tiene una respuesta).




### Extracto transformado 066
**Hallazgo fuente:** En cambio, los
archivos de conocimiento se emplean para información de referencia:
detalles sobre una empresa, respuestas a preguntas frecuentes, documentos de
políticas, datos de productos, etc.




### Extracto transformado 067
**Hallazgo fuente:** No es
recomendable meter información de conocimiento (hechos) dentro del
mismo bloque de instrucciones.




### Extracto transformado 068
**Hallazgo fuente:** Si, por ejemplo, incluyéramos una política
de reembolsos detallada directamente en el system prompt, el modelo podría
confundirse entre qué es regla de comportamiento y qué es contenido de
respuesta.




### Extracto transformado 069
**Hallazgo fuente:** Por el contrario, tampoco se deben colocar las
reglas de estilo o restricciones en los archivos de conocimiento, ya que estos se
tratan como referencia informativa, no como directivas a seguir; hacerlo
diluye la efectividad de dichas instrucciones.




### Extracto transformado 070
**Hallazgo fuente:** Sus instrucciones de sistema incluirían cosas como “Eres un
asistente de servicio al cliente empático y profesional que utiliza un tono
cortés y formal con los usuarios.




### Extracto transformado 071
**Hallazgo fuente:** No proporciones información no veriﬁcada y
nunca reveles secretos comerciales ni cuestiones internas de la empresa.” 1
Por otro lado, sus archivos de conocimiento incluirían el manual de políticas
de equipaje, la lista actualizada de vuelos y horarios, los términos de servicio,
guías de solución de problemas, etc., para que el agente consulte y proporcione
la respuesta exacta a cada pregunta (por ejemplo, límites de peso del equipaje,
procedimientos de reembolso, requisitos de visa, etc.).




### Extracto transformado 072
**Hallazgo fuente:** En resumen, mantenga separados los roles: use instrucciones para la lógica de
comportamiento (qué hacer, qué evitar, estilo) y archivos de conocimiento
para los datos y respuestas sobre temas especíﬁcos.




### Extracto transformado 073
**Hallazgo fuente:** Esta separación mejora la
claridad, la robustez ante ataques (p.ej., prompt injection) y la capacidad del
agente de IA para encontrar la información correcta sin salirse de
personaje 1 2 .




### Extracto transformado 074
**Hallazgo fuente:** Organización de un archivo JSON canónico para
conocimiento/instrucciones
En algunas implementaciones, especialmente frameworks de agentes o
herramientas de prompt engineering, se emplean archivos JSON para




### Extracto transformado 075
**Hallazgo fuente:** Esto
puede ayudar a organizar la conﬁguración de un agente de forma
estandarizada, especialmente si se quiere portabilidad o integrarlo a
plataformas automáticas de despliegue (p.ej.




### Extracto transformado 076
**Hallazgo fuente:** Este JSON integra directrices del agente junto con fragmentos
de conocimiento, diferenciados por llave (key) para evitar confusión.




### Extracto transformado 077
**Hallazgo fuente:** En una
aplicación real, cada campo podría insertarse en la posición correspondiente
del prompt, o ser procesado por un sistema de orquestación.




### Extracto transformado 078
**Hallazgo fuente:** --- SOURCE: Biografía familiar y migratoria ---
Guía Integral para Crear Biografías
Familiares Ficticias Realistas para
Modelos IA (IDUNEX)
Diseñar biografías familiares ﬁcticias altamente realistas – con profundidad
identitaria y plena plausibilidad – permite dotar a modelos de IA (adultos) de
una personalidad consistente y creíble.




### Extracto transformado 079
**Hallazgo fuente:** Este informe brinda un marco
escalable y accionable para crear decenas o centenares de perﬁles
sintéticos con diversidad sociocultural (contexto PROJECT_DECLARED_LOCALITY) y en alineación
con el ecosistema PROJECT_BRAND_ENTITY.




### Extracto transformado 080
**Hallazgo fuente:** Se abordan recomendaciones detalladas para
un uso tanto interno (entrenamiento de modelos) como externo
(marketing de contenido), salvaguardando los aspectos éticos y legales.




### Extracto transformado 081
**Hallazgo fuente:** Estructura Biográﬁca Completa y Verosímil
Una biografía familiar ﬁcticia realista debe abarcar todas las etapas vitales
y relaciones esenciales de la persona artiﬁcial.




### Extracto transformado 082
**Hallazgo fuente:** Esto conﬁere profundidad al
personaje y proporciona material coherente para entrenar su
comportamiento y comunicación como modelo IA.




### Extracto transformado 083
**Hallazgo fuente:** una estructura recomendada, asegurando que cada elemento de la ruta de vida
se integre de forma lógica y rica en contexto local:




### Extracto transformado 084
**Hallazgo fuente:** Pautas de implementación: Presenta la biografía de forma cronológica
(infancia → adolescencia → formación → vida adulta actual) para mayor




### Extracto transformado 085
**Hallazgo fuente:** Evita saturar con datos irrelevantes: cada detalle debe aportar a la
caracterización del modelo, ya sea en su personalidad, valores o
habilidades 2 .




### Extracto transformado 086
**Hallazgo fuente:** Antes de ﬁnalizar, comprueba que la edad actual del personaje
concuerda con los eventos narrados (nacimiento, graduaciones, trabajos)
para no generar inconsistencias.




### Extracto transformado 087
**Hallazgo fuente:** Mapeo Causal: De la Historia Familiar a la
Identidad del Modelo
Una biografía bien conectada con la personalidad actual del modelo es
esencial para su credibilidad.




### Extracto transformado 088
**Hallazgo fuente:** Esto signiﬁca establecer cómo el recorrido vital y
familiar del personaje inﬂuye en sus valores, forma de hablar, profesión y
estilo.




### Extracto transformado 089
**Hallazgo fuente:** Este mapa causal garantiza una coherencia psicológica: las vivencias
pasadas justiﬁcan el comportamiento presente.




### Extracto transformado 090
**Hallazgo fuente:** --- SOURCE: Moral valores y tica personal ---
Matriz moral realista para IA
humanizada: Desarrollo y aplicación
Desarrollar una matriz de moral convincente y realista para modelos de IA
con personalidad humana implica dotar a la IA de un perﬁl ético complejo,
creíble y consistente.




### Extracto transformado 091
**Hallazgo fuente:** Este marco moral debe funcionar para múltiples roles y
contextos simultáneamente: desde personajes de ﬁcción narrativos (A),
hasta asistentes conversacionales en producción (B), agentes creativos
para arte y redes sociales (C) y un marco general reutilizable (D) para
distintos dominios.




### Extracto transformado 092
**Hallazgo fuente:** A continuación presentamos una investigación completa y
práctica sobre cómo construir dicha matriz moral, abordando sus
componentes, la teoría ética relevante, su implementación
comportamental, la prevención de sesgos moralistas, un esquema técnico
para su codiﬁcación, casos de prueba detallados y un marco de
aseguramiento de calidad (QA) para garantizar la coherencia moral en el
tiempo y en diferentes contextos.




### Extracto transformado 093
**Hallazgo fuente:** Componentes estructurales de la matriz moral
Una matriz moral consiste en atributos éticos que delinean el carácter
moral del agente de IA.




### Extracto transformado 094
**Hallazgo fuente:** Estos componentes, deﬁnidos en forma estructurada
y explícita, permiten programar e inspeccionar los valores y tendencias éticas
del sistema.




### Extracto transformado 095
**Hallazgo fuente:** Una matriz moral realista no solo incluye normas positivas, sino
también elementos de tensión y falibilidad que evitan que la IA resulte
idealizada o simplista.




### Extracto transformado 096
**Hallazgo fuente:** Resumen de la estructura: En conjunto, estos componentes conﬁguran la
matriz moral, que puede representarse de forma estructurada (p.




### Extracto transformado 097
**Hallazgo fuente:** La inclusión explícita de valores y límites le da un marco axiológico
claro a la IA, mientras que las virtudes, defectos y dilemas proveen la
textura moral necesaria para un comportamiento realista y atractivo.




### Extracto transformado 098
**Hallazgo fuente:** razonamiento moral en situaciones difíciles, y las lealtades crean tensiones
narrativas realistas y alinean la IA con contextos especíﬁcos (p.




### Extracto transformado 099
**Hallazgo fuente:** (El ejemplo anterior ilustra cómo podría verse una matriz moral para un
asistente conversacional corporativo, con campos JSON personalizables por
contexto; en formato TXT o DOCX se podría representar de modo análogo con
listas y descripciones.)




### Extracto transformado 100
**Hallazgo fuente:** Fundamentos teóricos para una IA moral y
creíble
Una matriz moral robusta debe basarse en teorías éticas sólidas, adaptadas
al contexto de una IA humanizada.




### Extracto transformado 101
**Hallazgo fuente:** Integrar diversos enfoques de la ﬁlosofía
moral y la psicología permite dotar a la IA de un marco normativo rico, con
capacidad de razonamiento moral adulto y sensibilidad a diferencias
culturales.




### Extracto transformado 102
**Hallazgo fuente:** Ética de la virtud (Aristóteles y enfoques contemporáneos): La ética de la
virtud se enfoca en la formación del carácter moral más que en seguir reglas
aisladas.




### Extracto transformado 103
**Hallazgo fuente:** Aristóteles sostuvo que ser virtuoso consiste en cultivar cualidades
de excelencia moral (virtudes) que llevan a la “vida buena” y a la eudaimonía
(ﬂorecimiento).




### Extracto transformado 104
**Hallazgo fuente:** En el contexto de IA, adoptar un enfoque de virtudes signiﬁca
deﬁnir “qué tipo de persona” es el agente: sus intenciones, motivaciones
profundas y su carácter.




### Extracto transformado 105
**Hallazgo fuente:** Esto complementa las reglas y objetivos con una
coherencia interna, haciendo que la IA actúe de manera virtuosa por
convicción, no solo por cumplir órdenes.




### Extracto transformado 106
**Hallazgo fuente:** --- SOURCE: Lenguaje acento y voz escrita ---
Diseño de un Perﬁl Lingüístico para
un Modelo de IA con Voz PROJECT_DECLARED_COUNTRYana/
Latinoamericana
La personalidad lingüística de un modelo de Inteligencia Artiﬁcial (IA)
deﬁne cómo se comunica con los usuarios en distintos contextos.




### Extracto transformado 107
**Hallazgo fuente:** Diseñar un
perﬁl lingüístico consiste en especiﬁcar el tono, el vocabulario, las
expresiones y la forma de hablar que la IA adoptará para sonar coherente,
natural y relevante para su audiencia objetivo.




### Extracto transformado 108
**Hallazgo fuente:** La personalidad de un
modelo conversacional abarca rasgos distintivos en su tono, registro y
estilo comunicativo: desde su forma de expresar emociones y humor hasta
cómo adapta su discurso según con quién hable 1 .




### Extracto transformado 109
**Hallazgo fuente:** A continuación,
presentamos una investigación exhaustiva para crear un perﬁl lingüístico
integral y aplicado para un modelo de IA de voz adulta basado en el español
project-declared, con ajustes para Latinoamérica y versatilidad para distintos
ámbitos (marca, chatbot conversacional, avatar o voz artística).




### Extracto transformado 110
**Hallazgo fuente:** Fundamentos del Perﬁl Lingüístico (PROJECT_DECLARED_COUNTRY/
Latam)
Base cultural y geográﬁca: El perﬁl se sustenta en el español project-declared,
particularmente la variedad de la costa central (PROJECT_DECLARED_CITY), reconocida como base
del español normativo project-declared 2 .




### Extracto transformado 111
**Hallazgo fuente:** Esta variante incorpora inﬂuencias andinas,
criollas y quechuas, pero es entendida en toda Hispanoamérica 2 .




### Extracto transformado 112
**Hallazgo fuente:** Al ser
adaptable a Latinoamérica, el perﬁl incluirá módulos de ajuste regional: es
decir, lineamientos para adaptar o neutralizar ciertos modismos project-declareds y
evitar malentendidos fuera de PROJECT_DECLARED_COUNTRY, sin perder el sabor local.




### Extracto transformado 113
**Hallazgo fuente:** Debe funcionar igualmente bien en contextos de marca corporativa,
asistencia conversacional (chatbots), personajes digitales (avatares) e
incluso interpretaciones artísticas (canciones, videos).




### Extracto transformado 114
**Hallazgo fuente:** Si bien mantendrá un
carácter central coherente, deberá ser tan versátil como para ajustar su
registro a situaciones formales e informales.




### Extracto transformado 115
**Hallazgo fuente:** Esto requiere un enfoque
integral: no se trata de un estilo monolítico, sino de un conjunto de variantes
que el modelo pueda alternar según la circunstancia.




### Extracto transformado 116
**Hallazgo fuente:** Enfoque de máxima profundidad: Cubriremos dimensiones lingüísticas
(vocabulario, muletillas, sintaxis), psicológicas/emocionales (empatía, humor,
expresividad) y riesgos ético-comerciales (ﬁdelidad al perﬁl cultural,
autenticidad percibida, etc.).




### Extracto transformado 117
**Hallazgo fuente:** Cada sección aportará tanto principios como
ejemplos prácticos para que este perﬁl sea implementable.




### Extracto transformado 118
**Hallazgo fuente:** Variantes del Español PROJECT_DECLARED_COUNTRYano: Formal, Casual,
Urbano, Profesional y Emocional
El español project-declared abarca diferentes registros que reﬂejan contexto social y
nivel de formalidad.




### Extracto transformado 119
**Hallazgo fuente:** A continuación, describimos cada variante en detalle, incluyendo:
vocabulario y expresiones características, muletillas (muletas
conversacionales), ritmo y cadencia (estructura de oraciones), uso del humor
(chistes, tono jocoso) y frases típicas vs.




### Extracto transformado 120
**Hallazgo fuente:** Contexto: Usado en situaciones de máxima cortesía y respeto, como
comunicados oﬁciales, correspondencia formal (cartas, correos ejecutivos) y al
dirigirse a desconocidos o superiores.




### Extracto transformado 121
**Hallazgo fuente:** “Por
consiguiente”, “sin embargo”, “en ese sentido” son comunes, aportando
estructura argumentativa a los mensajes.




### Extracto transformado 122
**Hallazgo fuente:** El lenguaje formal en PROJECT_DECLARED_COUNTRY se
asemeja al de otros países hispanos en la preferencia por oraciones largas y
sintaxis cuidada.




### Extracto transformado 123
**Hallazgo fuente:** En contextos formales
se evitan muletillas coloquiales como “pues” o “o sea”, ya que pueden restar
profesionalidad.




### Extracto transformado 124
**Hallazgo fuente:** Pueden usarse marcadores más neutros como “bien,”
“mire,” o “en efecto” para ganar tiempo o enfatizar, pero con moderación.




### Extracto transformado 125
**Hallazgo fuente:** Se favorecen oraciones compuestas y
completas, con abundancia de cláusulas subordinadas para matizar el
discurso.




### Extracto transformado 126
**Hallazgo fuente:** En entornos formales, el humor se utiliza con
cautela: si se emplea es de tipo sutil e inteligente (por ejemplo, un juego de
palabras reﬁnado o referencias culturales discretas).




### Extracto transformado 127
**Hallazgo fuente:** El español formal
project-declared preﬁere seriedad y respeto, así que se evitan las bromas
excesivamente informales.




### Extracto transformado 128
**Hallazgo fuente:** Ejemplo: En una conferencia profesional, en vez de
un chiste directo, se puede optar por un comentario ingenioso pero
respetuoso.




### Extracto transformado 129
**Hallazgo fuente:** Contexto: Registro cotidiano y desenfadado usado entre amigos cercanos,
familiares de conﬁanza o iguales en edad/estatus, incluso con colegas en un
entorno relajado.




### Extracto transformado 130
**Hallazgo fuente:** Se emplea el pronombre
“tú” (tuteo) con la mayoría de las personas conocidas y de similar rango,
reﬂejando la cultura project-declared de trato amigable (en PROJECT_DECLARED_COUNTRY, a diferencia de
países vecinos, el “tú” es común incluso en contextos no íntimos,
especialmente entre jóvenes y en entornos urbanos 3 ).




### Extracto transformado 131
**Hallazgo fuente:** El léxico es colloquial:
diminutivos afectivos (“amiguito/a”), exclamaciones genuinas (“¡Qué lindo!”,
“¡Qué roche!” para vergüenza, etc.), palabras como “genial”, “chevere” o “bacán”
para decir “estupendo” 5 , y “qué tal” como saludo casual.




### Extracto transformado 132
**Hallazgo fuente:** Las oraciones suelen
ser más cortas y simples que en el registro formal, a veces omitiendo palabras
entendidas por contexto (“¿Vienes mañana?” en lugar de “¿Vas a venir
mañana?”).




### Extracto transformado 133
**Hallazgo fuente:** Ejemplos:
“pues” (y su contracción coloquial “pe”), “ya” (para cerrar ideas), “no más”
(para insistir: “Dime no más” = “dime simplemente”), “¿no?” (como coletilla
conﬁrmatoria), “¡Pucha!” (interjección de frustración o sorpresa 5 ), “O sea”
(para introducir explicaciones 5 ) y “mmm… este…” (para pensar).




### Extracto transformado 134
**Hallazgo fuente:** El habla informal tiende a mezclar
oraciones cortas con algunas frases encadenadas por conjunciones sencillas
(“y”, “pero”, “entonces”, “ya”).




### Extracto transformado 135
**Hallazgo fuente:** El ritmo es dinámico – los project-declareds en
contextos informales pueden acelerar al emocionarse y pausar para énfasis o
suspenso con silencios breves, e.g.




### Extracto transformado 136
**Hallazgo fuente:** En la escritura casual (mensajes, chats), se suele imitar este ritmo: se
reparten ideas en varias oraciones, a veces sin sujeto explícito (ej.




### Extracto transformado 137
**Hallazgo fuente:** En el registro casual, el
sentido del humor project-declared se hace evidente: bromas amistosas, sarcasmo
ligero y referencias culturales (por ejemplo, mencionar comida típica o frases
de programas populares).




### Extracto transformado 138
**Hallazgo fuente:** Ejemplo: “¡Más lento que la cola del banco, hermano!”
Este humor es parte esencial para sonar cercano: los project-declareds son conocidos
por ser bromistas incluso en conversaciones cotidianas 5 .




### Extracto transformado 139
**Hallazgo fuente:** --- SOURCE: Gobernanza legal PROJECT_DECLARED_COUNTRY PROJECT_BRAND_ENTITY ---
Marco de Gobernanza Legal y Ético
para Modelos de IA Sintéticos en
PROJECT_BRAND_ENTITY (PROJECT_DECLARED_COUNTRY)
Informe de PROJECT_BRAND_ENTITY – Gerencia General




### Extracto transformado 140
**Hallazgo fuente:** Introducción
Objetivo: PROJECT_BRAND_ENTITY, como empresa creativa y audiovisual en PROJECT_DECLARED_COUNTRY, planea
utilizar modelos de Inteligencia Artiﬁcial (IA) sintéticos para generar
contenido digital con apariencia y voz humanas (“modelos sintéticos
adultos”).




### Extracto transformado 141
**Hallazgo fuente:** Para asegurar un uso responsable, ético y legal de esta tecnología,
se propone un Marco de Gobernanza Legal y Ético.




### Extracto transformado 142
**Hallazgo fuente:** Este marco será aplicable
tanto a contenidos generados para clientes comerciales, como a
producciones propias de PROJECT_BRAND_ENTITY.




### Extracto transformado 143
**Hallazgo fuente:** Su ﬁnalidad es servir a la vez como
guía operativa interna y como documento cuasi-legal, de modo que sus
lineamientos puedan integrarse en contratos, Términos y Condiciones y
políticas públicas relevantes.




### Extracto transformado 144
**Hallazgo fuente:** Contexto Normativo en PROJECT_DECLARED_COUNTRY: La introducción de modelos de IA generativa
coincide con recientes avances regulatorios en PROJECT_DECLARED_COUNTRY.




### Extracto transformado 145
**Hallazgo fuente:** El país cuenta con un
régimen robusto de protección de datos personales (Ley N.º 29733 de 2011,
con Reglamento modiﬁcado en 2024) que establece principios y obligaciones




### Extracto transformado 146
**Hallazgo fuente:** Además, en 2023 se promulgó la Ley N.º 31814 sobre desarrollo ético y
seguro de la IA, cuyo Reglamento de 2025 enfatiza transparencia, gestión de
riesgos e intervención humana en sistemas de IA 3 .




### Extracto transformado 147
**Hallazgo fuente:** También se han
introducido sanciones especíﬁcas contra el uso malicioso de la IA – por
ejemplo, el Decreto Legislativo N.º 32314 (2025) modiﬁca el Código Penal para
penalizar duramente la suplantación de identidad o voz mediante IA 4 .




### Extracto transformado 148
**Hallazgo fuente:** Estructura: Este informe desarrolla siete componentes fundamentales del
marco de gobernanza: Privacidad y Protección de Datos (Ley N.º 29733),
Derechos de Imagen, Voz, Música y Marcas, Transparencia y Disclosures
(identidad sintética), Análisis de Riesgos y Mitigación, Reglas para
Datasets y Referencias, Plantilla de “Sidecar Legal” por Output y Checklist
de aprobación previo a la publicación.




### Extracto transformado 149
**Hallazgo fuente:** Se priorizan los aspectos más
relevantes para PROJECT_DECLARED_COUNTRY y las necesidades especíﬁcas de PROJECT_BRAND_ENTITY como
empresa creativa audiovisual, integrando normativa local y mejores
prácticas internacionales.




### Extracto transformado 150
**Hallazgo fuente:** A continuación, se examina cada componente con detalle, ofreciendo
recomendaciones concretas y referencias a las fuentes normativas y
doctrinales pertinentes.




### Extracto transformado 151
**Hallazgo fuente:** Privacidad y Datos Personales (Ley N.º 29733)
Contexto legal: La Ley N.º 29733, Ley de Protección de Datos Personales, es
el pilar central del marco de privacidad en PROJECT_DECLARED_COUNTRY 5 .




### Extracto transformado 152
**Hallazgo fuente:** La Autoridad Nacional de
Protección de Datos Personales (ANPDP), adscrita al Ministerio de Justicia,
supervisa su cumplimiento, pudiendo imponer sanciones severas 5 .




### Extracto transformado 153
**Hallazgo fuente:** Principios rectores: La Ley 29733 se sustenta en ocho principios
fundamentales que orientan todo tratamiento de datos personales 5 :




### Extracto transformado 154
**Hallazgo fuente:** Obligaciones adicionales: Además de los principios, la Ley 29733 impone a
las empresas obligaciones operativas clave 5 .




### Extracto transformado 155
**Hallazgo fuente:** --- SOURCE: Identidad musical Suno por modelo ---
Informe técnico: Identidad musical
Suno por modelo IA – voz, estilo,
letra, energía y performance
(PROJECT_BRAND_ENTITY / IDUNEX)
1.




### Extracto transformado 156
**Hallazgo fuente:** Resumen ejecutivo
PROJECT_BRAND_ENTITY e IDUNEX [LEGACY_MARKETING_TERM_REMOVED] han desarrollado un sistema de 10 modelos
IA sintéticos (MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_07g, MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_03, MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_04, MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_02, MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_05,
MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_01, MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_06, MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_10, MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_11 y MULTI_SUBJECT_TEMPLATE_EXAMPLE_MODEL_09; todos
personajes adultos ﬁcción).




### Extracto transformado 157
**Hallazgo fuente:** Cada modelo ha sido cuidadosamente diseñado
con una identidad musical única y diferenciada que abarca su voz, estilo de
música, letra, energía escénica y performance.




### Extracto transformado 158
**Hallazgo fuente:** Esto garantiza que al
generar contenido de audio o canciones completas mediante tecnologías Suno
u otros modelos de música AI, cada modelo suene distinto – en coherencia
con su edad percibida, personalidad, origen cultural, rol en PROJECT_BRAND_ENTITY e
historia ﬁcticia – y se evite que las producciones ﬁnales se sientan genéricas o
indistinguibles entre sí.




### Extracto transformado 159
**Hallazgo fuente:** El presente informe es un documento maestro
(whitepaper técnico-operativo) que deﬁne exhaustivamente la capa de
identidad musical de los modelos, sirviendo como guía para equipos
creativos, técnicos y de QA.




### Extracto transformado 160
**Hallazgo fuente:** Principios técnicos clave: Se establecen principios técnicos y reglas para
que la voz sintética y la música reﬂejen la identidad de cada personaje, al
tiempo que aseguren calidad sonora premium y coherencia de marca.




### Extracto transformado 161
**Hallazgo fuente:** Esto
incluye la diferenciación conceptual entre tipos de identidad (voz hablada, voz
cantada, identidad musical, identidad lírica, identidad de performance
escénica e identidad sonora de marca) y su implementación en variables
operativas.




### Extracto transformado 162
**Hallazgo fuente:** Matrices musicales por modelo: Para cada uno de los 10 modelos, se
presenta una matriz detallada de identidad musical que resume su estilo
base y secundarios, estilos a evitar, género vocal y rango objetivo, edad vocal
percibida, energía típica de su música, tipo de letra que maneja, estilo de
ganchos (hooks) y estribillos, actitud escénica, BPM y tonalidades
recomendadas, instrumentos principales, nivel de rareza, nivel de ﬁdelidad al
estilo (inﬂuencia de estilo) y usos ideales dentro de PROJECT_BRAND_ENTITY.




### Extracto transformado 163
**Hallazgo fuente:** Reglas por tipo de salida Suno: Se deﬁnen guías especíﬁcas para cada
modalidad de salida musical (canción completa, instrumental, sonido de un
golpe, loop, intro de video, jingle publicitario, tema de personaje, track para




### Extracto transformado 164
**Hallazgo fuente:** redes sociales, música de backstage, música de campaña premium), con
plantillas detalladas que enumeran todos los campos relevantes (título,
modelo, estilos a incluir/excluir, género vocal, modo de letra, niveles de
“weirdness” y “style inﬂuence”, estrategia de inﬂuencia de audio, BPM,
tonalidad, letra, prompt de portada de arte, y copys adaptados a redes sociales)
para la generación de audio y contenido promocional.




### Extracto transformado 165
**Hallazgo fuente:** Estos modelos de
prompts pueden aplicarse en la plataforma Suno y ser integrados con ﬂujos de
trabajo utilizando agentes de IA (e.g., ChatGPT para generar letras o visuales,
Copilot 365 para documentación) y sidecars para trazabilidad.




### Extracto transformado 166
**Hallazgo fuente:** Coherencia y calidad de resultados: Se incluye una matriz de coherencia
cruzada para asegurar que las producciones musicales respeten los ejes de
edad–voz (la voz suena acorde con la edad del personaje 1 ), personalidad–
letra (el contenido lírico reﬂeja la psicología e historia del personaje), origen–
elementos culturales musicales (inclusión de guiños culturales seguros sin
caer en estereotipos 2 3 ), cuerpo/acting–performance (nivel de energía,
actitud y estilo interpretativo en escena concordante con la presencia física
cannónica del modelo 3 ), rol PROJECT_BRAND_ENTITY–género musical (sus roles en la
marca orientan sus géneros, ej.




### Extracto transformado 167
**Hallazgo fuente:** la voz corporativa preferirá estilos suaves
mientras que un bailarín favorece ritmos intensos) y escena visual–arreglo
musical (la música generada coincide con el contexto visual/escénico en que
se usará: corporativo, nightlife, backstage, etc., manteniendo la cohesión
audiovisual 3 ).




### Extracto transformado 168
**Hallazgo fuente:** Se propone un checklist de QA con códigos especíﬁcos (PASS/
FAIL) para evaluar rápidamente posibles problemas: música genérica o sin
identidad (e.g.




### Extracto transformado 169
**Hallazgo fuente:** FAIL_GENERIC_POP 4 ), errores de concordancia voz-edad
(FAIL_WRONG_VOCAL_AGE), incoherencias entre modelo y música
(FAIL_MODEL_MUSIC_MISMATCH), lyrics que no reﬂejan personalidad
(FAIL_LYRIC_PERSONALITY_MISMATCH), abuso de tags o guiños culturales
inapropiados, etc.




### Extracto transformado 170
**Hallazgo fuente:** clichés líricos, imitar artistas reales 4 , estereotipos culturales,
sexualización gratuita, contradicciones de identidad) y procedimientos de
corrección (fallback) para casos donde la salida musical generada no cumpla
con las expectativas o requisitos de la marca (por ejemplo, aumentar weirdness
para evitar resultados muy genéricos, o disminuirla si el resultado es
demasiado experimental y poco utilizable comercialmente).




### Extracto transformado 171
**Hallazgo fuente:** Integración técnica: Finalmente, se describe cómo se integrarán estas
deﬁniciones musicales en los archivos de perﬁl y prompt de cada modelo




### Extracto transformado 172
**Hallazgo fuente:** (PROFILE-LF-*.json, PROMPT-LF-*.txt y reportes combinados PROFILE-
PROMPT-LF-*.docx), así como en un Suno PromptPack especializado para
música, sidecars de audio y en los ﬂujos de los agentes ChatGPT/Copilot 365
para asistir al equipo creativo y técnico durante la producción musical.




### Extracto transformado 173
**Hallazgo fuente:** La
meta es que el equipo pueda usar directamente este informe para generar y
evaluar contenido musical con los modelos PROJECT_BRAND_ENTITY de manera coherente
con su identidad, garantizando producciones audiovisuales de alta calidad,
diferenciadas y alineadas con la marca.




### Extracto transformado 174
**Hallazgo fuente:** Principios técnicos para la identidad musical de
modelos IA sintéticos
Diferenciación y autenticidad: Cada modelo debe poseer un estilo sonoro
propio.




### Extracto transformado 175
**Hallazgo fuente:** Desde la voz cantada hasta el género musical y la interpretación, la
identidad musical de un modelo debe ser única y consistente con su perﬁl
base de personalidad y background, evitando solapamientos con otros
personajes (no “identity blending” ni confusiones entre rostros/voces) 3 .




### Extracto transformado 176
**Hallazgo fuente:** Esto
implica asignar a cada modelo parámetros y atributos musicales distintos,
evitando reproducir la misma fórmula genérica (por ejemplo, no hacer que
todos canten reggaetón de la misma forma) 3 4 .




### Extracto transformado 177
**Hallazgo fuente:** Dentro del perﬁl musical de
cada modelo se deﬁnen claramente géneros primarios y secundarios, y se
prohíben aquellos estilos que contradicen o diluyen su personalidad.




### Extracto transformado 178
**Hallazgo fuente:** Además,
se enfatizan elementos singulares (timbre, acento, instrumentación
preferida, rasgos culturales) para dar autenticidad y robustecer la separación
entre identidades musicales.




### Extracto transformado 179
**Hallazgo fuente:** Coherencia con la identidad base (voz, edad y personalidad): La expresión
musical del modelo debe respetar su base de identidad demográﬁca y
psicológica.




### Extracto transformado 180
**Hallazgo fuente:** En particular: la edad vocal percibida en las interpretaciones
(vocal age band) debe coincidir con su edad visible (ej.
