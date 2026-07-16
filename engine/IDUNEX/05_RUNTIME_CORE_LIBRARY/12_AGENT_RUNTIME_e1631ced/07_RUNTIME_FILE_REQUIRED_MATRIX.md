# RUNTIME_FILE_REQUIRED_MATRIX

## Purpose
Defines minimum file load order per modality.

## Operational rules
- image with model: Project Core, Profile360, TechExt, Master Anchors, Scene Physics, Prompt Input Modes, Watermark, QA, Sidecar
- image without model: Project Core, Scene Physics, Prompt Input Modes, Watermark, QA, Sidecar
- voice: Profile360, Voice360, Dialogue Persona, vendor checklist, sidecar
- Suno: Profile360, Suno POV, Voice360, songwriting, sidecar
- video: Profile360, Motion360, Camera360, Lighting360, Scene Physics, continuity, sidecar

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

## P0 runtime file clarification

Each ChatGPT/Copilot agent uses 10 mandatory project core files plus 1 MODEL_RUNTIME_PROFILE_FULL per model. Maximum operational runtime files: 20. Maximum models per project/agent: 10. 11+ models must block with BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT. Do not split agents for the same project and do not use destructive summaries as completeness substitutes. Config, manifest, evidence and output media do not count as principal runtime knowledge unless explicitly defined.

MODEL_RUNTIME_PROFILE_FULL must contain Profile360 FULL60, TechExt FULL10, Master Visual Anchors, aliases, source trace, sidecar mapping, QA/fallbacks and runtime evidence. Final delivery must contain no null, blanks, placeholders, and no FACTORY_DEFINED_PROPOSED pendiente en entrega final.
