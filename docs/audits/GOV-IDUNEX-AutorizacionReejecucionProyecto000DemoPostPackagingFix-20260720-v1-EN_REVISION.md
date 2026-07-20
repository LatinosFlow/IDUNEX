# GOV-IDUNEX-AutorizacionReejecucionProyecto000DemoPostPackagingFix-20260720-v1-EN_REVISION

**Tipo:** Addendum documental de autorización operativa controlada
**ID:** AUD-024
**Fecha:** 2026-07-20
**Versión:** v1
**Estado:** `EN_REVISION`
**Repositorio:** `LatinosFlow/IDUNEX`
**Autoridad previa:** `AUD-023 v2`
**Commit técnico autorizado del motor:** `18be3cfc4704ecff7c0187548072de6541410313`
**Destino autorizado:** ChatGPT normal, fuera de GitHub

---

## 1. Resumen ejecutivo

AUD-024 documenta el cierre de la ejecución controlada autorizada por AUD-023 v2, que terminó en `DEMO_REGENERATION_BLOCKED`, y autoriza una única reejecución externa y controlada después de corregir exclusivamente la estructura del paquete operativo.

La ejecución anterior consumió su límite de una ejecución y terminó en `PRECHECK` antes de producir ZIP definitivo. No se ejecutó `validate`, no se creó entrega válida y no se modificaron el motor ni el input.

La causa fue una incompatibilidad de empaquetado:

- el factory busca la identidad no-release del motor en:
  - `governance/CURRENT_STATE.json`;
  - `governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json`;
  - `governance/baseline/IDUNEX_CURRENT_TREE_SHA256.txt`;
- el paquete ejecutado ubicó esos archivos en:
  - `02_AUTORIDAD/governance/...`.

La corrección autorizada es estructural y no modifica código, contratos, validators, schemas, templates, motor ni input.

---

## 2. Resultado de la ejecución consumida

- Decisión: `DEMO_REGENERATION_BLOCKED`
- Etapa: `PRECHECK`
- `generate_rc=1`
- `validate` ejecutado: `NO`
- ZIP definitivo producido: `NO`
- Directorio de salida válido: `NO`
- Root cause: `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`
- Fail secundario: `FAIL_H160_ATOMIC_FINALIZE_NOT_REACHED`
- Detalle: `certificate engine sha invalid`
- `CREATIVE_OUTPUT_CERTIFIED=false`
- `MOTOR_STATUS=EN_REVISION`

La evidencia de esta ejecución debe conservarse como `REFERENCIA_FORENSE` y no constituye PASS vigente.


### Evidencia forense de la ejecución bloqueada

- Resumen de ejecución SHA-256:
  `a251f44cd8def6387b9bb85531122c5956baf0651255236a412ba4586117884a`
- GenerateResult SHA-256:
  `9ed3a429dacacc16592994e34dd1d05bec47268b9c0ccff109e63fa3210c9429`
- stdout SHA-256:
  `5ec816d8acd19597527b3ce2ef615f58901ddcd9857dc94a858da2d5ddb81686`
- stderr SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Preconditions SHA-256:
  `5513686d82bab11e994b3fd2d460c7785cf23967fd87cd9345409ab2b4778424`

---

## 3. Autoridad técnica preservada

La reejecución debe conservar exactamente:

- Motor autorizado:
  `18be3cfc4704ecff7c0187548072de6541410313`
- Árbol SHA-256 del motor:
  `0165188a1d598bdbaab6c53f880208ef2a2f1af9e86fe6a91ffa61730d78d666`
- Archivos del motor:
  `981`
- Bytes del motor:
  `47,295,010`
- Input:
  `IDUNEX-Project000-Demo-Input-20260717-v1-EN_REVISION.json`
- SHA-256 del input:
  `801055FEB1D2BE3E932B99C71E38FEDAC612B4D106B2959439E935C5F8AF3B34`

No se autoriza reconstruir, modificar, completar ni sustituir el input.

---

## 4. Corrección estructural autorizada

El nuevo paquete debe incluir en su raíz:

```text
governance/
  CURRENT_STATE.json
  baseline/
    IDUNEX_CURRENT_TREE_MANIFEST.json
    IDUNEX_CURRENT_TREE_SHA256.txt
```

Estos archivos deben ser copias byte a byte de las superficies vigentes de `main`.

No se autoriza resolver el problema mediante:

- modificación del factory;
- hardcode de un SHA dentro del código;
- sustitución del tree SHA por un release SHA;
- cambio de `CURRENT_STATE.json`;
- alteración de variables de entorno fuera del paquete y prompt autorizados;
- modificación del motor;
- uso de una identidad histórica o no vigente.

El paquete puede conservar Informe Maestro, AUD-023, AUD-024 y evidencia bajo `02_AUTORIDAD`, pero la gobernanza operacional requerida por el factory debe estar en la ruta raíz `governance/...`.

---

## 5. Preflight obligatorio sin consumir la reejecución

Antes de ejecutar `generate`, se debe verificar:

1. Integridad ZIP y manifiesto del paquete.
2. SHA-256 exacto del input.
3. Conteos y tree SHA del motor.
4. Existencia y hashes de las tres superficies raíz de gobernanza.
5. Que `resolve_engine_zip_sha256()` devuelva exactamente:
   `0165188a1d598bdbaab6c53f880208ef2a2f1af9e86fe6a91ffa61730d78d666`.
6. Que el valor sea hexadecimal de 64 caracteres.
7. Que `CURRENT_STATE.json` conserve:
   - `motor_status=EN_REVISION`;
   - `release_authorized=false`;
   - `tag_authorized=false`;
   - `productive_closure_authorized=false`;
   - `creative_output_certified=false`.

La verificación del resolver no equivale a ejecutar `generate` y no consume el límite autorizado.

Si cualquier control falla: `DEMO_REGENERATION_BLOCKED` sin ejecutar `generate`.

---

## 6. Alcance autorizado

Después de aprobar el preflight, se autoriza una única reejecución para:

1. Ejecutar `generate` una sola vez.
2. Conservar stdout, stderr, código de salida y resultado JSON.
3. Si existe ZIP definitivo, ejecutar `validate` una sola vez.
4. Reabrir el ZIP definitivo.
5. Recomutar SHA-256 y companion.
6. Custodiar los cinco artefactos externos canónicos.
7. Preparar la entrega para reauditoría externa independiente.

---

## 7. Criterios técnicos requeridos

- `generate_rc=0`
- `validate_rc=0`
- `result=PASS`
- `delivery_status=DELIVERY_ALLOWED`
- `validators_fail=0`
- `blocking_warnings=0`
- `fail_codes=[]`
- ZIP `testzip=PASS`
- Companion SHA `PASS`
- Artefactos externos `5/5`
- Runtime ChatGPT `12`
- Runtime Copilot `12`
- Agent-load ChatGPT `10/10`
- Agent-load Copilot `10/10`
- Vale resuelve únicamente a Valeria Rios Andrade
- Mateo resuelve únicamente a Mateo Vargas Salinas
- `MODEL_REGISTRY=PASS`
- `NO_DRIFT_LEDGERS=PASS`
- Profile360 `61/61` por modelo
- TechExt `284/284` por modelo
- `CREATIVE_OUTPUT_CERTIFIED=false`

---

## 8. Restricciones duras

No se autoriza:

- modificar `main` fuera de este documento;
- modificar el motor;
- modificar `governance/CURRENT_STATE.json`;
- crear release o tag;
- declarar `MOTOR_STATUS=OFICIAL`;
- declarar cierre productivo;
- declarar `PROJECT_AUDIT_PASS`;
- cargar el proyecto en agentes;
- declarar certificación creativa;
- repetir `generate` después de consumir la ejecución autorizada;
- reutilizar la salida parcial bloqueada;
- inventar SHA, archivos, estados o resultados.

---

## 9. Evidencia obligatoria

Conservar:

1. Paquete ejecutado y SHA-256.
2. Manifiesto interno.
3. Preflight del resolver SHA.
4. Input y SHA-256.
5. Motor, conteos y tree SHA.
6. Comando generate.
7. stdout, stderr y RC.
8. GenerateResult.
9. Comando validate, si aplica.
10. ValidateResult, si aplica.
11. ZIP, companion y cinco artefactos externos, si aplica.
12. Resumen de ejecución.
13. Evidencia de la ejecución bloqueada anterior como `REFERENCIA_FORENSE`.

---

## 10. Ruta posterior

`AUD-024 MERGED → paquete estructural corregido → preflight resolver PASS → una reejecución → validate → reauditoría externa independiente`

Solo la reauditoría externa puede declarar `PROJECT_AUDIT_PASS`.

---

## 11. Decisión documental

Se autoriza:

`CONTROLLED_DEMO_REEXECUTION_POST_PACKAGING_FIX`

Límite:

`ONE`

La autorización entra en vigor únicamente después del merge de AUD-024 a `main` y de la validación del paquete corregido.

---

## 12. Estado final

- `AUD024_STATUS=EN_REVISION`
- `AUD024_PR_STATUS=PENDING_MERGE`
- `PRIOR_CONTROLLED_EXECUTION_STATUS=CONSUMED_BLOCKED`
- `PRIOR_BLOCK_ROOT_CAUSE=FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE`
- `PACKAGING_FIX_CLASS=STRUCTURE_ONLY`
- `ENGINE_CODE_CHANGED=false`
- `INPUT_CHANGED=false`
- `MOTOR_STATUS=EN_REVISION`
- `DEMO_REEXECUTION_AUTHORIZED=CONTROLLED_ONLY_AFTER_MERGE`
- `CONTROLLED_REEXECUTION_LIMIT=ONE`
- `AUTHORIZED_ENGINE_COMMIT=18be3cfc4704ecff7c0187548072de6541410313`
- `AUTHORIZED_ENGINE_TREE_SHA256=0165188a1d598bdbaab6c53f880208ef2a2f1af9e86fe6a91ffa61730d78d666`
- `AUTHORIZED_INPUT_SHA256=801055FEB1D2BE3E932B99C71E38FEDAC612B4D106B2959439E935C5F8AF3B34`
- `RELEASE_AUTHORIZED=false`
- `TAG_AUTHORIZED=false`
- `OFICIAL_AUTHORIZED=false`
- `PROJECT_AUDIT_PASS_AUTHORIZED=false`
- `AGENT_LOAD_AUTHORIZED=false`
