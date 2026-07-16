# SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10

Estado: PRODUCTIVE_BASE_ENGINE_VALIDATED

Autoridad: SRC_049_ENV_PHYSICS_FULL10 / ENV_PHYSICS_FULL10. Controla diseño de producción, mise-en-scène, blocking, cuerpo-objeto, props, escala, perspectiva, piso, pared, techo, luz, sombras, reflejos, continuidad y contexto cultural sin estereotipos.

## Fail codes ENV

### ENV-STYLE
- definition: Scene style, art direction or mise-en-scene contradicts model, project or editorial tone.
- trigger: ENV-STYLE triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-STYLE: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-STYLE, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-STYLE; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-STYLE dimension.
- sidecar_evidence_field: env_style_evidence

### ENV-COMP
- definition: Composition, blocking, lens height, thirds, depth or hierarchy fails.
- trigger: ENV-COMP triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-COMP: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-COMP, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-COMP; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-COMP dimension.
- sidecar_evidence_field: env_comp_evidence

### ENV-COLL
- definition: Body/object collision, clipping or impossible contact appears.
- trigger: ENV-COLL triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-COLL: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-COLL, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-COLL; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-COLL dimension.
- sidecar_evidence_field: env_coll_evidence

### ENV-PROP
- definition: Props are missing, anachronistic, unsafe or physically unsupported.
- trigger: ENV-PROP triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-PROP: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-PROP, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-PROP; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-PROP dimension.
- sidecar_evidence_field: env_prop_evidence

### ENV-GRAV
- definition: Gravity, fabric fall, hair, objects or posture appear weightless.
- trigger: ENV-GRAV triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-GRAV: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-GRAV, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-GRAV; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-GRAV dimension.
- sidecar_evidence_field: env_grav_evidence

### ENV-OCCL
- definition: Occlusion ordering between body, object and architecture is wrong.
- trigger: ENV-OCCL triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-OCCL: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-OCCL, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-OCCL; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-OCCL dimension.
- sidecar_evidence_field: env_occl_evidence

### ENV-SCALE
- definition: Human-to-object or architecture scale is inconsistent.
- trigger: ENV-SCALE triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-SCALE: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-SCALE, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-SCALE; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-SCALE dimension.
- sidecar_evidence_field: env_scale_evidence

### ENV-PERSP
- definition: Floor, wall, ceiling, vanishing point or lens perspective breaks.
- trigger: ENV-PERSP triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-PERSP: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-PERSP, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-PERSP; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-PERSP dimension.
- sidecar_evidence_field: env_persp_evidence

### ENV-LIGHT
- definition: Key/fill/rim, shadow direction or color temperature is inconsistent.
- trigger: ENV-LIGHT triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-LIGHT: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-LIGHT, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-LIGHT; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-LIGHT dimension.
- sidecar_evidence_field: env_light_evidence

### ENV-REFL
- definition: Reflections, mirrors, glass, wet floor or metals contradict light/space.
- trigger: ENV-REFL triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-REFL: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-REFL, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-REFL; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-REFL dimension.
- sidecar_evidence_field: env_refl_evidence

### ENV-CONT
- definition: Image-video continuity, wardrobe, props or blocking changes unintentionally.
- trigger: ENV-CONT triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-CONT: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-CONT, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-CONT; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-CONT dimension.
- sidecar_evidence_field: env_cont_evidence

### ENV-CULT
- definition: Locality or cultural context becomes stereotype, tourist cliché or wrong region.
- trigger: ENV-CULT triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-CULT: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-CULT, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-CULT; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-CULT dimension.
- sidecar_evidence_field: env_cult_evidence

### ENV-EDIT
- definition: Editorial safety or adult boundary fails.
- trigger: ENV-EDIT triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-EDIT: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-EDIT, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-EDIT; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-EDIT dimension.
- sidecar_evidence_field: env_edit_evidence

### ENV-CONTACT
- definition: Feet, hands, hips, props or furniture do not show believable contact.
- trigger: ENV-CONTACT triggers when visible/prompt/sidecar evidence contradicts SRC_049 scene physics.
- prompt_fix: Rewrite scene clause for ENV-CONTACT: specify plane, scale, contact, camera height, lens, key/fill/rim, shadows, reflections and continuity.
- negative_prompt_fix: NEGATIVE / AVOID: ENV-CONTACT, floating props, clipping, wrong occlusion, broken vanishing point, plastic scene, stereotype, unsafe editorial drift.
- qa_fix: Run SRC049 PASS/FAIL inspection for ENV-CONTACT; compare prompt, output and sidecar before output_go.
- manual_fallback: Simplify to one body, one prop, one floor plane and rebuild the failed ENV-CONTACT dimension.
- sidecar_evidence_field: env_contact_evidence

## Scene archetypes FULL10

### 01_ESTUDIO_FOTOGRAFICO
- **scene_purpose**: Sesión controlada de retrato/editorial donde el modelo, el fondo, el modificador de luz y el prop principal explican identidad visual sin ruido.
- **allowed_props**: ['c-stand', 'softbox/octabox', 'reflector', 'ciclorama mate', 'taburete estable', 'cinta gaffer visible solo si aporta realismo']
- **forbidden_props**: ['logos de cámara', 'cables atravesando cuerpo', 'fondos urbanos aleatorios', 'luces sin soporte', 'textos en pared']
- **lighting_logic**: Key grande a 45°, fill suave al lado opuesto, rim leve si separa cabello; sombras caen en el piso del ciclorama y no flotan.
- **camera_logic**: Full-frame 85mm f/4 para retrato medio o 50mm f/5.6 para cuerpo completo; cámara a altura de pecho/ojos según intención.
- **wardrobe_compatibility**: Ropa editorial limpia; telas con caída visible, costuras alineadas, sin clipping con codos/cintura.
- **body_object_interactions**: Pies apoyados, manos con intención sobre taburete/ropa/prop; contacto genera sombra de contacto.
- **cultural_context**: Neutral de estudio; puede incluir dirección de arte PROJECT_BRAND_ENTITY sin logos ni texto si el proyecto lo permite.
- **common_ai_failures**: ['fondos infinitos sin piso', 'luces flotantes', 'dedos extra al sujetar accesorios', 'piel plástica', 'sombras duplicadas']
- **negative_prompt**: floating lights, impossible backdrop, extra fingers, body clipping, wrong contact shadow, fake studio logo, text artifacts
- **qa_checklist**: ['PASS piso/pared continuidad', 'PASS catchlights coherentes', 'PASS manos y pies', 'PASS scale de softbox', 'PASS sin texto/logo']
- **fallback_fixes**: ['Reducir a un fondo mate y una luz principal', 'Bloquear posición de pies', 'Eliminar props secundarios', 'Reforzar contact shadows']
- **sidecar_fields**: ['studio_lighting_map', 'floor_wall_contact', 'prop_support_evidence']

### 02_ROOFTOP_LIMA
- **scene_purpose**: Rooftop contemporáneo de PROJECT_DECLARED_LOCALITY para lifestyle/editorial con ciudad al fondo, bruma costera controlada y barandas a escala.
- **allowed_props**: ['baranda metálica', 'macetas de concreto', 'mesa baja', 'luces cálidas pequeñas', 'vista urbana desenfocada']
- **forbidden_props**: ['Machu Picchu de fondo', 'rascacielos futuristas', 'baranda a media cintura imposible', 'viento tropical exagerado', 'logos de hoteles']
- **lighting_logic**: Golden hour o blue hour; key ambiental lateral, fill suave por rebote de muro claro, sombras largas coherentes sobre terraza.
- **camera_logic**: 35mm o 50mm, cámara a 1.3-1.6m, fondo con profundidad y horizonte nivelado; no gran angular extremo que deforme cuerpo.
- **wardrobe_compatibility**: Casual premium o urbano elegante con abrigo ligero por humedad limeña; telas no vuelan como playa tropical.
- **body_object_interactions**: Codos/manos pueden tocar baranda con oclusión correcta; pies apoyados sobre losa, no flotando.
- **cultural_context**: PROJECT_DECLARED_LOCALITY moderna sin cliché turístico; clima gris/costero permitido con estética premium.
- **common_ai_failures**: ['horizonte torcido', 'baranda atravesando cuerpo', 'escala de edificios falsa', 'sombras sin dirección', 'estereotipos andinos fuera de contexto']
- **negative_prompt**: tourist cliché, Machu Picchu skyline, floating terrace, warped railing, broken horizon, city scale mismatch, text signs
- **qa_checklist**: ['PASS horizonte', 'PASS baranda no corta articulaciones', 'PASS escala edificios', 'PASS clima PROJECT_DECLARED_LOCALITY coherente', 'PASS sombras terraza']
- **fallback_fixes**: ['Bajar profundidad de campo', 'Simplificar skyline', 'Fijar baranda detrás o delante claramente', 'Usar luz de tarde nublada']
- **sidecar_fields**: ['lima_rooftop_context', 'railing_occlusion', 'skyline_scale_check']

### 03_CALLE_URBANA
- **scene_purpose**: Calle urbana latinoamericana contemporánea para moda, baile o storytelling con tránsito espacial creíble y fondo no invasivo.
- **allowed_props**: ['vereda', 'muro pintado sin texto', 'poste', 'puerta metálica', 'bolardo', 'luz de tienda desenfocada']
- **forbidden_props**: ['pandillas explícitas', 'grafitis legibles con marcas', 'armas', 'vehículos deformes', 'basura caricaturesca']
- **lighting_logic**: Luz natural lateral o neón controlado; sombras siguen fachada y piso; reflejos de pista solo si hay humedad visible.
- **camera_logic**: 35mm documental o 50mm editorial; cámara a cintura/pecho para moda urbana; líneas de vereda conducen perspectiva.
- **wardrobe_compatibility**: Urbanwear, denim, zapatillas, chaquetas; ropa con contacto real en hombros/rodillas.
- **body_object_interactions**: Pies respetan plano de vereda; si se apoya al muro, hombro/espalda generan sombra y compresión leve.
- **cultural_context**: Puede ser PROJECT_DECLARED_CITY/PROJECT_DECLARED_PORT_CITY/PROJECT_DECLARED_COUNTRY city actual sin convertir pobreza o peligro en cliché.
- **common_ai_failures**: ['piso sin plano', 'vehículos microscópicos', 'dedos al sostener celular', 'carteles con texto falso', 'sombras cruzadas']
- **negative_prompt**: fake readable text, gang stereotype, weapon, floating feet, warped sidewalk, duplicate limbs, car scale error
- **qa_checklist**: ['PASS perspectiva vereda', 'PASS pies en piso', 'PASS props seguros', 'PASS sin texto artificial', 'PASS contexto urbano respetuoso']
- **fallback_fixes**: ['Eliminar carteles', 'Usar muro limpio', 'Reducir vehículos a bokeh', 'Reforzar sombra bajo zapatillas']
- **sidecar_fields**: ['urban_plane_evidence', 'street_context_safety', 'foot_contact_shadow']

### 04_BACKSTAGE_SHOW
- **scene_purpose**: Backstage realista de show con energía previa a escena: cables, rack, maquillaje y tránsito controlados sin desorden falso.
- **allowed_props**: ['flight cases', 'perchero', 'espejo con bombillas', 'cables ordenados', 'botella de agua', 'intercom']
- **forbidden_props**: ['cables atravesando piernas', 'marcas de equipos', 'escenario imposible detrás', 'fuego sin fuente', 'multitudes deformes']
- **lighting_logic**: Mixto cálido/frío: bombillas de espejo + rim de escenario; sombras múltiples pero justificadas por fuentes visibles.
- **camera_logic**: 28-35mm documental cercano, cámara a hombro; profundidad separa primer plano de utilería.
- **wardrobe_compatibility**: Vestuario escénico adulto editorial, capas ajustadas y accesorios anclados.
- **body_object_interactions**: Manos ajustan guante, micrófono o chaqueta; cables quedan en piso detrás o al lado, nunca atravesando cuerpo.
- **cultural_context**: Shows PROJECT_BRAND_ENTITY/PROJECT_DECLARED_COUNTRY: profesional, ordenado, sin logos ni marcas; ambiente de producción real.
- **common_ai_failures**: ['equipos fusionados', 'luces sin fuente', 'manos deformes en maquillaje', 'cables flotantes', 'reflejos imposibles']
- **negative_prompt**: cable through body, fake brand logo, impossible mirror reflection, deformed hands, floating equipment, chaotic unsafe backstage
- **qa_checklist**: ['PASS fuentes visibles', 'PASS cables seguros', 'PASS espejo/reflejo', 'PASS accesorios anclados', 'PASS no marcas']
- **fallback_fixes**: ['Reducir cantidad de cables', 'Cambiar espejo a pared lisa', 'Usar un prop principal', 'Separar rack del cuerpo']
- **sidecar_fields**: ['backstage_prop_map', 'cable_safety_evidence', 'mirror_reflection_check']

### 05_SALA_DE_ENSAYO
- **scene_purpose**: Sala de ensayo para baile/actuación con piso, espejo, barras o parlantes a escala y movimiento biomecánico verificable.
- **allowed_props**: ['espejo amplio', 'parlante', 'marca de cinta en piso', 'mochila', 'botella', 'barra de pared']
- **forbidden_props**: ['espejos que duplican identidad mal', 'piso inclinado', 'barras atravesando torso', 'logos de academias', 'menores sexualizados']
- **lighting_logic**: Fluorescente/LED suave de techo con rebote; sombras cortas bajo pies; reflejo del espejo consistente.
- **camera_logic**: 24-35mm si se muestra cuerpo completo; cámara horizontal/nivelada para ver piso y equilibrio.
- **wardrobe_compatibility**: Ropa deportiva/danza; telas elásticas con tensión en rodillas/codos y calzado de apoyo.
- **body_object_interactions**: Centro de gravedad sobre pie de apoyo; manos no desaparecen en espejo; botella/mochila en plano correcto.
- **cultural_context**: Espacio de práctica urbano de PROJECT_DECLARED_LOCALITY o estudio privado sin marcas; profesional y limpio.
- **common_ai_failures**: ['reflejo con otro rostro', 'piernas imposibles', 'piso sin contacto', 'espejo sin profundidad', 'parlantes flotantes']
- **negative_prompt**: wrong mirror identity, floating feet, impossible dance pose, warped floor grid, extra limbs, brand text
- **qa_checklist**: ['PASS espejo coincide', 'PASS balance corporal', 'PASS escala parlante', 'PASS contacto pies', 'PASS piso nivelado']
- **fallback_fixes**: ['Eliminar espejo si falla identidad', 'Congelar pose más simple', 'Agregar sombra bajo pie', 'Usar lente 35mm']
- **sidecar_fields**: ['mirror_identity_lock', 'movement_balance_check', 'floor_contact_points']

### 06_OFICINA_CREATIVA
- **scene_purpose**: Oficina creativa/productiva para planificación, branding o revisión audiovisual con mesa, pantallas y materiales ordenados.
- **allowed_props**: ['mesa de vidrio/madera', 'laptop sin logo', 'moodboard sin texto legible', 'silla ergonómica', 'luz de escritorio', 'plantas sobrias']
- **forbidden_props**: ['pantallas con UI falsa legible', 'logos de software', 'documentos con datos reales', 'cables imposibles', 'sillas fusionadas']
- **lighting_logic**: Key suave de ventana o panel LED, fill de pared blanca, sombras bajo mesa/silla; reflejos de vidrio controlados.
- **camera_logic**: 35-50mm, altura sentada/de pie según reunión; verticales arquitectónicas rectas.
- **wardrobe_compatibility**: Casual profesional o creativo; mangas y accesorios no atraviesan mesa.
- **body_object_interactions**: Manos sobre laptop/cuaderno con dedos visibles; silla soporta peso, pies al piso.
- **cultural_context**: Puede representar oficina PROJECT_BRAND_ENTITY sin exponer datos ni marcas; PROJECT_DECLARED_LOCALITY empresarial contemporánea.
- **common_ai_failures**: ['teclados deformes', 'texto falso en pantalla', 'manos fusionadas con laptop', 'reflejo de mesa incorrecto', 'silla sin patas']
- **negative_prompt**: readable fake UI, confidential documents, brand logos, fused fingers, floating chair, table reflection mismatch
- **qa_checklist**: ['PASS privacidad', 'PASS manos/laptop', 'PASS silla/mesa escala', 'PASS reflejo vidrio', 'PASS luz ventana']
- **fallback_fixes**: ['Apagar pantalla o blur', 'Quitar documentos', 'Usar una sola fuente de luz', 'Separar manos del teclado']
- **sidecar_fields**: ['office_privacy_check', 'desk_contact_evidence', 'screen_text_policy']

### 07_HABITACION_LIFESTYLE
- **scene_purpose**: Lifestyle íntimo no explícito, adulto editorial, donde cama/silla/ventana aportan personalidad sin sexualización indebida.
- **allowed_props**: ['cama tendida', 'lámpara', 'cortinas', 'libro sin texto legible', 'alfombra', 'mesa de noche']
- **forbidden_props**: ['desnudez', 'menores/apariencia menor', 'cama deformada', 'sábanas atravesando cuerpo', 'contenido explícito']
- **lighting_logic**: Luz de ventana o lámpara cálida; sombras suaves sobre cama/pared; reflejos mínimos.
- **camera_logic**: 50mm o 35mm moderado; cámara a altura humana, encuadre limpio sin voyeurismo.
- **wardrobe_compatibility**: Casual, pijama editorial, loungewear adulto no explícito; tela cae por gravedad.
- **body_object_interactions**: Peso del cuerpo deforma levemente cojín/silla; manos y pies visibles y anatómicos.
- **cultural_context**: Habitación contemporánea neutral; si aplica PROJECT_DECLARED_COUNTRY, detalles discretos sin folclorizar.
- **common_ai_failures**: ['sábanas con anatomía imposible', 'poses sexualizadas no pedidas', 'manos ocultas', 'ventanas sin perspectiva', 'objetos flotantes']
- **negative_prompt**: explicit nudity, minor-coded, voyeur angle, floating bedding, body clipping, deformed hands, text artifacts
- **qa_checklist**: ['PASS adulto editorial', 'PASS cama soporta peso', 'PASS tela no atraviesa cuerpo', 'PASS luz cálida coherente', 'PASS manos']
- **fallback_fixes**: ['Pasar a silla/ventana', 'Subir encuadre a torso', 'Simplificar bedding', 'Agregar sombra de contacto']
- **sidecar_fields**: ['adult_editorial_boundary', 'bedding_contact_check', 'lifestyle_privacy_policy']

### 08_PLAYA_PISCINA
- **scene_purpose**: Escena de playa/piscina adulta editorial con agua, reflejos, piel, tela y horizonte físicamente coherentes.
- **allowed_props**: ['toalla', 'lentes sin marca', 'sombrilla', 'borde de piscina', 'arena', 'vaso sin logo']
- **forbidden_props**: ['desnudez', 'poses explícitas', 'agua que atraviesa cuerpo', 'horizonte curvo', 'piel plástica mojada']
- **lighting_logic**: Sol lateral o sombra abierta; reflejos en agua obedecen fuente; sombras duras si mediodía, suaves si atardecer.
- **camera_logic**: 50mm o 70mm para glamour controlado; horizonte nivelado; evitar gran angular que distorsione cuerpo.
- **wardrobe_compatibility**: Ropa de baño adulta editorial; tirantes, bordes y tela respetan tensión y anatomía sin explicitud.
- **body_object_interactions**: Pies hunden levemente arena o apoyan borde; agua moja zonas plausibles y genera reflejo.
- **cultural_context**: Costa project-declared o piscina privada sin cliché tropical obligatorio; clima y luz coherentes.
- **common_ai_failures**: ['dedos extra en lentes', 'línea de bikini imposible', 'agua sin refracción', 'sombras contradictorias', 'horizonte torcido']
- **negative_prompt**: explicit pose, distorted swimwear, water through body, warped horizon, plastic wet skin, extra fingers, logo
- **qa_checklist**: ['PASS límite editorial', 'PASS horizonte', 'PASS reflejo agua', 'PASS tela/fit', 'PASS contacto pies']
- **fallback_fixes**: ['Usar pareo/kimono', 'Cambiar a plano medio', 'Reducir agua visible', 'Bloquear horizonte recto']
- **sidecar_fields**: ['swimwear_editorial_boundary', 'water_reflection_check', 'horizon_level_evidence']

### 09_ESCENARIO_MUSICAL
- **scene_purpose**: Escenario musical con performance creíble, micrófono/instrumentos y luces de show trazables.
- **allowed_props**: ['micrófono', 'stand', 'monitor de piso', 'haze sutil', 'backline sin marcas', 'luces PAR']
- **forbidden_props**: ['instrumentos imposibles', 'micrófono fusionado con boca', 'marcas de equipos', 'multitud deformada', 'fuego no justificado']
- **lighting_logic**: Key de escenario + rim color + haze controlado; sombras proyectadas por monitores/stand.
- **camera_logic**: 70mm para close performance o 35mm desde pit; cámara baja solo si no deforma anatomía.
- **wardrobe_compatibility**: Vestuario escénico adulto, accesorios asegurados; telas responden a movimiento.
- **body_object_interactions**: Mano envuelve micrófono con dedos visibles; cable/stand anclado al piso.
- **cultural_context**: Show profesional project-declared/PROJECT_BRAND_ENTITY sin logos; público como bokeh si no es foco.
- **common_ai_failures**: ['micrófonos duplicados', 'manos deformes', 'luces sin estructura', 'bocas desalineadas', 'cables flotantes']
- **negative_prompt**: fused microphone, extra fingers, fake brand, impossible stage light, warped crowd, cable through body
- **qa_checklist**: ['PASS mano-mic', 'PASS luz visible', 'PASS cable/stand', 'PASS boca/voz', 'PASS sin marcas']
- **fallback_fixes**: ['Usar mic inalámbrico', 'Reducir público', 'Fijar stand al piso', 'Simplificar luces a tres fuentes']
- **sidecar_fields**: ['stage_light_plot', 'microphone_contact_check', 'performance_continuity']

### 10_SET_AUDIOVISUAL
- **scene_purpose**: Set audiovisual realista para entrevista, comercial o making-of con cámara, monitor, boom/lav y blocking técnico.
- **allowed_props**: ['cámara en trípode', 'monitor articulado', 'boom pole', 'lavalier', 'claqueta sin texto', 'panel LED']
- **forbidden_props**: ['logos de cámaras', 'cámara sin soporte', 'micrófono atravesando ropa', 'pantallas con texto falso', 'cables peligrosos']
- **lighting_logic**: Key LED con difusión, fill negativo o reflector, rim según fondo; sombras coherentes con trípode y sujeto.
- **camera_logic**: Mostrar cámara de producción en ángulo 3/4 o POV limpio; focal 35-50mm, altura estable.
- **wardrobe_compatibility**: Ropa profesional acorde al rol: productor, modelo, entrevistado; lavalier anclado sin deformar tela.
- **body_object_interactions**: Trípode toca piso en tres puntos; operador sostiene cámara/monitor sin dedos extra.
- **cultural_context**: Producción audiovisual project-declared profesional; no exponer marcas ni datos de cliente.
- **common_ai_failures**: ['trípodes con patas extra', 'monitor flotante', 'mic de solapa gigante', 'cables atravesando piernas', 'pantallas con pseudo texto']
- **negative_prompt**: floating camera, impossible tripod, fake UI text, brand logos, lav mic clipping, deformed operator hands
- **qa_checklist**: ['PASS soporte cámara', 'PASS lavalier escala', 'PASS luz/trípode sombras', 'PASS cables seguros', 'PASS pantalla sin texto']
- **fallback_fixes**: ['Apagar monitor', 'Eliminar operador secundario', 'Cambiar boom a lavalier', 'Usar cámara en trípode simple']
- **sidecar_fields**: ['av_set_equipment_map', 'tripod_contact_points', 'screen_text_absence']

### 11_AMBIENTE_TERROR
- **scene_purpose**: Terror atmosférico psicológico con espacio legible, sombras motivadas y tensión sin gore explícito.
- **allowed_props**: ['puerta entreabierta', 'radio antigua', 'linterna', 'cortina', 'polvo', 'espejo opaco']
- **forbidden_props**: ['gore gráfico', 'menores sexualizados', 'monstruos con anatomía incoherente', 'símbolos ofensivos', 'texto falso']
- **lighting_logic**: Key mínima motivada por linterna/lámpara, fill frío ambiental, sombras largas y oclusiones claras.
- **camera_logic**: 35mm o 50mm, ángulo ligeramente bajo/alto si refuerza tensión; mantener geometría de habitación.
- **wardrobe_compatibility**: Ropa cotidiana o narrativa; telas con sombras y contacto real, no disfraces genéricos.
- **body_object_interactions**: Mano sostiene linterna con haz y sombra; pies/contacto visibles si hay figura humana.
- **cultural_context**: Terror latino/project-declared posible desde arquitectura común, sin apropiación ni cliché folclórico.
- **common_ai_failures**: ['sombras sin objeto', 'manos de linterna deformes', 'puertas con geometría imposible', 'texto fantasma', 'rostros derretidos no pedidos']
- **negative_prompt**: graphic gore, offensive symbols, fake text, impossible doorway, floating flashlight, random monster, deformed hands
- **qa_checklist**: ['PASS fuente de luz', 'PASS geometría puerta', 'PASS editorial safety', 'PASS sombras motivadas', 'PASS props escala']
- **fallback_fixes**: ['Usar solo puerta y linterna', 'Eliminar figura secundaria', 'Bajar contraste de rostro', 'Reforzar plano de piso']
- **sidecar_fields**: ['horror_safety_boundary', 'motivated_shadow_map', 'door_geometry_check']

### 12_EDITORIAL_PREMIUM
- **scene_purpose**: Editorial premium fashion/branding con composición depurada, materiales reales y belleza no genérica.
- **allowed_props**: ['silla de diseño sin marca', 'tela de fondo', 'flor/objeto escultórico', 'joyería sin logo', 'panel reflectante']
- **forbidden_props**: ['logos de lujo', 'piel plástica', 'poses imposibles', 'accesorios fusionados', 'fondos saturados sin jerarquía']
- **lighting_logic**: Key amplia, fill controlado, rim preciso; contraste elegante con sombras de volumen.
- **camera_logic**: 85mm/105mm para compresión premium o 50mm full-body; encuadre por tercios y aire negativo.
- **wardrobe_compatibility**: Alta moda no explícita; costuras, pliegues y capas respetan cuerpo y gravedad.
- **body_object_interactions**: Pose balanceada; manos muestran joyería o tela sin dedos extra; silla/prop soporta peso.
- **cultural_context**: Premium global adaptable a PROJECT_BRAND_ENTITY/generic visual system sin marcas registradas ni apropiación cultural.
- **common_ai_failures**: ['misma cara glam', 'joyería derretida', 'tela atraviesa brazo', 'manos escondidas', 'fondo genérico']
- **negative_prompt**: generic beauty, same face, melted jewelry, fabric clipping, luxury logos, extra fingers, plastic skin
- **qa_checklist**: ['PASS identidad única', 'PASS tela/material', 'PASS manos/joyería', 'PASS composición premium', 'PASS sin logos']
- **fallback_fixes**: ['Reducir accesorios', 'Usar fondo liso', 'Bloquear landmarks faciales', 'Pedir close-up de manos separado si falla']
- **sidecar_fields**: ['editorial_material_check', 'premium_composition_grid', 'accessory_anchor_evidence']

### 13_DOCUMENTAL_REALISTA
- **scene_purpose**: Documental realista con sujeto en contexto verificable, imperfecciones humanas y evidencia ambiental no fabricada.
- **allowed_props**: ['herramienta de trabajo', 'mesa real', 'pared con textura sin texto', 'luz natural', 'objetos cotidianos']
- **forbidden_props**: ['drama falso', 'texto inventado', 'uniformes/marcas no autorizadas', 'escena hiperproducida', 'expresiones melodramáticas']
- **lighting_logic**: Disponible o rebotada; sombras naturales, ruido leve permitido, color no excesivamente cinematográfico.
- **camera_logic**: 35mm/50mm, altura humana, encuadre observacional; profundidad moderada para leer contexto.
- **wardrobe_compatibility**: Ropa realista según oficio y clima; arrugas y desgaste moderado, sin glamour gratuito.
- **body_object_interactions**: Sujeto usa herramienta/mesa/objeto con agarre natural y oclusión correcta.
- **cultural_context**: PROJECT_DECLARED_LOCALITY/regions solo si el proyecto lo define; respetuoso, sin pobreza estética ni exotización.
- **common_ai_failures**: ['rostro demasiado perfecto', 'contexto falso con texto', 'manos sin función', 'profundidad inconsistente', 'props decorativos']
- **negative_prompt**: fake documentary text, poverty cliché, overglamour, staged melodrama, warped hands, invented logo, unrealistic prop
- **qa_checklist**: ['PASS contexto respeta sujeto', 'PASS objeto usado realmente', 'PASS luz disponible', 'PASS sin texto falso', 'PASS humanidad natural']
- **fallback_fixes**: ['Eliminar carteles', 'Usar objeto simple', 'Bajar grading', 'Añadir imperfecciones sutiles de piel/tela']
- **sidecar_fields**: ['documentary_context_evidence', 'realism_texture_check', 'ethical_representation_note']

## PHASE 1/4 — ENV-CONTACT extension policy
required_base_set_count = 13
documented_extension_count = 1
extension_fail_code = ENV-CONTACT
extension_reason = body-object-contact physics requires explicit blocker
extension_policy = NON_BREAKING_EXTENSION
base_fail_codes_complete = true
validator = VALIDATE_ENV_CONTACT_EXTENSION_DOCUMENTED
updated_at = NEUTRALIZED_ACTIVE_SCOPE
