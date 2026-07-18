# IA-IDUNEX-M04-PrimerProyectoPiloto-20260717-v1-EN_REVISION

**Tipo:** Informe de Auditoría Documental M04 (piloto controlado)  
**Código:** AUD-019  
**Fecha:** 2026-07-17  
**Motor evaluado:** IDUNEX v1.0.0  
**Estado del motor:** `MOTOR_STATUS=EN_REVISION` (sin cambios)  

---

## 1. Resultado ejecutivo

**Resultado de fase:** `M04_PASS`  
**Clasificación de estado global del motor:** `EN_REVISION` (se mantiene; no hay cierre oficial).

Se ejecutó el primer proyecto piloto controlado **`IDUNEX_M04_PILOTO_001`** fuera del repositorio, con generación, validación, update y migrate en PASS, sin contaminación del motor ni cambios de gobernanza, sin release y sin tags.

---

## 2. Contexto de control aplicado

- Flujo ejecutado exclusivamente con IDUNEX.
- Base auditada confirmada en `main`:
  - `HEAD = f4a4583ee305b2ce385690eebd3ad099ff8d4f0b`
  - `main = f4a4583ee305b2ce385690eebd3ad099ff8d4f0b`
  - Commit corresponde al merge de PR #33 (AUD-018).
- Árbol inicial limpio: `git status --porcelain` vacío.
- No se modificó `governance/CURRENT_STATE.json`.
- No se modificó `engine/IDUNEX/`.

---

## 3. Evidencia de ejecución del piloto

### 3.1 Generación controlada (fuera del repo)

- Nombre piloto: `IDUNEX_M04_PILOTO_001`
- Ruta de trabajo externa: `C:\temp\idunex_m04_pilot_001\`
- Proyecto generado:
  - `C:\temp\idunex_m04_pilot_001\generated\IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0`
- ZIP generado:
  - `C:\temp\idunex_m04_pilot_001\generated\IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0.zip`
- Companion generado:
  - `C:\temp\idunex_m04_pilot_001\generated\IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0.zip.sha256`
- SHA256 ZIP:
  - `88ea66ecfdf8e3160e3c0b08948ffef529cf5c90aa0781500a42b8a50a3004dc`
- Companion contiene el SHA del ZIP: **PASS**.

### 3.2 Validaciones del proyecto piloto

- `generate`: **PASS** (`result=PASS`, `delivery_status=DELIVERY_PASS`).
- `validate` del factory sobre directorio del proyecto: **PASS** (`validators_fail=0`, `blocking_warnings=0`).
- `validate` del factory sobre ZIP + companion (reapertura): **PASS** (`validators_fail=0`, `blocking_warnings=0`).
- Nota de gobernanza técnica:
  - Invocar `VALIDATE_IDUNEX_PROJECT.py` directamente retorna `BLOCKED_NON_AUTHORITATIVE_ENTRYPOINT` / `FAIL_AUD_009_DIRECT_SUBVALIDATOR_INVOCATION` por diseño de AUD-009; por ello la validación aplicable del piloto se tomó vía entrypoint canónico del factory.

### 3.3 Update / Migrate

- `update-project`: **PASS**  
  - `delivery_status=DELIVERY_ALLOWED`
  - `validators_fail=0`
  - `fail_codes=[]`
- `migrate-project --target-engine v1.0.0`: **PASS**  
  - `delivery_status=MIGRATION_REAL_OUTPUT_PASS`
  - `validators_fail=0`
  - `fail_codes=[]`

---

## 4. Verificaciones de no contaminación

- `engine/IDUNEX/` sin cambios (`git diff --name-only -- engine/IDUNEX` vacío): **PASS**.
- `governance/CURRENT_STATE.json` sin cambios:
  - hash antes = `9dea20040f3f4e4e523df71eb2251d04aabafba4f6f6ff46b87cca43750f0d83`
  - hash después = `9dea20040f3f4e4e523df71eb2251d04aabafba4f6f6ff46b87cca43750f0d83`
  - **PASS**.
- No se generó `Proyecto 000 Demo`: **PASS** (0 coincidencias).
- No se creó release: **PASS** (antes 0, después 0).
- No se creó tag: **PASS** (antes 0, después 0).

---

## 5. Verificación de separación ENGINE / PROJECT / AGENT

Separación validada por:

1. `VALIDATE_IDUNEX_RUNTIME.py` en **PASS** (`validators_fail=0`, `fail_codes=[]`), incluyendo controles activos de aislamiento de superficies de runtime/agent.
2. Proyecto materializado en superficies diferenciadas de nivel de proyecto y agente (`00_PROJECT_INDEX`, `01_CANON`, `02_MODELS`, `03_AGENTS`, `09_MANIFESTS_SHA`, `10_RELEASE`), sin escritura en `engine/IDUNEX`.

Resultado: **PASS**.

---

## 6. Re-ejecuciones de validación del motor

- Runtime validator del motor (`VALIDATE_IDUNEX_RUNTIME.py`): **PASS**.
- Intake Audit local (`tools/audit/intake_audit.py --repo-root .`): **PASS** (`result=PASS`).

---

## 7. Matriz de cumplimiento de tareas solicitadas

| # | Control solicitado | Estado |
|---|---|---|
| 1 | Confirmar commit auditado de `main` | PASS |
| 2 | Confirmar árbol inicial limpio | PASS |
| 3 | Ejecutar generación piloto desde factory oficial | PASS |
| 4 | Validar generación fuera del repo | PASS |
| 5 | Validar estructura completa del proyecto | PASS |
| 6 | Validar ZIP + companion SHA | PASS |
| 7 | Validar proyecto con validator correspondiente | PASS |
| 8 | Validar separación ENGINE/PROJECT/AGENT | PASS |
| 9 | Validar `engine/IDUNEX/` sin cambios | PASS |
| 10 | Validar `governance/CURRENT_STATE.json` sin cambios | PASS |
| 11 | Validar que no se generó Proyecto 000 Demo | PASS |
| 12 | Validar que no se creó release | PASS |
| 13 | Validar que no se creó tag | PASS |
| 14 | Ejecutar `update-project` | PASS |
| 15 | Ejecutar `migrate-project` (aplica) | PASS |
| 16 | Re-ejecutar validator runtime del motor | PASS |
| 17 | Re-ejecutar Intake Audit local | PASS |
| 18 | Confirmar `git status` limpio salvo informe | PASS |

---

## 8. Conclusión de gobernanza

Se cumple **M04_PASS** para el primer piloto controlado `IDUNEX_M04_PILOTO_001` bajo restricciones de no contaminación.

El motor **permanece en `EN_REVISION`**.  
Este informe **no autoriza** release, tag, cambio a `OFICIAL` ni modificación de `governance/CURRENT_STATE.json`.
