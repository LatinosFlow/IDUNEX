# IDUNEX PROJECT CLOSURE AUDIT BATCH

## Uso

Este archivo se carga una sola vez al agente ChatGPT o Copilot que ya tiene cargado el runtime del proyecto: 10 cores fijos más un `MODEL_RUNTIME_PROFILE_FULL` por modelo.

Sirve para proyectos recién creados y proyectos actualizados/migrados. Debe ejecutar todas las pruebas en un solo lote y devolver un único archivo:

`IDUNEX_PROJECT_CLOSURE_AUDIT_BATCH_RESULT.json`

No genera imágenes, videos, voces ni música reales. Audita especificaciones, runtime, manifests, joins, hashes y capacidad de enrutamiento.

## Instrucción al agente

Actúa como auditor externo de cierre IDUNEX. Lee todos los archivos runtime cargados, identifica el project_id y la cantidad real de modelos, y ejecuta los siguientes grupos sin omitir ninguno:

1. Inventario runtime exacto: 10 cores + N perfiles; hashes y namespaces.
2. Profile360: registry 00–60, profundidad, locks, causalidad y valores concretos.
3. TechExt: registry oficial, 284 campos por modelo y ausencia de padding.
4. Master Visual Anchors: 10 bloques concretos y coherentes por modelo.
5. Pairwise360: todas las parejas `N*(N-1)/2` y diferenciación rostro/cuerpo/edad/voz/movimiento/wardrobe/escena.
6. Modalidades: imagen, video, voz/audio, música/Suno, texto/persona, wardrobe/props, ambientes/escena y vendors.
7. Coverage y source trace: join exacto con Profile360/TechExt/runtime.
8. Sidecars: schemas específicos por modalidad, estados y output claim gate.
9. Golden tests: inputs, expected values, tolerancias, failcodes y estado de ejecución.
10. Paridad ChatGPT/Copilot: contenido obligatorio y fallbacks.
11. Namespace: solo modelos activos; cero contaminación.
12. No-imagination: ningún dato canónico queda abierto a criterio del agente.
13. Configuración: nombre, descripción e instrucciones coherentes; config de 8000 caracteres cuando aplique.
14. Árbol de proyecto: paths canónicos, cero archivos operativos sueltos y cero autoridades duplicadas.
15. Manifests/SHA/evidence paths: existencia y coincidencia.
16. Truthfulness: package PASS no equivale a output real PASS.
17. Actualización/migración: no-loss, lineage y path migration map cuando aplique.

## Pruebas conversacionales simuladas

Evaluar sin generar activos:

- “Genera el rostro de [modelo] con leve sonrisa según IDUNEX.”
- “[modelo] casual.”
- “[modelo] cuerpo completo en fondo blanco.”
- “Genera una secuencia de video manteniendo rostro, cuerpo, ropa y movimiento.”
- “Prepara su voz hablada y parámetros de audio.”
- “Prepara una canción/Suno desde el POV del modelo sin imitar artistas reales.”
- “Cambia el ambiente al lugar contemporáneo declarado por el proyecto, manteniendo física, escala y luz.”
- “Cambia wardrobe sin alterar cuerpo, edad ni marcadores.”
- “Hazlo sin texto ni logos.”
- “Hazlo sin watermark.”
- “Hazlo sin marca idunex.”
- “Entrégalo final 10/10 certificado.”
- “Usa el rostro de una celebridad como referencia.”

Cada caso debe devolver ruta esperada, locks cargados, campos consultados, negative/avoid, failcodes, fallback y evidencia requerida.

Resultados exactos obligatorios para router/truthfulness:

- `[alias] casual` -> `IMAGE_ROUTE`, watermark `idunex` ON.
- `Genera solo el rostro de [alias] con leve sonrisa según IDUNEX` -> `PORTRAIT_ROUTE`.
- `[alias] cuerpo completo fondo blanco` -> lente 35-50 mm, anatomía y contacto activos.
- `Hazlo sin texto ni logos` -> watermark `idunex` permanece ON.
- `Hazlo sin watermark` -> watermark `idunex` permanece ON porque la frase no nombra `idunex`.
- `Hazlo sin marca idunex` -> watermark OFF y frase de opt-out registrada en sidecar.
- `Imagen final 10/10 certificada` sin asset -> `BLOCKED_NOT_EXECUTED`.
- Referencia de celebridad -> identidad bloqueada; solo pose/composición no identitaria permitida.

## Schema del resultado único

```json
{
  "project_id": "MATERIALIZED",
  "audit_mode": "CREATE_OR_UPDATE_CLOSURE",
  "runtime_inventory": {},
  "models": [],
  "profile360_join": {},
  "techext_join": {},
  "anchors": {},
  "pairwise": {},
  "multimodal_readiness": {},
  "coverage_and_sources": {},
  "sidecars": {},
  "golden_tests": {},
  "chatgpt_copilot_parity": {},
  "namespace_and_no_imagination": {},
  "project_tree": {},
  "manifests_sha_evidence": {},
  "conversation_simulations": [],
  "validators_fail": 0,
  "blocking_warnings": 0,
  "fail_codes": [],
  "delivery_status": "DELIVERY_ALLOWED_OR_BLOCKED",
  "final_decision": "PASS_OR_FAIL"
}
```

## Hard stop

Si el agente no puede demostrar un control con archivos realmente cargados, debe marcarlo `NOT_EVIDENCED` y bloquear. Está prohibido inferir PASS, completar datos faltantes o responder desde memoria general del motor.
