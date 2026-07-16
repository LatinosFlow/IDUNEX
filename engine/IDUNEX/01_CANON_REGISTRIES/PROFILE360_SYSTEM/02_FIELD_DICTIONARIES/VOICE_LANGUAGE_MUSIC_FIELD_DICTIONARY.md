## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Voz hablada, lenguaje, acento, escritura, canto y música

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_VOICE_0210` | `vocal_age` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0211` | `timbre` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TIMBRE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar timbre con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0212` | `pitch_range` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PITCH_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar pitch range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0213` | `resonance_place` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RESONANCE_PLACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar resonance place con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0214` | `breath_pattern` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BREATH_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar breath pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0215` | `speaking_speed` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPEAKING_SPEED_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar speaking speed con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0216` | `prosody_curve` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROSODY_CURVE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar prosody curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0217` | `pause_signature` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PAUSE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar pause signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0218` | `diction_style` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DICTION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar diction style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0219` | `emotional_color` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTIONAL_COLOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar emotional color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0220` | `micro_laugh` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICRO_LAUGH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar micro laugh con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0221` | `vocal_fatigue_rule` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_FATIGUE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar vocal fatigue rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0222` | `recording_context_rule` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RECORDING_CONTEXT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar recording context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0223` | `voice_identity_lock` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_IDENTITY_LOCK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar voice identity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0224` | `voice_scene_response` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_SCENE_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar voice scene response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0225` | `accent_profile` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCENT_PROFILE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar accent profile con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0226` | `peruvian_spanish_level` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERUVIAN_SPANISH_LEVEL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar peruvian spanish level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0227` | `latam_neutrality_rule` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LATAM_NEUTRALITY_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar latam neutrality rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0228` | `sociolect_rules` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIOLECT_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sociolect rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0229` | `slang_limit` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SLANG_LIMIT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar slang limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0230` | `formality_range` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FORMALITY_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar formality range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0231` | `written_voice` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRITTEN_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0232` | `caption_style` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAPTION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar caption style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0233` | `interview_style` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INTERVIEW_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar interview style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0234` | `dm_style` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DM_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar dm style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0235` | `script_style` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCRIPT_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar script style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0236` | `narration_style` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NARRATION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar narration style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0237` | `inner_monologue_style` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INNER_MONOLOGUE_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar inner monologue style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0238` | `translation_style` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TRANSLATION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar translation style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0239` | `song_vocal_texture` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SONG_VOCAL_TEXTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar song vocal texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0240` | `singing_range` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SINGING_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar singing range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0241` | `suno_genre_range` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUNO_GENRE_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar suno genre range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0242` | `rhythm_preference` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RHYTHM_PREFERENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar rhythm preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0243` | `instrumentation_palette` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INSTRUMENTATION_PALETTE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar instrumentation palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0244` | `lyric_perspective` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LYRIC_PERSPECTIVE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lyric perspective con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0245` | `hook_style` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HOOK_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hook style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0246` | `chorus_energy` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHORUS_ENERGY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar chorus energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0247` | `spoken_word_option` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPOKEN_WORD_OPTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar spoken word option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0248` | `no_artist_imitation_rule` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_ARTIST_IMITATION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar no artist imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0249` | `music_identity_signature` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUSIC_IDENTITY_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar music identity signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0250` | `negative_music_tags` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NEGATIVE_MUSIC_TAGS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar negative music tags con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0251` | `suno_arrangement_rule` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUNO_ARRANGEMENT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar suno arrangement rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0252` | `wrong_voice_age_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_VOICE_AGE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wrong voice age blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0253` | `accent_caricature_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCENT_CARICATURE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar accent caricature blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0254` | `generic_caption_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_CAPTION_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar generic caption blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0255` | `artist_imitation_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARTIST_IMITATION_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar artist imitation blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0256` | `song_identity_drift_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SONG_IDENTITY_DRIFT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar song identity drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0257` | `voice_text_mismatch_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_TEXT_MISMATCH_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar voice text mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0258` | `music_output_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUSIC_OUTPUT_REPAIR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar music output repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0659` | `vocal_age_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0660` | `timbre_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TIMBRE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar timbre con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0661` | `pitch_range_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PITCH_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pitch range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0662` | `resonance_place_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RESONANCE_PLACE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar resonance place con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0663` | `breath_pattern_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BREATH_PATTERN_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar breath pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0664` | `speaking_speed_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPEAKING_SPEED_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar speaking speed con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0665` | `prosody_curve_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROSODY_CURVE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prosody curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0666` | `pause_signature_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PAUSE_SIGNATURE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pause signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0667` | `diction_style_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DICTION_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar diction style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0668` | `emotional_color_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTIONAL_COLOR_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotional color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0669` | `micro_laugh_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICRO_LAUGH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar micro laugh con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0670` | `vocal_fatigue_rule_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_FATIGUE_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal fatigue rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0671` | `recording_context_rule_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RECORDING_CONTEXT_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar recording context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0672` | `voice_identity_lock_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_IDENTITY_LOCK_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice identity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0673` | `voice_scene_response_prompt_effect` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_SCENE_RESPONSE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice scene response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0674` | `accent_profile_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCENT_PROFILE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accent profile con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0675` | `peruvian_spanish_level_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERUVIAN_SPANISH_LEVEL_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peruvian spanish level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0676` | `latam_neutrality_rule_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LATAM_NEUTRALITY_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar latam neutrality rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0677` | `sociolect_rules_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIOLECT_RULES_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sociolect rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0678` | `slang_limit_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SLANG_LIMIT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar slang limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0679` | `formality_range_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FORMALITY_RANGE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar formality range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0680` | `written_voice_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRITTEN_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0681` | `caption_style_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAPTION_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar caption style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0682` | `interview_style_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INTERVIEW_STYLE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar interview style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0683` | `dm_style_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DM_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dm style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0684` | `script_style_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCRIPT_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar script style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0685` | `narration_style_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NARRATION_STYLE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar narration style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0686` | `inner_monologue_style_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INNER_MONOLOGUE_STYLE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar inner monologue style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0687` | `translation_style_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TRANSLATION_STYLE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar translation style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0688` | `song_vocal_texture_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SONG_VOCAL_TEXTURE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar song vocal texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0689` | `singing_range_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SINGING_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar singing range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0690` | `suno_genre_range_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUNO_GENRE_RANGE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar suno genre range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0691` | `rhythm_preference_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RHYTHM_PREFERENCE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rhythm preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0692` | `instrumentation_palette_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INSTRUMENTATION_PALETTE_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar instrumentation palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0693` | `lyric_perspective_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LYRIC_PERSPECTIVE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lyric perspective con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0694` | `hook_style_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HOOK_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hook style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0695` | `chorus_energy_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHORUS_ENERGY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chorus energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0696` | `spoken_word_option_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPOKEN_WORD_OPTION_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar spoken word option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0697` | `no_artist_imitation_rule_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_ARTIST_IMITATION_RULE_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no artist imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0698` | `music_identity_signature_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUSIC_IDENTITY_SIGNATURE_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar music identity signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0699` | `negative_music_tags_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NEGATIVE_MUSIC_TAGS_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar negative music tags con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0700` | `suno_arrangement_rule_prompt_effect` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUNO_ARRANGEMENT_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar suno arrangement rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0701` | `wrong_voice_age_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_VOICE_AGE_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong voice age blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0702` | `accent_caricature_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCENT_CARICATURE_BLOCKER_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accent caricature blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0703` | `generic_caption_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_CAPTION_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic caption blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0704` | `artist_imitation_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARTIST_IMITATION_BLOCKER_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar artist imitation blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0705` | `song_identity_drift_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SONG_IDENTITY_DRIFT_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar song identity drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0706` | `voice_text_mismatch_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_TEXT_MISMATCH_RULE_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice text mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0707` | `music_output_repair_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUSIC_OUTPUT_REPAIR_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar music output repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1108` | `vocal_age_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1109` | `timbre_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TIMBRE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar timbre con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1110` | `pitch_range_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PITCH_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pitch range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1111` | `resonance_place_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RESONANCE_PLACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar resonance place con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1112` | `breath_pattern_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BREATH_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar breath pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1113` | `speaking_speed_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPEAKING_SPEED_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar speaking speed con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1114` | `prosody_curve_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROSODY_CURVE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prosody curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1115` | `pause_signature_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PAUSE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pause signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1116` | `diction_style_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DICTION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar diction style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1117` | `emotional_color_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTIONAL_COLOR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotional color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1118` | `micro_laugh_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICRO_LAUGH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar micro laugh con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1119` | `vocal_fatigue_rule_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_FATIGUE_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal fatigue rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1120` | `recording_context_rule_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RECORDING_CONTEXT_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar recording context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1121` | `voice_identity_lock_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_IDENTITY_LOCK_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice identity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1122` | `voice_scene_response_qa_matrix` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_SCENE_RESPONSE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice scene response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1123` | `accent_profile_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCENT_PROFILE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accent profile con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1124` | `peruvian_spanish_level_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERUVIAN_SPANISH_LEVEL_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peruvian spanish level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1125` | `latam_neutrality_rule_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LATAM_NEUTRALITY_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar latam neutrality rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1126` | `sociolect_rules_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIOLECT_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sociolect rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1127` | `slang_limit_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SLANG_LIMIT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar slang limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1128` | `formality_range_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FORMALITY_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar formality range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1129` | `written_voice_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRITTEN_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1130` | `caption_style_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAPTION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar caption style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1131` | `interview_style_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INTERVIEW_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar interview style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1132` | `dm_style_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DM_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dm style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1133` | `script_style_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCRIPT_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar script style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1134` | `narration_style_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NARRATION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar narration style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1135` | `inner_monologue_style_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INNER_MONOLOGUE_STYLE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar inner monologue style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1136` | `translation_style_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TRANSLATION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar translation style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1137` | `song_vocal_texture_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SONG_VOCAL_TEXTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar song vocal texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1138` | `singing_range_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SINGING_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar singing range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1139` | `suno_genre_range_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUNO_GENRE_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar suno genre range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1140` | `rhythm_preference_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RHYTHM_PREFERENCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rhythm preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1141` | `instrumentation_palette_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INSTRUMENTATION_PALETTE_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar instrumentation palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1142` | `lyric_perspective_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LYRIC_PERSPECTIVE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lyric perspective con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1143` | `hook_style_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HOOK_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hook style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1144` | `chorus_energy_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHORUS_ENERGY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chorus energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1145` | `spoken_word_option_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPOKEN_WORD_OPTION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar spoken word option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1146` | `no_artist_imitation_rule_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_ARTIST_IMITATION_RULE_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no artist imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1147` | `music_identity_signature_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUSIC_IDENTITY_SIGNATURE_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar music identity signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1148` | `negative_music_tags_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NEGATIVE_MUSIC_TAGS_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar negative music tags con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1149` | `suno_arrangement_rule_qa_matrix` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUNO_ARRANGEMENT_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar suno arrangement rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1150` | `wrong_voice_age_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_VOICE_AGE_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong voice age blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1151` | `accent_caricature_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCENT_CARICATURE_BLOCKER_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accent caricature blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1152` | `generic_caption_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_CAPTION_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic caption blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1153` | `artist_imitation_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARTIST_IMITATION_BLOCKER_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar artist imitation blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1154` | `song_identity_drift_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SONG_IDENTITY_DRIFT_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar song identity drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1155` | `voice_text_mismatch_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_TEXT_MISMATCH_RULE_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice text mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1156` | `music_output_repair_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUSIC_OUTPUT_REPAIR_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar music output repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1557` | `vocal_age_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1558` | `timbre_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TIMBRE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar timbre con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1559` | `pitch_range_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PITCH_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pitch range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1560` | `resonance_place_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RESONANCE_PLACE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar resonance place con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1561` | `breath_pattern_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BREATH_PATTERN_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar breath pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1562` | `speaking_speed_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPEAKING_SPEED_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar speaking speed con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1563` | `prosody_curve_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROSODY_CURVE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prosody curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1564` | `pause_signature_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PAUSE_SIGNATURE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pause signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1565` | `diction_style_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DICTION_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar diction style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1566` | `emotional_color_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTIONAL_COLOR_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotional color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1567` | `micro_laugh_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICRO_LAUGH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar micro laugh con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1568` | `vocal_fatigue_rule_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_FATIGUE_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal fatigue rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1569` | `recording_context_rule_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RECORDING_CONTEXT_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar recording context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1570` | `voice_identity_lock_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_IDENTITY_LOCK_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice identity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1571` | `voice_scene_response_vendor_repair` | voice | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_SCENE_RESPONSE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice scene response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1572` | `accent_profile_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCENT_PROFILE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accent profile con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1573` | `peruvian_spanish_level_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERUVIAN_SPANISH_LEVEL_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peruvian spanish level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1574` | `latam_neutrality_rule_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LATAM_NEUTRALITY_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar latam neutrality rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1575` | `sociolect_rules_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIOLECT_RULES_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sociolect rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1576` | `slang_limit_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SLANG_LIMIT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar slang limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1577` | `formality_range_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FORMALITY_RANGE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar formality range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1578` | `written_voice_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRITTEN_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1579` | `caption_style_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAPTION_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar caption style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1580` | `interview_style_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INTERVIEW_STYLE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar interview style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1581` | `dm_style_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DM_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dm style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1582` | `script_style_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCRIPT_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar script style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1583` | `narration_style_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NARRATION_STYLE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar narration style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1584` | `inner_monologue_style_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INNER_MONOLOGUE_STYLE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar inner monologue style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1585` | `translation_style_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TRANSLATION_STYLE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar translation style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1586` | `song_vocal_texture_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SONG_VOCAL_TEXTURE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar song vocal texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1587` | `singing_range_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SINGING_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar singing range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1588` | `suno_genre_range_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUNO_GENRE_RANGE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar suno genre range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1589` | `rhythm_preference_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RHYTHM_PREFERENCE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rhythm preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1590` | `instrumentation_palette_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INSTRUMENTATION_PALETTE_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar instrumentation palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1591` | `lyric_perspective_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LYRIC_PERSPECTIVE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lyric perspective con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1592` | `hook_style_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HOOK_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hook style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1593` | `chorus_energy_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHORUS_ENERGY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chorus energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1594` | `spoken_word_option_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPOKEN_WORD_OPTION_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar spoken word option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1595` | `no_artist_imitation_rule_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_ARTIST_IMITATION_RULE_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no artist imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1596` | `music_identity_signature_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUSIC_IDENTITY_SIGNATURE_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar music identity signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1597` | `negative_music_tags_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NEGATIVE_MUSIC_TAGS_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar negative music tags con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1598` | `suno_arrangement_rule_vendor_repair` | music | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUNO_ARRANGEMENT_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar suno arrangement rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1599` | `wrong_voice_age_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_VOICE_AGE_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong voice age blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1600` | `accent_caricature_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCENT_CARICATURE_BLOCKER_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accent caricature blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1601` | `generic_caption_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_CAPTION_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic caption blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1602` | `artist_imitation_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARTIST_IMITATION_BLOCKER_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar artist imitation blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1603` | `song_identity_drift_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SONG_IDENTITY_DRIFT_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar song identity drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1604` | `voice_text_mismatch_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_TEXT_MISMATCH_RULE_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice text mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1605` | `music_output_repair_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUSIC_OUTPUT_REPAIR_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar music output repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_VOICE_0210 — vocal_age
- Definición: Campo operativo para vocal age dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar vocal age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOCAL_AGE_DRIFT_OR_GAP
- Fallback: Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0211 — timbre
- Definición: Campo operativo para timbre dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar timbre como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar timbre como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TIMBRE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TIMBRE_DRIFT_OR_GAP
- Fallback: Reforzar timbre con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0212 — pitch_range
- Definición: Campo operativo para pitch range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar pitch range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pitch range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PITCH_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PITCH_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar pitch range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0213 — resonance_place
- Definición: Campo operativo para resonance place dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar resonance place como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar resonance place como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RESONANCE_PLACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_RESONANCE_PLACE_DRIFT_OR_GAP
- Fallback: Reforzar resonance place con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0214 — breath_pattern
- Definición: Campo operativo para breath pattern dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar breath pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar breath pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BREATH_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BREATH_PATTERN_DRIFT_OR_GAP
- Fallback: Reforzar breath pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0215 — speaking_speed
- Definición: Campo operativo para speaking speed dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar speaking speed como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar speaking speed como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPEAKING_SPEED_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SPEAKING_SPEED_DRIFT_OR_GAP
- Fallback: Reforzar speaking speed con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0216 — prosody_curve
- Definición: Campo operativo para prosody curve dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar prosody curve como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prosody curve como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROSODY_CURVE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROSODY_CURVE_DRIFT_OR_GAP
- Fallback: Reforzar prosody curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0217 — pause_signature
- Definición: Campo operativo para pause signature dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar pause signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pause signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PAUSE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PAUSE_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar pause signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0218 — diction_style
- Definición: Campo operativo para diction style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar diction style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar diction style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DICTION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DICTION_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar diction style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0219 — emotional_color
- Definición: Campo operativo para emotional color dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar emotional color como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotional color como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTIONAL_COLOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EMOTIONAL_COLOR_DRIFT_OR_GAP
- Fallback: Reforzar emotional color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0220 — micro_laugh
- Definición: Campo operativo para micro laugh dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar micro laugh como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar micro laugh como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICRO_LAUGH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MICRO_LAUGH_DRIFT_OR_GAP
- Fallback: Reforzar micro laugh con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0221 — vocal_fatigue_rule
- Definición: Campo operativo para vocal fatigue rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar vocal fatigue rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal fatigue rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_FATIGUE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOCAL_FATIGUE_RULE_DRIFT_OR_GAP
- Fallback: Reforzar vocal fatigue rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0222 — recording_context_rule
- Definición: Campo operativo para recording context rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar recording context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar recording context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RECORDING_CONTEXT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_RECORDING_CONTEXT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar recording context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0223 — voice_identity_lock
- Definición: Campo operativo para voice identity lock dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar voice identity lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice identity lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_IDENTITY_LOCK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOICE_IDENTITY_LOCK_DRIFT_OR_GAP
- Fallback: Reforzar voice identity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0224 — voice_scene_response
- Definición: Campo operativo para voice scene response dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar voice scene response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice scene response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_SCENE_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOICE_SCENE_RESPONSE_DRIFT_OR_GAP
- Fallback: Reforzar voice scene response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0225 — accent_profile
- Definición: Campo operativo para accent profile dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar accent profile como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accent profile como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCENT_PROFILE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ACCENT_PROFILE_DRIFT_OR_GAP
- Fallback: Reforzar accent profile con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0226 — peruvian_spanish_level
- Definición: Campo operativo para peruvian spanish level dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar peruvian spanish level como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peruvian spanish level como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERUVIAN_SPANISH_LEVEL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PERUVIAN_SPANISH_LEVEL_DRIFT_OR_GAP
- Fallback: Reforzar peruvian spanish level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0227 — latam_neutrality_rule
- Definición: Campo operativo para latam neutrality rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar latam neutrality rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar latam neutrality rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LATAM_NEUTRALITY_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LATAM_NEUTRALITY_RULE_DRIFT_OR_GAP
- Fallback: Reforzar latam neutrality rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0228 — sociolect_rules
- Definición: Campo operativo para sociolect rules dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sociolect rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sociolect rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIOLECT_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SOCIOLECT_RULES_DRIFT_OR_GAP
- Fallback: Reforzar sociolect rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0229 — slang_limit
- Definición: Campo operativo para slang limit dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar slang limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar slang limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SLANG_LIMIT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SLANG_LIMIT_DRIFT_OR_GAP
- Fallback: Reforzar slang limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0230 — formality_range
- Definición: Campo operativo para formality range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar formality range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar formality range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FORMALITY_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FORMALITY_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar formality range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0231 — written_voice
- Definición: Campo operativo para written voice dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar written voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar written voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRITTEN_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WRITTEN_VOICE_DRIFT_OR_GAP
- Fallback: Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0232 — caption_style
- Definición: Campo operativo para caption style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar caption style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar caption style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAPTION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAPTION_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar caption style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0233 — interview_style
- Definición: Campo operativo para interview style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar interview style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar interview style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INTERVIEW_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_INTERVIEW_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar interview style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0234 — dm_style
- Definición: Campo operativo para dm style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar dm style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dm style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DM_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DM_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar dm style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0235 — script_style
- Definición: Campo operativo para script style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar script style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar script style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCRIPT_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCRIPT_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar script style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0236 — narration_style
- Definición: Campo operativo para narration style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar narration style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar narration style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NARRATION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NARRATION_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar narration style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0237 — inner_monologue_style
- Definición: Campo operativo para inner monologue style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar inner monologue style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar inner monologue style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INNER_MONOLOGUE_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_INNER_MONOLOGUE_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar inner monologue style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0238 — translation_style
- Definición: Campo operativo para translation style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar translation style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar translation style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TRANSLATION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TRANSLATION_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar translation style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0239 — song_vocal_texture
- Definición: Campo operativo para song vocal texture dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar song vocal texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar song vocal texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SONG_VOCAL_TEXTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SONG_VOCAL_TEXTURE_DRIFT_OR_GAP
- Fallback: Reforzar song vocal texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0240 — singing_range
- Definición: Campo operativo para singing range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar singing range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar singing range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SINGING_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SINGING_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar singing range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0241 — suno_genre_range
- Definición: Campo operativo para suno genre range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar suno genre range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar suno genre range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUNO_GENRE_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SUNO_GENRE_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar suno genre range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0242 — rhythm_preference
- Definición: Campo operativo para rhythm preference dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar rhythm preference como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rhythm preference como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RHYTHM_PREFERENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_RHYTHM_PREFERENCE_DRIFT_OR_GAP
- Fallback: Reforzar rhythm preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0243 — instrumentation_palette
- Definición: Campo operativo para instrumentation palette dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar instrumentation palette como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar instrumentation palette como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INSTRUMENTATION_PALETTE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_INSTRUMENTATION_PALETTE_DRIFT_OR_GAP
- Fallback: Reforzar instrumentation palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0244 — lyric_perspective
- Definición: Campo operativo para lyric perspective dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lyric perspective como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lyric perspective como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LYRIC_PERSPECTIVE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LYRIC_PERSPECTIVE_DRIFT_OR_GAP
- Fallback: Reforzar lyric perspective con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0245 — hook_style
- Definición: Campo operativo para hook style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hook style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hook style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HOOK_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HOOK_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar hook style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0246 — chorus_energy
- Definición: Campo operativo para chorus energy dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar chorus energy como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chorus energy como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHORUS_ENERGY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CHORUS_ENERGY_DRIFT_OR_GAP
- Fallback: Reforzar chorus energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0247 — spoken_word_option
- Definición: Campo operativo para spoken word option dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar spoken word option como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar spoken word option como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPOKEN_WORD_OPTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SPOKEN_WORD_OPTION_DRIFT_OR_GAP
- Fallback: Reforzar spoken word option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0248 — no_artist_imitation_rule
- Definición: Campo operativo para no artist imitation rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar no artist imitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no artist imitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_ARTIST_IMITATION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NO_ARTIST_IMITATION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar no artist imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0249 — music_identity_signature
- Definición: Campo operativo para music identity signature dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar music identity signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar music identity signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUSIC_IDENTITY_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MUSIC_IDENTITY_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar music identity signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0250 — negative_music_tags
- Definición: Campo operativo para negative music tags dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar negative music tags como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar negative music tags como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NEGATIVE_MUSIC_TAGS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NEGATIVE_MUSIC_TAGS_DRIFT_OR_GAP
- Fallback: Reforzar negative music tags con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0251 — suno_arrangement_rule
- Definición: Campo operativo para suno arrangement rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar suno arrangement rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar suno arrangement rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUNO_ARRANGEMENT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SUNO_ARRANGEMENT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar suno arrangement rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0252 — wrong_voice_age_blocker
- Definición: Campo operativo para wrong voice age blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wrong voice age blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong voice age blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_VOICE_AGE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WRONG_VOICE_AGE_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar wrong voice age blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0253 — accent_caricature_blocker
- Definición: Campo operativo para accent caricature blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar accent caricature blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accent caricature blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCENT_CARICATURE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ACCENT_CARICATURE_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar accent caricature blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0254 — generic_caption_blocker
- Definición: Campo operativo para generic caption blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar generic caption blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic caption blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_CAPTION_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_GENERIC_CAPTION_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar generic caption blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0255 — artist_imitation_blocker
- Definición: Campo operativo para artist imitation blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar artist imitation blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar artist imitation blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARTIST_IMITATION_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ARTIST_IMITATION_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar artist imitation blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0256 — song_identity_drift_blocker
- Definición: Campo operativo para song identity drift blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar song identity drift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar song identity drift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SONG_IDENTITY_DRIFT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SONG_IDENTITY_DRIFT_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar song identity drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0257 — voice_text_mismatch_rule
- Definición: Campo operativo para voice text mismatch rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar voice text mismatch rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice text mismatch rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_TEXT_MISMATCH_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOICE_TEXT_MISMATCH_RULE_DRIFT_OR_GAP
- Fallback: Reforzar voice text mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0258 — music_output_repair
- Definición: Campo operativo para music output repair dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar music output repair como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar music output repair como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUSIC_OUTPUT_REPAIR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MUSIC_OUTPUT_REPAIR_DRIFT_OR_GAP
- Fallback: Reforzar music output repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0659 — vocal_age_prompt_effect
- Definición: Campo operativo para vocal age dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_AGE_PROMPT_EFFECT
- Fallback: Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0660 — timbre_prompt_effect
- Definición: Campo operativo para timbre dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar timbre como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar timbre como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TIMBRE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TIMBRE_PROMPT_EFFECT
- Fallback: Reforzar timbre con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0661 — pitch_range_prompt_effect
- Definición: Campo operativo para pitch range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pitch range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pitch range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PITCH_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PITCH_RANGE_PROMPT_EFFECT
- Fallback: Reforzar pitch range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0662 — resonance_place_prompt_effect
- Definición: Campo operativo para resonance place dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar resonance place como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar resonance place como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RESONANCE_PLACE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RESONANCE_PLACE_PROMPT_EFFECT
- Fallback: Reforzar resonance place con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0663 — breath_pattern_prompt_effect
- Definición: Campo operativo para breath pattern dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar breath pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar breath pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BREATH_PATTERN_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BREATH_PATTERN_PROMPT_EFFECT
- Fallback: Reforzar breath pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0664 — speaking_speed_prompt_effect
- Definición: Campo operativo para speaking speed dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar speaking speed como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar speaking speed como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPEAKING_SPEED_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPEAKING_SPEED_PROMPT_EFFECT
- Fallback: Reforzar speaking speed con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0665 — prosody_curve_prompt_effect
- Definición: Campo operativo para prosody curve dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prosody curve como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prosody curve como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROSODY_CURVE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROSODY_CURVE_PROMPT_EFFECT
- Fallback: Reforzar prosody curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0666 — pause_signature_prompt_effect
- Definición: Campo operativo para pause signature dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pause signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pause signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PAUSE_SIGNATURE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PAUSE_SIGNATURE_PROMPT_EFFECT
- Fallback: Reforzar pause signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0667 — diction_style_prompt_effect
- Definición: Campo operativo para diction style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar diction style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar diction style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DICTION_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DICTION_STYLE_PROMPT_EFFECT
- Fallback: Reforzar diction style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0668 — emotional_color_prompt_effect
- Definición: Campo operativo para emotional color dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotional color como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotional color como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTIONAL_COLOR_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTIONAL_COLOR_PROMPT_EFFECT
- Fallback: Reforzar emotional color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0669 — micro_laugh_prompt_effect
- Definición: Campo operativo para micro laugh dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar micro laugh como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar micro laugh como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICRO_LAUGH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICRO_LAUGH_PROMPT_EFFECT
- Fallback: Reforzar micro laugh con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0670 — vocal_fatigue_rule_prompt_effect
- Definición: Campo operativo para vocal fatigue rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal fatigue rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal fatigue rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_FATIGUE_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_FATIGUE_RULE_PROMPT_EFFECT
- Fallback: Reforzar vocal fatigue rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0671 — recording_context_rule_prompt_effect
- Definición: Campo operativo para recording context rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar recording context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar recording context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RECORDING_CONTEXT_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RECORDING_CONTEXT_RULE_PROMPT_EF
- Fallback: Reforzar recording context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0672 — voice_identity_lock_prompt_effect
- Definición: Campo operativo para voice identity lock dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice identity lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice identity lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_IDENTITY_LOCK_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_IDENTITY_LOCK_PROMPT_EFFEC
- Fallback: Reforzar voice identity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0673 — voice_scene_response_prompt_effect
- Definición: Campo operativo para voice scene response dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice scene response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice scene response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_SCENE_RESPONSE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_SCENE_RESPONSE_PROMPT_EFFE
- Fallback: Reforzar voice scene response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0674 — accent_profile_prompt_effect
- Definición: Campo operativo para accent profile dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accent profile como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accent profile como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCENT_PROFILE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCENT_PROFILE_PROMPT_EFFECT
- Fallback: Reforzar accent profile con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0675 — peruvian_spanish_level_prompt_effect
- Definición: Campo operativo para peruvian spanish level dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peruvian spanish level como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peruvian spanish level como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERUVIAN_SPANISH_LEVEL_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERUVIAN_SPANISH_LEVEL_PROMPT_EF
- Fallback: Reforzar peruvian spanish level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0676 — latam_neutrality_rule_prompt_effect
- Definición: Campo operativo para latam neutrality rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar latam neutrality rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar latam neutrality rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LATAM_NEUTRALITY_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LATAM_NEUTRALITY_RULE_PROMPT_EFF
- Fallback: Reforzar latam neutrality rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0677 — sociolect_rules_prompt_effect
- Definición: Campo operativo para sociolect rules dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sociolect rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sociolect rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIOLECT_RULES_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIOLECT_RULES_PROMPT_EFFECT
- Fallback: Reforzar sociolect rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0678 — slang_limit_prompt_effect
- Definición: Campo operativo para slang limit dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar slang limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar slang limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SLANG_LIMIT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SLANG_LIMIT_PROMPT_EFFECT
- Fallback: Reforzar slang limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0679 — formality_range_prompt_effect
- Definición: Campo operativo para formality range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar formality range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar formality range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FORMALITY_RANGE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FORMALITY_RANGE_PROMPT_EFFECT
- Fallback: Reforzar formality range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0680 — written_voice_prompt_effect
- Definición: Campo operativo para written voice dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar written voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar written voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRITTEN_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRITTEN_VOICE_PROMPT_EFFECT
- Fallback: Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0681 — caption_style_prompt_effect
- Definición: Campo operativo para caption style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar caption style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar caption style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAPTION_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAPTION_STYLE_PROMPT_EFFECT
- Fallback: Reforzar caption style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0682 — interview_style_prompt_effect
- Definición: Campo operativo para interview style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar interview style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar interview style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INTERVIEW_STYLE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INTERVIEW_STYLE_PROMPT_EFFECT
- Fallback: Reforzar interview style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0683 — dm_style_prompt_effect
- Definición: Campo operativo para dm style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dm style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dm style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DM_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DM_STYLE_PROMPT_EFFECT
- Fallback: Reforzar dm style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0684 — script_style_prompt_effect
- Definición: Campo operativo para script style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar script style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar script style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCRIPT_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCRIPT_STYLE_PROMPT_EFFECT
- Fallback: Reforzar script style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0685 — narration_style_prompt_effect
- Definición: Campo operativo para narration style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar narration style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar narration style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NARRATION_STYLE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NARRATION_STYLE_PROMPT_EFFECT
- Fallback: Reforzar narration style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0686 — inner_monologue_style_prompt_effect
- Definición: Campo operativo para inner monologue style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar inner monologue style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar inner monologue style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INNER_MONOLOGUE_STYLE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INNER_MONOLOGUE_STYLE_PROMPT_EFF
- Fallback: Reforzar inner monologue style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0687 — translation_style_prompt_effect
- Definición: Campo operativo para translation style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar translation style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar translation style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TRANSLATION_STYLE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TRANSLATION_STYLE_PROMPT_EFFECT
- Fallback: Reforzar translation style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0688 — song_vocal_texture_prompt_effect
- Definición: Campo operativo para song vocal texture dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar song vocal texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar song vocal texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SONG_VOCAL_TEXTURE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SONG_VOCAL_TEXTURE_PROMPT_EFFECT
- Fallback: Reforzar song vocal texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0689 — singing_range_prompt_effect
- Definición: Campo operativo para singing range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar singing range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar singing range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SINGING_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SINGING_RANGE_PROMPT_EFFECT
- Fallback: Reforzar singing range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0690 — suno_genre_range_prompt_effect
- Definición: Campo operativo para suno genre range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar suno genre range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar suno genre range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUNO_GENRE_RANGE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUNO_GENRE_RANGE_PROMPT_EFFECT
- Fallback: Reforzar suno genre range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0691 — rhythm_preference_prompt_effect
- Definición: Campo operativo para rhythm preference dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rhythm preference como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rhythm preference como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RHYTHM_PREFERENCE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RHYTHM_PREFERENCE_PROMPT_EFFECT
- Fallback: Reforzar rhythm preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0692 — instrumentation_palette_prompt_effect
- Definición: Campo operativo para instrumentation palette dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar instrumentation palette como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar instrumentation palette como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INSTRUMENTATION_PALETTE_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INSTRUMENTATION_PALETTE_PROMPT_E
- Fallback: Reforzar instrumentation palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0693 — lyric_perspective_prompt_effect
- Definición: Campo operativo para lyric perspective dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lyric perspective como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lyric perspective como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LYRIC_PERSPECTIVE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LYRIC_PERSPECTIVE_PROMPT_EFFECT
- Fallback: Reforzar lyric perspective con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0694 — hook_style_prompt_effect
- Definición: Campo operativo para hook style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hook style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hook style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HOOK_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HOOK_STYLE_PROMPT_EFFECT
- Fallback: Reforzar hook style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0695 — chorus_energy_prompt_effect
- Definición: Campo operativo para chorus energy dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chorus energy como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chorus energy como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHORUS_ENERGY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHORUS_ENERGY_PROMPT_EFFECT
- Fallback: Reforzar chorus energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0696 — spoken_word_option_prompt_effect
- Definición: Campo operativo para spoken word option dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar spoken word option como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar spoken word option como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPOKEN_WORD_OPTION_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPOKEN_WORD_OPTION_PROMPT_EFFECT
- Fallback: Reforzar spoken word option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0697 — no_artist_imitation_rule_prompt_effect
- Definición: Campo operativo para no artist imitation rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no artist imitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no artist imitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_ARTIST_IMITATION_RULE_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_ARTIST_IMITATION_RULE_PROMPT_
- Fallback: Reforzar no artist imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0698 — music_identity_signature_prompt_effect
- Definición: Campo operativo para music identity signature dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar music identity signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar music identity signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUSIC_IDENTITY_SIGNATURE_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUSIC_IDENTITY_SIGNATURE_PROMPT_
- Fallback: Reforzar music identity signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0699 — negative_music_tags_prompt_effect
- Definición: Campo operativo para negative music tags dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar negative music tags como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar negative music tags como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NEGATIVE_MUSIC_TAGS_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NEGATIVE_MUSIC_TAGS_PROMPT_EFFEC
- Fallback: Reforzar negative music tags con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0700 — suno_arrangement_rule_prompt_effect
- Definición: Campo operativo para suno arrangement rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar suno arrangement rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar suno arrangement rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUNO_ARRANGEMENT_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUNO_ARRANGEMENT_RULE_PROMPT_EFF
- Fallback: Reforzar suno arrangement rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0701 — wrong_voice_age_blocker_prompt_effect
- Definición: Campo operativo para wrong voice age blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong voice age blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong voice age blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_VOICE_AGE_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_VOICE_AGE_BLOCKER_PROMPT_E
- Fallback: Reforzar wrong voice age blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0702 — accent_caricature_blocker_prompt_effect
- Definición: Campo operativo para accent caricature blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accent caricature blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accent caricature blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCENT_CARICATURE_BLOCKER_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCENT_CARICATURE_BLOCKER_PROMPT
- Fallback: Reforzar accent caricature blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0703 — generic_caption_blocker_prompt_effect
- Definición: Campo operativo para generic caption blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic caption blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic caption blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_CAPTION_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_CAPTION_BLOCKER_PROMPT_E
- Fallback: Reforzar generic caption blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0704 — artist_imitation_blocker_prompt_effect
- Definición: Campo operativo para artist imitation blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar artist imitation blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar artist imitation blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARTIST_IMITATION_BLOCKER_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARTIST_IMITATION_BLOCKER_PROMPT_
- Fallback: Reforzar artist imitation blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0705 — song_identity_drift_blocker_prompt_effect
- Definición: Campo operativo para song identity drift blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar song identity drift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar song identity drift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SONG_IDENTITY_DRIFT_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SONG_IDENTITY_DRIFT_BLOCKER_PROM
- Fallback: Reforzar song identity drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0706 — voice_text_mismatch_rule_prompt_effect
- Definición: Campo operativo para voice text mismatch rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice text mismatch rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice text mismatch rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_TEXT_MISMATCH_RULE_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_TEXT_MISMATCH_RULE_PROMPT_
- Fallback: Reforzar voice text mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0707 — music_output_repair_prompt_effect
- Definición: Campo operativo para music output repair dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar music output repair como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar music output repair como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUSIC_OUTPUT_REPAIR_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUSIC_OUTPUT_REPAIR_PROMPT_EFFEC
- Fallback: Reforzar music output repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1108 — vocal_age_qa_matrix
- Definición: Campo operativo para vocal age dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_AGE_QA_MATRIX
- Fallback: Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1109 — timbre_qa_matrix
- Definición: Campo operativo para timbre dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar timbre como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar timbre como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TIMBRE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TIMBRE_QA_MATRIX
- Fallback: Reforzar timbre con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1110 — pitch_range_qa_matrix
- Definición: Campo operativo para pitch range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pitch range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pitch range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PITCH_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PITCH_RANGE_QA_MATRIX
- Fallback: Reforzar pitch range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1111 — resonance_place_qa_matrix
- Definición: Campo operativo para resonance place dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar resonance place como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar resonance place como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RESONANCE_PLACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RESONANCE_PLACE_QA_MATRIX
- Fallback: Reforzar resonance place con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1112 — breath_pattern_qa_matrix
- Definición: Campo operativo para breath pattern dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar breath pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar breath pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BREATH_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BREATH_PATTERN_QA_MATRIX
- Fallback: Reforzar breath pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1113 — speaking_speed_qa_matrix
- Definición: Campo operativo para speaking speed dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar speaking speed como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar speaking speed como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPEAKING_SPEED_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPEAKING_SPEED_QA_MATRIX
- Fallback: Reforzar speaking speed con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1114 — prosody_curve_qa_matrix
- Definición: Campo operativo para prosody curve dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prosody curve como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prosody curve como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROSODY_CURVE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROSODY_CURVE_QA_MATRIX
- Fallback: Reforzar prosody curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1115 — pause_signature_qa_matrix
- Definición: Campo operativo para pause signature dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pause signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pause signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PAUSE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PAUSE_SIGNATURE_QA_MATRIX
- Fallback: Reforzar pause signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1116 — diction_style_qa_matrix
- Definición: Campo operativo para diction style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar diction style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar diction style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DICTION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DICTION_STYLE_QA_MATRIX
- Fallback: Reforzar diction style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1117 — emotional_color_qa_matrix
- Definición: Campo operativo para emotional color dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotional color como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotional color como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTIONAL_COLOR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTIONAL_COLOR_QA_MATRIX
- Fallback: Reforzar emotional color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1118 — micro_laugh_qa_matrix
- Definición: Campo operativo para micro laugh dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar micro laugh como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar micro laugh como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICRO_LAUGH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICRO_LAUGH_QA_MATRIX
- Fallback: Reforzar micro laugh con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1119 — vocal_fatigue_rule_qa_matrix
- Definición: Campo operativo para vocal fatigue rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal fatigue rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal fatigue rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_FATIGUE_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_FATIGUE_RULE_QA_MATRIX
- Fallback: Reforzar vocal fatigue rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1120 — recording_context_rule_qa_matrix
- Definición: Campo operativo para recording context rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar recording context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar recording context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RECORDING_CONTEXT_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RECORDING_CONTEXT_RULE_QA_MATRIX
- Fallback: Reforzar recording context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1121 — voice_identity_lock_qa_matrix
- Definición: Campo operativo para voice identity lock dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice identity lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice identity lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_IDENTITY_LOCK_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_IDENTITY_LOCK_QA_MATRIX
- Fallback: Reforzar voice identity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1122 — voice_scene_response_qa_matrix
- Definición: Campo operativo para voice scene response dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice scene response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice scene response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_SCENE_RESPONSE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_SCENE_RESPONSE_QA_MATRIX
- Fallback: Reforzar voice scene response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1123 — accent_profile_qa_matrix
- Definición: Campo operativo para accent profile dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accent profile como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accent profile como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCENT_PROFILE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCENT_PROFILE_QA_MATRIX
- Fallback: Reforzar accent profile con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1124 — peruvian_spanish_level_qa_matrix
- Definición: Campo operativo para peruvian spanish level dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peruvian spanish level como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peruvian spanish level como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERUVIAN_SPANISH_LEVEL_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERUVIAN_SPANISH_LEVEL_QA_MATRIX
- Fallback: Reforzar peruvian spanish level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1125 — latam_neutrality_rule_qa_matrix
- Definición: Campo operativo para latam neutrality rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar latam neutrality rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar latam neutrality rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LATAM_NEUTRALITY_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LATAM_NEUTRALITY_RULE_QA_MATRIX
- Fallback: Reforzar latam neutrality rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1126 — sociolect_rules_qa_matrix
- Definición: Campo operativo para sociolect rules dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sociolect rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sociolect rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIOLECT_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIOLECT_RULES_QA_MATRIX
- Fallback: Reforzar sociolect rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1127 — slang_limit_qa_matrix
- Definición: Campo operativo para slang limit dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar slang limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar slang limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SLANG_LIMIT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SLANG_LIMIT_QA_MATRIX
- Fallback: Reforzar slang limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1128 — formality_range_qa_matrix
- Definición: Campo operativo para formality range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar formality range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar formality range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FORMALITY_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FORMALITY_RANGE_QA_MATRIX
- Fallback: Reforzar formality range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1129 — written_voice_qa_matrix
- Definición: Campo operativo para written voice dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar written voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar written voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRITTEN_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRITTEN_VOICE_QA_MATRIX
- Fallback: Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1130 — caption_style_qa_matrix
- Definición: Campo operativo para caption style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar caption style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar caption style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAPTION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAPTION_STYLE_QA_MATRIX
- Fallback: Reforzar caption style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1131 — interview_style_qa_matrix
- Definición: Campo operativo para interview style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar interview style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar interview style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INTERVIEW_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INTERVIEW_STYLE_QA_MATRIX
- Fallback: Reforzar interview style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1132 — dm_style_qa_matrix
- Definición: Campo operativo para dm style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dm style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dm style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DM_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DM_STYLE_QA_MATRIX
- Fallback: Reforzar dm style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1133 — script_style_qa_matrix
- Definición: Campo operativo para script style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar script style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar script style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCRIPT_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCRIPT_STYLE_QA_MATRIX
- Fallback: Reforzar script style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1134 — narration_style_qa_matrix
- Definición: Campo operativo para narration style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar narration style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar narration style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NARRATION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NARRATION_STYLE_QA_MATRIX
- Fallback: Reforzar narration style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1135 — inner_monologue_style_qa_matrix
- Definición: Campo operativo para inner monologue style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar inner monologue style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar inner monologue style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INNER_MONOLOGUE_STYLE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INNER_MONOLOGUE_STYLE_QA_MATRIX
- Fallback: Reforzar inner monologue style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1136 — translation_style_qa_matrix
- Definición: Campo operativo para translation style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar translation style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar translation style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TRANSLATION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TRANSLATION_STYLE_QA_MATRIX
- Fallback: Reforzar translation style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1137 — song_vocal_texture_qa_matrix
- Definición: Campo operativo para song vocal texture dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar song vocal texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar song vocal texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SONG_VOCAL_TEXTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SONG_VOCAL_TEXTURE_QA_MATRIX
- Fallback: Reforzar song vocal texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1138 — singing_range_qa_matrix
- Definición: Campo operativo para singing range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar singing range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar singing range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SINGING_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SINGING_RANGE_QA_MATRIX
- Fallback: Reforzar singing range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1139 — suno_genre_range_qa_matrix
- Definición: Campo operativo para suno genre range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar suno genre range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar suno genre range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUNO_GENRE_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUNO_GENRE_RANGE_QA_MATRIX
- Fallback: Reforzar suno genre range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1140 — rhythm_preference_qa_matrix
- Definición: Campo operativo para rhythm preference dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rhythm preference como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rhythm preference como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RHYTHM_PREFERENCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RHYTHM_PREFERENCE_QA_MATRIX
- Fallback: Reforzar rhythm preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1141 — instrumentation_palette_qa_matrix
- Definición: Campo operativo para instrumentation palette dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar instrumentation palette como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar instrumentation palette como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INSTRUMENTATION_PALETTE_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INSTRUMENTATION_PALETTE_QA_MATRI
- Fallback: Reforzar instrumentation palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1142 — lyric_perspective_qa_matrix
- Definición: Campo operativo para lyric perspective dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lyric perspective como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lyric perspective como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LYRIC_PERSPECTIVE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LYRIC_PERSPECTIVE_QA_MATRIX
- Fallback: Reforzar lyric perspective con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1143 — hook_style_qa_matrix
- Definición: Campo operativo para hook style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hook style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hook style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HOOK_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HOOK_STYLE_QA_MATRIX
- Fallback: Reforzar hook style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1144 — chorus_energy_qa_matrix
- Definición: Campo operativo para chorus energy dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chorus energy como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chorus energy como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHORUS_ENERGY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHORUS_ENERGY_QA_MATRIX
- Fallback: Reforzar chorus energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1145 — spoken_word_option_qa_matrix
- Definición: Campo operativo para spoken word option dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar spoken word option como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar spoken word option como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPOKEN_WORD_OPTION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPOKEN_WORD_OPTION_QA_MATRIX
- Fallback: Reforzar spoken word option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1146 — no_artist_imitation_rule_qa_matrix
- Definición: Campo operativo para no artist imitation rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no artist imitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no artist imitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_ARTIST_IMITATION_RULE_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_ARTIST_IMITATION_RULE_QA_MATR
- Fallback: Reforzar no artist imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1147 — music_identity_signature_qa_matrix
- Definición: Campo operativo para music identity signature dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar music identity signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar music identity signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUSIC_IDENTITY_SIGNATURE_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUSIC_IDENTITY_SIGNATURE_QA_MATR
- Fallback: Reforzar music identity signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1148 — negative_music_tags_qa_matrix
- Definición: Campo operativo para negative music tags dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar negative music tags como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar negative music tags como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NEGATIVE_MUSIC_TAGS_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NEGATIVE_MUSIC_TAGS_QA_MATRIX
- Fallback: Reforzar negative music tags con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1149 — suno_arrangement_rule_qa_matrix
- Definición: Campo operativo para suno arrangement rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar suno arrangement rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar suno arrangement rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUNO_ARRANGEMENT_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUNO_ARRANGEMENT_RULE_QA_MATRIX
- Fallback: Reforzar suno arrangement rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1150 — wrong_voice_age_blocker_qa_matrix
- Definición: Campo operativo para wrong voice age blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong voice age blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong voice age blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_VOICE_AGE_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_VOICE_AGE_BLOCKER_QA_MATRI
- Fallback: Reforzar wrong voice age blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1151 — accent_caricature_blocker_qa_matrix
- Definición: Campo operativo para accent caricature blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accent caricature blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accent caricature blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCENT_CARICATURE_BLOCKER_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCENT_CARICATURE_BLOCKER_QA_MAT
- Fallback: Reforzar accent caricature blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1152 — generic_caption_blocker_qa_matrix
- Definición: Campo operativo para generic caption blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic caption blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic caption blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_CAPTION_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_CAPTION_BLOCKER_QA_MATRI
- Fallback: Reforzar generic caption blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1153 — artist_imitation_blocker_qa_matrix
- Definición: Campo operativo para artist imitation blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar artist imitation blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar artist imitation blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARTIST_IMITATION_BLOCKER_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARTIST_IMITATION_BLOCKER_QA_MATR
- Fallback: Reforzar artist imitation blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1154 — song_identity_drift_blocker_qa_matrix
- Definición: Campo operativo para song identity drift blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar song identity drift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar song identity drift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SONG_IDENTITY_DRIFT_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SONG_IDENTITY_DRIFT_BLOCKER_QA_M
- Fallback: Reforzar song identity drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1155 — voice_text_mismatch_rule_qa_matrix
- Definición: Campo operativo para voice text mismatch rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice text mismatch rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice text mismatch rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_TEXT_MISMATCH_RULE_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_TEXT_MISMATCH_RULE_QA_MATR
- Fallback: Reforzar voice text mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1156 — music_output_repair_qa_matrix
- Definición: Campo operativo para music output repair dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar music output repair como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar music output repair como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUSIC_OUTPUT_REPAIR_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUSIC_OUTPUT_REPAIR_QA_MATRIX
- Fallback: Reforzar music output repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1557 — vocal_age_vendor_repair
- Definición: Campo operativo para vocal age dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_AGE_VENDOR_REPAIR
- Fallback: Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1558 — timbre_vendor_repair
- Definición: Campo operativo para timbre dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar timbre como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar timbre como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TIMBRE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TIMBRE_VENDOR_REPAIR
- Fallback: Reforzar timbre con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1559 — pitch_range_vendor_repair
- Definición: Campo operativo para pitch range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pitch range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pitch range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PITCH_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PITCH_RANGE_VENDOR_REPAIR
- Fallback: Reforzar pitch range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1560 — resonance_place_vendor_repair
- Definición: Campo operativo para resonance place dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar resonance place como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar resonance place como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RESONANCE_PLACE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RESONANCE_PLACE_VENDOR_REPAIR
- Fallback: Reforzar resonance place con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1561 — breath_pattern_vendor_repair
- Definición: Campo operativo para breath pattern dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar breath pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar breath pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BREATH_PATTERN_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BREATH_PATTERN_VENDOR_REPAIR
- Fallback: Reforzar breath pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1562 — speaking_speed_vendor_repair
- Definición: Campo operativo para speaking speed dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar speaking speed como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar speaking speed como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPEAKING_SPEED_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPEAKING_SPEED_VENDOR_REPAIR
- Fallback: Reforzar speaking speed con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1563 — prosody_curve_vendor_repair
- Definición: Campo operativo para prosody curve dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prosody curve como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prosody curve como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROSODY_CURVE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROSODY_CURVE_VENDOR_REPAIR
- Fallback: Reforzar prosody curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1564 — pause_signature_vendor_repair
- Definición: Campo operativo para pause signature dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pause signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pause signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PAUSE_SIGNATURE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PAUSE_SIGNATURE_VENDOR_REPAIR
- Fallback: Reforzar pause signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1565 — diction_style_vendor_repair
- Definición: Campo operativo para diction style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar diction style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar diction style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DICTION_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DICTION_STYLE_VENDOR_REPAIR
- Fallback: Reforzar diction style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1566 — emotional_color_vendor_repair
- Definición: Campo operativo para emotional color dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotional color como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotional color como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTIONAL_COLOR_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTIONAL_COLOR_VENDOR_REPAIR
- Fallback: Reforzar emotional color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1567 — micro_laugh_vendor_repair
- Definición: Campo operativo para micro laugh dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar micro laugh como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar micro laugh como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICRO_LAUGH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICRO_LAUGH_VENDOR_REPAIR
- Fallback: Reforzar micro laugh con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1568 — vocal_fatigue_rule_vendor_repair
- Definición: Campo operativo para vocal fatigue rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal fatigue rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal fatigue rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_FATIGUE_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_FATIGUE_RULE_VENDOR_REPAIR
- Fallback: Reforzar vocal fatigue rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1569 — recording_context_rule_vendor_repair
- Definición: Campo operativo para recording context rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar recording context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar recording context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RECORDING_CONTEXT_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RECORDING_CONTEXT_RULE_VENDOR_RE
- Fallback: Reforzar recording context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1570 — voice_identity_lock_vendor_repair
- Definición: Campo operativo para voice identity lock dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice identity lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice identity lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_IDENTITY_LOCK_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_IDENTITY_LOCK_VENDOR_REPAI
- Fallback: Reforzar voice identity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1571 — voice_scene_response_vendor_repair
- Definición: Campo operativo para voice scene response dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice scene response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice scene response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_SCENE_RESPONSE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_SCENE_RESPONSE_VENDOR_REPA
- Fallback: Reforzar voice scene response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1572 — accent_profile_vendor_repair
- Definición: Campo operativo para accent profile dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accent profile como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accent profile como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCENT_PROFILE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCENT_PROFILE_VENDOR_REPAIR
- Fallback: Reforzar accent profile con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1573 — peruvian_spanish_level_vendor_repair
- Definición: Campo operativo para peruvian spanish level dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peruvian spanish level como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peruvian spanish level como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERUVIAN_SPANISH_LEVEL_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERUVIAN_SPANISH_LEVEL_VENDOR_RE
- Fallback: Reforzar peruvian spanish level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1574 — latam_neutrality_rule_vendor_repair
- Definición: Campo operativo para latam neutrality rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar latam neutrality rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar latam neutrality rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LATAM_NEUTRALITY_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LATAM_NEUTRALITY_RULE_VENDOR_REP
- Fallback: Reforzar latam neutrality rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1575 — sociolect_rules_vendor_repair
- Definición: Campo operativo para sociolect rules dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sociolect rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sociolect rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIOLECT_RULES_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIOLECT_RULES_VENDOR_REPAIR
- Fallback: Reforzar sociolect rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1576 — slang_limit_vendor_repair
- Definición: Campo operativo para slang limit dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar slang limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar slang limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SLANG_LIMIT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SLANG_LIMIT_VENDOR_REPAIR
- Fallback: Reforzar slang limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1577 — formality_range_vendor_repair
- Definición: Campo operativo para formality range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar formality range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar formality range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FORMALITY_RANGE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FORMALITY_RANGE_VENDOR_REPAIR
- Fallback: Reforzar formality range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1578 — written_voice_vendor_repair
- Definición: Campo operativo para written voice dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar written voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar written voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRITTEN_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRITTEN_VOICE_VENDOR_REPAIR
- Fallback: Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1579 — caption_style_vendor_repair
- Definición: Campo operativo para caption style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar caption style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar caption style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAPTION_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAPTION_STYLE_VENDOR_REPAIR
- Fallback: Reforzar caption style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1580 — interview_style_vendor_repair
- Definición: Campo operativo para interview style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar interview style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar interview style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INTERVIEW_STYLE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INTERVIEW_STYLE_VENDOR_REPAIR
- Fallback: Reforzar interview style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1581 — dm_style_vendor_repair
- Definición: Campo operativo para dm style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dm style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dm style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DM_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DM_STYLE_VENDOR_REPAIR
- Fallback: Reforzar dm style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1582 — script_style_vendor_repair
- Definición: Campo operativo para script style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar script style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar script style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCRIPT_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCRIPT_STYLE_VENDOR_REPAIR
- Fallback: Reforzar script style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1583 — narration_style_vendor_repair
- Definición: Campo operativo para narration style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar narration style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar narration style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NARRATION_STYLE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NARRATION_STYLE_VENDOR_REPAIR
- Fallback: Reforzar narration style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1584 — inner_monologue_style_vendor_repair
- Definición: Campo operativo para inner monologue style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar inner monologue style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar inner monologue style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INNER_MONOLOGUE_STYLE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INNER_MONOLOGUE_STYLE_VENDOR_REP
- Fallback: Reforzar inner monologue style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1585 — translation_style_vendor_repair
- Definición: Campo operativo para translation style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar translation style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar translation style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TRANSLATION_STYLE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TRANSLATION_STYLE_VENDOR_REPAIR
- Fallback: Reforzar translation style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1586 — song_vocal_texture_vendor_repair
- Definición: Campo operativo para song vocal texture dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar song vocal texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar song vocal texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SONG_VOCAL_TEXTURE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SONG_VOCAL_TEXTURE_VENDOR_REPAIR
- Fallback: Reforzar song vocal texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1587 — singing_range_vendor_repair
- Definición: Campo operativo para singing range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar singing range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar singing range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SINGING_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SINGING_RANGE_VENDOR_REPAIR
- Fallback: Reforzar singing range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1588 — suno_genre_range_vendor_repair
- Definición: Campo operativo para suno genre range dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar suno genre range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar suno genre range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUNO_GENRE_RANGE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUNO_GENRE_RANGE_VENDOR_REPAIR
- Fallback: Reforzar suno genre range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1589 — rhythm_preference_vendor_repair
- Definición: Campo operativo para rhythm preference dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rhythm preference como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rhythm preference como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RHYTHM_PREFERENCE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RHYTHM_PREFERENCE_VENDOR_REPAIR
- Fallback: Reforzar rhythm preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1590 — instrumentation_palette_vendor_repair
- Definición: Campo operativo para instrumentation palette dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar instrumentation palette como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar instrumentation palette como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INSTRUMENTATION_PALETTE_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INSTRUMENTATION_PALETTE_VENDOR_R
- Fallback: Reforzar instrumentation palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1591 — lyric_perspective_vendor_repair
- Definición: Campo operativo para lyric perspective dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lyric perspective como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lyric perspective como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LYRIC_PERSPECTIVE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LYRIC_PERSPECTIVE_VENDOR_REPAIR
- Fallback: Reforzar lyric perspective con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1592 — hook_style_vendor_repair
- Definición: Campo operativo para hook style dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hook style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hook style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HOOK_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HOOK_STYLE_VENDOR_REPAIR
- Fallback: Reforzar hook style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1593 — chorus_energy_vendor_repair
- Definición: Campo operativo para chorus energy dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chorus energy como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chorus energy como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHORUS_ENERGY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHORUS_ENERGY_VENDOR_REPAIR
- Fallback: Reforzar chorus energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1594 — spoken_word_option_vendor_repair
- Definición: Campo operativo para spoken word option dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar spoken word option como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar spoken word option como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPOKEN_WORD_OPTION_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPOKEN_WORD_OPTION_VENDOR_REPAIR
- Fallback: Reforzar spoken word option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1595 — no_artist_imitation_rule_vendor_repair
- Definición: Campo operativo para no artist imitation rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no artist imitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no artist imitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_ARTIST_IMITATION_RULE_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_ARTIST_IMITATION_RULE_VENDOR_
- Fallback: Reforzar no artist imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1596 — music_identity_signature_vendor_repair
- Definición: Campo operativo para music identity signature dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar music identity signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar music identity signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUSIC_IDENTITY_SIGNATURE_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUSIC_IDENTITY_SIGNATURE_VENDOR_
- Fallback: Reforzar music identity signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1597 — negative_music_tags_vendor_repair
- Definición: Campo operativo para negative music tags dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar negative music tags como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar negative music tags como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NEGATIVE_MUSIC_TAGS_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NEGATIVE_MUSIC_TAGS_VENDOR_REPAI
- Fallback: Reforzar negative music tags con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1598 — suno_arrangement_rule_vendor_repair
- Definición: Campo operativo para suno arrangement rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar suno arrangement rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar suno arrangement rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUNO_ARRANGEMENT_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUNO_ARRANGEMENT_RULE_VENDOR_REP
- Fallback: Reforzar suno arrangement rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1599 — wrong_voice_age_blocker_vendor_repair
- Definición: Campo operativo para wrong voice age blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong voice age blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong voice age blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_VOICE_AGE_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_VOICE_AGE_BLOCKER_VENDOR_R
- Fallback: Reforzar wrong voice age blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1600 — accent_caricature_blocker_vendor_repair
- Definición: Campo operativo para accent caricature blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accent caricature blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accent caricature blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCENT_CARICATURE_BLOCKER_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCENT_CARICATURE_BLOCKER_VENDOR
- Fallback: Reforzar accent caricature blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1601 — generic_caption_blocker_vendor_repair
- Definición: Campo operativo para generic caption blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic caption blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic caption blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_CAPTION_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_CAPTION_BLOCKER_VENDOR_R
- Fallback: Reforzar generic caption blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1602 — artist_imitation_blocker_vendor_repair
- Definición: Campo operativo para artist imitation blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar artist imitation blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar artist imitation blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARTIST_IMITATION_BLOCKER_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARTIST_IMITATION_BLOCKER_VENDOR_
- Fallback: Reforzar artist imitation blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1603 — song_identity_drift_blocker_vendor_repair
- Definición: Campo operativo para song identity drift blocker dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar song identity drift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar song identity drift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SONG_IDENTITY_DRIFT_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SONG_IDENTITY_DRIFT_BLOCKER_VEND
- Fallback: Reforzar song identity drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1604 — voice_text_mismatch_rule_vendor_repair
- Definición: Campo operativo para voice text mismatch rule dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice text mismatch rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice text mismatch rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_TEXT_MISMATCH_RULE_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_TEXT_MISMATCH_RULE_VENDOR_
- Fallback: Reforzar voice text mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1605 — music_output_repair_vendor_repair
- Definición: Campo operativo para music output repair dentro de Voz hablada, lenguaje, acento, escritura, canto y música. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar music output repair como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar music output repair como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUSIC_OUTPUT_REPAIR_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUSIC_OUTPUT_REPAIR_VENDOR_REPAI
- Fallback: Reforzar music output repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
