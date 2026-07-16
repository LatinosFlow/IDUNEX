# DELIVERY_ARTIFACT_MINIMAL_SET_POLICY

Estado: ACTIVE_PASS
SEMANTIC_VERSION=v1.0.0
VERSION_BUMP=NO
CORRECTION_MODE=DIRECT_CANONICAL_NO_PATCH
OUTPUT_EXTERNAL_CONTRACT=EXACT_7_OF_7

## Set externo permitido vigente
1. IDUNEX_MOTOR_v1.0.0.zip
2. IDUNEX_MOTOR_v1.0.0.zip.sha256
3. IDUNEX_MOTOR_v1.0.0_RELEASE_CERTIFICATE.txt
4. IDUNEX_MOTOR_v1.0.0_MANUAL_TECNICO_ALCANCE_LATINOSFLOW.pdf
5. IDUNEX_MOTOR_v1.0.0_MANUAL_DE_TRABAJO_LATINOSFLOW.pdf
6. IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO_AUTORIDAD_MOTOR.txt
7. IDUNEX_PROMPT_SUITE_PLANTILLAS_PROYECTOS_AUTORIDAD_MOTOR_.docx

Los reportes detallados viven dentro del ZIP. La evidencia historica P03/P034 solo puede existir como lineage compacto no autoritativo bajo 12_HISTORICAL_NON_AUTHORITY; no es artefacto externo activo.

## Hard gates activos
- FAIL si el set externo activo no es 7/7 exacto.
- FAIL si falta el prompt canonico.
- FAIL si falta la prompt suite DOCX.
- FAIL si un changelog P03 aparece como artefacto externo activo.
- FAIL si la version semantica usa sufijos o marcador unchanged.

## actual_value
external_artifacts_allowed=7; detailed_reports_inside_zip=true; prompt_canonical_and_prompt_suite_required=true
