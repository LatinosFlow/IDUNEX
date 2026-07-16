# SOURCE_RUNTIME_LEDGER_MINIFIED_STRICT_VALIDATOR

Estado: ACTIVE_PASS

## Schema estricto por SRC
Cada entrada SRC_001-SRC_049 debe contener: `source_id`, `source_title` o `title`, `engine_layer`, `project_layer`, `exported_files` o `derived_project_files`, `coverage_status`, `no_loss_assertion` y `validator_reference`.

## Regla bloqueante
Si cualquier SRC carece de un campo obligatorio o si un campo obligatorio queda vacio, el proyecto/motor queda DELIVERY_BLOCKED hasta corregir el ledger, recalcular SHA/manifests, reabrir ZIP final y ejecutar auditoria independiente completa.

## actual_value
validated_files=2; entries_per_file=49; required_fields=8; missing=0
