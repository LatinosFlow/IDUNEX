# H41 - PAIRWISE360_EXTERNAL_MATRIX_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `PAIRWISE360_ALL_MODEL_PAIRS_MATRIX.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H41_PAIRWISE_MATRIX_MISSING`
- `FAIL_H41_PAIRWISE_PAIR_COUNT_MISMATCH`
- `FAIL_H41_PAIRWISE_DOMAIN_MISSING`
- `FAIL_H41_PAIRWISE_DELTA_NOT_EXPLICIT`
- `FAIL_H41_PAIRWISE_ANTI_BLEND_FALLBACK_MISSING`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
