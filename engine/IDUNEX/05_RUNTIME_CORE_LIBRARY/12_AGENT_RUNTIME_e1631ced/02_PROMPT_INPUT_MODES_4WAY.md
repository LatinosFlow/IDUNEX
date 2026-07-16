# PROMPT_INPUT_MODES_4WAY

## Purpose
Defines four core prompt/image input routes and expanded multimodal routes.

## Operational rules
- IMAGE_FROM_TECH_PROMPT
- IMAGE_FROM_COLLOQUIAL_IDEA
- PROMPT_FROM_REFERENCE_IMAGE
- PROMPT_FROM_COLLOQUIAL_IDEA
- VIDEO_FROM_IDEA
- VIDEO_FROM_REFERENCE
- VOICE_FROM_MODEL_PROFILE
- ELEVENLABS_DIRECTION
- SUNO_FROM_MODEL_POV
- AUDIO_SFX_FOLEY_SCENE
- MODEL_DIALOGUE_TEXT
- MODEL_DIALOGUE_AUDIO_DIRECTION
- IDUNEX_SCENE_ONLY
- IDUNEX_FULL_MODEL

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
