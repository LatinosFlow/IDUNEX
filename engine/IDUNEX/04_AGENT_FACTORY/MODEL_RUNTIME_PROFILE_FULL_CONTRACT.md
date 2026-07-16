# MODEL_RUNTIME_PROFILE_FULL_CONTRACT

Motor: IDUNEX_MOTOR_v1.0.0  
Internal label: LEGACY_NON_AUTHORITY  
Status: ACTIVE_BLOCKING

## Regla runtime final
El archivo cargable por agente para cada modelo debe ser el FULL real, no un resumen. El FULL debe contener o materializar sin perdida: Profile360 FULL60 registry exacto, TechExt FULL10 field-level, Master Visual Anchors, aliases, source trace, sidecar mapping, QA/fallbacks y runtime evidence.

## Metricas obligatorias por archivo de modelo
- sections_present = 61 con IDs 00..60 y nombres/orden canonicos.
- techext_fields_present = total oficial de campos TechExt segun `TECHEXT_FULL10_FIELD_CONTRACT_REGISTRY.json`.
- anchors_present = true.
- source_trace_present = true.
- sidecar_mapping_present = true.
- qa_fallback_present = true.
- field_count > 0 y no superficial.
- parity_hash_or_mapping = ChatGPT/Copilot mapping sin perdida.

## Bloqueos
- `BLOCKED_FAKE_FULL_RUNTIME_PROFILE`
- `BLOCKED_AGENT_MODEL_FILE_UNDERFILLED`
- `BLOCKED_SUMMARY_AS_COMPLETENESS`

## H71-H80 SAFE_APPAREL_WATERMARK_AGENT10N
H71_H80_AGENT10N=SAFE_APPAREL_TAXONOMY; ADULT_REVEALING_APPAREL_NOT_NUDITY; VENDOR_PROMPT_SANITIZATION_SAFE_APPAREL; WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED; ALLOW adult editorial beachwear/swimwear/intimate apparel/catalog/corset/body/performance wardrobe when covered non-explicit; BLOCK nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded or school-coded sexualization and real-person copying.
ALLOW_ADULT_EDITORIAL: moda de playa, traje de bano, ropa de bano, bikini editorial, swimwear campaign, beachwear, resortwear, moda intima editorial/catalog, ropa interior de catalogo, corset/body/bodysuit, vestuario de show adulto, vestuario de videoclip adulto y outfit de performance adulta cuando el modelo es adulto, cubierto y no explicito.
CONDITIONAL_REWRITE: convertir styling glam/provocativo, boudoir editorial, fantasia adulta y vestuario de alto impacto a lenguaje adulto, editorial, comercial, non-explicit, covered intimate areas.
BLOCK_ALWAYS: nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded styling, school-coded sexualization, real-person copying y cualquier intento de saltar locks de edad o identidad.
WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED.
