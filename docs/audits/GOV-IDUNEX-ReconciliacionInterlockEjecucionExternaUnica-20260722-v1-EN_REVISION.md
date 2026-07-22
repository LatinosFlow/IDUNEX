# GOV-IDUNEX-ReconciliacionInterlockEjecucionExternaUnica-20260722-v1-EN_REVISION

**Tipo:** Reconciliación de gobernanza machine-readable  
**ID:** `AUD-029`  
**Fecha:** `2026-07-22`  
**Versión:** `v1`  
**Estado:** `EN_REVISION`  
**Repositorio:** `LatinosFlow/IDUNEX`  
**Issue de control:** `#54`  
**Issue padre:** `#53`  
**Autoridad global:** `governance/CURRENT_STATE.json`  
**Motor:** `EN_REVISION`  
**CREATIVE_OUTPUT_CERTIFIED:** `false`

---

## 1. Resumen ejecutivo

AUD-029 resuelve una contradicción de flujo sin habilitar todavía el Proyecto 000 Demo.

El motor debe completar una prueba externa controlada antes de cualquier evaluación productiva, pero la autoridad global vigente mantenía `PROJECT_DEMO_GENERATION` bloqueado de forma absoluta mientras `MOTOR_STATUS=EN_REVISION`. Una autorización exclusivamente narrativa no podía superar esa autoridad machine-readable.

Se implementa una máquina de estados separada y fail-closed para una futura ejecución externa única:

`controlled_external_demo_execution`

La capacidad general permanece bloqueada. El estado inicial es:

`PENDING_AUTHORIZATION`

Por tanto, esta implementación:

- no autoriza todavía la ejecución;
- no genera el Proyecto 000 Demo;
- no modifica `engine/IDUNEX`;
- no habilita release, tag, `OFICIAL`, cierre productivo ni carga de agentes;
- no certifica outputs creativos;
- permite que una autorización posterior quede expresada, validada y consumida de forma auditable.

**Determinación:**

`AUD029_SCHEMA_IMPLEMENTED_PENDING_AUTHORIZATION`

---

## 2. Autoridad técnica de inicio

| Campo | Valor |
|---|---|
| Base commit | `53a235461a99c37cda7e2fc6c4bd31df4b5bd736` |
| Scope motor | `engine/IDUNEX` |
| Archivos motor | `981` |
| Bytes motor | `47,302,063` |
| Engine tree SHA-256 | `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9` |
| M02 | `M02_PASS_RECOMPUTED_POST_PR44` |
| M03 | `M03_PASS_RECOMPUTED_POST_PR44` |
| Motor package SHA-256 | `53711cae748d3f8cda29e17d0a7663c3f73dbae6a691c82edfce704292cb2ac5` |
| Informe Maestro SHA-256 | `1158d68f4863ead61c22472bc604a2aa32b475f4f3a6ed85d9e2d6d7d2d6708f` |
| Estado global | `EN_REVISION` |

El paquete del motor fue generado mediante GitHub Actions run `29884622077` y validado como candidato reproducible, no como release.

---

## 3. Contradicción original

La autoridad global declaraba simultáneamente:

1. `MOTOR_STATUS=EN_REVISION`;
2. `ready_for_project_demo_generation=false`;
3. `PROJECT_DEMO_GENERATION` dentro de `denied_capabilities`;
4. una regla que impedía a certificados internos habilitar el Demo mientras el motor siguiera en revisión.

El flujo de cierre exige, sin embargo, una prueba externa controlada del Proyecto 000 Demo antes de evaluar promoción productiva.

La solución no puede ser:

- ignorar `CURRENT_STATE.json`;
- cambiar silenciosamente `ready_for_project_demo_generation` a `true`;
- declarar el motor `OFICIAL`;
- usar un certificado narrativo como sustituto de la autoridad machine-readable;
- permitir ejecuciones repetibles o generales.

---

## 4. Alternativa elegida

Se adopta una excepción machine-readable acotada dentro de `CURRENT_STATE.json`.

Se mantiene:

- `motor_status=EN_REVISION`;
- `ready_for_project_demo_generation=false`;
- `PROJECT_DEMO_GENERATION` denegado como capacidad general;
- `release_authorized=false`;
- `tag_authorized=false`;
- `productive_closure_authorized=false`;
- `creative_output_certified=false`.

Se agrega:

`controlled_external_demo_execution`

Este objeto no habilita generación general. Solo modela una futura excepción externa, identificada por SHA y limitada a una ejecución.

---

## 5. Máquina de estados

### 5.1 `PENDING_AUTHORIZATION`

Estado vigente después de este PR:

- `authorized=false`;
- `consumed=false`;
- `execution_limit=1`;
- `execution_count=0`;
- `generate_executions_allowed=0`;
- `validate_executions_allowed=0`;
- `authorization_id=null`;
- `prompt_path=null`;
- `prompt_sha256=null`.

Decisión:

`DEMO_EXECUTION_NOT_AUTHORIZED`

### 5.2 `AUTHORIZED_NOT_CONSUMED`

Solo una futura autorización documental y machine-readable puede activar este estado. Debe exigir:

- `authorized=true`;
- `consumed=false`;
- `execution_limit=1`;
- `execution_count=0`;
- `generate_executions_allowed=1`;
- `validate_executions_allowed` igual a `0` o `1`;
- `authorization_id` obligatorio;
- commit Git obligatorio;
- engine tree SHA obligatorio;
- package SHA obligatorio;
- Informe Maestro SHA obligatorio;
- prompt activo y prompt SHA obligatorios;
- todas las prohibiciones no-release en `false`.

### 5.3 `CONSUMED`

Después de la única ejecución:

- `authorized=false`;
- `consumed=true`;
- `execution_count=1`;
- `generate_executions_allowed=0`;
- `validate_executions_allowed=0`.

La autorización consumida no puede reutilizarse.

---

## 6. Scanner y validación

`tools/audit/governance_state_check.py` valida:

- estados permitidos;
- SHA-256 en formato hexadecimal de 64 caracteres;
- commit Git de 40 caracteres hexadecimales;
- límite de ejecución igual a uno;
- prohibición de generación general;
- incompatibilidad entre `authorized=true` y `consumed=true`;
- ausencia de permisos de release, tag, `OFICIAL`, cierre, agentes o certificación creativa;
- contratos exactos de cada estado;
- permanencia de `ready_for_project_demo_generation=false`.

El scanner continúa rechazando cualquier intento de habilitación general del Demo.

---

## 7. Pruebas requeridas

La implementación incorpora pruebas para:

1. repositorio vigente consistente;
2. `PENDING_AUTHORIZATION` válido;
3. `AUTHORIZED_NOT_CONSUMED` completo válido;
4. autorización sin prompt SHA rechazada;
5. SHA inválido rechazado;
6. estado autorizado y consumido simultáneamente rechazado;
7. `execution_limit > 1` rechazado;
8. generación general habilitada rechazada;
9. `ready_for_project_demo_generation=true` rechazado;
10. `CONSUMED` válido;
11. superficie rogue con readiness declarativo rechazada.

Los checks de PR deben confirmar Intake y Security antes del merge.

---

## 8. Archivos afectados

Modificados:

1. `governance/CURRENT_STATE.json`;
2. `tools/audit/governance_state_check.py`;
3. `tests/intake/test_governance_state.py`;
4. `README.md`;
5. `GOVERNANCE_STATUS.md`;
6. `REPOSITORY_MANIFEST.yml`.

Creado:

7. `docs/audits/GOV-IDUNEX-ReconciliacionInterlockEjecucionExternaUnica-20260722-v1-EN_REVISION.md`.

No modificado:

- `engine/IDUNEX`;
- factory;
- validator del motor;
- empaquetador;
- prompt del Demo;
- releases;
- tags.

---

## 9. Plan de consumo

La autorización futura debe:

1. fijar el prompt activo y su SHA;
2. fijar la autorización AUD-028;
3. cambiar el estado a `AUTHORIZED_NOT_CONSUMED` mediante PR separado;
4. pasar CI;
5. fusionarse antes de abrir el chat de ejecución;
6. permitir una sola ejecución externa;
7. registrar evidencia de consumo;
8. cambiar el estado a `CONSUMED` mediante PR posterior;
9. impedir cualquier repetición.

---

## 10. Reversión

Si este esquema presenta un defecto:

1. revertir el PR completo;
2. restaurar el `CURRENT_STATE.json` anterior;
3. confirmar que `engine/IDUNEX` conserva 981 archivos, 47,302,063 bytes y tree SHA autorizado;
4. mantener bloqueada la ejecución del Demo;
5. no reutilizar autorizaciones parciales.

La reversión no requiere modificar el motor.

---

## 11. Estado final

- `AUD029_STATUS=EN_REVISION`
- `AUD029_SCHEMA=IMPLEMENTED_PENDING_PR_REVIEW`
- `CONTROLLED_EXTERNAL_DEMO_STATUS=PENDING_AUTHORIZATION`
- `CONTROLLED_EXTERNAL_DEMO_AUTHORIZED=false`
- `CONTROLLED_EXTERNAL_DEMO_CONSUMED=false`
- `EXECUTION_LIMIT=1`
- `GENERATE_EXECUTIONS_ALLOWED=0`
- `DEMO_EXECUTION_AUTHORIZED=false`
- `READY_FOR_PROJECT_DEMO_GENERATION=false`
- `RELEASE_AUTHORIZED=false`
- `TAG_AUTHORIZED=false`
- `OFICIAL_AUTHORIZED=false`
- `PRODUCTIVE_CLOSURE_AUTHORIZED=false`
- `AGENT_LOAD_AUTHORIZED=false`
- `CREATIVE_OUTPUT_CERTIFIED=false`

**Veredicto:**

`AUD029_SCHEMA_IMPLEMENTED_PENDING_AUTHORIZATION`
