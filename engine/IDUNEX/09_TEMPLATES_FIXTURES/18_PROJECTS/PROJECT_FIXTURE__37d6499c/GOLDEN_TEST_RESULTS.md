# GOLDEN_TEST_RESULTS — executable smoke evidence

## image — GT_IMAGE_FRONT_IDENTITY_LOCK
- input_fixture: IMAGE_TEST fixture in PROJECT_FIXTURE_CANONICAL_SMOKE_TEST
- expected_result: image respects Profile360 fields, source trace, sidecar and no-global-go policy
- actual_result_or_mock: validated_mock_result_recorded_for_non_production_smoke_test
- comparison_method: schema + field trace + sidecar + hash evidence + reviewer decision
- pass_fail_decision: PASS
- fail_codes_triggered: none
- fallback_applied: NO_FALLBACK_REQUIRED_AFTER_RETEST_PASS
- retest_result: PASS
- sidecar_id: SMOKE_OUTPUT_MULTIMODAL_EVIDENCE_001

## video — GT_VIDEO_FRAME_START_MID_END_LOCK
- input_fixture: VIDEO_TEST fixture in PROJECT_FIXTURE_CANONICAL_SMOKE_TEST
- expected_result: video respects Profile360 fields, source trace, sidecar and no-global-go policy
- actual_result_or_mock: validated_mock_result_recorded_for_non_production_smoke_test
- comparison_method: schema + field trace + sidecar + hash evidence + reviewer decision
- pass_fail_decision: PASS
- fail_codes_triggered: none
- fallback_applied: NO_FALLBACK_REQUIRED_AFTER_RETEST_PASS
- retest_result: PASS
- sidecar_id: SMOKE_OUTPUT_MULTIMODAL_EVIDENCE_001

## voice — GT_VOICE_TIMBRE_LOCK
- input_fixture: VOICE_TEST fixture in PROJECT_FIXTURE_CANONICAL_SMOKE_TEST
- expected_result: voice respects Profile360 fields, source trace, sidecar and no-global-go policy
- actual_result_or_mock: validated_mock_result_recorded_for_non_production_smoke_test
- comparison_method: schema + field trace + sidecar + hash evidence + reviewer decision
- pass_fail_decision: PASS
- fail_codes_triggered: none
- fallback_applied: NO_FALLBACK_REQUIRED_AFTER_RETEST_PASS
- retest_result: PASS
- sidecar_id: SMOKE_OUTPUT_MULTIMODAL_EVIDENCE_001

## suno — GT_SUNO_LYRIC_PERSONALITY
- input_fixture: SUNO_TEST fixture in PROJECT_FIXTURE_CANONICAL_SMOKE_TEST
- expected_result: suno respects Profile360 fields, source trace, sidecar and no-global-go policy
- actual_result_or_mock: validated_mock_result_recorded_for_non_production_smoke_test
- comparison_method: schema + field trace + sidecar + hash evidence + reviewer decision
- pass_fail_decision: PASS
- fail_codes_triggered: none
- fallback_applied: NO_FALLBACK_REQUIRED_AFTER_RETEST_PASS
- retest_result: PASS
- sidecar_id: SMOKE_OUTPUT_MULTIMODAL_EVIDENCE_001

## copilot_docx — GT_COPILOT_DOCX_READBACK
- input_fixture: COPILOT_DOCX_TEST fixture in PROJECT_FIXTURE_CANONICAL_SMOKE_TEST
- expected_result: copilot_docx respects Profile360 fields, source trace, sidecar and no-global-go policy
- actual_result_or_mock: validated_mock_result_recorded_for_non_production_smoke_test
- comparison_method: schema + field trace + sidecar + hash evidence + reviewer decision
- pass_fail_decision: PASS
- fail_codes_triggered: none
- fallback_applied: NO_FALLBACK_REQUIRED_AFTER_RETEST_PASS
- retest_result: PASS
- sidecar_id: SMOKE_OUTPUT_MULTIMODAL_EVIDENCE_001

## sidecar — GT_SIDECAR_SCHEMA
- input_fixture: SIDECAR_TEST fixture in PROJECT_FIXTURE_CANONICAL_SMOKE_TEST
- expected_result: sidecar respects Profile360 fields, source trace, sidecar and no-global-go policy
- actual_result_or_mock: validated_mock_result_recorded_for_non_production_smoke_test
- comparison_method: schema + field trace + sidecar + hash evidence + reviewer decision
- pass_fail_decision: PASS
- fail_codes_triggered: none
- fallback_applied: NO_FALLBACK_REQUIRED_AFTER_RETEST_PASS
- retest_result: PASS
- sidecar_id: SMOKE_OUTPUT_MULTIMODAL_EVIDENCE_001

## Hashes
- hash_input: `sha256:4a3af41189908c42927f7f591f0ed9c8099746aa214d48d5cc97bb48f2a6a50e`
- hash_output: `sha256:f8e34febaf18eb57f295adfb6cf7fb5018a0ad1ea79344b282f7d5670ccffa45`

## Decision
prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE. GLOBAL_GO remains prohibited until real project output evidence.
