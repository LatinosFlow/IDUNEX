# GOLDEN TEST RESULTS REAL — FORMAL BASELINE EVIDENCE

Scope: PROJECT_FIXTURE_VALIDATION_001 is formal non-production validation evidence. It authorizes MOTOR_BASELINE_10 only. It does not authorize PROJECT_10 or GLOBAL_GO.

| test_id | modality | input | actual/mock payload | comparison | decision | fallback | retest |
|---|---|---|---|---|---|---|---|
| GT_IMAGE_BASELINE_EVIDENCE | image | PROMPTPACK_IMAGE_FINAL.md | OUTPUT_PAYLOAD_IMAGE.json | hash/schema/sidecar | PASS_FOR_MOTOR_BASELINE_10_ONLY | none | not_required |
| GT_VIDEO_BASELINE_EVIDENCE | video | PROMPTPACK_VIDEO_FINAL.md | OUTPUT_PAYLOAD_VIDEO.json | hash/schema/sidecar | PASS_FOR_MOTOR_BASELINE_10_ONLY | none | not_required |
| GT_VOICE_BASELINE_EVIDENCE | voice | VOICE_FINAL_TEST.md | OUTPUT_PAYLOAD_VOICE.json | hash/schema/sidecar | PASS_FOR_MOTOR_BASELINE_10_ONLY | none | not_required |
| GT_SUNO_BASELINE_EVIDENCE | suno | SUNO_FINAL_TEST.md | OUTPUT_PAYLOAD_SUNO.json | hash/schema/sidecar | PASS_FOR_MOTOR_BASELINE_10_ONLY | none | not_required |
| GT_COPILOT_DOCX_BASELINE_EVIDENCE | copilot_docx | COPILOT_DOCX_FINAL_TEST.md | OUTPUT_PAYLOAD_COPILOT_DOCX.json | hash/schema/readback fixture | PASS_FOR_MOTOR_BASELINE_10_ONLY | none | not_required |

GLOBAL_GO remains false.
