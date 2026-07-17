# H45 - VISUAL_ANCHOR_LIFECYCLE_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `MASTER_VISUAL_ANCHOR_REGISTER_ALL_MODELS.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H45_VISUAL_ANCHOR_REGISTER_MISSING`
- `FAIL_H45_APPROVED_ANCHOR_WITHOUT_HASH`
- `FAIL_H45_APPROVED_ANCHOR_WITHOUT_REVIEWER`
- `FAIL_H45_TEXTUAL_ANCHOR_FALSELY_CERTIFIED_AS_VISUAL`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
