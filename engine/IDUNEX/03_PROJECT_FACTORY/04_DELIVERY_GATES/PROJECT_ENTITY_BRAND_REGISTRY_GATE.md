# H43 - PROJECT_ENTITY_BRAND_REGISTRY_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `PROJECT_ENTITY_PROFILE.resolved.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H43_PROJECT_ENTITY_PROFILE_MISSING`
- `FAIL_H43_BRAND_SCOPE_UNRESOLVED`
- `FAIL_H43_RIGHTS_HOLDER_MISSING`
- `FAIL_H43_COMMERCIAL_SCOPE_WITHOUT_RIGHTS`
- `FAIL_H43_LOGO_EXACT_WITHOUT_OFFICIAL_ASSET_HASH`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
