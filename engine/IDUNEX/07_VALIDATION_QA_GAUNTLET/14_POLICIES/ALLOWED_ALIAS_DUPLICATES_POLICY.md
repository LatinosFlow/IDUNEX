# ALLOWED_ALIAS_DUPLICATES_POLICY — IDUNEX_MOTOR_v1.0.0

ENGINE_VERSION=IDUNEX_MOTOR_v1.0.0
ENGINE_RELEASE_DATE=NEUTRALIZED_ACTIVE_SCOPE
PRODUCTION_STATUS=prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE
prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE
prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; project_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE
prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE

## Política

Los duplicados exactos solo están permitidos cuando son alias técnicos intencionales, declarados con ruta canónica, owner funcional, motivo y severidad.  
Cualquier duplicado exacto no declarado debe clasificarse como WARNING o FAIL según severidad operativa.  
Esta política no autoriza duplicación semántica de investigaciones ni double-counting de cobertura.

## Alias técnicos permitidos

### ALIAS_GROUP_ID=ALIAS_FAIL_CODE_REGISTRY_MIRROR

CANONICAL_ROUTE=13_QA_GAUNTLET/FAIL_CODE_REGISTRY.json  
ALIAS_ROUTES=
- 04_PROFILE360_SYSTEM/04_QA_LINKS/PROFILE360_FAILCODES.json
- 04_PROFILE360_SYSTEM/05_QA_FAILCODES/PROFILE360_FAILCODES.json

OWNER_FUNCTIONAL=IDUNEX_QA_GOVERNANCE  
DUPLICATE_ROLE=failcode_registry_runtime_mirror  
REASON=El registro de fail codes se expone en rutas operativas de Perfil360 y QA Gauntlet para compatibilidad de lectura sin alterar el contenido canónico.  
SEVERITY_IF_UNDECLARED=FAIL  
ACTION_ON_DIFF=REVIEW_AND_SYNC_CANONICAL_REGISTRY

### ALIAS_GROUP_ID=ALIAS_SOURCE_COVERAGE_REPORT_MIRROR

CANONICAL_ROUTE=05_SOURCE_TO_RUNTIME/06_COVERAGE/SOURCE_SEMANTIC_COVERAGE_REPORT.json  
ALIAS_ROUTES=
- 05_SOURCE_TO_RUNTIME/04_COVERAGE/SOURCE_SEMANTIC_COVERAGE_REPORT.json

OWNER_FUNCTIONAL=IDUNEX_RESEARCH_QA_AUDITOR  
DUPLICATE_ROLE=coverage_report_compatibility_mirror  
REASON=La ruta 04_COVERAGE existe como alias de compatibilidad solicitado por auditoría; la ruta 06_COVERAGE conserva la ubicación histórica/canónica.  
SEVERITY_IF_UNDECLARED=FAIL  
ACTION_ON_DIFF=RESEARCH_LAYER_LOCKED_NOT_IN_SCOPE

### ALIAS_GROUP_ID=ALIAS_SHA256SUMS_INTERNAL_MIRROR

CANONICAL_ROUTE=SHA256SUMS.txt  
ALIAS_ROUTES=
- 99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt

OWNER_FUNCTIONAL=IDUNEX_HASH_GOVERNANCE  
DUPLICATE_ROLE=sha256_manifest_root_and_lineage_mirror  
REASON=El archivo SHA256SUMS se publica en raíz interna y en lineage para consumo humano y validación técnica con el mismo contenido.  
SEVERITY_IF_UNDECLARED=WARNING  
ACTION_ON_DIFF=REGENERATE_HASH_MANIFESTS

## Regla de cierre

ALLOWED_DUPLICATES_POLICY_STATUS=ACTIVE
UNDECLARED_DUPLICATES_POLICY=WARNING_OR_FAIL_BY_SEVERITY
RESEARCH_LAYER_SCOPE=LOCKED_NOT_IN_SCOPE
