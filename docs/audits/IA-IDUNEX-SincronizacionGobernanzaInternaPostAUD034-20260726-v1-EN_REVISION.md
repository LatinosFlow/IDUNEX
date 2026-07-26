# AUD-035 — Sincronización de gobernanza interna post-AUD034

Refs #70. Ejecución M03 `30189604763`, job `89760318680`, artifact `8628320119` (SHA-256 conservado como evidencia histórica en el tracker del issue).

## Hallazgo y corrección

El caso M03-19 reprodujo los failcodes globales `DOCUMENT_TRUTHFULNESS_PARITY_H245_H260` y `DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY`. La causa raíz fue la divergencia entre CURRENT_STATE, cinco superficies internas derivadas y el master governance contract. Se actualizaron esas superficies, el validador integrado, los scanners/contratos estáticos y los workflows/harnesses para rechazar la identidad anterior.

Identidad anterior: `981` archivos, `47323574` bytes, `58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7`.

NEW_ENGINE_IDENTITY: `981` archivos, `47324957` bytes, `22d64b639ed7657605787051d936bffc736cfa3d45b8799475adc28ef7ea0aeb`; el cálculo se repitió dos veces con igualdad exacta. Los seis manifests no autorreferenciales fueron regenerados por `tools/audit/baseline_scanner.py --write` bajo `NON_SELF_REFERENTIAL_INTERNAL_MANIFEST_POLICY`.

M02 y M03 quedan `NOT_RECOMPUTED_POST_AUD035`, `ESTADO_PROPUESTO_EN_REVISION_HASTA_MERGE`. Demo, release, tag, OFICIAL, agentes y cierre siguen bloqueados; AUD-028 continúa `CONSUMED`, no autorizado, con generate/validate en cero y `CREATIVE_OUTPUT_CERTIFIED=FALSE`.

## Validación y reversa

El validador global pasó con `validators_fail=0`, `blocking_warnings=0` y `fail_codes=[]`; no se ejecutaron M02, M03, Demo, generate real ni refresh externo. Las pruebas preventivas conservan M03-19 como rechazo de un validator FAIL.

Reversa: revertir atómicamente el commit del PR; regenerar manifests con el scanner canónico y volver a ejecutar los checks locales. No se creó release, tag ni merge.
