# COPILOT DOCX FINAL TEST — PROJECT_FIXTURE_VALIDATION_001

## DOCX AUTHORITY HIERARCHY
H1 engine state, H2 project manifest, H2 locks, H2 source trace, H2 field trace, H2 QA, H2 sidecar, H2 hash evidence. H3 modality fixtures. H4 fallback/retest.

## SOURCE TRACE TABLE
Columns: source_id, source_id_canonical, section, field_ids, adapter_domain, QA rule, fallback, evidence hash.

## FIELD TRACE TABLE
Columns: field_id, field_name, runtime_domain, primary_source_id, supporting_source_ids, adapter_targets, golden_test_id, fail_code.

## LOCK TABLE
JSON_LOCK, ANCHOR_LOCK, AGE_LOCK, ID_LOCK; no destructive summary; no legacy version mixing; no project/model injection inside motor.

## CHUNKING STRATEGY
Large canon chunks by authority: control center, Profile360, source runtime, adapters, QA, project factory, sidecar, manifests. Each chunk carries source and field trace.

## READBACK PROMPT
Before answering, Copilot must report engine_version, production_state, active_project_id, locks loaded, source_ids loaded, field_ids loaded, adapter_targets loaded, QA gates loaded, sidecar requirement, known gaps, GO/NO_GO.

## EXPECTED READBACK
prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE, global_go=false, project fixture only, no production authorization.

## FAILURE EXAMPLES
Missing H1-H4, summarized locks, hidden source trace, destructive summary, inferred source not loaded, GLOBAL_GO claim.

## FALLBACK FIXES
Move locks to front, split DOCX by authority, add source trace table, rerun readback, block output if readback omits GO/NO_GO.

## REQUIRED FIELD IDS
P360_EXPORT_0406, P360_EXPORT_0446, P360_QA_0409, P360_SIDECAR_0414

## REQUIRED ADAPTER
copilot_docx_adapter

## GOLDEN TEST
GT_COPILOT_DOCX_READBACK
