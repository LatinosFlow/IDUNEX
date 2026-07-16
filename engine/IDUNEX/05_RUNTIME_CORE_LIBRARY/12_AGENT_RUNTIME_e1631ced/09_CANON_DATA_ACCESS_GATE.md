# CANON_DATA_ACCESS_GATE

## Purpose
Gate that checks data access before any output.

## Operational rules
- Project Core
- Profile360
- TechExt
- Scene Physics
- Prompt Contracts
- QA
- Sidecars
- Vendor Guide
- Locks
- Manifest
- if access fails -> DRAFT_NO_CANON_ACCESS or NO_DELIVERY

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
