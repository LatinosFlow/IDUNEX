# AUD-009 — Consolidación de validator único autoritativo

## Estado de control

- `MOTOR_STATUS=EN_REVISION`
- `M02_RESULT=M02_FAIL`
- Proyecto Demo no generado.
- Release y tag no creados.
- Este cambio no decide M02 ni acepta un PASS declarado.

## Autoridad aplicada

El Informe Maestro exige validator único y prohíbe validators paralelos. El
Informe M02 identifica `B-07`: 21 scripts de validación/implementación entre 24
scripts Python activos en su corte auditado, un registry con 114 validators y
ningún ejecutable único efectivo. La base apilada vigente incorpora cambios
posteriores al corte y contiene 25 scripts Python activos. El plan M02 exige un
solo entrypoint público, checks secundarios no ejecutables como cierre global y
una prueba adversarial.

## Inventario antes

Sobre la base apilada de `AUD-007`:

| Clase | Cantidad | Capacidad observada |
|---|---:|---|
| Scripts Python activos del motor en la base actual | 25 | Sin clasificación exhaustiva de autoridad |
| Supuesto entrypoint | 1 | `VALIDATE_IDUNEX_RUNTIME.py` |
| Otros `VALIDATE_*.py` | 21 | Ejecutables directos; varios emitían `PASS`/`FAIL` y código de salida |
| Comandos de dominio | 3 | Factory, runner de matriz y packer; alcance proyecto/paquete |
| Checks del registry QA | 114 | Checks internos confundidos con validators ejecutables |

Los scripts secundarios incluían cierres nominales (`ENGINE_CLOSURE`,
`FINAL_CERTIFICATE`) y validaciones de proyecto, schema, prompts, runtime y
evidencia. No se eliminó ninguna implementación funcional.

## Arquitectura después

La fuente de clasificación es
`07_VALIDATION_QA_GAUNTLET/22_QA_GAUNTLET_C_a85c6f84/VALIDATOR_SURFACE_REGISTRY.json`.

| Clase | Cantidad | Política |
|---|---:|---|
| Entrypoint global | 1 | `99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py` |
| Subvalidators | 21 | Solo por delegación del entrypoint; CLI directo bloqueado |
| Soporte interno | 1 | Protocolo de delegación; no es validator ni CLI público |
| Comandos de dominio | 3 | No pueden emitir cierre global del motor |
| Checks internos registry QA | 114 | Dispatch interno; cero entrypoints adicionales |

El entrypoint captura la salida del subcheck dentro de una envolvente
`SUBCHECK_DELEGATION`, conserva su código de salida y fail codes, y fija:

- `global_closure_authorized=false`;
- `m02_decision_authority=false`;
- resultado de envolvente distinto de `PASS` global.

La ejecución directa de un secundario termina con código `3`,
`BLOCKED_NON_AUTHORITATIVE_ENTRYPOINT` y
`FAIL_AUD_009_DIRECT_SUBVALIDATOR_INVOCATION`.

## Registros QA sincronizados

- El registry de 114 entradas queda definido como catálogo de checks internos.
- El canonical bridge queda definido como registry/orden, no como executable.
- Evidencia bajo histórico y `H261_H268_EVIDENCE` queda clasificada como
  evidencia, no autoridad vigente.
- `governance/authority/REFERENCIA/` y `docs/audits/` quedan como referencia no
  autoritativa para ejecución.
- Las herramientas de `tools/audit/` quedan registradas como checks de
  repositorio no autoritativos y no pueden cerrar el motor.

## Enforcement

`tools/audit/validator_entrypoint_check.py` falla cuando:

1. el registry contiene cero o más de un entrypoint;
2. un script Python activo del motor no está clasificado;
3. un subvalidator no tiene bloqueo de ejecución directa;
4. una superficie secundaria declara capacidad de cierre global;
5. un check activo de repositorio no está clasificado.

La prueba adversarial muta el registry con un segundo entrypoint y exige fallo.
Otra prueba ejecuta directamente los 21 secundarios y exige bloqueo antes de
que corra su lógica.

## Evidencia ejecutada

| Comando/control | Resultado |
|---|---|
| `governance_state_check.py --repo-root .` | `CONSISTENT`; `EN_REVISION`; `M02_FAIL`; 0 contradicciones activas |
| `validator_entrypoint_check.py --repo-root .` | `CONSISTENT`; 1 entrypoint; 21 subvalidators; 22 scripts `VALIDATE*.py`; 26 superficies Python clasificadas |
| Mutación de segundo entrypoint | Rechazada por el scanner |
| CLI directo de los 21 secundarios | Bloqueado con rc=3 y sin autoridad global |
| Delegación de subcheck por entrypoint | Ejecutada bajo `SUBCHECK_DELEGATION`; sin autoridad global |
| `intake_audit.py --repo-root .` | PASS de intake; 0 failures |
| `python -m unittest discover -s tests/intake -p 'test_*.py'` | 22 pruebas; OK; 1 skip preexistente |
| Ejecución read-only de `VALIDATE_IDUNEX_RUNTIME.py` | rc=1 / `FAIL`; 4 bloqueantes preservados; `global_closure_authorized=false`; `M02_FAIL`; salida sin `M02_PASS` |

Los cuatro fallos del entrypoint global son
`ACTIVE_VALIDATORS_EXACT_SET`, `DOCUMENT_TRUTHFULNESS_PARITY_H245_H260`,
`DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY` y
`FAIL_INTERNAL_MANIFEST_STALE_OR_INCOMPLETE`. No se convierten en PASS ni se
corrigen aquí: incluyen paridad/manifest final fuera del alcance de `AUD-009`.

La inspección de archivos no rastreados y artefactos no encontró Proyecto Demo,
ZIP de motor, release ni tag creados por esta tarea.

## Fuera de alcance preservado

- No se corrigieron bloat/no-history.
- No se regeneraron baseline ni manifiestos finales.
- No se modificó lógica Demo en `AUD-009`.
- No se creó Proyecto Demo, release o tag.
- `EN_REVISION` y `M02_FAIL` permanecen vigentes.
