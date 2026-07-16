# EXPORT_PACKER_POLICY - IDUNEX MOTOR v1.0.0

correction_base_sha256 = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
historical_previous_base_sha256 = a7424ad2f7808162495c7c7f8aeba55a6e9160226e57e83cac7bd23b91c2666e
historical_previous_base_policy = HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL
updated_at = NEUTRALIZED_ACTIVE_SCOPE

## Productive export gate

`IDUNEX_EXPORT_PACKER.py` is not a simple zipper. It blocks export unless all productive project package gates pass:

- exists PROJECT_CORE/
- exists CHATGPT/
- exists COPILOT/
- exists PROJECT_PACKAGE_MANIFEST.txt
- exists PROJECT_PACKAGE_QA_REPORT.md
- exists PROJECT_PACKAGE_SHA256SUMS.txt
- ChatGPT contains exactly 10 official core .md files
- Copilot contains exactly 10 official core .docx files
- MODELS contains 1 to 10 Profile360 profiles per agent pack
- CONFIG/PROJECT-CONFIGURACION-AGENT.txt exists in ChatGPT and Copilot
- each agent config has exactly 8000 UTF-8 characters
- each agent config ends with CONFIG_END=IDUNEX_AGENT_CONFIG_LOCKED
- template hash ledgers are replaced before real export
- PROJECT_PACKAGE_SHA256SUMS.txt is regenerated with real hashes
- CHATGPT/COPILOT MANIFESTS/SHA256SUMS.txt are regenerated before package build
- PROJECT_PACKAGE_QA_REPORT.md cannot remain TEMPLATE_ONLY for real package
- project manifest validates against productive schema keys
- zip `testzip()` passes
- external companion `.sha256` is generated and matches the output zip

## Implemented callable functions

- validate_project_structure(root)
- validate_agent_packs(root)
- validate_profile360_models(root)
- validate_project_manifest_schema(root)
- regenerate_project_sha256sums(root)
- replace_template_hash_ledgers(root)
- validate_project_qa_report(root)
- build_project_package(project_root, output_zip)

## Delivery rule

Real project export remains blocked until project QA, output QA, sidecar, hash and lineage are satisfied.

## QA / source / fail / fallback controls

source trace: Project exports must preserve source_scope = ALL_ACTIVE_SOURCES_001_049 from Project Core to ChatGPT, Copilot, QA reports, SHA ledgers and sidecar evidence.
fail conditions: missing structure, incomplete agent packs, wrong config length, missing manifests, template hash ledgers, template-only QA, invalid manifest schema, zip integrity error, or mismatching external companion.
fallback fixes: regenerate SHA ledgers, replace template hashes, repair manifest schema fields, rebuild QA report from Project Core authority, then re-run build_project_package and zip testzip.
QA evidence: every export must retain project QA, hash evidence and sidecar lineage before delivery.

## Hash authority — surgical hardening a742

- input_package_sha256_before_this_surgical_patch: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`
- correction_base_sha256: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`
- expected_correction_base_sha256: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`
- FINAL_ZIP_SHA256_AUTHORITY: `EXTERNAL_COMPANION_SHA256_FILE`
- final_zip_sha256_real: `RECORDED_EXTERNALLY_IN_COMPANION_AFTER_PACKAGE_BUILD`
- historical_previous_bases_policy: `HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL` / `HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY` / `DO_NOT_USE_AS_BASE`
- historical_previous_bases_non_operational:
- `a7424ad2f7808162495c7c7f8aeba55a6e9160226e57e83cac7bd23b91c2666e` — PREVIOUS_SURGICAL_INPUT_LINEAGE; PARENT_PACKAGE_LINEAGE_ONLY; HISTORICAL_PARENT_NOT_OPERATIONAL_AS_CURRENT_BASE


## Historical previous bases — non-operational

- `8c9cac03080a16947bf74d580fc423d605e97643498da50bca09722e396a7d35` — HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL; HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY; DO_NOT_USE_AS_BASE
- `b259fb10bd9d69e8885b2f6896864d56dcc0edbf4f799f339bc533eb894e046b` — HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL; HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY; DO_NOT_USE_AS_BASE
- `c6e7ab123ab6e0f70838da426c30114bd27e6809c24df73469e8ce5f47b838db` — HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL; HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY; DO_NOT_USE_AS_BASE
- `ca146a322d59d0eb413756ef4fb7cde6a039bf796490473a7cff4cfb61514adf` — HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL; HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY; DO_NOT_USE_AS_BASE


## Surgical lineage patch — POSTPACKAGE_11F6F033_INPUT

- base_sha256_validated_before_patch = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
- correction_base_sha256 = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
- expected_correction_base_sha256 = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
- input_package_sha256_before_this_surgical_patch = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
- current_input_base_status = ACTIVE_CORRECTION_INPUT_BASE_NOT_HISTORICAL_NOT_DO_NOT_USE
- parent_package_lineage = a7424ad2f7808162495c7c7f8aeba55a6e9160226e57e83cac7bd23b91c2666e — PREVIOUS_SURGICAL_INPUT_LINEAGE / PARENT_PACKAGE_LINEAGE_ONLY / HISTORICAL_PARENT_NOT_OPERATIONAL_AS_CURRENT_BASE
- FINAL_ZIP_SHA256_AUTHORITY = EXTERNAL_COMPANION_SHA256_FILE
- final_sha256_real = RECORDED_EXTERNALLY_IN_COMPANION_AFTER_PACKAGE_BUILD
- EXTERNAL_VALIDATION_MODE = RUN_VALIDATOR_WITH_IDUNEX_PACKAGE_ZIP
- validator_hardening_added = VALIDATE_CURRENT_INPUT_BASE_NOT_MARKED_HISTORICAL_OR_DO_NOT_USE; VALIDATE_CURRENT_CORRECTION_BASE_NOT_MARKED_HISTORICAL_OR_DO_NOT_USE; VALIDATE_REPORT_HEADINGS_MATCH_ACTIVE_INPUT_BASE_PREFIX; VALIDATE_HISTORICAL_AUDITS_EXPLICITLY_NON_OPERATIONAL; VALIDATE_NO_DUPLICATE_CURRENT_BASE_IN_HISTORICAL_LISTS; VALIDATE_EXTERNAL_VALIDATION_SUMMARY_MATCHES_COMPANION_SHA; VALIDATE_VALIDATOR_FALSE_PASS_GUARD_FOR_BASE_STATUS_CONTRADICTIONS
