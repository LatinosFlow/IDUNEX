# GOLDEN TESTS VOICE

Cada prueba es específica para VOICE; no se permite copiar pasos genéricos sin parámetros de modalidad.


## GT_VOICE_ADULT_AGE
- test_id: GT_VOICE_ADULT_AGE
- modality: voice
- required_inputs: Profile360 field P360_VOICE_0212, source_ids SRC_012_Lenguaje_acento_y_voz_escrita, SRC_022_Voz_hablada_para_ElevenLabs, SRC_033_Causalidad_edad-origen-psicolog_a-voz, adapter elevenlabs_voice_adapter, locks activos y sidecar schema.
- steps: 1) cargar campos de la modalidad; 2) generar especificación controlada; 3) comparar parámetros medibles; 4) validar continuidad/identidad/traza; 5) registrar sidecar y hash; 6) ejecutar retest si hay WARNING/FAIL.
- expected_result: output coherente con profile360_voice y sin drift.
- fail_conditions: falta source trace, campo genérico, adapter incorrecto, placeholder final, drift, schema fail o sidecar incompleto.
- measurement_method: checklist por modalidad + matriz canónica + validator.
- source_ids_required: SRC_012_Lenguaje_acento_y_voz_escrita, SRC_022_Voz_hablada_para_ElevenLabs, SRC_033_Causalidad_edad-origen-psicolog_a-voz, SRC_041_PERUVIAN_SPANISH_ACCENT_SOCIOLECT
- field_ids_required: P360_VOICE_0212
- adapter_required: elevenlabs_voice_adapter
- fail_codes_triggered: FAIL_VOICE_0212_PITCH_RANGE
- fallback_fix: Si falla pitch_range, recargar primary_source_id SRC_012_Lenguaje_acento_y_voz_escrita, cruzar supporting_source_ids SRC_022_Voz_hablada_para_ElevenLabs, SRC_03...
- retest_required: true
- production_decision: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE only if PASS; no GLOBAL_GO.

## GT_VOICE_TIMBRE_LOCK
- test_id: GT_VOICE_TIMBRE_LOCK
- modality: voice
- required_inputs: Profile360 field P360_QA_0423, source_ids SRC_025_Golden_Tests_de_identidad, SRC_030_No-loss_migration_y_compatibilidad, SRC_038_PAIRWISE_UNIQUENESS_METRICS, adapter chatgpt_json_txt_adapter, locks activos y sidecar schema.
- steps: 1) cargar campos de la modalidad; 2) generar especificación controlada; 3) comparar parámetros medibles; 4) validar continuidad/identidad/traza; 5) registrar sidecar y hash; 6) ejecutar retest si hay WARNING/FAIL.
- expected_result: output coherente con profile360_qa y sin drift.
- fail_conditions: falta source trace, campo genérico, adapter incorrecto, placeholder final, drift, schema fail o sidecar incompleto.
- measurement_method: checklist por modalidad + matriz canónica + validator.
- source_ids_required: SRC_025_Golden_Tests_de_identidad, SRC_030_No-loss_migration_y_compatibilidad, SRC_038_PAIRWISE_UNIQUENESS_METRICS, SRC_047_JSON_SCHEMA_LINTER_NOLOSS
- field_ids_required: P360_QA_0423
- adapter_required: chatgpt_json_txt_adapter
- fail_codes_triggered: FAIL_QA_0423_QA_SNAPSHOT
- fallback_fix: Si falla qa_snapshot, recargar primary_source_id SRC_025_Golden_Tests_de_identidad, cruzar supporting_source_ids SRC_030_No-loss_migration_y_compatibilidad, SRC...
- retest_required: true
- production_decision: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE only if PASS; no GLOBAL_GO.

## GT_VOICE_ACCENT_LOCK
- test_id: GT_VOICE_ACCENT_LOCK
- modality: voice
- required_inputs: Profile360 field P360_SKIN_0634, source_ids SRC_004_Dermatolog_a_visual_realista, SRC_040_ETHNO_PHENOTYPE_CAUSALITY_SAFE, SRC_032_Anti_same-face_anti_same-body_para_10_modelos, adapter image_prompt_adapter, locks activos y sidecar schema.
- steps: 1) cargar campos de la modalidad; 2) generar especificación controlada; 3) comparar parámetros medibles; 4) validar continuidad/identidad/traza; 5) registrar sidecar y hash; 6) ejecutar retest si hay WARNING/FAIL.
- expected_result: output coherente con profile360_skin y sin drift.
- fail_conditions: falta source trace, campo genérico, adapter incorrecto, placeholder final, drift, schema fail o sidecar incompleto.
- measurement_method: checklist por modalidad + matriz canónica + validator.
- source_ids_required: SRC_004_Dermatolog_a_visual_realista, SRC_040_ETHNO_PHENOTYPE_CAUSALITY_SAFE, SRC_032_Anti_same-face_anti_same-body_para_10_modelos
- field_ids_required: P360_SKIN_0634
- adapter_required: image_prompt_adapter
- fail_codes_triggered: FAIL_SKIN_0634_LAYERING_RULE_PROMPT_EFFECT
- fallback_fix: Si falla layering_rule_prompt_effect, recargar primary_source_id SRC_004_Dermatolog_a_visual_realista, cruzar supporting_source_ids SRC_040_ETHNO_PHENOTYPE_CAUS...
- retest_required: true
- production_decision: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE only if PASS; no GLOBAL_GO.

## GT_VOICE_PROSODY_NATURALNESS
- test_id: GT_VOICE_PROSODY_NATURALNESS
- modality: voice
- required_inputs: Profile360 field P360_SCENE_0845, source_ids SRC_017_C_mara_sensor_lente_y_fotograf_a_premium, SRC_021_Video_IA_y_continuidad_entre_planos, SRC_027_C2PA_watermark_y_sidecar, adapter image_prompt_adapter, locks activos y sidecar schema.
- steps: 1) cargar campos de la modalidad; 2) generar especificación controlada; 3) comparar parámetros medibles; 4) validar continuidad/identidad/traza; 5) registrar sidecar y hash; 6) ejecutar retest si hay WARNING/FAIL.
- expected_result: output coherente con profile360_scene y sin drift.
- fail_conditions: falta source trace, campo genérico, adapter incorrecto, placeholder final, drift, schema fail o sidecar incompleto.
- measurement_method: checklist por modalidad + matriz canónica + validator.
- source_ids_required: SRC_017_C_mara_sensor_lente_y_fotograf_a_premium, SRC_021_Video_IA_y_continuidad_entre_planos, SRC_027_C2PA_watermark_y_sidecar
- field_ids_required: P360_SCENE_0845
- adapter_required: image_prompt_adapter
- fail_codes_triggered: FAIL_SCENE_0845_BACKGROUND_IDENTITY_CONFLICT_RULE_PROMPT_EFFECT
- fallback_fix: Si falla background_identity_conflict_rule_prompt_effect, recargar primary_source_id SRC_017_C_mara_sensor_lente_y_fotograf_a_premium, cruzar supporting_source_...
- retest_required: true
- production_decision: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE only if PASS; no GLOBAL_GO.

## GT_VOICE_SPEAKER_DRIFT
- test_id: GT_VOICE_SPEAKER_DRIFT
- modality: voice
- required_inputs: Profile360 field P360_QA_1056, source_ids SRC_025_Golden_Tests_de_identidad, SRC_030_No-loss_migration_y_compatibilidad, SRC_038_PAIRWISE_UNIQUENESS_METRICS, adapter chatgpt_json_txt_adapter, locks activos y sidecar schema.
- steps: 1) cargar campos de la modalidad; 2) generar especificación controlada; 3) comparar parámetros medibles; 4) validar continuidad/identidad/traza; 5) registrar sidecar y hash; 6) ejecutar retest si hay WARNING/FAIL.
- expected_result: output coherente con profile360_qa y sin drift.
- fail_conditions: falta source trace, campo genérico, adapter incorrecto, placeholder final, drift, schema fail o sidecar incompleto.
- measurement_method: checklist por modalidad + matriz canónica + validator.
- source_ids_required: SRC_025_Golden_Tests_de_identidad, SRC_030_No-loss_migration_y_compatibilidad, SRC_038_PAIRWISE_UNIQUENESS_METRICS, SRC_047_JSON_SCHEMA_LINTER_NOLOSS
- field_ids_required: P360_QA_1056
- adapter_required: chatgpt_json_txt_adapter
- fail_codes_triggered: FAIL_QA_1056_IMPOSSIBLE_POSE_BLOCKER_QA_MATRIX
- fallback_fix: Si falla impossible_pose_blocker_qa_matrix, recargar primary_source_id SRC_025_Golden_Tests_de_identidad, cruzar supporting_source_ids SRC_030_No-loss_migration...
- retest_required: true
- production_decision: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE only if PASS; no GLOBAL_GO.

## HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3 Remediación final QA/Evidencia/Hash


### Procedimiento ejecutable HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3
1. Input files: registry, source-to-runtime map, source inventory, source cards, schemas, smoke test, sidecar and manifests.
2. Execution steps: load JSON, validate schema, compute field/source/adapter coverage, compare manifest counts and hashes, inspect evidence_bundle, run smoke-test scope checks.
3. Checks: no missing fields, no missing source_ids, no adapter drift, no stale hash, no generic golden test, no GLOBAL_GO.
4. PASS criteria: zero critical errors, zero warnings for permitted state, project_test_ready_no_global_go only. [HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY]
5. FAIL criteria: schema mismatch, missing evidence, fake hash, coverage 10 without execution, sidecar mismatch, source card drift.
6. Fail codes: use registry fail_code plus blocker rules from HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3.
7. Fallback fixes: regenerate affected file from runtime truth source, retest and update manifests.
8. Retest protocol: re-run `VALIDATE_IDUNEX_RUNTIME.py` and verify external SHA.
9. Output report format: JSON validation result plus QA_FINAL_REPORT markdown.
10. Production decision: never escalate to GLOBAL_GO without real project evidence.

## Executable QA Procedure
- purpose: validate this QA dimension without interpretation drift.
- input files: project manifest, Profile360 fields, source map, fail codes, sidecars, hash evidence and modality fixtures.
- execution command: run `python IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py` and then execute the modality-specific checklist in this file.
- validation rules: JSON/schema pass; source trace present; field trace present; adapter trace present; sidecar hash present; GLOBAL_GO false.
- pass criteria: all checks pass with no critical errors and no unresolved placeholders in non-template outputs.
- warning criteria: baseline-only evidence, support-only source, coverage capped at 8/9, or manual review required before PROJECT_GO.
- fail criteria: schema mismatch, missing sidecar, missing hash evidence, adapter mismatch, GLOBAL_GO attempted from motor baseline.
- fail codes: FAIL_BLOCKER_VALIDATOR_INCOMPLETE; FAIL_BLOCKER_COVERAGE_10_WITHOUT_REAL_OUTPUT_EVIDENCE; FAIL_BLOCKER_GLOBAL_GO_FROM_MOTOR_BASELINE.
- fallback fixes: regenerate affected manifest, rerun source-to-runtime map, repair sidecar, recalculate hash, repeat test.
- retest protocol: rerun validator and produce PASS/FAIL report with timestamp and reviewer.
- output report format: JSON QA result plus Markdown summary with evidence paths and go/no-go decision.
- production decision: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE only; PROJECT_GO/GLOBAL_GO forbidden without real project evidence.

### Example PASS report
`audit_status=PASS`, `global_go=false`, all schemas valid, sidecars present, hash evidence reproducible, coverage score <= 9. [HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY]

### Example FAIL report
`audit_status=FAIL`, schema mismatch or missing sidecar/hash, fallback listed, retest required.
