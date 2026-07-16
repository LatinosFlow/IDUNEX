# GLOBAL_FIELD_DICTIONARY_RULES — IDUNEX MOTOR v1.0.0

## Propósito
Reglas comunes heredables para diccionarios Profile360. Este archivo evita duplicación de relleno sin perder contenido operativo.

## GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
- Permitido: valor explícito del canon, rango declarado en proyecto, default documentado por motor, gap registrado si no existe dato
- Prohibido: inventar canon silenciosamente, usar promedio genérico, mezclar rasgos de otro modelo, contradecir anchor oficial, usar evidencia FAIL como identidad
- Depende de: project_canon, model_profile, identity_lock, qa_gate, source_trace
- Afecta: prompt, camera, lighting, voice, movement, wardrobe, scene, qa, sidecar

## Regla de herencia
Cada diccionario debe declarar `inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS` y conservar su delta específico por campo: definition, source_trace, required_fields, allowed_values específico, forbidden_values específico, depends_on específico, affects específico, qa_rule, fail_code, fallback_fix, sidecar_field, project_core_rule, chatgpt_rule y copilot_rule.

## No-loss
La extracción a regla global no elimina criterio; traslada repetición exacta a autoridad común y mantiene deltas en los archivos derivados.
