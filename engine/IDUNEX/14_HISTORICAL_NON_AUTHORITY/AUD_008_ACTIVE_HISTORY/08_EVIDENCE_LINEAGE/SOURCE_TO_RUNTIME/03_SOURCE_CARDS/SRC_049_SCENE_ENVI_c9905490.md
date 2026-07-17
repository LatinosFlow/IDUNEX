# Source Card SRC_049_ENV_PHYSICS_FULL10 - Physics & Mise-en-Scene Enhancer

source_id_canonical = SRC_049_ENV_PHYSICS_FULL10
source_alias = ENV_PHYSICS_FULL10
source_title = Physics & Mise-en-Scène Enhancer
runtime_module = SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10
status = PRODUCTIVE_BASE_ENGINE_VALIDATED

## Runtime authority
SRC_049 controls production design, art direction, mise-en-scene, spatial composition, blocking, body-object relation, props, gravity, occlusion, scale, perspective, lighting, shadows, reflections, image-video continuity, cultural/locality coherence and editorial safety.

## Alias exclusivity
Only SRC_049_ENV_PHYSICS_FULL10 can use source_alias=ENV_PHYSICS_FULL10. SRC_001-SRC_048 cannot use this alias.

## Source-to-runtime outputs
- Profile360 sections affected: 40-49, 52, 54-57, 60.
- Project Core rule: all scene prompts require physical contact, scale, occlusion, light/shadow and sidecar evidence.
- ChatGPT/Copilot rule: no scene output is accepted without ENV fail-code QA and fallback fixes.
- Validators: VALIDATE_SOURCE_049_ENV_PHYSICS_REGISTERED, VALIDATE_SRC049_ALIAS_EXCLUSIVE, VALIDATE_SCENE_SPATIAL_PHYSICS_FULL10.

## SRC049 family dedup policy
- card_role: BRIDGE/HISTORICAL-COMPATIBLE SOURCE CARD
- canonical_source_id: SRC_049_ENV_PHYSICS_FULL10
- bridge_runtime_module: SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10
- source_alias: ENV_PHYSICS_FULL10
- canonical_source_count: 49
- physical_card_files_may_be: 50 due SRC049 bridge only
- no_double_count_rule: both SRC049 files map to one canonical source family.


---
P1-01 SRC_049 BRIDGE POLICY UPDATE
physical_card_type = CANONICAL_BRIDGE_NOT_COUNTED_AS_SOURCE
canonical_source_count_impact = 0
source_id_canonical = SRC_049_ENV_PHYSICS_FULL10
source_alias = ENV_PHYSICS_FULL10
runtime_module = SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10
dedup_policy = SRC_049_ENV_PHYSICS_FULL10 is counted once in SOURCE_INVENTORY_MASTER; any second physical card is bridge evidence only and never increments canonical source count.
updated_at = NEUTRALIZED_ACTIVE_SCOPE
---

---
PHASE_1_4_SRC049_STRICT_NORMALIZATION
updated_at = NEUTRALIZED_ACTIVE_SCOPE
canonical_source_card = SRC_049_ENV_PHYSICS_FULL10_SOURCE_CARD.md
bridge_source_card = SRC_049_SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10.md
bridge_policy = COMPATIBILITY_BRIDGE_NOT_SECOND_CANONICAL_SOURCE
mirror_policy = COMPATIBILITY_MIRROR_NOT_SECOND_AUTHORITY
canonical_source_id = SRC_049_ENV_PHYSICS_FULL10
source_id_original = SRC_049_SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10
source_id_canonical = SRC_049_ENV_PHYSICS_FULL10
source_alias = ENV_PHYSICS_FULL10
runtime_module = SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10
canonical_lookup_keys = source_id, source_id_original, source_id_canonical, source_alias, runtime_module
runtime_authority = false_for_bridge_card_only
canonical_source_count = 49
physical_card_files_may_be = 50_due_SRC049_bridge_only
duplicate_count_policy = PHYSICAL_BRIDGE_ALLOWED_CANONICAL_COUNT_REMAINS_49
no_double_count_rule = SRC_049 physical bridge files resolve to one canonical source family only.
---
