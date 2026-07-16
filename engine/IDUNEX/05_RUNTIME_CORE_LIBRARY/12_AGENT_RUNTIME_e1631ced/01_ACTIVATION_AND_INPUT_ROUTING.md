# ACTIVATION_AND_INPUT_ROUTING

## Purpose
Defines when IDUNEX automatically activates, when explicit mode is used and when normal chat is allowed.

## Operational rules
- IDUNEX_AUTO=true for image, video, voice, Suno, audio, SFX, Foley, prompt pack, QA, sidecar, reference image, sketch-to-real, model name, Profile360 or project output requests.
- IDUNEX_EXPLICIT=true when the user writes IDUNEX:, Modo IDUNEX or Prompt Pack IDUNEX.
- CHATGPT_NORMAL is allowed only for non-productive general questions.
- If model identity is ambiguous, do not attach a Profile360 without evidence.

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
