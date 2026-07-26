# AUD-035 — Sincronización de gobernanza interna post-AUD034

Refs #70.

```text
M03_RUN=30189604763
M03_JOB=89760318680
M03_ARTIFACT_ID=8628320119
M03_ARTIFACT_SHA256=0e3e014e62d46bbfb383d3cf69902ab0ae88fe3dd6a7e2165c56c77b37ed0974
BASE_COMMIT=2eb99d5c43bae4b2b077c38d0e40923ef7072857
PREVIOUS_ENGINE_TREE=981 / 47323574 / 58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7
INTERMEDIATE_DRAFT_PR71_ENGINE_TREE=981 / 47324957 / 22d64b639ed7657605787051d936bffc736cfa3d45b8799475adc28ef7ea0aeb
FINAL_ENGINE_TREE=981 / 47324981 / c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e
```

## Hallazgo y causa raíz

El caso M03-19 reprodujo `DOCUMENT_TRUTHFULNESS_PARITY_H245_H260` y `DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY`. La causa raíz fue la divergencia entre `CURRENT_STATE`, cinco superficies internas derivadas y el master governance contract.

La recomputación M02 de AUD-034 permanece como evidencia válida exclusivamente para el árbol `58454565...`. Se clasifica `REFERENCIA_SUSTITUIDA`, tiene `current_tree_applicability=false` y no se reasigna a la identidad intermedia `22d64b...` ni al árbol definitivo `c5cb2f4b...`.

## Corrección

Se sincronizaron las superficies internas, el validador integrado, los scanners, los contratos estáticos y los workflows/harnesses. Los seis manifests no autorreferenciales fueron regenerados mediante el scanner canónico bajo `NON_SELF_REFERENTIAL_INTERNAL_MANIFEST_POLICY`.

M02 y M03 quedan `NOT_RECOMPUTED_POST_AUD035`, clasificación persistente `EN_REVISION_M02_M03_NOT_RECOMPUTED_POST_AUD035`. Demo, release, tag, OFICIAL, carga de agentes y cierre siguen bloqueados. AUD-028 continúa `CONSUMED`, no autorizado, con generate/validate en cero. `CREATIVE_OUTPUT_CERTIFIED=FALSE`.

## Validación y reversa

No se ejecutaron M02, M03, el Proyecto 000 Demo ni `refresh-external-artifacts` real. M03-19 conserva como resultado esperado el rechazo de un validator FAIL.

Plan de reversa: revertir atómicamente los commits de AUD-035, regenerar manifests con el scanner canónico y repetir los checks locales. No se creó release, tag ni merge.
