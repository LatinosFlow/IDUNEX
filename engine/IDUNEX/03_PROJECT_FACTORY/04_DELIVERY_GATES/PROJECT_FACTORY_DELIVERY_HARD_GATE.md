# PROJECT_FACTORY_DELIVERY_HARD_GATE

Motor: IDUNEX_MOTOR_v1.0.0  
Internal label: P034_PROJECT_ENTITY_BRAND_LOGO_IMAGE_DELIVERY_SAFE_APPAREL_CANONICAL_REOPEN  
Status: ACTIVE_BLOCKING

Este hard gate preserva la linea historica no autoritativa previa y agrega `PROJECT_DELIVERY_BY_CONTRACT_NOT_COUNT_GATE`.

## Regla
No se permite `DELIVERY_ALLOWED` por conteo superficial. Cada proyecto debe pasar los 16 gates contractuales del Project Factory Contract Validator activo con `actual_value` concreto y evidencia.

## Gana la auditoria independiente
Si una auditoria independiente futura encuentra un FAIL equivalente, la entrega queda bloqueada hasta correccion quirurgica, rebuild de SHA/manifests, ZIP reabierto y reauditoria completa.
