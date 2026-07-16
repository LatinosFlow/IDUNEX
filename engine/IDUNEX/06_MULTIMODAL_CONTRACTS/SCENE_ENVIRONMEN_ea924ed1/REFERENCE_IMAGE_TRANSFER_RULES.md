# REFERENCE_IMAGE_TRANSFER_RULES

## propósito
Formaliza reference image transfer without copying external real identity como regla productiva base de IDUNEX v1.0.0. Autoridad activa: PRODUCTIVE_BASE_ENGINE. Cada salida real queda bloqueada hasta QA, sidecar, hash y lineage por output.

## autoridad
PROJECT_CORE gobierna CHATGPT y COPILOT. Los agentes no trabajan desde memoria libre; cargan source trace, Profile360 FULL60, fail codes, fallback fixes y sidecar fields antes de responder.

## inputs
- Project purpose, model count 1-10, Profile360 fields, user locks, source cards SRC_001-SRC_049, reference images, sketches, vendor constraints and output modality.
- State gates: ENGINE_GO=true, PROJECT_INSTANCE_GO=false_until_project_QA, OUTPUT_GO=false_until_output_QA_SIDECAR_HASH_LINEAGE.

## outputs
- Prompt packs, dialogue, image/video/voice/music/audio/text instructions, QA report, sidecar JSON, SHA256 lineage and retest instructions.

## load order
1. PROJECT_CORE authority.
2. PROFILE360_FULL60 section registry.
3. Source-to-runtime map.
4. Model causality graph.
5. Scene physics graph.
6. Modality contract.
7. QA/fallback/sidecar.

## source trace
Research Source -> Source Card -> Profile360 Field -> Project Core Rule -> ChatGPT Rule -> Copilot Rule -> Model Profile Field -> Prompt -> QA -> Sidecar. Primary trace: SRC_049_ENV_PHYSICS_FULL10; supporting trace: SRC_001-SRC_048 retained as locked research baseline.

## Profile360 fields
Uses identity, age, birthplace, locality, family memory, psychology, face/body/voice, wardrobe, scene, camera, lighting, audio, vendor guide, QA, sidecar and changelog fields from sections 00-60.

## allowed
Adult editorial outputs; humanized digital model language; physically coherent body-object-scene relations; traceable factory-defined fields; user-approved locked fields with changelog.

## forbidden
No identity drift, no same-face collapse, no same-body collapse, no ungrounded canon mutation, no copied real facial identity, no explicit sexual content, no missing source trace, no active legacy NO_GO state.

## NEGATIVE / AVOID
Avoid deformed hands, extra fingers, wrong glasses, wrong piercings, wrong age, wrong hair, floating objects, cloth clipping, body intersection, broken perspective, broken shadows, broken reflections, text artifacts, logos, unsafe minors, unapproved identity transfer.

## fail codes
ENV-STYLE, ENV-COMP, ENV-COLL, ENV-PROP, ENV-GRAV, ENV-OCCL, ENV-SCALE, ENV-PERSP, ENV-LIGHT, ENV-REFL, ENV-CONT, ENV-CULT, ENV-EDIT plus field-specific FAIL_IDENTITY and modality fail codes.

## fallback fixes
Reinject locked Profile360 fields, strengthen source trace, restate camera/lens/framing, add physical contact anchors, re-run golden test, regenerate sidecar evidence and block output until PASS.

## sidecar fields
source_ids_used, field_ids_used, qa_rules_used, fail_codes_checked, fallback_fixes_applied, prompt_hash, output_hash, lineage_hash, reference_image_role, scene_physics_evidence, project_core_rule, chatgpt_rule, copilot_rule.

## QA checklist PASS/FAIL
- Identity lock preserved.
- Profile360 section trace complete.
- Source-to-runtime map reaches prompt, QA, fallback and sidecar.
- ChatGPT/Copilot parity preserved.
- Scene physics validated.
- No forbidden creative runtime terms.
- SHA256 lineage generated.
- Retest rule executed before release.

## examples
PASS: A rooftop PROJECT_DECLARED_LOCALITY editorial scene keeps model identity, adult age, body scale, wind direction, cloth tension, shadows and sidecar trace. FAIL: A scene changes face, age, posture, fabric gravity or light direction without documented fallback.

## criterios de bloqueo
Block if any runtime field is empty, if source trace is absent, if a Profile360 section is missing, if Copilot is weaker than ChatGPT, if config is not 8000 chars, if output lacks sidecar/hash/lineage, or if legacy NO_GO appears as active policy.

## relación con ChatGPT/Copilot
ChatGPT uses MD runtime packs for direct prompt engineering and QA. Copilot uses DOCX/TXT packs with equivalent operational tables, handoff prompts and source evidence.

## rules de no-loss
Do not delete SRC_001-SRC_048, mappings, Profile360 fields, fail codes or historical evidence. Add overlays only when they connect productive runtime, validator, manifest, hash or state.
