## Phase 3 file-level inheritance
inherits = AGENT_FACTORY_GLOBAL_RULES#COMMON_AGENT_RUNTIME_QA_BLOCK
inherits_mandatory_fields = AGENT_FACTORY_GLOBAL_RULES#COMMON_MANDATORY_FIELDS
agent_specific_delta_required = true

# AGENT FACTORY FULL CONTRACT — PRODUCTIVE ACTIVE AUTHORITY

## Active runtime authority patch — 1ADD3F8D surgical input
- IDUNEX_MOTOR_VERSION: v1.0.0
- runtime_authority: ACTIVE_PRODUCTIVE_BASE_ENGINE_CONTRACT
- ENGINE_GO: true
- PROJECT_FACTORY_GO: true
- AGENT_FACTORY_GO: true
- PROJECT_INSTANCE_GO: false_until_project_QA
- OUTPUT_GO: false_until_output_QA_SIDECAR_HASH_LINEAGE
- input_package_sha256_before_this_surgical_patch: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`
- parent_hash_1d0c_policy: `HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY / DO_NOT_USE_AS_BASE / NOT_RUNTIME_AUTHORITY`
- anti_regression_rule: preserve useful contract body below; do not restore historical headers as active authority.
- validation_state: PRODUCTIVE_BASE_ENGINE_ACTIVE
- updated_at: NEUTRALIZED_ACTIVE_SCOPE

ENGINE_STATE: runtime_validation_state=PRODUCTIVE_BASE_ENGINE_ACTIVE. ENGINE_GO: true; PROJECT_INSTANCE_GO: false_until_project_QA; OUTPUT_GO: false_until_output_QA_SIDECAR_HASH_LINEAGE.

## ChatGPT Agent


## Copilot Word Agent


## Copilot Excel Agent


## Copilot PowerPoint Agent


## Image Prompt Agent


## Video Prompt Agent


## Voice Agent


## Suno Agent


## QA Auditor Agent


## Legal Governance Agent


## Sidecar Auditor Agent


## No-Loss Migration Agent


## HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.5 Agent Factory — agent-complete contract
| Agent | role | scope | input_contract | output_contract | forbidden_actions | required_sources | required_locks | qa_before_output | handoff_protocol | readback_protocol | failure_protocol | example_prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ChatGPT Agent | planning/runtime writer | JSON/TXT/Profile360 | source_ids+field_ids+locks | structured runtime files | invent sources/locks | selected runtime sources | JSON/ANCHOR/AGE/ID | schema+source trace | emit sidecar refs | report loaded sources | FAIL_BLOCKER if missing | Load Profile360 and produce no-loss plan |
| Copilot Word Agent | DOCX grounding | Word/DOCX canon | H1-H4+trace tables | readback/document | summarize locks destructively | SRC_029/SRC_048 | docx locks | render/readback | package handoff | engine/project/locks/sources | split chunks | Read back loaded canon before writing |
| Copilot Excel Agent | tabular QA | matrix/spreadsheet | schemas+tables | validated workbook spec | infer hidden rows | QA/schemas | source trace | row/column validation | export tables | counts/checks | fail row drift | Validate matrix counts |
| Copilot PowerPoint Agent | slide briefing | presentation | claims+evidence | slide outline | unsupported claims | claim matrix | no-global-go | claim evidence | export outline | readback claims | fail thin claim | Build audit deck only from claims |
| Image Prompt Agent | image prompt | visual outputs | promptpack+Profile360 | image prompt/sidecar | identity drift | visual sources | identity locks | visual QC | sidecar required | report fields | repair prompt | Generate locked image prompt |
| Video Prompt Agent | video prompt | motion outputs | frame plan | video prompt/sidecar | morphing | video sources | continuity locks | frame checks | sidecar | frame readback | shorten shot | Generate frame-locked video prompt |
| Voice Agent | voice test | speech | script+voice fields | voice params/sidecar | childlike/celebrity | voice sources | age/voice locks | speaker drift | sidecar | voice readback | adjust prosody | Produce adult voice spec |
| Suno Agent | music test | music/lyrics | music fields | lyrics/prompt/sidecar | generic/celebrity | music sources | voice/music locks | genre/lyric QC | sidecar | music readback | rewrite tags | Produce music prompt |
| QA Auditor Agent | audit | all runtime | manifests+schemas | QA report | false PASS | all sources | all locks | validate all | fail report | gates readback | block GO | Audit package |
| Legal Governance Agent | legal/safety | policy | legal sources | policy gate | infer consent | governance sources | legal locks | policy check | no-go report | legal readback | block release | Check commercial scope |
| Sidecar Auditor Agent | trace | metadata | sidecars+hashes | sidecar QA | fake hash | sidecar sources | trace locks | hash validation | sidecar handoff | trace readback | fail mismatch | Validate sidecars |
| No-Loss Migration Agent | migration | versioning | old/new manifests | diff report | delete valid content | no-loss sources | version locks | no-loss diff | block/regenerate package | diff readback | block and regenerate | Migrate without loss |

## Agent operational fiches

### ChatGPT Agent

### Copilot Word Agent

### Copilot Excel Agent

### Copilot PowerPoint Agent

### Image Prompt Agent

### Video Prompt Agent

### Voice Agent

### Suno Agent

### QA Auditor Agent

### Legal Governance Agent

### Sidecar Auditor Agent

### No-Loss Migration Agent


## V1.0.8 AUTHORITY EXPANSION

This contract is the only authoritative runtime contract for this factory. Every derived project or agent must declare required_inputs, required_outputs, required_adapters, required_schemas, required_golden_tests, required_sidecars, required_hashes, fail_conditions, recovery_policy, readback_protocol and go_no_go_policy. PASS requires prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE until a real project-level output bundle passes sidecar, QA and hash reproducibility.

### Example PASS report
- required files loaded; source_ids traced; field_ids traced; adapters declared; QA gates pass; fallback not required; prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE.

### Example FAIL report
- missing sidecar, missing source trace, output without hash, project attempts GLOBAL_GO from motor baseline. Decision: FAIL_BLOCKER.

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
