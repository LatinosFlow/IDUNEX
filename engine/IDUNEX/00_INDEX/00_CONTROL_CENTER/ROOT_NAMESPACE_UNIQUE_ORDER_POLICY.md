# ROOT_NAMESPACE_UNIQUE_ORDER_POLICY - P0.2-001

Engine: IDUNEX_MOTOR_v1.0.0
Fecha: NEUTRALIZED_ACTIVE_SCOPE
Estado: BLOCKING_POLICY_ACTIVE

## Regla principal
En la raiz del ZIP IDUNEX no puede existir mas de una carpeta con el mismo prefijo numerico `NN_`. La regla tambien aplica por sibling scope: dentro de un mismo parent directory no puede repetirse el mismo `NN_` entre carpetas hermanas.

## Alcance obligatorio
- Root namespace completo del motor.
- Subdirectorios con prefijo numerico entre hermanos.
- Project Factory templates, Agent Factory, runtime packs, proyectos demo y subpaquetes.
- Manifests, SHA ledgers, documentation, certificates, configs y reportes derivados.

## Politica no-loss
Renombrar o mover carpetas solo para corregir orden y unicidad. No eliminar contenido valido. Si una ruta cambia, se deben reescribir referencias internas, recalcular manifests/hashes y reauditar desde el ZIP final reabierto.

## Criterio de bloqueo
`ENGINE_FINAL_RELEASE_GATE` queda bloqueado si root prefix duplicates > 0 o sibling prefix duplicates bloqueantes > 0.
