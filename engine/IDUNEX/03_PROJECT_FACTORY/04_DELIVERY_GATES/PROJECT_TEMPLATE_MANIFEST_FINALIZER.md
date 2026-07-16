# PROJECT_TEMPLATE_MANIFEST_FINALIZER - P0.2-004

Engine: IDUNEX_MOTOR_v1.0.0
Fecha: NEUTRALIZED_ACTIVE_SCOPE
Estado: ACTIVE_BLOCKING

## Regla
Despues de cualquier cambio en config, runtime core, profile template, source ledger, golden tests, vendor checklist u output provenance, el Project Factory debe recalcular manifests del template antes de generar el ZIP del motor.

## Cobertura minima
- `CHATGPT/MANIFESTS/SHA256SUMS.txt`
- `COPILOT/MANIFESTS/SHA256SUMS.txt`
- `PROJECT_PACKAGE_SHA256SUMS.txt`
- `PROJECT_PACKAGE_MANIFEST.json`
- Manifests runtime internos dentro de `IDUNEX_PROJECT_TEMPLATE_v1.0.0`
- Manifests de Agent Factory copiados a proyectos

## Gate
Si cualquier manifest del template queda desactualizado, el delivery se bloquea y se reemite el template antes del ZIP final.
