## Phase 3 file-level inheritance
inherits = AGENT_FACTORY_GLOBAL_RULES#COMMON_AGENT_RUNTIME_QA_BLOCK
inherits_mandatory_fields = AGENT_FACTORY_GLOBAL_RULES#COMMON_MANDATORY_FIELDS
agent_specific_delta_required = true

# COPILOT DOCX RUNTIME STANDARD

## Authority hierarchy
Copilot debe leer primero estado de motor, control center, locks, source inventory, Profile360 registry, source-to-runtime map, adapters, QA, sidecar y manifest. La jerarquía H1-H4 es obligatoria para impedir que el canon crítico quede enterrado.

## H1-H4 standard
H1 = unidad de autoridad; H2 = sección operativa; H3 = tabla o matriz; H4 = reglas/fallbacks. Todo DOCX debe incluir portada técnica, resumen ejecutivo, producción state, lock table, canon crítico, Profile360 fields, source mapping, multimodal rules, QA/golden tests, fallback fixes, sidecar, changelog y audit.

## Large canon chunking
El canon grande se divide por autoridad: motor core, project factory, agent factory, Profile360, source-to-runtime, adapters, QA, sidecar, policies, documentation. Cada chunk debe repetir engine_version, state, source scope y no-loss rule.

## Source and field trace
Toda sección DOCX debe tener matriz source_id → field_id → adapter → QA → fallback. Copilot no puede responder si no puede hacer readback de esa matriz.

## No destructive summary
Copilot puede resumir para orientar, pero no puede eliminar locks, source_ids, fail codes, fallback fixes, sidecar requirements o production state. Si un resumen omite esos elementos, se dispara FAIL_BLOCKER_COPILOT_DOCX_TOO_THIN.

## Render validation
Cada DOCX operativo debe abrir, renderizar y permitir extracción de texto. Si falla render o clipping visual, la entrega queda en NO_GO.

## Readback QA
Antes de operar, Copilot debe devolver engine_version, production_state, active_project_id si existe, active_locks, source_ids_loaded, field_ids_loaded, adapter_targets_loaded, QA gates, sidecar requirement, known gaps y GO/NO_GO.

## Project package handoff
El DOCX no otorga GLOBAL_GO. Solo prepara el motor para prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE y exige prueba de proyecto.


## Archivo específico
Ruta operativa: `04_AGENT_FACTORY/02_COPILOT_DOCX_AGENT_LOAD/COPILOT_DOCX_RUNTIME_STANDARD.md`. Esta ruta mantiene autoridad documental y prueba no-loss DOCX export.


## Operational depth extension
Este estándar obliga a Copilot a operar como lector de canon grande, no como resumidor libre. Para cada documento debe construir una tabla de autoridad con: sección, propósito, source_ids, field_ids, adapter_targets, QA, fail_code, fallback y estado. Si una sección contiene locks o reglas de identidad, Copilot debe repetirlas en la respuesta de readback antes de cualquier transformación. La estrategia de chunking se basa en autoridad, no en longitud: primero motor/control, luego Profile360, luego source-to-runtime, luego adapters, luego QA, luego sidecar, luego documentación. Si el contexto excede límite, se divide por autoridad y se preservan las relaciones source_id → field_id → adapter → QA. 

El protocolo anti-hallucination bloquea inferencias no presentes; todo dato no cargado se marca como gap. El protocolo anti-destructive-summary prohíbe resumir eliminando locks, sidecar, fail codes, source trace, schema rules o estado GO/NO-GO. El no-loss DOCX export test exige abrir/renderizar el DOCX, extraer texto, validar headings H1-H4, comprobar tablas de locks y confirmar que SRC_029 y SRC_048 están referenciadas en grounding, chunking, readback y claim verification. Si Copilot no puede citar sección interna, debe devolver REVIEW_REQUIRED.

## HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3 Remediación final QA/Evidencia/Hash


### Grounding evidence HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.3
- DOCX authority hierarchy: Control Center → Motor Core → Profile360 → Source-to-Runtime → Schemas → QA → Smoke Evidence → Sidecar.
- H1-H4 standard: every section must expose title, authority, source trace and QA gate.
- Source trace table: source_id, canonical id, runtime domains, fields impacted, primary/support counts, score and evidence.
- Field trace table: field_id, field_name, runtime_domain, adapter_domain, qa_rule_id, fail_code, fallback.
- Lock table: JSON_LOCK, ANCHOR_LOCK, AGE_LOCK, ID_LOCK, NO_LOSS_LOCK, NO_GLOBAL_GO_LOCK.
- Chunking strategy: split by authority, repeat locks at chunk boundary, no destructive summary.
- Readback protocol: engine_version, production_state, active_project_id, active_locks, source_ids_loaded, field_ids_loaded, adapter_targets_loaded, QA gates loaded, sidecar requirement, known gaps, GO/NO_GO state.
- Render gate: DOCX must be rendered; layout issues block Copilot-ready claim.
- Hallucination blocker: Copilot must not infer fields, projects, people, models or GLOBAL_GO absent from loaded package.


## Phase 3 agent inheritance

## LEGACY_NON_AUTHORITY - ACTIVE_BLOCKING
Engine: IDUNEX_MOTOR_v1.0.0. Internal label: LEGACY_NON_AUTHORITY; not a semantic version. This block is embedded inside the runtime core file loaded by ChatGPT/Copilot and is not a documentary-only external reference.

Closed runtime policy: one ChatGPT agent per project and one Copilot agent per project; max 20 files per agent; max 10 models per project/agent; runtime formula = 10 core IDUNEX + 1 MODEL_RUNTIME_PROFILE_FULL per model; 1 model = 11 files; 2 models = 12 files; 5 models = 15 files; 10 models = 20 files; 11+ models = BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT. No split agents. No destructive summary. Digest, coverage map and evidence never replace the FULL model file.

Embedded mandatory controls: 
01. Conversational Operation Router.
02. Startup Capability Menu.
03. Project Intake Decision Tree.
04. Auto / Basic Guided / Detailed creation modes.
05. Auto Model Synthesis Engine.
06. Field Ownership Policy.
07. Update/Migration Variable Decision Gate.
08. Full Runtime Evidence Policy.
09. Agent Runtime Fit Planner.
10. Runtime Coverage Map obligatorio.
11. Agent Export Parity Gate.
12. Project Evidence Bundle.
13. TechExt Materialization Gate.
14. Alias Resolver desde Profile360.
15. Legacy Contamination Linter.
16. Project Core Namespace Gate.
17. Colloquial Fuzz Suite.
18. Universal Pre-Delivery Audit + Retry Loop.
19. No Summary As Completeness Policy.
20. Project Package 10/10 vs Output Real 10/10 Separation.
21. Policy Harmonization / No Duplicate Authority Gate.
22. 20-file runtime policy.
23. MODEL_RUNTIME_PROFILE_FULL per model.
24. No split agent policy.
25. Max 10 models policy.

MODEL_RUNTIME_PROFILE_FULL per model is mandatory and must materialize Profile360 FULL60, TechExt FULL10, Master Visual Anchors, aliases, Face360, Body360, Skin360, Hair360, Wardrobe360, Voice360, Motion360, Scene/Environment affinity, camera/lighting rules, image/video reference rules, voice/audio/music/Suno/ElevenLabs rules, sidecar mapping, QA/fallbacks and source trace. No null, blank, placeholder or pending FACTORY_DEFINED_PROPOSED can remain in a final project delivery.

Runtime evidence gate: PROJECT_RUNTIME_COVERAGE_MAP required; Project Evidence Bundle required; Agent Export Parity Gate required; TechExt materialization required; alias resolver from Profile360 required; legacy contamination blocked; Project Core namespace gate required. PROJECT_PACKAGE_10_10 != OUTPUT_REAL_10_10. OUTPUT_REAL_10_10 requires asset + sidecar + prompt_hash + output_hash + QA + reviewer + lineage.

Truthfulness gate: if independent audit finds FAIL, delivery is blocked. No PASS with empty actual_value. Retry until 100% PASS. Policy harmonization/no duplicate authority gate blocks parallel authorities that conflict with LEGACY_NON_AUTHORITY.

Blocking fail codes: BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT, BLOCKED_TECH_EXT_NOT_MATERIALIZED, BLOCKED_TECH_EXT_NULL_INHERITANCE, BLOCKED_RUNTIME_COVERAGE_MAP_MISSING, BLOCKED_MODEL_ALIAS_NOT_RESOLVED, BLOCKED_LEGACY_MODEL_OUTSIDE_NAMESPACE, BLOCKED_PROJECT_CORE_PREFIX_DUPLICATE, BLOCKED_OUTPUT_REAL_10_10_WITHOUT_ASSET, BLOCKED_TRUTHFULNESS_INDEPENDENT_FAIL, BLOCKED_POLICY_DUPLICATE_AUTHORITY, BLOCKED_SUMMARY_AS_COMPLETENESS, BLOCKED_CONFIG_8000_REQUIRED_TOKEN_MISSING, BLOCKED_RUNTIME_CORE_LEGACY_NON_AUTHORITY.

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

# H245-H260 Agent Visual Routing Canonical Layer

Motor: IDUNEX_MOTOR_v1.0.0
Semantic version: v1.0.0
Correction mode: DIRECT_CANONICAL_NO_PATCH
Direct correction scope: H245_H260_APPLIED_ON_H01_H244
Creative output certified: FALSE

## H245 Agent execution routing layer
Runtime normativo, runtime operativo de generacion, companion forense compacto y certificacion por activo son capas separadas. Cargar runtime en agente habilita operacion; no equivale a cierre forense completo.

## H246-H252 Visual generation route
CLAUSE|IMAGE_FAST_ROUTE|For valid image requests targeting canonical fictional adult models, image generation must route directly to native image generation after minimal safety and model selector checks. Field-level QA, sidecar, hashes, reviewer and certification checks are post-generation requirements and must not block first visual candidate generation.|FAIL=FAIL_IMAGE_ROUTE_BLOCKED_BY_FORENSIC_PRECHECK|FALLBACK=generate candidate visual first, then emit GENERATED_VISIBLE_NOT_PACKAGED and missing evidence list.
CLAUSE|NO_AUXILIARY_TOOL_IMAGE_SUBSTITUTE|Python, code interpreter, data analysis, web search, canvas, diagrams, placeholder PNGs and no-op actions must never be used as substitutes for native image generation. If native image generation is unavailable, return IMAGE_TOOL_ROUTING_FAILED and do not fabricate an image result.|FAIL=FAIL_IMAGE_GENERATION_SUBSTITUTED_BY_NON_IMAGE_TOOL|FALLBACK=report IMAGE_TOOL_ROUTING_FAILED and request capability/configuration check.
CLAUSE|CANDIDATE_GENERATION_NOT_CERTIFICATION|A visible generated image candidate may be created before sidecar/hash/reviewer/QA evidence exists. The asset state must remain GENERATED_VISIBLE_NOT_PACKAGED and CREATIVE_OUTPUT_CERTIFIED=FALSE until all certification evidence is complete.|FAIL=FAIL_CERTIFICATION_PRECHECK_BLOCKS_CANDIDATE|FALLBACK=generate candidate and emit missing evidence list.
CLAUSE|NO_TEXT_IN_IMAGE_BY_DEFAULT|Default generated images must contain no text, no captions, no info panels, no project ids, no age labels, no certification labels, no QR, no fake UI, no brand claims and no rendered metadata. Watermark is postprocess-only unless explicitly supported and verified.|FAIL=FAIL_TEXT_ARTIFACT_CANON_DRIFT|FALLBACK=regenerate with NO TEXT and move all labels to sidecar/response.
CLAUSE|IMAGE_GENERATION_CLEAN_PROMPT_MODE|For image generation, send only visual scene, subject, composition, lighting, wardrobe, camera and negative constraints. Do not include audit metadata, project ids, certificate text, QA tables, sidecar status, hashes, lineage, visible age text, nationality text or profile fields inside the image prompt.|FAIL=FAIL_VENDOR_PROMPT_METADATA_LEAK|FALLBACK=strip metadata and reissue clean visual prompt; emit audit metadata only in response/sidecar.
CLAUSE|WATERMARK_POSTPROCESS_ONLY|Do not ask the generative model to hallucinate watermark text. Generate clean image first. Apply IDUNEX watermark only via verified postprocess overlay. If overlay cannot be verified, mark VISIBLE_WATERMARK_NOT_VERIFIED and keep CREATIVE_OUTPUT_CERTIFIED=FALSE.|FAIL=FAIL_WATERMARK_UNVERIFIED|FALLBACK=state GENERATED_VISIBLE_NOT_PACKAGED and require postprocess overlay.
CLAUSE|AGENT_RESPONSE_STATE_BLOCK|Every image generation attempt must emit ASSET_STATE, CREATIVE_OUTPUT_CERTIFIED, MODEL_TARGET, ROUTE_USED, MISSING_EVIDENCE and NEXT_REQUIRED_STEP outside the image.|FAIL=FAIL_AGENT_RESPONSE_STATE_BLOCK_MISSING|FALLBACK=emit state block outside image before any certification claim.

## H253-H256 Platform and safety routing
CLAUSE|CHATGPT_AGENT_CONFIG_ROUTING|ChatGPT agent configuration must place native image route, no auxiliary substitution, candidate first and certification later before sidecar, closure and ZIP proof gates.|FAIL=FAIL_CHATGPT_IMAGE_ROUTE_NOT_PRIORITIZED|FALLBACK=move IDUNEX_CHATGPT_IMAGE_ROUTING to top priority block.
CLAUSE|COPILOT_AGENT_CONFIG_CLEAN_OUTPUT|Copilot agent configuration must forbid visual panels, info cards, rendered metadata, fake canon, exact logo without asset and unverified watermark claims; metadata remains outside image.|FAIL=FAIL_COPILOT_VISUAL_METADATA_RENDERING_ALLOWED|FALLBACK=strip visual metadata and mark VISIBLE_WATERMARK_NOT_VERIFIED when overlay cannot be proven.
CLAUSE|YOUNG_ADULT_DEFAULT_WARDROBE_SAFE_BASELINE|For visible age 18-21, default wardrobe must be brand-safe smart casual or editorial commercial with non-revealing top, no deep neckline, no transparent fabric, no lingerie cues, no school-coded styling, no barely-legal framing, no bedroom glamour, no sexualized pose and no abdomen-focused composition unless explicitly safe and context-justified.|FAIL=FAIL_YOUNG_ADULT_WARDROBE_RISK|FALLBACK=convert wardrobe to smart casual editorial: blazer/overshirt, non-revealing top, high-waist trousers or jeans, natural pose.
CLAUSE|LOGO_RENDERING_ASSET_GATE|Exact visual logo rendering requires official authorized asset, hash and lineage. Without verified asset, use no logo or outside-image/postprocess wordmark with official_logo_match=false; vendor must not invent an exact logo.|FAIL=FAIL_LOGO_RENDERING_WITHOUT_ASSET|FALLBACK=remove exact logo from prompt and route to verified postprocess asset gate.

## H257-H260 Companion, schema and runtime priority
CLAUSE|AGENT_FORENSIC_COMPANION_COMPACT|Generated projects export AGENT_FORENSIC_COMPANION as a compact audit index with manifests, source trace ledgers, reopened proof summary, validator summary, prompt templates and SHA256SUMS. It is audit material, not runtime upload and not a precondition for first image candidate.|FAIL=FAIL_AGENT_FORENSIC_COMPANION_INDEX|FALLBACK=generate compact companion after runtime compilation and before package manifest rebuild.
CLAUSE|RUNTIME_RULE_SCHEMA_NORMALIZATION|Active rules with FAIL and FALLBACK must use CLAUSE|ID|content|FAIL=...|FALLBACK=... or appear in formal shorthand allowlist.|FAIL=FAIL_RUNTIME_RULE_SCHEMA_UNNORMALIZED|FALLBACK=normalize rule line or register shorthand allowlist entry.
CLAUSE|FIXTURE_CONTEXTUAL_ALLOWLIST|Project/model demo-like names are allowed only when sourced from user input or PROJECT_MANIFEST/source trace, never as active engine defaults.|FAIL=FAIL_FIXTURE_NAME_WITHOUT_TRACE|FALLBACK=replace active default with generic source-traced value or record user-input trace.
CLAUSE|AGENT_RUNTIME_LITE_PRIORITY_MODE|Agent instructions must prioritize selector, minimal safety, image native route, candidate generation, state block, no auxiliary substitution, no text in image and certification later; sidecar/closure/SHA/ZIP proof are post-output certification gates.|FAIL=FAIL_AGENT_RUNTIME_FORENSIC_PRECHECK_FIRST|FALLBACK=reorder priority block before forensic closure clauses.
