# MODEL_ALIAS_BLOCKING_RULES

| Bloqueo | Cuándo aplica | Corrección |
|---|---|---|
| BLOCKED_MODEL_ALIAS_NOT_RESOLVED | Alias ambiguo o inexistente | Cargar manifest/model index o pedir identificación mínima |
| BLOCKED_PROFILE360_NOT_LOADED | No está cargado el Profile360 completo | Adjuntar/cargar Profile360 full, no resumen |
| BLOCKED_TECHEXT_NOT_AVAILABLE | Modalidad requiere TechExt y no existe | Exportar/cargar TechExt FULL10 |
| BLOCKED_MASTER_ANCHORS_NOT_AVAILABLE | Modalidad visual requiere anchors | Cargar Master Visual Anchors |
| BLOCKED_RUNTIME_CORE_NOT_LOADED | Faltan core runtime files | Cargar 10 archivos core obligatorios |
| BLOCKED_OUTPUT_GO_TRUE_WITHOUT_SIDECAR_HASH_LINEAGE | Se quiere declarar final sin evidencia | Crear sidecar, hash y lineage |
| BLOCKED_PROJECT_CLOSE_WITHOUT_GOLDEN_TESTS_DEFINED | Se quiere cerrar proyecto sin golden tests | Definir/ejecutar matriz según nivel |
