# COPILOT_DOCX_GROUNDING_MATRIX

| parameter_id | parameter_name | definition | unit_or_scale | allowed_range | warning_range | fail_range | modalities | source_ids | field_ids | qa_method | fail_code | fallback_fix | example_pass | example_fail | project_test_requirement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DOCX_HEADING_POLICY_001 | docx_heading_policy | measure docx_heading_policy | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_DOCX_HEADING_POLICY | fallback + retest | pass example | fail example | project test required |
| DOCX_CHUNKING_POLICY_002 | docx_chunking_policy | measure docx_chunking_policy | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_DOCX_CHUNKING_POLICY | fallback + retest | pass example | fail example | project test required |
| SOURCE_TRACE_TABLE_003 | source_trace_table | measure source_trace_table | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_SOURCE_TRACE_TABLE | fallback + retest | pass example | fail example | project test required |
| FIELD_TRACE_TABLE_004 | field_trace_table | measure field_trace_table | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_FIELD_TRACE_TABLE | fallback + retest | pass example | fail example | project test required |
| LOCK_TABLE_005 | lock_table | measure lock_table | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_LOCK_TABLE | fallback + retest | pass example | fail example | project test required |
| READBACK_PROTOCOL_006 | readback_protocol | measure readback_protocol | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_READBACK_PROTOCOL | fallback + retest | pass example | fail example | project test required |
| NO_DESTRUCTIVE_SUMMARY_007 | no_destructive_summary | measure no_destructive_summary | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_NO_DESTRUCTIVE_SUMMARY | fallback + retest | pass example | fail example | project test required |
| DOCX_RENDER_GATE_008 | docx_render_gate | measure docx_render_gate | enum/0-100 | declared and traced | vague | missing/contradictory | all relevant | source map | field map | QA method | FAIL_MATRIX_DOCX_RENDER_GATE | fallback + retest | pass example | fail example | project test required |

## HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3 Remediación final QA/Evidencia/Hash


### Parámetros ejecutables HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3
| parameter_id | parameter_name | definition | unit_or_scale | allowed_range | warning_range | fail_range | modalities | qa_method | fail_code | fallback_fix | example_pass | example_fail | project_test_requirement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MATRIX_PARAM_001 | identity_measure_alignment | Alinea campo, fuente y adapter con evidencia | PASS/WARNING/FAIL | PASS | WARNING si falta evidencia mock | FAIL si falta source_id | all | schema+sidecar+hash | FAIL_MATRIX_ALIGNMENT | recargar source/runtime/sidecar | campo trazado y validado | campo sin fuente | smoke evidence required |
| MATRIX_PARAM_002 | modality_specificity | Evita test genérico entre modalidades | 0-100 | >=85 | 70-84 | <70 | image/video/voice/suno/copilot | golden test review | FAIL_GENERIC_TEST | reescribir pasos por modalidad | test con parámetros nativos | pasos genéricos copiados | modality evidence required |
| MATRIX_PARAM_003 | fallback_executability | Fallback quirúrgico y retest | PASS/WARNING/FAIL | PASS | fallback parcial | fallback ausente | all | failcode registry | FAIL_FALLBACK_THIN | agregar prompt_fix/adapter_fix/retest | fallback con retest | fallback genérico | retest required |
| MATRIX_PARAM_004 | hash_evidence | Hash reproducible del input/output | sha256 | 64 hex | hash sin comando | placeholder | sidecar/qa | recalculation | FAIL_HASH_EVIDENCE | regenerar HASH_EVIDENCE | hash recalculable | hash textual falso | hash evidence required |
