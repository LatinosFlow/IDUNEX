# GOV-IDUNEX-AutorizacionEjecucionExternaProyecto000Demo-20260722-v1-EN_REVISION

**Tipo:** Autorización documental y machine-readable de ejecución externa única  
**ID:** `AUD-028`  
**Fecha:** `2026-07-22`  
**Versión:** `v1`  
**Estado documental:** `EN_REVISION`  
**Estado operativo:** `AUTHORIZED_NOT_CONSUMED`  
**Repositorio:** `LatinosFlow/IDUNEX`  
**Issue de control:** `#53`  
**Autoridad global:** `governance/CURRENT_STATE.json`  
**MOTOR_STATUS:** `EN_REVISION`  
**CREATIVE_OUTPUT_CERTIFIED:** `false`

---

## 1. Resumen ejecutivo

AUD-028 autoriza una sola ejecución externa del Proyecto 000 Demo en ChatGPT normal.
La autorización no habilita generación general, release, tag, `OFICIAL`, cierre productivo,
carga de agentes ni certificación creativa.

La ejecución deberá utilizar exactamente los tres adjuntos fijados por esta autorización.
El inicio de `generate` consume la autorización, incluso si la ejecución falla posteriormente.

**Decisión:**

`CONTROLLED_EXTERNAL_DEMO_EXECUTION_AUTHORIZED_NOT_CONSUMED`

---

## 2. Autoridad técnica

| Campo | Valor |
|---|---|
| Base de autorización | `main@98f13b62e0e0635d675fa1fb936ecc51c6c67bcc` |
| Paquete source commit | `53a235461a99c37cda7e2fc6c4bd31df4b5bd736` |
| Motor | 981 archivos / 47,302,063 bytes |
| Engine tree SHA-256 | `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9` |
| M02 | `M02_PASS_RECOMPUTED_POST_PR44` |
| M03 | `M03_PASS_RECOMPUTED_POST_PR44` |
| Motor status | `EN_REVISION` |

---

## 3. Tres adjuntos autorizados

### 3.1 Motor

- Filename: `IDUNEX_MOTOR_v1.0.0.zip`
- SHA-256: `53711cae748d3f8cda29e17d0a7663c3f73dbae6a691c82edfce704292cb2ac5`
- Entradas: `981`
- Bytes descomprimidos: `47,302,063`
- `testzip=PASS`

### 3.2 Informe Maestro

- Filename: `Informe Maestro - Gobernanza, Arquitectura y Políticas Oficiales del Motor IDUNEX.pdf`
- SHA-256: `1158d68f4863ead61c22472bc604a2aa32b475f4f3a6ed85d9e2d6d7d2d6708f`

### 3.3 Prompt canónico

- Ruta: `governance/authority/ACTIVO/IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO.txt`
- Filename operativo: `IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO.txt`
- Bytes UTF-8: `8982`
- SHA-256: `710b01f5603331f2a46f8fede16938e86b4577d3e0e5af2d68f2b50a284abc1f`
- Estado: `VALIDADO / AUTHORIZED_NOT_CONSUMED`

No se autoriza sustituir, completar o editar ninguno de los tres adjuntos.

---

## 4. Estado machine-readable

`governance/CURRENT_STATE.json` deberá registrar:

```text
status=AUTHORIZED_NOT_CONSUMED
authorized=true
consumed=false
execution_limit=1
execution_count=0
generate_executions_allowed=1
validate_executions_allowed=1
authorization_id=AUD-028
allowed_environment=CHATGPT_NORMAL_EXTERNAL
```

La capacidad general permanece bloqueada:

```text
ready_for_project_demo_generation=false
general_project_generation_enabled=false
release_authorized=false
tag_authorized=false
productive_closure_authorized=false
creative_output_certified=false
```

---

## 5. Preflight sin consumo

Antes de `generate`, la sesión debe:

1. Leer íntegramente los tres adjuntos.
2. Recalcular SHA-256 del motor, Informe Maestro y prompt.
3. Exigir coincidencia del motor e Informe con los valores autorizados.
4. Reportar el SHA recomputado del prompt para auditoría externa.
5. Validar ZIP, conteos, tree SHA, ausencia de rutas inseguras y temporales.
6. Confirmar el input completo del Demo.
7. Confirmar los bloqueos no-release.

Si el preflight falla:

`DEMO_REGENERATION_BLOCKED`

No se consume la autorización y no se ejecuta `generate`.

---

## 6. Regla de consumo

La autorización se consume al comenzar `generate`.

Después de ese punto:

- no se permite repetir `generate`;
- `validate` puede ejecutarse como máximo una vez si existe ZIP candidato;
- un fallo, timeout o limitación del entorno no habilita reintento;
- la evidencia debe conservarse y el estado deberá transicionar posteriormente a `CONSUMED`.

---

## 7. Gates requeridos

- `generate_rc=0`
- `validate_rc=0`
- `result=PASS`
- `validators_fail=0`
- `blocking_warnings=0`
- `fail_codes=[]`
- ZIP `testzip=PASS`
- companion SHA coincide
- artefactos externos `5/5`
- content-tree sincronizado
- fidelity mismatches `0`
- duplicate count consistente
- `H160_ATOMIC_PROJECT_FINALIZER=PASS`
- Runtime ChatGPT `12`
- Runtime Copilot `12`
- Agent-load surfaces `10/10` por plataforma
- Profile360 `61/61` por modelo
- TechExt `284/284` por modelo
- `MODEL_REGISTRY=PASS`
- `NO_DRIFT_LEDGERS=PASS`
- `CREATIVE_OUTPUT_CERTIFIED=false`

---

## 8. Decisiones permitidas

La sesión solo puede declarar:

- `DEMO_GENERATION_PASS_PENDING_INDEPENDENT_AUDIT`
- `DEMO_GENERATION_FAIL`
- `DEMO_EN_REVISION`
- `DEMO_REGENERATION_BLOCKED`

No puede declarar `PROJECT_AUDIT_PASS`, `PROJECT_AGENT_LOAD_PASS`, release, tag, `OFICIAL`,
cierre productivo ni certificación creativa.

---

## 9. Reversión y consumo posterior

Antes de ejecutar, la reversión consiste en no fusionar este PR o revertirlo por completo.

Después de iniciar `generate`, no se revierte a `AUTHORIZED_NOT_CONSUMED`. Debe emitirse una
actualización separada a `CONSUMED`, con evidencia de la sesión y sin modificar el motor.

---

## 10. Estado final de esta autorización

- `AUD028_STATUS=EN_REVISION`
- `AUD028_OPERATIONAL_STATUS=AUTHORIZED_NOT_CONSUMED`
- `EXECUTION_LIMIT=ONE`
- `DEMO_EXECUTION_AUTHORIZED=true`
- `GENERAL_PROJECT_GENERATION_ENABLED=false`
- `RELEASE_AUTHORIZED=false`
- `TAG_AUTHORIZED=false`
- `OFICIAL_AUTHORIZED=false`
- `PRODUCTIVE_CLOSURE_AUTHORIZED=false`
- `AGENT_LOAD_AUTHORIZED=false`
- `CREATIVE_OUTPUT_CERTIFIED=false`
