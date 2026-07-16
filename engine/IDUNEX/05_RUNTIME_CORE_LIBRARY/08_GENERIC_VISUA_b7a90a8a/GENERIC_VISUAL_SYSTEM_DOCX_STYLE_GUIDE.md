# generic visual system DOCX Style Guide 10/10

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


generic visual system es la capa visual documental y de presentación de PROJECT_BRAND_ENTITY aplicada a IDUNEX. No modifica identidad de modelos. Gobierna documentos, reportes, diagramas, tablas, portadas, watermark, QA visual y consistencia corporativa.

## Tokens de marca PROJECT_BRAND_ENTITY
- Primary: PROJECT_BRAND_PRIMARY_COLOR
- Secondary: PROJECT_BRAND_SECONDARY_COLOR
- Accent: PROJECT_BRAND_ACCENT_COLOR
- Text: PROJECT_BRAND_TEXT_COLOR
- Background: PROJECT_BRAND_BACKGROUND_COLOR
- Contrast pair: PROJECT_BRAND_CONTRAST_PAIR_AA
- Fallback documental no autoritativo: NEUTRAL_DOC_PRIMARY / NEUTRAL_DOC_ACCENT / NEUTRAL_DOC_TEXT / NEUTRAL_DOC_BACKGROUND, pendientes de resolución por proyecto.

**BRD-PAL-001:** esta superficie genérica no contiene valores hex reales de marca ni paletas de proyectos como default activo. Los valores reales se resuelven exclusivamente desde `PROJECT_BRAND_REGISTRY` del proyecto generado o desde input externo autorizado. Si no existe registro autorizado, se conserva el token semántico pendiente y se bloquea cualquier materialización de paleta concreta en runtime activo.

## Reglas
1. Contraste mínimo AA con PROJECT_BRAND_CONTRAST_PAIR_AA.
2. Títulos con jerarquía clara.
3. Tablas legibles y sin saturación.
4. Diagramas con flujo motor → proyecto → modelo → prompt/sidecar → QA.
5. Watermark interno no debe contaminar imagen limpia.
6. Portadas con naming limpio.
7. No usar marcas ajenas.
8. Estética premium, técnica y documental.

## H21 - Gobernanza de duplicados activos generic visual system

Los bloques repetidos `Regla generic visual system 01-80` quedan deduplicados canonicamente en una sola regla activa `GENERIC_VISUAL_SYSTEM_STYLE_RULE_CANONICAL_001`. Las numeraciones historicas no son entradas activas independientes, no aumentan autoridad, no deben contarse como coverage adicional y no pueden ocultar drift semantico.

### GENERIC_VISUAL_SYSTEM_STYLE_RULE_CANONICAL_001
Aplicar identidad PROJECT_BRAND_ENTITY con jerarquia visual, espacios, contraste AA, paleta controlada, tabla legible y consistencia de exportacion. Si el documento es para Copilot, usar headings, tablas pequenas, matrices y glosarios. Si es reporte QA, priorizar claridad de PASS/FAIL. Si es diagrama, mantener lectura izquierda a derecha o top-down, sin mezclar identidad visual con canon fisico de modelos.

**Duplicate governance:** `ACTIVE_MAP_DUPLICATE_ENTRY_GOVERNANCE_GATE=ACTIVE_VALIDATED`; `dedupe_keep_first_preserve_order`; duplicados textuales activos removidos; futuras repeticiones deben justificarse con `canonical_rule_id`, `reason` y `runtime_effect`, o bloquearse.
