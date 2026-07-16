## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_BODY_0114` | `height_range` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HEIGHT_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar height range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0115` | `body_build` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_BUILD_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar body build con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0116` | `visual_mass` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VISUAL_MASS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar visual mass con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0117` | `shoulder_width` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shoulder width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0118` | `neck_length` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NECK_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar neck length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0119` | `clavicle_visibility` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLAVICLE_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar clavicle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0120` | `torso_length` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TORSO_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar torso length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0121` | `torso_leg_ratio` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TORSO_LEG_RATIO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar torso leg ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0122` | `waist_hip_relation` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WAIST_HIP_RELATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar waist hip relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0123` | `pelvis_width` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PELVIS_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar pelvis width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0124` | `arm_length` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARM_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar arm length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0125` | `forearm_shape` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOREARM_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar forearm shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0126` | `wrist_scale` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRIST_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wrist scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0127` | `leg_line` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LEG_LINE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar leg line con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0128` | `knee_visibility` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KNEE_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar knee visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0129` | `ankle_scale` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANKLE_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar ankle scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0130` | `foot_scale` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOOT_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar foot scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0131` | `body_age_signature` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_AGE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar body age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0132` | `hand_shape` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hand shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0133` | `finger_length` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINGER_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar finger length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0134` | `finger_taper` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINGER_TAPER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar finger taper con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0135` | `knuckle_visibility` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KNUCKLE_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar knuckle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0136` | `nail_style` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NAIL_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar nail style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0137` | `hand_gesture_rest` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_GESTURE_REST_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hand gesture rest con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PROPS_0138` | `hand_object_contact` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_OBJECT_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0139` | `feet_ground_contact` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FEET_GROUND_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar feet ground contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0140` | `toe_visibility_rule` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TOE_VISIBILITY_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar toe visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0141` | `shoe_fit_rule` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOE_FIT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shoe fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0142` | `hands_age_signature` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_AGE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hands age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0143` | `contact_pressure_rule` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTACT_PRESSURE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar contact pressure rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0144` | `center_of_gravity` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CENTER_OF_GRAVITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar center of gravity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0145` | `posture_base` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSTURE_BASE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar posture base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0146` | `spine_curve` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPINE_CURVE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar spine curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0147` | `shoulder_behavior` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_BEHAVIOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shoulder behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0148` | `hip_alignment` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HIP_ALIGNMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hip alignment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0149` | `weight_distribution` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WEIGHT_DISTRIBUTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar weight distribution con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0150` | `standing_balance` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STANDING_BALANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar standing balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0151` | `sitting_balance` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SITTING_BALANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar sitting balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0152` | `walking_weight` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0153` | `dance_range` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DANCE_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar dance range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0154` | `fitness_tone` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FITNESS_TONE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fitness tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0155` | `body_energy_signature` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_ENERGY_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar body energy signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0156` | `same_body_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SAME_BODY_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar same body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0157` | `wrong_age_body_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_AGE_BODY_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wrong age body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0158` | `impossible_pose_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMPOSSIBLE_POSE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar impossible pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0159` | `body_lens_distortion_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_LENS_DISTORTION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar body lens distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PROPS_0160` | `proportion_repair_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROPORTION_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar proportion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0161` | `hands_feet_repair_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_FEET_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hands feet repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0162` | `adult_body_safety_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_BODY_SAFETY_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar adult body safety rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0563` | `height_range_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HEIGHT_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar height range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0564` | `body_build_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_BUILD_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body build con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0565` | `visual_mass_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VISUAL_MASS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar visual mass con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0566` | `shoulder_width_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0567` | `neck_length_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NECK_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar neck length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0568` | `clavicle_visibility_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLAVICLE_VISIBILITY_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clavicle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0569` | `torso_length_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TORSO_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar torso length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0570` | `torso_leg_ratio_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TORSO_LEG_RATIO_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar torso leg ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0571` | `waist_hip_relation_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WAIST_HIP_RELATION_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar waist hip relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0572` | `pelvis_width_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PELVIS_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pelvis width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0573` | `arm_length_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARM_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar arm length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0574` | `forearm_shape_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOREARM_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar forearm shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0575` | `wrist_scale_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRIST_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrist scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0576` | `leg_line_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LEG_LINE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar leg line con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0577` | `knee_visibility_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KNEE_VISIBILITY_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar knee visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0578` | `ankle_scale_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANKLE_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ankle scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0579` | `foot_scale_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOOT_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar foot scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0580` | `body_age_signature_prompt_effect` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_AGE_SIGNATURE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0581` | `hand_shape_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0582` | `finger_length_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINGER_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar finger length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0583` | `finger_taper_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINGER_TAPER_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar finger taper con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0584` | `knuckle_visibility_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KNUCKLE_VISIBILITY_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar knuckle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0585` | `nail_style_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NAIL_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nail style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0586` | `hand_gesture_rest_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_GESTURE_REST_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand gesture rest con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PROPS_0587` | `hand_object_contact_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_OBJECT_CONTACT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0588` | `feet_ground_contact_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FEET_GROUND_CONTACT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar feet ground contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0589` | `toe_visibility_rule_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TOE_VISIBILITY_RULE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar toe visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0590` | `shoe_fit_rule_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOE_FIT_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoe fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0591` | `hands_age_signature_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_AGE_SIGNATURE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0592` | `contact_pressure_rule_prompt_effect` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTACT_PRESSURE_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contact pressure rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0593` | `center_of_gravity_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CENTER_OF_GRAVITY_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar center of gravity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0594` | `posture_base_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSTURE_BASE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar posture base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0595` | `spine_curve_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPINE_CURVE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar spine curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0596` | `shoulder_behavior_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_BEHAVIOR_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0597` | `hip_alignment_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HIP_ALIGNMENT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hip alignment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0598` | `weight_distribution_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WEIGHT_DISTRIBUTION_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar weight distribution con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0599` | `standing_balance_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STANDING_BALANCE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar standing balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0600` | `sitting_balance_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SITTING_BALANCE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sitting balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0601` | `walking_weight_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_WEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0602` | `dance_range_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DANCE_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dance range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0603` | `fitness_tone_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FITNESS_TONE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fitness tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0604` | `body_energy_signature_prompt_effect` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_ENERGY_SIGNATURE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body energy signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0605` | `same_body_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SAME_BODY_BLOCKER_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar same body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0606` | `wrong_age_body_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_AGE_BODY_BLOCKER_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong age body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0607` | `impossible_pose_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMPOSSIBLE_POSE_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar impossible pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0608` | `body_lens_distortion_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_LENS_DISTORTION_RULE_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body lens distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PROPS_0609` | `proportion_repair_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROPORTION_REPAIR_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar proportion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0610` | `hands_feet_repair_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_FEET_REPAIR_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands feet repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_0611` | `adult_body_safety_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_BODY_SAFETY_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult body safety rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1012` | `height_range_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HEIGHT_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar height range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1013` | `body_build_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_BUILD_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body build con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1014` | `visual_mass_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VISUAL_MASS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar visual mass con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1015` | `shoulder_width_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1016` | `neck_length_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NECK_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar neck length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1017` | `clavicle_visibility_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLAVICLE_VISIBILITY_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clavicle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1018` | `torso_length_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TORSO_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar torso length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1019` | `torso_leg_ratio_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TORSO_LEG_RATIO_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar torso leg ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1020` | `waist_hip_relation_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WAIST_HIP_RELATION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar waist hip relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1021` | `pelvis_width_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PELVIS_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pelvis width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1022` | `arm_length_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARM_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar arm length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1023` | `forearm_shape_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOREARM_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar forearm shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1024` | `wrist_scale_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRIST_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrist scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1025` | `leg_line_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LEG_LINE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar leg line con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1026` | `knee_visibility_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KNEE_VISIBILITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar knee visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1027` | `ankle_scale_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANKLE_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ankle scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1028` | `foot_scale_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOOT_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar foot scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1029` | `body_age_signature_qa_matrix` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_AGE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1030` | `hand_shape_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1031` | `finger_length_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINGER_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar finger length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1032` | `finger_taper_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINGER_TAPER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar finger taper con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1033` | `knuckle_visibility_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KNUCKLE_VISIBILITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar knuckle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1034` | `nail_style_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NAIL_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nail style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1035` | `hand_gesture_rest_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_GESTURE_REST_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand gesture rest con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PROPS_1036` | `hand_object_contact_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_OBJECT_CONTACT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1037` | `feet_ground_contact_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FEET_GROUND_CONTACT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar feet ground contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1038` | `toe_visibility_rule_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TOE_VISIBILITY_RULE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar toe visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1039` | `shoe_fit_rule_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOE_FIT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoe fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1040` | `hands_age_signature_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_AGE_SIGNATURE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1041` | `contact_pressure_rule_qa_matrix` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTACT_PRESSURE_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contact pressure rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1042` | `center_of_gravity_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CENTER_OF_GRAVITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar center of gravity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1043` | `posture_base_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSTURE_BASE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar posture base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1044` | `spine_curve_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPINE_CURVE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar spine curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1045` | `shoulder_behavior_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_BEHAVIOR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1046` | `hip_alignment_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HIP_ALIGNMENT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hip alignment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1047` | `weight_distribution_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WEIGHT_DISTRIBUTION_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar weight distribution con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1048` | `standing_balance_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STANDING_BALANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar standing balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1049` | `sitting_balance_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SITTING_BALANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sitting balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1050` | `walking_weight_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1051` | `dance_range_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DANCE_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dance range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1052` | `fitness_tone_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FITNESS_TONE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fitness tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1053` | `body_energy_signature_qa_matrix` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_ENERGY_SIGNATURE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body energy signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1054` | `same_body_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SAME_BODY_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar same body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1055` | `wrong_age_body_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_AGE_BODY_BLOCKER_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong age body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1056` | `impossible_pose_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMPOSSIBLE_POSE_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar impossible pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1057` | `body_lens_distortion_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_LENS_DISTORTION_RULE_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body lens distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PROPS_1058` | `proportion_repair_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROPORTION_REPAIR_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar proportion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1059` | `hands_feet_repair_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_FEET_REPAIR_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands feet repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1060` | `adult_body_safety_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_BODY_SAFETY_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult body safety rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1461` | `height_range_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HEIGHT_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar height range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1462` | `body_build_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_BUILD_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body build con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1463` | `visual_mass_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VISUAL_MASS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar visual mass con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1464` | `shoulder_width_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1465` | `neck_length_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NECK_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar neck length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1466` | `clavicle_visibility_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLAVICLE_VISIBILITY_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clavicle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1467` | `torso_length_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TORSO_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar torso length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1468` | `torso_leg_ratio_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TORSO_LEG_RATIO_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar torso leg ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1469` | `waist_hip_relation_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WAIST_HIP_RELATION_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar waist hip relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1470` | `pelvis_width_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PELVIS_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pelvis width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1471` | `arm_length_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARM_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar arm length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1472` | `forearm_shape_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOREARM_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar forearm shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1473` | `wrist_scale_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRIST_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrist scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1474` | `leg_line_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LEG_LINE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar leg line con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1475` | `knee_visibility_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KNEE_VISIBILITY_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar knee visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1476` | `ankle_scale_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ANKLE_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar ankle scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1477` | `foot_scale_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FOOT_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar foot scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1478` | `body_age_signature_vendor_repair` | structure | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_AGE_SIGNATURE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1479` | `hand_shape_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1480` | `finger_length_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINGER_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar finger length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1481` | `finger_taper_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FINGER_TAPER_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar finger taper con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1482` | `knuckle_visibility_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_KNUCKLE_VISIBILITY_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar knuckle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1483` | `nail_style_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NAIL_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar nail style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1484` | `hand_gesture_rest_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_GESTURE_REST_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand gesture rest con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PROPS_1485` | `hand_object_contact_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_OBJECT_CONTACT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1486` | `feet_ground_contact_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FEET_GROUND_CONTACT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar feet ground contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1487` | `toe_visibility_rule_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TOE_VISIBILITY_RULE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar toe visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1488` | `shoe_fit_rule_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOE_FIT_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoe fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1489` | `hands_age_signature_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_AGE_SIGNATURE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1490` | `contact_pressure_rule_vendor_repair` | hands_feet | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CONTACT_PRESSURE_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar contact pressure rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1491` | `center_of_gravity_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CENTER_OF_GRAVITY_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar center of gravity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1492` | `posture_base_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSTURE_BASE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar posture base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1493` | `spine_curve_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SPINE_CURVE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar spine curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1494` | `shoulder_behavior_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_BEHAVIOR_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1495` | `hip_alignment_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HIP_ALIGNMENT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hip alignment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1496` | `weight_distribution_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WEIGHT_DISTRIBUTION_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar weight distribution con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1497` | `standing_balance_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STANDING_BALANCE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar standing balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1498` | `sitting_balance_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SITTING_BALANCE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar sitting balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1499` | `walking_weight_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_WEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1500` | `dance_range_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DANCE_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dance range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1501` | `fitness_tone_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FITNESS_TONE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fitness tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1502` | `body_energy_signature_vendor_repair` | posture | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_ENERGY_SIGNATURE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body energy signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1503` | `same_body_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SAME_BODY_BLOCKER_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar same body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1504` | `wrong_age_body_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_AGE_BODY_BLOCKER_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong age body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1505` | `impossible_pose_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_IMPOSSIBLE_POSE_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar impossible pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1506` | `body_lens_distortion_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_LENS_DISTORTION_RULE_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body lens distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_PROPS_1507` | `proportion_repair_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROPORTION_REPAIR_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar proportion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1508` | `hands_feet_repair_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_FEET_REPAIR_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands feet repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_BODY_1509` | `adult_body_safety_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_BODY_SAFETY_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult body safety rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_BODY_0114 — height_range
- Definición: Campo operativo para height range dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar height range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar height range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HEIGHT_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HEIGHT_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar height range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0115 — body_build
- Definición: Campo operativo para body build dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar body build como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body build como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_BUILD_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BODY_BUILD_DRIFT_OR_GAP
- Fallback: Reforzar body build con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0116 — visual_mass
- Definición: Campo operativo para visual mass dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar visual mass como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar visual mass como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VISUAL_MASS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VISUAL_MASS_DRIFT_OR_GAP
- Fallback: Reforzar visual mass con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0117 — shoulder_width
- Definición: Campo operativo para shoulder width dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shoulder width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHOULDER_WIDTH_DRIFT_OR_GAP
- Fallback: Reforzar shoulder width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0118 — neck_length
- Definición: Campo operativo para neck length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar neck length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar neck length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NECK_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NECK_LENGTH_DRIFT_OR_GAP
- Fallback: Reforzar neck length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0119 — clavicle_visibility
- Definición: Campo operativo para clavicle visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar clavicle visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clavicle visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLAVICLE_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CLAVICLE_VISIBILITY_DRIFT_OR_GAP
- Fallback: Reforzar clavicle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0120 — torso_length
- Definición: Campo operativo para torso length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar torso length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar torso length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TORSO_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TORSO_LENGTH_DRIFT_OR_GAP
- Fallback: Reforzar torso length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0121 — torso_leg_ratio
- Definición: Campo operativo para torso leg ratio dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar torso leg ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar torso leg ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TORSO_LEG_RATIO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TORSO_LEG_RATIO_DRIFT_OR_GAP
- Fallback: Reforzar torso leg ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0122 — waist_hip_relation
- Definición: Campo operativo para waist hip relation dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar waist hip relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar waist hip relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WAIST_HIP_RELATION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WAIST_HIP_RELATION_DRIFT_OR_GAP
- Fallback: Reforzar waist hip relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0123 — pelvis_width
- Definición: Campo operativo para pelvis width dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar pelvis width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pelvis width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PELVIS_WIDTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PELVIS_WIDTH_DRIFT_OR_GAP
- Fallback: Reforzar pelvis width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0124 — arm_length
- Definición: Campo operativo para arm length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar arm length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar arm length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARM_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ARM_LENGTH_DRIFT_OR_GAP
- Fallback: Reforzar arm length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0125 — forearm_shape
- Definición: Campo operativo para forearm shape dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar forearm shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar forearm shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOREARM_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FOREARM_SHAPE_DRIFT_OR_GAP
- Fallback: Reforzar forearm shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0126 — wrist_scale
- Definición: Campo operativo para wrist scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wrist scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrist scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRIST_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WRIST_SCALE_DRIFT_OR_GAP
- Fallback: Reforzar wrist scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0127 — leg_line
- Definición: Campo operativo para leg line dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar leg line como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar leg line como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LEG_LINE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LEG_LINE_DRIFT_OR_GAP
- Fallback: Reforzar leg line con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0128 — knee_visibility
- Definición: Campo operativo para knee visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar knee visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar knee visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KNEE_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_KNEE_VISIBILITY_DRIFT_OR_GAP
- Fallback: Reforzar knee visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0129 — ankle_scale
- Definición: Campo operativo para ankle scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar ankle scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ankle scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANKLE_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ANKLE_SCALE_DRIFT_OR_GAP
- Fallback: Reforzar ankle scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0130 — foot_scale
- Definición: Campo operativo para foot scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar foot scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar foot scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOOT_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FOOT_SCALE_DRIFT_OR_GAP
- Fallback: Reforzar foot scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0131 — body_age_signature
- Definición: Campo operativo para body age signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar body age signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body age signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_AGE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BODY_AGE_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar body age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0132 — hand_shape
- Definición: Campo operativo para hand shape dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hand shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_SHAPE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAND_SHAPE_DRIFT_OR_GAP
- Fallback: Reforzar hand shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0133 — finger_length
- Definición: Campo operativo para finger length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar finger length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar finger length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINGER_LENGTH_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FINGER_LENGTH_DRIFT_OR_GAP
- Fallback: Reforzar finger length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0134 — finger_taper
- Definición: Campo operativo para finger taper dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar finger taper como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar finger taper como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINGER_TAPER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FINGER_TAPER_DRIFT_OR_GAP
- Fallback: Reforzar finger taper con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0135 — knuckle_visibility
- Definición: Campo operativo para knuckle visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar knuckle visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar knuckle visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KNUCKLE_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_KNUCKLE_VISIBILITY_DRIFT_OR_GAP
- Fallback: Reforzar knuckle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0136 — nail_style
- Definición: Campo operativo para nail style dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar nail style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nail style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NAIL_STYLE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NAIL_STYLE_DRIFT_OR_GAP
- Fallback: Reforzar nail style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0137 — hand_gesture_rest
- Definición: Campo operativo para hand gesture rest dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hand gesture rest como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand gesture rest como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_GESTURE_REST_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAND_GESTURE_REST_DRIFT_OR_GAP
- Fallback: Reforzar hand gesture rest con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PROPS_0138 — hand_object_contact
- Definición: Campo operativo para hand object contact dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hand object contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand object contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_OBJECT_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAND_OBJECT_CONTACT_DRIFT_OR_GAP
- Fallback: Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0139 — feet_ground_contact
- Definición: Campo operativo para feet ground contact dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar feet ground contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar feet ground contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FEET_GROUND_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FEET_GROUND_CONTACT_DRIFT_OR_GAP
- Fallback: Reforzar feet ground contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0140 — toe_visibility_rule
- Definición: Campo operativo para toe visibility rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar toe visibility rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar toe visibility rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TOE_VISIBILITY_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TOE_VISIBILITY_RULE_DRIFT_OR_GAP
- Fallback: Reforzar toe visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0141 — shoe_fit_rule
- Definición: Campo operativo para shoe fit rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shoe fit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoe fit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOE_FIT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHOE_FIT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar shoe fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0142 — hands_age_signature
- Definición: Campo operativo para hands age signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hands age signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands age signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_AGE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HANDS_AGE_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar hands age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0143 — contact_pressure_rule
- Definición: Campo operativo para contact pressure rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar contact pressure rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contact pressure rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTACT_PRESSURE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CONTACT_PRESSURE_RULE_DRIFT_OR_GAP
- Fallback: Reforzar contact pressure rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0144 — center_of_gravity
- Definición: Campo operativo para center of gravity dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar center of gravity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar center of gravity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CENTER_OF_GRAVITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CENTER_OF_GRAVITY_DRIFT_OR_GAP
- Fallback: Reforzar center of gravity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0145 — posture_base
- Definición: Campo operativo para posture base dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar posture base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar posture base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSTURE_BASE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_POSTURE_BASE_DRIFT_OR_GAP
- Fallback: Reforzar posture base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0146 — spine_curve
- Definición: Campo operativo para spine curve dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar spine curve como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar spine curve como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPINE_CURVE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SPINE_CURVE_DRIFT_OR_GAP
- Fallback: Reforzar spine curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0147 — shoulder_behavior
- Definición: Campo operativo para shoulder behavior dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shoulder behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_BEHAVIOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHOULDER_BEHAVIOR_DRIFT_OR_GAP
- Fallback: Reforzar shoulder behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0148 — hip_alignment
- Definición: Campo operativo para hip alignment dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hip alignment como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hip alignment como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HIP_ALIGNMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HIP_ALIGNMENT_DRIFT_OR_GAP
- Fallback: Reforzar hip alignment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0149 — weight_distribution
- Definición: Campo operativo para weight distribution dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar weight distribution como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar weight distribution como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WEIGHT_DISTRIBUTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WEIGHT_DISTRIBUTION_DRIFT_OR_GAP
- Fallback: Reforzar weight distribution con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0150 — standing_balance
- Definición: Campo operativo para standing balance dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar standing balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar standing balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STANDING_BALANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_STANDING_BALANCE_DRIFT_OR_GAP
- Fallback: Reforzar standing balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0151 — sitting_balance
- Definición: Campo operativo para sitting balance dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar sitting balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sitting balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SITTING_BALANCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SITTING_BALANCE_DRIFT_OR_GAP
- Fallback: Reforzar sitting balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0152 — walking_weight
- Definición: Campo operativo para walking weight dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar walking weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WALKING_WEIGHT_DRIFT_OR_GAP
- Fallback: Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0153 — dance_range
- Definición: Campo operativo para dance range dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar dance range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dance range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DANCE_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DANCE_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar dance range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0154 — fitness_tone
- Definición: Campo operativo para fitness tone dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fitness tone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fitness tone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FITNESS_TONE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FITNESS_TONE_DRIFT_OR_GAP
- Fallback: Reforzar fitness tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0155 — body_energy_signature
- Definición: Campo operativo para body energy signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar body energy signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body energy signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_ENERGY_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BODY_ENERGY_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar body energy signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0156 — same_body_blocker
- Definición: Campo operativo para same body blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar same body blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar same body blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SAME_BODY_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SAME_BODY_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar same body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0157 — wrong_age_body_blocker
- Definición: Campo operativo para wrong age body blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wrong age body blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong age body blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_AGE_BODY_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WRONG_AGE_BODY_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar wrong age body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0158 — impossible_pose_blocker
- Definición: Campo operativo para impossible pose blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar impossible pose blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar impossible pose blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMPOSSIBLE_POSE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_IMPOSSIBLE_POSE_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar impossible pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0159 — body_lens_distortion_rule
- Definición: Campo operativo para body lens distortion rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar body lens distortion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body lens distortion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_LENS_DISTORTION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BODY_LENS_DISTORTION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar body lens distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PROPS_0160 — proportion_repair_rule
- Definición: Campo operativo para proportion repair rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar proportion repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar proportion repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROPORTION_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROPORTION_REPAIR_RULE_DRIFT_OR_GAP
- Fallback: Reforzar proportion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0161 — hands_feet_repair_rule
- Definición: Campo operativo para hands feet repair rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hands feet repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands feet repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_FEET_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HANDS_FEET_REPAIR_RULE_DRIFT_OR_GAP
- Fallback: Reforzar hands feet repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0162 — adult_body_safety_rule
- Definición: Campo operativo para adult body safety rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar adult body safety rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult body safety rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_BODY_SAFETY_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ADULT_BODY_SAFETY_RULE_DRIFT_OR_GAP
- Fallback: Reforzar adult body safety rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0563 — height_range_prompt_effect
- Definición: Campo operativo para height range dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar height range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar height range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HEIGHT_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HEIGHT_RANGE_PROMPT_EFFECT
- Fallback: Reforzar height range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0564 — body_build_prompt_effect
- Definición: Campo operativo para body build dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body build como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body build como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_BUILD_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_BUILD_PROMPT_EFFECT
- Fallback: Reforzar body build con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0565 — visual_mass_prompt_effect
- Definición: Campo operativo para visual mass dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar visual mass como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar visual mass como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VISUAL_MASS_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VISUAL_MASS_PROMPT_EFFECT
- Fallback: Reforzar visual mass con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0566 — shoulder_width_prompt_effect
- Definición: Campo operativo para shoulder width dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_WIDTH_PROMPT_EFFECT
- Fallback: Reforzar shoulder width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0567 — neck_length_prompt_effect
- Definición: Campo operativo para neck length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar neck length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar neck length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NECK_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NECK_LENGTH_PROMPT_EFFECT
- Fallback: Reforzar neck length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0568 — clavicle_visibility_prompt_effect
- Definición: Campo operativo para clavicle visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clavicle visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clavicle visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLAVICLE_VISIBILITY_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLAVICLE_VISIBILITY_PROMPT_EFFEC
- Fallback: Reforzar clavicle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0569 — torso_length_prompt_effect
- Definición: Campo operativo para torso length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar torso length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar torso length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TORSO_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TORSO_LENGTH_PROMPT_EFFECT
- Fallback: Reforzar torso length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0570 — torso_leg_ratio_prompt_effect
- Definición: Campo operativo para torso leg ratio dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar torso leg ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar torso leg ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TORSO_LEG_RATIO_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TORSO_LEG_RATIO_PROMPT_EFFECT
- Fallback: Reforzar torso leg ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0571 — waist_hip_relation_prompt_effect
- Definición: Campo operativo para waist hip relation dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar waist hip relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar waist hip relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WAIST_HIP_RELATION_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WAIST_HIP_RELATION_PROMPT_EFFECT
- Fallback: Reforzar waist hip relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0572 — pelvis_width_prompt_effect
- Definición: Campo operativo para pelvis width dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pelvis width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pelvis width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PELVIS_WIDTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PELVIS_WIDTH_PROMPT_EFFECT
- Fallback: Reforzar pelvis width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0573 — arm_length_prompt_effect
- Definición: Campo operativo para arm length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar arm length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar arm length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARM_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARM_LENGTH_PROMPT_EFFECT
- Fallback: Reforzar arm length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0574 — forearm_shape_prompt_effect
- Definición: Campo operativo para forearm shape dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar forearm shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar forearm shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOREARM_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOREARM_SHAPE_PROMPT_EFFECT
- Fallback: Reforzar forearm shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0575 — wrist_scale_prompt_effect
- Definición: Campo operativo para wrist scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrist scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrist scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRIST_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRIST_SCALE_PROMPT_EFFECT
- Fallback: Reforzar wrist scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0576 — leg_line_prompt_effect
- Definición: Campo operativo para leg line dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar leg line como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar leg line como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LEG_LINE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LEG_LINE_PROMPT_EFFECT
- Fallback: Reforzar leg line con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0577 — knee_visibility_prompt_effect
- Definición: Campo operativo para knee visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar knee visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar knee visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KNEE_VISIBILITY_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KNEE_VISIBILITY_PROMPT_EFFECT
- Fallback: Reforzar knee visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0578 — ankle_scale_prompt_effect
- Definición: Campo operativo para ankle scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ankle scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ankle scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANKLE_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANKLE_SCALE_PROMPT_EFFECT
- Fallback: Reforzar ankle scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0579 — foot_scale_prompt_effect
- Definición: Campo operativo para foot scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar foot scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar foot scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOOT_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOOT_SCALE_PROMPT_EFFECT
- Fallback: Reforzar foot scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0580 — body_age_signature_prompt_effect
- Definición: Campo operativo para body age signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body age signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body age signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_AGE_SIGNATURE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_AGE_SIGNATURE_PROMPT_EFFECT
- Fallback: Reforzar body age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0581 — hand_shape_prompt_effect
- Definición: Campo operativo para hand shape dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_SHAPE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_SHAPE_PROMPT_EFFECT
- Fallback: Reforzar hand shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0582 — finger_length_prompt_effect
- Definición: Campo operativo para finger length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar finger length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar finger length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINGER_LENGTH_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINGER_LENGTH_PROMPT_EFFECT
- Fallback: Reforzar finger length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0583 — finger_taper_prompt_effect
- Definición: Campo operativo para finger taper dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar finger taper como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar finger taper como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINGER_TAPER_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINGER_TAPER_PROMPT_EFFECT
- Fallback: Reforzar finger taper con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0584 — knuckle_visibility_prompt_effect
- Definición: Campo operativo para knuckle visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar knuckle visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar knuckle visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KNUCKLE_VISIBILITY_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KNUCKLE_VISIBILITY_PROMPT_EFFECT
- Fallback: Reforzar knuckle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0585 — nail_style_prompt_effect
- Definición: Campo operativo para nail style dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nail style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nail style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NAIL_STYLE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NAIL_STYLE_PROMPT_EFFECT
- Fallback: Reforzar nail style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0586 — hand_gesture_rest_prompt_effect
- Definición: Campo operativo para hand gesture rest dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand gesture rest como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand gesture rest como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_GESTURE_REST_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_GESTURE_REST_PROMPT_EFFECT
- Fallback: Reforzar hand gesture rest con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PROPS_0587 — hand_object_contact_prompt_effect
- Definición: Campo operativo para hand object contact dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand object contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand object contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_OBJECT_CONTACT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_OBJECT_CONTACT_PROMPT_EFFEC
- Fallback: Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0588 — feet_ground_contact_prompt_effect
- Definición: Campo operativo para feet ground contact dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar feet ground contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar feet ground contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FEET_GROUND_CONTACT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FEET_GROUND_CONTACT_PROMPT_EFFEC
- Fallback: Reforzar feet ground contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0589 — toe_visibility_rule_prompt_effect
- Definición: Campo operativo para toe visibility rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar toe visibility rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar toe visibility rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TOE_VISIBILITY_RULE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TOE_VISIBILITY_RULE_PROMPT_EFFEC
- Fallback: Reforzar toe visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0590 — shoe_fit_rule_prompt_effect
- Definición: Campo operativo para shoe fit rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoe fit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoe fit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOE_FIT_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOE_FIT_RULE_PROMPT_EFFECT
- Fallback: Reforzar shoe fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0591 — hands_age_signature_prompt_effect
- Definición: Campo operativo para hands age signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands age signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands age signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_AGE_SIGNATURE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_AGE_SIGNATURE_PROMPT_EFFEC
- Fallback: Reforzar hands age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0592 — contact_pressure_rule_prompt_effect
- Definición: Campo operativo para contact pressure rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contact pressure rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contact pressure rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTACT_PRESSURE_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTACT_PRESSURE_RULE_PROMPT_EFF
- Fallback: Reforzar contact pressure rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0593 — center_of_gravity_prompt_effect
- Definición: Campo operativo para center of gravity dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar center of gravity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar center of gravity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CENTER_OF_GRAVITY_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CENTER_OF_GRAVITY_PROMPT_EFFECT
- Fallback: Reforzar center of gravity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0594 — posture_base_prompt_effect
- Definición: Campo operativo para posture base dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar posture base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar posture base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSTURE_BASE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSTURE_BASE_PROMPT_EFFECT
- Fallback: Reforzar posture base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0595 — spine_curve_prompt_effect
- Definición: Campo operativo para spine curve dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar spine curve como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar spine curve como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPINE_CURVE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPINE_CURVE_PROMPT_EFFECT
- Fallback: Reforzar spine curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0596 — shoulder_behavior_prompt_effect
- Definición: Campo operativo para shoulder behavior dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_BEHAVIOR_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_BEHAVIOR_PROMPT_EFFECT
- Fallback: Reforzar shoulder behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0597 — hip_alignment_prompt_effect
- Definición: Campo operativo para hip alignment dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hip alignment como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hip alignment como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HIP_ALIGNMENT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HIP_ALIGNMENT_PROMPT_EFFECT
- Fallback: Reforzar hip alignment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0598 — weight_distribution_prompt_effect
- Definición: Campo operativo para weight distribution dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar weight distribution como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar weight distribution como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WEIGHT_DISTRIBUTION_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WEIGHT_DISTRIBUTION_PROMPT_EFFEC
- Fallback: Reforzar weight distribution con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0599 — standing_balance_prompt_effect
- Definición: Campo operativo para standing balance dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar standing balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar standing balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STANDING_BALANCE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STANDING_BALANCE_PROMPT_EFFECT
- Fallback: Reforzar standing balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0600 — sitting_balance_prompt_effect
- Definición: Campo operativo para sitting balance dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sitting balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sitting balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SITTING_BALANCE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SITTING_BALANCE_PROMPT_EFFECT
- Fallback: Reforzar sitting balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0601 — walking_weight_prompt_effect
- Definición: Campo operativo para walking weight dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_WEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_WEIGHT_PROMPT_EFFECT
- Fallback: Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0602 — dance_range_prompt_effect
- Definición: Campo operativo para dance range dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dance range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dance range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DANCE_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DANCE_RANGE_PROMPT_EFFECT
- Fallback: Reforzar dance range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0603 — fitness_tone_prompt_effect
- Definición: Campo operativo para fitness tone dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fitness tone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fitness tone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FITNESS_TONE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FITNESS_TONE_PROMPT_EFFECT
- Fallback: Reforzar fitness tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0604 — body_energy_signature_prompt_effect
- Definición: Campo operativo para body energy signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body energy signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body energy signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_ENERGY_SIGNATURE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_ENERGY_SIGNATURE_PROMPT_EFF
- Fallback: Reforzar body energy signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0605 — same_body_blocker_prompt_effect
- Definición: Campo operativo para same body blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar same body blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar same body blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SAME_BODY_BLOCKER_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SAME_BODY_BLOCKER_PROMPT_EFFECT
- Fallback: Reforzar same body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0606 — wrong_age_body_blocker_prompt_effect
- Definición: Campo operativo para wrong age body blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong age body blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong age body blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_AGE_BODY_BLOCKER_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_AGE_BODY_BLOCKER_PROMPT_EF
- Fallback: Reforzar wrong age body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0607 — impossible_pose_blocker_prompt_effect
- Definición: Campo operativo para impossible pose blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar impossible pose blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar impossible pose blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMPOSSIBLE_POSE_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMPOSSIBLE_POSE_BLOCKER_PROMPT_E
- Fallback: Reforzar impossible pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0608 — body_lens_distortion_rule_prompt_effect
- Definición: Campo operativo para body lens distortion rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body lens distortion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body lens distortion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_LENS_DISTORTION_RULE_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_LENS_DISTORTION_RULE_PROMPT
- Fallback: Reforzar body lens distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PROPS_0609 — proportion_repair_rule_prompt_effect
- Definición: Campo operativo para proportion repair rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar proportion repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar proportion repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROPORTION_REPAIR_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROPORTION_REPAIR_RULE_PROMPT_EF
- Fallback: Reforzar proportion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0610 — hands_feet_repair_rule_prompt_effect
- Definición: Campo operativo para hands feet repair rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands feet repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands feet repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_FEET_REPAIR_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_FEET_REPAIR_RULE_PROMPT_EF
- Fallback: Reforzar hands feet repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_0611 — adult_body_safety_rule_prompt_effect
- Definición: Campo operativo para adult body safety rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult body safety rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult body safety rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_BODY_SAFETY_RULE_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_BODY_SAFETY_RULE_PROMPT_EF
- Fallback: Reforzar adult body safety rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1012 — height_range_qa_matrix
- Definición: Campo operativo para height range dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar height range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar height range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HEIGHT_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HEIGHT_RANGE_QA_MATRIX
- Fallback: Reforzar height range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1013 — body_build_qa_matrix
- Definición: Campo operativo para body build dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body build como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body build como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_BUILD_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_BUILD_QA_MATRIX
- Fallback: Reforzar body build con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1014 — visual_mass_qa_matrix
- Definición: Campo operativo para visual mass dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar visual mass como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar visual mass como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VISUAL_MASS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VISUAL_MASS_QA_MATRIX
- Fallback: Reforzar visual mass con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1015 — shoulder_width_qa_matrix
- Definición: Campo operativo para shoulder width dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_WIDTH_QA_MATRIX
- Fallback: Reforzar shoulder width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1016 — neck_length_qa_matrix
- Definición: Campo operativo para neck length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar neck length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar neck length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NECK_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NECK_LENGTH_QA_MATRIX
- Fallback: Reforzar neck length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1017 — clavicle_visibility_qa_matrix
- Definición: Campo operativo para clavicle visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clavicle visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clavicle visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLAVICLE_VISIBILITY_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLAVICLE_VISIBILITY_QA_MATRIX
- Fallback: Reforzar clavicle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1018 — torso_length_qa_matrix
- Definición: Campo operativo para torso length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar torso length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar torso length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TORSO_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TORSO_LENGTH_QA_MATRIX
- Fallback: Reforzar torso length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1019 — torso_leg_ratio_qa_matrix
- Definición: Campo operativo para torso leg ratio dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar torso leg ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar torso leg ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TORSO_LEG_RATIO_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TORSO_LEG_RATIO_QA_MATRIX
- Fallback: Reforzar torso leg ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1020 — waist_hip_relation_qa_matrix
- Definición: Campo operativo para waist hip relation dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar waist hip relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar waist hip relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WAIST_HIP_RELATION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WAIST_HIP_RELATION_QA_MATRIX
- Fallback: Reforzar waist hip relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1021 — pelvis_width_qa_matrix
- Definición: Campo operativo para pelvis width dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pelvis width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pelvis width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PELVIS_WIDTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PELVIS_WIDTH_QA_MATRIX
- Fallback: Reforzar pelvis width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1022 — arm_length_qa_matrix
- Definición: Campo operativo para arm length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar arm length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar arm length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARM_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARM_LENGTH_QA_MATRIX
- Fallback: Reforzar arm length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1023 — forearm_shape_qa_matrix
- Definición: Campo operativo para forearm shape dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar forearm shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar forearm shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOREARM_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOREARM_SHAPE_QA_MATRIX
- Fallback: Reforzar forearm shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1024 — wrist_scale_qa_matrix
- Definición: Campo operativo para wrist scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrist scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrist scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRIST_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRIST_SCALE_QA_MATRIX
- Fallback: Reforzar wrist scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1025 — leg_line_qa_matrix
- Definición: Campo operativo para leg line dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar leg line como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar leg line como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LEG_LINE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LEG_LINE_QA_MATRIX
- Fallback: Reforzar leg line con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1026 — knee_visibility_qa_matrix
- Definición: Campo operativo para knee visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar knee visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar knee visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KNEE_VISIBILITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KNEE_VISIBILITY_QA_MATRIX
- Fallback: Reforzar knee visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1027 — ankle_scale_qa_matrix
- Definición: Campo operativo para ankle scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ankle scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ankle scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANKLE_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANKLE_SCALE_QA_MATRIX
- Fallback: Reforzar ankle scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1028 — foot_scale_qa_matrix
- Definición: Campo operativo para foot scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar foot scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar foot scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOOT_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOOT_SCALE_QA_MATRIX
- Fallback: Reforzar foot scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1029 — body_age_signature_qa_matrix
- Definición: Campo operativo para body age signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body age signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body age signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_AGE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_AGE_SIGNATURE_QA_MATRIX
- Fallback: Reforzar body age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1030 — hand_shape_qa_matrix
- Definición: Campo operativo para hand shape dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_SHAPE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_SHAPE_QA_MATRIX
- Fallback: Reforzar hand shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1031 — finger_length_qa_matrix
- Definición: Campo operativo para finger length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar finger length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar finger length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINGER_LENGTH_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINGER_LENGTH_QA_MATRIX
- Fallback: Reforzar finger length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1032 — finger_taper_qa_matrix
- Definición: Campo operativo para finger taper dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar finger taper como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar finger taper como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINGER_TAPER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINGER_TAPER_QA_MATRIX
- Fallback: Reforzar finger taper con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1033 — knuckle_visibility_qa_matrix
- Definición: Campo operativo para knuckle visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar knuckle visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar knuckle visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KNUCKLE_VISIBILITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KNUCKLE_VISIBILITY_QA_MATRIX
- Fallback: Reforzar knuckle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1034 — nail_style_qa_matrix
- Definición: Campo operativo para nail style dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nail style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nail style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NAIL_STYLE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NAIL_STYLE_QA_MATRIX
- Fallback: Reforzar nail style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1035 — hand_gesture_rest_qa_matrix
- Definición: Campo operativo para hand gesture rest dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand gesture rest como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand gesture rest como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_GESTURE_REST_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_GESTURE_REST_QA_MATRIX
- Fallback: Reforzar hand gesture rest con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PROPS_1036 — hand_object_contact_qa_matrix
- Definición: Campo operativo para hand object contact dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand object contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand object contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_OBJECT_CONTACT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_OBJECT_CONTACT_QA_MATRIX
- Fallback: Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1037 — feet_ground_contact_qa_matrix
- Definición: Campo operativo para feet ground contact dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar feet ground contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar feet ground contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FEET_GROUND_CONTACT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FEET_GROUND_CONTACT_QA_MATRIX
- Fallback: Reforzar feet ground contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1038 — toe_visibility_rule_qa_matrix
- Definición: Campo operativo para toe visibility rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar toe visibility rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar toe visibility rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TOE_VISIBILITY_RULE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TOE_VISIBILITY_RULE_QA_MATRIX
- Fallback: Reforzar toe visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1039 — shoe_fit_rule_qa_matrix
- Definición: Campo operativo para shoe fit rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoe fit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoe fit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOE_FIT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOE_FIT_RULE_QA_MATRIX
- Fallback: Reforzar shoe fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1040 — hands_age_signature_qa_matrix
- Definición: Campo operativo para hands age signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands age signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands age signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_AGE_SIGNATURE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_AGE_SIGNATURE_QA_MATRIX
- Fallback: Reforzar hands age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1041 — contact_pressure_rule_qa_matrix
- Definición: Campo operativo para contact pressure rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contact pressure rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contact pressure rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTACT_PRESSURE_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTACT_PRESSURE_RULE_QA_MATRIX
- Fallback: Reforzar contact pressure rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1042 — center_of_gravity_qa_matrix
- Definición: Campo operativo para center of gravity dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar center of gravity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar center of gravity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CENTER_OF_GRAVITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CENTER_OF_GRAVITY_QA_MATRIX
- Fallback: Reforzar center of gravity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1043 — posture_base_qa_matrix
- Definición: Campo operativo para posture base dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar posture base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar posture base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSTURE_BASE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSTURE_BASE_QA_MATRIX
- Fallback: Reforzar posture base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1044 — spine_curve_qa_matrix
- Definición: Campo operativo para spine curve dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar spine curve como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar spine curve como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPINE_CURVE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPINE_CURVE_QA_MATRIX
- Fallback: Reforzar spine curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1045 — shoulder_behavior_qa_matrix
- Definición: Campo operativo para shoulder behavior dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_BEHAVIOR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_BEHAVIOR_QA_MATRIX
- Fallback: Reforzar shoulder behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1046 — hip_alignment_qa_matrix
- Definición: Campo operativo para hip alignment dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hip alignment como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hip alignment como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HIP_ALIGNMENT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HIP_ALIGNMENT_QA_MATRIX
- Fallback: Reforzar hip alignment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1047 — weight_distribution_qa_matrix
- Definición: Campo operativo para weight distribution dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar weight distribution como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar weight distribution como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WEIGHT_DISTRIBUTION_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WEIGHT_DISTRIBUTION_QA_MATRIX
- Fallback: Reforzar weight distribution con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1048 — standing_balance_qa_matrix
- Definición: Campo operativo para standing balance dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar standing balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar standing balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STANDING_BALANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STANDING_BALANCE_QA_MATRIX
- Fallback: Reforzar standing balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1049 — sitting_balance_qa_matrix
- Definición: Campo operativo para sitting balance dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sitting balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sitting balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SITTING_BALANCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SITTING_BALANCE_QA_MATRIX
- Fallback: Reforzar sitting balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1050 — walking_weight_qa_matrix
- Definición: Campo operativo para walking weight dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_WEIGHT_QA_MATRIX
- Fallback: Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1051 — dance_range_qa_matrix
- Definición: Campo operativo para dance range dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dance range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dance range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DANCE_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DANCE_RANGE_QA_MATRIX
- Fallback: Reforzar dance range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1052 — fitness_tone_qa_matrix
- Definición: Campo operativo para fitness tone dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fitness tone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fitness tone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FITNESS_TONE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FITNESS_TONE_QA_MATRIX
- Fallback: Reforzar fitness tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1053 — body_energy_signature_qa_matrix
- Definición: Campo operativo para body energy signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body energy signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body energy signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_ENERGY_SIGNATURE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_ENERGY_SIGNATURE_QA_MATRIX
- Fallback: Reforzar body energy signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1054 — same_body_blocker_qa_matrix
- Definición: Campo operativo para same body blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar same body blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar same body blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SAME_BODY_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SAME_BODY_BLOCKER_QA_MATRIX
- Fallback: Reforzar same body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1055 — wrong_age_body_blocker_qa_matrix
- Definición: Campo operativo para wrong age body blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong age body blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong age body blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_AGE_BODY_BLOCKER_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_AGE_BODY_BLOCKER_QA_MATRIX
- Fallback: Reforzar wrong age body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1056 — impossible_pose_blocker_qa_matrix
- Definición: Campo operativo para impossible pose blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar impossible pose blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar impossible pose blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMPOSSIBLE_POSE_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMPOSSIBLE_POSE_BLOCKER_QA_MATRI
- Fallback: Reforzar impossible pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1057 — body_lens_distortion_rule_qa_matrix
- Definición: Campo operativo para body lens distortion rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body lens distortion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body lens distortion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_LENS_DISTORTION_RULE_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_LENS_DISTORTION_RULE_QA_MAT
- Fallback: Reforzar body lens distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PROPS_1058 — proportion_repair_rule_qa_matrix
- Definición: Campo operativo para proportion repair rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar proportion repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar proportion repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROPORTION_REPAIR_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROPORTION_REPAIR_RULE_QA_MATRIX
- Fallback: Reforzar proportion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1059 — hands_feet_repair_rule_qa_matrix
- Definición: Campo operativo para hands feet repair rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands feet repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands feet repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_FEET_REPAIR_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_FEET_REPAIR_RULE_QA_MATRIX
- Fallback: Reforzar hands feet repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1060 — adult_body_safety_rule_qa_matrix
- Definición: Campo operativo para adult body safety rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult body safety rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult body safety rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_BODY_SAFETY_RULE_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_BODY_SAFETY_RULE_QA_MATRIX
- Fallback: Reforzar adult body safety rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1461 — height_range_vendor_repair
- Definición: Campo operativo para height range dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar height range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar height range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HEIGHT_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HEIGHT_RANGE_VENDOR_REPAIR
- Fallback: Reforzar height range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1462 — body_build_vendor_repair
- Definición: Campo operativo para body build dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body build como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body build como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_BUILD_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_BUILD_VENDOR_REPAIR
- Fallback: Reforzar body build con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1463 — visual_mass_vendor_repair
- Definición: Campo operativo para visual mass dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar visual mass como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar visual mass como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VISUAL_MASS_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VISUAL_MASS_VENDOR_REPAIR
- Fallback: Reforzar visual mass con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1464 — shoulder_width_vendor_repair
- Definición: Campo operativo para shoulder width dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_WIDTH_VENDOR_REPAIR
- Fallback: Reforzar shoulder width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1465 — neck_length_vendor_repair
- Definición: Campo operativo para neck length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar neck length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar neck length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NECK_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NECK_LENGTH_VENDOR_REPAIR
- Fallback: Reforzar neck length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1466 — clavicle_visibility_vendor_repair
- Definición: Campo operativo para clavicle visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clavicle visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clavicle visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLAVICLE_VISIBILITY_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLAVICLE_VISIBILITY_VENDOR_REPAI
- Fallback: Reforzar clavicle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1467 — torso_length_vendor_repair
- Definición: Campo operativo para torso length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar torso length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar torso length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TORSO_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TORSO_LENGTH_VENDOR_REPAIR
- Fallback: Reforzar torso length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1468 — torso_leg_ratio_vendor_repair
- Definición: Campo operativo para torso leg ratio dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar torso leg ratio como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar torso leg ratio como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TORSO_LEG_RATIO_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TORSO_LEG_RATIO_VENDOR_REPAIR
- Fallback: Reforzar torso leg ratio con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1469 — waist_hip_relation_vendor_repair
- Definición: Campo operativo para waist hip relation dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar waist hip relation como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar waist hip relation como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WAIST_HIP_RELATION_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WAIST_HIP_RELATION_VENDOR_REPAIR
- Fallback: Reforzar waist hip relation con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1470 — pelvis_width_vendor_repair
- Definición: Campo operativo para pelvis width dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pelvis width como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pelvis width como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PELVIS_WIDTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PELVIS_WIDTH_VENDOR_REPAIR
- Fallback: Reforzar pelvis width con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1471 — arm_length_vendor_repair
- Definición: Campo operativo para arm length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar arm length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar arm length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARM_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARM_LENGTH_VENDOR_REPAIR
- Fallback: Reforzar arm length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1472 — forearm_shape_vendor_repair
- Definición: Campo operativo para forearm shape dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar forearm shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar forearm shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOREARM_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOREARM_SHAPE_VENDOR_REPAIR
- Fallback: Reforzar forearm shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1473 — wrist_scale_vendor_repair
- Definición: Campo operativo para wrist scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrist scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrist scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRIST_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRIST_SCALE_VENDOR_REPAIR
- Fallback: Reforzar wrist scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1474 — leg_line_vendor_repair
- Definición: Campo operativo para leg line dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar leg line como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar leg line como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LEG_LINE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LEG_LINE_VENDOR_REPAIR
- Fallback: Reforzar leg line con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1475 — knee_visibility_vendor_repair
- Definición: Campo operativo para knee visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar knee visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar knee visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KNEE_VISIBILITY_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KNEE_VISIBILITY_VENDOR_REPAIR
- Fallback: Reforzar knee visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1476 — ankle_scale_vendor_repair
- Definición: Campo operativo para ankle scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar ankle scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar ankle scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ANKLE_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ANKLE_SCALE_VENDOR_REPAIR
- Fallback: Reforzar ankle scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1477 — foot_scale_vendor_repair
- Definición: Campo operativo para foot scale dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar foot scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar foot scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FOOT_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FOOT_SCALE_VENDOR_REPAIR
- Fallback: Reforzar foot scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1478 — body_age_signature_vendor_repair
- Definición: Campo operativo para body age signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body age signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body age signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_AGE_SIGNATURE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_AGE_SIGNATURE_VENDOR_REPAIR
- Fallback: Reforzar body age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1479 — hand_shape_vendor_repair
- Definición: Campo operativo para hand shape dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand shape como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand shape como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_SHAPE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_SHAPE_VENDOR_REPAIR
- Fallback: Reforzar hand shape con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1480 — finger_length_vendor_repair
- Definición: Campo operativo para finger length dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar finger length como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar finger length como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINGER_LENGTH_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINGER_LENGTH_VENDOR_REPAIR
- Fallback: Reforzar finger length con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1481 — finger_taper_vendor_repair
- Definición: Campo operativo para finger taper dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar finger taper como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar finger taper como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FINGER_TAPER_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FINGER_TAPER_VENDOR_REPAIR
- Fallback: Reforzar finger taper con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1482 — knuckle_visibility_vendor_repair
- Definición: Campo operativo para knuckle visibility dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar knuckle visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar knuckle visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_KNUCKLE_VISIBILITY_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_KNUCKLE_VISIBILITY_VENDOR_REPAIR
- Fallback: Reforzar knuckle visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1483 — nail_style_vendor_repair
- Definición: Campo operativo para nail style dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar nail style como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar nail style como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NAIL_STYLE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NAIL_STYLE_VENDOR_REPAIR
- Fallback: Reforzar nail style con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1484 — hand_gesture_rest_vendor_repair
- Definición: Campo operativo para hand gesture rest dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand gesture rest como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand gesture rest como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_GESTURE_REST_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_GESTURE_REST_VENDOR_REPAIR
- Fallback: Reforzar hand gesture rest con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PROPS_1485 — hand_object_contact_vendor_repair
- Definición: Campo operativo para hand object contact dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand object contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand object contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_OBJECT_CONTACT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_OBJECT_CONTACT_VENDOR_REPAI
- Fallback: Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1486 — feet_ground_contact_vendor_repair
- Definición: Campo operativo para feet ground contact dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar feet ground contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar feet ground contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FEET_GROUND_CONTACT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FEET_GROUND_CONTACT_VENDOR_REPAI
- Fallback: Reforzar feet ground contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1487 — toe_visibility_rule_vendor_repair
- Definición: Campo operativo para toe visibility rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar toe visibility rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar toe visibility rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TOE_VISIBILITY_RULE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TOE_VISIBILITY_RULE_VENDOR_REPAI
- Fallback: Reforzar toe visibility rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1488 — shoe_fit_rule_vendor_repair
- Definición: Campo operativo para shoe fit rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoe fit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoe fit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOE_FIT_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOE_FIT_RULE_VENDOR_REPAIR
- Fallback: Reforzar shoe fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1489 — hands_age_signature_vendor_repair
- Definición: Campo operativo para hands age signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands age signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands age signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_AGE_SIGNATURE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_AGE_SIGNATURE_VENDOR_REPAI
- Fallback: Reforzar hands age signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1490 — contact_pressure_rule_vendor_repair
- Definición: Campo operativo para contact pressure rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar contact pressure rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar contact pressure rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CONTACT_PRESSURE_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CONTACT_PRESSURE_RULE_VENDOR_REP
- Fallback: Reforzar contact pressure rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1491 — center_of_gravity_vendor_repair
- Definición: Campo operativo para center of gravity dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar center of gravity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar center of gravity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CENTER_OF_GRAVITY_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CENTER_OF_GRAVITY_VENDOR_REPAIR
- Fallback: Reforzar center of gravity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1492 — posture_base_vendor_repair
- Definición: Campo operativo para posture base dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar posture base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar posture base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSTURE_BASE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSTURE_BASE_VENDOR_REPAIR
- Fallback: Reforzar posture base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1493 — spine_curve_vendor_repair
- Definición: Campo operativo para spine curve dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar spine curve como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar spine curve como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SPINE_CURVE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SPINE_CURVE_VENDOR_REPAIR
- Fallback: Reforzar spine curve con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1494 — shoulder_behavior_vendor_repair
- Definición: Campo operativo para shoulder behavior dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_BEHAVIOR_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_BEHAVIOR_VENDOR_REPAIR
- Fallback: Reforzar shoulder behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1495 — hip_alignment_vendor_repair
- Definición: Campo operativo para hip alignment dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hip alignment como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hip alignment como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HIP_ALIGNMENT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HIP_ALIGNMENT_VENDOR_REPAIR
- Fallback: Reforzar hip alignment con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1496 — weight_distribution_vendor_repair
- Definición: Campo operativo para weight distribution dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar weight distribution como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar weight distribution como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WEIGHT_DISTRIBUTION_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WEIGHT_DISTRIBUTION_VENDOR_REPAI
- Fallback: Reforzar weight distribution con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1497 — standing_balance_vendor_repair
- Definición: Campo operativo para standing balance dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar standing balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar standing balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STANDING_BALANCE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STANDING_BALANCE_VENDOR_REPAIR
- Fallback: Reforzar standing balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1498 — sitting_balance_vendor_repair
- Definición: Campo operativo para sitting balance dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar sitting balance como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar sitting balance como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SITTING_BALANCE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SITTING_BALANCE_VENDOR_REPAIR
- Fallback: Reforzar sitting balance con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1499 — walking_weight_vendor_repair
- Definición: Campo operativo para walking weight dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_WEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_WEIGHT_VENDOR_REPAIR
- Fallback: Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1500 — dance_range_vendor_repair
- Definición: Campo operativo para dance range dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dance range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dance range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DANCE_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DANCE_RANGE_VENDOR_REPAIR
- Fallback: Reforzar dance range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1501 — fitness_tone_vendor_repair
- Definición: Campo operativo para fitness tone dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fitness tone como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fitness tone como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FITNESS_TONE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FITNESS_TONE_VENDOR_REPAIR
- Fallback: Reforzar fitness tone con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1502 — body_energy_signature_vendor_repair
- Definición: Campo operativo para body energy signature dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body energy signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body energy signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_ENERGY_SIGNATURE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_ENERGY_SIGNATURE_VENDOR_REP
- Fallback: Reforzar body energy signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1503 — same_body_blocker_vendor_repair
- Definición: Campo operativo para same body blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar same body blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar same body blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SAME_BODY_BLOCKER_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SAME_BODY_BLOCKER_VENDOR_REPAIR
- Fallback: Reforzar same body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1504 — wrong_age_body_blocker_vendor_repair
- Definición: Campo operativo para wrong age body blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong age body blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong age body blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_AGE_BODY_BLOCKER_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_AGE_BODY_BLOCKER_VENDOR_RE
- Fallback: Reforzar wrong age body blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1505 — impossible_pose_blocker_vendor_repair
- Definición: Campo operativo para impossible pose blocker dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar impossible pose blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar impossible pose blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_IMPOSSIBLE_POSE_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_IMPOSSIBLE_POSE_BLOCKER_VENDOR_R
- Fallback: Reforzar impossible pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1506 — body_lens_distortion_rule_vendor_repair
- Definición: Campo operativo para body lens distortion rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body lens distortion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body lens distortion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_LENS_DISTORTION_RULE_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_LENS_DISTORTION_RULE_VENDOR
- Fallback: Reforzar body lens distortion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_PROPS_1507 — proportion_repair_rule_vendor_repair
- Definición: Campo operativo para proportion repair rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar proportion repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar proportion repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROPORTION_REPAIR_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROPORTION_REPAIR_RULE_VENDOR_RE
- Fallback: Reforzar proportion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1508 — hands_feet_repair_rule_vendor_repair
- Definición: Campo operativo para hands feet repair rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands feet repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands feet repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_FEET_REPAIR_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_FEET_REPAIR_RULE_VENDOR_RE
- Fallback: Reforzar hands feet repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_BODY_1509 — adult_body_safety_rule_vendor_repair
- Definición: Campo operativo para adult body safety rule dentro de Cuerpo, antropometría, edad adulta, fitness editorial y uniqueness corporal. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult body safety rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult body safety rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_BODY_SAFETY_RULE_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_BODY_SAFETY_RULE_VENDOR_RE
- Fallback: Reforzar adult body safety rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
