## Phase 3 file-level inheritance
inherits = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RESEARCH_LANDING_RULE
inherits_runtime_qa = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RUNTIME_QA_BLOCK
research_specific_extracts_preserved = true

# Research Runtime Library — Wardrobe, bodywear editorial adulto, props, materiales y física textil

**Motor:** IDUNEX_MOTOR_v1.0.0_20260614  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**Fecha de generación:** 20260613  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.



Define vestuario como identidad material y cultural: paleta, fit, tela, costura, caída, soporte, props, contacto físico y restricciones.

## Fuentes vinculadas

- **SRC_003_Antropometr_a_corporal_avanzada** | Dominio: body_age_anthropometry | Palabras: 4644 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: corporal, grasa, mujeres, hombros, muscular, ejemplo, altura, hombres, estatura, cuerpo.
- **SRC_016_Lencer_abodywear_editorial_adulto_no_expl_cito** | Dominio: body_age_anthropometry | Palabras: 1429 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: lencería, modelos, explícito, ejemplo, encaje, contenido, prenda, editorial, cualquier, poses.
- **SRC_019_Motion_bible_y_caminada** | Dominio: body_age_anthropometry | Palabras: 6732 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: movimiento, marcha, movimientos, pasos, puede, vídeo, ejemplo, hacia, cuerpo, brazos.
- **SRC_020_Acting_bible** | Dominio: body_age_anthropometry | Palabras: 7223 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: actuación, personaje, avatar, plano, mirada, escena, emoción, ejemplo, gestos, emociones.
- **SRC_034_Wardrobe_premium_por_modelo_y_cuerpo** | Dominio: body_age_anthropometry | Palabras: 7399 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: imagen, cuerpo, arrugas, prenda, contenido, poses, vestuario, ejemplo, calidad, evitar.
- **SRC_035_Acting_poses_y_microgestos_por_personalidad** | Dominio: body_age_anthropometry | Palabras: 12962 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: poses, gestos, mirada, sonrisa, manos, personalidad, corporal, guías, puede, creativas.
- **SRC_039_BODY_BEAUTY_FITNESS_EDITORIAL_NON_EXPLICIT** | Dominio: body_age_anthropometry | Palabras: 6577 | Se migra como: reglas, campos, QA, fallbacks y tests. Keywords: persona, sección, personaje, idunex, texto, imagen, generación, estilo, modelos, personas.

## Campos derivados


### Grupo operativo: wardrobe

| `wardrobe_signature` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `color_palette` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `silhouette_preference` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fabric_preferences` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fabric_weight` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fabric_texture` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `fit_rules` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `seam_visibility` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `drape_behavior` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wrinkle_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `support_physics` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `layering_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `season_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `occasion_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `body_shape_fit_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wardrobe_story_logic` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: bodywear

| `bodywear_editorial_limits` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `swimwear_editorial_limits` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `lingerie_non_explicit_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `adult_context_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `no_exploitation_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `camera_angle_safety` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `pose_safety` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `styling_alternative_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `commercial_safe_rewrite` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: props

| `accessory_rules` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `jewelry_limit` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_material` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_weight` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_scale` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `hand_object_contact` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `object_shadow_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brand_logo_restrictions` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_scene_coherence` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `object_continuity_video` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_lineage_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

### Grupo operativo: qa

| `floating_cloth_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `texture_flat_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wrong_style_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `brand_logo_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `unsupported_bodywear_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `prop_physics_blocker` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `wardrobe_identity_drift_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |
| `material_repair_rule` | Convertir en descriptor/canon/rango, conectado a salida real. | Bloquear drift, falta de dato, contradicción o promedio genérico. | Reforzar campo, añadir negative/avoid, registrar gap y crear regression test. |

## Reglas y casos

**Regla 01 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 02 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 03 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 04 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 05 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 06 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 07 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 08 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 09 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 10 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 11 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 12 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 13 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 14 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

**Regla 15 — Wardrobe, bodywear editorial adulto, props, materiales y física textil**: todo agente debe transformar este dominio en campo verificable. No basta declarar intención; debe existir impacto en prompt, sidecar, QA y fallback. Si una salida falla, se registra fail code, se aplica reparación y se ejecuta re-test. Ejemplo de control: no aceptar descripciones genéricas, no usar datos ausentes, no migrar evidencia no canon a identidad, no omitir relación con cámara/luz/movimiento/voz/wardrobe/escena.

#### Caso operativo 1: wardrobe
**Entrada coloquial:** el usuario pide un output que afecta wardrobe.  
**Acción del motor:** cargar Perfil360, filtrar campos `wardrobe_signature, color_palette, silhouette_preference, fabric_preferences, fabric_weight`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 2: bodywear
**Entrada coloquial:** el usuario pide un output que afecta bodywear.  
**Acción del motor:** cargar Perfil360, filtrar campos `bodywear_editorial_limits, swimwear_editorial_limits, lingerie_non_explicit_rule, adult_context_rule, no_exploitation_rule`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 3: props
**Entrada coloquial:** el usuario pide un output que afecta props.  
**Acción del motor:** cargar Perfil360, filtrar campos `accessory_rules, jewelry_limit, prop_material, prop_weight, prop_scale`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

#### Caso operativo 4: qa
**Entrada coloquial:** el usuario pide un output que afecta qa.  
**Acción del motor:** cargar Perfil360, filtrar campos `floating_cloth_blocker, texture_flat_blocker, wrong_style_blocker, brand_logo_blocker, unsupported_bodywear_blocker`, construir prompt creativo limpio, separar sidecar técnico, ejecutar QA y devolver fallback fixes.  

## Extractos transformados de investigación

### Extracto transformado 001
**Hallazgo fuente:** --- SOURCE: Antropometr a corporal avanzada ---
Canon corporal realista para modelos
de IA adultos en Latinoamérica
(IDUNEX – PROJECT_BRAND_ENTITY)
Nota: No se encontraron referencias internas especíﬁcas sobre IDUNEX o
PROJECT_BRAND_ENTITY en las búsquedas, por lo que esta investigación se basa en fuentes
públicas ﬁables y estudios relevantes.




### Extracto transformado 002
**Hallazgo fuente:** Crear modelos de IA con cuerpos humanos realistas requiere fundamentar
sus proporciones y características en datos antropométricos y principios
cientíﬁcos.




### Extracto transformado 003
**Hallazgo fuente:** Para un entorno latinoamericano (tomando a PROJECT_DECLARED_COUNTRY como
referencia central y comparando con variaciones regionales), se deﬁnen a
continuación los parámetros corporales clave, variaciones demográﬁcas
por edad, sexo y estilo de vida, la metodología de modelado para traducir
datos físicos a modelos digitales (con poses, movimiento, ropa y cámara),
normas para evitar fallos de realismo físico y pruebas de validación
(“golden tests”) de los modelos generados.




### Extracto transformado 004
**Hallazgo fuente:** Parámetros antropométricos completos para
adultos
Altura y peso: Los adultos latinoamericanos suelen tener estaturas
promedio algo menores que las de poblaciones europeas o norteamericanas.




### Extracto transformado 005
**Hallazgo fuente:** En PROJECT_DECLARED_COUNTRY, estudios recientes (2019) reportan una estatura media de ~1.65 m
en hombres y 1.53 m en mujeres, mientras los promedios para
Latinoamérica (8 países) rondan los 1.71 m en varones y 1.58 m en
mujeres 1 .




### Extracto transformado 006
**Hallazgo fuente:** Estas medidas reﬂejan inﬂuencias genéticas (fuerte ascendencia
indígena andina en PROJECT_DECLARED_COUNTRY) y factores socioeconómicos (nutrición infantil, salud
pública) 2 .




### Extracto transformado 007
**Hallazgo fuente:** En comparación, la media global de estatura es cercana a 1.71 m
en hombres y 1.59 m en mujeres, situando a la población latina ligeramente
por debajo de la media mundial.




### Extracto transformado 008
**Hallazgo fuente:** Rangos realistas: La distribución de estaturas en Latinoamérica es amplia;
un 90% de los hombres latinoamericanos miden aproximadamente entre ~158
cm (5° percentil) y ~183 cm (95° percentil), y las mujeres entre ~146 cm y
~170 cm (5° y 95° percentil, respectivamente) 1 .




### Extracto transformado 009
**Hallazgo fuente:** En diseño antropométrico se
suelen usar estos percentiles extremos (5° y 95°) para dimensionar
productos y espacios socavando el 90% central de la población 2 .




### Extracto transformado 010
**Hallazgo fuente:** desórdenes de crecimiento, deportistas extremos) y por tanto
servirían para modelos particulares, no para un “canon” general.




### Extracto transformado 011
**Hallazgo fuente:** Los project-declareds son en promedio más bajos, con ~165 cm los
hombres y ~153 cm las mujeres, frente a ~171/158 cm en Latinoamérica 1 y
~171/159 cm a nivel mundial.




### Extracto transformado 012
**Hallazgo fuente:** El Índice de Masa Corporal (IMC) proporciona
un indicador integrado de constitución: en Latinoamérica se ubica típicamente
en rango de sobrepeso para un adulto medio (25 ≤ IMC < 30).




### Extracto transformado 013
**Hallazgo fuente:** En
efecto, cerca de el 42% de la población project-declared adulta tiene sobrepeso (IMC
≥ 25 pero < 30) y alrededor de 22% sufre obesidad (IMC ≥ 30) 4 , cifras
acordes con el promedio latinoamericano (obesidad ~25% en la región según
estudio ELANS de 8 países) 4 .




### Extracto transformado 014
**Hallazgo fuente:** Estos datos de alto peso relativo reﬂejan
condiciones nutricionales y estilos de vida urbanos cambiantes en las últimas
décadas, con dietas más calóricas e inactividad física creciente 5 .




### Extracto transformado 015
**Hallazgo fuente:** No obstante,
al deﬁnir un canon realista típicamente se opta por representar un cuerpo en
normopeso (IMC ~22–24), con variantes ajustables hacia contextos de ﬁguras




### Extracto transformado 016
**Hallazgo fuente:** más corpulentas (IMC ~27) o más esbeltas (IMC ~20) según se requieran
ejempliﬁcaciones de diferentes perﬁles.




### Extracto transformado 017
**Hallazgo fuente:** Composición corporal (músculo y grasa): La composición (% de músculo y
grasa) varía por sexo, edad y entrenamiento.




### Extracto transformado 018
**Hallazgo fuente:** De media, el hombre adulto
tiene aproximadamente 38% de su peso en masa muscular (músculo
esquelético) y las mujeres ~31% 6 .




### Extracto transformado 019
**Hallazgo fuente:** En ambos sexos, la masa muscular alcanza
su cenit a ﬁn de la juventud (veintitantos años) y declina con la edad, más
aceleradamente en hombres 6 (véase sección 2).




### Extracto transformado 020
**Hallazgo fuente:** Simultáneamente, el
porcentaje de grasa corporal suele crecer: un varón adulto en peso normal
suele tener ~15–20% de grasa corporal; en la mujer es más elevado, ~20–30%
(parte del dimorﬁsmo sexual humano).




### Extracto transformado 021
**Hallazgo fuente:** En individuos deportistas
(especialmente atletas de rendimiento), la proporción de grasa puede bajar
hasta ~10–12% en varones o ~18–22% en mujeres, con la masa muscular
incrementándose en consecuencia.




### Extracto transformado 022
**Hallazgo fuente:** La diferencia sexual en la composición
corporal es ﬁsiológica: los hombres tienen mayor masa magra y densidad
ósea (inﬂuencia de testosterona) mientras las mujeres tienden a acumular
tejido adiposo en caderas, muslos y mamas por efecto estrogénico.




### Extracto transformado 023
**Hallazgo fuente:** Somatotipos (tipologías corporales): La población real presenta
variabilidad en la forma corporal que suele clasiﬁcarse en tres somatotipos
principales: (1) Ectomorfo: delgado, extremidades largas, poca masa
muscular/grasa; (2) Mesomorfo: atlético, musculoso y proporcionado; (3)
Endomorfo: tendencia a mayor adiposidad, constitución más robusta.




### Extracto transformado 024
**Hallazgo fuente:** ej., a partir de un modelo base mesomorfo
promedio, se podrá ajustar hacia un fenotipo más ectomorfo (reduciendo
circunferencias musculares y peso) o más endomorfo (aumentando depósitos
adiposos y formas redondeadas) según la aplicación.




### Extracto transformado 025
**Hallazgo fuente:** Dimensiones corporales (proporciones relativas): Para un realismo
convincente, es crucial preservar relaciones proporcionales humanas típicas.




### Extracto transformado 026
**Hallazgo fuente:** Reglas clásicas como la ﬁgura de “7.5–8 cabezas” de altura por persona
adulta proporcionan un punto de partida: un modelo idealizado mide unas 8
veces la longitud de su propia cabeza 7 .




### Extracto transformado 027
**Hallazgo fuente:** Ancho de hombros: un varón adulto
de estatura media (~170 cm) presenta hombros de ~45 cm (≈ 26% de su
altura), en tanto una mujer de ~160 cm tiene hombros de ~39 cm (≈ 24% de




### Extracto transformado 028
**Hallazgo fuente:** La cadera femenina suele ser notablemente más ancha en proporción
(similar o mayor que los hombros), mientras la cadera masculina es más
estrecha (≈ 80% de la anchura de hombros, aportando la silueta en forma de
“V”) 7 .




### Extracto transformado 029
**Hallazgo fuente:** La relación cintura-cadera es un índice clave: típicamente ~0.85–0.95
en hombres y ~0.70–0.80 en mujeres, reﬂejando un tronco más rectilíneo en
varones y una forma de “reloj de arena” en mujeres.




### Extracto transformado 030
**Hallazgo fuente:** Otras relaciones
prototípicas: piernas ~ 50% de la estatura total (longitud de pierna medida
desde cadera hasta pie), torso ~ 30% de la altura, pies ~ 15% de la altura, y
manos ~ 10% de la altura (p.




### Extracto transformado 031
**Hallazgo fuente:** La
circunferencia de cuello adulta oscila en ~35–38 cm en varones y ~30–34 cm
en mujeres, valores que correlacionan con la composición corporal (un cuello
>39 cm en varón se asocia a obesidad central) 6 .




### Extracto transformado 032
**Hallazgo fuente:** Estas proporciones servirán
de guía para calibrar cada segmento corporal en los modelos de IA,
asegurando que su físico tenga una coherencia interna: por ejemplo, si
aumentamos la anchura de hombros para un somatotipo mesomorfo, debe
mantenerse en equilibrio con la circunferencia de pecho y brazos, para no
crear una morfología inverosímil.




### Extracto transformado 033
**Hallazgo fuente:** Variaciones por edad, sexo/género,
entrenamiento y estilo de vida
Ciclos de edad adulta: El aspecto corporal varía notablemente a lo largo de
la vida adulta.




### Extracto transformado 034
**Hallazgo fuente:** En el adulto joven (20–35 años), se alcanza la cúspide física:
los músculos están plenamente desarrollados (pudiendo constituir ~40% del
peso en varones jóvenes; ~30% en mujeres 6 8 ) y la grasa corporal se
mantiene en niveles bajos (10–20% en hombres; 18–28% en mujeres).




### Extracto transformado 035
**Hallazgo fuente:** La
fuerza y densidad ósea son máximas alrededor de los 30 años y la piel es
uniforme y ﬁrme, con alta elasticidad y sin pérdida de tono visible.




### Extracto transformado 036
**Hallazgo fuente:** Hacia la
franja de 36–55 años, surgen cambios graduales: descenso lento de masa
muscular (en hombres ~1–2% por año tras los 50; en mujeres ~0.5–1%
anual) 6 , y un aumento progresivo en grasa corporal central (grasa visceral
en abdomen y perivisceral).




### Extracto transformado 037
**Hallazgo fuente:** Por ejemplo, a los 50 años un hombre puede
haber perdido ~4–5 kg de músculo en comparación con sus 20s 6 , y acumulado
grasa abdominal, aumentando su perímetro de cintura unos centímetros.




### Extracto transformado 038
**Hallazgo fuente:** En la
madurez tardía (más de 55–60 años), se aceleran la sarcopenia (pérdida
muscular, ~1% anual de masa muscular en la sexta década) y la reducción de




### Extracto transformado 039
**Hallazgo fuente:** estatura (por cambios en columna y discos intervertebrales, ~1–2 cm por
década tras los 40–50 años).




### Extracto transformado 040
**Hallazgo fuente:** Los hombres mayores pueden perder peso
corporal total ligeramente tras los 60 (por disminución hormonal, densidad
ósea y masa magra), y las mujeres mayores tras la menopausia experimentan
cambios en la densidad ósea y distribución de grasa (más acumulación central
al disminuir estrógenos).




### Extracto transformado 041
**Hallazgo fuente:** Diferencias por sexo (biológicas): Los hombres y mujeres exhiben rasgos
corporales distintos desde la pubertad: los varones son por lo general más
altos y de complexión más musculosa (particularmente tronco superior),
con espalda y hombros más anchos y pelvis estrecha 7 .




### Extracto transformado 042
**Hallazgo fuente:** Tienen huesos más
densos y metabolismo basal más alto (debido mayor masa magra), lo que
facilita menor porcentaje de grasa.




### Extracto transformado 043
**Hallazgo fuente:** Las mujeres, en promedio, son más bajas
y de contextura menos muscular; presentan hombros más estrechos y una
pelvis más ancha (adaptada a la gestación) 7 , acumulando más grasa
subcutánea en ca




### Extracto transformado 044
**Hallazgo fuente:** --- SOURCE: Lencer abodywear editorial adulto no expl cito ---
Lineamientos para la representación
de lencería mediante modelos de IA
sintéticos adultos (Guía Integral)
La representación de lencería, ropa interior, bikinis y bodywear con
modelos sintéticos generados por IA es un campo emergente que requiere
un enfoque 360 grados para garantizar que el contenido sea editorial,
elegante, no explícito y comercialmente seguro.




### Extracto transformado 045
**Hallazgo fuente:** En esta guía abordamos los
aspectos creativos, técnicos, legales-comerciales y de control de calidad.




### Extracto transformado 046
**Hallazgo fuente:** Cada sección contiene directrices detalladas, tablas y ejemplos prácticos, con
un lenguaje técnico enfocado en moda y publicidad.




### Extracto transformado 047
**Hallazgo fuente:** Respalda el cumplimiento de estándares profesionales de
la industria de la moda y la publicidad, incluyendo políticas de plataformas
como Amazon, Google Ads e Instagram.




### Extracto transformado 048
**Hallazgo fuente:** Límites visuales y de contenido
Objetivo: Establecer qué se considera “editorial, elegante, no explícito y
seguro” y reclasiﬁcar visualmente qué está estrictamente prohibido.




### Extracto transformado 049
**Hallazgo fuente:** Garantizar que las representaciones de lencería con IA se mantengan dentro
de límites claros de decoro.




### Extracto transformado 050
**Hallazgo fuente:** Amazon, en sus directrices, exige que las poses no sean
sugerentes: modelos sin abrir demasiado las piernas, ojos abiertos, boca
cerrada, brazos relajados y sin cubrir estratégicamente partes íntimas 1 .




### Extracto transformado 051
**Hallazgo fuente:** Diseño y realismo de las prendas
Objetivo: Asegurar que las prendas generadas por IA (sujetadores, panties,
bikinis, bodies) sean visualmente realistas, en términos de diseño, ajuste,
materiales, comportamiento de telas, costuras, elasticidad, compresión,
así como transparencias manejadas de forma segura (sheerness controlada).




### Extracto transformado 052
**Hallazgo fuente:** Esto garantizará que, aunque el modelo sea sintético, la prenda se perciba real
y bien confeccionada, tal como lo haría en una sesión fotográﬁca profesional.




### Extracto transformado 053
**Hallazgo fuente:** --- SOURCE: Motion bible y caminada ---
Control de pasos y equilibrio          Personalidad en el
En una marcha realista, el cuerpo      movimiento
alterna soportando peso en cada        La forma de caminar revela
pie.




### Extracto transformado 054
**Hallazgo fuente:** Cada paso debe mostrar un         personalidad: movimientos
apoyo ﬁrme del pie con el suelo,       amplios y rítmicos indican
seguido de un despegue, mientras       conﬁanza; pasos suaves y lentos
el centro de gravedad se desplaza      reﬂejan calma; gestos ﬂuidos y
suavemente de un lado a otro.




### Extracto transformado 055
**Hallazgo fuente:** El       miradas sutiles sugieren seducción;
cuerpo desciende ligeramente al        postura erguida y controlada
recibir el peso (pose down) y luego    transmite profesionalidad; un
asciende al impulsarse con la punta    andar suelto con cambios de ritmo
del pie (pose up), evitando que el     parece casual y urbano; una
personaje parezca ﬂotar sin peso.




### Extracto transformado 056
**Hallazgo fuente:** Ropa y calzado inﬂuyen en la           Prompts detallados para
marcha                                 capturar el movimiento
Tacones altos obligan a acortar la     Para guiar un modelo de vídeo IA,
zancada e inclinar el cuerpo           describe el sujeto, la acción y el
ligeramente hacia adelante,            entorno de forma narrativa y
requiriendo equilibrio extra en        precisa.




### Extracto transformado 057
**Hallazgo fuente:** movimiento, mientras que ropa          “sin jitter ni extremidades
suelta y calzado deportivo permiten    deformes”).




### Extracto transformado 058
**Hallazgo fuente:** Informe: Movimiento Humano
Realista en Modelos de IA para Vídeo
Resumen ejecutivo:
Para generar un movimiento humano convincente en vídeos creados por IA, es
indispensable integrar conocimientos de biomecánica real con técnicas
avanzadas de ingeniería de prompts y herramientas de control.




### Extracto transformado 059
**Hallazgo fuente:** Este
informe presenta una guía práctica y técnica para lograr movimientos
realistas y corregir las posibles distorsiones típicas de los modelos
generativos.




### Extracto transformado 060
**Hallazgo fuente:** A lo largo del informe se proporcionan recomendaciones especíﬁcas apoyadas
por fuentes técnicas de biomecánica y animación y por experiencias de la
industria, cada una debidamente referenciada.




### Extracto transformado 061
**Hallazgo fuente:** Esto servirá tanto a creadores
prácticos (que buscan consejos de implementación en sus herramientas de
IA), como a desarrolladores técnicos (interesados en la fundamentación).




### Extracto transformado 062
**Hallazgo fuente:** Análisis básico de la marcha (gait analysis)
aplicado a IA
El gait analysis (análisis de la marcha) estudia la locomoción humana,
segmentando el ciclo de la marcha en fases con patrones bien deﬁnidos 1 .




### Extracto transformado 063
**Hallazgo fuente:** Un ciclo completo de marcha (desde que un pie contacta el suelo hasta que
vuelve a hacerlo) dura aproximadamente 1,0 – 1,2 segundos a velocidad normal
de caminata (unos 4 km/h) 2 .




### Extracto transformado 064
**Hallazgo fuente:** En este tiempo, un adulto sano suele dar cerca de
1–2 pasos por segundo, lo que se traduce en una cadencia promedio de 100 a
120 pasos por minuto 2 .




### Extracto transformado 065
**Hallazgo fuente:** Estudios indican que las mujeres presentan un ritmo
ligeramente mayor (~122 pasos/min de media) que los varones (~116 pasos/
min) al caminar cómodamente 2 .




### Extracto transformado 066
**Hallazgo fuente:** Brazo opuesto a pierna opuesta: La coordinación natural implica que,
cuando una pierna se adelanta, el brazo contrario también lo hace hacia
adelante, mientras el brazo del mismo lado va hacia atrás.




### Extracto transformado 067
**Hallazgo fuente:** Este balanceo de
los brazos ocurre para contrarrestar la rotación del tronco generada por las
piernas, manteniendo así el equilibrio del cuerpo 2 3 .




### Extracto transformado 068
**Hallazgo fuente:** Es importante describir
esta contracoordinación en prompts o guiarla con controladores de pose para
que el personaje no luzca estático o desequilibrado.




### Extracto transformado 069
**Hallazgo fuente:** Centro de gravedad (CG) y oscilaciones del tronco: Durante una marcha
natural, el CG del cuerpo sube y baja levemente en cada paso, adaptándose a




### Extracto transformado 070
**Hallazgo fuente:** En el instante del impacto del pie, el cuerpo baja un
poco por la ﬂexión de la rodilla(pose down), y luego se eleva durante la fase de
propulsión(pose up).




### Extracto transformado 071
**Hallazgo fuente:** Este sutil movimiento vertical reﬂeja la inﬂuencia de la
gravedad y la física: sin ello, la marcha pareciera antinatural, como si el sujeto
ﬂotara sin peso.




### Extracto transformado 072
**Hallazgo fuente:** Para capturar esto con IA, se puede añadir en la descripción
del movimiento que la persona “desciende ligeramente al apoyar cada
paso”, o que “sus hombros suben y bajan sutilmente al ritmo de la marcha”,
enfatizando la presencia de inercia y gravedad.




### Extracto transformado 073
**Hallazgo fuente:** Tronco, caderas, hombros y cabeza: Para mantener la estabilidad, el tronco
realiza contrarrotaciones: las caderas rotan suavemente hacia adelante
junto con la pierna que avanza, mientras que los hombros y la parte
superior del torso rotan en sentido opuesto, compensando la inercia 2 .




### Extracto transformado 074
**Hallazgo fuente:** La columna vertebral permanece erguida pero ﬂexible, evitando rigidez
excesiva y permitiendo la transferencia suave de peso.




### Extracto transformado 075
**Hallazgo fuente:** La cabeza suele
conservarse nivelada con relación al horizonte, con la mirada al frente, para
facilitar el equilibrio visual.




### Extracto transformado 076
**Hallazgo fuente:** Al describir la marcha en un prompt, conviene
mencionar “manteniendo la cabeza estable y mirada ﬁja hacia adelante” si el
modelo tiende a generar cabezas tambaleantes.




### Extracto transformado 077
**Hallazgo fuente:** En síntesis, la marcha realista requiere respetar los fundamentos
biomecánicos (apoyo, balanceo, centro de gravedad, cadencia, coordinación) y
comunicar estos elementos al modelo de IA mediante descripciones claras o
controladores apropiados.




### Extracto transformado 078
**Hallazgo fuente:** --- SOURCE: Acting bible ---
Biblia de Actuación para Modelos de
IA Sintéticos (Adultos)
La siguiente “biblia” de actuación integra métodos tradicionales de actuación
(teatro y cine) con perspectivas de psicología cognitiva, afectiva y semiótica
para modelos de IA sintéticos destinados a imagen, video y agentes
conversacionales con avatar.




### Extracto transformado 079
**Hallazgo fuente:** Se presentan los fundamentos actorales,
adaptaciones a distintos formatos, aspectos internos del personaje, esquemas
técnicos (JSON/TXT/DOCX), gramáticas de prompts, así como lineamientos de
control de calidad (QA) y pruebas por emoción y por plano.




### Extracto transformado 080
**Hallazgo fuente:** El objetivo es
lograr actuaciones auténticas, coherentes y creíbles, evitando la
sobreactuación o la “mirada vacía”, y garantizar consistencia en diversas
situaciones.




### Extracto transformado 081
**Hallazgo fuente:** La guía se estructura en secciones detalladas a continuación, con
ejemplos conceptuales y buenas prácticas.




### Extracto transformado 082
**Hallazgo fuente:** Fundamentos de la Actuación para IA:
presencia, intención, subtexto, reacción, timing,
silencios y mirada
Actuar con “presencia” escénica y verdad: Los modelos de IA actuantes
deben “estar presentes” en la escena con la misma intensidad que un actor
humano.




### Extracto transformado 083
**Hallazgo fuente:** Presencia escénica implica proyectar energía, credibilidad,
dominio del espacio y mantener una conexión con el público o
interlocutor 1 .




### Extracto transformado 084
**Hallazgo fuente:** Como en la actuación humana, la naturalidad surge de
involucrar cuerpo y mente: postura, gestos, expresiones y voz se coordinan en
coherencia con el personaje.




### Extracto transformado 085
**Hallazgo fuente:** Esto requiere empatía (entender y sentir las
circunstancias del personaje) y espontaneidad contenida (evitar lo robótico)
para transmitir una sensacióun genuina de estar ahí.




### Extracto transformado 086
**Hallazgo fuente:** Intención y objetivo narrativo: Toda acción y diálogo deben estar guiados
por un propósito dramático deﬁnido.




### Extracto transformado 087
**Hallazgo fuente:** En el acting clásico, “las acciones de
un personaje, aunque aparenten ser espontáneas, deben estar cargadas
de una intención que permita al observador recibir el mensaje
completo” 2 .




### Extracto transformado 088
**Hallazgo fuente:** Por ejemplo, en un diálogo, un avatar con intención
de persuadir a otro personaje mantendrá un tono cálido y abierto en su voz y
contacto visual constante, modulando su lenguaje corporal para reforzar su
propósito.




### Extracto transformado 089
**Hallazgo fuente:** La intención articulada internamente (lo que el personaje
realmente desea) debe reﬂejarse externamente mediante acciones físicas y
verbales consistentes, evitando contradicciones.




### Extracto transformado 090
**Hallazgo fuente:** Un modelo de IA solo
recitando texto sin motivación interna transmitirá menos realismo que uno
que actúa con un objetivo claro.




### Extracto transformado 091
**Hallazgo fuente:** Subtexto y emoción implícita: En la actuación humana, lo importante no
siempre es lo que se dice explícitamente; el subtexto –los pensamientos y
sentimientos no verbalizados– dota a la actuación de profundidad 3 .




### Extracto transformado 092
**Hallazgo fuente:** Por ejemplo, un avatar que dice “estoy bien” cuando en
realidad se siente herido puede mostrar microgestos de tristeza (ojos
ligeramente acuosos, sonrisa forzada) que revelen su verdadero estado
emocional.




### Extracto transformado 093
**Hallazgo fuente:** El subtexto se sostiene mediante sutiles gestos, inﬂexiones y
silencios cargados de signiﬁcado; “el silencio también forma parte del




### Extracto transformado 094
**Hallazgo fuente:** Esto signiﬁca que pausas bien colocadas pueden
hablar tanto como las palabras, sugiriendo duda, tensión o emotividad.




### Extracto transformado 095
**Hallazgo fuente:** Gestionar los silencios de forma intencional –por ejemplo, una pausa antes
de responder a una pregunta difícil– añade verosimilitud y coherencia
emocional.




### Extracto transformado 096
**Hallazgo fuente:** En una conversación, no solo se “actúa” al hablar, sino también al
escuchar –sincronizando la expresión facial y corporal con lo que el otro dice.




### Extracto transformado 097
**Hallazgo fuente:** Para un avatar conversacional, esto signiﬁca movimientos de cabeza
asintiendo, expresiones faciales reactivas (sonreír, fruncir el ceño),
mantener la mirada de forma natural, etc., durante las intervenciones de la
otra persona.




### Extracto transformado 098
**Hallazgo fuente:** En la práctica, muchos modelos de avatar generativo son
“hablantes” pero no “escuchantes”: permanecen inexpresivos mientras no les
toca hablar, lo que se siente estático y antinatural 4 .




### Extracto transformado 099
**Hallazgo fuente:** Solución: entrenar la IA
con datos de personas que escuchan activamente (asintiendo levemente,
mostrando reacciones acordes) o incluso usar enfoques como Preferencia
Directa (DPO) para premiar los comportamientos de escucha atentos frente a
los pasivos 4 .




### Extracto transformado 100
**Hallazgo fuente:** Un avatar debe responder tanto al contenido como a las
reacciones del interlocutor (p.ej., si el usuario sonríe o asiente, el avatar
puede corresponder con otra sonrisa o pausa calibrada).




### Extracto transformado 101
**Hallazgo fuente:** Esto logra
interacciones más ﬂuidas y realistas, y evita la “mirada de piedra” que
desconecta al público.




### Extracto transformado 102
**Hallazgo fuente:** Dominio del timing y ritmo: El tempo de la actuación –es decir, la velocidad
con la que el avatar habla, se mueve o reacciona– inﬂuye en la narrativa y la
verosimilitud.




### Extracto transformado 103
**Hallazgo fuente:** Una IA debe aprender timing cómico (cómo pausar unos
instantes antes de rematar un chiste para maximizar la gracia) y timing
dramático (pausas estratégicas para enfatizar tensión o emoción).




### Extracto transformado 104
**Hallazgo fuente:** Un buen
timing requiere calibración: ni demasiado apresurado (lo que suena ansioso o
artiﬁcial) ni excesivamente lento (que puede parecer robótico).




### Extracto transformado 105
**Hallazgo fuente:** Por ejemplo,
un avatar que cuenta una anécdota humorística debe dejar un silencio breve
antes del remate y quizá reír junto al espectador justo después para enfatizar
la conexión cómica.




### Extracto transformado 106
**Hallazgo fuente:** Una escena dramática de confrontación podría
beneﬁciarse de silencios tensos, respiraciones audibles y variaciones
rítmicas en la voz para mostrar conﬂicto interno.




### Extracto transformado 107
**Hallazgo fuente:** Estos matices de ritmo y
cadencia –aprendidos de la actuación tradicional– permiten a la IA marcar los




### Extracto transformado 108
**Hallazgo fuente:** puntos emotivos clave y mantener el interés del público, ajustando su tempo
según la dinámica de la escena.




### Extracto transformado 109
**Hallazgo fuente:** Mirada y expresividad visual (evitar “mirada vacía”): La mirada es
fundamental para transmitir emociones y conexiones.




### Extracto transformado 110
**Hallazgo fuente:** Un avatar con ojos
estáticos o vacíos provoca una reacción inquietante en la audiencia,
contribuyendo al efecto del valle inquietante 5 .




### Extracto transformado 111
**Hallazgo fuente:** Para evitar esa “mirada en
blanco”, los modelos deben incorporar micro-comportamientos visuales:
pestañeos naturales, movimientos sutiles de los globos oculares (pequeños
sacádicos), ligeros seguimientos de objetos o personas en la escena 5 .




### Extracto transformado 112
**Hallazgo fuente:** Además,
detalles técnicos como reﬂejos especulares en la pupila generan
profundidad y vitalidad en la mirada 5 .




### Extracto transformado 113
**Hallazgo fuente:** Por ejemplo, en una escena emotiva,
los ojos del avatar deben enfocarse suavemente en el interlocutor o en el objeto
de su atención, evitando un mirar ﬁjo excesivo.




### Extracto transformado 114
**Hallazgo fuente:** Microexpresiones faciales –
contracciones leves alrededor de los ojos o la boca– añaden credibilidad
emocional 5 .




### Extracto transformado 115
**Hallazgo fuente:** En suma, la expresión ocular y facial del avatar debe ser rica,
reactiva y congruente con sus emociones (evitando la hiperexpresión
exagerada o la falta de reacción).




### Extracto transformado 116
**Hallazgo fuente:** Una mirada convincente junto con una
expresión matizada genera esa sensación de presencia en cámara, como la que
logra un buen actor humano en un primer plano intenso.




### Extracto transformado 117
**Hallazgo fuente:** Actuación según el Formato y Contexto:
fotografía, video musical, entrevista, escena
narrativa, anuncio y backstage
Los distintos formatos audiovisuales requieren ajustar la actuación del
modelo para conservar coherencia artística y efectividad comunicativa.




### Extracto transformado 118
**Hallazgo fuente:** --- SOURCE: Wardrobe premium por modelo y cuerpo ---
Wardrobe premium, física textil y ﬁt por cuerpo, edad y rol de modelo IA
Aplicable a IDUNEX v1.0.0‑RC1 [LEGACY_MARKETING_TERM_REMOVED] (Proyecto PROJECT_BRAND_ENTITY / IDUNEX)




### Extracto transformado 119
**Hallazgo fuente:** Resumen ejecutivo
Objetivos: Garantizar que el wardrobe o vestuario de los modelos sintéticos de
IDUNEX [LEGACY_MARKETING_TERM_REMOVED] posea una calidad premium, simulando ﬁelmente las
propiedades físicas de las telas (PBR – Physically-Based Rendering) y un ﬁt
adecuado al cuerpo, edad y rol de cada modelo digital.




### Extracto transformado 120
**Hallazgo fuente:** Esto implica aplicar un
baseline técnico estándar, incluyendo materiales realistas, simulación de
telas con gravedad, colisiones y elasticidad, sombras de contacto y
comportamiento físico auténtico (tensión, arrugas, caída natural de la tela,
etc.).




### Extracto transformado 121
**Hallazgo fuente:** Se busca lograr resultados visuales creíbles donde la ropa interactúe
coherentemente con el cuerpo del modelo, manteniendo proporciones
realistas, contacto piel-prenda, y sin exhibir artefactos digitales (p.




### Extracto transformado 122
**Hallazgo fuente:** Beneﬁcios: Un vestuario premium y físicamente realista aumenta la
credibilidad visual de los modelos sintéticos, mejorando la inmersión y la
calidad de las imágenes generadas.




### Extracto transformado 123
**Hallazgo fuente:** Vestuario adaptado a la edad y al cuerpo
promueve la coherencia antropométrica (con los parámetros de altura, peso
y complexión predeﬁnidos en el perﬁl de cada modelo) 2 .




### Extracto transformado 124
**Hallazgo fuente:** Además, la
incorporación de roles estilísticos (Editorial, Corporativo, Performance, Swim
& Bodywear, Lifestyle, Brand Ambassador) aporta versatilidad, permitiendo
producir imágenes ajustadas a contextos especíﬁcos (p.




### Extracto transformado 125
**Hallazgo fuente:** ej., editorial de moda,
escenario corporativo, sesión de fotos lifestyle) manteniendo la consistencia
con la identidad de marca PROJECT_BRAND_ENTITY.




### Extracto transformado 126
**Hallazgo fuente:** Riesgos y medidas de mitigación: Los riesgos técnicos incluyen posibles
incongruencias físicas (ropa que atraviesa el cuerpo, falta de gravedad,
propiedades de tela irreales), lo que se previene con simulación de telas
calibrada y un arsenal de pruebas de QA para veriﬁcar colisiones, arrugas y
ajuste correcto.




### Extracto transformado 127
**Hallazgo fuente:** Otro riesgo es la sexualización no deseada de los modelos
(especialmente en ropa de baño o interior); para evitarlo se han deﬁnido
límites de contenido – ninguna imagen debe presentar poses pornográﬁcas,
desnudez ni contenido sexual explícito, y las prendas Swim & Bodywear se




### Extracto transformado 128
**Hallazgo fuente:** También es crítico
prevenir el desvío de identidad o incoherencias: gracias a variables de
control (bloqueo de edad, proporciones, etc.) cada modelo mantiene sus rasgos
únicos y no se confunde con otros 2 .




### Extracto transformado 129
**Hallazgo fuente:** Por último, garantizar la calidad
premium del output requerirá ciclos de reﬁnamiento iterativos y validación
manual para aﬁnar el pipeline generativo, mitigando riesgos de imágenes de
baja calidad o poco realistas.




### Extracto transformado 130
**Hallazgo fuente:** Criterios de éxito: El proyecto se considerará exitoso si cada imagen generada
presenta prendas fotorrealistas correctamente ajustadas al cuerpo y edad del
modelo, con simulación física verosímil de telas (peso, caída, arrugas y
deformaciones naturales) 1 .




### Extracto transformado 131
**Hallazgo fuente:** Además, cada imagen debe alinearse con el rol
asignado al modelo sin salirse de las pautas (estéticas y éticas) deﬁnidas para
ese rol 2 .




### Extracto transformado 132
**Hallazgo fuente:** El sistema debe superar todas las pruebas QA internas (sin códigos
de fallo), manteniendo cero casos de sexualización explícita o
inconsistentencias notables en identidad, edad o physique.




### Extracto transformado 133
**Hallazgo fuente:** Finalmente, se
espera que el PromptPack resultante sea modular, reutilizable y fácilmente
integrable en la versión v1.0.0-RC1 de IDUNEX [LEGACY_MARKETING_TERM_REMOVED].




### Extracto transformado 134
**Hallazgo fuente:** Variables JSON clave y esquema para
conﬁguración
Para implementar estas políticas de wardrobe premium en IDUNEX [LEGACY_MARKETING_TERM_REMOVED],
se deﬁne un esquema JSON con variables estructuradas que permiten la




### Extracto transformado 135
**Hallazgo fuente:** A continuación se describe un esquema de variables organizadas
por categorías clave: cuerpo, edad, rol, material, parámetros físicos, ajuste
(ﬁt), QA, evitaciones (negativos) y correcciones (fallback):




### Extracto transformado 136
**Hallazgo fuente:** Estas variables JSON forman un marco de control robusto para garantizar
que la física textil, el ﬁt corporal, la estética de rol y la calidad ﬁnal de
cada imagen generada se apeguen a estándares premium de IDUNEX [LEGACY_MARKETING_TERM_REMOVED].




### Extracto transformado 137
**Hallazgo fuente:** Tablas por tipo de prenda y parámetros técnicos
A continuación, se presentan tablas comparativas que resumen las
especiﬁcaciones clave para distintas categorías de prenda/estilo relevantes
en el marco PROJECT_BRAND_ENTITY.




### Extracto transformado 138
**Hallazgo fuente:** --- SOURCE: Acting poses y microgestos por personalidad ---
Acting, microgestos, poses y lenguaje
corporal por personalidad (OCEAN/
HEXACO) para modelos IA sintéticos
Acting técnico en modelos IA – La presente propuesta deﬁne un marco
técnico independiente para actuación (acting), microgestualidad, posado
corporal y lenguaje no verbal en modelos IA sintéticos adultos.




### Extracto transformado 139
**Hallazgo fuente:** El enfoque
se basa en matrices de personalidad OCEAN (Big Five) y HEXACO, con la
ﬁnalidad de orientar la producción audiovisual y la fotografía comercial de
PROJECT_BRAND_ENTITY (LF) en PROJECT_DECLARED_COUNTRY.




### Extracto transformado 140
**Hallazgo fuente:** El marco garantiza que cada modelo sintético
exprese gestualidad única, coherente con su personalidad, evitando poses
genéricas, sonrisas clonadas, miradas vacías y actuaciones artiﬁciales.




### Extracto transformado 141
**Hallazgo fuente:** Este
estándar es independiente de los perﬁles HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former RC19.6.2 existentes, pero ha sido
diseñado para integrarse completamente en ellos.




### Extracto transformado 142
**Hallazgo fuente:** Resumen ejecutivo
Objetivo del marco: proporcionar lineamientos técnicos integrales para la
actuación y lenguaje corporal de los modelos IA de PROJECT_BRAND_ENTITY, enfocándose
en su coherencia con la personalidad, evitando la homogeneidad.




### Extracto transformado 143
**Hallazgo fuente:** Se introduce
un sistema de variables especializadas que extienden la deﬁnición de cada
modelo sin duplicar campos existentes.




### Extracto transformado 144
**Hallazgo fuente:** Estas variables capturan actitud y
comportamiento no verbal (gestos, poses, mirada, etc.), vinculándolos con
perﬁles psicológicos OCEAN/HEXACO.
