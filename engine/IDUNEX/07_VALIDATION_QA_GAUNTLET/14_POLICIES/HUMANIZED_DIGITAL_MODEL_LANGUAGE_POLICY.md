# HUMANIZED DIGITAL MODEL LANGUAGE POLICY — IDUNEX v1.0.0

## Runtime creativo permitido
- modelo humano digital IDUNEX
- persona digital humanizada
- modelo digital con identidad operativa propia
- identidad digital canonizada
- modelo editorial digital
- modelo con Profile360
- IDUNEX_HUMANIZED_DIGITAL_VALIDATION_MODEL_001

## Términos técnicos legacy
Cualquier término heredado tipo avatar vacío, maniquí, doll realism, fake person o synthetic label queda restringido a auditoría técnica y debe marcarse como: [TECHNICAL_LEGACY_TERM_NOT_CREATIVE_RUNTIME]
TECHNICAL_LEGACY_TERM_NOT_CREATIVE_RUNTIME

## Runtime productivo
Los prompt packs, sidecars, QA, outputs de prueba y outputs reales deben usar lenguaje humanizado. El validator `VALIDATE_FORBIDDEN_CREATIVE_TERMS_ALL_RUNTIME_OUTPUTS` bloquea las frases heredadas en capas de salida runtime.

Updated UTC: NEUTRALIZED_ACTIVE_SCOPEZ

## NEGATIVE / AVOID - etiqueta permitida no creativa
NEGATIVE_AVOID_ALLOWED_NOT_CREATIVE_IDENTITY_LABEL

Regla quirúrgica:
- FAIL: usar términos heredados como descripción creativa o identidad del modelo.
- PASS: usar términos como `muñeco`, `muñeca`, `doll realism`, `maniquí`, `fake person` o equivalentes solo dentro de NEGATIVE / AVOID, fail examples, QA técnico o política, siempre marcados con `NEGATIVE_AVOID_ALLOWED_NOT_CREATIVE_IDENTITY_LABEL`. [NEGATIVE_AVOID_ALLOWED_NOT_CREATIVE_IDENTITY]
- La etiqueta no autoriza lenguaje de identidad; solo evita falsos positivos cuando el término está usado como error a bloquear.
