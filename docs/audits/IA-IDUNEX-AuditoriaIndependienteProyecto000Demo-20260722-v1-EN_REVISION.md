# IA — Auditoría independiente del Proyecto 000 Demo

**Estado:** `EN_REVISION`  
**Proyecto:** `IDUNEX_PROJECT_PROYECTO_000_DEMO_v1.0.0`  
**Autorización:** `AUD-028 — CONSUMED`  
**Issue correctivo:** `#58`

## Decisión ejecutiva

```text
ZIP_OPERATIONAL_VALIDATION=PASS
PROJECT_AUDIT_PASS=FALSE
PROJECT_AUDIT_DECISION=PROJECT_AUDIT_FAIL_EXTERNAL_SURFACE_DESYNC
PROJECT_AGENT_LOAD_PASS=FALSE
PROJECT_READY_FOR_PRODUCTION=FALSE
CREATIVE_OUTPUT_CERTIFIED=FALSE
MOTOR_STATUS=EN_REVISION
```

## Identidad del paquete

- ZIP SHA-256: `539cc5b7077e12025deefa0304525a9aa8bfaa627a4d408cf01127e8beb8460b`
- ZIP bytes: `1,380,284`
- Entradas: `304`
- Bytes descomprimidos: `12,298,443`
- `testzip=PASS`
- companion SHA: coincide
- JSON válidos: `229/229`
- entradas `ZIP_STORED`: `0`
- directorios explícitos: `0`
- rutas inseguras: `0`
- symlinks: `0`
- entradas cifradas: `0`

## Gates recomputados

- Runtime ChatGPT: `12/12`.
- Runtime Copilot: `12/12`.
- Agent-load surfaces ChatGPT: `10/10`.
- Agent-load surfaces Copilot: `10/10`.
- Profile360: `61/61` por modelo.
- TechExt: `284/284` por modelo.
- Anchors: `10/10` por modelo.
- Prompt packs A-J: completos en 8 modalidades.
- Duplicados físicos: 5 grupos; allowlist exacta.
- Vale resuelve solo a Valeria Rios Andrade.
- Mateo resuelve solo a Mateo Vargas Salinas.
- Colisiones de alias: `0`.

## Validator independiente

Se ejecutó nuevamente el factory canónico en modo `validate` sobre el ZIP final y su companion.

```text
RC=0
result=PASS
validation_scope=FINAL_REOPENED_ZIP
delivery_status=DELIVERY_ALLOWED
validators_fail=0
blocking_warnings=0
fail_codes=[]
```

El host emitió un warning de inicialización de `artifact_tool` anterior al validator. No modificó el RC ni el JSON PASS del validator IDUNEX.

## Hallazgo bloqueante — AUD030-EXT-SURFACE-DESYNC

El content-tree final recomputado desde `09_MANIFESTS_SHA/PROJECT_PACKAGE_SHA256SUMS.txt` es:

```text
806a308dbefb650687b35d034bd90133997ebb5a3598ae78b41e6f5cb4dc3b35
```

Coincide con:

- `10_RELEASE/FINAL_AUDIT_REPORT.md` interno;
- `10_RELEASE/RELEASE_CERTIFICATE.txt` interno;
- `09_MANIFESTS_SHA/POST_EXPORT_FINALIZER_REPORT.json`;
- `09_MANIFESTS_SHA/PROJECT_REOPENED_ZIP_PROOF.json`.

Pero los dos artefactos externos adjuntos declaran el valor anterior:

```text
f37d5c761bd389e26d3cebfe73ea379d37421dd626b193517229892c1dc70386
```

Superficies afectadas:

1. `IDUNEX_PROJECT_PROYECTO_000_DEMO_v1.0.0_FINAL_AUDIT_REPORT.md`.
2. `IDUNEX_PROJECT_PROYECTO_000_DEMO_v1.0.0_RELEASE_CERTIFICATE.txt`.

Por tanto, la afirmación `content-tree post-finalizer sincronizado` no pasa para el set externo 5/5.

## Alcance

La auditoría no invalida la integridad operativa del ZIP. Invalida el cierre documental integral de la entrega externa.

Quedan bloqueados:

- `PROJECT_AUDIT_PASS`;
- carga de agentes;
- uso productivo;
- release o tag;
- promoción a `OFICIAL`;
- certificación creativa.

## Acción correctiva

1. Mantener AUD-028 en `CONSUMED` y sin reintento.
2. Corregir el orden de refresco de artefactos externos después de H410.
3. Añadir prueba de igualdad del content-tree interno/externo.
4. No editar ni regenerar manualmente el ZIP.
5. Emitir únicamente superficies documentales externas corregidas mediante flujo automatizado y autorizado.
6. Repetir auditoría independiente antes de cargar agentes.

## Reversión

Este documento y la transición a `CONSUMED` pueden revertirse como cambios documentales, pero la ejecución física de `generate` no puede desconsumirse ni habilitar un reintento.
