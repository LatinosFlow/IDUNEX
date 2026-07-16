# AGENT_PACK_NOLOSS_COMPILATION_POLICY

## Purpose
Ensures ChatGPT and Copilot packs are canonical no-loss compilations.

## Operational rules
- do not reduce to a summary
- do not lose validators
- do not lose locks
- do not lose source trace
- do not lose QA
- do not lose sidecar
- do not lose fallback
- do not lose modalities
- do not lose Profile360 TechExt

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
