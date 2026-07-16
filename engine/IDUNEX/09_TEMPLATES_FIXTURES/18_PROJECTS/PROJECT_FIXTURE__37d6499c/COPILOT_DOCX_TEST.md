# COPILOT_DOCX_TEST — grounding/readback smoke fixture

## DOCX authority hierarchy
1. Control Center. 2. Motor Core. 3. Profile360 Registry. 4. Source-to-Runtime Map. 5. Schemas. 6. QA Gauntlet. 7. Smoke Test Evidence. 8. Sidecar.

## H1-H4 structure
H1: Engine State. H2: Locks. H2: Source Trace. H2: Field Trace. H2: Adapter Trace. H2: QA Gates. H2: Sidecar and Hash Evidence. H2: GO/NO-GO.

## Source trace table
Columns: source_id, source_id_canonical, runtime_domain, field_count_impacted, primary_source_fields_count, adapter_targets, coverage_score, evidence_status.

## Field trace table
Columns: field_id, field_name, runtime_domain, primary_source_id, adapter_domain, qa_rule_id, fail_code, golden_test_id, fallback_fix.

## Lock table
JSON_LOCK, ANCHOR_LOCK, AGE_LOCK, ID_LOCK, NO_GLOBAL_GO_LOCK, NO_LOSS_LOCK.

## Canon priority order
Never infer beyond loaded files. Prefer JSON registry and maps over prose. If JSON and prose conflict, use JSON and mark review.

## Chunking strategy
Chunk by authority: 8k-12k characters per chunk, source table repeated at chunk boundaries, no destructive summary, no removing locks.

## Readback prompt
Before answering, return: engine_version, production_state, active_project_id, active_locks, source_ids_loaded, field_ids_loaded, adapter_targets_loaded, QA gates loaded, sidecar requirement, known gaps, GO/NO_GO state.

## Expected Copilot readback
engine_version={ENGINE_VERSION}; production_state={STATE}; active_project_id=IDUNEX_PROJECT_CANONICAL_SMOKE_TEST_v1.0.0; GO/NO_GO={STATE}; prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE.

## Actual/mock Copilot readback
Formal mock readback recorded in QA_RESULT evidence_bundle. Real Copilot execution required before PROJECT_GO.

## Failure examples
Missing locks, summary removing field trace, source_ids absent, hallucinated model identity, no sidecar, no hash evidence.

## Fallback fixes
Reload authority chunks, force readback, split DOCX by section, repeat lock table, require source_id/field_id citations, block GLOBAL_GO.

## Render validation checklist
DOCX must render without blank critical pages, broken tables or hidden lock tables. Render gate status: PASS for current package audit.
