# OUTPUT_ASSET_PROVENANCE_POLICY

## Purpose
Defines evidence fields for all assets.

## Operational rules
- project_id
- engine_parent_sha
- model_id
- output_id
- output_type
- prompt_id
- prompt_hash
- output_hash
- vendor
- timestamp
- qa_result
- sidecar_hash
- lineage_parent
- watermark status
- metadata status

## Required evidence
- files_checked
- rules_checked
- expected_value
- actual_value
- result
- timestamp

## Runtime connection
This policy must be referenced by Project Factory, Agent Factory, ChatGPT config, Copilot config, prompt packs, QA, sidecar and release validator.

## Fail codes
- RUNTIME-SOURCE-MISSING
- SUMMARY-LOSS
- CANON-INVENTED
- OUTPUT-GATE-BYPASS
- WATERMARK-POLICY-MISSING
- VENDOR-HANDOFF-INCOMPLETE

## Fallback fixes
- Re-load required files.
- Convert destructive summary into canonical compilation.
- Mark new values as FACTORY_DEFINED_PROPOSED.
- Return output status to DRAFT or QA_PENDING.
- Generate missing sidecar/hash/lineage evidence.
