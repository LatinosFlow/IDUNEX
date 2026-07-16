## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Identidad, memoria, biografía, cultura segura y persona digital adulta

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_IDENTITY_0001` | `canonical_name` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CANONICAL_NAME_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar canonical name con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0002` | `model_code` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MODEL_CODE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar model code con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0003` | `aliases` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ALIASES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar aliases con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0004` | `adult_age` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar adult age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0005` | `visual_age` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VISUAL_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar visual age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0006` | `body_age` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar body age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0007` | `vocal_age` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0008` | `project_role` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_ROLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar project role con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0009` | `canon_scope` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CANON_SCOPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar canon scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0010` | `mutable_scope` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUTABLE_SCOPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar mutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0011` | `immutable_scope` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMMUTABLE_SCOPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar immutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0012` | `identity_status` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IDENTITY_STATUS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar identity status con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0013` | `relationship_to_project` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RELATIONSHIP_TO_PROJECT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar relationship to project con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0014` | `persona_boundary` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERSONA_BOUNDARY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar persona boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0015` | `private_public_boundary` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRIVATE_PUBLIC_BOUNDARY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar private public boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0016` | `birth_context` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BIRTH_CONTEXT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar birth context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0017` | `family_structure` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAMILY_STRUCTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar family structure con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0018` | `migration_trace` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIGRATION_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar migration trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0019` | `education_trace` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EDUCATION_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar education trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0020` | `work_trace` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WORK_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar work trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0021` | `social_environment` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIAL_ENVIRONMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar social environment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0022` | `formative_events` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FORMATIVE_EVENTS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar formative events con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0023` | `life_turning_points` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIFE_TURNING_POINTS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar life turning points con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0024` | `habit_map` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HABIT_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar habit map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0025` | `daily_routines` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DAILY_ROUTINES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar daily routines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0026` | `memory_triggers` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MEMORY_TRIGGERS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar memory triggers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0027` | `emotional_anchors` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTIONAL_ANCHORS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar emotional anchors con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0028` | `personal_limits` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERSONAL_LIMITS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar personal limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0029` | `conflict_history` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFLICT_HISTORY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar conflict history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0030` | `growth_arc` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GROWTH_ARC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar growth arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0031` | `temperament` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEMPERAMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar temperament con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0032` | `motivation_stack` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTIVATION_STACK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar motivation stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0033` | `fear_stack` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FEAR_STACK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fear stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0034` | `desire_stack` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DESIRE_STACK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar desire stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0035` | `values_map` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VALUES_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar values map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0036` | `moral_boundaries` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MORAL_BOUNDARIES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar moral boundaries con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0037` | `worldview` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WORLDVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar worldview con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0038` | `contradictions` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTRADICTIONS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar contradictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0039` | `humor_style` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HUMOR_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar humor style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0040` | `decision_style` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DECISION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar decision style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0041` | `social_reaction` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIAL_REACTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar social reaction con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0042` | `conflict_response` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFLICT_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar conflict response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0043` | `confidence_pattern` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFIDENCE_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar confidence pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0044` | `attention_style` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ATTENTION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar attention style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0045` | `empathy_pattern` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMPATHY_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar empathy pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0046` | `inner_voice` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INNER_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar inner voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0047` | `written_voice` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRITTEN_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0048` | `speech_register` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPEECH_REGISTER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar speech register con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0049` | `silence_style` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SILENCE_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar silence style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0050` | `vocabulary_range` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCABULARY_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar vocabulary range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0051` | `peruvian_latam_usage` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERUVIAN_LATAM_USAGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar peruvian latam usage con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0052` | `sociolect_limit` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIOLECT_LIMIT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sociolect limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0053` | `interview_voice` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INTERVIEW_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar interview voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0054` | `caption_voice` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAPTION_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar caption voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0055` | `script_voice` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCRIPT_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar script voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0056` | `no_generic_text_rule` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_GENERIC_TEXT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar no generic text rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0057` | `non_imitation_rule` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NON_IMITATION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar non imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0450` | `canonical_name_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CANONICAL_NAME_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar canonical name con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0451` | `model_code_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MODEL_CODE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar model code con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0452` | `aliases_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ALIASES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar aliases con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0453` | `adult_age_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0454` | `visual_age_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VISUAL_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar visual age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0455` | `body_age_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0456` | `vocal_age_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0457` | `project_role_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_ROLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project role con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0458` | `canon_scope_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CANON_SCOPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar canon scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0459` | `mutable_scope_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUTABLE_SCOPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0460` | `immutable_scope_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMMUTABLE_SCOPE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar immutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0461` | `identity_status_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IDENTITY_STATUS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar identity status con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0462` | `relationship_to_project_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RELATIONSHIP_TO_PROJECT_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar relationship to project con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0463` | `persona_boundary_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERSONA_BOUNDARY_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar persona boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0464` | `private_public_boundary_prompt_effect` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRIVATE_PUBLIC_BOUNDARY_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar private public boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0465` | `birth_context_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BIRTH_CONTEXT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar birth context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0466` | `family_structure_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAMILY_STRUCTURE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar family structure con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0467` | `migration_trace_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIGRATION_TRACE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar migration trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0468` | `education_trace_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EDUCATION_TRACE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar education trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0469` | `work_trace_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WORK_TRACE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar work trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0470` | `social_environment_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIAL_ENVIRONMENT_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar social environment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0471` | `formative_events_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FORMATIVE_EVENTS_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar formative events con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0472` | `life_turning_points_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIFE_TURNING_POINTS_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar life turning points con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0473` | `habit_map_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HABIT_MAP_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar habit map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0474` | `daily_routines_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DAILY_ROUTINES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar daily routines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0475` | `memory_triggers_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MEMORY_TRIGGERS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar memory triggers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0476` | `emotional_anchors_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTIONAL_ANCHORS_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotional anchors con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0477` | `personal_limits_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERSONAL_LIMITS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar personal limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0478` | `conflict_history_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFLICT_HISTORY_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar conflict history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0479` | `growth_arc_prompt_effect` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GROWTH_ARC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar growth arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0480` | `temperament_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEMPERAMENT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar temperament con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0481` | `motivation_stack_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTIVATION_STACK_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motivation stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0482` | `fear_stack_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FEAR_STACK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fear stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0483` | `desire_stack_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DESIRE_STACK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar desire stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0484` | `values_map_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VALUES_MAP_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar values map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0485` | `moral_boundaries_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MORAL_BOUNDARIES_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar moral boundaries con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0486` | `worldview_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WORLDVIEW_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar worldview con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0487` | `contradictions_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTRADICTIONS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contradictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0488` | `humor_style_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HUMOR_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar humor style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0489` | `decision_style_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DECISION_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar decision style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0490` | `social_reaction_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIAL_REACTION_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar social reaction con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0491` | `conflict_response_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFLICT_RESPONSE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar conflict response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0492` | `confidence_pattern_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFIDENCE_PATTERN_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar confidence pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0493` | `attention_style_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ATTENTION_STYLE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar attention style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0494` | `empathy_pattern_prompt_effect` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMPATHY_PATTERN_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar empathy pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0495` | `inner_voice_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INNER_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar inner voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0496` | `written_voice_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRITTEN_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0497` | `speech_register_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPEECH_REGISTER_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar speech register con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0498` | `silence_style_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SILENCE_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar silence style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0499` | `vocabulary_range_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCABULARY_RANGE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocabulary range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0500` | `peruvian_latam_usage_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERUVIAN_LATAM_USAGE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peruvian latam usage con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0501` | `sociolect_limit_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIOLECT_LIMIT_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sociolect limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0502` | `interview_voice_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INTERVIEW_VOICE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar interview voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0503` | `caption_voice_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAPTION_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar caption voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0504` | `script_voice_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCRIPT_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar script voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0505` | `no_generic_text_rule_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_GENERIC_TEXT_RULE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no generic text rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0506` | `non_imitation_rule_prompt_effect` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NON_IMITATION_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar non imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0899` | `canonical_name_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CANONICAL_NAME_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar canonical name con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0900` | `model_code_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MODEL_CODE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar model code con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0901` | `aliases_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ALIASES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar aliases con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0902` | `adult_age_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0903` | `visual_age_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VISUAL_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar visual age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0904` | `body_age_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0905` | `vocal_age_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0906` | `project_role_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_ROLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project role con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0907` | `canon_scope_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CANON_SCOPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar canon scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0908` | `mutable_scope_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUTABLE_SCOPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0909` | `immutable_scope_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMMUTABLE_SCOPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar immutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0910` | `identity_status_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IDENTITY_STATUS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar identity status con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0911` | `relationship_to_project_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RELATIONSHIP_TO_PROJECT_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar relationship to project con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_0912` | `persona_boundary_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERSONA_BOUNDARY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar persona boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0913` | `private_public_boundary_qa_matrix` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRIVATE_PUBLIC_BOUNDARY_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar private public boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0914` | `birth_context_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BIRTH_CONTEXT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar birth context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0915` | `family_structure_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAMILY_STRUCTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar family structure con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0916` | `migration_trace_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIGRATION_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar migration trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0917` | `education_trace_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EDUCATION_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar education trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0918` | `work_trace_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WORK_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar work trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0919` | `social_environment_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIAL_ENVIRONMENT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar social environment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0920` | `formative_events_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FORMATIVE_EVENTS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar formative events con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0921` | `life_turning_points_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIFE_TURNING_POINTS_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar life turning points con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0922` | `habit_map_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HABIT_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar habit map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0923` | `daily_routines_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DAILY_ROUTINES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar daily routines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0924` | `memory_triggers_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MEMORY_TRIGGERS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar memory triggers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0925` | `emotional_anchors_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTIONAL_ANCHORS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotional anchors con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0926` | `personal_limits_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERSONAL_LIMITS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar personal limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0927` | `conflict_history_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFLICT_HISTORY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar conflict history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0928` | `growth_arc_qa_matrix` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GROWTH_ARC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar growth arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0929` | `temperament_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEMPERAMENT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar temperament con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0930` | `motivation_stack_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTIVATION_STACK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motivation stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0931` | `fear_stack_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FEAR_STACK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fear stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0932` | `desire_stack_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DESIRE_STACK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar desire stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0933` | `values_map_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VALUES_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar values map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0934` | `moral_boundaries_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MORAL_BOUNDARIES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar moral boundaries con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0935` | `worldview_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WORLDVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar worldview con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0936` | `contradictions_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTRADICTIONS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contradictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0937` | `humor_style_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HUMOR_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar humor style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0938` | `decision_style_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DECISION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar decision style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0939` | `social_reaction_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIAL_REACTION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar social reaction con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0940` | `conflict_response_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFLICT_RESPONSE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar conflict response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0941` | `confidence_pattern_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFIDENCE_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar confidence pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0942` | `attention_style_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ATTENTION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar attention style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0943` | `empathy_pattern_qa_matrix` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMPATHY_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar empathy pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0944` | `inner_voice_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INNER_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar inner voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0945` | `written_voice_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRITTEN_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0946` | `speech_register_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPEECH_REGISTER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar speech register con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0947` | `silence_style_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SILENCE_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar silence style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0948` | `vocabulary_range_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCABULARY_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocabulary range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0949` | `peruvian_latam_usage_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERUVIAN_LATAM_USAGE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peruvian latam usage con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0950` | `sociolect_limit_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIOLECT_LIMIT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sociolect limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0951` | `interview_voice_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INTERVIEW_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar interview voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0952` | `caption_voice_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAPTION_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar caption voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0953` | `script_voice_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCRIPT_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar script voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0954` | `no_generic_text_rule_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_GENERIC_TEXT_RULE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no generic text rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_0955` | `non_imitation_rule_qa_matrix` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NON_IMITATION_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar non imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_1348` | `canonical_name_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CANONICAL_NAME_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar canonical name con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_1349` | `model_code_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MODEL_CODE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar model code con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_1350` | `aliases_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ALIASES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar aliases con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1351` | `adult_age_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1352` | `visual_age_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VISUAL_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar visual age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1353` | `body_age_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1354` | `vocal_age_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCAL_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1355` | `project_role_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_ROLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project role con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1356` | `canon_scope_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CANON_SCOPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar canon scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_1357` | `mutable_scope_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MUTABLE_SCOPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_1358` | `immutable_scope_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMMUTABLE_SCOPE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar immutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_1359` | `identity_status_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IDENTITY_STATUS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar identity status con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1360` | `relationship_to_project_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RELATIONSHIP_TO_PROJECT_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar relationship to project con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_IDENTITY_1361` | `persona_boundary_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERSONA_BOUNDARY_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar persona boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1362` | `private_public_boundary_vendor_repair` | canon | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRIVATE_PUBLIC_BOUNDARY_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar private public boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1363` | `birth_context_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BIRTH_CONTEXT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar birth context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1364` | `family_structure_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAMILY_STRUCTURE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar family structure con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_1365` | `migration_trace_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIGRATION_TRACE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar migration trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1366` | `education_trace_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EDUCATION_TRACE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar education trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1367` | `work_trace_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WORK_TRACE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar work trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1368` | `social_environment_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIAL_ENVIRONMENT_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar social environment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1369` | `formative_events_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FORMATIVE_EVENTS_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar formative events con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1370` | `life_turning_points_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIFE_TURNING_POINTS_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar life turning points con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1371` | `habit_map_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HABIT_MAP_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar habit map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1372` | `daily_routines_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DAILY_ROUTINES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar daily routines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1373` | `memory_triggers_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MEMORY_TRIGGERS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar memory triggers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1374` | `emotional_anchors_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTIONAL_ANCHORS_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotional anchors con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1375` | `personal_limits_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERSONAL_LIMITS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar personal limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1376` | `conflict_history_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFLICT_HISTORY_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar conflict history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1377` | `growth_arc_vendor_repair` | biography | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GROWTH_ARC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar growth arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1378` | `temperament_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEMPERAMENT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar temperament con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1379` | `motivation_stack_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTIVATION_STACK_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motivation stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1380` | `fear_stack_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FEAR_STACK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fear stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1381` | `desire_stack_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DESIRE_STACK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar desire stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_1382` | `values_map_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VALUES_MAP_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar values map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1383` | `moral_boundaries_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MORAL_BOUNDARIES_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar moral boundaries con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_1384` | `worldview_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WORLDVIEW_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar worldview con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1385` | `contradictions_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTRADICTIONS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contradictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1386` | `humor_style_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HUMOR_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar humor style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1387` | `decision_style_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DECISION_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar decision style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1388` | `social_reaction_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIAL_REACTION_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar social reaction con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1389` | `conflict_response_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFLICT_RESPONSE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar conflict response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1390` | `confidence_pattern_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONFIDENCE_PATTERN_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar confidence pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1391` | `attention_style_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ATTENTION_STYLE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar attention style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1392` | `empathy_pattern_vendor_repair` | personhood | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMPATHY_PATTERN_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar empathy pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1393` | `inner_voice_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INNER_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar inner voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1394` | `written_voice_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRITTEN_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_1395` | `speech_register_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPEECH_REGISTER_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar speech register con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_1396` | `silence_style_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SILENCE_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar silence style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_1397` | `vocabulary_range_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOCABULARY_RANGE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vocabulary range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_1398` | `peruvian_latam_usage_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERUVIAN_LATAM_USAGE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peruvian latam usage con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1399` | `sociolect_limit_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOCIOLECT_LIMIT_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sociolect limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1400` | `interview_voice_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_INTERVIEW_VOICE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar interview voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1401` | `caption_voice_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAPTION_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar caption voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1402` | `script_voice_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCRIPT_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar script voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_1403` | `no_generic_text_rule_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_GENERIC_TEXT_RULE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no generic text rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LANGUAGE_1404` | `non_imitation_rule_vendor_repair` | language | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NON_IMITATION_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar non imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_IDENTITY_0001 — canonical_name
- Definición: Campo operativo para canonical name dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar canonical name como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar canonical name como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CANONICAL_NAME_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CANONICAL_NAME_DRIFT_OR_GAP
- Fallback: Reforzar canonical name con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0002 — model_code
- Definición: Campo operativo para model code dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar model code como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar model code como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MODEL_CODE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MODEL_CODE_DRIFT_OR_GAP
- Fallback: Reforzar model code con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0003 — aliases
- Definición: Campo operativo para aliases dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar aliases como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar aliases como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ALIASES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ALIASES_DRIFT_OR_GAP
- Fallback: Reforzar aliases con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0004 — adult_age
- Definición: Campo operativo para adult age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar adult age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ADULT_AGE_DRIFT_OR_GAP
- Fallback: Reforzar adult age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0005 — visual_age
- Definición: Campo operativo para visual age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar visual age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar visual age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VISUAL_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VISUAL_AGE_DRIFT_OR_GAP
- Fallback: Reforzar visual age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0006 — body_age
- Definición: Campo operativo para body age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar body age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BODY_AGE_DRIFT_OR_GAP
- Fallback: Reforzar body age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0007 — vocal_age
- Definición: Campo operativo para vocal age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar vocal age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_AGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOCAL_AGE_DRIFT_OR_GAP
- Fallback: Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0008 — project_role
- Definición: Campo operativo para project role dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar project role como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project role como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_ROLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROJECT_ROLE_DRIFT_OR_GAP
- Fallback: Reforzar project role con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0009 — canon_scope
- Definición: Campo operativo para canon scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar canon scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar canon scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CANON_SCOPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CANON_SCOPE_DRIFT_OR_GAP
- Fallback: Reforzar canon scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0010 — mutable_scope
- Definición: Campo operativo para mutable scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar mutable scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mutable scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUTABLE_SCOPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MUTABLE_SCOPE_DRIFT_OR_GAP
- Fallback: Reforzar mutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0011 — immutable_scope
- Definición: Campo operativo para immutable scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar immutable scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar immutable scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMMUTABLE_SCOPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_IMMUTABLE_SCOPE_DRIFT_OR_GAP
- Fallback: Reforzar immutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0012 — identity_status
- Definición: Campo operativo para identity status dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar identity status como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar identity status como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IDENTITY_STATUS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_IDENTITY_STATUS_DRIFT_OR_GAP
- Fallback: Reforzar identity status con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0013 — relationship_to_project
- Definición: Campo operativo para relationship to project dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar relationship to project como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar relationship to project como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RELATIONSHIP_TO_PROJECT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_RELATIONSHIP_TO_PROJECT_DRIFT_OR_GAP
- Fallback: Reforzar relationship to project con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0014 — persona_boundary
- Definición: Campo operativo para persona boundary dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar persona boundary como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar persona boundary como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERSONA_BOUNDARY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PERSONA_BOUNDARY_DRIFT_OR_GAP
- Fallback: Reforzar persona boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0015 — private_public_boundary
- Definición: Campo operativo para private public boundary dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar private public boundary como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar private public boundary como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRIVATE_PUBLIC_BOUNDARY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PRIVATE_PUBLIC_BOUNDARY_DRIFT_OR_GAP
- Fallback: Reforzar private public boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0016 — birth_context
- Definición: Campo operativo para birth context dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar birth context como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar birth context como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BIRTH_CONTEXT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BIRTH_CONTEXT_DRIFT_OR_GAP
- Fallback: Reforzar birth context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0017 — family_structure
- Definición: Campo operativo para family structure dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar family structure como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar family structure como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAMILY_STRUCTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FAMILY_STRUCTURE_DRIFT_OR_GAP
- Fallback: Reforzar family structure con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0018 — migration_trace
- Definición: Campo operativo para migration trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar migration trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar migration trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIGRATION_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MIGRATION_TRACE_DRIFT_OR_GAP
- Fallback: Reforzar migration trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0019 — education_trace
- Definición: Campo operativo para education trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar education trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar education trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EDUCATION_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EDUCATION_TRACE_DRIFT_OR_GAP
- Fallback: Reforzar education trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0020 — work_trace
- Definición: Campo operativo para work trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar work trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar work trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WORK_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WORK_TRACE_DRIFT_OR_GAP
- Fallback: Reforzar work trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0021 — social_environment
- Definición: Campo operativo para social environment dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar social environment como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar social environment como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIAL_ENVIRONMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SOCIAL_ENVIRONMENT_DRIFT_OR_GAP
- Fallback: Reforzar social environment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0022 — formative_events
- Definición: Campo operativo para formative events dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar formative events como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar formative events como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FORMATIVE_EVENTS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FORMATIVE_EVENTS_DRIFT_OR_GAP
- Fallback: Reforzar formative events con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0023 — life_turning_points
- Definición: Campo operativo para life turning points dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar life turning points como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar life turning points como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIFE_TURNING_POINTS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LIFE_TURNING_POINTS_DRIFT_OR_GAP
- Fallback: Reforzar life turning points con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0024 — habit_map
- Definición: Campo operativo para habit map dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar habit map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar habit map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HABIT_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HABIT_MAP_DRIFT_OR_GAP
- Fallback: Reforzar habit map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0025 — daily_routines
- Definición: Campo operativo para daily routines dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar daily routines como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar daily routines como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DAILY_ROUTINES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DAILY_ROUTINES_DRIFT_OR_GAP
- Fallback: Reforzar daily routines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0026 — memory_triggers
- Definición: Campo operativo para memory triggers dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar memory triggers como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar memory triggers como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MEMORY_TRIGGERS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MEMORY_TRIGGERS_DRIFT_OR_GAP
- Fallback: Reforzar memory triggers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0027 — emotional_anchors
- Definición: Campo operativo para emotional anchors dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar emotional anchors como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotional anchors como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTIONAL_ANCHORS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EMOTIONAL_ANCHORS_DRIFT_OR_GAP
- Fallback: Reforzar emotional anchors con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0028 — personal_limits
- Definición: Campo operativo para personal limits dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar personal limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar personal limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERSONAL_LIMITS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PERSONAL_LIMITS_DRIFT_OR_GAP
- Fallback: Reforzar personal limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0029 — conflict_history
- Definición: Campo operativo para conflict history dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar conflict history como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar conflict history como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFLICT_HISTORY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CONFLICT_HISTORY_DRIFT_OR_GAP
- Fallback: Reforzar conflict history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0030 — growth_arc
- Definición: Campo operativo para growth arc dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar growth arc como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar growth arc como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GROWTH_ARC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_GROWTH_ARC_DRIFT_OR_GAP
- Fallback: Reforzar growth arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0031 — temperament
- Definición: Campo operativo para temperament dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar temperament como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar temperament como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEMPERAMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TEMPERAMENT_DRIFT_OR_GAP
- Fallback: Reforzar temperament con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0032 — motivation_stack
- Definición: Campo operativo para motivation stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar motivation stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motivation stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTIVATION_STACK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MOTIVATION_STACK_DRIFT_OR_GAP
- Fallback: Reforzar motivation stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0033 — fear_stack
- Definición: Campo operativo para fear stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fear stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fear stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FEAR_STACK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FEAR_STACK_DRIFT_OR_GAP
- Fallback: Reforzar fear stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0034 — desire_stack
- Definición: Campo operativo para desire stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar desire stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar desire stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DESIRE_STACK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DESIRE_STACK_DRIFT_OR_GAP
- Fallback: Reforzar desire stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0035 — values_map
- Definición: Campo operativo para values map dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar values map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar values map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VALUES_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VALUES_MAP_DRIFT_OR_GAP
- Fallback: Reforzar values map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0036 — moral_boundaries
- Definición: Campo operativo para moral boundaries dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar moral boundaries como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar moral boundaries como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MORAL_BOUNDARIES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MORAL_BOUNDARIES_DRIFT_OR_GAP
- Fallback: Reforzar moral boundaries con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0037 — worldview
- Definición: Campo operativo para worldview dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar worldview como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar worldview como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WORLDVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WORLDVIEW_DRIFT_OR_GAP
- Fallback: Reforzar worldview con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0038 — contradictions
- Definición: Campo operativo para contradictions dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar contradictions como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contradictions como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTRADICTIONS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CONTRADICTIONS_DRIFT_OR_GAP
- Fallback: Reforzar contradictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0039 — humor_style
- Definición: Campo operativo para humor style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar humor style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar humor style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HUMOR_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HUMOR_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar humor style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0040 — decision_style
- Definición: Campo operativo para decision style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar decision style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar decision style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DECISION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DECISION_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar decision style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0041 — social_reaction
- Definición: Campo operativo para social reaction dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar social reaction como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar social reaction como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIAL_REACTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SOCIAL_REACTION_DRIFT_OR_GAP
- Fallback: Reforzar social reaction con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0042 — conflict_response
- Definición: Campo operativo para conflict response dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar conflict response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar conflict response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFLICT_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CONFLICT_RESPONSE_DRIFT_OR_GAP
- Fallback: Reforzar conflict response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0043 — confidence_pattern
- Definición: Campo operativo para confidence pattern dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar confidence pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar confidence pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFIDENCE_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CONFIDENCE_PATTERN_DRIFT_OR_GAP
- Fallback: Reforzar confidence pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0044 — attention_style
- Definición: Campo operativo para attention style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar attention style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar attention style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ATTENTION_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ATTENTION_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar attention style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0045 — empathy_pattern
- Definición: Campo operativo para empathy pattern dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar empathy pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar empathy pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMPATHY_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EMPATHY_PATTERN_DRIFT_OR_GAP
- Fallback: Reforzar empathy pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0046 — inner_voice
- Definición: Campo operativo para inner voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar inner voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar inner voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INNER_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_INNER_VOICE_DRIFT_OR_GAP
- Fallback: Reforzar inner voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0047 — written_voice
- Definición: Campo operativo para written voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar written voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar written voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRITTEN_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WRITTEN_VOICE_DRIFT_OR_GAP
- Fallback: Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0048 — speech_register
- Definición: Campo operativo para speech register dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar speech register como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar speech register como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPEECH_REGISTER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SPEECH_REGISTER_DRIFT_OR_GAP
- Fallback: Reforzar speech register con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0049 — silence_style
- Definición: Campo operativo para silence style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar silence style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar silence style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SILENCE_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SILENCE_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar silence style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0050 — vocabulary_range
- Definición: Campo operativo para vocabulary range dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar vocabulary range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocabulary range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCABULARY_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOCABULARY_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar vocabulary range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0051 — peruvian_latam_usage
- Definición: Campo operativo para peruvian latam usage dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar peruvian latam usage como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peruvian latam usage como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERUVIAN_LATAM_USAGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PERUVIAN_LATAM_USAGE_DRIFT_OR_GAP
- Fallback: Reforzar peruvian latam usage con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0052 — sociolect_limit
- Definición: Campo operativo para sociolect limit dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sociolect limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sociolect limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIOLECT_LIMIT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SOCIOLECT_LIMIT_DRIFT_OR_GAP
- Fallback: Reforzar sociolect limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0053 — interview_voice
- Definición: Campo operativo para interview voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar interview voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar interview voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INTERVIEW_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_INTERVIEW_VOICE_DRIFT_OR_GAP
- Fallback: Reforzar interview voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0054 — caption_voice
- Definición: Campo operativo para caption voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar caption voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar caption voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAPTION_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAPTION_VOICE_DRIFT_OR_GAP
- Fallback: Reforzar caption voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0055 — script_voice
- Definición: Campo operativo para script voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar script voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar script voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCRIPT_VOICE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCRIPT_VOICE_DRIFT_OR_GAP
- Fallback: Reforzar script voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0056 — no_generic_text_rule
- Definición: Campo operativo para no generic text rule dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar no generic text rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no generic text rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_GENERIC_TEXT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NO_GENERIC_TEXT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar no generic text rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0057 — non_imitation_rule
- Definición: Campo operativo para non imitation rule dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar non imitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar non imitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NON_IMITATION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NON_IMITATION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar non imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0450 — canonical_name_prompt_effect
- Definición: Campo operativo para canonical name dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar canonical name como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar canonical name como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CANONICAL_NAME_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CANONICAL_NAME_PROMPT_EFFECT
- Fallback: Reforzar canonical name con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0451 — model_code_prompt_effect
- Definición: Campo operativo para model code dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar model code como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar model code como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MODEL_CODE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MODEL_CODE_PROMPT_EFFECT
- Fallback: Reforzar model code con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0452 — aliases_prompt_effect
- Definición: Campo operativo para aliases dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar aliases como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar aliases como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ALIASES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ALIASES_PROMPT_EFFECT
- Fallback: Reforzar aliases con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0453 — adult_age_prompt_effect
- Definición: Campo operativo para adult age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_AGE_PROMPT_EFFECT
- Fallback: Reforzar adult age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0454 — visual_age_prompt_effect
- Definición: Campo operativo para visual age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar visual age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar visual age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VISUAL_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VISUAL_AGE_PROMPT_EFFECT
- Fallback: Reforzar visual age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0455 — body_age_prompt_effect
- Definición: Campo operativo para body age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_AGE_PROMPT_EFFECT
- Fallback: Reforzar body age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0456 — vocal_age_prompt_effect
- Definición: Campo operativo para vocal age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_AGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_AGE_PROMPT_EFFECT
- Fallback: Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0457 — project_role_prompt_effect
- Definición: Campo operativo para project role dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project role como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project role como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_ROLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_ROLE_PROMPT_EFFECT
- Fallback: Reforzar project role con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0458 — canon_scope_prompt_effect
- Definición: Campo operativo para canon scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar canon scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar canon scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CANON_SCOPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CANON_SCOPE_PROMPT_EFFECT
- Fallback: Reforzar canon scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0459 — mutable_scope_prompt_effect
- Definición: Campo operativo para mutable scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mutable scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mutable scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUTABLE_SCOPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUTABLE_SCOPE_PROMPT_EFFECT
- Fallback: Reforzar mutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0460 — immutable_scope_prompt_effect
- Definición: Campo operativo para immutable scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar immutable scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar immutable scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMMUTABLE_SCOPE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMMUTABLE_SCOPE_PROMPT_EFFECT
- Fallback: Reforzar immutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0461 — identity_status_prompt_effect
- Definición: Campo operativo para identity status dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar identity status como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar identity status como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IDENTITY_STATUS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IDENTITY_STATUS_PROMPT_EFFECT
- Fallback: Reforzar identity status con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0462 — relationship_to_project_prompt_effect
- Definición: Campo operativo para relationship to project dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar relationship to project como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar relationship to project como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RELATIONSHIP_TO_PROJECT_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RELATIONSHIP_TO_PROJECT_PROMPT_E
- Fallback: Reforzar relationship to project con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0463 — persona_boundary_prompt_effect
- Definición: Campo operativo para persona boundary dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar persona boundary como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar persona boundary como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERSONA_BOUNDARY_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERSONA_BOUNDARY_PROMPT_EFFECT
- Fallback: Reforzar persona boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0464 — private_public_boundary_prompt_effect
- Definición: Campo operativo para private public boundary dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar private public boundary como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar private public boundary como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRIVATE_PUBLIC_BOUNDARY_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRIVATE_PUBLIC_BOUNDARY_PROMPT_E
- Fallback: Reforzar private public boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0465 — birth_context_prompt_effect
- Definición: Campo operativo para birth context dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar birth context como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar birth context como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BIRTH_CONTEXT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BIRTH_CONTEXT_PROMPT_EFFECT
- Fallback: Reforzar birth context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0466 — family_structure_prompt_effect
- Definición: Campo operativo para family structure dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar family structure como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar family structure como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAMILY_STRUCTURE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAMILY_STRUCTURE_PROMPT_EFFECT
- Fallback: Reforzar family structure con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0467 — migration_trace_prompt_effect
- Definición: Campo operativo para migration trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar migration trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar migration trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIGRATION_TRACE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIGRATION_TRACE_PROMPT_EFFECT
- Fallback: Reforzar migration trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0468 — education_trace_prompt_effect
- Definición: Campo operativo para education trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar education trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar education trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EDUCATION_TRACE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EDUCATION_TRACE_PROMPT_EFFECT
- Fallback: Reforzar education trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0469 — work_trace_prompt_effect
- Definición: Campo operativo para work trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar work trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar work trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WORK_TRACE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WORK_TRACE_PROMPT_EFFECT
- Fallback: Reforzar work trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0470 — social_environment_prompt_effect
- Definición: Campo operativo para social environment dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar social environment como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar social environment como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIAL_ENVIRONMENT_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIAL_ENVIRONMENT_PROMPT_EFFECT
- Fallback: Reforzar social environment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0471 — formative_events_prompt_effect
- Definición: Campo operativo para formative events dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar formative events como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar formative events como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FORMATIVE_EVENTS_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FORMATIVE_EVENTS_PROMPT_EFFECT
- Fallback: Reforzar formative events con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0472 — life_turning_points_prompt_effect
- Definición: Campo operativo para life turning points dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar life turning points como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar life turning points como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIFE_TURNING_POINTS_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIFE_TURNING_POINTS_PROMPT_EFFEC
- Fallback: Reforzar life turning points con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0473 — habit_map_prompt_effect
- Definición: Campo operativo para habit map dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar habit map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar habit map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HABIT_MAP_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HABIT_MAP_PROMPT_EFFECT
- Fallback: Reforzar habit map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0474 — daily_routines_prompt_effect
- Definición: Campo operativo para daily routines dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar daily routines como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar daily routines como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DAILY_ROUTINES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DAILY_ROUTINES_PROMPT_EFFECT
- Fallback: Reforzar daily routines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0475 — memory_triggers_prompt_effect
- Definición: Campo operativo para memory triggers dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar memory triggers como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar memory triggers como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MEMORY_TRIGGERS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MEMORY_TRIGGERS_PROMPT_EFFECT
- Fallback: Reforzar memory triggers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0476 — emotional_anchors_prompt_effect
- Definición: Campo operativo para emotional anchors dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotional anchors como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotional anchors como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTIONAL_ANCHORS_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTIONAL_ANCHORS_PROMPT_EFFECT
- Fallback: Reforzar emotional anchors con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0477 — personal_limits_prompt_effect
- Definición: Campo operativo para personal limits dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar personal limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar personal limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERSONAL_LIMITS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERSONAL_LIMITS_PROMPT_EFFECT
- Fallback: Reforzar personal limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0478 — conflict_history_prompt_effect
- Definición: Campo operativo para conflict history dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar conflict history como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar conflict history como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFLICT_HISTORY_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFLICT_HISTORY_PROMPT_EFFECT
- Fallback: Reforzar conflict history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0479 — growth_arc_prompt_effect
- Definición: Campo operativo para growth arc dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar growth arc como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar growth arc como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GROWTH_ARC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GROWTH_ARC_PROMPT_EFFECT
- Fallback: Reforzar growth arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0480 — temperament_prompt_effect
- Definición: Campo operativo para temperament dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar temperament como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar temperament como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEMPERAMENT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEMPERAMENT_PROMPT_EFFECT
- Fallback: Reforzar temperament con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0481 — motivation_stack_prompt_effect
- Definición: Campo operativo para motivation stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motivation stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motivation stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTIVATION_STACK_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTIVATION_STACK_PROMPT_EFFECT
- Fallback: Reforzar motivation stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0482 — fear_stack_prompt_effect
- Definición: Campo operativo para fear stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fear stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fear stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FEAR_STACK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FEAR_STACK_PROMPT_EFFECT
- Fallback: Reforzar fear stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0483 — desire_stack_prompt_effect
- Definición: Campo operativo para desire stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar desire stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar desire stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DESIRE_STACK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DESIRE_STACK_PROMPT_EFFECT
- Fallback: Reforzar desire stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0484 — values_map_prompt_effect
- Definición: Campo operativo para values map dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar values map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar values map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VALUES_MAP_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VALUES_MAP_PROMPT_EFFECT
- Fallback: Reforzar values map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0485 — moral_boundaries_prompt_effect
- Definición: Campo operativo para moral boundaries dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar moral boundaries como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar moral boundaries como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MORAL_BOUNDARIES_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MORAL_BOUNDARIES_PROMPT_EFFECT
- Fallback: Reforzar moral boundaries con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0486 — worldview_prompt_effect
- Definición: Campo operativo para worldview dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar worldview como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar worldview como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WORLDVIEW_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WORLDVIEW_PROMPT_EFFECT
- Fallback: Reforzar worldview con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0487 — contradictions_prompt_effect
- Definición: Campo operativo para contradictions dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contradictions como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contradictions como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTRADICTIONS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTRADICTIONS_PROMPT_EFFECT
- Fallback: Reforzar contradictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0488 — humor_style_prompt_effect
- Definición: Campo operativo para humor style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar humor style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar humor style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HUMOR_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HUMOR_STYLE_PROMPT_EFFECT
- Fallback: Reforzar humor style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0489 — decision_style_prompt_effect
- Definición: Campo operativo para decision style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar decision style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar decision style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DECISION_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DECISION_STYLE_PROMPT_EFFECT
- Fallback: Reforzar decision style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0490 — social_reaction_prompt_effect
- Definición: Campo operativo para social reaction dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar social reaction como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar social reaction como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIAL_REACTION_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIAL_REACTION_PROMPT_EFFECT
- Fallback: Reforzar social reaction con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0491 — conflict_response_prompt_effect
- Definición: Campo operativo para conflict response dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar conflict response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar conflict response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFLICT_RESPONSE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFLICT_RESPONSE_PROMPT_EFFECT
- Fallback: Reforzar conflict response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0492 — confidence_pattern_prompt_effect
- Definición: Campo operativo para confidence pattern dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar confidence pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar confidence pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFIDENCE_PATTERN_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFIDENCE_PATTERN_PROMPT_EFFECT
- Fallback: Reforzar confidence pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0493 — attention_style_prompt_effect
- Definición: Campo operativo para attention style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar attention style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar attention style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ATTENTION_STYLE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ATTENTION_STYLE_PROMPT_EFFECT
- Fallback: Reforzar attention style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0494 — empathy_pattern_prompt_effect
- Definición: Campo operativo para empathy pattern dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar empathy pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar empathy pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMPATHY_PATTERN_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMPATHY_PATTERN_PROMPT_EFFECT
- Fallback: Reforzar empathy pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0495 — inner_voice_prompt_effect
- Definición: Campo operativo para inner voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar inner voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar inner voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INNER_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INNER_VOICE_PROMPT_EFFECT
- Fallback: Reforzar inner voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0496 — written_voice_prompt_effect
- Definición: Campo operativo para written voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar written voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar written voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRITTEN_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRITTEN_VOICE_PROMPT_EFFECT
- Fallback: Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0497 — speech_register_prompt_effect
- Definición: Campo operativo para speech register dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar speech register como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar speech register como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPEECH_REGISTER_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPEECH_REGISTER_PROMPT_EFFECT
- Fallback: Reforzar speech register con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0498 — silence_style_prompt_effect
- Definición: Campo operativo para silence style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar silence style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar silence style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SILENCE_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SILENCE_STYLE_PROMPT_EFFECT
- Fallback: Reforzar silence style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0499 — vocabulary_range_prompt_effect
- Definición: Campo operativo para vocabulary range dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocabulary range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocabulary range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCABULARY_RANGE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCABULARY_RANGE_PROMPT_EFFECT
- Fallback: Reforzar vocabulary range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0500 — peruvian_latam_usage_prompt_effect
- Definición: Campo operativo para peruvian latam usage dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peruvian latam usage como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peruvian latam usage como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERUVIAN_LATAM_USAGE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERUVIAN_LATAM_USAGE_PROMPT_EFFE
- Fallback: Reforzar peruvian latam usage con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0501 — sociolect_limit_prompt_effect
- Definición: Campo operativo para sociolect limit dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sociolect limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sociolect limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIOLECT_LIMIT_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIOLECT_LIMIT_PROMPT_EFFECT
- Fallback: Reforzar sociolect limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0502 — interview_voice_prompt_effect
- Definición: Campo operativo para interview voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar interview voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar interview voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INTERVIEW_VOICE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INTERVIEW_VOICE_PROMPT_EFFECT
- Fallback: Reforzar interview voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0503 — caption_voice_prompt_effect
- Definición: Campo operativo para caption voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar caption voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar caption voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAPTION_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAPTION_VOICE_PROMPT_EFFECT
- Fallback: Reforzar caption voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0504 — script_voice_prompt_effect
- Definición: Campo operativo para script voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar script voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar script voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCRIPT_VOICE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCRIPT_VOICE_PROMPT_EFFECT
- Fallback: Reforzar script voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0505 — no_generic_text_rule_prompt_effect
- Definición: Campo operativo para no generic text rule dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no generic text rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no generic text rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_GENERIC_TEXT_RULE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_GENERIC_TEXT_RULE_PROMPT_EFFE
- Fallback: Reforzar no generic text rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0506 — non_imitation_rule_prompt_effect
- Definición: Campo operativo para non imitation rule dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar non imitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar non imitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NON_IMITATION_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NON_IMITATION_RULE_PROMPT_EFFECT
- Fallback: Reforzar non imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0899 — canonical_name_qa_matrix
- Definición: Campo operativo para canonical name dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar canonical name como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar canonical name como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CANONICAL_NAME_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CANONICAL_NAME_QA_MATRIX
- Fallback: Reforzar canonical name con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0900 — model_code_qa_matrix
- Definición: Campo operativo para model code dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar model code como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar model code como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MODEL_CODE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MODEL_CODE_QA_MATRIX
- Fallback: Reforzar model code con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0901 — aliases_qa_matrix
- Definición: Campo operativo para aliases dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar aliases como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar aliases como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ALIASES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ALIASES_QA_MATRIX
- Fallback: Reforzar aliases con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0902 — adult_age_qa_matrix
- Definición: Campo operativo para adult age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_AGE_QA_MATRIX
- Fallback: Reforzar adult age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0903 — visual_age_qa_matrix
- Definición: Campo operativo para visual age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar visual age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar visual age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VISUAL_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VISUAL_AGE_QA_MATRIX
- Fallback: Reforzar visual age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0904 — body_age_qa_matrix
- Definición: Campo operativo para body age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_AGE_QA_MATRIX
- Fallback: Reforzar body age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0905 — vocal_age_qa_matrix
- Definición: Campo operativo para vocal age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_AGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_AGE_QA_MATRIX
- Fallback: Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0906 — project_role_qa_matrix
- Definición: Campo operativo para project role dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project role como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project role como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_ROLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_ROLE_QA_MATRIX
- Fallback: Reforzar project role con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0907 — canon_scope_qa_matrix
- Definición: Campo operativo para canon scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar canon scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar canon scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CANON_SCOPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CANON_SCOPE_QA_MATRIX
- Fallback: Reforzar canon scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0908 — mutable_scope_qa_matrix
- Definición: Campo operativo para mutable scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mutable scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mutable scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUTABLE_SCOPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUTABLE_SCOPE_QA_MATRIX
- Fallback: Reforzar mutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0909 — immutable_scope_qa_matrix
- Definición: Campo operativo para immutable scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar immutable scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar immutable scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMMUTABLE_SCOPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMMUTABLE_SCOPE_QA_MATRIX
- Fallback: Reforzar immutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0910 — identity_status_qa_matrix
- Definición: Campo operativo para identity status dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar identity status como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar identity status como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IDENTITY_STATUS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IDENTITY_STATUS_QA_MATRIX
- Fallback: Reforzar identity status con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0911 — relationship_to_project_qa_matrix
- Definición: Campo operativo para relationship to project dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar relationship to project como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar relationship to project como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RELATIONSHIP_TO_PROJECT_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RELATIONSHIP_TO_PROJECT_QA_MATRI
- Fallback: Reforzar relationship to project con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_0912 — persona_boundary_qa_matrix
- Definición: Campo operativo para persona boundary dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar persona boundary como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar persona boundary como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERSONA_BOUNDARY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERSONA_BOUNDARY_QA_MATRIX
- Fallback: Reforzar persona boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0913 — private_public_boundary_qa_matrix
- Definición: Campo operativo para private public boundary dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar private public boundary como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar private public boundary como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRIVATE_PUBLIC_BOUNDARY_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRIVATE_PUBLIC_BOUNDARY_QA_MATRI
- Fallback: Reforzar private public boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0914 — birth_context_qa_matrix
- Definición: Campo operativo para birth context dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar birth context como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar birth context como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BIRTH_CONTEXT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BIRTH_CONTEXT_QA_MATRIX
- Fallback: Reforzar birth context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0915 — family_structure_qa_matrix
- Definición: Campo operativo para family structure dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar family structure como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar family structure como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAMILY_STRUCTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAMILY_STRUCTURE_QA_MATRIX
- Fallback: Reforzar family structure con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0916 — migration_trace_qa_matrix
- Definición: Campo operativo para migration trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar migration trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar migration trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIGRATION_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIGRATION_TRACE_QA_MATRIX
- Fallback: Reforzar migration trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0917 — education_trace_qa_matrix
- Definición: Campo operativo para education trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar education trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar education trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EDUCATION_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EDUCATION_TRACE_QA_MATRIX
- Fallback: Reforzar education trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0918 — work_trace_qa_matrix
- Definición: Campo operativo para work trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar work trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar work trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WORK_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WORK_TRACE_QA_MATRIX
- Fallback: Reforzar work trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0919 — social_environment_qa_matrix
- Definición: Campo operativo para social environment dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar social environment como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar social environment como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIAL_ENVIRONMENT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIAL_ENVIRONMENT_QA_MATRIX
- Fallback: Reforzar social environment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0920 — formative_events_qa_matrix
- Definición: Campo operativo para formative events dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar formative events como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar formative events como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FORMATIVE_EVENTS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FORMATIVE_EVENTS_QA_MATRIX
- Fallback: Reforzar formative events con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0921 — life_turning_points_qa_matrix
- Definición: Campo operativo para life turning points dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar life turning points como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar life turning points como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIFE_TURNING_POINTS_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIFE_TURNING_POINTS_QA_MATRIX
- Fallback: Reforzar life turning points con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0922 — habit_map_qa_matrix
- Definición: Campo operativo para habit map dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar habit map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar habit map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HABIT_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HABIT_MAP_QA_MATRIX
- Fallback: Reforzar habit map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0923 — daily_routines_qa_matrix
- Definición: Campo operativo para daily routines dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar daily routines como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar daily routines como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DAILY_ROUTINES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DAILY_ROUTINES_QA_MATRIX
- Fallback: Reforzar daily routines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0924 — memory_triggers_qa_matrix
- Definición: Campo operativo para memory triggers dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar memory triggers como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar memory triggers como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MEMORY_TRIGGERS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MEMORY_TRIGGERS_QA_MATRIX
- Fallback: Reforzar memory triggers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0925 — emotional_anchors_qa_matrix
- Definición: Campo operativo para emotional anchors dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotional anchors como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotional anchors como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTIONAL_ANCHORS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTIONAL_ANCHORS_QA_MATRIX
- Fallback: Reforzar emotional anchors con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0926 — personal_limits_qa_matrix
- Definición: Campo operativo para personal limits dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar personal limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar personal limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERSONAL_LIMITS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERSONAL_LIMITS_QA_MATRIX
- Fallback: Reforzar personal limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0927 — conflict_history_qa_matrix
- Definición: Campo operativo para conflict history dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar conflict history como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar conflict history como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFLICT_HISTORY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFLICT_HISTORY_QA_MATRIX
- Fallback: Reforzar conflict history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0928 — growth_arc_qa_matrix
- Definición: Campo operativo para growth arc dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar growth arc como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar growth arc como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GROWTH_ARC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GROWTH_ARC_QA_MATRIX
- Fallback: Reforzar growth arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0929 — temperament_qa_matrix
- Definición: Campo operativo para temperament dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar temperament como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar temperament como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEMPERAMENT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEMPERAMENT_QA_MATRIX
- Fallback: Reforzar temperament con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0930 — motivation_stack_qa_matrix
- Definición: Campo operativo para motivation stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motivation stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motivation stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTIVATION_STACK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTIVATION_STACK_QA_MATRIX
- Fallback: Reforzar motivation stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0931 — fear_stack_qa_matrix
- Definición: Campo operativo para fear stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fear stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fear stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FEAR_STACK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FEAR_STACK_QA_MATRIX
- Fallback: Reforzar fear stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0932 — desire_stack_qa_matrix
- Definición: Campo operativo para desire stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar desire stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar desire stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DESIRE_STACK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DESIRE_STACK_QA_MATRIX
- Fallback: Reforzar desire stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0933 — values_map_qa_matrix
- Definición: Campo operativo para values map dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar values map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar values map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VALUES_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VALUES_MAP_QA_MATRIX
- Fallback: Reforzar values map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0934 — moral_boundaries_qa_matrix
- Definición: Campo operativo para moral boundaries dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar moral boundaries como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar moral boundaries como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MORAL_BOUNDARIES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MORAL_BOUNDARIES_QA_MATRIX
- Fallback: Reforzar moral boundaries con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0935 — worldview_qa_matrix
- Definición: Campo operativo para worldview dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar worldview como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar worldview como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WORLDVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WORLDVIEW_QA_MATRIX
- Fallback: Reforzar worldview con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0936 — contradictions_qa_matrix
- Definición: Campo operativo para contradictions dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contradictions como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contradictions como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTRADICTIONS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTRADICTIONS_QA_MATRIX
- Fallback: Reforzar contradictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0937 — humor_style_qa_matrix
- Definición: Campo operativo para humor style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar humor style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar humor style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HUMOR_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HUMOR_STYLE_QA_MATRIX
- Fallback: Reforzar humor style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0938 — decision_style_qa_matrix
- Definición: Campo operativo para decision style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar decision style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar decision style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DECISION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DECISION_STYLE_QA_MATRIX
- Fallback: Reforzar decision style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0939 — social_reaction_qa_matrix
- Definición: Campo operativo para social reaction dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar social reaction como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar social reaction como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIAL_REACTION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIAL_REACTION_QA_MATRIX
- Fallback: Reforzar social reaction con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0940 — conflict_response_qa_matrix
- Definición: Campo operativo para conflict response dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar conflict response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar conflict response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFLICT_RESPONSE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFLICT_RESPONSE_QA_MATRIX
- Fallback: Reforzar conflict response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0941 — confidence_pattern_qa_matrix
- Definición: Campo operativo para confidence pattern dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar confidence pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar confidence pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFIDENCE_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFIDENCE_PATTERN_QA_MATRIX
- Fallback: Reforzar confidence pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0942 — attention_style_qa_matrix
- Definición: Campo operativo para attention style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar attention style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar attention style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ATTENTION_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ATTENTION_STYLE_QA_MATRIX
- Fallback: Reforzar attention style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0943 — empathy_pattern_qa_matrix
- Definición: Campo operativo para empathy pattern dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar empathy pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar empathy pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMPATHY_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMPATHY_PATTERN_QA_MATRIX
- Fallback: Reforzar empathy pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0944 — inner_voice_qa_matrix
- Definición: Campo operativo para inner voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar inner voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar inner voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INNER_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INNER_VOICE_QA_MATRIX
- Fallback: Reforzar inner voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0945 — written_voice_qa_matrix
- Definición: Campo operativo para written voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar written voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar written voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRITTEN_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRITTEN_VOICE_QA_MATRIX
- Fallback: Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0946 — speech_register_qa_matrix
- Definición: Campo operativo para speech register dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar speech register como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar speech register como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPEECH_REGISTER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPEECH_REGISTER_QA_MATRIX
- Fallback: Reforzar speech register con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0947 — silence_style_qa_matrix
- Definición: Campo operativo para silence style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar silence style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar silence style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SILENCE_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SILENCE_STYLE_QA_MATRIX
- Fallback: Reforzar silence style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0948 — vocabulary_range_qa_matrix
- Definición: Campo operativo para vocabulary range dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocabulary range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocabulary range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCABULARY_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCABULARY_RANGE_QA_MATRIX
- Fallback: Reforzar vocabulary range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0949 — peruvian_latam_usage_qa_matrix
- Definición: Campo operativo para peruvian latam usage dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peruvian latam usage como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peruvian latam usage como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERUVIAN_LATAM_USAGE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERUVIAN_LATAM_USAGE_QA_MATRIX
- Fallback: Reforzar peruvian latam usage con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0950 — sociolect_limit_qa_matrix
- Definición: Campo operativo para sociolect limit dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sociolect limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sociolect limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIOLECT_LIMIT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIOLECT_LIMIT_QA_MATRIX
- Fallback: Reforzar sociolect limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0951 — interview_voice_qa_matrix
- Definición: Campo operativo para interview voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar interview voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar interview voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INTERVIEW_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INTERVIEW_VOICE_QA_MATRIX
- Fallback: Reforzar interview voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0952 — caption_voice_qa_matrix
- Definición: Campo operativo para caption voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar caption voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar caption voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAPTION_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAPTION_VOICE_QA_MATRIX
- Fallback: Reforzar caption voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0953 — script_voice_qa_matrix
- Definición: Campo operativo para script voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar script voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar script voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCRIPT_VOICE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCRIPT_VOICE_QA_MATRIX
- Fallback: Reforzar script voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0954 — no_generic_text_rule_qa_matrix
- Definición: Campo operativo para no generic text rule dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no generic text rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no generic text rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_GENERIC_TEXT_RULE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_GENERIC_TEXT_RULE_QA_MATRIX
- Fallback: Reforzar no generic text rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_0955 — non_imitation_rule_qa_matrix
- Definición: Campo operativo para non imitation rule dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar non imitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar non imitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NON_IMITATION_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NON_IMITATION_RULE_QA_MATRIX
- Fallback: Reforzar non imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_1348 — canonical_name_vendor_repair
- Definición: Campo operativo para canonical name dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar canonical name como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar canonical name como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CANONICAL_NAME_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CANONICAL_NAME_VENDOR_REPAIR
- Fallback: Reforzar canonical name con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_1349 — model_code_vendor_repair
- Definición: Campo operativo para model code dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar model code como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar model code como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MODEL_CODE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MODEL_CODE_VENDOR_REPAIR
- Fallback: Reforzar model code con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_1350 — aliases_vendor_repair
- Definición: Campo operativo para aliases dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar aliases como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar aliases como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ALIASES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ALIASES_VENDOR_REPAIR
- Fallback: Reforzar aliases con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1351 — adult_age_vendor_repair
- Definición: Campo operativo para adult age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_AGE_VENDOR_REPAIR
- Fallback: Reforzar adult age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1352 — visual_age_vendor_repair
- Definición: Campo operativo para visual age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar visual age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar visual age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VISUAL_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VISUAL_AGE_VENDOR_REPAIR
- Fallback: Reforzar visual age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1353 — body_age_vendor_repair
- Definición: Campo operativo para body age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_AGE_VENDOR_REPAIR
- Fallback: Reforzar body age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1354 — vocal_age_vendor_repair
- Definición: Campo operativo para vocal age dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocal age como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocal age como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCAL_AGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCAL_AGE_VENDOR_REPAIR
- Fallback: Reforzar vocal age con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1355 — project_role_vendor_repair
- Definición: Campo operativo para project role dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project role como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project role como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_ROLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_ROLE_VENDOR_REPAIR
- Fallback: Reforzar project role con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1356 — canon_scope_vendor_repair
- Definición: Campo operativo para canon scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar canon scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar canon scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CANON_SCOPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CANON_SCOPE_VENDOR_REPAIR
- Fallback: Reforzar canon scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_1357 — mutable_scope_vendor_repair
- Definición: Campo operativo para mutable scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mutable scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mutable scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MUTABLE_SCOPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MUTABLE_SCOPE_VENDOR_REPAIR
- Fallback: Reforzar mutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_1358 — immutable_scope_vendor_repair
- Definición: Campo operativo para immutable scope dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar immutable scope como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar immutable scope como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMMUTABLE_SCOPE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMMUTABLE_SCOPE_VENDOR_REPAIR
- Fallback: Reforzar immutable scope con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_1359 — identity_status_vendor_repair
- Definición: Campo operativo para identity status dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar identity status como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar identity status como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IDENTITY_STATUS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IDENTITY_STATUS_VENDOR_REPAIR
- Fallback: Reforzar identity status con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1360 — relationship_to_project_vendor_repair
- Definición: Campo operativo para relationship to project dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar relationship to project como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar relationship to project como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RELATIONSHIP_TO_PROJECT_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RELATIONSHIP_TO_PROJECT_VENDOR_R
- Fallback: Reforzar relationship to project con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_IDENTITY_1361 — persona_boundary_vendor_repair
- Definición: Campo operativo para persona boundary dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar persona boundary como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar persona boundary como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERSONA_BOUNDARY_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERSONA_BOUNDARY_VENDOR_REPAIR
- Fallback: Reforzar persona boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1362 — private_public_boundary_vendor_repair
- Definición: Campo operativo para private public boundary dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar private public boundary como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar private public boundary como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRIVATE_PUBLIC_BOUNDARY_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRIVATE_PUBLIC_BOUNDARY_VENDOR_R
- Fallback: Reforzar private public boundary con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1363 — birth_context_vendor_repair
- Definición: Campo operativo para birth context dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar birth context como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar birth context como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BIRTH_CONTEXT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BIRTH_CONTEXT_VENDOR_REPAIR
- Fallback: Reforzar birth context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1364 — family_structure_vendor_repair
- Definición: Campo operativo para family structure dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar family structure como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar family structure como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAMILY_STRUCTURE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAMILY_STRUCTURE_VENDOR_REPAIR
- Fallback: Reforzar family structure con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_1365 — migration_trace_vendor_repair
- Definición: Campo operativo para migration trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar migration trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar migration trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIGRATION_TRACE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIGRATION_TRACE_VENDOR_REPAIR
- Fallback: Reforzar migration trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1366 — education_trace_vendor_repair
- Definición: Campo operativo para education trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar education trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar education trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EDUCATION_TRACE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EDUCATION_TRACE_VENDOR_REPAIR
- Fallback: Reforzar education trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1367 — work_trace_vendor_repair
- Definición: Campo operativo para work trace dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar work trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar work trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WORK_TRACE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WORK_TRACE_VENDOR_REPAIR
- Fallback: Reforzar work trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1368 — social_environment_vendor_repair
- Definición: Campo operativo para social environment dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar social environment como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar social environment como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIAL_ENVIRONMENT_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIAL_ENVIRONMENT_VENDOR_REPAIR
- Fallback: Reforzar social environment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1369 — formative_events_vendor_repair
- Definición: Campo operativo para formative events dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar formative events como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar formative events como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FORMATIVE_EVENTS_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FORMATIVE_EVENTS_VENDOR_REPAIR
- Fallback: Reforzar formative events con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1370 — life_turning_points_vendor_repair
- Definición: Campo operativo para life turning points dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar life turning points como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar life turning points como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIFE_TURNING_POINTS_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIFE_TURNING_POINTS_VENDOR_REPAI
- Fallback: Reforzar life turning points con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1371 — habit_map_vendor_repair
- Definición: Campo operativo para habit map dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar habit map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar habit map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HABIT_MAP_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HABIT_MAP_VENDOR_REPAIR
- Fallback: Reforzar habit map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1372 — daily_routines_vendor_repair
- Definición: Campo operativo para daily routines dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar daily routines como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar daily routines como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DAILY_ROUTINES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DAILY_ROUTINES_VENDOR_REPAIR
- Fallback: Reforzar daily routines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1373 — memory_triggers_vendor_repair
- Definición: Campo operativo para memory triggers dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar memory triggers como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar memory triggers como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MEMORY_TRIGGERS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MEMORY_TRIGGERS_VENDOR_REPAIR
- Fallback: Reforzar memory triggers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1374 — emotional_anchors_vendor_repair
- Definición: Campo operativo para emotional anchors dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotional anchors como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotional anchors como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTIONAL_ANCHORS_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTIONAL_ANCHORS_VENDOR_REPAIR
- Fallback: Reforzar emotional anchors con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1375 — personal_limits_vendor_repair
- Definición: Campo operativo para personal limits dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar personal limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar personal limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERSONAL_LIMITS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERSONAL_LIMITS_VENDOR_REPAIR
- Fallback: Reforzar personal limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1376 — conflict_history_vendor_repair
- Definición: Campo operativo para conflict history dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar conflict history como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar conflict history como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFLICT_HISTORY_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFLICT_HISTORY_VENDOR_REPAIR
- Fallback: Reforzar conflict history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1377 — growth_arc_vendor_repair
- Definición: Campo operativo para growth arc dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar growth arc como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar growth arc como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GROWTH_ARC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GROWTH_ARC_VENDOR_REPAIR
- Fallback: Reforzar growth arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1378 — temperament_vendor_repair
- Definición: Campo operativo para temperament dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar temperament como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar temperament como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEMPERAMENT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEMPERAMENT_VENDOR_REPAIR
- Fallback: Reforzar temperament con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1379 — motivation_stack_vendor_repair
- Definición: Campo operativo para motivation stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motivation stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motivation stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTIVATION_STACK_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTIVATION_STACK_VENDOR_REPAIR
- Fallback: Reforzar motivation stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1380 — fear_stack_vendor_repair
- Definición: Campo operativo para fear stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fear stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fear stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FEAR_STACK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FEAR_STACK_VENDOR_REPAIR
- Fallback: Reforzar fear stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1381 — desire_stack_vendor_repair
- Definición: Campo operativo para desire stack dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar desire stack como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar desire stack como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DESIRE_STACK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DESIRE_STACK_VENDOR_REPAIR
- Fallback: Reforzar desire stack con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_1382 — values_map_vendor_repair
- Definición: Campo operativo para values map dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar values map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar values map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VALUES_MAP_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VALUES_MAP_VENDOR_REPAIR
- Fallback: Reforzar values map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1383 — moral_boundaries_vendor_repair
- Definición: Campo operativo para moral boundaries dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar moral boundaries como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar moral boundaries como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MORAL_BOUNDARIES_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MORAL_BOUNDARIES_VENDOR_REPAIR
- Fallback: Reforzar moral boundaries con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_1384 — worldview_vendor_repair
- Definición: Campo operativo para worldview dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar worldview como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar worldview como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WORLDVIEW_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WORLDVIEW_VENDOR_REPAIR
- Fallback: Reforzar worldview con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1385 — contradictions_vendor_repair
- Definición: Campo operativo para contradictions dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contradictions como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contradictions como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTRADICTIONS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTRADICTIONS_VENDOR_REPAIR
- Fallback: Reforzar contradictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1386 — humor_style_vendor_repair
- Definición: Campo operativo para humor style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar humor style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar humor style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HUMOR_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HUMOR_STYLE_VENDOR_REPAIR
- Fallback: Reforzar humor style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1387 — decision_style_vendor_repair
- Definición: Campo operativo para decision style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar decision style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar decision style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DECISION_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DECISION_STYLE_VENDOR_REPAIR
- Fallback: Reforzar decision style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1388 — social_reaction_vendor_repair
- Definición: Campo operativo para social reaction dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar social reaction como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar social reaction como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIAL_REACTION_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIAL_REACTION_VENDOR_REPAIR
- Fallback: Reforzar social reaction con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1389 — conflict_response_vendor_repair
- Definición: Campo operativo para conflict response dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar conflict response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar conflict response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFLICT_RESPONSE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFLICT_RESPONSE_VENDOR_REPAIR
- Fallback: Reforzar conflict response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1390 — confidence_pattern_vendor_repair
- Definición: Campo operativo para confidence pattern dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar confidence pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar confidence pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONFIDENCE_PATTERN_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONFIDENCE_PATTERN_VENDOR_REPAIR
- Fallback: Reforzar confidence pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1391 — attention_style_vendor_repair
- Definición: Campo operativo para attention style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar attention style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar attention style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ATTENTION_STYLE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ATTENTION_STYLE_VENDOR_REPAIR
- Fallback: Reforzar attention style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1392 — empathy_pattern_vendor_repair
- Definición: Campo operativo para empathy pattern dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar empathy pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar empathy pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMPATHY_PATTERN_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMPATHY_PATTERN_VENDOR_REPAIR
- Fallback: Reforzar empathy pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1393 — inner_voice_vendor_repair
- Definición: Campo operativo para inner voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar inner voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar inner voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INNER_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INNER_VOICE_VENDOR_REPAIR
- Fallback: Reforzar inner voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1394 — written_voice_vendor_repair
- Definición: Campo operativo para written voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar written voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar written voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRITTEN_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRITTEN_VOICE_VENDOR_REPAIR
- Fallback: Reforzar written voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_1395 — speech_register_vendor_repair
- Definición: Campo operativo para speech register dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar speech register como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar speech register como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPEECH_REGISTER_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPEECH_REGISTER_VENDOR_REPAIR
- Fallback: Reforzar speech register con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_1396 — silence_style_vendor_repair
- Definición: Campo operativo para silence style dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar silence style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar silence style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SILENCE_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SILENCE_STYLE_VENDOR_REPAIR
- Fallback: Reforzar silence style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_1397 — vocabulary_range_vendor_repair
- Definición: Campo operativo para vocabulary range dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vocabulary range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vocabulary range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOCABULARY_RANGE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOCABULARY_RANGE_VENDOR_REPAIR
- Fallback: Reforzar vocabulary range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_1398 — peruvian_latam_usage_vendor_repair
- Definición: Campo operativo para peruvian latam usage dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peruvian latam usage como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peruvian latam usage como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERUVIAN_LATAM_USAGE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERUVIAN_LATAM_USAGE_VENDOR_REPA
- Fallback: Reforzar peruvian latam usage con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1399 — sociolect_limit_vendor_repair
- Definición: Campo operativo para sociolect limit dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sociolect limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sociolect limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOCIOLECT_LIMIT_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOCIOLECT_LIMIT_VENDOR_REPAIR
- Fallback: Reforzar sociolect limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1400 — interview_voice_vendor_repair
- Definición: Campo operativo para interview voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar interview voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar interview voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_INTERVIEW_VOICE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_INTERVIEW_VOICE_VENDOR_REPAIR
- Fallback: Reforzar interview voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1401 — caption_voice_vendor_repair
- Definición: Campo operativo para caption voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar caption voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar caption voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAPTION_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAPTION_VOICE_VENDOR_REPAIR
- Fallback: Reforzar caption voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1402 — script_voice_vendor_repair
- Definición: Campo operativo para script voice dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar script voice como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar script voice como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCRIPT_VOICE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCRIPT_VOICE_VENDOR_REPAIR
- Fallback: Reforzar script voice con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_1403 — no_generic_text_rule_vendor_repair
- Definición: Campo operativo para no generic text rule dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no generic text rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no generic text rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_GENERIC_TEXT_RULE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_GENERIC_TEXT_RULE_VENDOR_REPA
- Fallback: Reforzar no generic text rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LANGUAGE_1404 — non_imitation_rule_vendor_repair
- Definición: Campo operativo para non imitation rule dentro de Identidad, memoria, biografía, cultura segura y persona digital adulta. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar non imitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar non imitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NON_IMITATION_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NON_IMITATION_RULE_VENDOR_REPAIR
- Fallback: Reforzar non imitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
