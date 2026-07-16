## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Piel, dermatología visual, cabello y materialidad humana

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_SKIN_0163` | `skin_tone` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_TONE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0164` | `skin_subtone` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_SUBTONE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0165` | `pore_density` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PORE_DENSITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar pore density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0166` | `texture_zone_map` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEXTURE_ZONE_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar texture zone map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0167` | `natural_marks` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NATURAL_MARKS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar natural marks con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0168` | `fine_lines` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINE_LINES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fine lines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0169` | `specular_zones` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPECULAR_ZONES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar specular zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0170` | `matte_zones` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MATTE_ZONES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar matte zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0171` | `makeup_rules` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MAKEUP_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar makeup rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0172` | `skin_light_response` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_LIGHT_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin light response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0173` | `skin_climate_response` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_CLIMATE_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin climate response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0174` | `skin_age_response` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_AGE_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin age response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0175` | `anti_doll_markers` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANTI_DOLL_MARKERS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar anti doll markers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0176` | `no_airbrush_rule` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_AIRBRUSH_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar no airbrush rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0177` | `skin_camera_distance_rule` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_CAMERA_DISTANCE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin camera distance rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0178` | `hair_color_base` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_COLOR_BASE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair color base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0179` | `hair_subtone` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_SUBTONE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0180` | `hair_density` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_DENSITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0181` | `strand_thickness` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STRAND_THICKNESS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar strand thickness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0182` | `hairline_shape` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIRLINE_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hairline shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0183` | `hair_length` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0184` | `hair_parting` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_PARTING_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair parting con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0185` | `layering_rule` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LAYERING_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar layering rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0186` | `volume_rule` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOLUME_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar volume rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0187` | `frizz_level` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FRIZZ_LEVEL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar frizz level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0188` | `baby_hairs` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BABY_HAIRS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar baby hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0189` | `flyaway_hairs` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLYAWAY_HAIRS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar flyaway hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0190` | `humidity_response` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HUMIDITY_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar humidity response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0191` | `wind_response` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WIND_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wind response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0192` | `strand_motion` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STRAND_MOTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar strand motion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0193` | `hair_shadow_contact` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_SHADOW_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair shadow contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0194` | `hair_face_occlusion_rule` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_FACE_OCCLUSION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair face occlusion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0195` | `eye_wetness` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_WETNESS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eye wetness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0196` | `sclera_natural_variation` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCLERA_NATURAL_VARIATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0197` | `lip_texture` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_TEXTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lip texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0198` | `lip_specular_rule` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_SPECULAR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lip specular rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0199` | `teeth_natural_rule` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEETH_NATURAL_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar teeth natural rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0200` | `skin_hair_color_harmony` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_HAIR_COLOR_HARMONY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin hair color harmony con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0201` | `skin_makeup_continuity` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_MAKEUP_CONTINUITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin makeup continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0202` | `hair_video_continuity` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_VIDEO_CONTINUITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair video continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0203` | `plastic_skin_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PLASTIC_SKIN_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar plastic skin blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0204` | `hair_helmet_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_HELMET_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair helmet blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0205` | `overblur_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OVERBLUR_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar overblur blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0206` | `dead_eyes_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DEAD_EYES_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar dead eyes blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0207` | `skin_tone_shift_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_TONE_SHIFT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar skin tone shift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0208` | `hair_length_drift_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_LENGTH_DRIFT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair length drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0209` | `cgi_skin_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CGI_SKIN_REPAIR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar cgi skin repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0612` | `skin_tone_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_TONE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0613` | `skin_subtone_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_SUBTONE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0614` | `pore_density_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PORE_DENSITY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pore density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0615` | `texture_zone_map_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEXTURE_ZONE_MAP_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar texture zone map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0616` | `natural_marks_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NATURAL_MARKS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar natural marks con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0617` | `fine_lines_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINE_LINES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fine lines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0618` | `specular_zones_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPECULAR_ZONES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar specular zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0619` | `matte_zones_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MATTE_ZONES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar matte zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0620` | `makeup_rules_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MAKEUP_RULES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar makeup rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0621` | `skin_light_response_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_LIGHT_RESPONSE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin light response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0622` | `skin_climate_response_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_CLIMATE_RESPONSE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin climate response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0623` | `skin_age_response_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_AGE_RESPONSE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin age response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0624` | `anti_doll_markers_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANTI_DOLL_MARKERS_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar anti doll markers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0625` | `no_airbrush_rule_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_AIRBRUSH_RULE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no airbrush rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0626` | `skin_camera_distance_rule_prompt_effect` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_CAMERA_DISTANCE_RULE_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin camera distance rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0627` | `hair_color_base_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_COLOR_BASE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair color base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0628` | `hair_subtone_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_SUBTONE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0629` | `hair_density_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_DENSITY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0630` | `strand_thickness_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STRAND_THICKNESS_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar strand thickness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0631` | `hairline_shape_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIRLINE_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hairline shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0632` | `hair_length_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0633` | `hair_parting_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_PARTING_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair parting con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0634` | `layering_rule_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LAYERING_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar layering rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0635` | `volume_rule_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOLUME_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar volume rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0636` | `frizz_level_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FRIZZ_LEVEL_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar frizz level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0637` | `baby_hairs_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BABY_HAIRS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar baby hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0638` | `flyaway_hairs_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLYAWAY_HAIRS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar flyaway hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0639` | `humidity_response_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HUMIDITY_RESPONSE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar humidity response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0640` | `wind_response_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WIND_RESPONSE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wind response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0641` | `strand_motion_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STRAND_MOTION_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar strand motion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0642` | `hair_shadow_contact_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_SHADOW_CONTACT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair shadow contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0643` | `hair_face_occlusion_rule_prompt_effect` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_FACE_OCCLUSION_RULE_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair face occlusion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0644` | `eye_wetness_prompt_effect` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_WETNESS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye wetness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0645` | `sclera_natural_variation_prompt_effect` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCLERA_NATURAL_VARIATION_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0646` | `lip_texture_prompt_effect` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_TEXTURE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0647` | `lip_specular_rule_prompt_effect` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_SPECULAR_RULE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip specular rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0648` | `teeth_natural_rule_prompt_effect` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEETH_NATURAL_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar teeth natural rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0649` | `skin_hair_color_harmony_prompt_effect` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_HAIR_COLOR_HARMONY_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin hair color harmony con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0650` | `skin_makeup_continuity_prompt_effect` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_MAKEUP_CONTINUITY_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin makeup continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0651` | `hair_video_continuity_prompt_effect` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_VIDEO_CONTINUITY_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair video continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0652` | `plastic_skin_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PLASTIC_SKIN_BLOCKER_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar plastic skin blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0653` | `hair_helmet_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_HELMET_BLOCKER_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair helmet blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0654` | `overblur_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OVERBLUR_BLOCKER_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar overblur blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0655` | `dead_eyes_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DEAD_EYES_BLOCKER_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dead eyes blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0656` | `skin_tone_shift_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_TONE_SHIFT_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin tone shift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0657` | `hair_length_drift_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_LENGTH_DRIFT_BLOCKER_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair length drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0658` | `cgi_skin_repair_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CGI_SKIN_REPAIR_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cgi skin repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1061` | `skin_tone_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_TONE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1062` | `skin_subtone_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_SUBTONE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1063` | `pore_density_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PORE_DENSITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pore density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1064` | `texture_zone_map_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEXTURE_ZONE_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar texture zone map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1065` | `natural_marks_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NATURAL_MARKS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar natural marks con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1066` | `fine_lines_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINE_LINES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fine lines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1067` | `specular_zones_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPECULAR_ZONES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar specular zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1068` | `matte_zones_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MATTE_ZONES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar matte zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1069` | `makeup_rules_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MAKEUP_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar makeup rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_1070` | `skin_light_response_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_LIGHT_RESPONSE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin light response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1071` | `skin_climate_response_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_CLIMATE_RESPONSE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin climate response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1072` | `skin_age_response_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_AGE_RESPONSE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin age response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1073` | `anti_doll_markers_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANTI_DOLL_MARKERS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar anti doll markers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1074` | `no_airbrush_rule_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_AIRBRUSH_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no airbrush rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1075` | `skin_camera_distance_rule_qa_matrix` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_CAMERA_DISTANCE_RULE_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin camera distance rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1076` | `hair_color_base_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_COLOR_BASE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair color base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1077` | `hair_subtone_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_SUBTONE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1078` | `hair_density_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_DENSITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1079` | `strand_thickness_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STRAND_THICKNESS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar strand thickness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1080` | `hairline_shape_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIRLINE_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hairline shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1081` | `hair_length_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1082` | `hair_parting_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_PARTING_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair parting con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1083` | `layering_rule_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LAYERING_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar layering rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1084` | `volume_rule_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOLUME_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar volume rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1085` | `frizz_level_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FRIZZ_LEVEL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar frizz level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1086` | `baby_hairs_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BABY_HAIRS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar baby hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1087` | `flyaway_hairs_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLYAWAY_HAIRS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar flyaway hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1088` | `humidity_response_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HUMIDITY_RESPONSE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar humidity response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1089` | `wind_response_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WIND_RESPONSE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wind response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1090` | `strand_motion_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STRAND_MOTION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar strand motion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_1091` | `hair_shadow_contact_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_SHADOW_CONTACT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair shadow contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1092` | `hair_face_occlusion_rule_qa_matrix` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_FACE_OCCLUSION_RULE_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair face occlusion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1093` | `eye_wetness_qa_matrix` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_WETNESS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye wetness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1094` | `sclera_natural_variation_qa_matrix` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCLERA_NATURAL_VARIATION_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1095` | `lip_texture_qa_matrix` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_TEXTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1096` | `lip_specular_rule_qa_matrix` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_SPECULAR_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip specular rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1097` | `teeth_natural_rule_qa_matrix` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEETH_NATURAL_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar teeth natural rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1098` | `skin_hair_color_harmony_qa_matrix` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_HAIR_COLOR_HARMONY_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin hair color harmony con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1099` | `skin_makeup_continuity_qa_matrix` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_MAKEUP_CONTINUITY_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin makeup continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1100` | `hair_video_continuity_qa_matrix` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_VIDEO_CONTINUITY_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair video continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1101` | `plastic_skin_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PLASTIC_SKIN_BLOCKER_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar plastic skin blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1102` | `hair_helmet_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_HELMET_BLOCKER_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair helmet blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1103` | `overblur_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OVERBLUR_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar overblur blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1104` | `dead_eyes_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DEAD_EYES_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dead eyes blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1105` | `skin_tone_shift_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_TONE_SHIFT_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin tone shift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1106` | `hair_length_drift_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_LENGTH_DRIFT_BLOCKER_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair length drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1107` | `cgi_skin_repair_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CGI_SKIN_REPAIR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cgi skin repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1510` | `skin_tone_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_TONE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1511` | `skin_subtone_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_SUBTONE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1512` | `pore_density_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PORE_DENSITY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pore density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1513` | `texture_zone_map_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEXTURE_ZONE_MAP_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar texture zone map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1514` | `natural_marks_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NATURAL_MARKS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar natural marks con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1515` | `fine_lines_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINE_LINES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fine lines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1516` | `specular_zones_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPECULAR_ZONES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar specular zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1517` | `matte_zones_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MATTE_ZONES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar matte zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1518` | `makeup_rules_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MAKEUP_RULES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar makeup rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_1519` | `skin_light_response_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_LIGHT_RESPONSE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin light response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1520` | `skin_climate_response_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_CLIMATE_RESPONSE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin climate response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1521` | `skin_age_response_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_AGE_RESPONSE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin age response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1522` | `anti_doll_markers_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANTI_DOLL_MARKERS_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar anti doll markers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1523` | `no_airbrush_rule_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_AIRBRUSH_RULE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no airbrush rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1524` | `skin_camera_distance_rule_vendor_repair` | skin | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_CAMERA_DISTANCE_RULE_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin camera distance rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1525` | `hair_color_base_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_COLOR_BASE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair color base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1526` | `hair_subtone_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_SUBTONE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1527` | `hair_density_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_DENSITY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1528` | `strand_thickness_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STRAND_THICKNESS_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar strand thickness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1529` | `hairline_shape_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIRLINE_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hairline shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1530` | `hair_length_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1531` | `hair_parting_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_PARTING_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair parting con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1532` | `layering_rule_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LAYERING_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar layering rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1533` | `volume_rule_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOLUME_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar volume rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1534` | `frizz_level_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FRIZZ_LEVEL_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar frizz level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1535` | `baby_hairs_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BABY_HAIRS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar baby hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1536` | `flyaway_hairs_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLYAWAY_HAIRS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar flyaway hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1537` | `humidity_response_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HUMIDITY_RESPONSE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar humidity response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1538` | `wind_response_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WIND_RESPONSE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wind response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1539` | `strand_motion_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STRAND_MOTION_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar strand motion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_1540` | `hair_shadow_contact_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_SHADOW_CONTACT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair shadow contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1541` | `hair_face_occlusion_rule_vendor_repair` | hair | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_FACE_OCCLUSION_RULE_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair face occlusion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1542` | `eye_wetness_vendor_repair` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_WETNESS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye wetness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1543` | `sclera_natural_variation_vendor_repair` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCLERA_NATURAL_VARIATION_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1544` | `lip_texture_vendor_repair` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_TEXTURE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1545` | `lip_specular_rule_vendor_repair` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_SPECULAR_RULE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip specular rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1546` | `teeth_natural_rule_vendor_repair` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEETH_NATURAL_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar teeth natural rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1547` | `skin_hair_color_harmony_vendor_repair` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_HAIR_COLOR_HARMONY_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin hair color harmony con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1548` | `skin_makeup_continuity_vendor_repair` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_MAKEUP_CONTINUITY_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin makeup continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1549` | `hair_video_continuity_vendor_repair` | detail | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_VIDEO_CONTINUITY_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair video continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1550` | `plastic_skin_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PLASTIC_SKIN_BLOCKER_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar plastic skin blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1551` | `hair_helmet_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_HELMET_BLOCKER_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair helmet blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1552` | `overblur_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OVERBLUR_BLOCKER_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar overblur blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1553` | `dead_eyes_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DEAD_EYES_BLOCKER_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dead eyes blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1554` | `skin_tone_shift_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SKIN_TONE_SHIFT_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar skin tone shift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1555` | `hair_length_drift_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_LENGTH_DRIFT_BLOCKER_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair length drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1556` | `cgi_skin_repair_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CGI_SKIN_REPAIR_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cgi skin repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_SKIN_0163 — skin_tone
- Definición: Campo operativo para skin tone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin tone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin tone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_TONE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_TONE_DRIFT_OR_GAP
- Fallback: Reforzar skin tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0164 — skin_subtone
- Definición: Campo operativo para skin subtone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin subtone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin subtone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_SUBTONE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_SUBTONE_DRIFT_OR_GAP
- Fallback: Reforzar skin subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0165 — pore_density
- Definición: Campo operativo para pore density dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar pore density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pore density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PORE_DENSITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PORE_DENSITY_DRIFT_OR_GAP
- Fallback: Reforzar pore density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0166 — texture_zone_map
- Definición: Campo operativo para texture zone map dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar texture zone map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar texture zone map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEXTURE_ZONE_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TEXTURE_ZONE_MAP_DRIFT_OR_GAP
- Fallback: Reforzar texture zone map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0167 — natural_marks
- Definición: Campo operativo para natural marks dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar natural marks como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar natural marks como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NATURAL_MARKS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NATURAL_MARKS_DRIFT_OR_GAP
- Fallback: Reforzar natural marks con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0168 — fine_lines
- Definición: Campo operativo para fine lines dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fine lines como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fine lines como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINE_LINES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FINE_LINES_DRIFT_OR_GAP
- Fallback: Reforzar fine lines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0169 — specular_zones
- Definición: Campo operativo para specular zones dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar specular zones como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar specular zones como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPECULAR_ZONES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SPECULAR_ZONES_DRIFT_OR_GAP
- Fallback: Reforzar specular zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0170 — matte_zones
- Definición: Campo operativo para matte zones dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar matte zones como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar matte zones como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MATTE_ZONES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MATTE_ZONES_DRIFT_OR_GAP
- Fallback: Reforzar matte zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0171 — makeup_rules
- Definición: Campo operativo para makeup rules dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar makeup rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar makeup rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MAKEUP_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MAKEUP_RULES_DRIFT_OR_GAP
- Fallback: Reforzar makeup rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0172 — skin_light_response
- Definición: Campo operativo para skin light response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin light response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin light response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_LIGHT_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_LIGHT_RESPONSE_DRIFT_OR_GAP
- Fallback: Reforzar skin light response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0173 — skin_climate_response
- Definición: Campo operativo para skin climate response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin climate response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin climate response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_CLIMATE_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_CLIMATE_RESPONSE_DRIFT_OR_GAP
- Fallback: Reforzar skin climate response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0174 — skin_age_response
- Definición: Campo operativo para skin age response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin age response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin age response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_AGE_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_AGE_RESPONSE_DRIFT_OR_GAP
- Fallback: Reforzar skin age response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0175 — anti_doll_markers
- Definición: Campo operativo para anti doll markers dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar anti doll markers como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar anti doll markers como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANTI_DOLL_MARKERS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ANTI_DOLL_MARKERS_DRIFT_OR_GAP
- Fallback: Reforzar anti doll markers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0176 — no_airbrush_rule
- Definición: Campo operativo para no airbrush rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar no airbrush rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no airbrush rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_AIRBRUSH_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NO_AIRBRUSH_RULE_DRIFT_OR_GAP
- Fallback: Reforzar no airbrush rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0177 — skin_camera_distance_rule
- Definición: Campo operativo para skin camera distance rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin camera distance rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin camera distance rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_CAMERA_DISTANCE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_CAMERA_DISTANCE_RULE_DRIFT_OR_GAP
- Fallback: Reforzar skin camera distance rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0178 — hair_color_base
- Definición: Campo operativo para hair color base dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair color base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair color base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_COLOR_BASE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_COLOR_BASE_DRIFT_OR_GAP
- Fallback: Reforzar hair color base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0179 — hair_subtone
- Definición: Campo operativo para hair subtone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair subtone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair subtone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_SUBTONE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_SUBTONE_DRIFT_OR_GAP
- Fallback: Reforzar hair subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0180 — hair_density
- Definición: Campo operativo para hair density dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_DENSITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_DENSITY_DRIFT_OR_GAP
- Fallback: Reforzar hair density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0181 — strand_thickness
- Definición: Campo operativo para strand thickness dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar strand thickness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar strand thickness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STRAND_THICKNESS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_STRAND_THICKNESS_DRIFT_OR_GAP
- Fallback: Reforzar strand thickness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0182 — hairline_shape
- Definición: Campo operativo para hairline shape dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hairline shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hairline shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIRLINE_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIRLINE_SHAPE_DRIFT_OR_GAP
- Fallback: Reforzar hairline shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0183 — hair_length
- Definición: Campo operativo para hair length dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_LENGTH_DRIFT_OR_GAP
- Fallback: Reforzar hair length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0184 — hair_parting
- Definición: Campo operativo para hair parting dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair parting como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair parting como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_PARTING_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_PARTING_DRIFT_OR_GAP
- Fallback: Reforzar hair parting con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0185 — layering_rule
- Definición: Campo operativo para layering rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar layering rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar layering rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LAYERING_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LAYERING_RULE_DRIFT_OR_GAP
- Fallback: Reforzar layering rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0186 — volume_rule
- Definición: Campo operativo para volume rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar volume rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar volume rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOLUME_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOLUME_RULE_DRIFT_OR_GAP
- Fallback: Reforzar volume rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0187 — frizz_level
- Definición: Campo operativo para frizz level dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar frizz level como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar frizz level como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FRIZZ_LEVEL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FRIZZ_LEVEL_DRIFT_OR_GAP
- Fallback: Reforzar frizz level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0188 — baby_hairs
- Definición: Campo operativo para baby hairs dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar baby hairs como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar baby hairs como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BABY_HAIRS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BABY_HAIRS_DRIFT_OR_GAP
- Fallback: Reforzar baby hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0189 — flyaway_hairs
- Definición: Campo operativo para flyaway hairs dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar flyaway hairs como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar flyaway hairs como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLYAWAY_HAIRS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FLYAWAY_HAIRS_DRIFT_OR_GAP
- Fallback: Reforzar flyaway hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0190 — humidity_response
- Definición: Campo operativo para humidity response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar humidity response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar humidity response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HUMIDITY_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HUMIDITY_RESPONSE_DRIFT_OR_GAP
- Fallback: Reforzar humidity response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0191 — wind_response
- Definición: Campo operativo para wind response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wind response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wind response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WIND_RESPONSE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WIND_RESPONSE_DRIFT_OR_GAP
- Fallback: Reforzar wind response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0192 — strand_motion
- Definición: Campo operativo para strand motion dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar strand motion como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar strand motion como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STRAND_MOTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_STRAND_MOTION_DRIFT_OR_GAP
- Fallback: Reforzar strand motion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0193 — hair_shadow_contact
- Definición: Campo operativo para hair shadow contact dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair shadow contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair shadow contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_SHADOW_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_SHADOW_CONTACT_DRIFT_OR_GAP
- Fallback: Reforzar hair shadow contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0194 — hair_face_occlusion_rule
- Definición: Campo operativo para hair face occlusion rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair face occlusion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair face occlusion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_FACE_OCCLUSION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_FACE_OCCLUSION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar hair face occlusion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0195 — eye_wetness
- Definición: Campo operativo para eye wetness dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eye wetness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye wetness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_WETNESS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYE_WETNESS_DRIFT_OR_GAP
- Fallback: Reforzar eye wetness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0196 — sclera_natural_variation
- Definición: Campo operativo para sclera natural variation dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sclera natural variation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sclera natural variation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCLERA_NATURAL_VARIATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCLERA_NATURAL_VARIATION_DRIFT_OR_GAP
- Fallback: Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0197 — lip_texture
- Definición: Campo operativo para lip texture dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lip texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_TEXTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LIP_TEXTURE_DRIFT_OR_GAP
- Fallback: Reforzar lip texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0198 — lip_specular_rule
- Definición: Campo operativo para lip specular rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lip specular rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip specular rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_SPECULAR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LIP_SPECULAR_RULE_DRIFT_OR_GAP
- Fallback: Reforzar lip specular rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0199 — teeth_natural_rule
- Definición: Campo operativo para teeth natural rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar teeth natural rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar teeth natural rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEETH_NATURAL_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TEETH_NATURAL_RULE_DRIFT_OR_GAP
- Fallback: Reforzar teeth natural rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0200 — skin_hair_color_harmony
- Definición: Campo operativo para skin hair color harmony dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin hair color harmony como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin hair color harmony como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_HAIR_COLOR_HARMONY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_HAIR_COLOR_HARMONY_DRIFT_OR_GAP
- Fallback: Reforzar skin hair color harmony con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0201 — skin_makeup_continuity
- Definición: Campo operativo para skin makeup continuity dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin makeup continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin makeup continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_MAKEUP_CONTINUITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_MAKEUP_CONTINUITY_DRIFT_OR_GAP
- Fallback: Reforzar skin makeup continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0202 — hair_video_continuity
- Definición: Campo operativo para hair video continuity dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair video continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair video continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_VIDEO_CONTINUITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_VIDEO_CONTINUITY_DRIFT_OR_GAP
- Fallback: Reforzar hair video continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0203 — plastic_skin_blocker
- Definición: Campo operativo para plastic skin blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar plastic skin blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar plastic skin blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PLASTIC_SKIN_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PLASTIC_SKIN_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar plastic skin blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0204 — hair_helmet_blocker
- Definición: Campo operativo para hair helmet blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair helmet blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair helmet blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_HELMET_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_HELMET_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar hair helmet blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0205 — overblur_blocker
- Definición: Campo operativo para overblur blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar overblur blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar overblur blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OVERBLUR_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_OVERBLUR_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar overblur blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0206 — dead_eyes_blocker
- Definición: Campo operativo para dead eyes blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar dead eyes blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dead eyes blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DEAD_EYES_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DEAD_EYES_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar dead eyes blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0207 — skin_tone_shift_blocker
- Definición: Campo operativo para skin tone shift blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar skin tone shift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin tone shift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_TONE_SHIFT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SKIN_TONE_SHIFT_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar skin tone shift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0208 — hair_length_drift_blocker
- Definición: Campo operativo para hair length drift blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair length drift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair length drift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_LENGTH_DRIFT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_LENGTH_DRIFT_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar hair length drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0209 — cgi_skin_repair
- Definición: Campo operativo para cgi skin repair dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar cgi skin repair como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cgi skin repair como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CGI_SKIN_REPAIR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CGI_SKIN_REPAIR_DRIFT_OR_GAP
- Fallback: Reforzar cgi skin repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0612 — skin_tone_prompt_effect
- Definición: Campo operativo para skin tone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin tone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin tone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_TONE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_TONE_PROMPT_EFFECT
- Fallback: Reforzar skin tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0613 — skin_subtone_prompt_effect
- Definición: Campo operativo para skin subtone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin subtone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin subtone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_SUBTONE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_SUBTONE_PROMPT_EFFECT
- Fallback: Reforzar skin subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0614 — pore_density_prompt_effect
- Definición: Campo operativo para pore density dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pore density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pore density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PORE_DENSITY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PORE_DENSITY_PROMPT_EFFECT
- Fallback: Reforzar pore density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0615 — texture_zone_map_prompt_effect
- Definición: Campo operativo para texture zone map dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar texture zone map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar texture zone map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEXTURE_ZONE_MAP_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEXTURE_ZONE_MAP_PROMPT_EFFECT
- Fallback: Reforzar texture zone map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0616 — natural_marks_prompt_effect
- Definición: Campo operativo para natural marks dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar natural marks como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar natural marks como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NATURAL_MARKS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NATURAL_MARKS_PROMPT_EFFECT
- Fallback: Reforzar natural marks con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0617 — fine_lines_prompt_effect
- Definición: Campo operativo para fine lines dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fine lines como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fine lines como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINE_LINES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINE_LINES_PROMPT_EFFECT
- Fallback: Reforzar fine lines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0618 — specular_zones_prompt_effect
- Definición: Campo operativo para specular zones dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar specular zones como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar specular zones como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPECULAR_ZONES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPECULAR_ZONES_PROMPT_EFFECT
- Fallback: Reforzar specular zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0619 — matte_zones_prompt_effect
- Definición: Campo operativo para matte zones dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar matte zones como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar matte zones como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MATTE_ZONES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MATTE_ZONES_PROMPT_EFFECT
- Fallback: Reforzar matte zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0620 — makeup_rules_prompt_effect
- Definición: Campo operativo para makeup rules dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar makeup rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar makeup rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MAKEUP_RULES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MAKEUP_RULES_PROMPT_EFFECT
- Fallback: Reforzar makeup rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0621 — skin_light_response_prompt_effect
- Definición: Campo operativo para skin light response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin light response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin light response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_LIGHT_RESPONSE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_LIGHT_RESPONSE_PROMPT_EFFEC
- Fallback: Reforzar skin light response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0622 — skin_climate_response_prompt_effect
- Definición: Campo operativo para skin climate response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin climate response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin climate response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_CLIMATE_RESPONSE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_CLIMATE_RESPONSE_PROMPT_EFF
- Fallback: Reforzar skin climate response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0623 — skin_age_response_prompt_effect
- Definición: Campo operativo para skin age response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin age response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin age response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_AGE_RESPONSE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_AGE_RESPONSE_PROMPT_EFFECT
- Fallback: Reforzar skin age response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0624 — anti_doll_markers_prompt_effect
- Definición: Campo operativo para anti doll markers dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar anti doll markers como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar anti doll markers como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANTI_DOLL_MARKERS_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANTI_DOLL_MARKERS_PROMPT_EFFECT
- Fallback: Reforzar anti doll markers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0625 — no_airbrush_rule_prompt_effect
- Definición: Campo operativo para no airbrush rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no airbrush rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no airbrush rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_AIRBRUSH_RULE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_AIRBRUSH_RULE_PROMPT_EFFECT
- Fallback: Reforzar no airbrush rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0626 — skin_camera_distance_rule_prompt_effect
- Definición: Campo operativo para skin camera distance rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin camera distance rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin camera distance rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_CAMERA_DISTANCE_RULE_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_CAMERA_DISTANCE_RULE_PROMPT
- Fallback: Reforzar skin camera distance rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0627 — hair_color_base_prompt_effect
- Definición: Campo operativo para hair color base dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair color base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair color base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_COLOR_BASE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_COLOR_BASE_PROMPT_EFFECT
- Fallback: Reforzar hair color base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0628 — hair_subtone_prompt_effect
- Definición: Campo operativo para hair subtone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair subtone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair subtone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_SUBTONE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_SUBTONE_PROMPT_EFFECT
- Fallback: Reforzar hair subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0629 — hair_density_prompt_effect
- Definición: Campo operativo para hair density dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_DENSITY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_DENSITY_PROMPT_EFFECT
- Fallback: Reforzar hair density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0630 — strand_thickness_prompt_effect
- Definición: Campo operativo para strand thickness dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar strand thickness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar strand thickness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STRAND_THICKNESS_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STRAND_THICKNESS_PROMPT_EFFECT
- Fallback: Reforzar strand thickness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0631 — hairline_shape_prompt_effect
- Definición: Campo operativo para hairline shape dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hairline shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hairline shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIRLINE_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIRLINE_SHAPE_PROMPT_EFFECT
- Fallback: Reforzar hairline shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0632 — hair_length_prompt_effect
- Definición: Campo operativo para hair length dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_LENGTH_PROMPT_EFFECT
- Fallback: Reforzar hair length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0633 — hair_parting_prompt_effect
- Definición: Campo operativo para hair parting dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair parting como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair parting como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_PARTING_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_PARTING_PROMPT_EFFECT
- Fallback: Reforzar hair parting con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0634 — layering_rule_prompt_effect
- Definición: Campo operativo para layering rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar layering rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar layering rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LAYERING_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LAYERING_RULE_PROMPT_EFFECT
- Fallback: Reforzar layering rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0635 — volume_rule_prompt_effect
- Definición: Campo operativo para volume rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar volume rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar volume rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOLUME_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOLUME_RULE_PROMPT_EFFECT
- Fallback: Reforzar volume rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0636 — frizz_level_prompt_effect
- Definición: Campo operativo para frizz level dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar frizz level como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar frizz level como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FRIZZ_LEVEL_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FRIZZ_LEVEL_PROMPT_EFFECT
- Fallback: Reforzar frizz level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0637 — baby_hairs_prompt_effect
- Definición: Campo operativo para baby hairs dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar baby hairs como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar baby hairs como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BABY_HAIRS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BABY_HAIRS_PROMPT_EFFECT
- Fallback: Reforzar baby hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0638 — flyaway_hairs_prompt_effect
- Definición: Campo operativo para flyaway hairs dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar flyaway hairs como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar flyaway hairs como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLYAWAY_HAIRS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLYAWAY_HAIRS_PROMPT_EFFECT
- Fallback: Reforzar flyaway hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0639 — humidity_response_prompt_effect
- Definición: Campo operativo para humidity response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar humidity response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar humidity response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HUMIDITY_RESPONSE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HUMIDITY_RESPONSE_PROMPT_EFFECT
- Fallback: Reforzar humidity response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0640 — wind_response_prompt_effect
- Definición: Campo operativo para wind response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wind response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wind response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WIND_RESPONSE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WIND_RESPONSE_PROMPT_EFFECT
- Fallback: Reforzar wind response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0641 — strand_motion_prompt_effect
- Definición: Campo operativo para strand motion dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar strand motion como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar strand motion como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STRAND_MOTION_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STRAND_MOTION_PROMPT_EFFECT
- Fallback: Reforzar strand motion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0642 — hair_shadow_contact_prompt_effect
- Definición: Campo operativo para hair shadow contact dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair shadow contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair shadow contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_SHADOW_CONTACT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_SHADOW_CONTACT_PROMPT_EFFEC
- Fallback: Reforzar hair shadow contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0643 — hair_face_occlusion_rule_prompt_effect
- Definición: Campo operativo para hair face occlusion rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair face occlusion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair face occlusion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_FACE_OCCLUSION_RULE_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_FACE_OCCLUSION_RULE_PROMPT_
- Fallback: Reforzar hair face occlusion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0644 — eye_wetness_prompt_effect
- Definición: Campo operativo para eye wetness dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye wetness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye wetness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_WETNESS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_WETNESS_PROMPT_EFFECT
- Fallback: Reforzar eye wetness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0645 — sclera_natural_variation_prompt_effect
- Definición: Campo operativo para sclera natural variation dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sclera natural variation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sclera natural variation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCLERA_NATURAL_VARIATION_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCLERA_NATURAL_VARIATION_PROMPT_
- Fallback: Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0646 — lip_texture_prompt_effect
- Definición: Campo operativo para lip texture dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_TEXTURE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_TEXTURE_PROMPT_EFFECT
- Fallback: Reforzar lip texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0647 — lip_specular_rule_prompt_effect
- Definición: Campo operativo para lip specular rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip specular rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip specular rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_SPECULAR_RULE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_SPECULAR_RULE_PROMPT_EFFECT
- Fallback: Reforzar lip specular rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0648 — teeth_natural_rule_prompt_effect
- Definición: Campo operativo para teeth natural rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar teeth natural rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar teeth natural rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEETH_NATURAL_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEETH_NATURAL_RULE_PROMPT_EFFECT
- Fallback: Reforzar teeth natural rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0649 — skin_hair_color_harmony_prompt_effect
- Definición: Campo operativo para skin hair color harmony dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin hair color harmony como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin hair color harmony como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_HAIR_COLOR_HARMONY_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_HAIR_COLOR_HARMONY_PROMPT_E
- Fallback: Reforzar skin hair color harmony con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0650 — skin_makeup_continuity_prompt_effect
- Definición: Campo operativo para skin makeup continuity dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin makeup continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin makeup continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_MAKEUP_CONTINUITY_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_MAKEUP_CONTINUITY_PROMPT_EF
- Fallback: Reforzar skin makeup continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0651 — hair_video_continuity_prompt_effect
- Definición: Campo operativo para hair video continuity dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair video continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair video continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_VIDEO_CONTINUITY_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_VIDEO_CONTINUITY_PROMPT_EFF
- Fallback: Reforzar hair video continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0652 — plastic_skin_blocker_prompt_effect
- Definición: Campo operativo para plastic skin blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar plastic skin blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar plastic skin blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PLASTIC_SKIN_BLOCKER_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PLASTIC_SKIN_BLOCKER_PROMPT_EFFE
- Fallback: Reforzar plastic skin blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0653 — hair_helmet_blocker_prompt_effect
- Definición: Campo operativo para hair helmet blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair helmet blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair helmet blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_HELMET_BLOCKER_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_HELMET_BLOCKER_PROMPT_EFFEC
- Fallback: Reforzar hair helmet blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0654 — overblur_blocker_prompt_effect
- Definición: Campo operativo para overblur blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar overblur blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar overblur blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OVERBLUR_BLOCKER_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OVERBLUR_BLOCKER_PROMPT_EFFECT
- Fallback: Reforzar overblur blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0655 — dead_eyes_blocker_prompt_effect
- Definición: Campo operativo para dead eyes blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dead eyes blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dead eyes blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DEAD_EYES_BLOCKER_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DEAD_EYES_BLOCKER_PROMPT_EFFECT
- Fallback: Reforzar dead eyes blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0656 — skin_tone_shift_blocker_prompt_effect
- Definición: Campo operativo para skin tone shift blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin tone shift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin tone shift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_TONE_SHIFT_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_TONE_SHIFT_BLOCKER_PROMPT_E
- Fallback: Reforzar skin tone shift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0657 — hair_length_drift_blocker_prompt_effect
- Definición: Campo operativo para hair length drift blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair length drift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair length drift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_LENGTH_DRIFT_BLOCKER_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_LENGTH_DRIFT_BLOCKER_PROMPT
- Fallback: Reforzar hair length drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0658 — cgi_skin_repair_prompt_effect
- Definición: Campo operativo para cgi skin repair dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cgi skin repair como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cgi skin repair como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CGI_SKIN_REPAIR_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CGI_SKIN_REPAIR_PROMPT_EFFECT
- Fallback: Reforzar cgi skin repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1061 — skin_tone_qa_matrix
- Definición: Campo operativo para skin tone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin tone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin tone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_TONE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_TONE_QA_MATRIX
- Fallback: Reforzar skin tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1062 — skin_subtone_qa_matrix
- Definición: Campo operativo para skin subtone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin subtone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin subtone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_SUBTONE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_SUBTONE_QA_MATRIX
- Fallback: Reforzar skin subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1063 — pore_density_qa_matrix
- Definición: Campo operativo para pore density dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pore density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pore density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PORE_DENSITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PORE_DENSITY_QA_MATRIX
- Fallback: Reforzar pore density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1064 — texture_zone_map_qa_matrix
- Definición: Campo operativo para texture zone map dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar texture zone map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar texture zone map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEXTURE_ZONE_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEXTURE_ZONE_MAP_QA_MATRIX
- Fallback: Reforzar texture zone map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1065 — natural_marks_qa_matrix
- Definición: Campo operativo para natural marks dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar natural marks como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar natural marks como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NATURAL_MARKS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NATURAL_MARKS_QA_MATRIX
- Fallback: Reforzar natural marks con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1066 — fine_lines_qa_matrix
- Definición: Campo operativo para fine lines dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fine lines como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fine lines como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINE_LINES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINE_LINES_QA_MATRIX
- Fallback: Reforzar fine lines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1067 — specular_zones_qa_matrix
- Definición: Campo operativo para specular zones dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar specular zones como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar specular zones como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPECULAR_ZONES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPECULAR_ZONES_QA_MATRIX
- Fallback: Reforzar specular zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1068 — matte_zones_qa_matrix
- Definición: Campo operativo para matte zones dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar matte zones como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar matte zones como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MATTE_ZONES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MATTE_ZONES_QA_MATRIX
- Fallback: Reforzar matte zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1069 — makeup_rules_qa_matrix
- Definición: Campo operativo para makeup rules dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar makeup rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar makeup rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MAKEUP_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MAKEUP_RULES_QA_MATRIX
- Fallback: Reforzar makeup rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_1070 — skin_light_response_qa_matrix
- Definición: Campo operativo para skin light response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin light response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin light response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_LIGHT_RESPONSE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_LIGHT_RESPONSE_QA_MATRIX
- Fallback: Reforzar skin light response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1071 — skin_climate_response_qa_matrix
- Definición: Campo operativo para skin climate response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin climate response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin climate response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_CLIMATE_RESPONSE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_CLIMATE_RESPONSE_QA_MATRIX
- Fallback: Reforzar skin climate response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1072 — skin_age_response_qa_matrix
- Definición: Campo operativo para skin age response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin age response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin age response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_AGE_RESPONSE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_AGE_RESPONSE_QA_MATRIX
- Fallback: Reforzar skin age response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1073 — anti_doll_markers_qa_matrix
- Definición: Campo operativo para anti doll markers dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar anti doll markers como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar anti doll markers como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANTI_DOLL_MARKERS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANTI_DOLL_MARKERS_QA_MATRIX
- Fallback: Reforzar anti doll markers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1074 — no_airbrush_rule_qa_matrix
- Definición: Campo operativo para no airbrush rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no airbrush rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no airbrush rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_AIRBRUSH_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_AIRBRUSH_RULE_QA_MATRIX
- Fallback: Reforzar no airbrush rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1075 — skin_camera_distance_rule_qa_matrix
- Definición: Campo operativo para skin camera distance rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin camera distance rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin camera distance rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_CAMERA_DISTANCE_RULE_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_CAMERA_DISTANCE_RULE_QA_MAT
- Fallback: Reforzar skin camera distance rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1076 — hair_color_base_qa_matrix
- Definición: Campo operativo para hair color base dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair color base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair color base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_COLOR_BASE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_COLOR_BASE_QA_MATRIX
- Fallback: Reforzar hair color base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1077 — hair_subtone_qa_matrix
- Definición: Campo operativo para hair subtone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair subtone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair subtone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_SUBTONE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_SUBTONE_QA_MATRIX
- Fallback: Reforzar hair subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1078 — hair_density_qa_matrix
- Definición: Campo operativo para hair density dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_DENSITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_DENSITY_QA_MATRIX
- Fallback: Reforzar hair density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1079 — strand_thickness_qa_matrix
- Definición: Campo operativo para strand thickness dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar strand thickness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar strand thickness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STRAND_THICKNESS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STRAND_THICKNESS_QA_MATRIX
- Fallback: Reforzar strand thickness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1080 — hairline_shape_qa_matrix
- Definición: Campo operativo para hairline shape dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hairline shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hairline shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIRLINE_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIRLINE_SHAPE_QA_MATRIX
- Fallback: Reforzar hairline shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1081 — hair_length_qa_matrix
- Definición: Campo operativo para hair length dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_LENGTH_QA_MATRIX
- Fallback: Reforzar hair length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1082 — hair_parting_qa_matrix
- Definición: Campo operativo para hair parting dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair parting como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair parting como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_PARTING_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_PARTING_QA_MATRIX
- Fallback: Reforzar hair parting con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1083 — layering_rule_qa_matrix
- Definición: Campo operativo para layering rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar layering rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar layering rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LAYERING_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LAYERING_RULE_QA_MATRIX
- Fallback: Reforzar layering rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1084 — volume_rule_qa_matrix
- Definición: Campo operativo para volume rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar volume rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar volume rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOLUME_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOLUME_RULE_QA_MATRIX
- Fallback: Reforzar volume rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1085 — frizz_level_qa_matrix
- Definición: Campo operativo para frizz level dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar frizz level como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar frizz level como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FRIZZ_LEVEL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FRIZZ_LEVEL_QA_MATRIX
- Fallback: Reforzar frizz level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1086 — baby_hairs_qa_matrix
- Definición: Campo operativo para baby hairs dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar baby hairs como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar baby hairs como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BABY_HAIRS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BABY_HAIRS_QA_MATRIX
- Fallback: Reforzar baby hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1087 — flyaway_hairs_qa_matrix
- Definición: Campo operativo para flyaway hairs dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar flyaway hairs como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar flyaway hairs como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLYAWAY_HAIRS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLYAWAY_HAIRS_QA_MATRIX
- Fallback: Reforzar flyaway hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1088 — humidity_response_qa_matrix
- Definición: Campo operativo para humidity response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar humidity response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar humidity response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HUMIDITY_RESPONSE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HUMIDITY_RESPONSE_QA_MATRIX
- Fallback: Reforzar humidity response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1089 — wind_response_qa_matrix
- Definición: Campo operativo para wind response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wind response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wind response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WIND_RESPONSE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WIND_RESPONSE_QA_MATRIX
- Fallback: Reforzar wind response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1090 — strand_motion_qa_matrix
- Definición: Campo operativo para strand motion dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar strand motion como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar strand motion como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STRAND_MOTION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STRAND_MOTION_QA_MATRIX
- Fallback: Reforzar strand motion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_1091 — hair_shadow_contact_qa_matrix
- Definición: Campo operativo para hair shadow contact dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair shadow contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair shadow contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_SHADOW_CONTACT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_SHADOW_CONTACT_QA_MATRIX
- Fallback: Reforzar hair shadow contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1092 — hair_face_occlusion_rule_qa_matrix
- Definición: Campo operativo para hair face occlusion rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair face occlusion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair face occlusion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_FACE_OCCLUSION_RULE_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_FACE_OCCLUSION_RULE_QA_MATR
- Fallback: Reforzar hair face occlusion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1093 — eye_wetness_qa_matrix
- Definición: Campo operativo para eye wetness dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye wetness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye wetness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_WETNESS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_WETNESS_QA_MATRIX
- Fallback: Reforzar eye wetness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1094 — sclera_natural_variation_qa_matrix
- Definición: Campo operativo para sclera natural variation dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sclera natural variation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sclera natural variation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCLERA_NATURAL_VARIATION_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCLERA_NATURAL_VARIATION_QA_MATR
- Fallback: Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1095 — lip_texture_qa_matrix
- Definición: Campo operativo para lip texture dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_TEXTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_TEXTURE_QA_MATRIX
- Fallback: Reforzar lip texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1096 — lip_specular_rule_qa_matrix
- Definición: Campo operativo para lip specular rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip specular rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip specular rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_SPECULAR_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_SPECULAR_RULE_QA_MATRIX
- Fallback: Reforzar lip specular rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1097 — teeth_natural_rule_qa_matrix
- Definición: Campo operativo para teeth natural rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar teeth natural rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar teeth natural rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEETH_NATURAL_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEETH_NATURAL_RULE_QA_MATRIX
- Fallback: Reforzar teeth natural rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1098 — skin_hair_color_harmony_qa_matrix
- Definición: Campo operativo para skin hair color harmony dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin hair color harmony como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin hair color harmony como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_HAIR_COLOR_HARMONY_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_HAIR_COLOR_HARMONY_QA_MATRI
- Fallback: Reforzar skin hair color harmony con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1099 — skin_makeup_continuity_qa_matrix
- Definición: Campo operativo para skin makeup continuity dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin makeup continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin makeup continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_MAKEUP_CONTINUITY_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_MAKEUP_CONTINUITY_QA_MATRIX
- Fallback: Reforzar skin makeup continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1100 — hair_video_continuity_qa_matrix
- Definición: Campo operativo para hair video continuity dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair video continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair video continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_VIDEO_CONTINUITY_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_VIDEO_CONTINUITY_QA_MATRIX
- Fallback: Reforzar hair video continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1101 — plastic_skin_blocker_qa_matrix
- Definición: Campo operativo para plastic skin blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar plastic skin blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar plastic skin blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PLASTIC_SKIN_BLOCKER_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PLASTIC_SKIN_BLOCKER_QA_MATRIX
- Fallback: Reforzar plastic skin blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1102 — hair_helmet_blocker_qa_matrix
- Definición: Campo operativo para hair helmet blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair helmet blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair helmet blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_HELMET_BLOCKER_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_HELMET_BLOCKER_QA_MATRIX
- Fallback: Reforzar hair helmet blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1103 — overblur_blocker_qa_matrix
- Definición: Campo operativo para overblur blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar overblur blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar overblur blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OVERBLUR_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OVERBLUR_BLOCKER_QA_MATRIX
- Fallback: Reforzar overblur blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1104 — dead_eyes_blocker_qa_matrix
- Definición: Campo operativo para dead eyes blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dead eyes blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dead eyes blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DEAD_EYES_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DEAD_EYES_BLOCKER_QA_MATRIX
- Fallback: Reforzar dead eyes blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1105 — skin_tone_shift_blocker_qa_matrix
- Definición: Campo operativo para skin tone shift blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin tone shift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin tone shift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_TONE_SHIFT_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_TONE_SHIFT_BLOCKER_QA_MATRI
- Fallback: Reforzar skin tone shift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1106 — hair_length_drift_blocker_qa_matrix
- Definición: Campo operativo para hair length drift blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair length drift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair length drift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_LENGTH_DRIFT_BLOCKER_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_LENGTH_DRIFT_BLOCKER_QA_MAT
- Fallback: Reforzar hair length drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1107 — cgi_skin_repair_qa_matrix
- Definición: Campo operativo para cgi skin repair dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cgi skin repair como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cgi skin repair como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CGI_SKIN_REPAIR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CGI_SKIN_REPAIR_QA_MATRIX
- Fallback: Reforzar cgi skin repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1510 — skin_tone_vendor_repair
- Definición: Campo operativo para skin tone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin tone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin tone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_TONE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_TONE_VENDOR_REPAIR
- Fallback: Reforzar skin tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1511 — skin_subtone_vendor_repair
- Definición: Campo operativo para skin subtone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin subtone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin subtone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_SUBTONE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_SUBTONE_VENDOR_REPAIR
- Fallback: Reforzar skin subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1512 — pore_density_vendor_repair
- Definición: Campo operativo para pore density dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pore density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pore density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PORE_DENSITY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PORE_DENSITY_VENDOR_REPAIR
- Fallback: Reforzar pore density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1513 — texture_zone_map_vendor_repair
- Definición: Campo operativo para texture zone map dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar texture zone map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar texture zone map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEXTURE_ZONE_MAP_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEXTURE_ZONE_MAP_VENDOR_REPAIR
- Fallback: Reforzar texture zone map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1514 — natural_marks_vendor_repair
- Definición: Campo operativo para natural marks dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar natural marks como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar natural marks como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NATURAL_MARKS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NATURAL_MARKS_VENDOR_REPAIR
- Fallback: Reforzar natural marks con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1515 — fine_lines_vendor_repair
- Definición: Campo operativo para fine lines dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fine lines como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fine lines como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINE_LINES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINE_LINES_VENDOR_REPAIR
- Fallback: Reforzar fine lines con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1516 — specular_zones_vendor_repair
- Definición: Campo operativo para specular zones dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar specular zones como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar specular zones como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPECULAR_ZONES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPECULAR_ZONES_VENDOR_REPAIR
- Fallback: Reforzar specular zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1517 — matte_zones_vendor_repair
- Definición: Campo operativo para matte zones dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar matte zones como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar matte zones como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MATTE_ZONES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MATTE_ZONES_VENDOR_REPAIR
- Fallback: Reforzar matte zones con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1518 — makeup_rules_vendor_repair
- Definición: Campo operativo para makeup rules dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar makeup rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar makeup rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MAKEUP_RULES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MAKEUP_RULES_VENDOR_REPAIR
- Fallback: Reforzar makeup rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_1519 — skin_light_response_vendor_repair
- Definición: Campo operativo para skin light response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin light response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin light response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_LIGHT_RESPONSE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_LIGHT_RESPONSE_VENDOR_REPAI
- Fallback: Reforzar skin light response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1520 — skin_climate_response_vendor_repair
- Definición: Campo operativo para skin climate response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin climate response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin climate response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_CLIMATE_RESPONSE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_CLIMATE_RESPONSE_VENDOR_REP
- Fallback: Reforzar skin climate response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1521 — skin_age_response_vendor_repair
- Definición: Campo operativo para skin age response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin age response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin age response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_AGE_RESPONSE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_AGE_RESPONSE_VENDOR_REPAIR
- Fallback: Reforzar skin age response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1522 — anti_doll_markers_vendor_repair
- Definición: Campo operativo para anti doll markers dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar anti doll markers como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar anti doll markers como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANTI_DOLL_MARKERS_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANTI_DOLL_MARKERS_VENDOR_REPAIR
- Fallback: Reforzar anti doll markers con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1523 — no_airbrush_rule_vendor_repair
- Definición: Campo operativo para no airbrush rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no airbrush rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no airbrush rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_AIRBRUSH_RULE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_AIRBRUSH_RULE_VENDOR_REPAIR
- Fallback: Reforzar no airbrush rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1524 — skin_camera_distance_rule_vendor_repair
- Definición: Campo operativo para skin camera distance rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin camera distance rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin camera distance rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_CAMERA_DISTANCE_RULE_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_CAMERA_DISTANCE_RULE_VENDOR
- Fallback: Reforzar skin camera distance rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1525 — hair_color_base_vendor_repair
- Definición: Campo operativo para hair color base dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair color base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair color base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_COLOR_BASE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_COLOR_BASE_VENDOR_REPAIR
- Fallback: Reforzar hair color base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1526 — hair_subtone_vendor_repair
- Definición: Campo operativo para hair subtone dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair subtone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair subtone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_SUBTONE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_SUBTONE_VENDOR_REPAIR
- Fallback: Reforzar hair subtone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1527 — hair_density_vendor_repair
- Definición: Campo operativo para hair density dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_DENSITY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_DENSITY_VENDOR_REPAIR
- Fallback: Reforzar hair density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1528 — strand_thickness_vendor_repair
- Definición: Campo operativo para strand thickness dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar strand thickness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar strand thickness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STRAND_THICKNESS_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STRAND_THICKNESS_VENDOR_REPAIR
- Fallback: Reforzar strand thickness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1529 — hairline_shape_vendor_repair
- Definición: Campo operativo para hairline shape dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hairline shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hairline shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIRLINE_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIRLINE_SHAPE_VENDOR_REPAIR
- Fallback: Reforzar hairline shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1530 — hair_length_vendor_repair
- Definición: Campo operativo para hair length dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_LENGTH_VENDOR_REPAIR
- Fallback: Reforzar hair length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1531 — hair_parting_vendor_repair
- Definición: Campo operativo para hair parting dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair parting como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair parting como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_PARTING_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_PARTING_VENDOR_REPAIR
- Fallback: Reforzar hair parting con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1532 — layering_rule_vendor_repair
- Definición: Campo operativo para layering rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar layering rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar layering rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LAYERING_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LAYERING_RULE_VENDOR_REPAIR
- Fallback: Reforzar layering rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1533 — volume_rule_vendor_repair
- Definición: Campo operativo para volume rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar volume rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar volume rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOLUME_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOLUME_RULE_VENDOR_REPAIR
- Fallback: Reforzar volume rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1534 — frizz_level_vendor_repair
- Definición: Campo operativo para frizz level dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar frizz level como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar frizz level como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FRIZZ_LEVEL_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FRIZZ_LEVEL_VENDOR_REPAIR
- Fallback: Reforzar frizz level con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1535 — baby_hairs_vendor_repair
- Definición: Campo operativo para baby hairs dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar baby hairs como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar baby hairs como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BABY_HAIRS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BABY_HAIRS_VENDOR_REPAIR
- Fallback: Reforzar baby hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1536 — flyaway_hairs_vendor_repair
- Definición: Campo operativo para flyaway hairs dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar flyaway hairs como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar flyaway hairs como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLYAWAY_HAIRS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLYAWAY_HAIRS_VENDOR_REPAIR
- Fallback: Reforzar flyaway hairs con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1537 — humidity_response_vendor_repair
- Definición: Campo operativo para humidity response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar humidity response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar humidity response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HUMIDITY_RESPONSE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HUMIDITY_RESPONSE_VENDOR_REPAIR
- Fallback: Reforzar humidity response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1538 — wind_response_vendor_repair
- Definición: Campo operativo para wind response dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wind response como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wind response como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WIND_RESPONSE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WIND_RESPONSE_VENDOR_REPAIR
- Fallback: Reforzar wind response con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1539 — strand_motion_vendor_repair
- Definición: Campo operativo para strand motion dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar strand motion como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar strand motion como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STRAND_MOTION_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STRAND_MOTION_VENDOR_REPAIR
- Fallback: Reforzar strand motion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_1540 — hair_shadow_contact_vendor_repair
- Definición: Campo operativo para hair shadow contact dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair shadow contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair shadow contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_SHADOW_CONTACT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_SHADOW_CONTACT_VENDOR_REPAI
- Fallback: Reforzar hair shadow contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1541 — hair_face_occlusion_rule_vendor_repair
- Definición: Campo operativo para hair face occlusion rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair face occlusion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair face occlusion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_FACE_OCCLUSION_RULE_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_FACE_OCCLUSION_RULE_VENDOR_
- Fallback: Reforzar hair face occlusion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1542 — eye_wetness_vendor_repair
- Definición: Campo operativo para eye wetness dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye wetness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye wetness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_WETNESS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_WETNESS_VENDOR_REPAIR
- Fallback: Reforzar eye wetness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1543 — sclera_natural_variation_vendor_repair
- Definición: Campo operativo para sclera natural variation dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sclera natural variation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sclera natural variation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCLERA_NATURAL_VARIATION_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCLERA_NATURAL_VARIATION_VENDOR_
- Fallback: Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1544 — lip_texture_vendor_repair
- Definición: Campo operativo para lip texture dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_TEXTURE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_TEXTURE_VENDOR_REPAIR
- Fallback: Reforzar lip texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1545 — lip_specular_rule_vendor_repair
- Definición: Campo operativo para lip specular rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip specular rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip specular rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_SPECULAR_RULE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_SPECULAR_RULE_VENDOR_REPAIR
- Fallback: Reforzar lip specular rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1546 — teeth_natural_rule_vendor_repair
- Definición: Campo operativo para teeth natural rule dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar teeth natural rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar teeth natural rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEETH_NATURAL_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEETH_NATURAL_RULE_VENDOR_REPAIR
- Fallback: Reforzar teeth natural rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1547 — skin_hair_color_harmony_vendor_repair
- Definición: Campo operativo para skin hair color harmony dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin hair color harmony como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin hair color harmony como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_HAIR_COLOR_HARMONY_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_HAIR_COLOR_HARMONY_VENDOR_R
- Fallback: Reforzar skin hair color harmony con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1548 — skin_makeup_continuity_vendor_repair
- Definición: Campo operativo para skin makeup continuity dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin makeup continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin makeup continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_MAKEUP_CONTINUITY_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_MAKEUP_CONTINUITY_VENDOR_RE
- Fallback: Reforzar skin makeup continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1549 — hair_video_continuity_vendor_repair
- Definición: Campo operativo para hair video continuity dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair video continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair video continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_VIDEO_CONTINUITY_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_VIDEO_CONTINUITY_VENDOR_REP
- Fallback: Reforzar hair video continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1550 — plastic_skin_blocker_vendor_repair
- Definición: Campo operativo para plastic skin blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar plastic skin blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar plastic skin blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PLASTIC_SKIN_BLOCKER_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PLASTIC_SKIN_BLOCKER_VENDOR_REPA
- Fallback: Reforzar plastic skin blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1551 — hair_helmet_blocker_vendor_repair
- Definición: Campo operativo para hair helmet blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair helmet blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair helmet blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_HELMET_BLOCKER_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_HELMET_BLOCKER_VENDOR_REPAI
- Fallback: Reforzar hair helmet blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1552 — overblur_blocker_vendor_repair
- Definición: Campo operativo para overblur blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar overblur blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar overblur blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OVERBLUR_BLOCKER_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OVERBLUR_BLOCKER_VENDOR_REPAIR
- Fallback: Reforzar overblur blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1553 — dead_eyes_blocker_vendor_repair
- Definición: Campo operativo para dead eyes blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dead eyes blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dead eyes blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DEAD_EYES_BLOCKER_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DEAD_EYES_BLOCKER_VENDOR_REPAIR
- Fallback: Reforzar dead eyes blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1554 — skin_tone_shift_blocker_vendor_repair
- Definición: Campo operativo para skin tone shift blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar skin tone shift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar skin tone shift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SKIN_TONE_SHIFT_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SKIN_TONE_SHIFT_BLOCKER_VENDOR_R
- Fallback: Reforzar skin tone shift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1555 — hair_length_drift_blocker_vendor_repair
- Definición: Campo operativo para hair length drift blocker dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair length drift blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair length drift blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_LENGTH_DRIFT_BLOCKER_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_LENGTH_DRIFT_BLOCKER_VENDOR
- Fallback: Reforzar hair length drift blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1556 — cgi_skin_repair_vendor_repair
- Definición: Campo operativo para cgi skin repair dentro de Piel, dermatología visual, cabello y materialidad humana. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cgi skin repair como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cgi skin repair como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CGI_SKIN_REPAIR_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CGI_SKIN_REPAIR_VENDOR_REPAIR
- Fallback: Reforzar cgi skin repair con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
