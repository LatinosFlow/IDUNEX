# MIRROR POLICY — COMPATIBILITY WITHOUT DUPLICATE AUTHORITY

generated_at = NEUTRALIZED_ACTIVE_SCOPE
phase = FASE_1_4
mirror_policy = COMPATIBILITY_MIRROR_NOT_SECOND_AUTHORITY

## Rule
Duplicated physical files may remain for compatibility/no-loss, but only one file in each group is runtime authority. Mirrors MUST declare:

- mirror_of = <authority_file>
- runtime_authority = false
- hash_sync_required = true
- no_duplicate_authority = true

## Registered evidence
See: IDUNEX/99_MANIFESTS_SHA_LINEAGE/PHASE_1_MIRROR_POLICY_REGISTRY.json

## Validator
VALIDATE_MIRROR_POLICY_NO_DUPLICATE_AUTHORITY = PASS only if every duplicate group has one authority and all other files are mirrors.

## LEGACY_NON_AUTHORITY No Duplicate Authority Extension
Before adding any policy, search existing authority, extend equivalent authority, record why a new file is required, create migration/equivalence map, update references, recalc manifests and audit POLICY_DUPLICATE_AUTHORITY=0.
