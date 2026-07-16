# GOLDEN_TESTS_BY_MODALITY

| test_id | modality | specificity | release rule |
|---|---|---|---|
| GT_IMAGE_FRONT_IDENTITY_LOCK | IMAGE | modality-specific | PASS requires sidecar and adapter trace |
| GT_IMAGE_3Q_IDENTITY_LOCK | IMAGE | modality-specific | PASS requires sidecar and adapter trace |
| GT_IMAGE_PROFILE_IDENTITY_LOCK | IMAGE | modality-specific | PASS requires sidecar and adapter trace |
| GT_IMAGE_FULL_BODY_PROPORTIONS | IMAGE | modality-specific | PASS requires sidecar and adapter trace |
| GT_IMAGE_HANDS_FEET_ANATOMY | IMAGE | modality-specific | PASS requires sidecar and adapter trace |
| GT_IMAGE_SKIN_HAIR_REALISM | IMAGE | modality-specific | PASS requires sidecar and adapter trace |
| GT_IMAGE_WARDROBE_PHYSICS | IMAGE | modality-specific | PASS requires sidecar and adapter trace |
| GT_VIDEO_FRAME_START_MID_END_LOCK | VIDEO | modality-specific | PASS requires sidecar and adapter trace |
| GT_VIDEO_FACE_MORPH_BLOCKER | VIDEO | modality-specific | PASS requires sidecar and adapter trace |
| GT_VIDEO_BODY_MORPH_BLOCKER | VIDEO | modality-specific | PASS requires sidecar and adapter trace |
| GT_VIDEO_WARDROBE_CONTINUITY | VIDEO | modality-specific | PASS requires sidecar and adapter trace |
| GT_VIDEO_LIGHTING_CONTINUITY | VIDEO | modality-specific | PASS requires sidecar and adapter trace |
| GT_VIDEO_CAMERA_PATH_STABILITY | VIDEO | modality-specific | PASS requires sidecar and adapter trace |
| GT_VOICE_ADULT_AGE | VOICE | modality-specific | PASS requires sidecar and adapter trace |
| GT_VOICE_TIMBRE_LOCK | VOICE | modality-specific | PASS requires sidecar and adapter trace |
| GT_VOICE_ACCENT_LOCK | VOICE | modality-specific | PASS requires sidecar and adapter trace |
| GT_VOICE_PROSODY_NATURALNESS | VOICE | modality-specific | PASS requires sidecar and adapter trace |
| GT_VOICE_SPEAKER_DRIFT | VOICE | modality-specific | PASS requires sidecar and adapter trace |
| GT_SUNO_GENRE_IDENTITY | SUNO | modality-specific | PASS requires sidecar and adapter trace |
| GT_SUNO_VOCAL_AGE | SUNO | modality-specific | PASS requires sidecar and adapter trace |
| GT_SUNO_LYRIC_PERSONALITY | SUNO | modality-specific | PASS requires sidecar and adapter trace |
| GT_SUNO_NEGATIVE_TAGS | SUNO | modality-specific | PASS requires sidecar and adapter trace |
| GT_SUNO_NO_GENERIC_OUTPUT | SUNO | modality-specific | PASS requires sidecar and adapter trace |
| GT_COPILOT_DOCX_HEADINGS | COPILOT_DOCX | modality-specific | PASS requires sidecar and adapter trace |
| GT_COPILOT_DOCX_GROUNDING | COPILOT_DOCX | modality-specific | PASS requires sidecar and adapter trace |
| GT_COPILOT_DOCX_NO_LOSS | COPILOT_DOCX | modality-specific | PASS requires sidecar and adapter trace |
| GT_COPILOT_DOCX_READBACK | COPILOT_DOCX | modality-specific | PASS requires sidecar and adapter trace |
| GT_COPILOT_DOCX_VERSION_ISOLATION | COPILOT_DOCX | modality-specific | PASS requires sidecar and adapter trace |
| GT_SIDECAR_SCHEMA | SIDECAR | modality-specific | PASS requires sidecar and adapter trace |
| GT_SIDECAR_HASH | SIDECAR | modality-specific | PASS requires sidecar and adapter trace |
| GT_SIDECAR_SOURCE_TRACE | SIDECAR | modality-specific | PASS requires sidecar and adapter trace |
| GT_SIDECAR_FIELD_TRACE | SIDECAR | modality-specific | PASS requires sidecar and adapter trace |

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
