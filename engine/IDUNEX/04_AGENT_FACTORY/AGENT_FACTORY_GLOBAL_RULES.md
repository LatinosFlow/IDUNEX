# AGENT_FACTORY_GLOBAL_RULES — IDUNEX MOTOR v1.0.0

## COMMON_AGENT_RUNTIME_QA_BLOCK
| Campo | Uso en prompt | Uso en QA | Fallback quirúrgico |
|---|---|---|---|
**Bloqueo:** si falta dato estructural, activar GAP_REQUIRED y no inventar.  
**Criterio PASS:** salida conserva identidad, coherencia física, estilo, vendor constraints y lineage.

## COMMON_MANDATORY_FIELDS
- role: mandatory; unresolved values trigger REVIEW_REQUIRED.
- scope: mandatory; unresolved values trigger REVIEW_REQUIRED.
- input_contract: mandatory; unresolved values trigger REVIEW_REQUIRED.
- output_contract: mandatory; unresolved values trigger REVIEW_REQUIRED.
- forbidden_actions: mandatory; unresolved values trigger REVIEW_REQUIRED.
- required_sources: mandatory; unresolved values trigger REVIEW_REQUIRED.
- required_locks: mandatory; unresolved values trigger REVIEW_REQUIRED.
- qa_before_output: mandatory; unresolved values trigger REVIEW_REQUIRED.
- handoff_protocol: mandatory; unresolved values trigger REVIEW_REQUIRED.
- readback_protocol: mandatory; unresolved values trigger REVIEW_REQUIRED.
- failure_protocol: mandatory; unresolved values trigger REVIEW_REQUIRED.
- example_prompt: mandatory; unresolved values trigger REVIEW_REQUIRED.

## Regla de delta por agente
Cada archivo de Agent Factory conserva función diferencial: ChatGPT load, Copilot DOCX runtime, instrucciones, autoload router, config 8000 o contrato full.

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
