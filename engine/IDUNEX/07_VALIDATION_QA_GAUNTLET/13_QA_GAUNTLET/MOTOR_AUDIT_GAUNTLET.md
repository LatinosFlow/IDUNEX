# MOTOR_AUDIT_GAUNTLET.md

## Executable QA procedure — HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.5
Purpose: convert this QA file from summary into an executable audit protocol.

### Input files
- PROFILE360_FIELD_REGISTRY.json
- SOURCE_TO_RUNTIME_MASTER_MAP.json
- SOURCE_SEMANTIC_COVERAGE_REPORT.json
- SIDECAR schema/templates
- PROJECT_FIXTURE_VALIDATION_001 evidence bundle
- HASH_MANIFEST / FILE_MANIFEST / SHA256SUMS

### Execution steps
1. Load canonical manifests and verify file_count and hash lineage.
2. Validate field_id, runtime_domain, source_ids, adapter_targets, qa_rule_id, fail_code, fallback_fix and golden_test_id.
3. Run schema validation on all critical JSON fixtures.
4. Verify source cards and coverage are synchronized with runtime map.
5. Check sidecar by modality: adapter, vendor_params, field_ids, source_ids, hashes and production state.
6. Run modality-specific golden tests and record PASS/WARNING/FAIL.
7. Apply fallback and retest if any warning or fail is detected.

### PASS criteria
- 0 critical errors.
- No GLOBAL_GO in motor baseline.
- Coverage score never exceeds 9 without output+sidecar+QA+hash evidence.
- All failures have fail_code and surgical fallback.

### WARNING criteria
- Support-only source allowed for baseline but requires PROJECT_GO manual review.
- High-fidelity mock evidence allowed only for prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE.

### FAIL criteria
- Hash mismatch, schema mismatch, untracked source, generic golden test, adapter mismatch, fake hash, or GLOBAL_GO declaration from motor.

### Output report format
JSON object with audit_status, critical_errors, warnings, go_no_go_decision, files_checked, failed_files, fallback_actions and retest_result.

### Production decision
Motor baseline may reach prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE. PROJECT_GO/GLOBAL_GO require real project artifacts and human approval.

## Executable QA Procedure
- purpose: validate this QA dimension without interpretation drift.
- input files: project manifest, Profile360 fields, source map, fail codes, sidecars, hash evidence and modality fixtures.
- execution command: run `python IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py` and then execute the modality-specific checklist in this file.
- validation rules: JSON/schema pass; source trace present; field trace present; adapter trace present; sidecar hash present; GLOBAL_GO false.
- pass criteria: all checks pass with no critical errors and no unresolved placeholders in non-template outputs.
- warning criteria: baseline-only evidence, support-only source, coverage capped at 8/9, or manual review required before PROJECT_GO.
- fail criteria: schema mismatch, missing sidecar, missing hash evidence, adapter mismatch, GLOBAL_GO attempted from motor baseline.
- fail codes: FAIL_BLOCKER_VALIDATOR_INCOMPLETE; FAIL_BLOCKER_COVERAGE_10_WITHOUT_REAL_OUTPUT_EVIDENCE; FAIL_BLOCKER_GLOBAL_GO_FROM_MOTOR_BASELINE.
- fallback fixes: regenerate affected manifest, rerun source-to-runtime map, repair sidecar, recalculate hash, repeat test.
- retest protocol: rerun validator and produce PASS/FAIL report with timestamp and reviewer.
- output report format: JSON QA result plus Markdown summary with evidence paths and go/no-go decision.
- production decision: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE only; PROJECT_GO/GLOBAL_GO forbidden without real project evidence.

### Example PASS report
`audit_status=PASS`, `global_go=false`, all schemas valid, sidecars present, hash evidence reproducible, coverage score <= 9. [HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY]

### Example FAIL report
`audit_status=FAIL`, schema mismatch or missing sidecar/hash, fallback listed, retest required.

## H71-H80 SAFE_APPAREL_WATERMARK_AGENT10N
H71_H80_AGENT10N=SAFE_APPAREL_TAXONOMY; ADULT_REVEALING_APPAREL_NOT_NUDITY; VENDOR_PROMPT_SANITIZATION_SAFE_APPAREL; WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED; ALLOW adult editorial beachwear/swimwear/intimate apparel/catalog/corset/body/performance wardrobe when covered non-explicit; BLOCK nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded or school-coded sexualization and real-person copying.
ALLOW_ADULT_EDITORIAL: moda de playa, traje de bano, ropa de bano, bikini editorial, swimwear campaign, beachwear, resortwear, moda intima editorial/catalog, ropa interior de catalogo, corset/body/bodysuit, vestuario de show adulto, vestuario de videoclip adulto y outfit de performance adulta cuando el modelo es adulto, cubierto y no explicito.
CONDITIONAL_REWRITE: convertir styling glam/provocativo, boudoir editorial, fantasia adulta y vestuario de alto impacto a lenguaje adulto, editorial, comercial, non-explicit, covered intimate areas.
BLOCK_ALWAYS: nudity, exposed intimate areas, topless, intimate act, pornographic framing, minor-coded styling, school-coded sexualization, real-person copying y cualquier intento de saltar locks de edad o identidad.
WATERMARK_DEFAULT_ON=true; watermark_text=idunex; watermark_position=bottom_center; EXPLICIT_IDUNEX_OPTOUT_ONLY; POSTPROCESS_OVERLAY_REQUIRED.
