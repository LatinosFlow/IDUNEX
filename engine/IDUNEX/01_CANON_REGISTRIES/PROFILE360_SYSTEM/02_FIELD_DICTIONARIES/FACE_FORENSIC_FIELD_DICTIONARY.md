## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Rostro forense, landmarks, edad visual y autenticación de identidad

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_FACE_0058` | `face_shape` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACE_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar face shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0059` | `cranial_visual_volume` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CRANIAL_VISUAL_VOLUME_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar cranial visual volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0060` | `vertical_thirds` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VERTICAL_THIRDS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar vertical thirds con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0061` | `horizontal_fifths` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HORIZONTAL_FIFTHS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar horizontal fifths con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0062` | `forehead_height` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOREHEAD_HEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar forehead height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_HAIR_0063` | `hairline_relation` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIRLINE_RELATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hairline relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0064` | `temple_width` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEMPLE_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar temple width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0065` | `cheekbone_position` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHEEKBONE_POSITION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar cheekbone position con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0066` | `midface_length` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIDFACE_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar midface length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0067` | `lower_face_ratio` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_FACE_RATIO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lower face ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0068` | `jaw_angle` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_ANGLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar jaw angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0069` | `jaw_softness` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_SOFTNESS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar jaw softness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0070` | `chin_projection` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHIN_PROJECTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar chin projection con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0071` | `chin_width` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHIN_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar chin width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0072` | `facial_asymmetry_map` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACIAL_ASYMMETRY_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar facial asymmetry map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0073` | `age_face_signature` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AGE_FACE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar age face signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0074` | `eye_shape` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eye shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0075` | `eye_size` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SIZE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eye size con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0076` | `eye_spacing` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SPACING_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eye spacing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0077` | `eye_tilt` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_TILT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eye tilt con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0078` | `eyelid_fold` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYELID_FOLD_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eyelid fold con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0079` | `upper_lid_weight` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UPPER_LID_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar upper lid weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0080` | `lower_lid_tension` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_LID_TENSION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lower lid tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0081` | `iris_color` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IRIS_COLOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar iris color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0082` | `iris_signature` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IRIS_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar iris signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0083` | `catchlight_rule` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CATCHLIGHT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar catchlight rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0084` | `gaze_signature` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GAZE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar gaze signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0085` | `blink_pattern` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BLINK_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar blink pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0086` | `eye_emotion_map` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_EMOTION_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0087` | `under_eye_texture` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UNDER_EYE_TEXTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar under eye texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0088` | `sclera_natural_variation` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCLERA_NATURAL_VARIATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0089` | `brow_density` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_DENSITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar brow density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0090` | `brow_arc` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_ARC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar brow arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0091` | `brow_height` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_HEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar brow height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0092` | `brow_eye_distance` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_EYE_DISTANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar brow eye distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0093` | `nose_bridge` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_BRIDGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar nose bridge con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0094` | `nose_dorsum` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_DORSUM_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar nose dorsum con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0095` | `nose_tip` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_TIP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar nose tip con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0096` | `nostril_width` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSTRIL_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar nostril width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0097` | `alar_shape` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ALAR_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar alar shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0098` | `philtrum_length` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PHILTRUM_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar philtrum length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0099` | `lip_ratio` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_RATIO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lip ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0100` | `upper_lip_shape` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UPPER_LIP_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar upper lip shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0101` | `lower_lip_volume` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_LIP_VOLUME_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lower lip volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0102` | `cupid_bow` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CUPID_BOW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar cupid bow con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0103` | `mouth_width` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOUTH_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar mouth width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0104` | `smile_signature` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SMILE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar smile signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0105` | `teeth_visibility_rule` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEETH_VISIBILITY_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar teeth visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0106` | `wrong_face_blocker` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_FACE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wrong face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0107` | `same_face_blocker` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SAME_FACE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar same face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0108` | `generic_beauty_blocker` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_BEAUTY_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar generic beauty blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0109` | `over_symmetry_blocker` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OVER_SYMMETRY_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar over symmetry blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0110` | `makeup_face_drift_rule` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MAKEUP_FACE_DRIFT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar makeup face drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0111` | `lens_face_distortion_rule` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FACE_DISTORTION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lens face distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0112` | `anchor_face_match_rule` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANCHOR_FACE_MATCH_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar anchor face match rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0113` | `face_regression_test` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACE_REGRESSION_TEST_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar face regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0507` | `face_shape_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACE_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar face shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0508` | `cranial_visual_volume_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CRANIAL_VISUAL_VOLUME_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cranial visual volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0509` | `vertical_thirds_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VERTICAL_THIRDS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vertical thirds con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0510` | `horizontal_fifths_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HORIZONTAL_FIFTHS_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar horizontal fifths con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0511` | `forehead_height_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOREHEAD_HEIGHT_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar forehead height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_HAIR_0512` | `hairline_relation_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIRLINE_RELATION_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hairline relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0513` | `temple_width_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEMPLE_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar temple width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0514` | `cheekbone_position_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHEEKBONE_POSITION_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cheekbone position con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0515` | `midface_length_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIDFACE_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar midface length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0516` | `lower_face_ratio_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_FACE_RATIO_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower face ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0517` | `jaw_angle_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_ANGLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0518` | `jaw_softness_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_SOFTNESS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw softness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0519` | `chin_projection_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHIN_PROJECTION_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chin projection con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0520` | `chin_width_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHIN_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chin width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0521` | `facial_asymmetry_map_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACIAL_ASYMMETRY_MAP_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar facial asymmetry map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0522` | `age_face_signature_prompt_effect` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AGE_FACE_SIGNATURE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar age face signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0523` | `eye_shape_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0524` | `eye_size_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SIZE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye size con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0525` | `eye_spacing_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SPACING_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye spacing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0526` | `eye_tilt_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_TILT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye tilt con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0527` | `eyelid_fold_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYELID_FOLD_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eyelid fold con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0528` | `upper_lid_weight_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UPPER_LID_WEIGHT_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar upper lid weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0529` | `lower_lid_tension_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_LID_TENSION_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower lid tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0530` | `iris_color_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IRIS_COLOR_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iris color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0531` | `iris_signature_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IRIS_SIGNATURE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iris signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0532` | `catchlight_rule_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CATCHLIGHT_RULE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar catchlight rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0533` | `gaze_signature_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GAZE_SIGNATURE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar gaze signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0534` | `blink_pattern_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BLINK_PATTERN_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar blink pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0535` | `eye_emotion_map_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_EMOTION_MAP_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0536` | `under_eye_texture_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UNDER_EYE_TEXTURE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar under eye texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0537` | `sclera_natural_variation_prompt_effect` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCLERA_NATURAL_VARIATION_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0538` | `brow_density_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_DENSITY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0539` | `brow_arc_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_ARC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0540` | `brow_height_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_HEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0541` | `brow_eye_distance_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_EYE_DISTANCE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow eye distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0542` | `nose_bridge_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_BRIDGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose bridge con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0543` | `nose_dorsum_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_DORSUM_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose dorsum con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0544` | `nose_tip_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_TIP_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose tip con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0545` | `nostril_width_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSTRIL_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nostril width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0546` | `alar_shape_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ALAR_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar alar shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0547` | `philtrum_length_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PHILTRUM_LENGTH_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar philtrum length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0548` | `lip_ratio_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_RATIO_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0549` | `upper_lip_shape_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UPPER_LIP_SHAPE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar upper lip shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0550` | `lower_lip_volume_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_LIP_VOLUME_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower lip volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0551` | `cupid_bow_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CUPID_BOW_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cupid bow con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0552` | `mouth_width_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOUTH_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mouth width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0553` | `smile_signature_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SMILE_SIGNATURE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar smile signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0554` | `teeth_visibility_rule_prompt_effect` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEETH_VISIBILITY_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar teeth visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0555` | `wrong_face_blocker_prompt_effect` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_FACE_BLOCKER_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0556` | `same_face_blocker_prompt_effect` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SAME_FACE_BLOCKER_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar same face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0557` | `generic_beauty_blocker_prompt_effect` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_BEAUTY_BLOCKER_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic beauty blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0558` | `over_symmetry_blocker_prompt_effect` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OVER_SYMMETRY_BLOCKER_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar over symmetry blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_0559` | `makeup_face_drift_rule_prompt_effect` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MAKEUP_FACE_DRIFT_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar makeup face drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0560` | `lens_face_distortion_rule_prompt_effect` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FACE_DISTORTION_RULE_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens face distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0561` | `anchor_face_match_rule_prompt_effect` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANCHOR_FACE_MATCH_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar anchor face match rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0562` | `face_regression_test_prompt_effect` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACE_REGRESSION_TEST_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar face regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0956` | `face_shape_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACE_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar face shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0957` | `cranial_visual_volume_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CRANIAL_VISUAL_VOLUME_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cranial visual volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0958` | `vertical_thirds_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VERTICAL_THIRDS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vertical thirds con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0959` | `horizontal_fifths_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HORIZONTAL_FIFTHS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar horizontal fifths con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0960` | `forehead_height_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOREHEAD_HEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar forehead height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_HAIR_0961` | `hairline_relation_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIRLINE_RELATION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hairline relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0962` | `temple_width_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEMPLE_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar temple width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0963` | `cheekbone_position_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHEEKBONE_POSITION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cheekbone position con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0964` | `midface_length_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIDFACE_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar midface length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0965` | `lower_face_ratio_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_FACE_RATIO_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower face ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0966` | `jaw_angle_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_ANGLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0967` | `jaw_softness_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_SOFTNESS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw softness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0968` | `chin_projection_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHIN_PROJECTION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chin projection con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0969` | `chin_width_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHIN_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chin width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0970` | `facial_asymmetry_map_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACIAL_ASYMMETRY_MAP_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar facial asymmetry map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0971` | `age_face_signature_qa_matrix` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AGE_FACE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar age face signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0972` | `eye_shape_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0973` | `eye_size_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SIZE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye size con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0974` | `eye_spacing_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SPACING_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye spacing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0975` | `eye_tilt_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_TILT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye tilt con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0976` | `eyelid_fold_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYELID_FOLD_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eyelid fold con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0977` | `upper_lid_weight_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UPPER_LID_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar upper lid weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0978` | `lower_lid_tension_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_LID_TENSION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower lid tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0979` | `iris_color_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IRIS_COLOR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iris color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0980` | `iris_signature_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IRIS_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iris signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0981` | `catchlight_rule_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CATCHLIGHT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar catchlight rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0982` | `gaze_signature_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GAZE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar gaze signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0983` | `blink_pattern_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BLINK_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar blink pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0984` | `eye_emotion_map_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_EMOTION_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0985` | `under_eye_texture_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UNDER_EYE_TEXTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar under eye texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_0986` | `sclera_natural_variation_qa_matrix` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCLERA_NATURAL_VARIATION_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0987` | `brow_density_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_DENSITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0988` | `brow_arc_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_ARC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0989` | `brow_height_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_HEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0990` | `brow_eye_distance_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_EYE_DISTANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow eye distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0991` | `nose_bridge_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_BRIDGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose bridge con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0992` | `nose_dorsum_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_DORSUM_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose dorsum con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0993` | `nose_tip_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_TIP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose tip con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0994` | `nostril_width_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSTRIL_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nostril width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0995` | `alar_shape_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ALAR_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar alar shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0996` | `philtrum_length_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PHILTRUM_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar philtrum length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0997` | `lip_ratio_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_RATIO_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0998` | `upper_lip_shape_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UPPER_LIP_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar upper lip shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0999` | `lower_lip_volume_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_LIP_VOLUME_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower lip volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1000` | `cupid_bow_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CUPID_BOW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cupid bow con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1001` | `mouth_width_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOUTH_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mouth width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1002` | `smile_signature_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SMILE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar smile signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1003` | `teeth_visibility_rule_qa_matrix` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEETH_VISIBILITY_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar teeth visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1004` | `wrong_face_blocker_qa_matrix` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_FACE_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1005` | `same_face_blocker_qa_matrix` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SAME_FACE_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar same face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1006` | `generic_beauty_blocker_qa_matrix` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_BEAUTY_BLOCKER_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic beauty blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1007` | `over_symmetry_blocker_qa_matrix` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OVER_SYMMETRY_BLOCKER_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar over symmetry blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1008` | `makeup_face_drift_rule_qa_matrix` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MAKEUP_FACE_DRIFT_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar makeup face drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1009` | `lens_face_distortion_rule_qa_matrix` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FACE_DISTORTION_RULE_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens face distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1010` | `anchor_face_match_rule_qa_matrix` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANCHOR_FACE_MATCH_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar anchor face match rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1011` | `face_regression_test_qa_matrix` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACE_REGRESSION_TEST_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar face regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1405` | `face_shape_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACE_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar face shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1406` | `cranial_visual_volume_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CRANIAL_VISUAL_VOLUME_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cranial visual volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1407` | `vertical_thirds_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VERTICAL_THIRDS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar vertical thirds con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1408` | `horizontal_fifths_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HORIZONTAL_FIFTHS_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar horizontal fifths con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1409` | `forehead_height_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOREHEAD_HEIGHT_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar forehead height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_HAIR_1410` | `hairline_relation_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIRLINE_RELATION_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hairline relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1411` | `temple_width_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEMPLE_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar temple width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1412` | `cheekbone_position_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHEEKBONE_POSITION_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cheekbone position con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1413` | `midface_length_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MIDFACE_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar midface length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1414` | `lower_face_ratio_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_FACE_RATIO_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower face ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1415` | `jaw_angle_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_ANGLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1416` | `jaw_softness_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_SOFTNESS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw softness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1417` | `chin_projection_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHIN_PROJECTION_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chin projection con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1418` | `chin_width_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CHIN_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar chin width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1419` | `facial_asymmetry_map_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACIAL_ASYMMETRY_MAP_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar facial asymmetry map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1420` | `age_face_signature_vendor_repair` | shape | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_AGE_FACE_SIGNATURE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar age face signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1421` | `eye_shape_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1422` | `eye_size_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SIZE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye size con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1423` | `eye_spacing_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_SPACING_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye spacing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1424` | `eye_tilt_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_TILT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye tilt con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1425` | `eyelid_fold_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYELID_FOLD_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eyelid fold con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1426` | `upper_lid_weight_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UPPER_LID_WEIGHT_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar upper lid weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1427` | `lower_lid_tension_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_LID_TENSION_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower lid tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1428` | `iris_color_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IRIS_COLOR_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iris color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1429` | `iris_signature_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IRIS_SIGNATURE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar iris signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_1430` | `catchlight_rule_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CATCHLIGHT_RULE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar catchlight rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1431` | `gaze_signature_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GAZE_SIGNATURE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar gaze signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1432` | `blink_pattern_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BLINK_PATTERN_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar blink pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1433` | `eye_emotion_map_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_EMOTION_MAP_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1434` | `under_eye_texture_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UNDER_EYE_TEXTURE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar under eye texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1435` | `sclera_natural_variation_vendor_repair` | eyes | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SCLERA_NATURAL_VARIATION_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1436` | `brow_density_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_DENSITY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1437` | `brow_arc_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_ARC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1438` | `brow_height_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_HEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1439` | `brow_eye_distance_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_EYE_DISTANCE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow eye distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1440` | `nose_bridge_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_BRIDGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose bridge con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1441` | `nose_dorsum_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_DORSUM_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose dorsum con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1442` | `nose_tip_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSE_TIP_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nose tip con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1443` | `nostril_width_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NOSTRIL_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nostril width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1444` | `alar_shape_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ALAR_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar alar shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1445` | `philtrum_length_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PHILTRUM_LENGTH_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar philtrum length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1446` | `lip_ratio_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LIP_RATIO_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lip ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1447` | `upper_lip_shape_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UPPER_LIP_SHAPE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar upper lip shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1448` | `lower_lip_volume_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LOWER_LIP_VOLUME_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lower lip volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1449` | `cupid_bow_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CUPID_BOW_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar cupid bow con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1450` | `mouth_width_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOUTH_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mouth width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1451` | `smile_signature_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SMILE_SIGNATURE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar smile signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1452` | `teeth_visibility_rule_vendor_repair` | brows_nose_mouth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEETH_VISIBILITY_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar teeth visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1453` | `wrong_face_blocker_vendor_repair` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_FACE_BLOCKER_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1454` | `same_face_blocker_vendor_repair` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SAME_FACE_BLOCKER_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar same face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1455` | `generic_beauty_blocker_vendor_repair` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_GENERIC_BEAUTY_BLOCKER_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar generic beauty blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1456` | `over_symmetry_blocker_vendor_repair` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OVER_SYMMETRY_BLOCKER_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar over symmetry blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SKIN_1457` | `makeup_face_drift_rule_vendor_repair` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MAKEUP_FACE_DRIFT_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar makeup face drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1458` | `lens_face_distortion_rule_vendor_repair` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LENS_FACE_DISTORTION_RULE_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lens face distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1459` | `anchor_face_match_rule_vendor_repair` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANCHOR_FACE_MATCH_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar anchor face match rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_FACE_1460` | `face_regression_test_vendor_repair` | auth | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACE_REGRESSION_TEST_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar face regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_FACE_0058 — face_shape
- Definición: Campo operativo para face shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar face shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar face shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACE_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FACE_SHAPE_DRIFT_OR_GAP
- Fallback: Reforzar face shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0059 — cranial_visual_volume
- Definición: Campo operativo para cranial visual volume dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar cranial visual volume como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cranial visual volume como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CRANIAL_VISUAL_VOLUME_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CRANIAL_VISUAL_VOLUME_DRIFT_OR_GAP
- Fallback: Reforzar cranial visual volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0060 — vertical_thirds
- Definición: Campo operativo para vertical thirds dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar vertical thirds como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vertical thirds como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VERTICAL_THIRDS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VERTICAL_THIRDS_DRIFT_OR_GAP
- Fallback: Reforzar vertical thirds con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0061 — horizontal_fifths
- Definición: Campo operativo para horizontal fifths dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar horizontal fifths como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar horizontal fifths como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HORIZONTAL_FIFTHS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HORIZONTAL_FIFTHS_DRIFT_OR_GAP
- Fallback: Reforzar horizontal fifths con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0062 — forehead_height
- Definición: Campo operativo para forehead height dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar forehead height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar forehead height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOREHEAD_HEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FOREHEAD_HEIGHT_DRIFT_OR_GAP
- Fallback: Reforzar forehead height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_HAIR_0063 — hairline_relation
- Definición: Campo operativo para hairline relation dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hairline relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hairline relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIRLINE_RELATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIRLINE_RELATION_DRIFT_OR_GAP
- Fallback: Reforzar hairline relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0064 — temple_width
- Definición: Campo operativo para temple width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar temple width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar temple width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEMPLE_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TEMPLE_WIDTH_DRIFT_OR_GAP
- Fallback: Reforzar temple width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0065 — cheekbone_position
- Definición: Campo operativo para cheekbone position dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar cheekbone position como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cheekbone position como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHEEKBONE_POSITION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CHEEKBONE_POSITION_DRIFT_OR_GAP
- Fallback: Reforzar cheekbone position con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0066 — midface_length
- Definición: Campo operativo para midface length dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar midface length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar midface length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIDFACE_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MIDFACE_LENGTH_DRIFT_OR_GAP
- Fallback: Reforzar midface length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0067 — lower_face_ratio
- Definición: Campo operativo para lower face ratio dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lower face ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower face ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_FACE_RATIO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LOWER_FACE_RATIO_DRIFT_OR_GAP
- Fallback: Reforzar lower face ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0068 — jaw_angle
- Definición: Campo operativo para jaw angle dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar jaw angle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw angle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_ANGLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_JAW_ANGLE_DRIFT_OR_GAP
- Fallback: Reforzar jaw angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0069 — jaw_softness
- Definición: Campo operativo para jaw softness dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar jaw softness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw softness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_SOFTNESS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_JAW_SOFTNESS_DRIFT_OR_GAP
- Fallback: Reforzar jaw softness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0070 — chin_projection
- Definición: Campo operativo para chin projection dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar chin projection como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chin projection como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHIN_PROJECTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CHIN_PROJECTION_DRIFT_OR_GAP
- Fallback: Reforzar chin projection con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0071 — chin_width
- Definición: Campo operativo para chin width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar chin width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chin width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHIN_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CHIN_WIDTH_DRIFT_OR_GAP
- Fallback: Reforzar chin width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0072 — facial_asymmetry_map
- Definición: Campo operativo para facial asymmetry map dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar facial asymmetry map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar facial asymmetry map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACIAL_ASYMMETRY_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FACIAL_ASYMMETRY_MAP_DRIFT_OR_GAP
- Fallback: Reforzar facial asymmetry map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0073 — age_face_signature
- Definición: Campo operativo para age face signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar age face signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar age face signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AGE_FACE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_AGE_FACE_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar age face signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0074 — eye_shape
- Definición: Campo operativo para eye shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eye shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYE_SHAPE_DRIFT_OR_GAP
- Fallback: Reforzar eye shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0075 — eye_size
- Definición: Campo operativo para eye size dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eye size como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye size como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SIZE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYE_SIZE_DRIFT_OR_GAP
- Fallback: Reforzar eye size con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0076 — eye_spacing
- Definición: Campo operativo para eye spacing dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eye spacing como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye spacing como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SPACING_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYE_SPACING_DRIFT_OR_GAP
- Fallback: Reforzar eye spacing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0077 — eye_tilt
- Definición: Campo operativo para eye tilt dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eye tilt como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye tilt como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_TILT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYE_TILT_DRIFT_OR_GAP
- Fallback: Reforzar eye tilt con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0078 — eyelid_fold
- Definición: Campo operativo para eyelid fold dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eyelid fold como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eyelid fold como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYELID_FOLD_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYELID_FOLD_DRIFT_OR_GAP
- Fallback: Reforzar eyelid fold con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0079 — upper_lid_weight
- Definición: Campo operativo para upper lid weight dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar upper lid weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar upper lid weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UPPER_LID_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_UPPER_LID_WEIGHT_DRIFT_OR_GAP
- Fallback: Reforzar upper lid weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0080 — lower_lid_tension
- Definición: Campo operativo para lower lid tension dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lower lid tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower lid tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_LID_TENSION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LOWER_LID_TENSION_DRIFT_OR_GAP
- Fallback: Reforzar lower lid tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0081 — iris_color
- Definición: Campo operativo para iris color dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar iris color como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iris color como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IRIS_COLOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_IRIS_COLOR_DRIFT_OR_GAP
- Fallback: Reforzar iris color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0082 — iris_signature
- Definición: Campo operativo para iris signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar iris signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iris signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IRIS_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_IRIS_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar iris signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0083 — catchlight_rule
- Definición: Campo operativo para catchlight rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar catchlight rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar catchlight rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CATCHLIGHT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CATCHLIGHT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar catchlight rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0084 — gaze_signature
- Definición: Campo operativo para gaze signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar gaze signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar gaze signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GAZE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_GAZE_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar gaze signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0085 — blink_pattern
- Definición: Campo operativo para blink pattern dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar blink pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar blink pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BLINK_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BLINK_PATTERN_DRIFT_OR_GAP
- Fallback: Reforzar blink pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0086 — eye_emotion_map
- Definición: Campo operativo para eye emotion map dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eye emotion map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye emotion map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_EMOTION_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYE_EMOTION_MAP_DRIFT_OR_GAP
- Fallback: Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0087 — under_eye_texture
- Definición: Campo operativo para under eye texture dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar under eye texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar under eye texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UNDER_EYE_TEXTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_UNDER_EYE_TEXTURE_DRIFT_OR_GAP
- Fallback: Reforzar under eye texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0088 — sclera_natural_variation
- Definición: Campo operativo para sclera natural variation dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sclera natural variation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sclera natural variation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCLERA_NATURAL_VARIATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SCLERA_NATURAL_VARIATION_DRIFT_OR_GAP
- Fallback: Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0089 — brow_density
- Definición: Campo operativo para brow density dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar brow density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_DENSITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BROW_DENSITY_DRIFT_OR_GAP
- Fallback: Reforzar brow density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0090 — brow_arc
- Definición: Campo operativo para brow arc dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar brow arc como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow arc como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_ARC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BROW_ARC_DRIFT_OR_GAP
- Fallback: Reforzar brow arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0091 — brow_height
- Definición: Campo operativo para brow height dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar brow height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_HEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BROW_HEIGHT_DRIFT_OR_GAP
- Fallback: Reforzar brow height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0092 — brow_eye_distance
- Definición: Campo operativo para brow eye distance dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar brow eye distance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow eye distance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_EYE_DISTANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BROW_EYE_DISTANCE_DRIFT_OR_GAP
- Fallback: Reforzar brow eye distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0093 — nose_bridge
- Definición: Campo operativo para nose bridge dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar nose bridge como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose bridge como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_BRIDGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NOSE_BRIDGE_DRIFT_OR_GAP
- Fallback: Reforzar nose bridge con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0094 — nose_dorsum
- Definición: Campo operativo para nose dorsum dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar nose dorsum como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose dorsum como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_DORSUM_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NOSE_DORSUM_DRIFT_OR_GAP
- Fallback: Reforzar nose dorsum con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0095 — nose_tip
- Definición: Campo operativo para nose tip dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar nose tip como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose tip como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_TIP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NOSE_TIP_DRIFT_OR_GAP
- Fallback: Reforzar nose tip con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0096 — nostril_width
- Definición: Campo operativo para nostril width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar nostril width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nostril width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSTRIL_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NOSTRIL_WIDTH_DRIFT_OR_GAP
- Fallback: Reforzar nostril width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0097 — alar_shape
- Definición: Campo operativo para alar shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar alar shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar alar shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ALAR_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ALAR_SHAPE_DRIFT_OR_GAP
- Fallback: Reforzar alar shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0098 — philtrum_length
- Definición: Campo operativo para philtrum length dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar philtrum length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar philtrum length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PHILTRUM_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PHILTRUM_LENGTH_DRIFT_OR_GAP
- Fallback: Reforzar philtrum length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0099 — lip_ratio
- Definición: Campo operativo para lip ratio dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lip ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_RATIO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LIP_RATIO_DRIFT_OR_GAP
- Fallback: Reforzar lip ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0100 — upper_lip_shape
- Definición: Campo operativo para upper lip shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar upper lip shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar upper lip shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UPPER_LIP_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_UPPER_LIP_SHAPE_DRIFT_OR_GAP
- Fallback: Reforzar upper lip shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0101 — lower_lip_volume
- Definición: Campo operativo para lower lip volume dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lower lip volume como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower lip volume como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_LIP_VOLUME_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LOWER_LIP_VOLUME_DRIFT_OR_GAP
- Fallback: Reforzar lower lip volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0102 — cupid_bow
- Definición: Campo operativo para cupid bow dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar cupid bow como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cupid bow como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CUPID_BOW_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CUPID_BOW_DRIFT_OR_GAP
- Fallback: Reforzar cupid bow con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0103 — mouth_width
- Definición: Campo operativo para mouth width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar mouth width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mouth width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOUTH_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MOUTH_WIDTH_DRIFT_OR_GAP
- Fallback: Reforzar mouth width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0104 — smile_signature
- Definición: Campo operativo para smile signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar smile signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar smile signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SMILE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SMILE_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar smile signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0105 — teeth_visibility_rule
- Definición: Campo operativo para teeth visibility rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar teeth visibility rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar teeth visibility rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEETH_VISIBILITY_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TEETH_VISIBILITY_RULE_DRIFT_OR_GAP
- Fallback: Reforzar teeth visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0106 — wrong_face_blocker
- Definición: Campo operativo para wrong face blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wrong face blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong face blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_FACE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WRONG_FACE_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar wrong face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0107 — same_face_blocker
- Definición: Campo operativo para same face blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar same face blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar same face blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SAME_FACE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SAME_FACE_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar same face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0108 — generic_beauty_blocker
- Definición: Campo operativo para generic beauty blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar generic beauty blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic beauty blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_BEAUTY_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_GENERIC_BEAUTY_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar generic beauty blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0109 — over_symmetry_blocker
- Definición: Campo operativo para over symmetry blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar over symmetry blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar over symmetry blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OVER_SYMMETRY_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_OVER_SYMMETRY_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar over symmetry blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0110 — makeup_face_drift_rule
- Definición: Campo operativo para makeup face drift rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar makeup face drift rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar makeup face drift rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MAKEUP_FACE_DRIFT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MAKEUP_FACE_DRIFT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar makeup face drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0111 — lens_face_distortion_rule
- Definición: Campo operativo para lens face distortion rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lens face distortion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens face distortion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FACE_DISTORTION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LENS_FACE_DISTORTION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar lens face distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0112 — anchor_face_match_rule
- Definición: Campo operativo para anchor face match rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar anchor face match rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar anchor face match rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANCHOR_FACE_MATCH_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ANCHOR_FACE_MATCH_RULE_DRIFT_OR_GAP
- Fallback: Reforzar anchor face match rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0113 — face_regression_test
- Definición: Campo operativo para face regression test dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar face regression test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar face regression test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACE_REGRESSION_TEST_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FACE_REGRESSION_TEST_DRIFT_OR_GAP
- Fallback: Reforzar face regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0507 — face_shape_prompt_effect
- Definición: Campo operativo para face shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar face shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar face shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACE_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACE_SHAPE_PROMPT_EFFECT
- Fallback: Reforzar face shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0508 — cranial_visual_volume_prompt_effect
- Definición: Campo operativo para cranial visual volume dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cranial visual volume como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cranial visual volume como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CRANIAL_VISUAL_VOLUME_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CRANIAL_VISUAL_VOLUME_PROMPT_EFF
- Fallback: Reforzar cranial visual volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0509 — vertical_thirds_prompt_effect
- Definición: Campo operativo para vertical thirds dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vertical thirds como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vertical thirds como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VERTICAL_THIRDS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VERTICAL_THIRDS_PROMPT_EFFECT
- Fallback: Reforzar vertical thirds con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0510 — horizontal_fifths_prompt_effect
- Definición: Campo operativo para horizontal fifths dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar horizontal fifths como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar horizontal fifths como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HORIZONTAL_FIFTHS_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HORIZONTAL_FIFTHS_PROMPT_EFFECT
- Fallback: Reforzar horizontal fifths con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0511 — forehead_height_prompt_effect
- Definición: Campo operativo para forehead height dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar forehead height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar forehead height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOREHEAD_HEIGHT_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOREHEAD_HEIGHT_PROMPT_EFFECT
- Fallback: Reforzar forehead height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_HAIR_0512 — hairline_relation_prompt_effect
- Definición: Campo operativo para hairline relation dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hairline relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hairline relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIRLINE_RELATION_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIRLINE_RELATION_PROMPT_EFFECT
- Fallback: Reforzar hairline relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0513 — temple_width_prompt_effect
- Definición: Campo operativo para temple width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar temple width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar temple width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEMPLE_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEMPLE_WIDTH_PROMPT_EFFECT
- Fallback: Reforzar temple width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0514 — cheekbone_position_prompt_effect
- Definición: Campo operativo para cheekbone position dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cheekbone position como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cheekbone position como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHEEKBONE_POSITION_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHEEKBONE_POSITION_PROMPT_EFFECT
- Fallback: Reforzar cheekbone position con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0515 — midface_length_prompt_effect
- Definición: Campo operativo para midface length dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar midface length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar midface length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIDFACE_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIDFACE_LENGTH_PROMPT_EFFECT
- Fallback: Reforzar midface length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0516 — lower_face_ratio_prompt_effect
- Definición: Campo operativo para lower face ratio dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower face ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower face ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_FACE_RATIO_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_FACE_RATIO_PROMPT_EFFECT
- Fallback: Reforzar lower face ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0517 — jaw_angle_prompt_effect
- Definición: Campo operativo para jaw angle dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw angle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw angle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_ANGLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_ANGLE_PROMPT_EFFECT
- Fallback: Reforzar jaw angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0518 — jaw_softness_prompt_effect
- Definición: Campo operativo para jaw softness dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw softness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw softness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_SOFTNESS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_SOFTNESS_PROMPT_EFFECT
- Fallback: Reforzar jaw softness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0519 — chin_projection_prompt_effect
- Definición: Campo operativo para chin projection dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chin projection como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chin projection como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHIN_PROJECTION_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHIN_PROJECTION_PROMPT_EFFECT
- Fallback: Reforzar chin projection con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0520 — chin_width_prompt_effect
- Definición: Campo operativo para chin width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chin width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chin width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHIN_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHIN_WIDTH_PROMPT_EFFECT
- Fallback: Reforzar chin width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0521 — facial_asymmetry_map_prompt_effect
- Definición: Campo operativo para facial asymmetry map dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar facial asymmetry map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar facial asymmetry map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACIAL_ASYMMETRY_MAP_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACIAL_ASYMMETRY_MAP_PROMPT_EFFE
- Fallback: Reforzar facial asymmetry map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0522 — age_face_signature_prompt_effect
- Definición: Campo operativo para age face signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar age face signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar age face signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AGE_FACE_SIGNATURE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AGE_FACE_SIGNATURE_PROMPT_EFFECT
- Fallback: Reforzar age face signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0523 — eye_shape_prompt_effect
- Definición: Campo operativo para eye shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SHAPE_PROMPT_EFFECT
- Fallback: Reforzar eye shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0524 — eye_size_prompt_effect
- Definición: Campo operativo para eye size dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye size como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye size como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SIZE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SIZE_PROMPT_EFFECT
- Fallback: Reforzar eye size con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0525 — eye_spacing_prompt_effect
- Definición: Campo operativo para eye spacing dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye spacing como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye spacing como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SPACING_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SPACING_PROMPT_EFFECT
- Fallback: Reforzar eye spacing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0526 — eye_tilt_prompt_effect
- Definición: Campo operativo para eye tilt dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye tilt como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye tilt como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_TILT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_TILT_PROMPT_EFFECT
- Fallback: Reforzar eye tilt con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0527 — eyelid_fold_prompt_effect
- Definición: Campo operativo para eyelid fold dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eyelid fold como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eyelid fold como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYELID_FOLD_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYELID_FOLD_PROMPT_EFFECT
- Fallback: Reforzar eyelid fold con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0528 — upper_lid_weight_prompt_effect
- Definición: Campo operativo para upper lid weight dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar upper lid weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar upper lid weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UPPER_LID_WEIGHT_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UPPER_LID_WEIGHT_PROMPT_EFFECT
- Fallback: Reforzar upper lid weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0529 — lower_lid_tension_prompt_effect
- Definición: Campo operativo para lower lid tension dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower lid tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower lid tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_LID_TENSION_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_LID_TENSION_PROMPT_EFFECT
- Fallback: Reforzar lower lid tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0530 — iris_color_prompt_effect
- Definición: Campo operativo para iris color dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iris color como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iris color como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IRIS_COLOR_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IRIS_COLOR_PROMPT_EFFECT
- Fallback: Reforzar iris color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0531 — iris_signature_prompt_effect
- Definición: Campo operativo para iris signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iris signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iris signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IRIS_SIGNATURE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IRIS_SIGNATURE_PROMPT_EFFECT
- Fallback: Reforzar iris signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0532 — catchlight_rule_prompt_effect
- Definición: Campo operativo para catchlight rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar catchlight rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar catchlight rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CATCHLIGHT_RULE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CATCHLIGHT_RULE_PROMPT_EFFECT
- Fallback: Reforzar catchlight rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0533 — gaze_signature_prompt_effect
- Definición: Campo operativo para gaze signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar gaze signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar gaze signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GAZE_SIGNATURE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GAZE_SIGNATURE_PROMPT_EFFECT
- Fallback: Reforzar gaze signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0534 — blink_pattern_prompt_effect
- Definición: Campo operativo para blink pattern dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar blink pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar blink pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BLINK_PATTERN_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BLINK_PATTERN_PROMPT_EFFECT
- Fallback: Reforzar blink pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0535 — eye_emotion_map_prompt_effect
- Definición: Campo operativo para eye emotion map dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye emotion map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye emotion map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_EMOTION_MAP_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_EMOTION_MAP_PROMPT_EFFECT
- Fallback: Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0536 — under_eye_texture_prompt_effect
- Definición: Campo operativo para under eye texture dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar under eye texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar under eye texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UNDER_EYE_TEXTURE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UNDER_EYE_TEXTURE_PROMPT_EFFECT
- Fallback: Reforzar under eye texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0537 — sclera_natural_variation_prompt_effect
- Definición: Campo operativo para sclera natural variation dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sclera natural variation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sclera natural variation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCLERA_NATURAL_VARIATION_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCLERA_NATURAL_VARIATION_PROMPT_
- Fallback: Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0538 — brow_density_prompt_effect
- Definición: Campo operativo para brow density dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_DENSITY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_DENSITY_PROMPT_EFFECT
- Fallback: Reforzar brow density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0539 — brow_arc_prompt_effect
- Definición: Campo operativo para brow arc dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow arc como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow arc como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_ARC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_ARC_PROMPT_EFFECT
- Fallback: Reforzar brow arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0540 — brow_height_prompt_effect
- Definición: Campo operativo para brow height dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_HEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_HEIGHT_PROMPT_EFFECT
- Fallback: Reforzar brow height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0541 — brow_eye_distance_prompt_effect
- Definición: Campo operativo para brow eye distance dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow eye distance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow eye distance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_EYE_DISTANCE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_EYE_DISTANCE_PROMPT_EFFECT
- Fallback: Reforzar brow eye distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0542 — nose_bridge_prompt_effect
- Definición: Campo operativo para nose bridge dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose bridge como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose bridge como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_BRIDGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_BRIDGE_PROMPT_EFFECT
- Fallback: Reforzar nose bridge con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0543 — nose_dorsum_prompt_effect
- Definición: Campo operativo para nose dorsum dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose dorsum como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose dorsum como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_DORSUM_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_DORSUM_PROMPT_EFFECT
- Fallback: Reforzar nose dorsum con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0544 — nose_tip_prompt_effect
- Definición: Campo operativo para nose tip dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose tip como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose tip como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_TIP_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_TIP_PROMPT_EFFECT
- Fallback: Reforzar nose tip con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0545 — nostril_width_prompt_effect
- Definición: Campo operativo para nostril width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nostril width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nostril width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSTRIL_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSTRIL_WIDTH_PROMPT_EFFECT
- Fallback: Reforzar nostril width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0546 — alar_shape_prompt_effect
- Definición: Campo operativo para alar shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar alar shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar alar shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ALAR_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ALAR_SHAPE_PROMPT_EFFECT
- Fallback: Reforzar alar shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0547 — philtrum_length_prompt_effect
- Definición: Campo operativo para philtrum length dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar philtrum length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar philtrum length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PHILTRUM_LENGTH_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PHILTRUM_LENGTH_PROMPT_EFFECT
- Fallback: Reforzar philtrum length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0548 — lip_ratio_prompt_effect
- Definición: Campo operativo para lip ratio dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_RATIO_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_RATIO_PROMPT_EFFECT
- Fallback: Reforzar lip ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0549 — upper_lip_shape_prompt_effect
- Definición: Campo operativo para upper lip shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar upper lip shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar upper lip shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UPPER_LIP_SHAPE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UPPER_LIP_SHAPE_PROMPT_EFFECT
- Fallback: Reforzar upper lip shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0550 — lower_lip_volume_prompt_effect
- Definición: Campo operativo para lower lip volume dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower lip volume como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower lip volume como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_LIP_VOLUME_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_LIP_VOLUME_PROMPT_EFFECT
- Fallback: Reforzar lower lip volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0551 — cupid_bow_prompt_effect
- Definición: Campo operativo para cupid bow dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cupid bow como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cupid bow como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CUPID_BOW_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CUPID_BOW_PROMPT_EFFECT
- Fallback: Reforzar cupid bow con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0552 — mouth_width_prompt_effect
- Definición: Campo operativo para mouth width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mouth width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mouth width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOUTH_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOUTH_WIDTH_PROMPT_EFFECT
- Fallback: Reforzar mouth width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0553 — smile_signature_prompt_effect
- Definición: Campo operativo para smile signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar smile signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar smile signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SMILE_SIGNATURE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SMILE_SIGNATURE_PROMPT_EFFECT
- Fallback: Reforzar smile signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0554 — teeth_visibility_rule_prompt_effect
- Definición: Campo operativo para teeth visibility rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar teeth visibility rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar teeth visibility rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEETH_VISIBILITY_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEETH_VISIBILITY_RULE_PROMPT_EFF
- Fallback: Reforzar teeth visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0555 — wrong_face_blocker_prompt_effect
- Definición: Campo operativo para wrong face blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong face blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong face blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_FACE_BLOCKER_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_FACE_BLOCKER_PROMPT_EFFECT
- Fallback: Reforzar wrong face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0556 — same_face_blocker_prompt_effect
- Definición: Campo operativo para same face blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar same face blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar same face blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SAME_FACE_BLOCKER_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SAME_FACE_BLOCKER_PROMPT_EFFECT
- Fallback: Reforzar same face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0557 — generic_beauty_blocker_prompt_effect
- Definición: Campo operativo para generic beauty blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic beauty blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic beauty blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_BEAUTY_BLOCKER_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_BEAUTY_BLOCKER_PROMPT_EF
- Fallback: Reforzar generic beauty blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0558 — over_symmetry_blocker_prompt_effect
- Definición: Campo operativo para over symmetry blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar over symmetry blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar over symmetry blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OVER_SYMMETRY_BLOCKER_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OVER_SYMMETRY_BLOCKER_PROMPT_EFF
- Fallback: Reforzar over symmetry blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_0559 — makeup_face_drift_rule_prompt_effect
- Definición: Campo operativo para makeup face drift rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar makeup face drift rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar makeup face drift rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MAKEUP_FACE_DRIFT_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MAKEUP_FACE_DRIFT_RULE_PROMPT_EF
- Fallback: Reforzar makeup face drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0560 — lens_face_distortion_rule_prompt_effect
- Definición: Campo operativo para lens face distortion rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens face distortion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens face distortion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FACE_DISTORTION_RULE_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FACE_DISTORTION_RULE_PROMPT
- Fallback: Reforzar lens face distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0561 — anchor_face_match_rule_prompt_effect
- Definición: Campo operativo para anchor face match rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar anchor face match rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar anchor face match rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANCHOR_FACE_MATCH_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANCHOR_FACE_MATCH_RULE_PROMPT_EF
- Fallback: Reforzar anchor face match rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0562 — face_regression_test_prompt_effect
- Definición: Campo operativo para face regression test dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar face regression test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar face regression test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACE_REGRESSION_TEST_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACE_REGRESSION_TEST_PROMPT_EFFE
- Fallback: Reforzar face regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0956 — face_shape_qa_matrix
- Definición: Campo operativo para face shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar face shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar face shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACE_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACE_SHAPE_QA_MATRIX
- Fallback: Reforzar face shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0957 — cranial_visual_volume_qa_matrix
- Definición: Campo operativo para cranial visual volume dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cranial visual volume como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cranial visual volume como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CRANIAL_VISUAL_VOLUME_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CRANIAL_VISUAL_VOLUME_QA_MATRIX
- Fallback: Reforzar cranial visual volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0958 — vertical_thirds_qa_matrix
- Definición: Campo operativo para vertical thirds dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vertical thirds como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vertical thirds como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VERTICAL_THIRDS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VERTICAL_THIRDS_QA_MATRIX
- Fallback: Reforzar vertical thirds con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0959 — horizontal_fifths_qa_matrix
- Definición: Campo operativo para horizontal fifths dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar horizontal fifths como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar horizontal fifths como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HORIZONTAL_FIFTHS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HORIZONTAL_FIFTHS_QA_MATRIX
- Fallback: Reforzar horizontal fifths con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0960 — forehead_height_qa_matrix
- Definición: Campo operativo para forehead height dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar forehead height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar forehead height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOREHEAD_HEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOREHEAD_HEIGHT_QA_MATRIX
- Fallback: Reforzar forehead height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_HAIR_0961 — hairline_relation_qa_matrix
- Definición: Campo operativo para hairline relation dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hairline relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hairline relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIRLINE_RELATION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIRLINE_RELATION_QA_MATRIX
- Fallback: Reforzar hairline relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0962 — temple_width_qa_matrix
- Definición: Campo operativo para temple width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar temple width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar temple width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEMPLE_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEMPLE_WIDTH_QA_MATRIX
- Fallback: Reforzar temple width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0963 — cheekbone_position_qa_matrix
- Definición: Campo operativo para cheekbone position dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cheekbone position como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cheekbone position como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHEEKBONE_POSITION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHEEKBONE_POSITION_QA_MATRIX
- Fallback: Reforzar cheekbone position con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0964 — midface_length_qa_matrix
- Definición: Campo operativo para midface length dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar midface length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar midface length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIDFACE_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIDFACE_LENGTH_QA_MATRIX
- Fallback: Reforzar midface length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0965 — lower_face_ratio_qa_matrix
- Definición: Campo operativo para lower face ratio dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower face ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower face ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_FACE_RATIO_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_FACE_RATIO_QA_MATRIX
- Fallback: Reforzar lower face ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0966 — jaw_angle_qa_matrix
- Definición: Campo operativo para jaw angle dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw angle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw angle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_ANGLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_ANGLE_QA_MATRIX
- Fallback: Reforzar jaw angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0967 — jaw_softness_qa_matrix
- Definición: Campo operativo para jaw softness dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw softness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw softness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_SOFTNESS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_SOFTNESS_QA_MATRIX
- Fallback: Reforzar jaw softness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0968 — chin_projection_qa_matrix
- Definición: Campo operativo para chin projection dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chin projection como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chin projection como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHIN_PROJECTION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHIN_PROJECTION_QA_MATRIX
- Fallback: Reforzar chin projection con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0969 — chin_width_qa_matrix
- Definición: Campo operativo para chin width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chin width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chin width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHIN_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHIN_WIDTH_QA_MATRIX
- Fallback: Reforzar chin width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0970 — facial_asymmetry_map_qa_matrix
- Definición: Campo operativo para facial asymmetry map dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar facial asymmetry map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar facial asymmetry map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACIAL_ASYMMETRY_MAP_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACIAL_ASYMMETRY_MAP_QA_MATRIX
- Fallback: Reforzar facial asymmetry map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0971 — age_face_signature_qa_matrix
- Definición: Campo operativo para age face signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar age face signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar age face signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AGE_FACE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AGE_FACE_SIGNATURE_QA_MATRIX
- Fallback: Reforzar age face signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0972 — eye_shape_qa_matrix
- Definición: Campo operativo para eye shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SHAPE_QA_MATRIX
- Fallback: Reforzar eye shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0973 — eye_size_qa_matrix
- Definición: Campo operativo para eye size dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye size como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye size como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SIZE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SIZE_QA_MATRIX
- Fallback: Reforzar eye size con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0974 — eye_spacing_qa_matrix
- Definición: Campo operativo para eye spacing dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye spacing como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye spacing como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SPACING_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SPACING_QA_MATRIX
- Fallback: Reforzar eye spacing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0975 — eye_tilt_qa_matrix
- Definición: Campo operativo para eye tilt dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye tilt como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye tilt como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_TILT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_TILT_QA_MATRIX
- Fallback: Reforzar eye tilt con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0976 — eyelid_fold_qa_matrix
- Definición: Campo operativo para eyelid fold dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eyelid fold como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eyelid fold como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYELID_FOLD_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYELID_FOLD_QA_MATRIX
- Fallback: Reforzar eyelid fold con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0977 — upper_lid_weight_qa_matrix
- Definición: Campo operativo para upper lid weight dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar upper lid weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar upper lid weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UPPER_LID_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UPPER_LID_WEIGHT_QA_MATRIX
- Fallback: Reforzar upper lid weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0978 — lower_lid_tension_qa_matrix
- Definición: Campo operativo para lower lid tension dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower lid tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower lid tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_LID_TENSION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_LID_TENSION_QA_MATRIX
- Fallback: Reforzar lower lid tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0979 — iris_color_qa_matrix
- Definición: Campo operativo para iris color dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iris color como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iris color como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IRIS_COLOR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IRIS_COLOR_QA_MATRIX
- Fallback: Reforzar iris color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0980 — iris_signature_qa_matrix
- Definición: Campo operativo para iris signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iris signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iris signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IRIS_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IRIS_SIGNATURE_QA_MATRIX
- Fallback: Reforzar iris signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0981 — catchlight_rule_qa_matrix
- Definición: Campo operativo para catchlight rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar catchlight rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar catchlight rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CATCHLIGHT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CATCHLIGHT_RULE_QA_MATRIX
- Fallback: Reforzar catchlight rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0982 — gaze_signature_qa_matrix
- Definición: Campo operativo para gaze signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar gaze signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar gaze signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GAZE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GAZE_SIGNATURE_QA_MATRIX
- Fallback: Reforzar gaze signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0983 — blink_pattern_qa_matrix
- Definición: Campo operativo para blink pattern dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar blink pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar blink pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BLINK_PATTERN_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BLINK_PATTERN_QA_MATRIX
- Fallback: Reforzar blink pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0984 — eye_emotion_map_qa_matrix
- Definición: Campo operativo para eye emotion map dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye emotion map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye emotion map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_EMOTION_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_EMOTION_MAP_QA_MATRIX
- Fallback: Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0985 — under_eye_texture_qa_matrix
- Definición: Campo operativo para under eye texture dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar under eye texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar under eye texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UNDER_EYE_TEXTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UNDER_EYE_TEXTURE_QA_MATRIX
- Fallback: Reforzar under eye texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_0986 — sclera_natural_variation_qa_matrix
- Definición: Campo operativo para sclera natural variation dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sclera natural variation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sclera natural variation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCLERA_NATURAL_VARIATION_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCLERA_NATURAL_VARIATION_QA_MATR
- Fallback: Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0987 — brow_density_qa_matrix
- Definición: Campo operativo para brow density dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_DENSITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_DENSITY_QA_MATRIX
- Fallback: Reforzar brow density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0988 — brow_arc_qa_matrix
- Definición: Campo operativo para brow arc dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow arc como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow arc como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_ARC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_ARC_QA_MATRIX
- Fallback: Reforzar brow arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0989 — brow_height_qa_matrix
- Definición: Campo operativo para brow height dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_HEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_HEIGHT_QA_MATRIX
- Fallback: Reforzar brow height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0990 — brow_eye_distance_qa_matrix
- Definición: Campo operativo para brow eye distance dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow eye distance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow eye distance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_EYE_DISTANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_EYE_DISTANCE_QA_MATRIX
- Fallback: Reforzar brow eye distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0991 — nose_bridge_qa_matrix
- Definición: Campo operativo para nose bridge dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose bridge como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose bridge como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_BRIDGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_BRIDGE_QA_MATRIX
- Fallback: Reforzar nose bridge con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0992 — nose_dorsum_qa_matrix
- Definición: Campo operativo para nose dorsum dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose dorsum como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose dorsum como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_DORSUM_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_DORSUM_QA_MATRIX
- Fallback: Reforzar nose dorsum con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0993 — nose_tip_qa_matrix
- Definición: Campo operativo para nose tip dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose tip como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose tip como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_TIP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_TIP_QA_MATRIX
- Fallback: Reforzar nose tip con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0994 — nostril_width_qa_matrix
- Definición: Campo operativo para nostril width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nostril width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nostril width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSTRIL_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSTRIL_WIDTH_QA_MATRIX
- Fallback: Reforzar nostril width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0995 — alar_shape_qa_matrix
- Definición: Campo operativo para alar shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar alar shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar alar shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ALAR_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ALAR_SHAPE_QA_MATRIX
- Fallback: Reforzar alar shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0996 — philtrum_length_qa_matrix
- Definición: Campo operativo para philtrum length dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar philtrum length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar philtrum length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PHILTRUM_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PHILTRUM_LENGTH_QA_MATRIX
- Fallback: Reforzar philtrum length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0997 — lip_ratio_qa_matrix
- Definición: Campo operativo para lip ratio dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_RATIO_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_RATIO_QA_MATRIX
- Fallback: Reforzar lip ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0998 — upper_lip_shape_qa_matrix
- Definición: Campo operativo para upper lip shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar upper lip shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar upper lip shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UPPER_LIP_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UPPER_LIP_SHAPE_QA_MATRIX
- Fallback: Reforzar upper lip shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0999 — lower_lip_volume_qa_matrix
- Definición: Campo operativo para lower lip volume dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower lip volume como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower lip volume como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_LIP_VOLUME_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_LIP_VOLUME_QA_MATRIX
- Fallback: Reforzar lower lip volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1000 — cupid_bow_qa_matrix
- Definición: Campo operativo para cupid bow dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cupid bow como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cupid bow como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CUPID_BOW_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CUPID_BOW_QA_MATRIX
- Fallback: Reforzar cupid bow con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1001 — mouth_width_qa_matrix
- Definición: Campo operativo para mouth width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mouth width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mouth width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOUTH_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOUTH_WIDTH_QA_MATRIX
- Fallback: Reforzar mouth width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1002 — smile_signature_qa_matrix
- Definición: Campo operativo para smile signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar smile signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar smile signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SMILE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SMILE_SIGNATURE_QA_MATRIX
- Fallback: Reforzar smile signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1003 — teeth_visibility_rule_qa_matrix
- Definición: Campo operativo para teeth visibility rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar teeth visibility rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar teeth visibility rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEETH_VISIBILITY_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEETH_VISIBILITY_RULE_QA_MATRIX
- Fallback: Reforzar teeth visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1004 — wrong_face_blocker_qa_matrix
- Definición: Campo operativo para wrong face blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong face blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong face blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_FACE_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_FACE_BLOCKER_QA_MATRIX
- Fallback: Reforzar wrong face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1005 — same_face_blocker_qa_matrix
- Definición: Campo operativo para same face blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar same face blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar same face blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SAME_FACE_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SAME_FACE_BLOCKER_QA_MATRIX
- Fallback: Reforzar same face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1006 — generic_beauty_blocker_qa_matrix
- Definición: Campo operativo para generic beauty blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic beauty blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic beauty blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_BEAUTY_BLOCKER_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_BEAUTY_BLOCKER_QA_MATRIX
- Fallback: Reforzar generic beauty blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1007 — over_symmetry_blocker_qa_matrix
- Definición: Campo operativo para over symmetry blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar over symmetry blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar over symmetry blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OVER_SYMMETRY_BLOCKER_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OVER_SYMMETRY_BLOCKER_QA_MATRIX
- Fallback: Reforzar over symmetry blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1008 — makeup_face_drift_rule_qa_matrix
- Definición: Campo operativo para makeup face drift rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar makeup face drift rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar makeup face drift rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MAKEUP_FACE_DRIFT_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MAKEUP_FACE_DRIFT_RULE_QA_MATRIX
- Fallback: Reforzar makeup face drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1009 — lens_face_distortion_rule_qa_matrix
- Definición: Campo operativo para lens face distortion rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens face distortion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens face distortion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FACE_DISTORTION_RULE_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FACE_DISTORTION_RULE_QA_MAT
- Fallback: Reforzar lens face distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1010 — anchor_face_match_rule_qa_matrix
- Definición: Campo operativo para anchor face match rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar anchor face match rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar anchor face match rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANCHOR_FACE_MATCH_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANCHOR_FACE_MATCH_RULE_QA_MATRIX
- Fallback: Reforzar anchor face match rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1011 — face_regression_test_qa_matrix
- Definición: Campo operativo para face regression test dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar face regression test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar face regression test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACE_REGRESSION_TEST_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACE_REGRESSION_TEST_QA_MATRIX
- Fallback: Reforzar face regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1405 — face_shape_vendor_repair
- Definición: Campo operativo para face shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar face shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar face shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACE_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACE_SHAPE_VENDOR_REPAIR
- Fallback: Reforzar face shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1406 — cranial_visual_volume_vendor_repair
- Definición: Campo operativo para cranial visual volume dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cranial visual volume como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cranial visual volume como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CRANIAL_VISUAL_VOLUME_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CRANIAL_VISUAL_VOLUME_VENDOR_REP
- Fallback: Reforzar cranial visual volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1407 — vertical_thirds_vendor_repair
- Definición: Campo operativo para vertical thirds dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar vertical thirds como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar vertical thirds como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VERTICAL_THIRDS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VERTICAL_THIRDS_VENDOR_REPAIR
- Fallback: Reforzar vertical thirds con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1408 — horizontal_fifths_vendor_repair
- Definición: Campo operativo para horizontal fifths dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar horizontal fifths como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar horizontal fifths como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HORIZONTAL_FIFTHS_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HORIZONTAL_FIFTHS_VENDOR_REPAIR
- Fallback: Reforzar horizontal fifths con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1409 — forehead_height_vendor_repair
- Definición: Campo operativo para forehead height dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar forehead height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar forehead height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOREHEAD_HEIGHT_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOREHEAD_HEIGHT_VENDOR_REPAIR
- Fallback: Reforzar forehead height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_HAIR_1410 — hairline_relation_vendor_repair
- Definición: Campo operativo para hairline relation dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hairline relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hairline relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIRLINE_RELATION_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIRLINE_RELATION_VENDOR_REPAIR
- Fallback: Reforzar hairline relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1411 — temple_width_vendor_repair
- Definición: Campo operativo para temple width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar temple width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar temple width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEMPLE_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEMPLE_WIDTH_VENDOR_REPAIR
- Fallback: Reforzar temple width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1412 — cheekbone_position_vendor_repair
- Definición: Campo operativo para cheekbone position dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cheekbone position como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cheekbone position como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHEEKBONE_POSITION_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHEEKBONE_POSITION_VENDOR_REPAIR
- Fallback: Reforzar cheekbone position con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1413 — midface_length_vendor_repair
- Definición: Campo operativo para midface length dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar midface length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar midface length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MIDFACE_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MIDFACE_LENGTH_VENDOR_REPAIR
- Fallback: Reforzar midface length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1414 — lower_face_ratio_vendor_repair
- Definición: Campo operativo para lower face ratio dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower face ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower face ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_FACE_RATIO_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_FACE_RATIO_VENDOR_REPAIR
- Fallback: Reforzar lower face ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1415 — jaw_angle_vendor_repair
- Definición: Campo operativo para jaw angle dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw angle como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw angle como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_ANGLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_ANGLE_VENDOR_REPAIR
- Fallback: Reforzar jaw angle con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1416 — jaw_softness_vendor_repair
- Definición: Campo operativo para jaw softness dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw softness como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw softness como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_SOFTNESS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_SOFTNESS_VENDOR_REPAIR
- Fallback: Reforzar jaw softness con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1417 — chin_projection_vendor_repair
- Definición: Campo operativo para chin projection dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chin projection como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chin projection como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHIN_PROJECTION_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHIN_PROJECTION_VENDOR_REPAIR
- Fallback: Reforzar chin projection con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1418 — chin_width_vendor_repair
- Definición: Campo operativo para chin width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar chin width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar chin width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CHIN_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CHIN_WIDTH_VENDOR_REPAIR
- Fallback: Reforzar chin width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1419 — facial_asymmetry_map_vendor_repair
- Definición: Campo operativo para facial asymmetry map dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar facial asymmetry map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar facial asymmetry map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACIAL_ASYMMETRY_MAP_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACIAL_ASYMMETRY_MAP_VENDOR_REPA
- Fallback: Reforzar facial asymmetry map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1420 — age_face_signature_vendor_repair
- Definición: Campo operativo para age face signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar age face signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar age face signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_AGE_FACE_SIGNATURE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_AGE_FACE_SIGNATURE_VENDOR_REPAIR
- Fallback: Reforzar age face signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1421 — eye_shape_vendor_repair
- Definición: Campo operativo para eye shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SHAPE_VENDOR_REPAIR
- Fallback: Reforzar eye shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1422 — eye_size_vendor_repair
- Definición: Campo operativo para eye size dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye size como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye size como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SIZE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SIZE_VENDOR_REPAIR
- Fallback: Reforzar eye size con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1423 — eye_spacing_vendor_repair
- Definición: Campo operativo para eye spacing dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye spacing como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye spacing como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_SPACING_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_SPACING_VENDOR_REPAIR
- Fallback: Reforzar eye spacing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1424 — eye_tilt_vendor_repair
- Definición: Campo operativo para eye tilt dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye tilt como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye tilt como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_TILT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_TILT_VENDOR_REPAIR
- Fallback: Reforzar eye tilt con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1425 — eyelid_fold_vendor_repair
- Definición: Campo operativo para eyelid fold dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eyelid fold como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eyelid fold como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYELID_FOLD_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYELID_FOLD_VENDOR_REPAIR
- Fallback: Reforzar eyelid fold con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1426 — upper_lid_weight_vendor_repair
- Definición: Campo operativo para upper lid weight dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar upper lid weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar upper lid weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UPPER_LID_WEIGHT_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UPPER_LID_WEIGHT_VENDOR_REPAIR
- Fallback: Reforzar upper lid weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1427 — lower_lid_tension_vendor_repair
- Definición: Campo operativo para lower lid tension dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower lid tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower lid tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_LID_TENSION_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_LID_TENSION_VENDOR_REPAIR
- Fallback: Reforzar lower lid tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1428 — iris_color_vendor_repair
- Definición: Campo operativo para iris color dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iris color como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iris color como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IRIS_COLOR_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IRIS_COLOR_VENDOR_REPAIR
- Fallback: Reforzar iris color con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1429 — iris_signature_vendor_repair
- Definición: Campo operativo para iris signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar iris signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar iris signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IRIS_SIGNATURE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IRIS_SIGNATURE_VENDOR_REPAIR
- Fallback: Reforzar iris signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_1430 — catchlight_rule_vendor_repair
- Definición: Campo operativo para catchlight rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar catchlight rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar catchlight rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CATCHLIGHT_RULE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CATCHLIGHT_RULE_VENDOR_REPAIR
- Fallback: Reforzar catchlight rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1431 — gaze_signature_vendor_repair
- Definición: Campo operativo para gaze signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar gaze signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar gaze signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GAZE_SIGNATURE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GAZE_SIGNATURE_VENDOR_REPAIR
- Fallback: Reforzar gaze signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1432 — blink_pattern_vendor_repair
- Definición: Campo operativo para blink pattern dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar blink pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar blink pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BLINK_PATTERN_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BLINK_PATTERN_VENDOR_REPAIR
- Fallback: Reforzar blink pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1433 — eye_emotion_map_vendor_repair
- Definición: Campo operativo para eye emotion map dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye emotion map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye emotion map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_EMOTION_MAP_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_EMOTION_MAP_VENDOR_REPAIR
- Fallback: Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1434 — under_eye_texture_vendor_repair
- Definición: Campo operativo para under eye texture dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar under eye texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar under eye texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UNDER_EYE_TEXTURE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UNDER_EYE_TEXTURE_VENDOR_REPAIR
- Fallback: Reforzar under eye texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1435 — sclera_natural_variation_vendor_repair
- Definición: Campo operativo para sclera natural variation dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sclera natural variation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sclera natural variation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SCLERA_NATURAL_VARIATION_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SCLERA_NATURAL_VARIATION_VENDOR_
- Fallback: Reforzar sclera natural variation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1436 — brow_density_vendor_repair
- Definición: Campo operativo para brow density dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow density como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow density como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_DENSITY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_DENSITY_VENDOR_REPAIR
- Fallback: Reforzar brow density con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1437 — brow_arc_vendor_repair
- Definición: Campo operativo para brow arc dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow arc como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow arc como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_ARC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_ARC_VENDOR_REPAIR
- Fallback: Reforzar brow arc con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1438 — brow_height_vendor_repair
- Definición: Campo operativo para brow height dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow height como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow height como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_HEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_HEIGHT_VENDOR_REPAIR
- Fallback: Reforzar brow height con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1439 — brow_eye_distance_vendor_repair
- Definición: Campo operativo para brow eye distance dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow eye distance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow eye distance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_EYE_DISTANCE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_EYE_DISTANCE_VENDOR_REPAIR
- Fallback: Reforzar brow eye distance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1440 — nose_bridge_vendor_repair
- Definición: Campo operativo para nose bridge dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose bridge como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose bridge como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_BRIDGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_BRIDGE_VENDOR_REPAIR
- Fallback: Reforzar nose bridge con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1441 — nose_dorsum_vendor_repair
- Definición: Campo operativo para nose dorsum dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose dorsum como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose dorsum como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_DORSUM_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_DORSUM_VENDOR_REPAIR
- Fallback: Reforzar nose dorsum con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1442 — nose_tip_vendor_repair
- Definición: Campo operativo para nose tip dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nose tip como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nose tip como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSE_TIP_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSE_TIP_VENDOR_REPAIR
- Fallback: Reforzar nose tip con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1443 — nostril_width_vendor_repair
- Definición: Campo operativo para nostril width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nostril width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nostril width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NOSTRIL_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NOSTRIL_WIDTH_VENDOR_REPAIR
- Fallback: Reforzar nostril width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1444 — alar_shape_vendor_repair
- Definición: Campo operativo para alar shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar alar shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar alar shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ALAR_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ALAR_SHAPE_VENDOR_REPAIR
- Fallback: Reforzar alar shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1445 — philtrum_length_vendor_repair
- Definición: Campo operativo para philtrum length dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar philtrum length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar philtrum length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PHILTRUM_LENGTH_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PHILTRUM_LENGTH_VENDOR_REPAIR
- Fallback: Reforzar philtrum length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1446 — lip_ratio_vendor_repair
- Definición: Campo operativo para lip ratio dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lip ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lip ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LIP_RATIO_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LIP_RATIO_VENDOR_REPAIR
- Fallback: Reforzar lip ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1447 — upper_lip_shape_vendor_repair
- Definición: Campo operativo para upper lip shape dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar upper lip shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar upper lip shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UPPER_LIP_SHAPE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UPPER_LIP_SHAPE_VENDOR_REPAIR
- Fallback: Reforzar upper lip shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1448 — lower_lip_volume_vendor_repair
- Definición: Campo operativo para lower lip volume dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lower lip volume como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lower lip volume como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LOWER_LIP_VOLUME_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LOWER_LIP_VOLUME_VENDOR_REPAIR
- Fallback: Reforzar lower lip volume con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1449 — cupid_bow_vendor_repair
- Definición: Campo operativo para cupid bow dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar cupid bow como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar cupid bow como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CUPID_BOW_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CUPID_BOW_VENDOR_REPAIR
- Fallback: Reforzar cupid bow con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1450 — mouth_width_vendor_repair
- Definición: Campo operativo para mouth width dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mouth width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mouth width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOUTH_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOUTH_WIDTH_VENDOR_REPAIR
- Fallback: Reforzar mouth width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1451 — smile_signature_vendor_repair
- Definición: Campo operativo para smile signature dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar smile signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar smile signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SMILE_SIGNATURE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SMILE_SIGNATURE_VENDOR_REPAIR
- Fallback: Reforzar smile signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1452 — teeth_visibility_rule_vendor_repair
- Definición: Campo operativo para teeth visibility rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar teeth visibility rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar teeth visibility rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEETH_VISIBILITY_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEETH_VISIBILITY_RULE_VENDOR_REP
- Fallback: Reforzar teeth visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1453 — wrong_face_blocker_vendor_repair
- Definición: Campo operativo para wrong face blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong face blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong face blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_FACE_BLOCKER_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_FACE_BLOCKER_VENDOR_REPAIR
- Fallback: Reforzar wrong face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1454 — same_face_blocker_vendor_repair
- Definición: Campo operativo para same face blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar same face blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar same face blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SAME_FACE_BLOCKER_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SAME_FACE_BLOCKER_VENDOR_REPAIR
- Fallback: Reforzar same face blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1455 — generic_beauty_blocker_vendor_repair
- Definición: Campo operativo para generic beauty blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar generic beauty blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar generic beauty blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_GENERIC_BEAUTY_BLOCKER_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_GENERIC_BEAUTY_BLOCKER_VENDOR_RE
- Fallback: Reforzar generic beauty blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1456 — over_symmetry_blocker_vendor_repair
- Definición: Campo operativo para over symmetry blocker dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar over symmetry blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar over symmetry blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OVER_SYMMETRY_BLOCKER_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OVER_SYMMETRY_BLOCKER_VENDOR_REP
- Fallback: Reforzar over symmetry blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SKIN_1457 — makeup_face_drift_rule_vendor_repair
- Definición: Campo operativo para makeup face drift rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar makeup face drift rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar makeup face drift rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MAKEUP_FACE_DRIFT_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MAKEUP_FACE_DRIFT_RULE_VENDOR_RE
- Fallback: Reforzar makeup face drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1458 — lens_face_distortion_rule_vendor_repair
- Definición: Campo operativo para lens face distortion rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lens face distortion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lens face distortion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LENS_FACE_DISTORTION_RULE_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LENS_FACE_DISTORTION_RULE_VENDOR
- Fallback: Reforzar lens face distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1459 — anchor_face_match_rule_vendor_repair
- Definición: Campo operativo para anchor face match rule dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar anchor face match rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar anchor face match rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANCHOR_FACE_MATCH_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANCHOR_FACE_MATCH_RULE_VENDOR_RE
- Fallback: Reforzar anchor face match rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_FACE_1460 — face_regression_test_vendor_repair
- Definición: Campo operativo para face regression test dentro de Rostro forense, landmarks, edad visual y autenticación de identidad. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar face regression test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar face regression test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACE_REGRESSION_TEST_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACE_REGRESSION_TEST_VENDOR_REPA
- Fallback: Reforzar face regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
