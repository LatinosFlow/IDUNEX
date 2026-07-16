# SIDECAR_C2PA_WATERMARK_MATRIX

| parameter_id | parameter_name | definition | unit_or_scale | allowed_range | warning_range | fail_range | modalities | source_ids | field_ids | qa_method | fail_code | fallback_fix | example_pass | example_fail | project_test_requirement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OUTPUT_ID_001 | output_id | measure output_id | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_OUTPUT_ID | fallback + retest | pass example | fail example | project test required |
| PROJECT_ID_002 | project_id | measure project_id | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_PROJECT_ID | fallback + retest | pass example | fail example | project test required |
| MODEL_ID_003 | model_id | measure model_id | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_MODEL_ID | fallback + retest | pass example | fail example | project test required |
| ENGINE_VERSION_004 | engine_version | measure engine_version | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_ENGINE_VERSION | fallback + retest | pass example | fail example | project test required |
| SOURCE_IDS_USED_005 | source_ids_used | measure source_ids_used | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_SOURCE_IDS_USED | fallback + retest | pass example | fail example | project test required |
| FIELD_IDS_USED_006 | field_ids_used | measure field_ids_used | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_FIELD_IDS_USED | fallback + retest | pass example | fail example | project test required |
| ADAPTER_USED_007 | adapter_used | measure adapter_used | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_ADAPTER_USED | fallback + retest | pass example | fail example | project test required |
| VENDOR_PARAMS_008 | vendor_params | measure vendor_params | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_VENDOR_PARAMS | fallback + retest | pass example | fail example | project test required |
| HASH_INPUT_009 | hash_input | measure hash_input | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_HASH_INPUT | fallback + retest | pass example | fail example | project test required |
| HASH_OUTPUT_010 | hash_output | measure hash_output | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_HASH_OUTPUT | fallback + retest | pass example | fail example | project test required |
| PRODUCTION_STATE_011 | production_state | measure production_state | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_PRODUCTION_STATE | fallback + retest | pass example | fail example | project test required |

## HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3 Remediación final QA/Evidencia/Hash


### Parámetros ejecutables HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3
| parameter_id | parameter_name | definition | unit_or_scale | allowed_range | warning_range | fail_range | modalities | qa_method | fail_code | fallback_fix | example_pass | example_fail | project_test_requirement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MATRIX_PARAM_001 | identity_measure_alignment | Alinea campo, fuente y adapter con evidencia | PASS/WARNING/FAIL | PASS | WARNING si falta evidencia mock | FAIL si falta source_id | all | schema+sidecar+hash | FAIL_MATRIX_ALIGNMENT | recargar source/runtime/sidecar | campo trazado y validado | campo sin fuente | smoke evidence required |
| MATRIX_PARAM_002 | modality_specificity | Evita test genérico entre modalidades | 0-100 | >=85 | 70-84 | <70 | image/video/voice/suno/copilot | golden test review | FAIL_GENERIC_TEST | reescribir pasos por modalidad | test con parámetros nativos | pasos genéricos copiados | modality evidence required |
| MATRIX_PARAM_003 | fallback_executability | Fallback quirúrgico y retest | PASS/WARNING/FAIL | PASS | fallback parcial | fallback ausente | all | failcode registry | FAIL_FALLBACK_THIN | agregar prompt_fix/adapter_fix/retest | fallback con retest | fallback genérico | retest required |
| MATRIX_PARAM_004 | hash_evidence | Hash reproducible del input/output | sha256 | 64 hex | hash sin comando | placeholder | sidecar/qa | recalculation | FAIL_HASH_EVIDENCE | regenerar HASH_EVIDENCE | hash recalculable | hash textual falso | hash evidence required |
