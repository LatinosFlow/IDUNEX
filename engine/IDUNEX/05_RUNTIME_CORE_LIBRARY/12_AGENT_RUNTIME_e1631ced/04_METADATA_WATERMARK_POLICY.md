# METADATA_WATERMARK_POLICY

## Purpose
Defines sidecar and metadata fields for portable provenance.

## Operational rules
- sidecar JSON required
- prompt_hash
- output_hash
- lineage_id
- project_id
- model_id
- profile360_fields
- source_cards
- qa_result
- fail_codes
- fallback
- timestamp
- watermark status
- metadata_embedded
- XMP/EXIF recommended when asset format permits

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

# P034 IMAGE DELIVERY / WATERMARK / PHOTOQUALITY BLOCK

Motor: IDUNEX_MOTOR_v1.0.0
Versión semántica: v1.0.0
Etiqueta interna: P034_PROJECT_ENTITY_BRAND_LOGO_IMAGE_DELIVERY_SAFE_APPAREL_CANONICAL_REOPEN
Preserva: LEGACY_NON_AUTHORITY; LEGACY_NON_AUTHORITY
Fecha: NEUTRALIZED_ACTIVE_SCOPE

## IMAGE_REQUEST_ROUTER mandatory
Route colloquial prompts such as `genera`, `crea`, `foto`, `imagen`, `rostro`, `retrato`, `cuerpo completo`, `casual`, `deportivo`, `vestido`, `fondo blanco`, `macro`, `primer plano`, and model-name + scene requests to the image tool.

## Delivery states
- PREVIEW_RENDER: visible platform render, not 10/10 certified.
- IDUNEX_DELIVERY_WITH_SIDECAR: image with sidecar mínimo, hash and QA mínimo.
- OUTPUT_REAL_10_10: asset, sidecar completo, prompt_hash, config_hash, output_hash, QA completo, reviewer, lineage, validators_fail=0 and blocking_warnings=0.

## IDUNEX_DEFAULT_WATERMARK_POLICY = ON
Every IDUNEX image includes exact text `idunex` bottom-center, simple and discreet generic visual system-style, unless the user explicitly says `sin marca idunex`, `sin watermark idunex`, `sin marca de agua idunex`, or `no pongas idunex`. `sin texto` or `sin logos` does not remove the idunex mark.

## Premium photorealism
Every visual prompt must require real adult human-like appearance, natural pores, skin microtexture, realistic asymmetry, physically plausible lighting, contact shadows, real textile physics, correct hands/anatomy and coherent lensing: 85-105mm equivalent for face/macro; 35-50mm equivalent for full body.

## Negative / avoid
No doll-like face, wax skin, porcelain skin, plastic skin, CGI, mannequin, over-smoothed skin, fake symmetry, broken hands, extra fingers, floating subject, wrong lens, text artifacts except exact small lower-center `idunex` watermark.
