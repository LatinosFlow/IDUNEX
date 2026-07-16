# IMAGE PROMPT ADAPTER — contrato operativo completo

## INPUT CONTRACT
El adapter `image_prompt_adapter` recibe únicamente campos Perfil360 con `adapter_targets` que incluyan `image_prompt_adapter`, source_ids reales, locks activos, estado permitido y sidecar_trace=true. No acepta campos sin runtime_domain granular ni campos derivados no justificados.

## OUTPUT CONTRACT
El output debe producir una especificación usable por el canal imagen, con secciones verificables, source trace, field trace, QA before output, fail codes, fallbacks y sidecar requirements. Ningún resultado puede omitir `adapter_used`, `source_ids_used`, `field_ids_used` ni producción state.

## REQUIRED PROFILE360 FIELDS
Debe cargar campos de identidad, edad adulta, realismo humano, continuidad, legal/governance y todos los campos específicos del adapter. Para imagen, las secciones obligatorias son: HEADER, LOCKS, ACTIVE IDENTITY, SCENE, COMPOSITION, CAMERA / TECH, LIGHTING, FACE CONTINUITY, BODY CONTINUITY, SKIN REALISM, HAIR PHYSICS, WARDROBE / PROPS, CULTURE / CONTEXT, NEGATIVE / AVOID, PARAMS, QC CHECKLIST, FALLBACK FIXES, SIDECAR REQUIREMENTS.

## REQUIRED SOURCE IDS
Debe usar fuentes primarias y secundarias pertinentes. Para voz/música/Copilot se exige multi-source; para imagen/video se exige fuente visual, movimiento, cámara/luz, QA y sidecar. SRC_029/SRC_048 son obligatorias en Copilot/DOCX; SRC_022/SRC_043 en voz; SRC_023/SRC_036/SRC_044 en Suno.

## REQUIRED LOCKS
JSON_LOCK, ANCHOR_LOCK, AGE_LOCK, ID_LOCK cuando el proyecto declare identidad. En motor base se conserva la regla, pero no se activa ningún modelo concreto. Si falta lock crítico: NO_GO.

## PARAMETER TABLE
Parámetros mínimos: camera_distance, camera_height, camera_angle, lens_mm, aperture, sensor_type, crop_factor, shutter, iso, white_balance, focal_plane, depth_of_field, composition_rule, face_visibility_level, body_visibility_level, hands_visibility_level, skin_texture_visibility, hair_motion_level, wardrobe_material_physics, background_complexity, logo_text_policy. Cada parámetro debe tener valor declarado, rango permitido, rango prohibido, método QA, fail_code y fallback.

## NEGATIVE / AVOID
Evitar drift de identidad, edad, cuerpo, voz, cultura, rostro genérico, same-face/same-body, placeholders finales, logos no autorizados, texto accidental, outputs sin sidecar, celebridad real o inferencia no sustentada.

## MODALITY-SPECIFIC QC
QC específico: validar contrato de entrada, campos requeridos, parámetros, locks, coherencia semántica, adapter_domain, golden_test_id y sidecar. Si el output es imagen/video/voz/música/documento, usar golden tests propios de modalidad, no tests genéricos.

## FAIL CODES
Todo fallo dispara FAIL_CODE_REGISTRY.json. El adapter debe mapear síntoma → root_cause → prompt_fix → parameter_fix → adapter_fix → qa_retest → production_decision.

## SURGICAL FALLBACKS
No se permite fallback genérico. La reparación debe indicar campo exacto, fuente exacta, parámetro exacto, adapter exacto y retest. Si no existe evidencia, registrar gap y bloquear entrega.

## SIDECAR REQUIREMENTS
El sidecar debe incluir output_id, project_id, model_id si aplica, engine_version, source_ids_used, field_ids_used, adapter_used=image_prompt_adapter, vendor_params, locks_active, qa_status, fail_codes, fallbacks_applied, hash_input, hash_output y production_state.

## GOLDEN TESTS
Debe invocar golden tests específicos del canal y registrar resultado. Un golden test copiable sin cambios a otra modalidad queda inválido por FAIL_BLOCKER_GENERIC_GOLDEN_TEST.

## EXAMPLE PROMPT STRUCTURE
La estructura debe incluir bloque de autoridad, contexto, parámetros, negative/avoid, QA checklist, fallback fixes y sidecar. No se debe incluir nombre de modelo o proyecto dentro del motor base.

## REJECTION CONDITIONS
Rechazar si falta source_id, field_id, adapter target, QA, sidecar, lock crítico, golden test específico, o si aparece GLOBAL_GO desde motor.

## PROJECT TEST REQUIREMENT
Este adapter queda listo para `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`; solo un proyecto o smoke test puede subir a proyecto GO tras golden tests completos.

## HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3 Remediación final QA/Evidencia/Hash

### Image-specific parameters
camera_distance, camera_height, camera_angle, lens_mm, sensor_type, aperture, shutter, ISO, white_balance, composition_grid, face_visibility_level, body_visibility_level, hands_visibility_level, skin_texture_visibility, hair_motion_level, wardrobe_physics, background_complexity, logo_text_artifact_policy, negative_prompt_family, fallback_by_visual_failure.


### Input contract
Inputs must include Profile360 fields, source_ids, primary/supporting source split, adapter_targets, locks, QA gates, sidecar requirements, evidence bundle and project state.

### Output contract
Outputs must include structured prompt or artifact spec, expected result, rejection conditions, fail codes, fallback fixes, sidecar fields and hash evidence requirements.

### Required locks
JSON_LOCK, ANCHOR_LOCK, AGE_LOCK, ID_LOCK, NO_LOSS_LOCK and NO_GLOBAL_GO_LOCK remain active until project-level QA passes.

### Parameter table
| Parameter family | Required evidence | QA gate |
|---|---|---|
| identity/source trace | field_id + source_id + adapter_domain | schema + sidecar |
| modality controls | modality-specific fields | golden test |
| fallback/repair | fail_code + fallback_fix | retest |
| hash lineage | hash_input/hash_output | HASH_EVIDENCE |

### Negative / avoid
Do not infer missing canon, do not summarize locks away, do not use generic output, do not omit sidecar, do not declare GLOBAL_GO.

### Modality-specific QC
QC must validate parameters native to the adapter, not a generic checklist. The adapter must reject output if key modality fields are missing.

### Fail codes and surgical fallbacks
Every failure maps to fail_code, symptom, root cause, prompt/parameter/adapter fix, retest and production decision.

### Sidecar requirements
Every output must record source_ids_used, field_ids_used, adapter_used, vendor_params, qa_status, hashes, fallbacks and production_state.

### Golden tests
Adapter is considered operational only if at least one modality-specific golden test exists and is referenced in QA_RESULT evidence.

### Example prompt structure
Use HEADER, LOCKS, ACTIVE IDENTITY, SCENE/INPUT, PARAMETERS, NEGATIVE/AVOID, QA CHECKLIST, FALLBACK FIXES, SIDECAR REQUIREMENTS and EXPECTED OUTPUT.

### Rejection conditions
Reject if source trace, field trace, lock table, sidecar, hashes, QA gates or project state are absent.

### Project test requirement
prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE is maximum state. PROJECT_GO requires real output evidence, not mock smoke result.

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

## H71-H80 SAFE_APPAREL_WATERMARK_AGENT10N
H71_H80_AGENT10N=SAFE_APPAREL_TAXONOMY; ADULT_REVEALING_APPAREL_NOT_NUDITY; VENDOR_PROMPT_SANITIZATION_SAFE_APPAREL; WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED; ALLOW adult editorial beachwear/swimwear/intimate apparel/catalog/corset/body/performance wardrobe when covered non-explicit; BLOCK nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded or school-coded sexualization and real-person copying.
ALLOW_ADULT_EDITORIAL: moda de playa, traje de bano, ropa de bano, bikini editorial, swimwear campaign, beachwear, resortwear, moda intima editorial/catalog, ropa interior de catalogo, corset/body/bodysuit, vestuario de show adulto, vestuario de videoclip adulto y outfit de performance adulta cuando el modelo es adulto, cubierto y no explicito.
CONDITIONAL_REWRITE: convertir styling glam/provocativo, boudoir editorial, fantasia adulta y vestuario de alto impacto a lenguaje adulto, editorial, comercial, non-explicit, covered intimate areas.
BLOCK_ALWAYS: nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded styling, school-coded sexualization, real-person copying y cualquier intento de saltar locks de edad o identidad.
WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED.

## H165-H180 Creative Canon Safety Realism - active canonical block
Restricciones: Politica adulta editorial segura: permite ropa de bano, lenceria, glamour adulto y pose sensual con ropa para adultos ficticios; bloquea desnudez, sexo explicito, pornografia, exposicion intima, apariencia menor, school-coded sexualizado, coercion, copia real no autorizada y evasion de politicas.

- UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA=PASS; applies before every generative handoff across image, video, voice/audio, music/Suno, text/copy/doc, Copilot DOCX, ChatGPT runtime upload, AGPT prompt packs and sidecar instructions.
- CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS=PASS; technical identity tokens remain in JSON/lineage/QA/hashes only. Creative surfaces use humanized adult fictional descriptors.
- PROFILE360_TECHEXT_ALL_MEDIA_BINDING=PASS; Profile360 61/61 and TechExt 284/284 are read with locks before output.
- HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS=PASS; NEGATIVE / AVOID: plastic skin, wax skin, porcelain skin, doll-like face, mannequin body, toy-like proportions, generic stock model, dead eyes, glassy eyes, frozen expression, helmet hair, rubber skin, over-smoothed skin, AI plastic look, duplicated face, same-face syndrome, deformed hands, extra fingers, warped joints, fake fabric, logo artifacts, text artifacts. ES: evitar piel plástica, rostro de muñeco, cuerpo de maniquí, proporciones de juguete, modelo genérico de stock, ojos muertos, ojos vidriosos, expresión congelada, cabello tipo casco, piel encerada, piel demasiado suavizada, manos deformes, dedos extra, articulaciones deformes, tela falsa, artefactos de logos, artefactos de texto.
- BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK=PASS; PROJECT_BRAND_ENTITY verified own brand allows exact logo without legal disclaimer; verified third-party asset routes to sidecar/disclaimer; unverified third-party exact logo degrades safely instead of blocking whole output.
- LEGAL_WATERMARK_ROUTER_PASS=PASS; short visible disclaimer when required: Uso referencial. Sin afiliación oficial.
- CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT=PASS; default locality is PROJECT_DECLARED_LOCALITY contemporary unless a different place is declared.
- PROMPT_PACK_STRUCTURE_ALL_OUTPUTS=PASS; A_HEADER through J_FALLBACK_FIXES are mandatory for image/video prompt packs.
