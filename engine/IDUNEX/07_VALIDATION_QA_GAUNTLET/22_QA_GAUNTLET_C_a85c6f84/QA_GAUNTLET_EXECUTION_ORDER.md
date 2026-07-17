# QA_GAUNTLET_EXECUTION_ORDER

Comando público único: `python IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py [IDUNEX_ROOT]`.

Las entradas siguientes son checks internos agregados por ese entrypoint, no CLIs de cierre independientes. Un subvalidator solo puede ejecutarse para diagnóstico mediante `VALIDATE_IDUNEX_RUNTIME.py --subcheck <ID>` y su resultado queda limitado a `LOCAL_SUBCHECK_ONLY`.

1. JSON syntax: VALIDATE_JSON_INTERNALS_VALID.
2. Productive schemas: VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL y validators schema-productive específicos.
3. Runtime state: VALIDATE_PRODUCTIVE_BASE_ENGINE_STATE, no legacy activo.
4. Research/source: SRC_001-SRC_048 protected hashes, SRC_049 family dedup.
5. Project/Agent factories: Project Core, ChatGPT 10, Copilot 10 DOCX parity depth.
6. Profile360: 60 sections, registry keys, no empty runtime fields.
7. Model causality: node specificity and pairwise uniqueness.
8. Scene physics: arquetipos 13, fail codes ENV, sidecar evidence fields.
9. Manifests/hashes: SHA256SUMS, FILE_MANIFEST, HASH_MANIFEST.
10. External release: companion .sha256 + FINAL_EXTERNAL_RELEASE_EVIDENCE.

Stop rule: first BLOCKER failure produces NO_DELIVERY. Ningún resultado de esta secuencia declara M02_PASS; el estado vigente permanece `EN_REVISION` / `M02_FAIL` hasta re-auditoría independiente.
