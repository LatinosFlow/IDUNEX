# CONFIG_8000_SEMANTIC_DENSITY_GATE

Motor: IDUNEX_MOTOR_v1.0.0  
Internal label: LEGACY_NON_AUTHORITY  
Estado: ACTIVE_BLOCKING

## Correccion de falso positivo
El validador distingue referencia normativa anti-padding de padding real. No cuenta como filler: fail codes, nombres de gates, metricas, `no padding loops`, `repeated_padding_blocks = 0` ni reglas que prohiben padding.

## Si cuenta como filler
Lineas identicas repetidas, bloques repetidos para llegar a 8000 caracteres, loops textuales, texto semánticamente vacio, repeticiones artificiales y duplicados sin autoridad funcional.

## Metricas obligatorias
- normative_padding_reference_count
- actual_padding_loop_count
- repeated_line_max
- repeated_block_max
- filler_ratio
- semantic_sections_count
- required_tokens_present

## Bloqueos
`BLOCKED_CONFIG_8000_VALIDATOR_FALSE_POSITIVE`, `BLOCKED_CONFIG_8000_PADDING_LOOP`, `BLOCKED_CONFIG_8000_BY_CONTENT_FAIL`.
