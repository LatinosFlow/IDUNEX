## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Cámara, lente, iluminación, color, escena y física espacial

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_CAMERA_0346` | `shot_type` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOT_TYPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shot type con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0347` | `camera_distance` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_DISTANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar camera distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0348` | `camera_height` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_HEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar camera height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0349` | `camera_angle` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_ANGLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar camera angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0350` | `lens_focal_range` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FOCAL_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lens focal range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0351` | `aperture_range` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_APERTURE_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar aperture range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0352` | `shutter_logic` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHUTTER_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shutter logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0353` | `iso_logic` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ISO_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar iso logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0354` | `white_balance` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WHITE_BALANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar white balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0355` | `sensor_look` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SENSOR_LOOK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sensor look con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0356` | `depth_of_field_rule` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DEPTH_OF_FIELD_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar depth of field rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0357` | `distortion_control` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DISTORTION_CONTROL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar distortion control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0358` | `crop_safe_area` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CROP_SAFE_AREA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar crop safe area con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0359` | `composition_grid` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMPOSITION_GRID_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar composition grid con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0360` | `negative_space_rule` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NEGATIVE_SPACE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar negative space rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0361` | `camera_body_relation` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_BODY_RELATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar camera body relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0362` | `key_light` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KEY_LIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar key light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0363` | `fill_light` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FILL_LIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fill light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0364` | `rim_light` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RIM_LIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar rim light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0365` | `catchlight_pattern` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CATCHLIGHT_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar catchlight pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0366` | `shadow_logic` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHADOW_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shadow logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0367` | `softness_rule` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOFTNESS_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar softness rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0368` | `contrast_ratio` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTRAST_RATIO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar contrast ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0369` | `color_temperature` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COLOR_TEMPERATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar color temperature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0370` | `ambient_light` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AMBIENT_LIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar ambient light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0371` | `practical_lights` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRACTICAL_LIGHTS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar practical lights con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0372` | `skin_highlight_control` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_HIGHLIGHT_CONTROL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin highlight control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0373` | `hair_rim_control` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_RIM_CONTROL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair rim control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0374` | `eye_light_rule` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_LIGHT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eye light rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0375` | `night_scene_rule` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NIGHT_SCENE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar night scene rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0376` | `lighting_mood_map` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIGHTING_MOOD_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lighting mood map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0377` | `scene_location` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_LOCATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar scene location con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0378` | `period_context` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERIOD_CONTEXT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar period context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0379` | `weather_rule` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WEATHER_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar weather rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0380` | `scale_contact` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCALE_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar scale contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0381` | `gravity_rules` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GRAVITY_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar gravity rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0382` | `reflection_rules` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REFLECTION_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar reflection rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0383` | `floor_contact` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLOOR_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar floor contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0384` | `wall_contact` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALL_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wall contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0385` | `background_depth` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BACKGROUND_DEPTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar background depth con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0386` | `object_scale` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar object scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0387` | `cultural_context_safe` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CULTURAL_CONTEXT_SAFE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar cultural context safe con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0388` | `lima_peru_context_option` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIMA_PERU_CONTEXT_OPTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lima peru context option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0389` | `set_dressing_logic` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SET_DRESSING_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar set dressing logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0390` | `scene_story_logic` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_STORY_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar scene story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0391` | `lens_face_distortion_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FACE_DISTORTION_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lens face distortion blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0392` | `impossible_light_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMPOSSIBLE_LIGHT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar impossible light blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0393` | `shadow_mismatch_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHADOW_MISMATCH_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shadow mismatch blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0394` | `scale_error_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCALE_ERROR_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar scale error blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0395` | `cgi_grading_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CGI_GRADING_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar cgi grading blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0396` | `background_identity_conflict_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BACKGROUND_IDENTITY_CONFLICT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar background identity conflict rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0397` | `scene_physics_repair_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_PHYSICS_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar scene physics repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0398` | `environment_continuity_test` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ENVIRONMENT_CONTINUITY_TEST_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar environment continuity test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0795` | `shot_type_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOT_TYPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shot type con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0796` | `camera_distance_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_DISTANCE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0797` | `camera_height_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_HEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0798` | `camera_angle_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_ANGLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0799` | `lens_focal_range_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FOCAL_RANGE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens focal range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0800` | `aperture_range_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_APERTURE_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar aperture range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0801` | `shutter_logic_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHUTTER_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shutter logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0802` | `iso_logic_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ISO_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iso logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0803` | `white_balance_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WHITE_BALANCE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar white balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0804` | `sensor_look_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SENSOR_LOOK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sensor look con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0805` | `depth_of_field_rule_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DEPTH_OF_FIELD_RULE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar depth of field rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0806` | `distortion_control_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DISTORTION_CONTROL_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar distortion control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0807` | `crop_safe_area_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CROP_SAFE_AREA_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar crop safe area con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0808` | `composition_grid_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMPOSITION_GRID_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar composition grid con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0809` | `negative_space_rule_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NEGATIVE_SPACE_RULE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar negative space rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0810` | `camera_body_relation_prompt_effect` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_BODY_RELATION_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera body relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0811` | `key_light_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KEY_LIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar key light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0812` | `fill_light_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FILL_LIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fill light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0813` | `rim_light_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RIM_LIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rim light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0814` | `catchlight_pattern_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CATCHLIGHT_PATTERN_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar catchlight pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0815` | `shadow_logic_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHADOW_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shadow logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0816` | `softness_rule_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOFTNESS_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar softness rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0817` | `contrast_ratio_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTRAST_RATIO_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contrast ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0818` | `color_temperature_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COLOR_TEMPERATURE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar color temperature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0819` | `ambient_light_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AMBIENT_LIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ambient light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0820` | `practical_lights_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRACTICAL_LIGHTS_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar practical lights con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0821` | `skin_highlight_control_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_HIGHLIGHT_CONTROL_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin highlight control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0822` | `hair_rim_control_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_RIM_CONTROL_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair rim control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0823` | `eye_light_rule_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_LIGHT_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye light rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0824` | `night_scene_rule_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NIGHT_SCENE_RULE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar night scene rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0825` | `lighting_mood_map_prompt_effect` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIGHTING_MOOD_MAP_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lighting mood map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0826` | `scene_location_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_LOCATION_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene location con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0827` | `period_context_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERIOD_CONTEXT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar period context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0828` | `weather_rule_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WEATHER_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar weather rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0829` | `scale_contact_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCALE_CONTACT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scale contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0830` | `gravity_rules_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GRAVITY_RULES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar gravity rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0831` | `reflection_rules_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REFLECTION_RULES_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar reflection rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0832` | `floor_contact_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLOOR_CONTACT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar floor contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0833` | `wall_contact_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALL_CONTACT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wall contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0834` | `background_depth_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BACKGROUND_DEPTH_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar background depth con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0835` | `object_scale_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_0836` | `cultural_context_safe_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CULTURAL_CONTEXT_SAFE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cultural context safe con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0837` | `lima_peru_context_option_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIMA_PERU_CONTEXT_OPTION_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lima peru context option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0838` | `set_dressing_logic_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SET_DRESSING_LOGIC_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar set dressing logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0839` | `scene_story_logic_prompt_effect` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_STORY_LOGIC_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0840` | `lens_face_distortion_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FACE_DISTORTION_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens face distortion blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0841` | `impossible_light_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMPOSSIBLE_LIGHT_BLOCKER_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar impossible light blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0842` | `shadow_mismatch_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHADOW_MISMATCH_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shadow mismatch blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0843` | `scale_error_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCALE_ERROR_BLOCKER_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scale error blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0844` | `cgi_grading_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CGI_GRADING_BLOCKER_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cgi grading blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_0845` | `background_identity_conflict_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BACKGROUND_IDENTITY_CONFLICT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar background identity conflict rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0846` | `scene_physics_repair_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_PHYSICS_REPAIR_RULE_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene physics repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0847` | `environment_continuity_test_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ENVIRONMENT_CONTINUITY_TEST__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar environment continuity test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1244` | `shot_type_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOT_TYPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shot type con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1245` | `camera_distance_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_DISTANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1246` | `camera_height_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_HEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1247` | `camera_angle_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_ANGLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1248` | `lens_focal_range_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FOCAL_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens focal range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1249` | `aperture_range_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_APERTURE_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar aperture range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1250` | `shutter_logic_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHUTTER_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shutter logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1251` | `iso_logic_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ISO_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iso logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1252` | `white_balance_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WHITE_BALANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar white balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1253` | `sensor_look_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SENSOR_LOOK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sensor look con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1254` | `depth_of_field_rule_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DEPTH_OF_FIELD_RULE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar depth of field rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1255` | `distortion_control_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DISTORTION_CONTROL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar distortion control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1256` | `crop_safe_area_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CROP_SAFE_AREA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar crop safe area con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1257` | `composition_grid_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMPOSITION_GRID_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar composition grid con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1258` | `negative_space_rule_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NEGATIVE_SPACE_RULE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar negative space rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1259` | `camera_body_relation_qa_matrix` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_BODY_RELATION_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera body relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1260` | `key_light_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KEY_LIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar key light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1261` | `fill_light_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FILL_LIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fill light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1262` | `rim_light_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RIM_LIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rim light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1263` | `catchlight_pattern_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CATCHLIGHT_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar catchlight pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1264` | `shadow_logic_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHADOW_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shadow logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1265` | `softness_rule_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOFTNESS_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar softness rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1266` | `contrast_ratio_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTRAST_RATIO_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contrast ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1267` | `color_temperature_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COLOR_TEMPERATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar color temperature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1268` | `ambient_light_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AMBIENT_LIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ambient light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1269` | `practical_lights_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRACTICAL_LIGHTS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar practical lights con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1270` | `skin_highlight_control_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_HIGHLIGHT_CONTROL_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin highlight control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1271` | `hair_rim_control_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_RIM_CONTROL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair rim control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1272` | `eye_light_rule_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_LIGHT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye light rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1273` | `night_scene_rule_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NIGHT_SCENE_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar night scene rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1274` | `lighting_mood_map_qa_matrix` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIGHTING_MOOD_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lighting mood map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1275` | `scene_location_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_LOCATION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene location con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1276` | `period_context_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERIOD_CONTEXT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar period context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1277` | `weather_rule_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WEATHER_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar weather rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1278` | `scale_contact_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCALE_CONTACT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scale contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1279` | `gravity_rules_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GRAVITY_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar gravity rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1280` | `reflection_rules_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REFLECTION_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar reflection rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1281` | `floor_contact_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLOOR_CONTACT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar floor contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1282` | `wall_contact_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALL_CONTACT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wall contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1283` | `background_depth_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BACKGROUND_DEPTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar background depth con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1284` | `object_scale_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_1285` | `cultural_context_safe_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CULTURAL_CONTEXT_SAFE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cultural context safe con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1286` | `lima_peru_context_option_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIMA_PERU_CONTEXT_OPTION_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lima peru context option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1287` | `set_dressing_logic_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SET_DRESSING_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar set dressing logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1288` | `scene_story_logic_qa_matrix` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_STORY_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1289` | `lens_face_distortion_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FACE_DISTORTION_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens face distortion blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1290` | `impossible_light_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMPOSSIBLE_LIGHT_BLOCKER_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar impossible light blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1291` | `shadow_mismatch_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHADOW_MISMATCH_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shadow mismatch blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1292` | `scale_error_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCALE_ERROR_BLOCKER_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scale error blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1293` | `cgi_grading_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CGI_GRADING_BLOCKER_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cgi grading blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1294` | `background_identity_conflict_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BACKGROUND_IDENTITY_CONFLICT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar background identity conflict rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1295` | `scene_physics_repair_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_PHYSICS_REPAIR_RULE_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene physics repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1296` | `environment_continuity_test_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ENVIRONMENT_CONTINUITY_TEST__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar environment continuity test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1693` | `shot_type_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOT_TYPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shot type con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1694` | `camera_distance_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_DISTANCE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1695` | `camera_height_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_HEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1696` | `camera_angle_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_ANGLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1697` | `lens_focal_range_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FOCAL_RANGE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens focal range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1698` | `aperture_range_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_APERTURE_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar aperture range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1699` | `shutter_logic_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHUTTER_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shutter logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1700` | `iso_logic_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ISO_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iso logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1701` | `white_balance_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WHITE_BALANCE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar white balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1702` | `sensor_look_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SENSOR_LOOK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sensor look con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1703` | `depth_of_field_rule_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DEPTH_OF_FIELD_RULE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar depth of field rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1704` | `distortion_control_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DISTORTION_CONTROL_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar distortion control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1705` | `crop_safe_area_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CROP_SAFE_AREA_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar crop safe area con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1706` | `composition_grid_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMPOSITION_GRID_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar composition grid con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1707` | `negative_space_rule_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NEGATIVE_SPACE_RULE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar negative space rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1708` | `camera_body_relation_vendor_repair` | camera | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_BODY_RELATION_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera body relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1709` | `key_light_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KEY_LIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar key light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1710` | `fill_light_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FILL_LIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fill light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1711` | `rim_light_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RIM_LIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rim light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1712` | `catchlight_pattern_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CATCHLIGHT_PATTERN_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar catchlight pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1713` | `shadow_logic_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHADOW_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shadow logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1714` | `softness_rule_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SOFTNESS_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar softness rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1715` | `contrast_ratio_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTRAST_RATIO_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contrast ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1716` | `color_temperature_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COLOR_TEMPERATURE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar color temperature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1717` | `ambient_light_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AMBIENT_LIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ambient light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1718` | `practical_lights_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PRACTICAL_LIGHTS_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar practical lights con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1719` | `skin_highlight_control_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_HIGHLIGHT_CONTROL_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin highlight control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1720` | `hair_rim_control_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_RIM_CONTROL_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair rim control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1721` | `eye_light_rule_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_LIGHT_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye light rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1722` | `night_scene_rule_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NIGHT_SCENE_RULE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar night scene rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1723` | `lighting_mood_map_vendor_repair` | lighting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIGHTING_MOOD_MAP_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lighting mood map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1724` | `scene_location_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_LOCATION_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene location con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1725` | `period_context_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PERIOD_CONTEXT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar period context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1726` | `weather_rule_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WEATHER_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar weather rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1727` | `scale_contact_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCALE_CONTACT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scale contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1728` | `gravity_rules_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GRAVITY_RULES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar gravity rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1729` | `reflection_rules_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_REFLECTION_RULES_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar reflection rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1730` | `floor_contact_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLOOR_CONTACT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar floor contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1731` | `wall_contact_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALL_CONTACT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wall contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1732` | `background_depth_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BACKGROUND_DEPTH_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar background depth con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1733` | `object_scale_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CULTURE_1734` | `cultural_context_safe_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CULTURAL_CONTEXT_SAFE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cultural context safe con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1735` | `lima_peru_context_option_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIMA_PERU_CONTEXT_OPTION_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lima peru context option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1736` | `set_dressing_logic_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SET_DRESSING_LOGIC_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar set dressing logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1737` | `scene_story_logic_vendor_repair` | scene | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_STORY_LOGIC_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1738` | `lens_face_distortion_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FACE_DISTORTION_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens face distortion blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1739` | `impossible_light_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMPOSSIBLE_LIGHT_BLOCKER_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar impossible light blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1740` | `shadow_mismatch_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHADOW_MISMATCH_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shadow mismatch blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1741` | `scale_error_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCALE_ERROR_BLOCKER_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scale error blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1742` | `cgi_grading_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CGI_GRADING_BLOCKER_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cgi grading blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PSYCHOLOGY_1743` | `background_identity_conflict_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BACKGROUND_IDENTITY_CONFLICT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar background identity conflict rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1744` | `scene_physics_repair_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCENE_PHYSICS_REPAIR_RULE_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar scene physics repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1745` | `environment_continuity_test_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ENVIRONMENT_CONTINUITY_TEST__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar environment continuity test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_CAMERA_0346 — shot_type
- Definición: Campo operativo para shot type dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shot type como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shot type como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOT_TYPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHOT_TYPE_DRIFT_OR_GAP
- Fallback: Reforzar shot type con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0347 — camera_distance
- Definición: Campo operativo para camera distance dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar camera distance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera distance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_DISTANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAMERA_DISTANCE_DRIFT_OR_GAP
- Fallback: Reforzar camera distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0348 — camera_height
- Definición: Campo operativo para camera height dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar camera height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_HEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAMERA_HEIGHT_DRIFT_OR_GAP
- Fallback: Reforzar camera height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0349 — camera_angle
- Definición: Campo operativo para camera angle dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar camera angle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera angle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_ANGLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAMERA_ANGLE_DRIFT_OR_GAP
- Fallback: Reforzar camera angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0350 — lens_focal_range
- Definición: Campo operativo para lens focal range dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lens focal range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens focal range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FOCAL_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LENS_FOCAL_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar lens focal range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0351 — aperture_range
- Definición: Campo operativo para aperture range dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar aperture range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar aperture range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_APERTURE_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_APERTURE_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar aperture range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0352 — shutter_logic
- Definición: Campo operativo para shutter logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shutter logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shutter logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHUTTER_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHUTTER_LOGIC_DRIFT_OR_GAP
- Fallback: Reforzar shutter logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0353 — iso_logic
- Definición: Campo operativo para iso logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar iso logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iso logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ISO_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ISO_LOGIC_DRIFT_OR_GAP
- Fallback: Reforzar iso logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0354 — white_balance
- Definición: Campo operativo para white balance dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar white balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar white balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WHITE_BALANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WHITE_BALANCE_DRIFT_OR_GAP
- Fallback: Reforzar white balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0355 — sensor_look
- Definición: Campo operativo para sensor look dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sensor look como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sensor look como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SENSOR_LOOK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SENSOR_LOOK_DRIFT_OR_GAP
- Fallback: Reforzar sensor look con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0356 — depth_of_field_rule
- Definición: Campo operativo para depth of field rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar depth of field rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar depth of field rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DEPTH_OF_FIELD_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DEPTH_OF_FIELD_RULE_DRIFT_OR_GAP
- Fallback: Reforzar depth of field rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0357 — distortion_control
- Definición: Campo operativo para distortion control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar distortion control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar distortion control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DISTORTION_CONTROL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DISTORTION_CONTROL_DRIFT_OR_GAP
- Fallback: Reforzar distortion control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0358 — crop_safe_area
- Definición: Campo operativo para crop safe area dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar crop safe area como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar crop safe area como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CROP_SAFE_AREA_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CROP_SAFE_AREA_DRIFT_OR_GAP
- Fallback: Reforzar crop safe area con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0359 — composition_grid
- Definición: Campo operativo para composition grid dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar composition grid como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar composition grid como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMPOSITION_GRID_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_COMPOSITION_GRID_DRIFT_OR_GAP
- Fallback: Reforzar composition grid con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0360 — negative_space_rule
- Definición: Campo operativo para negative space rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar negative space rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar negative space rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NEGATIVE_SPACE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NEGATIVE_SPACE_RULE_DRIFT_OR_GAP
- Fallback: Reforzar negative space rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0361 — camera_body_relation
- Definición: Campo operativo para camera body relation dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar camera body relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera body relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_BODY_RELATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAMERA_BODY_RELATION_DRIFT_OR_GAP
- Fallback: Reforzar camera body relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0362 — key_light
- Definición: Campo operativo para key light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar key light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar key light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KEY_LIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_KEY_LIGHT_DRIFT_OR_GAP
- Fallback: Reforzar key light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0363 — fill_light
- Definición: Campo operativo para fill light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fill light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fill light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FILL_LIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FILL_LIGHT_DRIFT_OR_GAP
- Fallback: Reforzar fill light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0364 — rim_light
- Definición: Campo operativo para rim light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar rim light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rim light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RIM_LIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_RIM_LIGHT_DRIFT_OR_GAP
- Fallback: Reforzar rim light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0365 — catchlight_pattern
- Definición: Campo operativo para catchlight pattern dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar catchlight pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar catchlight pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CATCHLIGHT_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CATCHLIGHT_PATTERN_DRIFT_OR_GAP
- Fallback: Reforzar catchlight pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0366 — shadow_logic
- Definición: Campo operativo para shadow logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shadow logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shadow logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHADOW_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHADOW_LOGIC_DRIFT_OR_GAP
- Fallback: Reforzar shadow logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0367 — softness_rule
- Definición: Campo operativo para softness rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar softness rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar softness rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOFTNESS_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SOFTNESS_RULE_DRIFT_OR_GAP
- Fallback: Reforzar softness rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0368 — contrast_ratio
- Definición: Campo operativo para contrast ratio dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar contrast ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contrast ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTRAST_RATIO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CONTRAST_RATIO_DRIFT_OR_GAP
- Fallback: Reforzar contrast ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0369 — color_temperature
- Definición: Campo operativo para color temperature dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar color temperature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar color temperature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COLOR_TEMPERATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_COLOR_TEMPERATURE_DRIFT_OR_GAP
- Fallback: Reforzar color temperature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0370 — ambient_light
- Definición: Campo operativo para ambient light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar ambient light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ambient light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AMBIENT_LIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_AMBIENT_LIGHT_DRIFT_OR_GAP
- Fallback: Reforzar ambient light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0371 — practical_lights
- Definición: Campo operativo para practical lights dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar practical lights como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar practical lights como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRACTICAL_LIGHTS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PRACTICAL_LIGHTS_DRIFT_OR_GAP
- Fallback: Reforzar practical lights con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0372 — skin_highlight_control
- Definición: Campo operativo para skin highlight control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin highlight control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin highlight control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_HIGHLIGHT_CONTROL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_HIGHLIGHT_CONTROL_DRIFT_OR_GAP
- Fallback: Reforzar skin highlight control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0373 — hair_rim_control
- Definición: Campo operativo para hair rim control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair rim control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair rim control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_RIM_CONTROL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_RIM_CONTROL_DRIFT_OR_GAP
- Fallback: Reforzar hair rim control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0374 — eye_light_rule
- Definición: Campo operativo para eye light rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eye light rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye light rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_LIGHT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYE_LIGHT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar eye light rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0375 — night_scene_rule
- Definición: Campo operativo para night scene rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar night scene rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar night scene rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NIGHT_SCENE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NIGHT_SCENE_RULE_DRIFT_OR_GAP
- Fallback: Reforzar night scene rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0376 — lighting_mood_map
- Definición: Campo operativo para lighting mood map dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lighting mood map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lighting mood map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIGHTING_MOOD_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LIGHTING_MOOD_MAP_DRIFT_OR_GAP
- Fallback: Reforzar lighting mood map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0377 — scene_location
- Definición: Campo operativo para scene location dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar scene location como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene location como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_LOCATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCENE_LOCATION_DRIFT_OR_GAP
- Fallback: Reforzar scene location con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0378 — period_context
- Definición: Campo operativo para period context dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar period context como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar period context como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERIOD_CONTEXT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PERIOD_CONTEXT_DRIFT_OR_GAP
- Fallback: Reforzar period context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0379 — weather_rule
- Definición: Campo operativo para weather rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar weather rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar weather rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WEATHER_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WEATHER_RULE_DRIFT_OR_GAP
- Fallback: Reforzar weather rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0380 — scale_contact
- Definición: Campo operativo para scale contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar scale contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scale contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCALE_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCALE_CONTACT_DRIFT_OR_GAP
- Fallback: Reforzar scale contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0381 — gravity_rules
- Definición: Campo operativo para gravity rules dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar gravity rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar gravity rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GRAVITY_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_GRAVITY_RULES_DRIFT_OR_GAP
- Fallback: Reforzar gravity rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0382 — reflection_rules
- Definición: Campo operativo para reflection rules dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar reflection rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar reflection rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REFLECTION_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_REFLECTION_RULES_DRIFT_OR_GAP
- Fallback: Reforzar reflection rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0383 — floor_contact
- Definición: Campo operativo para floor contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar floor contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar floor contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLOOR_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FLOOR_CONTACT_DRIFT_OR_GAP
- Fallback: Reforzar floor contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0384 — wall_contact
- Definición: Campo operativo para wall contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wall contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wall contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALL_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WALL_CONTACT_DRIFT_OR_GAP
- Fallback: Reforzar wall contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0385 — background_depth
- Definición: Campo operativo para background depth dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar background depth como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar background depth como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BACKGROUND_DEPTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BACKGROUND_DEPTH_DRIFT_OR_GAP
- Fallback: Reforzar background depth con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0386 — object_scale
- Definición: Campo operativo para object scale dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar object scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_OBJECT_SCALE_DRIFT_OR_GAP
- Fallback: Reforzar object scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0387 — cultural_context_safe
- Definición: Campo operativo para cultural context safe dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar cultural context safe como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cultural context safe como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CULTURAL_CONTEXT_SAFE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CULTURAL_CONTEXT_SAFE_DRIFT_OR_GAP
- Fallback: Reforzar cultural context safe con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0388 — lima_peru_context_option
- Definición: Campo operativo para lima peru context option dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lima peru context option como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lima peru context option como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIMA_PERU_CONTEXT_OPTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LIMA_PERU_CONTEXT_OPTION_DRIFT_OR_GAP
- Fallback: Reforzar lima peru context option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0389 — set_dressing_logic
- Definición: Campo operativo para set dressing logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar set dressing logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar set dressing logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SET_DRESSING_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SET_DRESSING_LOGIC_DRIFT_OR_GAP
- Fallback: Reforzar set dressing logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0390 — scene_story_logic
- Definición: Campo operativo para scene story logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar scene story logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene story logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_STORY_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCENE_STORY_LOGIC_DRIFT_OR_GAP
- Fallback: Reforzar scene story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0391 — lens_face_distortion_blocker
- Definición: Campo operativo para lens face distortion blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lens face distortion blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens face distortion blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FACE_DISTORTION_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LENS_FACE_DISTORTION_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar lens face distortion blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0392 — impossible_light_blocker
- Definición: Campo operativo para impossible light blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar impossible light blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar impossible light blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMPOSSIBLE_LIGHT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_IMPOSSIBLE_LIGHT_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar impossible light blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0393 — shadow_mismatch_blocker
- Definición: Campo operativo para shadow mismatch blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shadow mismatch blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shadow mismatch blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHADOW_MISMATCH_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHADOW_MISMATCH_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar shadow mismatch blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0394 — scale_error_blocker
- Definición: Campo operativo para scale error blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar scale error blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scale error blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCALE_ERROR_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCALE_ERROR_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar scale error blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0395 — cgi_grading_blocker
- Definición: Campo operativo para cgi grading blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar cgi grading blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cgi grading blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CGI_GRADING_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CGI_GRADING_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar cgi grading blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0396 — background_identity_conflict_rule
- Definición: Campo operativo para background identity conflict rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar background identity conflict rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar background identity conflict rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BACKGROUND_IDENTITY_CONFLICT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BACKGROUND_IDENTITY_CONFLICT_RUL_DRIFT_OR_GAP
- Fallback: Reforzar background identity conflict rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0397 — scene_physics_repair_rule
- Definición: Campo operativo para scene physics repair rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar scene physics repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene physics repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_PHYSICS_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCENE_PHYSICS_REPAIR_RULE_DRIFT_OR_GAP
- Fallback: Reforzar scene physics repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0398 — environment_continuity_test
- Definición: Campo operativo para environment continuity test dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar environment continuity test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar environment continuity test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ENVIRONMENT_CONTINUITY_TEST_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ENVIRONMENT_CONTINUITY_TEST_DRIFT_OR_GAP
- Fallback: Reforzar environment continuity test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0795 — shot_type_prompt_effect
- Definición: Campo operativo para shot type dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shot type como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shot type como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOT_TYPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOT_TYPE_PROMPT_EFFECT
- Fallback: Reforzar shot type con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0796 — camera_distance_prompt_effect
- Definición: Campo operativo para camera distance dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera distance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera distance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_DISTANCE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_DISTANCE_PROMPT_EFFECT
- Fallback: Reforzar camera distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0797 — camera_height_prompt_effect
- Definición: Campo operativo para camera height dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_HEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_HEIGHT_PROMPT_EFFECT
- Fallback: Reforzar camera height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0798 — camera_angle_prompt_effect
- Definición: Campo operativo para camera angle dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera angle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera angle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_ANGLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_ANGLE_PROMPT_EFFECT
- Fallback: Reforzar camera angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0799 — lens_focal_range_prompt_effect
- Definición: Campo operativo para lens focal range dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens focal range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens focal range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FOCAL_RANGE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FOCAL_RANGE_PROMPT_EFFECT
- Fallback: Reforzar lens focal range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0800 — aperture_range_prompt_effect
- Definición: Campo operativo para aperture range dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar aperture range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar aperture range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_APERTURE_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_APERTURE_RANGE_PROMPT_EFFECT
- Fallback: Reforzar aperture range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0801 — shutter_logic_prompt_effect
- Definición: Campo operativo para shutter logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shutter logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shutter logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHUTTER_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHUTTER_LOGIC_PROMPT_EFFECT
- Fallback: Reforzar shutter logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0802 — iso_logic_prompt_effect
- Definición: Campo operativo para iso logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iso logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iso logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ISO_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ISO_LOGIC_PROMPT_EFFECT
- Fallback: Reforzar iso logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0803 — white_balance_prompt_effect
- Definición: Campo operativo para white balance dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar white balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar white balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WHITE_BALANCE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WHITE_BALANCE_PROMPT_EFFECT
- Fallback: Reforzar white balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0804 — sensor_look_prompt_effect
- Definición: Campo operativo para sensor look dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sensor look como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sensor look como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SENSOR_LOOK_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SENSOR_LOOK_PROMPT_EFFECT
- Fallback: Reforzar sensor look con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0805 — depth_of_field_rule_prompt_effect
- Definición: Campo operativo para depth of field rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar depth of field rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar depth of field rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DEPTH_OF_FIELD_RULE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DEPTH_OF_FIELD_RULE_PROMPT_EFFEC
- Fallback: Reforzar depth of field rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0806 — distortion_control_prompt_effect
- Definición: Campo operativo para distortion control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar distortion control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar distortion control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DISTORTION_CONTROL_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DISTORTION_CONTROL_PROMPT_EFFECT
- Fallback: Reforzar distortion control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0807 — crop_safe_area_prompt_effect
- Definición: Campo operativo para crop safe area dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar crop safe area como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar crop safe area como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CROP_SAFE_AREA_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CROP_SAFE_AREA_PROMPT_EFFECT
- Fallback: Reforzar crop safe area con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0808 — composition_grid_prompt_effect
- Definición: Campo operativo para composition grid dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar composition grid como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar composition grid como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMPOSITION_GRID_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMPOSITION_GRID_PROMPT_EFFECT
- Fallback: Reforzar composition grid con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0809 — negative_space_rule_prompt_effect
- Definición: Campo operativo para negative space rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar negative space rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar negative space rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NEGATIVE_SPACE_RULE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NEGATIVE_SPACE_RULE_PROMPT_EFFEC
- Fallback: Reforzar negative space rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0810 — camera_body_relation_prompt_effect
- Definición: Campo operativo para camera body relation dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera body relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera body relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_BODY_RELATION_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_BODY_RELATION_PROMPT_EFFE
- Fallback: Reforzar camera body relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0811 — key_light_prompt_effect
- Definición: Campo operativo para key light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar key light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar key light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KEY_LIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KEY_LIGHT_PROMPT_EFFECT
- Fallback: Reforzar key light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0812 — fill_light_prompt_effect
- Definición: Campo operativo para fill light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fill light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fill light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FILL_LIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FILL_LIGHT_PROMPT_EFFECT
- Fallback: Reforzar fill light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0813 — rim_light_prompt_effect
- Definición: Campo operativo para rim light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rim light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rim light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RIM_LIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RIM_LIGHT_PROMPT_EFFECT
- Fallback: Reforzar rim light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0814 — catchlight_pattern_prompt_effect
- Definición: Campo operativo para catchlight pattern dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar catchlight pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar catchlight pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CATCHLIGHT_PATTERN_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CATCHLIGHT_PATTERN_PROMPT_EFFECT
- Fallback: Reforzar catchlight pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0815 — shadow_logic_prompt_effect
- Definición: Campo operativo para shadow logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shadow logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shadow logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHADOW_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHADOW_LOGIC_PROMPT_EFFECT
- Fallback: Reforzar shadow logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0816 — softness_rule_prompt_effect
- Definición: Campo operativo para softness rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar softness rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar softness rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOFTNESS_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOFTNESS_RULE_PROMPT_EFFECT
- Fallback: Reforzar softness rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0817 — contrast_ratio_prompt_effect
- Definición: Campo operativo para contrast ratio dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contrast ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contrast ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTRAST_RATIO_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTRAST_RATIO_PROMPT_EFFECT
- Fallback: Reforzar contrast ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0818 — color_temperature_prompt_effect
- Definición: Campo operativo para color temperature dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar color temperature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar color temperature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COLOR_TEMPERATURE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COLOR_TEMPERATURE_PROMPT_EFFECT
- Fallback: Reforzar color temperature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0819 — ambient_light_prompt_effect
- Definición: Campo operativo para ambient light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ambient light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ambient light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AMBIENT_LIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AMBIENT_LIGHT_PROMPT_EFFECT
- Fallback: Reforzar ambient light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0820 — practical_lights_prompt_effect
- Definición: Campo operativo para practical lights dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar practical lights como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar practical lights como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRACTICAL_LIGHTS_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRACTICAL_LIGHTS_PROMPT_EFFECT
- Fallback: Reforzar practical lights con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0821 — skin_highlight_control_prompt_effect
- Definición: Campo operativo para skin highlight control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin highlight control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin highlight control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_HIGHLIGHT_CONTROL_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_HIGHLIGHT_CONTROL_PROMPT_EF
- Fallback: Reforzar skin highlight control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0822 — hair_rim_control_prompt_effect
- Definición: Campo operativo para hair rim control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair rim control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair rim control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_RIM_CONTROL_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_RIM_CONTROL_PROMPT_EFFECT
- Fallback: Reforzar hair rim control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0823 — eye_light_rule_prompt_effect
- Definición: Campo operativo para eye light rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye light rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye light rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_LIGHT_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_LIGHT_RULE_PROMPT_EFFECT
- Fallback: Reforzar eye light rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0824 — night_scene_rule_prompt_effect
- Definición: Campo operativo para night scene rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar night scene rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar night scene rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NIGHT_SCENE_RULE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NIGHT_SCENE_RULE_PROMPT_EFFECT
- Fallback: Reforzar night scene rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0825 — lighting_mood_map_prompt_effect
- Definición: Campo operativo para lighting mood map dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lighting mood map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lighting mood map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIGHTING_MOOD_MAP_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIGHTING_MOOD_MAP_PROMPT_EFFECT
- Fallback: Reforzar lighting mood map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0826 — scene_location_prompt_effect
- Definición: Campo operativo para scene location dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene location como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene location como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_LOCATION_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_LOCATION_PROMPT_EFFECT
- Fallback: Reforzar scene location con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0827 — period_context_prompt_effect
- Definición: Campo operativo para period context dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar period context como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar period context como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERIOD_CONTEXT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERIOD_CONTEXT_PROMPT_EFFECT
- Fallback: Reforzar period context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0828 — weather_rule_prompt_effect
- Definición: Campo operativo para weather rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar weather rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar weather rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WEATHER_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WEATHER_RULE_PROMPT_EFFECT
- Fallback: Reforzar weather rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0829 — scale_contact_prompt_effect
- Definición: Campo operativo para scale contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scale contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scale contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCALE_CONTACT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCALE_CONTACT_PROMPT_EFFECT
- Fallback: Reforzar scale contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0830 — gravity_rules_prompt_effect
- Definición: Campo operativo para gravity rules dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar gravity rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar gravity rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GRAVITY_RULES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GRAVITY_RULES_PROMPT_EFFECT
- Fallback: Reforzar gravity rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0831 — reflection_rules_prompt_effect
- Definición: Campo operativo para reflection rules dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar reflection rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar reflection rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REFLECTION_RULES_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REFLECTION_RULES_PROMPT_EFFECT
- Fallback: Reforzar reflection rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0832 — floor_contact_prompt_effect
- Definición: Campo operativo para floor contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar floor contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar floor contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLOOR_CONTACT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLOOR_CONTACT_PROMPT_EFFECT
- Fallback: Reforzar floor contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0833 — wall_contact_prompt_effect
- Definición: Campo operativo para wall contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wall contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wall contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALL_CONTACT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALL_CONTACT_PROMPT_EFFECT
- Fallback: Reforzar wall contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0834 — background_depth_prompt_effect
- Definición: Campo operativo para background depth dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar background depth como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar background depth como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BACKGROUND_DEPTH_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BACKGROUND_DEPTH_PROMPT_EFFECT
- Fallback: Reforzar background depth con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0835 — object_scale_prompt_effect
- Definición: Campo operativo para object scale dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_SCALE_PROMPT_EFFECT
- Fallback: Reforzar object scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_0836 — cultural_context_safe_prompt_effect
- Definición: Campo operativo para cultural context safe dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cultural context safe como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cultural context safe como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CULTURAL_CONTEXT_SAFE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CULTURAL_CONTEXT_SAFE_PROMPT_EFF
- Fallback: Reforzar cultural context safe con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0837 — lima_peru_context_option_prompt_effect
- Definición: Campo operativo para lima peru context option dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lima peru context option como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lima peru context option como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIMA_PERU_CONTEXT_OPTION_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIMA_PERU_CONTEXT_OPTION_PROMPT_
- Fallback: Reforzar lima peru context option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0838 — set_dressing_logic_prompt_effect
- Definición: Campo operativo para set dressing logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar set dressing logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar set dressing logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SET_DRESSING_LOGIC_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SET_DRESSING_LOGIC_PROMPT_EFFECT
- Fallback: Reforzar set dressing logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0839 — scene_story_logic_prompt_effect
- Definición: Campo operativo para scene story logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene story logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene story logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_STORY_LOGIC_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_STORY_LOGIC_PROMPT_EFFECT
- Fallback: Reforzar scene story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0840 — lens_face_distortion_blocker_prompt_effect
- Definición: Campo operativo para lens face distortion blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens face distortion blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens face distortion blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FACE_DISTORTION_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FACE_DISTORTION_BLOCKER_PRO
- Fallback: Reforzar lens face distortion blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0841 — impossible_light_blocker_prompt_effect
- Definición: Campo operativo para impossible light blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar impossible light blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar impossible light blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMPOSSIBLE_LIGHT_BLOCKER_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMPOSSIBLE_LIGHT_BLOCKER_PROMPT_
- Fallback: Reforzar impossible light blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0842 — shadow_mismatch_blocker_prompt_effect
- Definición: Campo operativo para shadow mismatch blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shadow mismatch blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shadow mismatch blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHADOW_MISMATCH_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHADOW_MISMATCH_BLOCKER_PROMPT_E
- Fallback: Reforzar shadow mismatch blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0843 — scale_error_blocker_prompt_effect
- Definición: Campo operativo para scale error blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scale error blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scale error blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCALE_ERROR_BLOCKER_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCALE_ERROR_BLOCKER_PROMPT_EFFEC
- Fallback: Reforzar scale error blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0844 — cgi_grading_blocker_prompt_effect
- Definición: Campo operativo para cgi grading blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cgi grading blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cgi grading blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CGI_GRADING_BLOCKER_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CGI_GRADING_BLOCKER_PROMPT_EFFEC
- Fallback: Reforzar cgi grading blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_0845 — background_identity_conflict_rule_prompt_effect
- Definición: Campo operativo para background identity conflict rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar background identity conflict rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar background identity conflict rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BACKGROUND_IDENTITY_CONFLICT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BACKGROUND_IDENTITY_CONFLICT_RUL
- Fallback: Reforzar background identity conflict rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0846 — scene_physics_repair_rule_prompt_effect
- Definición: Campo operativo para scene physics repair rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene physics repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene physics repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_PHYSICS_REPAIR_RULE_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_PHYSICS_REPAIR_RULE_PROMPT
- Fallback: Reforzar scene physics repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0847 — environment_continuity_test_prompt_effect
- Definición: Campo operativo para environment continuity test dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar environment continuity test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar environment continuity test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ENVIRONMENT_CONTINUITY_TEST__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ENVIRONMENT_CONTINUITY_TEST_PROM
- Fallback: Reforzar environment continuity test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1244 — shot_type_qa_matrix
- Definición: Campo operativo para shot type dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shot type como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shot type como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOT_TYPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOT_TYPE_QA_MATRIX
- Fallback: Reforzar shot type con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1245 — camera_distance_qa_matrix
- Definición: Campo operativo para camera distance dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera distance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera distance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_DISTANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_DISTANCE_QA_MATRIX
- Fallback: Reforzar camera distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1246 — camera_height_qa_matrix
- Definición: Campo operativo para camera height dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_HEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_HEIGHT_QA_MATRIX
- Fallback: Reforzar camera height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1247 — camera_angle_qa_matrix
- Definición: Campo operativo para camera angle dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera angle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera angle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_ANGLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_ANGLE_QA_MATRIX
- Fallback: Reforzar camera angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1248 — lens_focal_range_qa_matrix
- Definición: Campo operativo para lens focal range dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens focal range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens focal range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FOCAL_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FOCAL_RANGE_QA_MATRIX
- Fallback: Reforzar lens focal range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1249 — aperture_range_qa_matrix
- Definición: Campo operativo para aperture range dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar aperture range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar aperture range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_APERTURE_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_APERTURE_RANGE_QA_MATRIX
- Fallback: Reforzar aperture range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1250 — shutter_logic_qa_matrix
- Definición: Campo operativo para shutter logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shutter logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shutter logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHUTTER_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHUTTER_LOGIC_QA_MATRIX
- Fallback: Reforzar shutter logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1251 — iso_logic_qa_matrix
- Definición: Campo operativo para iso logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iso logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iso logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ISO_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ISO_LOGIC_QA_MATRIX
- Fallback: Reforzar iso logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1252 — white_balance_qa_matrix
- Definición: Campo operativo para white balance dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar white balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar white balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WHITE_BALANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WHITE_BALANCE_QA_MATRIX
- Fallback: Reforzar white balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1253 — sensor_look_qa_matrix
- Definición: Campo operativo para sensor look dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sensor look como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sensor look como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SENSOR_LOOK_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SENSOR_LOOK_QA_MATRIX
- Fallback: Reforzar sensor look con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1254 — depth_of_field_rule_qa_matrix
- Definición: Campo operativo para depth of field rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar depth of field rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar depth of field rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DEPTH_OF_FIELD_RULE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DEPTH_OF_FIELD_RULE_QA_MATRIX
- Fallback: Reforzar depth of field rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1255 — distortion_control_qa_matrix
- Definición: Campo operativo para distortion control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar distortion control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar distortion control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DISTORTION_CONTROL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DISTORTION_CONTROL_QA_MATRIX
- Fallback: Reforzar distortion control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1256 — crop_safe_area_qa_matrix
- Definición: Campo operativo para crop safe area dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar crop safe area como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar crop safe area como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CROP_SAFE_AREA_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CROP_SAFE_AREA_QA_MATRIX
- Fallback: Reforzar crop safe area con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1257 — composition_grid_qa_matrix
- Definición: Campo operativo para composition grid dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar composition grid como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar composition grid como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMPOSITION_GRID_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMPOSITION_GRID_QA_MATRIX
- Fallback: Reforzar composition grid con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1258 — negative_space_rule_qa_matrix
- Definición: Campo operativo para negative space rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar negative space rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar negative space rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NEGATIVE_SPACE_RULE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NEGATIVE_SPACE_RULE_QA_MATRIX
- Fallback: Reforzar negative space rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1259 — camera_body_relation_qa_matrix
- Definición: Campo operativo para camera body relation dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera body relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera body relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_BODY_RELATION_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_BODY_RELATION_QA_MATRIX
- Fallback: Reforzar camera body relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1260 — key_light_qa_matrix
- Definición: Campo operativo para key light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar key light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar key light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KEY_LIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KEY_LIGHT_QA_MATRIX
- Fallback: Reforzar key light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1261 — fill_light_qa_matrix
- Definición: Campo operativo para fill light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fill light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fill light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FILL_LIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FILL_LIGHT_QA_MATRIX
- Fallback: Reforzar fill light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1262 — rim_light_qa_matrix
- Definición: Campo operativo para rim light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rim light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rim light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RIM_LIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RIM_LIGHT_QA_MATRIX
- Fallback: Reforzar rim light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1263 — catchlight_pattern_qa_matrix
- Definición: Campo operativo para catchlight pattern dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar catchlight pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar catchlight pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CATCHLIGHT_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CATCHLIGHT_PATTERN_QA_MATRIX
- Fallback: Reforzar catchlight pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1264 — shadow_logic_qa_matrix
- Definición: Campo operativo para shadow logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shadow logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shadow logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHADOW_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHADOW_LOGIC_QA_MATRIX
- Fallback: Reforzar shadow logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1265 — softness_rule_qa_matrix
- Definición: Campo operativo para softness rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar softness rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar softness rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOFTNESS_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOFTNESS_RULE_QA_MATRIX
- Fallback: Reforzar softness rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1266 — contrast_ratio_qa_matrix
- Definición: Campo operativo para contrast ratio dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contrast ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contrast ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTRAST_RATIO_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTRAST_RATIO_QA_MATRIX
- Fallback: Reforzar contrast ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1267 — color_temperature_qa_matrix
- Definición: Campo operativo para color temperature dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar color temperature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar color temperature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COLOR_TEMPERATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COLOR_TEMPERATURE_QA_MATRIX
- Fallback: Reforzar color temperature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1268 — ambient_light_qa_matrix
- Definición: Campo operativo para ambient light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ambient light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ambient light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AMBIENT_LIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AMBIENT_LIGHT_QA_MATRIX
- Fallback: Reforzar ambient light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1269 — practical_lights_qa_matrix
- Definición: Campo operativo para practical lights dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar practical lights como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar practical lights como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRACTICAL_LIGHTS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRACTICAL_LIGHTS_QA_MATRIX
- Fallback: Reforzar practical lights con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1270 — skin_highlight_control_qa_matrix
- Definición: Campo operativo para skin highlight control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin highlight control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin highlight control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_HIGHLIGHT_CONTROL_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_HIGHLIGHT_CONTROL_QA_MATRIX
- Fallback: Reforzar skin highlight control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1271 — hair_rim_control_qa_matrix
- Definición: Campo operativo para hair rim control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair rim control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair rim control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_RIM_CONTROL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_RIM_CONTROL_QA_MATRIX
- Fallback: Reforzar hair rim control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1272 — eye_light_rule_qa_matrix
- Definición: Campo operativo para eye light rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye light rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye light rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_LIGHT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_LIGHT_RULE_QA_MATRIX
- Fallback: Reforzar eye light rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1273 — night_scene_rule_qa_matrix
- Definición: Campo operativo para night scene rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar night scene rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar night scene rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NIGHT_SCENE_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NIGHT_SCENE_RULE_QA_MATRIX
- Fallback: Reforzar night scene rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1274 — lighting_mood_map_qa_matrix
- Definición: Campo operativo para lighting mood map dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lighting mood map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lighting mood map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIGHTING_MOOD_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIGHTING_MOOD_MAP_QA_MATRIX
- Fallback: Reforzar lighting mood map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1275 — scene_location_qa_matrix
- Definición: Campo operativo para scene location dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene location como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene location como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_LOCATION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_LOCATION_QA_MATRIX
- Fallback: Reforzar scene location con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1276 — period_context_qa_matrix
- Definición: Campo operativo para period context dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar period context como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar period context como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERIOD_CONTEXT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERIOD_CONTEXT_QA_MATRIX
- Fallback: Reforzar period context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1277 — weather_rule_qa_matrix
- Definición: Campo operativo para weather rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar weather rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar weather rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WEATHER_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WEATHER_RULE_QA_MATRIX
- Fallback: Reforzar weather rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1278 — scale_contact_qa_matrix
- Definición: Campo operativo para scale contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scale contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scale contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCALE_CONTACT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCALE_CONTACT_QA_MATRIX
- Fallback: Reforzar scale contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1279 — gravity_rules_qa_matrix
- Definición: Campo operativo para gravity rules dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar gravity rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar gravity rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GRAVITY_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GRAVITY_RULES_QA_MATRIX
- Fallback: Reforzar gravity rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1280 — reflection_rules_qa_matrix
- Definición: Campo operativo para reflection rules dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar reflection rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar reflection rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REFLECTION_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REFLECTION_RULES_QA_MATRIX
- Fallback: Reforzar reflection rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1281 — floor_contact_qa_matrix
- Definición: Campo operativo para floor contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar floor contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar floor contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLOOR_CONTACT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLOOR_CONTACT_QA_MATRIX
- Fallback: Reforzar floor contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1282 — wall_contact_qa_matrix
- Definición: Campo operativo para wall contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wall contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wall contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALL_CONTACT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALL_CONTACT_QA_MATRIX
- Fallback: Reforzar wall contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1283 — background_depth_qa_matrix
- Definición: Campo operativo para background depth dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar background depth como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar background depth como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BACKGROUND_DEPTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BACKGROUND_DEPTH_QA_MATRIX
- Fallback: Reforzar background depth con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1284 — object_scale_qa_matrix
- Definición: Campo operativo para object scale dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_SCALE_QA_MATRIX
- Fallback: Reforzar object scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_1285 — cultural_context_safe_qa_matrix
- Definición: Campo operativo para cultural context safe dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cultural context safe como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cultural context safe como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CULTURAL_CONTEXT_SAFE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CULTURAL_CONTEXT_SAFE_QA_MATRIX
- Fallback: Reforzar cultural context safe con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1286 — lima_peru_context_option_qa_matrix
- Definición: Campo operativo para lima peru context option dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lima peru context option como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lima peru context option como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIMA_PERU_CONTEXT_OPTION_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIMA_PERU_CONTEXT_OPTION_QA_MATR
- Fallback: Reforzar lima peru context option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1287 — set_dressing_logic_qa_matrix
- Definición: Campo operativo para set dressing logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar set dressing logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar set dressing logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SET_DRESSING_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SET_DRESSING_LOGIC_QA_MATRIX
- Fallback: Reforzar set dressing logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1288 — scene_story_logic_qa_matrix
- Definición: Campo operativo para scene story logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene story logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene story logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_STORY_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_STORY_LOGIC_QA_MATRIX
- Fallback: Reforzar scene story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1289 — lens_face_distortion_blocker_qa_matrix
- Definición: Campo operativo para lens face distortion blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens face distortion blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens face distortion blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FACE_DISTORTION_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FACE_DISTORTION_BLOCKER_QA_
- Fallback: Reforzar lens face distortion blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1290 — impossible_light_blocker_qa_matrix
- Definición: Campo operativo para impossible light blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar impossible light blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar impossible light blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMPOSSIBLE_LIGHT_BLOCKER_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMPOSSIBLE_LIGHT_BLOCKER_QA_MATR
- Fallback: Reforzar impossible light blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1291 — shadow_mismatch_blocker_qa_matrix
- Definición: Campo operativo para shadow mismatch blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shadow mismatch blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shadow mismatch blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHADOW_MISMATCH_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHADOW_MISMATCH_BLOCKER_QA_MATRI
- Fallback: Reforzar shadow mismatch blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1292 — scale_error_blocker_qa_matrix
- Definición: Campo operativo para scale error blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scale error blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scale error blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCALE_ERROR_BLOCKER_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCALE_ERROR_BLOCKER_QA_MATRIX
- Fallback: Reforzar scale error blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1293 — cgi_grading_blocker_qa_matrix
- Definición: Campo operativo para cgi grading blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cgi grading blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cgi grading blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CGI_GRADING_BLOCKER_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CGI_GRADING_BLOCKER_QA_MATRIX
- Fallback: Reforzar cgi grading blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1294 — background_identity_conflict_rule_qa_matrix
- Definición: Campo operativo para background identity conflict rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar background identity conflict rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar background identity conflict rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BACKGROUND_IDENTITY_CONFLICT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BACKGROUND_IDENTITY_CONFLICT_RUL
- Fallback: Reforzar background identity conflict rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1295 — scene_physics_repair_rule_qa_matrix
- Definición: Campo operativo para scene physics repair rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene physics repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene physics repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_PHYSICS_REPAIR_RULE_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_PHYSICS_REPAIR_RULE_QA_MAT
- Fallback: Reforzar scene physics repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1296 — environment_continuity_test_qa_matrix
- Definición: Campo operativo para environment continuity test dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar environment continuity test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar environment continuity test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ENVIRONMENT_CONTINUITY_TEST__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ENVIRONMENT_CONTINUITY_TEST_QA_M
- Fallback: Reforzar environment continuity test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1693 — shot_type_vendor_repair
- Definición: Campo operativo para shot type dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shot type como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shot type como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOT_TYPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOT_TYPE_VENDOR_REPAIR
- Fallback: Reforzar shot type con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1694 — camera_distance_vendor_repair
- Definición: Campo operativo para camera distance dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera distance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera distance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_DISTANCE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_DISTANCE_VENDOR_REPAIR
- Fallback: Reforzar camera distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1695 — camera_height_vendor_repair
- Definición: Campo operativo para camera height dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_HEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_HEIGHT_VENDOR_REPAIR
- Fallback: Reforzar camera height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1696 — camera_angle_vendor_repair
- Definición: Campo operativo para camera angle dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera angle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera angle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_ANGLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_ANGLE_VENDOR_REPAIR
- Fallback: Reforzar camera angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1697 — lens_focal_range_vendor_repair
- Definición: Campo operativo para lens focal range dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens focal range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens focal range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FOCAL_RANGE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FOCAL_RANGE_VENDOR_REPAIR
- Fallback: Reforzar lens focal range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1698 — aperture_range_vendor_repair
- Definición: Campo operativo para aperture range dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar aperture range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar aperture range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_APERTURE_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_APERTURE_RANGE_VENDOR_REPAIR
- Fallback: Reforzar aperture range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1699 — shutter_logic_vendor_repair
- Definición: Campo operativo para shutter logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shutter logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shutter logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHUTTER_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHUTTER_LOGIC_VENDOR_REPAIR
- Fallback: Reforzar shutter logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1700 — iso_logic_vendor_repair
- Definición: Campo operativo para iso logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iso logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iso logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ISO_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ISO_LOGIC_VENDOR_REPAIR
- Fallback: Reforzar iso logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1701 — white_balance_vendor_repair
- Definición: Campo operativo para white balance dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar white balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar white balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WHITE_BALANCE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WHITE_BALANCE_VENDOR_REPAIR
- Fallback: Reforzar white balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1702 — sensor_look_vendor_repair
- Definición: Campo operativo para sensor look dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sensor look como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sensor look como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SENSOR_LOOK_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SENSOR_LOOK_VENDOR_REPAIR
- Fallback: Reforzar sensor look con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1703 — depth_of_field_rule_vendor_repair
- Definición: Campo operativo para depth of field rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar depth of field rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar depth of field rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DEPTH_OF_FIELD_RULE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DEPTH_OF_FIELD_RULE_VENDOR_REPAI
- Fallback: Reforzar depth of field rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1704 — distortion_control_vendor_repair
- Definición: Campo operativo para distortion control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar distortion control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar distortion control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DISTORTION_CONTROL_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DISTORTION_CONTROL_VENDOR_REPAIR
- Fallback: Reforzar distortion control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1705 — crop_safe_area_vendor_repair
- Definición: Campo operativo para crop safe area dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar crop safe area como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar crop safe area como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CROP_SAFE_AREA_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CROP_SAFE_AREA_VENDOR_REPAIR
- Fallback: Reforzar crop safe area con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1706 — composition_grid_vendor_repair
- Definición: Campo operativo para composition grid dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar composition grid como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar composition grid como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMPOSITION_GRID_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMPOSITION_GRID_VENDOR_REPAIR
- Fallback: Reforzar composition grid con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1707 — negative_space_rule_vendor_repair
- Definición: Campo operativo para negative space rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar negative space rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar negative space rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NEGATIVE_SPACE_RULE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NEGATIVE_SPACE_RULE_VENDOR_REPAI
- Fallback: Reforzar negative space rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1708 — camera_body_relation_vendor_repair
- Definición: Campo operativo para camera body relation dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera body relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera body relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_BODY_RELATION_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_BODY_RELATION_VENDOR_REPA
- Fallback: Reforzar camera body relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1709 — key_light_vendor_repair
- Definición: Campo operativo para key light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar key light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar key light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KEY_LIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KEY_LIGHT_VENDOR_REPAIR
- Fallback: Reforzar key light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1710 — fill_light_vendor_repair
- Definición: Campo operativo para fill light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fill light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fill light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FILL_LIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FILL_LIGHT_VENDOR_REPAIR
- Fallback: Reforzar fill light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1711 — rim_light_vendor_repair
- Definición: Campo operativo para rim light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rim light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rim light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RIM_LIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RIM_LIGHT_VENDOR_REPAIR
- Fallback: Reforzar rim light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1712 — catchlight_pattern_vendor_repair
- Definición: Campo operativo para catchlight pattern dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar catchlight pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar catchlight pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CATCHLIGHT_PATTERN_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CATCHLIGHT_PATTERN_VENDOR_REPAIR
- Fallback: Reforzar catchlight pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1713 — shadow_logic_vendor_repair
- Definición: Campo operativo para shadow logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shadow logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shadow logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHADOW_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHADOW_LOGIC_VENDOR_REPAIR
- Fallback: Reforzar shadow logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1714 — softness_rule_vendor_repair
- Definición: Campo operativo para softness rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar softness rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar softness rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SOFTNESS_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SOFTNESS_RULE_VENDOR_REPAIR
- Fallback: Reforzar softness rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1715 — contrast_ratio_vendor_repair
- Definición: Campo operativo para contrast ratio dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contrast ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contrast ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTRAST_RATIO_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTRAST_RATIO_VENDOR_REPAIR
- Fallback: Reforzar contrast ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1716 — color_temperature_vendor_repair
- Definición: Campo operativo para color temperature dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar color temperature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar color temperature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COLOR_TEMPERATURE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COLOR_TEMPERATURE_VENDOR_REPAIR
- Fallback: Reforzar color temperature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1717 — ambient_light_vendor_repair
- Definición: Campo operativo para ambient light dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ambient light como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ambient light como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AMBIENT_LIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AMBIENT_LIGHT_VENDOR_REPAIR
- Fallback: Reforzar ambient light con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1718 — practical_lights_vendor_repair
- Definición: Campo operativo para practical lights dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar practical lights como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar practical lights como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PRACTICAL_LIGHTS_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PRACTICAL_LIGHTS_VENDOR_REPAIR
- Fallback: Reforzar practical lights con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1719 — skin_highlight_control_vendor_repair
- Definición: Campo operativo para skin highlight control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin highlight control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin highlight control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_HIGHLIGHT_CONTROL_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_HIGHLIGHT_CONTROL_VENDOR_RE
- Fallback: Reforzar skin highlight control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1720 — hair_rim_control_vendor_repair
- Definición: Campo operativo para hair rim control dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair rim control como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair rim control como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_RIM_CONTROL_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_RIM_CONTROL_VENDOR_REPAIR
- Fallback: Reforzar hair rim control con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1721 — eye_light_rule_vendor_repair
- Definición: Campo operativo para eye light rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye light rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye light rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_LIGHT_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_LIGHT_RULE_VENDOR_REPAIR
- Fallback: Reforzar eye light rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1722 — night_scene_rule_vendor_repair
- Definición: Campo operativo para night scene rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar night scene rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar night scene rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NIGHT_SCENE_RULE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NIGHT_SCENE_RULE_VENDOR_REPAIR
- Fallback: Reforzar night scene rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1723 — lighting_mood_map_vendor_repair
- Definición: Campo operativo para lighting mood map dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lighting mood map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lighting mood map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIGHTING_MOOD_MAP_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIGHTING_MOOD_MAP_VENDOR_REPAIR
- Fallback: Reforzar lighting mood map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1724 — scene_location_vendor_repair
- Definición: Campo operativo para scene location dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene location como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene location como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_LOCATION_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_LOCATION_VENDOR_REPAIR
- Fallback: Reforzar scene location con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1725 — period_context_vendor_repair
- Definición: Campo operativo para period context dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar period context como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar period context como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PERIOD_CONTEXT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PERIOD_CONTEXT_VENDOR_REPAIR
- Fallback: Reforzar period context con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1726 — weather_rule_vendor_repair
- Definición: Campo operativo para weather rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar weather rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar weather rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WEATHER_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WEATHER_RULE_VENDOR_REPAIR
- Fallback: Reforzar weather rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1727 — scale_contact_vendor_repair
- Definición: Campo operativo para scale contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scale contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scale contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCALE_CONTACT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCALE_CONTACT_VENDOR_REPAIR
- Fallback: Reforzar scale contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1728 — gravity_rules_vendor_repair
- Definición: Campo operativo para gravity rules dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar gravity rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar gravity rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GRAVITY_RULES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GRAVITY_RULES_VENDOR_REPAIR
- Fallback: Reforzar gravity rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1729 — reflection_rules_vendor_repair
- Definición: Campo operativo para reflection rules dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar reflection rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar reflection rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_REFLECTION_RULES_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_REFLECTION_RULES_VENDOR_REPAIR
- Fallback: Reforzar reflection rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1730 — floor_contact_vendor_repair
- Definición: Campo operativo para floor contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar floor contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar floor contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLOOR_CONTACT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLOOR_CONTACT_VENDOR_REPAIR
- Fallback: Reforzar floor contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1731 — wall_contact_vendor_repair
- Definición: Campo operativo para wall contact dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wall contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wall contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALL_CONTACT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALL_CONTACT_VENDOR_REPAIR
- Fallback: Reforzar wall contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1732 — background_depth_vendor_repair
- Definición: Campo operativo para background depth dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar background depth como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar background depth como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BACKGROUND_DEPTH_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BACKGROUND_DEPTH_VENDOR_REPAIR
- Fallback: Reforzar background depth con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1733 — object_scale_vendor_repair
- Definición: Campo operativo para object scale dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_SCALE_VENDOR_REPAIR
- Fallback: Reforzar object scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CULTURE_1734 — cultural_context_safe_vendor_repair
- Definición: Campo operativo para cultural context safe dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cultural context safe como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cultural context safe como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CULTURAL_CONTEXT_SAFE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CULTURAL_CONTEXT_SAFE_VENDOR_REP
- Fallback: Reforzar cultural context safe con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1735 — lima_peru_context_option_vendor_repair
- Definición: Campo operativo para lima peru context option dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lima peru context option como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lima peru context option como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIMA_PERU_CONTEXT_OPTION_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIMA_PERU_CONTEXT_OPTION_VENDOR_
- Fallback: Reforzar lima peru context option con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1736 — set_dressing_logic_vendor_repair
- Definición: Campo operativo para set dressing logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar set dressing logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar set dressing logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SET_DRESSING_LOGIC_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SET_DRESSING_LOGIC_VENDOR_REPAIR
- Fallback: Reforzar set dressing logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1737 — scene_story_logic_vendor_repair
- Definición: Campo operativo para scene story logic dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene story logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene story logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_STORY_LOGIC_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_STORY_LOGIC_VENDOR_REPAIR
- Fallback: Reforzar scene story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1738 — lens_face_distortion_blocker_vendor_repair
- Definición: Campo operativo para lens face distortion blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens face distortion blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens face distortion blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FACE_DISTORTION_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FACE_DISTORTION_BLOCKER_VEN
- Fallback: Reforzar lens face distortion blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1739 — impossible_light_blocker_vendor_repair
- Definición: Campo operativo para impossible light blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar impossible light blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar impossible light blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMPOSSIBLE_LIGHT_BLOCKER_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMPOSSIBLE_LIGHT_BLOCKER_VENDOR_
- Fallback: Reforzar impossible light blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1740 — shadow_mismatch_blocker_vendor_repair
- Definición: Campo operativo para shadow mismatch blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shadow mismatch blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shadow mismatch blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHADOW_MISMATCH_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHADOW_MISMATCH_BLOCKER_VENDOR_R
- Fallback: Reforzar shadow mismatch blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1741 — scale_error_blocker_vendor_repair
- Definición: Campo operativo para scale error blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scale error blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scale error blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCALE_ERROR_BLOCKER_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCALE_ERROR_BLOCKER_VENDOR_REPAI
- Fallback: Reforzar scale error blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1742 — cgi_grading_blocker_vendor_repair
- Definición: Campo operativo para cgi grading blocker dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cgi grading blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cgi grading blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CGI_GRADING_BLOCKER_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CGI_GRADING_BLOCKER_VENDOR_REPAI
- Fallback: Reforzar cgi grading blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PSYCHOLOGY_1743 — background_identity_conflict_rule_vendor_repair
- Definición: Campo operativo para background identity conflict rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar background identity conflict rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar background identity conflict rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BACKGROUND_IDENTITY_CONFLICT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BACKGROUND_IDENTITY_CONFLICT_RUL
- Fallback: Reforzar background identity conflict rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1744 — scene_physics_repair_rule_vendor_repair
- Definición: Campo operativo para scene physics repair rule dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar scene physics repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar scene physics repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCENE_PHYSICS_REPAIR_RULE_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCENE_PHYSICS_REPAIR_RULE_VENDOR
- Fallback: Reforzar scene physics repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1745 — environment_continuity_test_vendor_repair
- Definición: Campo operativo para environment continuity test dentro de Cámara, lente, iluminación, color, escena y física espacial. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar environment continuity test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar environment continuity test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ENVIRONMENT_CONTINUITY_TEST__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ENVIRONMENT_CONTINUITY_TEST_VEND
- Fallback: Reforzar environment continuity test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
