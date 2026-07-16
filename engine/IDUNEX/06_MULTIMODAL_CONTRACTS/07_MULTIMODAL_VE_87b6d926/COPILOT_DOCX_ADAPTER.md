# COPILOT DOCX ADAPTER — contrato operativo completo

## INPUT CONTRACT
El adapter `copilot_docx_adapter` recibe únicamente campos Perfil360 con `adapter_targets` que incluyan `copilot_docx_adapter`, source_ids reales, locks activos, estado permitido y sidecar_trace=true. No acepta campos sin runtime_domain granular ni campos derivados no justificados.

## OUTPUT CONTRACT
El output debe producir una especificación usable por el canal Copilot DOCX, con secciones verificables, source trace, field trace, QA before output, fail codes, fallbacks y sidecar requirements. Ningún resultado puede omitir `adapter_used`, `source_ids_used`, `field_ids_used` ni producción state.

## REQUIRED PROFILE360 FIELDS
Debe cargar campos de identidad, edad adulta, realismo humano, continuidad, legal/governance y todos los campos específicos del adapter. Para Copilot DOCX, las secciones obligatorias son: docx_heading_policy, docx_chunking_policy, large_canon_grounding, source_trace_table, lock_table, readback_protocol, no_destructive_summary, notebook_load_order, docx_render_gate, copilot_response_gate, claim_to_runtime_verification.

## REQUIRED SOURCE IDS
Debe usar fuentes primarias y secundarias pertinentes. Para voz/música/Copilot se exige multi-source; para imagen/video se exige fuente visual, movimiento, cámara/luz, QA y sidecar. SRC_029/SRC_048 son obligatorias en Copilot/DOCX; SRC_022/SRC_043 en voz; SRC_023/SRC_036/SRC_044 en Suno.

## REQUIRED LOCKS
JSON_LOCK, ANCHOR_LOCK, AGE_LOCK, ID_LOCK cuando el proyecto declare identidad. En motor base se conserva la regla, pero no se activa ningún modelo concreto. Si falta lock crítico: NO_GO.

## PARAMETER TABLE
Parámetros mínimos: heading_level, chunk_size, authority_order, readback_fields, render_validation, source_trace_table, no_loss_export. Cada parámetro debe tener valor declarado, rango permitido, rango prohibido, método QA, fail_code y fallback.

## NEGATIVE / AVOID
Evitar drift de identidad, edad, cuerpo, voz, cultura, rostro genérico, same-face/same-body, placeholders finales, logos no autorizados, texto accidental, outputs sin sidecar, celebridad real o inferencia no sustentada.

## MODALITY-SPECIFIC QC
QC específico: validar contrato de entrada, campos requeridos, parámetros, locks, coherencia semántica, adapter_domain, golden_test_id y sidecar. Si el output es imagen/video/voz/música/documento, usar golden tests propios de modalidad, no tests genéricos.

## FAIL CODES
Todo fallo dispara FAIL_CODE_REGISTRY.json. El adapter debe mapear síntoma → root_cause → prompt_fix → parameter_fix → adapter_fix → qa_retest → production_decision.

## SURGICAL FALLBACKS
No se permite fallback genérico. La reparación debe indicar campo exacto, fuente exacta, parámetro exacto, adapter exacto y retest. Si no existe evidencia, registrar gap y bloquear entrega.

## SIDECAR REQUIREMENTS
El sidecar debe incluir output_id, project_id, model_id si aplica, engine_version, source_ids_used, field_ids_used, adapter_used=copilot_docx_adapter, vendor_params, locks_active, qa_status, fail_codes, fallbacks_applied, hash_input, hash_output y production_state.

## GOLDEN TESTS
Debe invocar golden tests específicos del canal y registrar resultado. Un golden test copiable sin cambios a otra modalidad queda inválido por FAIL_BLOCKER_GENERIC_GOLDEN_TEST.

## EXAMPLE PROMPT STRUCTURE
La estructura debe incluir bloque de autoridad, contexto, parámetros, negative/avoid, QA checklist, fallback fixes y sidecar. No se debe incluir nombre de modelo o proyecto dentro del motor base.

## REJECTION CONDITIONS
Rechazar si falta source_id, field_id, adapter target, QA, sidecar, lock crítico, golden test específico, o si aparece GLOBAL_GO desde motor.

## PROJECT TEST REQUIREMENT
Este adapter queda listo para `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`; solo un proyecto o smoke test puede subir a proyecto GO tras golden tests completos.

## HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3 Remediación final QA/Evidencia/Hash

### Copilot/DOCX-specific parameters
docx_heading_policy, H1_H4_contract, large_canon_chunking, source_trace_table, field_trace_table, lock_table, readback_protocol, no_destructive_summary, notebook_load_order, section_authority_map, docx_render_gate, copilot_response_gate, claim_to_runtime_verification.


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
