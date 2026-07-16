# BLOCKED_TECH_EXT_NULL_INHERITANCE

TechExt template JSON is schema-only/non-exportable until the Project Factory materializes unique model-specific values inside MODEL_RUNTIME_PROFILE_FULL. Final project export is blocked if any mandatory TechExt field contains null, blank, placeholder, FACTORY_DEFINED_PROPOSED pending or FACTORY_FILL_REQUIRED_NON_EXPORTABLE. If TechExt is incomplete, PROJECT_PACKAGE_PASS is blocked.

Fallback fix: materialize all TechExt FULL10 fields per model, rebuild sidecar mapping and PROJECT_RUNTIME_COVERAGE_MAP, run TECHEXT_TEMPLATE_NULL_INHERITANCE_AUDIT and retry until 100% PASS.
