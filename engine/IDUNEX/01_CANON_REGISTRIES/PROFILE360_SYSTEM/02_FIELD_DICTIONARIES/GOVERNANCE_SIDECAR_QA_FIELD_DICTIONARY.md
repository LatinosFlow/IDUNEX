## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_SIDECAR_0399` | `status_internal` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STATUS_INTERNAL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar status internal con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0400` | `policy_set` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POLICY_SET_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar policy set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0401` | `compatible_with` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMPATIBLE_WITH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar compatible with con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0402` | `source_trace` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar source trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0403` | `source_classification` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_CLASSIFICATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar source classification con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0404` | `sha_lock` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHA_LOCK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sha lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0405` | `lineage_lock` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LINEAGE_LOCK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lineage lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0406` | `version_semver` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VERSION_SEMVER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar version semver con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0407` | `migration_state` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIGRATION_STATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar migration state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0408` | `no_loss_evidence` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_LOSS_EVIDENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar no loss evidence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0409` | `audit_cycle` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AUDIT_CYCLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar audit cycle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0410` | `final_only_gate` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINAL_ONLY_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar final only gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0411` | `readback_gate` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_READBACK_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar readback gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0412` | `rebuild_gate` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REBUILD_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar rebuild gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0413` | `acceptance_gate` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCEPTANCE_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar acceptance gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0414` | `sidecar_schema` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SIDECAR_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sidecar schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0415` | `watermark_state` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WATERMARK_STATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar watermark state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0416` | `clean_master_rule` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLEAN_MASTER_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar clean master rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0417` | `c2pa_conceptual_note` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_C2PA_CONCEPTUAL_NOTE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar c2pa conceptual note con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0418` | `prompt_hash` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROMPT_HASH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar prompt hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0419` | `output_hash` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OUTPUT_HASH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar output hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0420` | `vendor_parameters` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VENDOR_PARAMETERS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar vendor parameters con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0421` | `model_profile_hash` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MODEL_PROFILE_HASH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar model profile hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0422` | `project_hash` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_HASH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar project hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0423` | `qa_snapshot` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_QA_SNAPSHOT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar qa snapshot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0424` | `fallback_history` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FALLBACK_HISTORY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fallback history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0425` | `regression_test_link` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REGRESSION_TEST_LINK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar regression test link con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0426` | `sidecar_required_fields` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SIDECAR_REQUIRED_FIELDS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sidecar required fields con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0427` | `privacy_review` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRIVACY_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar privacy review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0428` | `ley_29733_review` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LEY_29733_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar ley 29733 review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0429` | `license_review` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LICENSE_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar license review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0430` | `likeness_review` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIKENESS_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar likeness review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0431` | `brand_logo_review` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar brand logo review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0432` | `adult_editorial_review` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_EDITORIAL_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar adult editorial review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0433` | `data_minimization_rule` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DATA_MINIMIZATION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar data minimization rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0434` | `consent_trace` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONSENT_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar consent trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0435` | `commercial_use_flag` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMMERCIAL_USE_FLAG_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar commercial use flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0436` | `vendor_terms_flag` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VENDOR_TERMS_FLAG_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar vendor terms flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0437` | `peru_context_rule` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERU_CONTEXT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar peru context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0438` | `fail_code_schema` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAIL_CODE_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fail code schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0439` | `fallback_schema` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FALLBACK_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fallback schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0440` | `golden_test_schema` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GOLDEN_TEST_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar golden test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0441` | `regression_test_schema` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REGRESSION_TEST_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar regression test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0442` | `padding_linter` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PADDING_LINTER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar padding linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0443` | `naming_linter` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NAMING_LINTER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar naming linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0444` | `source_runtime_gate` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_RUNTIME_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar source runtime gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0445` | `profile_fullness_gate` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROFILE_FULLNESS_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar profile fullness gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_EXPORT_0446` | `copilot_render_gate` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COPILOT_RENDER_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar copilot render gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0447` | `chatgpt_load_gate` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHATGPT_LOAD_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar chatgpt load gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0448` | `project_factory_gate` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_FACTORY_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar project factory gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0449` | `generic_visual_system_gate` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_VISUAL_SYSTEM_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar generic_visual_system_reference gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0848` | `status_internal_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STATUS_INTERNAL_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar status internal con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0849` | `policy_set_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POLICY_SET_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar policy set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0850` | `compatible_with_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMPATIBLE_WITH_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar compatible with con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0851` | `source_trace_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_TRACE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0852` | `source_classification_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_CLASSIFICATION_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source classification con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0853` | `sha_lock_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHA_LOCK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sha lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0854` | `lineage_lock_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LINEAGE_LOCK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lineage lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0855` | `version_semver_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VERSION_SEMVER_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar version semver con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0856` | `migration_state_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIGRATION_STATE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar migration state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0857` | `no_loss_evidence_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_LOSS_EVIDENCE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no loss evidence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0858` | `audit_cycle_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AUDIT_CYCLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar audit cycle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0859` | `final_only_gate_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINAL_ONLY_GATE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar final only gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0860` | `readback_gate_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_READBACK_GATE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar readback gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0861` | `rebuild_gate_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REBUILD_GATE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rebuild gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0862` | `acceptance_gate_prompt_effect` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCEPTANCE_GATE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar acceptance gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0863` | `sidecar_schema_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SIDECAR_SCHEMA_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sidecar schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0864` | `watermark_state_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WATERMARK_STATE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar watermark state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0865` | `clean_master_rule_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLEAN_MASTER_RULE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clean master rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0866` | `c2pa_conceptual_note_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_C2PA_CONCEPTUAL_NOTE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar c2pa conceptual note con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0867` | `prompt_hash_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROMPT_HASH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prompt hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0868` | `output_hash_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OUTPUT_HASH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar output hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0869` | `vendor_parameters_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VENDOR_PARAMETERS_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vendor parameters con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0870` | `model_profile_hash_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MODEL_PROFILE_HASH_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar model profile hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0871` | `project_hash_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_HASH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0872` | `qa_snapshot_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_QA_SNAPSHOT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar qa snapshot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0873` | `fallback_history_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FALLBACK_HISTORY_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fallback history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0874` | `regression_test_link_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REGRESSION_TEST_LINK_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar regression test link con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0875` | `sidecar_required_fields_prompt_effect` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SIDECAR_REQUIRED_FIELDS_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sidecar required fields con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0876` | `privacy_review_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRIVACY_REVIEW_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar privacy review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0877` | `ley_29733_review_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LEY_29733_REVIEW_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ley 29733 review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0878` | `license_review_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LICENSE_REVIEW_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar license review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0879` | `likeness_review_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIKENESS_REVIEW_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar likeness review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0880` | `brand_logo_review_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_REVIEW_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0881` | `adult_editorial_review_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_EDITORIAL_REVIEW_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult editorial review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0882` | `data_minimization_rule_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DATA_MINIMIZATION_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar data minimization rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0883` | `consent_trace_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONSENT_TRACE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar consent trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0884` | `commercial_use_flag_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMMERCIAL_USE_FLAG_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar commercial use flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0885` | `vendor_terms_flag_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VENDOR_TERMS_FLAG_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vendor terms flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0886` | `peru_context_rule_prompt_effect` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERU_CONTEXT_RULE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peru context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0887` | `fail_code_schema_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAIL_CODE_SCHEMA_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fail code schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0888` | `fallback_schema_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FALLBACK_SCHEMA_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fallback schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0889` | `golden_test_schema_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GOLDEN_TEST_SCHEMA_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar golden test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0890` | `regression_test_schema_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REGRESSION_TEST_SCHEMA_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar regression test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0891` | `padding_linter_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PADDING_LINTER_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar padding linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0892` | `naming_linter_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NAMING_LINTER_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar naming linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0893` | `source_runtime_gate_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_RUNTIME_GATE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source runtime gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0894` | `profile_fullness_gate_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROFILE_FULLNESS_GATE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar profile fullness gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_EXPORT_0895` | `copilot_render_gate_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COPILOT_RENDER_GATE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar copilot render gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0896` | `chatgpt_load_gate_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHATGPT_LOAD_GATE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chatgpt load gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0897` | `project_factory_gate_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_FACTORY_GATE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project factory gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_0898` | `generic_visual_system_gate_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_VISUAL_SYSTEM_GATE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic_visual_system_reference gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1297` | `status_internal_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STATUS_INTERNAL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar status internal con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1298` | `policy_set_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POLICY_SET_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar policy set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1299` | `compatible_with_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMPATIBLE_WITH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar compatible with con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1300` | `source_trace_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1301` | `source_classification_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_CLASSIFICATION_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source classification con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1302` | `sha_lock_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHA_LOCK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sha lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1303` | `lineage_lock_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LINEAGE_LOCK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lineage lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1304` | `version_semver_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VERSION_SEMVER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar version semver con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1305` | `migration_state_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIGRATION_STATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar migration state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1306` | `no_loss_evidence_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_LOSS_EVIDENCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no loss evidence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1307` | `audit_cycle_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AUDIT_CYCLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar audit cycle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1308` | `final_only_gate_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINAL_ONLY_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar final only gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1309` | `readback_gate_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_READBACK_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar readback gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1310` | `rebuild_gate_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REBUILD_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rebuild gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1311` | `acceptance_gate_qa_matrix` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCEPTANCE_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar acceptance gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1312` | `sidecar_schema_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SIDECAR_SCHEMA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sidecar schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1313` | `watermark_state_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WATERMARK_STATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar watermark state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1314` | `clean_master_rule_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLEAN_MASTER_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clean master rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1315` | `c2pa_conceptual_note_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_C2PA_CONCEPTUAL_NOTE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar c2pa conceptual note con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1316` | `prompt_hash_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROMPT_HASH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prompt hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1317` | `output_hash_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OUTPUT_HASH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar output hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1318` | `vendor_parameters_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VENDOR_PARAMETERS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vendor parameters con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1319` | `model_profile_hash_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MODEL_PROFILE_HASH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar model profile hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1320` | `project_hash_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_HASH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1321` | `qa_snapshot_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_QA_SNAPSHOT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar qa snapshot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1322` | `fallback_history_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FALLBACK_HISTORY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fallback history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1323` | `regression_test_link_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REGRESSION_TEST_LINK_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar regression test link con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1324` | `sidecar_required_fields_qa_matrix` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SIDECAR_REQUIRED_FIELDS_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sidecar required fields con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1325` | `privacy_review_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRIVACY_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar privacy review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1326` | `ley_29733_review_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LEY_29733_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ley 29733 review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1327` | `license_review_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LICENSE_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar license review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1328` | `likeness_review_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIKENESS_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar likeness review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1329` | `brand_logo_review_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1330` | `adult_editorial_review_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_EDITORIAL_REVIEW_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult editorial review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1331` | `data_minimization_rule_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DATA_MINIMIZATION_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar data minimization rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1332` | `consent_trace_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONSENT_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar consent trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1333` | `commercial_use_flag_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMMERCIAL_USE_FLAG_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar commercial use flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1334` | `vendor_terms_flag_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VENDOR_TERMS_FLAG_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vendor terms flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1335` | `peru_context_rule_qa_matrix` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERU_CONTEXT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peru context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1336` | `fail_code_schema_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAIL_CODE_SCHEMA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fail code schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1337` | `fallback_schema_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FALLBACK_SCHEMA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fallback schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1338` | `golden_test_schema_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GOLDEN_TEST_SCHEMA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar golden test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1339` | `regression_test_schema_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REGRESSION_TEST_SCHEMA_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar regression test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1340` | `padding_linter_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PADDING_LINTER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar padding linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1341` | `naming_linter_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NAMING_LINTER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar naming linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1342` | `source_runtime_gate_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_RUNTIME_GATE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source runtime gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1343` | `profile_fullness_gate_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROFILE_FULLNESS_GATE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar profile fullness gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_EXPORT_1344` | `copilot_render_gate_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COPILOT_RENDER_GATE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar copilot render gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1345` | `chatgpt_load_gate_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHATGPT_LOAD_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chatgpt load gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1346` | `project_factory_gate_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_FACTORY_GATE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project factory gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1347` | `generic_visual_system_gate_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_VISUAL_SYSTEM_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic_visual_system_reference gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1746` | `status_internal_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STATUS_INTERNAL_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar status internal con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1747` | `policy_set_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POLICY_SET_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar policy set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1748` | `compatible_with_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMPATIBLE_WITH_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar compatible with con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1749` | `source_trace_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_TRACE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1750` | `source_classification_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_CLASSIFICATION_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source classification con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1751` | `sha_lock_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHA_LOCK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sha lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1752` | `lineage_lock_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LINEAGE_LOCK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lineage lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1753` | `version_semver_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VERSION_SEMVER_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar version semver con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1754` | `migration_state_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIGRATION_STATE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar migration state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1755` | `no_loss_evidence_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_LOSS_EVIDENCE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no loss evidence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1756` | `audit_cycle_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AUDIT_CYCLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar audit cycle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1757` | `final_only_gate_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINAL_ONLY_GATE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar final only gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1758` | `readback_gate_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_READBACK_GATE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar readback gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1759` | `rebuild_gate_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REBUILD_GATE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rebuild gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1760` | `acceptance_gate_vendor_repair` | governance | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCEPTANCE_GATE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar acceptance gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1761` | `sidecar_schema_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SIDECAR_SCHEMA_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sidecar schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1762` | `watermark_state_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WATERMARK_STATE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar watermark state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1763` | `clean_master_rule_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLEAN_MASTER_RULE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clean master rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1764` | `c2pa_conceptual_note_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_C2PA_CONCEPTUAL_NOTE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar c2pa conceptual note con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1765` | `prompt_hash_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROMPT_HASH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prompt hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1766` | `output_hash_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OUTPUT_HASH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar output hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1767` | `vendor_parameters_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VENDOR_PARAMETERS_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vendor parameters con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1768` | `model_profile_hash_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MODEL_PROFILE_HASH_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar model profile hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1769` | `project_hash_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_HASH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1770` | `qa_snapshot_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_QA_SNAPSHOT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar qa snapshot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1771` | `fallback_history_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FALLBACK_HISTORY_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fallback history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1772` | `regression_test_link_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REGRESSION_TEST_LINK_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar regression test link con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1773` | `sidecar_required_fields_vendor_repair` | sidecar | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SIDECAR_REQUIRED_FIELDS_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sidecar required fields con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1774` | `privacy_review_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRIVACY_REVIEW_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar privacy review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1775` | `ley_29733_review_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LEY_29733_REVIEW_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ley 29733 review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1776` | `license_review_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LICENSE_REVIEW_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar license review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1777` | `likeness_review_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIKENESS_REVIEW_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar likeness review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1778` | `brand_logo_review_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_REVIEW_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1779` | `adult_editorial_review_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_EDITORIAL_REVIEW_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult editorial review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1780` | `data_minimization_rule_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DATA_MINIMIZATION_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar data minimization rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1781` | `consent_trace_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONSENT_TRACE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar consent trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1782` | `commercial_use_flag_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMMERCIAL_USE_FLAG_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar commercial use flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1783` | `vendor_terms_flag_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VENDOR_TERMS_FLAG_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vendor terms flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1784` | `peru_context_rule_vendor_repair` | legal | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERU_CONTEXT_RULE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar peru context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1785` | `fail_code_schema_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAIL_CODE_SCHEMA_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fail code schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1786` | `fallback_schema_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FALLBACK_SCHEMA_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fallback schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1787` | `golden_test_schema_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GOLDEN_TEST_SCHEMA_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar golden test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1788` | `regression_test_schema_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REGRESSION_TEST_SCHEMA_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar regression test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1789` | `padding_linter_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PADDING_LINTER_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar padding linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1790` | `naming_linter_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NAMING_LINTER_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar naming linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1791` | `source_runtime_gate_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOURCE_RUNTIME_GATE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar source runtime gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1792` | `profile_fullness_gate_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROFILE_FULLNESS_GATE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar profile fullness gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_EXPORT_1793` | `copilot_render_gate_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COPILOT_RENDER_GATE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar copilot render gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1794` | `chatgpt_load_gate_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHATGPT_LOAD_GATE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chatgpt load gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1795` | `project_factory_gate_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROJECT_FACTORY_GATE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar project factory gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SIDECAR_1796` | `generic_visual_system_gate_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_VISUAL_SYSTEM_GATE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic_visual_system_reference gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_SIDECAR_0399 — status_internal
- Definición: Campo operativo para status internal dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar status internal como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar status internal como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STATUS_INTERNAL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_STATUS_INTERNAL_DRIFT_OR_GAP
- Fallback: Reforzar status internal con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0400 — policy_set
- Definición: Campo operativo para policy set dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar policy set como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar policy set como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POLICY_SET_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_POLICY_SET_DRIFT_OR_GAP
- Fallback: Reforzar policy set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0401 — compatible_with
- Definición: Campo operativo para compatible with dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar compatible with como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar compatible with como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMPATIBLE_WITH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_COMPATIBLE_WITH_DRIFT_OR_GAP
- Fallback: Reforzar compatible with con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0402 — source_trace
- Definición: Campo operativo para source trace dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar source trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SOURCE_TRACE_DRIFT_OR_GAP
- Fallback: Reforzar source trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0403 — source_classification
- Definición: Campo operativo para source classification dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar source classification como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source classification como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_CLASSIFICATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SOURCE_CLASSIFICATION_DRIFT_OR_GAP
- Fallback: Reforzar source classification con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0404 — sha_lock
- Definición: Campo operativo para sha lock dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sha lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sha lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHA_LOCK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHA_LOCK_DRIFT_OR_GAP
- Fallback: Reforzar sha lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0405 — lineage_lock
- Definición: Campo operativo para lineage lock dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lineage lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lineage lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LINEAGE_LOCK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LINEAGE_LOCK_DRIFT_OR_GAP
- Fallback: Reforzar lineage lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0406 — version_semver
- Definición: Campo operativo para version semver dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar version semver como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar version semver como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VERSION_SEMVER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VERSION_SEMVER_DRIFT_OR_GAP
- Fallback: Reforzar version semver con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0407 — migration_state
- Definición: Campo operativo para migration state dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar migration state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar migration state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIGRATION_STATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MIGRATION_STATE_DRIFT_OR_GAP
- Fallback: Reforzar migration state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0408 — no_loss_evidence
- Definición: Campo operativo para no loss evidence dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar no loss evidence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no loss evidence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_LOSS_EVIDENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NO_LOSS_EVIDENCE_DRIFT_OR_GAP
- Fallback: Reforzar no loss evidence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0409 — audit_cycle
- Definición: Campo operativo para audit cycle dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar audit cycle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar audit cycle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AUDIT_CYCLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_AUDIT_CYCLE_DRIFT_OR_GAP
- Fallback: Reforzar audit cycle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0410 — final_only_gate
- Definición: Campo operativo para final only gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar final only gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar final only gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINAL_ONLY_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FINAL_ONLY_GATE_DRIFT_OR_GAP
- Fallback: Reforzar final only gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0411 — readback_gate
- Definición: Campo operativo para readback gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar readback gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar readback gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_READBACK_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_READBACK_GATE_DRIFT_OR_GAP
- Fallback: Reforzar readback gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0412 — rebuild_gate
- Definición: Campo operativo para rebuild gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar rebuild gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rebuild gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REBUILD_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_REBUILD_GATE_DRIFT_OR_GAP
- Fallback: Reforzar rebuild gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0413 — acceptance_gate
- Definición: Campo operativo para acceptance gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar acceptance gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar acceptance gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCEPTANCE_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ACCEPTANCE_GATE_DRIFT_OR_GAP
- Fallback: Reforzar acceptance gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0414 — sidecar_schema
- Definición: Campo operativo para sidecar schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sidecar schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sidecar schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SIDECAR_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SIDECAR_SCHEMA_DRIFT_OR_GAP
- Fallback: Reforzar sidecar schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0415 — watermark_state
- Definición: Campo operativo para watermark state dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar watermark state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar watermark state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WATERMARK_STATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WATERMARK_STATE_DRIFT_OR_GAP
- Fallback: Reforzar watermark state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0416 — clean_master_rule
- Definición: Campo operativo para clean master rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar clean master rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clean master rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLEAN_MASTER_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CLEAN_MASTER_RULE_DRIFT_OR_GAP
- Fallback: Reforzar clean master rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0417 — c2pa_conceptual_note
- Definición: Campo operativo para c2pa conceptual note dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar c2pa conceptual note como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar c2pa conceptual note como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_C2PA_CONCEPTUAL_NOTE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_C2PA_CONCEPTUAL_NOTE_DRIFT_OR_GAP
- Fallback: Reforzar c2pa conceptual note con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0418 — prompt_hash
- Definición: Campo operativo para prompt hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar prompt hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prompt hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROMPT_HASH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROMPT_HASH_DRIFT_OR_GAP
- Fallback: Reforzar prompt hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0419 — output_hash
- Definición: Campo operativo para output hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar output hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar output hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OUTPUT_HASH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_OUTPUT_HASH_DRIFT_OR_GAP
- Fallback: Reforzar output hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0420 — vendor_parameters
- Definición: Campo operativo para vendor parameters dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar vendor parameters como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vendor parameters como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VENDOR_PARAMETERS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VENDOR_PARAMETERS_DRIFT_OR_GAP
- Fallback: Reforzar vendor parameters con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0421 — model_profile_hash
- Definición: Campo operativo para model profile hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar model profile hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar model profile hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MODEL_PROFILE_HASH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MODEL_PROFILE_HASH_DRIFT_OR_GAP
- Fallback: Reforzar model profile hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0422 — project_hash
- Definición: Campo operativo para project hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar project hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_HASH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROJECT_HASH_DRIFT_OR_GAP
- Fallback: Reforzar project hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0423 — qa_snapshot
- Definición: Campo operativo para qa snapshot dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar qa snapshot como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar qa snapshot como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_QA_SNAPSHOT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_QA_SNAPSHOT_DRIFT_OR_GAP
- Fallback: Reforzar qa snapshot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0424 — fallback_history
- Definición: Campo operativo para fallback history dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fallback history como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fallback history como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FALLBACK_HISTORY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FALLBACK_HISTORY_DRIFT_OR_GAP
- Fallback: Reforzar fallback history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0425 — regression_test_link
- Definición: Campo operativo para regression test link dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar regression test link como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar regression test link como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REGRESSION_TEST_LINK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_REGRESSION_TEST_LINK_DRIFT_OR_GAP
- Fallback: Reforzar regression test link con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0426 — sidecar_required_fields
- Definición: Campo operativo para sidecar required fields dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sidecar required fields como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sidecar required fields como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SIDECAR_REQUIRED_FIELDS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SIDECAR_REQUIRED_FIELDS_DRIFT_OR_GAP
- Fallback: Reforzar sidecar required fields con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0427 — privacy_review
- Definición: Campo operativo para privacy review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar privacy review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar privacy review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRIVACY_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PRIVACY_REVIEW_DRIFT_OR_GAP
- Fallback: Reforzar privacy review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0428 — ley_29733_review
- Definición: Campo operativo para ley 29733 review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar ley 29733 review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ley 29733 review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LEY_29733_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LEY_29733_REVIEW_DRIFT_OR_GAP
- Fallback: Reforzar ley 29733 review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0429 — license_review
- Definición: Campo operativo para license review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar license review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar license review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LICENSE_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LICENSE_REVIEW_DRIFT_OR_GAP
- Fallback: Reforzar license review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0430 — likeness_review
- Definición: Campo operativo para likeness review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar likeness review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar likeness review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIKENESS_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LIKENESS_REVIEW_DRIFT_OR_GAP
- Fallback: Reforzar likeness review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0431 — brand_logo_review
- Definición: Campo operativo para brand logo review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar brand logo review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BRAND_LOGO_REVIEW_DRIFT_OR_GAP
- Fallback: Reforzar brand logo review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0432 — adult_editorial_review
- Definición: Campo operativo para adult editorial review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar adult editorial review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult editorial review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_EDITORIAL_REVIEW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ADULT_EDITORIAL_REVIEW_DRIFT_OR_GAP
- Fallback: Reforzar adult editorial review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0433 — data_minimization_rule
- Definición: Campo operativo para data minimization rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar data minimization rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar data minimization rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DATA_MINIMIZATION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DATA_MINIMIZATION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar data minimization rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0434 — consent_trace
- Definición: Campo operativo para consent trace dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar consent trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar consent trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONSENT_TRACE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CONSENT_TRACE_DRIFT_OR_GAP
- Fallback: Reforzar consent trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0435 — commercial_use_flag
- Definición: Campo operativo para commercial use flag dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar commercial use flag como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar commercial use flag como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMMERCIAL_USE_FLAG_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_COMMERCIAL_USE_FLAG_DRIFT_OR_GAP
- Fallback: Reforzar commercial use flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0436 — vendor_terms_flag
- Definición: Campo operativo para vendor terms flag dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar vendor terms flag como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vendor terms flag como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VENDOR_TERMS_FLAG_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VENDOR_TERMS_FLAG_DRIFT_OR_GAP
- Fallback: Reforzar vendor terms flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0437 — peru_context_rule
- Definición: Campo operativo para peru context rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar peru context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peru context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERU_CONTEXT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PERU_CONTEXT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar peru context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0438 — fail_code_schema
- Definición: Campo operativo para fail code schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fail code schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fail code schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAIL_CODE_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FAIL_CODE_SCHEMA_DRIFT_OR_GAP
- Fallback: Reforzar fail code schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0439 — fallback_schema
- Definición: Campo operativo para fallback schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fallback schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fallback schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FALLBACK_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FALLBACK_SCHEMA_DRIFT_OR_GAP
- Fallback: Reforzar fallback schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0440 — golden_test_schema
- Definición: Campo operativo para golden test schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar golden test schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar golden test schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GOLDEN_TEST_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_GOLDEN_TEST_SCHEMA_DRIFT_OR_GAP
- Fallback: Reforzar golden test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0441 — regression_test_schema
- Definición: Campo operativo para regression test schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar regression test schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar regression test schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REGRESSION_TEST_SCHEMA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_REGRESSION_TEST_SCHEMA_DRIFT_OR_GAP
- Fallback: Reforzar regression test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0442 — padding_linter
- Definición: Campo operativo para padding linter dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar padding linter como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar padding linter como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PADDING_LINTER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PADDING_LINTER_DRIFT_OR_GAP
- Fallback: Reforzar padding linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0443 — naming_linter
- Definición: Campo operativo para naming linter dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar naming linter como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar naming linter como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NAMING_LINTER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NAMING_LINTER_DRIFT_OR_GAP
- Fallback: Reforzar naming linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0444 — source_runtime_gate
- Definición: Campo operativo para source runtime gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar source runtime gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source runtime gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_RUNTIME_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SOURCE_RUNTIME_GATE_DRIFT_OR_GAP
- Fallback: Reforzar source runtime gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0445 — profile_fullness_gate
- Definición: Campo operativo para profile fullness gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar profile fullness gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar profile fullness gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROFILE_FULLNESS_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROFILE_FULLNESS_GATE_DRIFT_OR_GAP
- Fallback: Reforzar profile fullness gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_EXPORT_0446 — copilot_render_gate
- Definición: Campo operativo para copilot render gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar copilot render gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar copilot render gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COPILOT_RENDER_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_COPILOT_RENDER_GATE_DRIFT_OR_GAP
- Fallback: Reforzar copilot render gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0447 — chatgpt_load_gate
- Definición: Campo operativo para chatgpt load gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar chatgpt load gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chatgpt load gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHATGPT_LOAD_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CHATGPT_LOAD_GATE_DRIFT_OR_GAP
- Fallback: Reforzar chatgpt load gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0448 — project_factory_gate
- Definición: Campo operativo para project factory gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar project factory gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project factory gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_FACTORY_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROJECT_FACTORY_GATE_DRIFT_OR_GAP
- Fallback: Reforzar project factory gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0449 — generic_visual_system_gate
- Definición: Campo operativo para generic_visual_system_reference gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar generic_visual_system_reference gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic_visual_system_reference gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_VISUAL_SYSTEM_GATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_GENERIC_VISUAL_SYSTEM_GATE_DRIFT_OR_GAP
- Fallback: Reforzar generic_visual_system_reference gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0848 — status_internal_prompt_effect
- Definición: Campo operativo para status internal dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar status internal como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar status internal como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STATUS_INTERNAL_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STATUS_INTERNAL_PROMPT_EFFECT
- Fallback: Reforzar status internal con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0849 — policy_set_prompt_effect
- Definición: Campo operativo para policy set dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar policy set como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar policy set como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POLICY_SET_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POLICY_SET_PROMPT_EFFECT
- Fallback: Reforzar policy set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0850 — compatible_with_prompt_effect
- Definición: Campo operativo para compatible with dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar compatible with como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar compatible with como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMPATIBLE_WITH_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMPATIBLE_WITH_PROMPT_EFFECT
- Fallback: Reforzar compatible with con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0851 — source_trace_prompt_effect
- Definición: Campo operativo para source trace dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_TRACE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_TRACE_PROMPT_EFFECT
- Fallback: Reforzar source trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0852 — source_classification_prompt_effect
- Definición: Campo operativo para source classification dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source classification como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source classification como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_CLASSIFICATION_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_CLASSIFICATION_PROMPT_EFF
- Fallback: Reforzar source classification con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0853 — sha_lock_prompt_effect
- Definición: Campo operativo para sha lock dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sha lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sha lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHA_LOCK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHA_LOCK_PROMPT_EFFECT
- Fallback: Reforzar sha lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0854 — lineage_lock_prompt_effect
- Definición: Campo operativo para lineage lock dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lineage lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lineage lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LINEAGE_LOCK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LINEAGE_LOCK_PROMPT_EFFECT
- Fallback: Reforzar lineage lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0855 — version_semver_prompt_effect
- Definición: Campo operativo para version semver dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar version semver como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar version semver como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VERSION_SEMVER_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VERSION_SEMVER_PROMPT_EFFECT
- Fallback: Reforzar version semver con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0856 — migration_state_prompt_effect
- Definición: Campo operativo para migration state dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar migration state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar migration state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIGRATION_STATE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIGRATION_STATE_PROMPT_EFFECT
- Fallback: Reforzar migration state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0857 — no_loss_evidence_prompt_effect
- Definición: Campo operativo para no loss evidence dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no loss evidence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no loss evidence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_LOSS_EVIDENCE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_LOSS_EVIDENCE_PROMPT_EFFECT
- Fallback: Reforzar no loss evidence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0858 — audit_cycle_prompt_effect
- Definición: Campo operativo para audit cycle dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar audit cycle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar audit cycle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AUDIT_CYCLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AUDIT_CYCLE_PROMPT_EFFECT
- Fallback: Reforzar audit cycle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0859 — final_only_gate_prompt_effect
- Definición: Campo operativo para final only gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar final only gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar final only gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINAL_ONLY_GATE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINAL_ONLY_GATE_PROMPT_EFFECT
- Fallback: Reforzar final only gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0860 — readback_gate_prompt_effect
- Definición: Campo operativo para readback gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar readback gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar readback gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_READBACK_GATE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_READBACK_GATE_PROMPT_EFFECT
- Fallback: Reforzar readback gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0861 — rebuild_gate_prompt_effect
- Definición: Campo operativo para rebuild gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rebuild gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rebuild gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REBUILD_GATE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REBUILD_GATE_PROMPT_EFFECT
- Fallback: Reforzar rebuild gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0862 — acceptance_gate_prompt_effect
- Definición: Campo operativo para acceptance gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar acceptance gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar acceptance gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCEPTANCE_GATE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCEPTANCE_GATE_PROMPT_EFFECT
- Fallback: Reforzar acceptance gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0863 — sidecar_schema_prompt_effect
- Definición: Campo operativo para sidecar schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sidecar schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sidecar schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SIDECAR_SCHEMA_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SIDECAR_SCHEMA_PROMPT_EFFECT
- Fallback: Reforzar sidecar schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0864 — watermark_state_prompt_effect
- Definición: Campo operativo para watermark state dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar watermark state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar watermark state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WATERMARK_STATE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WATERMARK_STATE_PROMPT_EFFECT
- Fallback: Reforzar watermark state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0865 — clean_master_rule_prompt_effect
- Definición: Campo operativo para clean master rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clean master rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clean master rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLEAN_MASTER_RULE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLEAN_MASTER_RULE_PROMPT_EFFECT
- Fallback: Reforzar clean master rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0866 — c2pa_conceptual_note_prompt_effect
- Definición: Campo operativo para c2pa conceptual note dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar c2pa conceptual note como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar c2pa conceptual note como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_C2PA_CONCEPTUAL_NOTE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_C2PA_CONCEPTUAL_NOTE_PROMPT_EFFE
- Fallback: Reforzar c2pa conceptual note con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0867 — prompt_hash_prompt_effect
- Definición: Campo operativo para prompt hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prompt hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prompt hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROMPT_HASH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROMPT_HASH_PROMPT_EFFECT
- Fallback: Reforzar prompt hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0868 — output_hash_prompt_effect
- Definición: Campo operativo para output hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar output hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar output hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OUTPUT_HASH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OUTPUT_HASH_PROMPT_EFFECT
- Fallback: Reforzar output hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0869 — vendor_parameters_prompt_effect
- Definición: Campo operativo para vendor parameters dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vendor parameters como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vendor parameters como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VENDOR_PARAMETERS_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VENDOR_PARAMETERS_PROMPT_EFFECT
- Fallback: Reforzar vendor parameters con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0870 — model_profile_hash_prompt_effect
- Definición: Campo operativo para model profile hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar model profile hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar model profile hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MODEL_PROFILE_HASH_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MODEL_PROFILE_HASH_PROMPT_EFFECT
- Fallback: Reforzar model profile hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0871 — project_hash_prompt_effect
- Definición: Campo operativo para project hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_HASH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_HASH_PROMPT_EFFECT
- Fallback: Reforzar project hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0872 — qa_snapshot_prompt_effect
- Definición: Campo operativo para qa snapshot dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar qa snapshot como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar qa snapshot como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_QA_SNAPSHOT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_QA_SNAPSHOT_PROMPT_EFFECT
- Fallback: Reforzar qa snapshot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0873 — fallback_history_prompt_effect
- Definición: Campo operativo para fallback history dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fallback history como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fallback history como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FALLBACK_HISTORY_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FALLBACK_HISTORY_PROMPT_EFFECT
- Fallback: Reforzar fallback history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0874 — regression_test_link_prompt_effect
- Definición: Campo operativo para regression test link dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar regression test link como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar regression test link como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REGRESSION_TEST_LINK_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REGRESSION_TEST_LINK_PROMPT_EFFE
- Fallback: Reforzar regression test link con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0875 — sidecar_required_fields_prompt_effect
- Definición: Campo operativo para sidecar required fields dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sidecar required fields como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sidecar required fields como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SIDECAR_REQUIRED_FIELDS_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SIDECAR_REQUIRED_FIELDS_PROMPT_E
- Fallback: Reforzar sidecar required fields con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0876 — privacy_review_prompt_effect
- Definición: Campo operativo para privacy review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar privacy review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar privacy review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRIVACY_REVIEW_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRIVACY_REVIEW_PROMPT_EFFECT
- Fallback: Reforzar privacy review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0877 — ley_29733_review_prompt_effect
- Definición: Campo operativo para ley 29733 review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ley 29733 review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ley 29733 review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LEY_29733_REVIEW_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LEY_29733_REVIEW_PROMPT_EFFECT
- Fallback: Reforzar ley 29733 review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0878 — license_review_prompt_effect
- Definición: Campo operativo para license review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar license review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar license review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LICENSE_REVIEW_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LICENSE_REVIEW_PROMPT_EFFECT
- Fallback: Reforzar license review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0879 — likeness_review_prompt_effect
- Definición: Campo operativo para likeness review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar likeness review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar likeness review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIKENESS_REVIEW_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIKENESS_REVIEW_PROMPT_EFFECT
- Fallback: Reforzar likeness review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0880 — brand_logo_review_prompt_effect
- Definición: Campo operativo para brand logo review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_REVIEW_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_REVIEW_PROMPT_EFFECT
- Fallback: Reforzar brand logo review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0881 — adult_editorial_review_prompt_effect
- Definición: Campo operativo para adult editorial review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult editorial review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult editorial review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_EDITORIAL_REVIEW_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_EDITORIAL_REVIEW_PROMPT_EF
- Fallback: Reforzar adult editorial review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0882 — data_minimization_rule_prompt_effect
- Definición: Campo operativo para data minimization rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar data minimization rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar data minimization rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DATA_MINIMIZATION_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DATA_MINIMIZATION_RULE_PROMPT_EF
- Fallback: Reforzar data minimization rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0883 — consent_trace_prompt_effect
- Definición: Campo operativo para consent trace dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar consent trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar consent trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONSENT_TRACE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONSENT_TRACE_PROMPT_EFFECT
- Fallback: Reforzar consent trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0884 — commercial_use_flag_prompt_effect
- Definición: Campo operativo para commercial use flag dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar commercial use flag como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar commercial use flag como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMMERCIAL_USE_FLAG_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMMERCIAL_USE_FLAG_PROMPT_EFFEC
- Fallback: Reforzar commercial use flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0885 — vendor_terms_flag_prompt_effect
- Definición: Campo operativo para vendor terms flag dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vendor terms flag como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vendor terms flag como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VENDOR_TERMS_FLAG_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VENDOR_TERMS_FLAG_PROMPT_EFFECT
- Fallback: Reforzar vendor terms flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0886 — peru_context_rule_prompt_effect
- Definición: Campo operativo para peru context rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peru context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peru context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERU_CONTEXT_RULE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERU_CONTEXT_RULE_PROMPT_EFFECT
- Fallback: Reforzar peru context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0887 — fail_code_schema_prompt_effect
- Definición: Campo operativo para fail code schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fail code schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fail code schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAIL_CODE_SCHEMA_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAIL_CODE_SCHEMA_PROMPT_EFFECT
- Fallback: Reforzar fail code schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0888 — fallback_schema_prompt_effect
- Definición: Campo operativo para fallback schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fallback schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fallback schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FALLBACK_SCHEMA_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FALLBACK_SCHEMA_PROMPT_EFFECT
- Fallback: Reforzar fallback schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0889 — golden_test_schema_prompt_effect
- Definición: Campo operativo para golden test schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar golden test schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar golden test schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GOLDEN_TEST_SCHEMA_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GOLDEN_TEST_SCHEMA_PROMPT_EFFECT
- Fallback: Reforzar golden test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0890 — regression_test_schema_prompt_effect
- Definición: Campo operativo para regression test schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar regression test schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar regression test schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REGRESSION_TEST_SCHEMA_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REGRESSION_TEST_SCHEMA_PROMPT_EF
- Fallback: Reforzar regression test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0891 — padding_linter_prompt_effect
- Definición: Campo operativo para padding linter dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar padding linter como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar padding linter como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PADDING_LINTER_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PADDING_LINTER_PROMPT_EFFECT
- Fallback: Reforzar padding linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0892 — naming_linter_prompt_effect
- Definición: Campo operativo para naming linter dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar naming linter como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar naming linter como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NAMING_LINTER_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NAMING_LINTER_PROMPT_EFFECT
- Fallback: Reforzar naming linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0893 — source_runtime_gate_prompt_effect
- Definición: Campo operativo para source runtime gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source runtime gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source runtime gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_RUNTIME_GATE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_RUNTIME_GATE_PROMPT_EFFEC
- Fallback: Reforzar source runtime gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0894 — profile_fullness_gate_prompt_effect
- Definición: Campo operativo para profile fullness gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar profile fullness gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar profile fullness gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROFILE_FULLNESS_GATE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROFILE_FULLNESS_GATE_PROMPT_EFF
- Fallback: Reforzar profile fullness gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_EXPORT_0895 — copilot_render_gate_prompt_effect
- Definición: Campo operativo para copilot render gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar copilot render gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar copilot render gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COPILOT_RENDER_GATE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COPILOT_RENDER_GATE_PROMPT_EFFEC
- Fallback: Reforzar copilot render gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0896 — chatgpt_load_gate_prompt_effect
- Definición: Campo operativo para chatgpt load gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chatgpt load gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chatgpt load gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHATGPT_LOAD_GATE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHATGPT_LOAD_GATE_PROMPT_EFFECT
- Fallback: Reforzar chatgpt load gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0897 — project_factory_gate_prompt_effect
- Definición: Campo operativo para project factory gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project factory gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project factory gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_FACTORY_GATE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_FACTORY_GATE_PROMPT_EFFE
- Fallback: Reforzar project factory gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_0898 — generic_visual_system_gate_prompt_effect
- Definición: Campo operativo para generic_visual_system_reference gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic_visual_system_reference gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic_visual_system_reference gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_VISUAL_SYSTEM_GATE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_VISUAL_SYSTEM_GATE_PROMPT_EFFECT
- Fallback: Reforzar generic_visual_system_reference gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1297 — status_internal_qa_matrix
- Definición: Campo operativo para status internal dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar status internal como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar status internal como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STATUS_INTERNAL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STATUS_INTERNAL_QA_MATRIX
- Fallback: Reforzar status internal con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1298 — policy_set_qa_matrix
- Definición: Campo operativo para policy set dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar policy set como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar policy set como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POLICY_SET_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POLICY_SET_QA_MATRIX
- Fallback: Reforzar policy set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1299 — compatible_with_qa_matrix
- Definición: Campo operativo para compatible with dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar compatible with como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar compatible with como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMPATIBLE_WITH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMPATIBLE_WITH_QA_MATRIX
- Fallback: Reforzar compatible with con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1300 — source_trace_qa_matrix
- Definición: Campo operativo para source trace dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_TRACE_QA_MATRIX
- Fallback: Reforzar source trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1301 — source_classification_qa_matrix
- Definición: Campo operativo para source classification dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source classification como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source classification como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_CLASSIFICATION_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_CLASSIFICATION_QA_MATRIX
- Fallback: Reforzar source classification con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1302 — sha_lock_qa_matrix
- Definición: Campo operativo para sha lock dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sha lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sha lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHA_LOCK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHA_LOCK_QA_MATRIX
- Fallback: Reforzar sha lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1303 — lineage_lock_qa_matrix
- Definición: Campo operativo para lineage lock dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lineage lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lineage lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LINEAGE_LOCK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LINEAGE_LOCK_QA_MATRIX
- Fallback: Reforzar lineage lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1304 — version_semver_qa_matrix
- Definición: Campo operativo para version semver dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar version semver como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar version semver como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VERSION_SEMVER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VERSION_SEMVER_QA_MATRIX
- Fallback: Reforzar version semver con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1305 — migration_state_qa_matrix
- Definición: Campo operativo para migration state dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar migration state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar migration state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIGRATION_STATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIGRATION_STATE_QA_MATRIX
- Fallback: Reforzar migration state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1306 — no_loss_evidence_qa_matrix
- Definición: Campo operativo para no loss evidence dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no loss evidence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no loss evidence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_LOSS_EVIDENCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_LOSS_EVIDENCE_QA_MATRIX
- Fallback: Reforzar no loss evidence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1307 — audit_cycle_qa_matrix
- Definición: Campo operativo para audit cycle dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar audit cycle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar audit cycle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AUDIT_CYCLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AUDIT_CYCLE_QA_MATRIX
- Fallback: Reforzar audit cycle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1308 — final_only_gate_qa_matrix
- Definición: Campo operativo para final only gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar final only gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar final only gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINAL_ONLY_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINAL_ONLY_GATE_QA_MATRIX
- Fallback: Reforzar final only gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1309 — readback_gate_qa_matrix
- Definición: Campo operativo para readback gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar readback gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar readback gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_READBACK_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_READBACK_GATE_QA_MATRIX
- Fallback: Reforzar readback gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1310 — rebuild_gate_qa_matrix
- Definición: Campo operativo para rebuild gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rebuild gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rebuild gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REBUILD_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REBUILD_GATE_QA_MATRIX
- Fallback: Reforzar rebuild gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1311 — acceptance_gate_qa_matrix
- Definición: Campo operativo para acceptance gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar acceptance gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar acceptance gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCEPTANCE_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCEPTANCE_GATE_QA_MATRIX
- Fallback: Reforzar acceptance gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1312 — sidecar_schema_qa_matrix
- Definición: Campo operativo para sidecar schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sidecar schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sidecar schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SIDECAR_SCHEMA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SIDECAR_SCHEMA_QA_MATRIX
- Fallback: Reforzar sidecar schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1313 — watermark_state_qa_matrix
- Definición: Campo operativo para watermark state dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar watermark state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar watermark state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WATERMARK_STATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WATERMARK_STATE_QA_MATRIX
- Fallback: Reforzar watermark state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1314 — clean_master_rule_qa_matrix
- Definición: Campo operativo para clean master rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clean master rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clean master rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLEAN_MASTER_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLEAN_MASTER_RULE_QA_MATRIX
- Fallback: Reforzar clean master rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1315 — c2pa_conceptual_note_qa_matrix
- Definición: Campo operativo para c2pa conceptual note dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar c2pa conceptual note como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar c2pa conceptual note como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_C2PA_CONCEPTUAL_NOTE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_C2PA_CONCEPTUAL_NOTE_QA_MATRIX
- Fallback: Reforzar c2pa conceptual note con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1316 — prompt_hash_qa_matrix
- Definición: Campo operativo para prompt hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prompt hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prompt hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROMPT_HASH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROMPT_HASH_QA_MATRIX
- Fallback: Reforzar prompt hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1317 — output_hash_qa_matrix
- Definición: Campo operativo para output hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar output hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar output hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OUTPUT_HASH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OUTPUT_HASH_QA_MATRIX
- Fallback: Reforzar output hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1318 — vendor_parameters_qa_matrix
- Definición: Campo operativo para vendor parameters dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vendor parameters como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vendor parameters como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VENDOR_PARAMETERS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VENDOR_PARAMETERS_QA_MATRIX
- Fallback: Reforzar vendor parameters con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1319 — model_profile_hash_qa_matrix
- Definición: Campo operativo para model profile hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar model profile hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar model profile hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MODEL_PROFILE_HASH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MODEL_PROFILE_HASH_QA_MATRIX
- Fallback: Reforzar model profile hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1320 — project_hash_qa_matrix
- Definición: Campo operativo para project hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_HASH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_HASH_QA_MATRIX
- Fallback: Reforzar project hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1321 — qa_snapshot_qa_matrix
- Definición: Campo operativo para qa snapshot dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar qa snapshot como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar qa snapshot como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_QA_SNAPSHOT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_QA_SNAPSHOT_QA_MATRIX
- Fallback: Reforzar qa snapshot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1322 — fallback_history_qa_matrix
- Definición: Campo operativo para fallback history dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fallback history como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fallback history como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FALLBACK_HISTORY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FALLBACK_HISTORY_QA_MATRIX
- Fallback: Reforzar fallback history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1323 — regression_test_link_qa_matrix
- Definición: Campo operativo para regression test link dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar regression test link como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar regression test link como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REGRESSION_TEST_LINK_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REGRESSION_TEST_LINK_QA_MATRIX
- Fallback: Reforzar regression test link con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1324 — sidecar_required_fields_qa_matrix
- Definición: Campo operativo para sidecar required fields dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sidecar required fields como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sidecar required fields como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SIDECAR_REQUIRED_FIELDS_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SIDECAR_REQUIRED_FIELDS_QA_MATRI
- Fallback: Reforzar sidecar required fields con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1325 — privacy_review_qa_matrix
- Definición: Campo operativo para privacy review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar privacy review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar privacy review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRIVACY_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRIVACY_REVIEW_QA_MATRIX
- Fallback: Reforzar privacy review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1326 — ley_29733_review_qa_matrix
- Definición: Campo operativo para ley 29733 review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ley 29733 review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ley 29733 review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LEY_29733_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LEY_29733_REVIEW_QA_MATRIX
- Fallback: Reforzar ley 29733 review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1327 — license_review_qa_matrix
- Definición: Campo operativo para license review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar license review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar license review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LICENSE_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LICENSE_REVIEW_QA_MATRIX
- Fallback: Reforzar license review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1328 — likeness_review_qa_matrix
- Definición: Campo operativo para likeness review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar likeness review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar likeness review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIKENESS_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIKENESS_REVIEW_QA_MATRIX
- Fallback: Reforzar likeness review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1329 — brand_logo_review_qa_matrix
- Definición: Campo operativo para brand logo review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_REVIEW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_REVIEW_QA_MATRIX
- Fallback: Reforzar brand logo review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1330 — adult_editorial_review_qa_matrix
- Definición: Campo operativo para adult editorial review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult editorial review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult editorial review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_EDITORIAL_REVIEW_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_EDITORIAL_REVIEW_QA_MATRIX
- Fallback: Reforzar adult editorial review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1331 — data_minimization_rule_qa_matrix
- Definición: Campo operativo para data minimization rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar data minimization rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar data minimization rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DATA_MINIMIZATION_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DATA_MINIMIZATION_RULE_QA_MATRIX
- Fallback: Reforzar data minimization rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1332 — consent_trace_qa_matrix
- Definición: Campo operativo para consent trace dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar consent trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar consent trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONSENT_TRACE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONSENT_TRACE_QA_MATRIX
- Fallback: Reforzar consent trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1333 — commercial_use_flag_qa_matrix
- Definición: Campo operativo para commercial use flag dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar commercial use flag como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar commercial use flag como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMMERCIAL_USE_FLAG_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMMERCIAL_USE_FLAG_QA_MATRIX
- Fallback: Reforzar commercial use flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1334 — vendor_terms_flag_qa_matrix
- Definición: Campo operativo para vendor terms flag dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vendor terms flag como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vendor terms flag como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VENDOR_TERMS_FLAG_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VENDOR_TERMS_FLAG_QA_MATRIX
- Fallback: Reforzar vendor terms flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1335 — peru_context_rule_qa_matrix
- Definición: Campo operativo para peru context rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peru context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peru context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERU_CONTEXT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERU_CONTEXT_RULE_QA_MATRIX
- Fallback: Reforzar peru context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1336 — fail_code_schema_qa_matrix
- Definición: Campo operativo para fail code schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fail code schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fail code schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAIL_CODE_SCHEMA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAIL_CODE_SCHEMA_QA_MATRIX
- Fallback: Reforzar fail code schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1337 — fallback_schema_qa_matrix
- Definición: Campo operativo para fallback schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fallback schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fallback schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FALLBACK_SCHEMA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FALLBACK_SCHEMA_QA_MATRIX
- Fallback: Reforzar fallback schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1338 — golden_test_schema_qa_matrix
- Definición: Campo operativo para golden test schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar golden test schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar golden test schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GOLDEN_TEST_SCHEMA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GOLDEN_TEST_SCHEMA_QA_MATRIX
- Fallback: Reforzar golden test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1339 — regression_test_schema_qa_matrix
- Definición: Campo operativo para regression test schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar regression test schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar regression test schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REGRESSION_TEST_SCHEMA_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REGRESSION_TEST_SCHEMA_QA_MATRIX
- Fallback: Reforzar regression test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1340 — padding_linter_qa_matrix
- Definición: Campo operativo para padding linter dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar padding linter como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar padding linter como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PADDING_LINTER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PADDING_LINTER_QA_MATRIX
- Fallback: Reforzar padding linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1341 — naming_linter_qa_matrix
- Definición: Campo operativo para naming linter dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar naming linter como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar naming linter como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NAMING_LINTER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NAMING_LINTER_QA_MATRIX
- Fallback: Reforzar naming linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1342 — source_runtime_gate_qa_matrix
- Definición: Campo operativo para source runtime gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source runtime gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source runtime gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_RUNTIME_GATE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_RUNTIME_GATE_QA_MATRIX
- Fallback: Reforzar source runtime gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1343 — profile_fullness_gate_qa_matrix
- Definición: Campo operativo para profile fullness gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar profile fullness gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar profile fullness gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROFILE_FULLNESS_GATE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROFILE_FULLNESS_GATE_QA_MATRIX
- Fallback: Reforzar profile fullness gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_EXPORT_1344 — copilot_render_gate_qa_matrix
- Definición: Campo operativo para copilot render gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar copilot render gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar copilot render gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COPILOT_RENDER_GATE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COPILOT_RENDER_GATE_QA_MATRIX
- Fallback: Reforzar copilot render gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1345 — chatgpt_load_gate_qa_matrix
- Definición: Campo operativo para chatgpt load gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chatgpt load gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chatgpt load gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHATGPT_LOAD_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHATGPT_LOAD_GATE_QA_MATRIX
- Fallback: Reforzar chatgpt load gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1346 — project_factory_gate_qa_matrix
- Definición: Campo operativo para project factory gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project factory gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project factory gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_FACTORY_GATE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_FACTORY_GATE_QA_MATRIX
- Fallback: Reforzar project factory gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1347 — generic_visual_system_gate_qa_matrix
- Definición: Campo operativo para generic_visual_system_reference gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic_visual_system_reference gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic_visual_system_reference gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_VISUAL_SYSTEM_GATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_VISUAL_SYSTEM_GATE_QA_MATRIX
- Fallback: Reforzar generic_visual_system_reference gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1746 — status_internal_vendor_repair
- Definición: Campo operativo para status internal dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar status internal como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar status internal como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STATUS_INTERNAL_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STATUS_INTERNAL_VENDOR_REPAIR
- Fallback: Reforzar status internal con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1747 — policy_set_vendor_repair
- Definición: Campo operativo para policy set dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar policy set como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar policy set como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POLICY_SET_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POLICY_SET_VENDOR_REPAIR
- Fallback: Reforzar policy set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1748 — compatible_with_vendor_repair
- Definición: Campo operativo para compatible with dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar compatible with como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar compatible with como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMPATIBLE_WITH_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMPATIBLE_WITH_VENDOR_REPAIR
- Fallback: Reforzar compatible with con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1749 — source_trace_vendor_repair
- Definición: Campo operativo para source trace dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_TRACE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_TRACE_VENDOR_REPAIR
- Fallback: Reforzar source trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1750 — source_classification_vendor_repair
- Definición: Campo operativo para source classification dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source classification como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source classification como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_CLASSIFICATION_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_CLASSIFICATION_VENDOR_REP
- Fallback: Reforzar source classification con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1751 — sha_lock_vendor_repair
- Definición: Campo operativo para sha lock dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sha lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sha lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHA_LOCK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHA_LOCK_VENDOR_REPAIR
- Fallback: Reforzar sha lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1752 — lineage_lock_vendor_repair
- Definición: Campo operativo para lineage lock dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lineage lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lineage lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LINEAGE_LOCK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LINEAGE_LOCK_VENDOR_REPAIR
- Fallback: Reforzar lineage lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1753 — version_semver_vendor_repair
- Definición: Campo operativo para version semver dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar version semver como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar version semver como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VERSION_SEMVER_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VERSION_SEMVER_VENDOR_REPAIR
- Fallback: Reforzar version semver con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1754 — migration_state_vendor_repair
- Definición: Campo operativo para migration state dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar migration state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar migration state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIGRATION_STATE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIGRATION_STATE_VENDOR_REPAIR
- Fallback: Reforzar migration state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1755 — no_loss_evidence_vendor_repair
- Definición: Campo operativo para no loss evidence dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no loss evidence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no loss evidence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_LOSS_EVIDENCE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_LOSS_EVIDENCE_VENDOR_REPAIR
- Fallback: Reforzar no loss evidence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1756 — audit_cycle_vendor_repair
- Definición: Campo operativo para audit cycle dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar audit cycle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar audit cycle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AUDIT_CYCLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AUDIT_CYCLE_VENDOR_REPAIR
- Fallback: Reforzar audit cycle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1757 — final_only_gate_vendor_repair
- Definición: Campo operativo para final only gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar final only gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar final only gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINAL_ONLY_GATE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINAL_ONLY_GATE_VENDOR_REPAIR
- Fallback: Reforzar final only gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1758 — readback_gate_vendor_repair
- Definición: Campo operativo para readback gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar readback gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar readback gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_READBACK_GATE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_READBACK_GATE_VENDOR_REPAIR
- Fallback: Reforzar readback gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1759 — rebuild_gate_vendor_repair
- Definición: Campo operativo para rebuild gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rebuild gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rebuild gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REBUILD_GATE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REBUILD_GATE_VENDOR_REPAIR
- Fallback: Reforzar rebuild gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1760 — acceptance_gate_vendor_repair
- Definición: Campo operativo para acceptance gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar acceptance gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar acceptance gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCEPTANCE_GATE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCEPTANCE_GATE_VENDOR_REPAIR
- Fallback: Reforzar acceptance gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1761 — sidecar_schema_vendor_repair
- Definición: Campo operativo para sidecar schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sidecar schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sidecar schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SIDECAR_SCHEMA_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SIDECAR_SCHEMA_VENDOR_REPAIR
- Fallback: Reforzar sidecar schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1762 — watermark_state_vendor_repair
- Definición: Campo operativo para watermark state dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar watermark state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar watermark state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WATERMARK_STATE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WATERMARK_STATE_VENDOR_REPAIR
- Fallback: Reforzar watermark state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1763 — clean_master_rule_vendor_repair
- Definición: Campo operativo para clean master rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clean master rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clean master rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLEAN_MASTER_RULE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLEAN_MASTER_RULE_VENDOR_REPAIR
- Fallback: Reforzar clean master rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1764 — c2pa_conceptual_note_vendor_repair
- Definición: Campo operativo para c2pa conceptual note dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar c2pa conceptual note como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar c2pa conceptual note como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_C2PA_CONCEPTUAL_NOTE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_C2PA_CONCEPTUAL_NOTE_VENDOR_REPA
- Fallback: Reforzar c2pa conceptual note con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1765 — prompt_hash_vendor_repair
- Definición: Campo operativo para prompt hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prompt hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prompt hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROMPT_HASH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROMPT_HASH_VENDOR_REPAIR
- Fallback: Reforzar prompt hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1766 — output_hash_vendor_repair
- Definición: Campo operativo para output hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar output hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar output hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OUTPUT_HASH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OUTPUT_HASH_VENDOR_REPAIR
- Fallback: Reforzar output hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1767 — vendor_parameters_vendor_repair
- Definición: Campo operativo para vendor parameters dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vendor parameters como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vendor parameters como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VENDOR_PARAMETERS_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VENDOR_PARAMETERS_VENDOR_REPAIR
- Fallback: Reforzar vendor parameters con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1768 — model_profile_hash_vendor_repair
- Definición: Campo operativo para model profile hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar model profile hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar model profile hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MODEL_PROFILE_HASH_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MODEL_PROFILE_HASH_VENDOR_REPAIR
- Fallback: Reforzar model profile hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1769 — project_hash_vendor_repair
- Definición: Campo operativo para project hash dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project hash como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project hash como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_HASH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_HASH_VENDOR_REPAIR
- Fallback: Reforzar project hash con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1770 — qa_snapshot_vendor_repair
- Definición: Campo operativo para qa snapshot dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar qa snapshot como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar qa snapshot como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_QA_SNAPSHOT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_QA_SNAPSHOT_VENDOR_REPAIR
- Fallback: Reforzar qa snapshot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1771 — fallback_history_vendor_repair
- Definición: Campo operativo para fallback history dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fallback history como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fallback history como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FALLBACK_HISTORY_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FALLBACK_HISTORY_VENDOR_REPAIR
- Fallback: Reforzar fallback history con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1772 — regression_test_link_vendor_repair
- Definición: Campo operativo para regression test link dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar regression test link como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar regression test link como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REGRESSION_TEST_LINK_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REGRESSION_TEST_LINK_VENDOR_REPA
- Fallback: Reforzar regression test link con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1773 — sidecar_required_fields_vendor_repair
- Definición: Campo operativo para sidecar required fields dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sidecar required fields como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sidecar required fields como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SIDECAR_REQUIRED_FIELDS_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SIDECAR_REQUIRED_FIELDS_VENDOR_R
- Fallback: Reforzar sidecar required fields con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1774 — privacy_review_vendor_repair
- Definición: Campo operativo para privacy review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar privacy review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar privacy review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRIVACY_REVIEW_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRIVACY_REVIEW_VENDOR_REPAIR
- Fallback: Reforzar privacy review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1775 — ley_29733_review_vendor_repair
- Definición: Campo operativo para ley 29733 review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ley 29733 review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ley 29733 review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LEY_29733_REVIEW_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LEY_29733_REVIEW_VENDOR_REPAIR
- Fallback: Reforzar ley 29733 review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1776 — license_review_vendor_repair
- Definición: Campo operativo para license review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar license review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar license review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LICENSE_REVIEW_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LICENSE_REVIEW_VENDOR_REPAIR
- Fallback: Reforzar license review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1777 — likeness_review_vendor_repair
- Definición: Campo operativo para likeness review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar likeness review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar likeness review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIKENESS_REVIEW_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIKENESS_REVIEW_VENDOR_REPAIR
- Fallback: Reforzar likeness review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1778 — brand_logo_review_vendor_repair
- Definición: Campo operativo para brand logo review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_REVIEW_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_REVIEW_VENDOR_REPAIR
- Fallback: Reforzar brand logo review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1779 — adult_editorial_review_vendor_repair
- Definición: Campo operativo para adult editorial review dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult editorial review como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult editorial review como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_EDITORIAL_REVIEW_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_EDITORIAL_REVIEW_VENDOR_RE
- Fallback: Reforzar adult editorial review con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1780 — data_minimization_rule_vendor_repair
- Definición: Campo operativo para data minimization rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar data minimization rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar data minimization rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DATA_MINIMIZATION_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DATA_MINIMIZATION_RULE_VENDOR_RE
- Fallback: Reforzar data minimization rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1781 — consent_trace_vendor_repair
- Definición: Campo operativo para consent trace dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar consent trace como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar consent trace como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONSENT_TRACE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONSENT_TRACE_VENDOR_REPAIR
- Fallback: Reforzar consent trace con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1782 — commercial_use_flag_vendor_repair
- Definición: Campo operativo para commercial use flag dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar commercial use flag como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar commercial use flag como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMMERCIAL_USE_FLAG_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMMERCIAL_USE_FLAG_VENDOR_REPAI
- Fallback: Reforzar commercial use flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1783 — vendor_terms_flag_vendor_repair
- Definición: Campo operativo para vendor terms flag dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vendor terms flag como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vendor terms flag como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VENDOR_TERMS_FLAG_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VENDOR_TERMS_FLAG_VENDOR_REPAIR
- Fallback: Reforzar vendor terms flag con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1784 — peru_context_rule_vendor_repair
- Definición: Campo operativo para peru context rule dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar peru context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar peru context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERU_CONTEXT_RULE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERU_CONTEXT_RULE_VENDOR_REPAIR
- Fallback: Reforzar peru context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1785 — fail_code_schema_vendor_repair
- Definición: Campo operativo para fail code schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fail code schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fail code schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAIL_CODE_SCHEMA_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAIL_CODE_SCHEMA_VENDOR_REPAIR
- Fallback: Reforzar fail code schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1786 — fallback_schema_vendor_repair
- Definición: Campo operativo para fallback schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fallback schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fallback schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FALLBACK_SCHEMA_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FALLBACK_SCHEMA_VENDOR_REPAIR
- Fallback: Reforzar fallback schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1787 — golden_test_schema_vendor_repair
- Definición: Campo operativo para golden test schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar golden test schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar golden test schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GOLDEN_TEST_SCHEMA_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GOLDEN_TEST_SCHEMA_VENDOR_REPAIR
- Fallback: Reforzar golden test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1788 — regression_test_schema_vendor_repair
- Definición: Campo operativo para regression test schema dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar regression test schema como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar regression test schema como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REGRESSION_TEST_SCHEMA_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REGRESSION_TEST_SCHEMA_VENDOR_RE
- Fallback: Reforzar regression test schema con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1789 — padding_linter_vendor_repair
- Definición: Campo operativo para padding linter dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar padding linter como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar padding linter como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PADDING_LINTER_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PADDING_LINTER_VENDOR_REPAIR
- Fallback: Reforzar padding linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1790 — naming_linter_vendor_repair
- Definición: Campo operativo para naming linter dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar naming linter como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar naming linter como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NAMING_LINTER_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NAMING_LINTER_VENDOR_REPAIR
- Fallback: Reforzar naming linter con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1791 — source_runtime_gate_vendor_repair
- Definición: Campo operativo para source runtime gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar source runtime gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar source runtime gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOURCE_RUNTIME_GATE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOURCE_RUNTIME_GATE_VENDOR_REPAI
- Fallback: Reforzar source runtime gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1792 — profile_fullness_gate_vendor_repair
- Definición: Campo operativo para profile fullness gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar profile fullness gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar profile fullness gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROFILE_FULLNESS_GATE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROFILE_FULLNESS_GATE_VENDOR_REP
- Fallback: Reforzar profile fullness gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_EXPORT_1793 — copilot_render_gate_vendor_repair
- Definición: Campo operativo para copilot render gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar copilot render gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar copilot render gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COPILOT_RENDER_GATE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COPILOT_RENDER_GATE_VENDOR_REPAI
- Fallback: Reforzar copilot render gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1794 — chatgpt_load_gate_vendor_repair
- Definición: Campo operativo para chatgpt load gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chatgpt load gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chatgpt load gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHATGPT_LOAD_GATE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHATGPT_LOAD_GATE_VENDOR_REPAIR
- Fallback: Reforzar chatgpt load gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1795 — project_factory_gate_vendor_repair
- Definición: Campo operativo para project factory gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar project factory gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar project factory gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROJECT_FACTORY_GATE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROJECT_FACTORY_GATE_VENDOR_REPA
- Fallback: Reforzar project factory gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SIDECAR_1796 — generic_visual_system_gate_vendor_repair
- Definición: Campo operativo para generic_visual_system_reference gate dentro de Gobernanza, sidecar, watermark, legal, QA, no-loss y lineage. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic_visual_system_reference gate como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic_visual_system_reference gate como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_VISUAL_SYSTEM_GATE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_VISUAL_SYSTEM_GATE_VENDOR_REPAIR
- Fallback: Reforzar generic_visual_system_reference gate con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
