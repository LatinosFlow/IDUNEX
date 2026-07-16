# OUTPUT_STATUS_AND_APPROVAL_GATE

## Purpose
Defines output state transitions and blocks false final approval.

## Operational rules
- DRAFT
- QA_PENDING
- QA_FAIL
- QA_PASS_OUTPUT_GO_FALSE
- OUTPUT_GO_TRUE only with QA PASS, sidecar JSON, prompt_hash, output_hash, sidecar_hash and lineage_id

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
