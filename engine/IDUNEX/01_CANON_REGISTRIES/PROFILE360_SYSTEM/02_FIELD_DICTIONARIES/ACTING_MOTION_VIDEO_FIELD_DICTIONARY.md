## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Acting, FACS, microgestos, pose, caminada y continuidad de video

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_VIDEO_0259` | `facs_base` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACS_BASE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar facs base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0260` | `smile_types` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SMILE_TYPES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar smile types con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0261` | `microgesture_set` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICROGESTURE_SET_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar microgesture set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0262` | `eye_emotion_map` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_EMOTION_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0263` | `brow_micro_movement` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_MICRO_MOVEMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar brow micro movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0264` | `jaw_tension` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_TENSION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar jaw tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0265` | `mouth_corner_behavior` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOUTH_CORNER_BEHAVIOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar mouth corner behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0266` | `neck_tension` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NECK_TENSION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar neck tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0267` | `subtext_state` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUBTEXT_STATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar subtext state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0268` | `emotion_transition_rule` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_TRANSITION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar emotion transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0269` | `camera_reaction_pattern` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_REACTION_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar camera reaction pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0270` | `emotion_to_pose_map` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_TO_POSE_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar emotion to pose map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0271` | `walking_rhythm` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_RHYTHM_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar walking rhythm con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0272` | `walking_weight` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0273` | `hip_movement` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HIP_MOVEMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hip movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0274` | `shoulder_countermotion` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_COUNTERMOTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shoulder countermotion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0275` | `arm_swing` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARM_SWING_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar arm swing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0276` | `hand_gesture_library` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_GESTURE_LIBRARY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hand gesture library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0277` | `breathing_visibility` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BREATHING_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar breathing visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0278` | `pose_energy` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_ENERGY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar pose energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0279` | `pose_range` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar pose range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0280` | `dance_signature` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DANCE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar dance signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0281` | `runway_presence` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RUNWAY_PRESENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar runway presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0282` | `camera_presence` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_PRESENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar camera presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0283` | `micro_action_library` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICRO_ACTION_LIBRARY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar micro action library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0284` | `video_continuity_lock` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_CONTINUITY_LOCK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar video continuity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0285` | `frame_to_frame_identity` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FRAME_TO_FRAME_IDENTITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar frame to frame identity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0286` | `shot_transition_rule` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOT_TRANSITION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar shot transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0287` | `motion_blur_rule` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTION_BLUR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar motion blur rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0288` | `hair_motion_continuity` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_MOTION_CONTINUITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hair motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0289` | `wardrobe_motion_continuity` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_MOTION_CONTINUITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wardrobe motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0290` | `voice_body_sync` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_BODY_SYNC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar voice body sync con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0291` | `acting_intention_per_shot` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACTING_INTENTION_PER_SHOT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar acting intention per shot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0292` | `clip_complexity_limit` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLIP_COMPLEXITY_LIMIT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar clip complexity limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0293` | `video_prompt_timeline` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_PROMPT_TIMELINE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar video prompt timeline con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0294` | `rigid_pose_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RIGID_POSE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar rigid pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0295` | `fake_expression_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAKE_EXPRESSION_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fake expression blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0296` | `morphing_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MORPHING_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar morphing blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0297` | `video_identity_jump_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_IDENTITY_JUMP_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar video identity jump blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0298` | `hands_warp_video_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_WARP_VIDEO_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hands warp video blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0299` | `emotion_mismatch_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_MISMATCH_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar emotion mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0300` | `motion_repair_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTION_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar motion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0301` | `video_regression_test` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_REGRESSION_TEST_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar video regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0708` | `facs_base_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACS_BASE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar facs base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0709` | `smile_types_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SMILE_TYPES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar smile types con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0710` | `microgesture_set_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICROGESTURE_SET_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar microgesture set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0711` | `eye_emotion_map_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_EMOTION_MAP_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0712` | `brow_micro_movement_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_MICRO_MOVEMENT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow micro movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0713` | `jaw_tension_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_TENSION_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0714` | `mouth_corner_behavior_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOUTH_CORNER_BEHAVIOR_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mouth corner behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0715` | `neck_tension_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NECK_TENSION_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar neck tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0716` | `subtext_state_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUBTEXT_STATE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar subtext state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0717` | `emotion_transition_rule_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_TRANSITION_RULE_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0718` | `camera_reaction_pattern_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_REACTION_PATTERN_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera reaction pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0719` | `emotion_to_pose_map_prompt_effect` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_TO_POSE_MAP_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion to pose map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0720` | `walking_rhythm_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_RHYTHM_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking rhythm con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0721` | `walking_weight_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_WEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0722` | `hip_movement_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HIP_MOVEMENT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hip movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0723` | `shoulder_countermotion_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_COUNTERMOTION_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder countermotion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0724` | `arm_swing_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARM_SWING_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar arm swing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0725` | `hand_gesture_library_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_GESTURE_LIBRARY_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand gesture library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0726` | `breathing_visibility_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BREATHING_VISIBILITY_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar breathing visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0727` | `pose_energy_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_ENERGY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0728` | `pose_range_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0729` | `dance_signature_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DANCE_SIGNATURE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dance signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0730` | `runway_presence_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RUNWAY_PRESENCE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar runway presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0731` | `camera_presence_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_PRESENCE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0732` | `micro_action_library_prompt_effect` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICRO_ACTION_LIBRARY_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar micro action library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0733` | `video_continuity_lock_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_CONTINUITY_LOCK_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video continuity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0734` | `frame_to_frame_identity_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FRAME_TO_FRAME_IDENTITY_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar frame to frame identity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0735` | `shot_transition_rule_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOT_TRANSITION_RULE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shot transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0736` | `motion_blur_rule_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTION_BLUR_RULE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motion blur rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0737` | `hair_motion_continuity_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_MOTION_CONTINUITY_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0738` | `wardrobe_motion_continuity_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_MOTION_CONTINUITY_P_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_0739` | `voice_body_sync_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_BODY_SYNC_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice body sync con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0740` | `acting_intention_per_shot_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACTING_INTENTION_PER_SHOT_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar acting intention per shot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0741` | `clip_complexity_limit_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLIP_COMPLEXITY_LIMIT_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clip complexity limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0742` | `video_prompt_timeline_prompt_effect` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_PROMPT_TIMELINE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video prompt timeline con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0743` | `rigid_pose_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RIGID_POSE_BLOCKER_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rigid pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0744` | `fake_expression_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAKE_EXPRESSION_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fake expression blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0745` | `morphing_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MORPHING_BLOCKER_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar morphing blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0746` | `video_identity_jump_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_IDENTITY_JUMP_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video identity jump blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0747` | `hands_warp_video_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_WARP_VIDEO_BLOCKER_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands warp video blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0748` | `emotion_mismatch_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_MISMATCH_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0749` | `motion_repair_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTION_REPAIR_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0750` | `video_regression_test_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_REGRESSION_TEST_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1157` | `facs_base_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACS_BASE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar facs base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1158` | `smile_types_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SMILE_TYPES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar smile types con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1159` | `microgesture_set_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICROGESTURE_SET_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar microgesture set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1160` | `eye_emotion_map_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_EMOTION_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1161` | `brow_micro_movement_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_MICRO_MOVEMENT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow micro movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1162` | `jaw_tension_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_TENSION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1163` | `mouth_corner_behavior_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOUTH_CORNER_BEHAVIOR_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mouth corner behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1164` | `neck_tension_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NECK_TENSION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar neck tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1165` | `subtext_state_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUBTEXT_STATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar subtext state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1166` | `emotion_transition_rule_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_TRANSITION_RULE_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1167` | `camera_reaction_pattern_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_REACTION_PATTERN_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera reaction pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1168` | `emotion_to_pose_map_qa_matrix` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_TO_POSE_MAP_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion to pose map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1169` | `walking_rhythm_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_RHYTHM_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking rhythm con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1170` | `walking_weight_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1171` | `hip_movement_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HIP_MOVEMENT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hip movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1172` | `shoulder_countermotion_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_COUNTERMOTION_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder countermotion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1173` | `arm_swing_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARM_SWING_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar arm swing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1174` | `hand_gesture_library_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_GESTURE_LIBRARY_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand gesture library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1175` | `breathing_visibility_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BREATHING_VISIBILITY_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar breathing visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1176` | `pose_energy_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_ENERGY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1177` | `pose_range_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1178` | `dance_signature_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DANCE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dance signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1179` | `runway_presence_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RUNWAY_PRESENCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar runway presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1180` | `camera_presence_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_PRESENCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1181` | `micro_action_library_qa_matrix` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICRO_ACTION_LIBRARY_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar micro action library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1182` | `video_continuity_lock_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_CONTINUITY_LOCK_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video continuity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1183` | `frame_to_frame_identity_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FRAME_TO_FRAME_IDENTITY_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar frame to frame identity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1184` | `shot_transition_rule_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOT_TRANSITION_RULE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shot transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1185` | `motion_blur_rule_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTION_BLUR_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motion blur rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1186` | `hair_motion_continuity_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_MOTION_CONTINUITY_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1187` | `wardrobe_motion_continuity_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_MOTION_CONTINUITY_Q_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1188` | `voice_body_sync_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_BODY_SYNC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice body sync con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1189` | `acting_intention_per_shot_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACTING_INTENTION_PER_SHOT_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar acting intention per shot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1190` | `clip_complexity_limit_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLIP_COMPLEXITY_LIMIT_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clip complexity limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1191` | `video_prompt_timeline_qa_matrix` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_PROMPT_TIMELINE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video prompt timeline con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1192` | `rigid_pose_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RIGID_POSE_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rigid pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1193` | `fake_expression_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAKE_EXPRESSION_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fake expression blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1194` | `morphing_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MORPHING_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar morphing blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1195` | `video_identity_jump_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_IDENTITY_JUMP_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video identity jump blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1196` | `hands_warp_video_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_WARP_VIDEO_BLOCKER_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands warp video blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1197` | `emotion_mismatch_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_MISMATCH_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1198` | `motion_repair_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTION_REPAIR_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1199` | `video_regression_test_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_REGRESSION_TEST_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1606` | `facs_base_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FACS_BASE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar facs base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1607` | `smile_types_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SMILE_TYPES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar smile types con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1608` | `microgesture_set_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICROGESTURE_SET_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar microgesture set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1609` | `eye_emotion_map_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EYE_EMOTION_MAP_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1610` | `brow_micro_movement_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BROW_MICRO_MOVEMENT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brow micro movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1611` | `jaw_tension_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JAW_TENSION_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jaw tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1612` | `mouth_corner_behavior_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOUTH_CORNER_BEHAVIOR_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar mouth corner behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1613` | `neck_tension_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NECK_TENSION_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar neck tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1614` | `subtext_state_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUBTEXT_STATE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar subtext state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1615` | `emotion_transition_rule_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_TRANSITION_RULE_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1616` | `camera_reaction_pattern_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_REACTION_PATTERN_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera reaction pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1617` | `emotion_to_pose_map_vendor_repair` | face_acting | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_TO_POSE_MAP_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion to pose map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1618` | `walking_rhythm_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_RHYTHM_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking rhythm con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1619` | `walking_weight_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WALKING_WEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1620` | `hip_movement_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HIP_MOVEMENT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hip movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1621` | `shoulder_countermotion_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOULDER_COUNTERMOTION_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shoulder countermotion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1622` | `arm_swing_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ARM_SWING_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar arm swing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1623` | `hand_gesture_library_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_GESTURE_LIBRARY_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand gesture library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1624` | `breathing_visibility_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BREATHING_VISIBILITY_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar breathing visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1625` | `pose_energy_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_ENERGY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1626` | `pose_range_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1627` | `dance_signature_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DANCE_SIGNATURE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar dance signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1628` | `runway_presence_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RUNWAY_PRESENCE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar runway presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1629` | `camera_presence_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_PRESENCE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1630` | `micro_action_library_vendor_repair` | body_motion | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MICRO_ACTION_LIBRARY_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar micro action library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1631` | `video_continuity_lock_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_CONTINUITY_LOCK_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video continuity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1632` | `frame_to_frame_identity_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FRAME_TO_FRAME_IDENTITY_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar frame to frame identity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1633` | `shot_transition_rule_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SHOT_TRANSITION_RULE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar shot transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1634` | `motion_blur_rule_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTION_BLUR_RULE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motion blur rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1635` | `hair_motion_continuity_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAIR_MOTION_CONTINUITY_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hair motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1636` | `wardrobe_motion_continuity_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_MOTION_CONTINUITY_V_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VOICE_1637` | `voice_body_sync_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VOICE_BODY_SYNC_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar voice body sync con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1638` | `acting_intention_per_shot_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACTING_INTENTION_PER_SHOT_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar acting intention per shot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1639` | `clip_complexity_limit_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CLIP_COMPLEXITY_LIMIT_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar clip complexity limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1640` | `video_prompt_timeline_vendor_repair` | video | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_PROMPT_TIMELINE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video prompt timeline con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1641` | `rigid_pose_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_RIGID_POSE_BLOCKER_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar rigid pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1642` | `fake_expression_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FAKE_EXPRESSION_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fake expression blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1643` | `morphing_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MORPHING_BLOCKER_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar morphing blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1644` | `video_identity_jump_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_IDENTITY_JUMP_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video identity jump blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1645` | `hands_warp_video_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HANDS_WARP_VIDEO_BLOCKER_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hands warp video blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1646` | `emotion_mismatch_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_EMOTION_MISMATCH_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar emotion mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1647` | `motion_repair_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MOTION_REPAIR_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar motion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1648` | `video_regression_test_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_VIDEO_REGRESSION_TEST_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar video regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_VIDEO_0259 — facs_base
- Definición: Campo operativo para facs base dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar facs base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar facs base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACS_BASE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FACS_BASE_DRIFT_OR_GAP
- Fallback: Reforzar facs base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0260 — smile_types
- Definición: Campo operativo para smile types dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar smile types como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar smile types como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SMILE_TYPES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SMILE_TYPES_DRIFT_OR_GAP
- Fallback: Reforzar smile types con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0261 — microgesture_set
- Definición: Campo operativo para microgesture set dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar microgesture set como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar microgesture set como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICROGESTURE_SET_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MICROGESTURE_SET_DRIFT_OR_GAP
- Fallback: Reforzar microgesture set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0262 — eye_emotion_map
- Definición: Campo operativo para eye emotion map dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar eye emotion map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye emotion map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_EMOTION_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EYE_EMOTION_MAP_DRIFT_OR_GAP
- Fallback: Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0263 — brow_micro_movement
- Definición: Campo operativo para brow micro movement dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar brow micro movement como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow micro movement como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_MICRO_MOVEMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BROW_MICRO_MOVEMENT_DRIFT_OR_GAP
- Fallback: Reforzar brow micro movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0264 — jaw_tension
- Definición: Campo operativo para jaw tension dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar jaw tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_TENSION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_JAW_TENSION_DRIFT_OR_GAP
- Fallback: Reforzar jaw tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0265 — mouth_corner_behavior
- Definición: Campo operativo para mouth corner behavior dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar mouth corner behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mouth corner behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOUTH_CORNER_BEHAVIOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MOUTH_CORNER_BEHAVIOR_DRIFT_OR_GAP
- Fallback: Reforzar mouth corner behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0266 — neck_tension
- Definición: Campo operativo para neck tension dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar neck tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar neck tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NECK_TENSION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NECK_TENSION_DRIFT_OR_GAP
- Fallback: Reforzar neck tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0267 — subtext_state
- Definición: Campo operativo para subtext state dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar subtext state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar subtext state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUBTEXT_STATE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SUBTEXT_STATE_DRIFT_OR_GAP
- Fallback: Reforzar subtext state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0268 — emotion_transition_rule
- Definición: Campo operativo para emotion transition rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar emotion transition rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion transition rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_TRANSITION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EMOTION_TRANSITION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar emotion transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0269 — camera_reaction_pattern
- Definición: Campo operativo para camera reaction pattern dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar camera reaction pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera reaction pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_REACTION_PATTERN_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAMERA_REACTION_PATTERN_DRIFT_OR_GAP
- Fallback: Reforzar camera reaction pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0270 — emotion_to_pose_map
- Definición: Campo operativo para emotion to pose map dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar emotion to pose map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion to pose map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_TO_POSE_MAP_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EMOTION_TO_POSE_MAP_DRIFT_OR_GAP
- Fallback: Reforzar emotion to pose map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0271 — walking_rhythm
- Definición: Campo operativo para walking rhythm dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar walking rhythm como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking rhythm como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_RHYTHM_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WALKING_RHYTHM_DRIFT_OR_GAP
- Fallback: Reforzar walking rhythm con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0272 — walking_weight
- Definición: Campo operativo para walking weight dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar walking weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WALKING_WEIGHT_DRIFT_OR_GAP
- Fallback: Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0273 — hip_movement
- Definición: Campo operativo para hip movement dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hip movement como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hip movement como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HIP_MOVEMENT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HIP_MOVEMENT_DRIFT_OR_GAP
- Fallback: Reforzar hip movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0274 — shoulder_countermotion
- Definición: Campo operativo para shoulder countermotion dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shoulder countermotion como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder countermotion como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_COUNTERMOTION_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHOULDER_COUNTERMOTION_DRIFT_OR_GAP
- Fallback: Reforzar shoulder countermotion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0275 — arm_swing
- Definición: Campo operativo para arm swing dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar arm swing como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar arm swing como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARM_SWING_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ARM_SWING_DRIFT_OR_GAP
- Fallback: Reforzar arm swing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0276 — hand_gesture_library
- Definición: Campo operativo para hand gesture library dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hand gesture library como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand gesture library como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_GESTURE_LIBRARY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAND_GESTURE_LIBRARY_DRIFT_OR_GAP
- Fallback: Reforzar hand gesture library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0277 — breathing_visibility
- Definición: Campo operativo para breathing visibility dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar breathing visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar breathing visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BREATHING_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BREATHING_VISIBILITY_DRIFT_OR_GAP
- Fallback: Reforzar breathing visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0278 — pose_energy
- Definición: Campo operativo para pose energy dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar pose energy como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose energy como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_ENERGY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_POSE_ENERGY_DRIFT_OR_GAP
- Fallback: Reforzar pose energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0279 — pose_range
- Definición: Campo operativo para pose range dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar pose range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_RANGE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_POSE_RANGE_DRIFT_OR_GAP
- Fallback: Reforzar pose range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0280 — dance_signature
- Definición: Campo operativo para dance signature dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar dance signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dance signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DANCE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DANCE_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar dance signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0281 — runway_presence
- Definición: Campo operativo para runway presence dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar runway presence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar runway presence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RUNWAY_PRESENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_RUNWAY_PRESENCE_DRIFT_OR_GAP
- Fallback: Reforzar runway presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0282 — camera_presence
- Definición: Campo operativo para camera presence dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar camera presence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera presence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_PRESENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAMERA_PRESENCE_DRIFT_OR_GAP
- Fallback: Reforzar camera presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0283 — micro_action_library
- Definición: Campo operativo para micro action library dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar micro action library como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar micro action library como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICRO_ACTION_LIBRARY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MICRO_ACTION_LIBRARY_DRIFT_OR_GAP
- Fallback: Reforzar micro action library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0284 — video_continuity_lock
- Definición: Campo operativo para video continuity lock dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar video continuity lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video continuity lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_CONTINUITY_LOCK_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VIDEO_CONTINUITY_LOCK_DRIFT_OR_GAP
- Fallback: Reforzar video continuity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0285 — frame_to_frame_identity
- Definición: Campo operativo para frame to frame identity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar frame to frame identity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar frame to frame identity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FRAME_TO_FRAME_IDENTITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FRAME_TO_FRAME_IDENTITY_DRIFT_OR_GAP
- Fallback: Reforzar frame to frame identity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0286 — shot_transition_rule
- Definición: Campo operativo para shot transition rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar shot transition rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shot transition rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOT_TRANSITION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SHOT_TRANSITION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar shot transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0287 — motion_blur_rule
- Definición: Campo operativo para motion blur rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar motion blur rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motion blur rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTION_BLUR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MOTION_BLUR_RULE_DRIFT_OR_GAP
- Fallback: Reforzar motion blur rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0288 — hair_motion_continuity
- Definición: Campo operativo para hair motion continuity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hair motion continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair motion continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_MOTION_CONTINUITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAIR_MOTION_CONTINUITY_DRIFT_OR_GAP
- Fallback: Reforzar hair motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0289 — wardrobe_motion_continuity
- Definición: Campo operativo para wardrobe motion continuity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wardrobe motion continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe motion continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_MOTION_CONTINUITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WARDROBE_MOTION_CONTINUITY_DRIFT_OR_GAP
- Fallback: Reforzar wardrobe motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0290 — voice_body_sync
- Definición: Campo operativo para voice body sync dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar voice body sync como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice body sync como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_BODY_SYNC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VOICE_BODY_SYNC_DRIFT_OR_GAP
- Fallback: Reforzar voice body sync con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0291 — acting_intention_per_shot
- Definición: Campo operativo para acting intention per shot dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar acting intention per shot como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar acting intention per shot como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACTING_INTENTION_PER_SHOT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ACTING_INTENTION_PER_SHOT_DRIFT_OR_GAP
- Fallback: Reforzar acting intention per shot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0292 — clip_complexity_limit
- Definición: Campo operativo para clip complexity limit dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar clip complexity limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clip complexity limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLIP_COMPLEXITY_LIMIT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CLIP_COMPLEXITY_LIMIT_DRIFT_OR_GAP
- Fallback: Reforzar clip complexity limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0293 — video_prompt_timeline
- Definición: Campo operativo para video prompt timeline dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar video prompt timeline como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video prompt timeline como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_PROMPT_TIMELINE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VIDEO_PROMPT_TIMELINE_DRIFT_OR_GAP
- Fallback: Reforzar video prompt timeline con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0294 — rigid_pose_blocker
- Definición: Campo operativo para rigid pose blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar rigid pose blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rigid pose blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RIGID_POSE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_RIGID_POSE_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar rigid pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0295 — fake_expression_blocker
- Definición: Campo operativo para fake expression blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fake expression blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fake expression blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAKE_EXPRESSION_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FAKE_EXPRESSION_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar fake expression blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0296 — morphing_blocker
- Definición: Campo operativo para morphing blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar morphing blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar morphing blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MORPHING_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MORPHING_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar morphing blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0297 — video_identity_jump_blocker
- Definición: Campo operativo para video identity jump blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar video identity jump blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video identity jump blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_IDENTITY_JUMP_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VIDEO_IDENTITY_JUMP_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar video identity jump blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0298 — hands_warp_video_blocker
- Definición: Campo operativo para hands warp video blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hands warp video blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands warp video blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_WARP_VIDEO_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HANDS_WARP_VIDEO_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar hands warp video blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0299 — emotion_mismatch_rule
- Definición: Campo operativo para emotion mismatch rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar emotion mismatch rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion mismatch rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_MISMATCH_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_EMOTION_MISMATCH_RULE_DRIFT_OR_GAP
- Fallback: Reforzar emotion mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0300 — motion_repair_rule
- Definición: Campo operativo para motion repair rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar motion repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motion repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTION_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MOTION_REPAIR_RULE_DRIFT_OR_GAP
- Fallback: Reforzar motion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0301 — video_regression_test
- Definición: Campo operativo para video regression test dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar video regression test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video regression test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_REGRESSION_TEST_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_VIDEO_REGRESSION_TEST_DRIFT_OR_GAP
- Fallback: Reforzar video regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0708 — facs_base_prompt_effect
- Definición: Campo operativo para facs base dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar facs base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar facs base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACS_BASE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACS_BASE_PROMPT_EFFECT
- Fallback: Reforzar facs base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0709 — smile_types_prompt_effect
- Definición: Campo operativo para smile types dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar smile types como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar smile types como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SMILE_TYPES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SMILE_TYPES_PROMPT_EFFECT
- Fallback: Reforzar smile types con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0710 — microgesture_set_prompt_effect
- Definición: Campo operativo para microgesture set dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar microgesture set como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar microgesture set como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICROGESTURE_SET_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICROGESTURE_SET_PROMPT_EFFECT
- Fallback: Reforzar microgesture set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0711 — eye_emotion_map_prompt_effect
- Definición: Campo operativo para eye emotion map dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye emotion map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye emotion map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_EMOTION_MAP_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_EMOTION_MAP_PROMPT_EFFECT
- Fallback: Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0712 — brow_micro_movement_prompt_effect
- Definición: Campo operativo para brow micro movement dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow micro movement como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow micro movement como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_MICRO_MOVEMENT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_MICRO_MOVEMENT_PROMPT_EFFEC
- Fallback: Reforzar brow micro movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0713 — jaw_tension_prompt_effect
- Definición: Campo operativo para jaw tension dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_TENSION_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_TENSION_PROMPT_EFFECT
- Fallback: Reforzar jaw tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0714 — mouth_corner_behavior_prompt_effect
- Definición: Campo operativo para mouth corner behavior dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mouth corner behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mouth corner behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOUTH_CORNER_BEHAVIOR_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOUTH_CORNER_BEHAVIOR_PROMPT_EFF
- Fallback: Reforzar mouth corner behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0715 — neck_tension_prompt_effect
- Definición: Campo operativo para neck tension dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar neck tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar neck tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NECK_TENSION_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NECK_TENSION_PROMPT_EFFECT
- Fallback: Reforzar neck tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0716 — subtext_state_prompt_effect
- Definición: Campo operativo para subtext state dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar subtext state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar subtext state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUBTEXT_STATE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUBTEXT_STATE_PROMPT_EFFECT
- Fallback: Reforzar subtext state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0717 — emotion_transition_rule_prompt_effect
- Definición: Campo operativo para emotion transition rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion transition rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion transition rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_TRANSITION_RULE_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_TRANSITION_RULE_PROMPT_E
- Fallback: Reforzar emotion transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0718 — camera_reaction_pattern_prompt_effect
- Definición: Campo operativo para camera reaction pattern dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera reaction pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera reaction pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_REACTION_PATTERN_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_REACTION_PATTERN_PROMPT_E
- Fallback: Reforzar camera reaction pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0719 — emotion_to_pose_map_prompt_effect
- Definición: Campo operativo para emotion to pose map dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion to pose map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion to pose map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_TO_POSE_MAP_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_TO_POSE_MAP_PROMPT_EFFEC
- Fallback: Reforzar emotion to pose map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0720 — walking_rhythm_prompt_effect
- Definición: Campo operativo para walking rhythm dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking rhythm como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking rhythm como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_RHYTHM_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_RHYTHM_PROMPT_EFFECT
- Fallback: Reforzar walking rhythm con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0721 — walking_weight_prompt_effect
- Definición: Campo operativo para walking weight dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_WEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_WEIGHT_PROMPT_EFFECT
- Fallback: Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0722 — hip_movement_prompt_effect
- Definición: Campo operativo para hip movement dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hip movement como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hip movement como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HIP_MOVEMENT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HIP_MOVEMENT_PROMPT_EFFECT
- Fallback: Reforzar hip movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0723 — shoulder_countermotion_prompt_effect
- Definición: Campo operativo para shoulder countermotion dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder countermotion como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder countermotion como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_COUNTERMOTION_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_COUNTERMOTION_PROMPT_EF
- Fallback: Reforzar shoulder countermotion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0724 — arm_swing_prompt_effect
- Definición: Campo operativo para arm swing dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar arm swing como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar arm swing como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARM_SWING_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARM_SWING_PROMPT_EFFECT
- Fallback: Reforzar arm swing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0725 — hand_gesture_library_prompt_effect
- Definición: Campo operativo para hand gesture library dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand gesture library como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand gesture library como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_GESTURE_LIBRARY_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_GESTURE_LIBRARY_PROMPT_EFFE
- Fallback: Reforzar hand gesture library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0726 — breathing_visibility_prompt_effect
- Definición: Campo operativo para breathing visibility dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar breathing visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar breathing visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BREATHING_VISIBILITY_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BREATHING_VISIBILITY_PROMPT_EFFE
- Fallback: Reforzar breathing visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0727 — pose_energy_prompt_effect
- Definición: Campo operativo para pose energy dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose energy como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose energy como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_ENERGY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_ENERGY_PROMPT_EFFECT
- Fallback: Reforzar pose energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0728 — pose_range_prompt_effect
- Definición: Campo operativo para pose range dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_RANGE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_RANGE_PROMPT_EFFECT
- Fallback: Reforzar pose range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0729 — dance_signature_prompt_effect
- Definición: Campo operativo para dance signature dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dance signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dance signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DANCE_SIGNATURE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DANCE_SIGNATURE_PROMPT_EFFECT
- Fallback: Reforzar dance signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0730 — runway_presence_prompt_effect
- Definición: Campo operativo para runway presence dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar runway presence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar runway presence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RUNWAY_PRESENCE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RUNWAY_PRESENCE_PROMPT_EFFECT
- Fallback: Reforzar runway presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0731 — camera_presence_prompt_effect
- Definición: Campo operativo para camera presence dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera presence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera presence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_PRESENCE_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_PRESENCE_PROMPT_EFFECT
- Fallback: Reforzar camera presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0732 — micro_action_library_prompt_effect
- Definición: Campo operativo para micro action library dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar micro action library como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar micro action library como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICRO_ACTION_LIBRARY_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICRO_ACTION_LIBRARY_PROMPT_EFFE
- Fallback: Reforzar micro action library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0733 — video_continuity_lock_prompt_effect
- Definición: Campo operativo para video continuity lock dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video continuity lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video continuity lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_CONTINUITY_LOCK_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_CONTINUITY_LOCK_PROMPT_EFF
- Fallback: Reforzar video continuity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0734 — frame_to_frame_identity_prompt_effect
- Definición: Campo operativo para frame to frame identity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar frame to frame identity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar frame to frame identity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FRAME_TO_FRAME_IDENTITY_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FRAME_TO_FRAME_IDENTITY_PROMPT_E
- Fallback: Reforzar frame to frame identity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0735 — shot_transition_rule_prompt_effect
- Definición: Campo operativo para shot transition rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shot transition rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shot transition rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOT_TRANSITION_RULE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOT_TRANSITION_RULE_PROMPT_EFFE
- Fallback: Reforzar shot transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0736 — motion_blur_rule_prompt_effect
- Definición: Campo operativo para motion blur rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motion blur rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motion blur rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTION_BLUR_RULE_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTION_BLUR_RULE_PROMPT_EFFECT
- Fallback: Reforzar motion blur rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0737 — hair_motion_continuity_prompt_effect
- Definición: Campo operativo para hair motion continuity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair motion continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair motion continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_MOTION_CONTINUITY_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_MOTION_CONTINUITY_PROMPT_EF
- Fallback: Reforzar hair motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0738 — wardrobe_motion_continuity_prompt_effect
- Definición: Campo operativo para wardrobe motion continuity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe motion continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe motion continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_MOTION_CONTINUITY_P_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_MOTION_CONTINUITY_PROMP
- Fallback: Reforzar wardrobe motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_0739 — voice_body_sync_prompt_effect
- Definición: Campo operativo para voice body sync dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice body sync como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice body sync como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_BODY_SYNC_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_BODY_SYNC_PROMPT_EFFECT
- Fallback: Reforzar voice body sync con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0740 — acting_intention_per_shot_prompt_effect
- Definición: Campo operativo para acting intention per shot dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar acting intention per shot como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar acting intention per shot como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACTING_INTENTION_PER_SHOT_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACTING_INTENTION_PER_SHOT_PROMPT
- Fallback: Reforzar acting intention per shot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0741 — clip_complexity_limit_prompt_effect
- Definición: Campo operativo para clip complexity limit dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clip complexity limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clip complexity limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLIP_COMPLEXITY_LIMIT_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLIP_COMPLEXITY_LIMIT_PROMPT_EFF
- Fallback: Reforzar clip complexity limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0742 — video_prompt_timeline_prompt_effect
- Definición: Campo operativo para video prompt timeline dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video prompt timeline como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video prompt timeline como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_PROMPT_TIMELINE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_PROMPT_TIMELINE_PROMPT_EFF
- Fallback: Reforzar video prompt timeline con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0743 — rigid_pose_blocker_prompt_effect
- Definición: Campo operativo para rigid pose blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rigid pose blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rigid pose blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RIGID_POSE_BLOCKER_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RIGID_POSE_BLOCKER_PROMPT_EFFECT
- Fallback: Reforzar rigid pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0744 — fake_expression_blocker_prompt_effect
- Definición: Campo operativo para fake expression blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fake expression blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fake expression blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAKE_EXPRESSION_BLOCKER_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAKE_EXPRESSION_BLOCKER_PROMPT_E
- Fallback: Reforzar fake expression blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0745 — morphing_blocker_prompt_effect
- Definición: Campo operativo para morphing blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar morphing blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar morphing blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MORPHING_BLOCKER_PROMPT_EFFE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MORPHING_BLOCKER_PROMPT_EFFECT
- Fallback: Reforzar morphing blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0746 — video_identity_jump_blocker_prompt_effect
- Definición: Campo operativo para video identity jump blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video identity jump blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video identity jump blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_IDENTITY_JUMP_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_IDENTITY_JUMP_BLOCKER_PROM
- Fallback: Reforzar video identity jump blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0747 — hands_warp_video_blocker_prompt_effect
- Definición: Campo operativo para hands warp video blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands warp video blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands warp video blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_WARP_VIDEO_BLOCKER_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_WARP_VIDEO_BLOCKER_PROMPT_
- Fallback: Reforzar hands warp video blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0748 — emotion_mismatch_rule_prompt_effect
- Definición: Campo operativo para emotion mismatch rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion mismatch rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion mismatch rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_MISMATCH_RULE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_MISMATCH_RULE_PROMPT_EFF
- Fallback: Reforzar emotion mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0749 — motion_repair_rule_prompt_effect
- Definición: Campo operativo para motion repair rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motion repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motion repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTION_REPAIR_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTION_REPAIR_RULE_PROMPT_EFFECT
- Fallback: Reforzar motion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0750 — video_regression_test_prompt_effect
- Definición: Campo operativo para video regression test dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video regression test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video regression test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_REGRESSION_TEST_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_REGRESSION_TEST_PROMPT_EFF
- Fallback: Reforzar video regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1157 — facs_base_qa_matrix
- Definición: Campo operativo para facs base dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar facs base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar facs base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACS_BASE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACS_BASE_QA_MATRIX
- Fallback: Reforzar facs base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1158 — smile_types_qa_matrix
- Definición: Campo operativo para smile types dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar smile types como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar smile types como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SMILE_TYPES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SMILE_TYPES_QA_MATRIX
- Fallback: Reforzar smile types con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1159 — microgesture_set_qa_matrix
- Definición: Campo operativo para microgesture set dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar microgesture set como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar microgesture set como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICROGESTURE_SET_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICROGESTURE_SET_QA_MATRIX
- Fallback: Reforzar microgesture set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1160 — eye_emotion_map_qa_matrix
- Definición: Campo operativo para eye emotion map dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye emotion map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye emotion map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_EMOTION_MAP_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_EMOTION_MAP_QA_MATRIX
- Fallback: Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1161 — brow_micro_movement_qa_matrix
- Definición: Campo operativo para brow micro movement dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow micro movement como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow micro movement como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_MICRO_MOVEMENT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_MICRO_MOVEMENT_QA_MATRIX
- Fallback: Reforzar brow micro movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1162 — jaw_tension_qa_matrix
- Definición: Campo operativo para jaw tension dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_TENSION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_TENSION_QA_MATRIX
- Fallback: Reforzar jaw tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1163 — mouth_corner_behavior_qa_matrix
- Definición: Campo operativo para mouth corner behavior dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mouth corner behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mouth corner behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOUTH_CORNER_BEHAVIOR_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOUTH_CORNER_BEHAVIOR_QA_MATRIX
- Fallback: Reforzar mouth corner behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1164 — neck_tension_qa_matrix
- Definición: Campo operativo para neck tension dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar neck tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar neck tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NECK_TENSION_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NECK_TENSION_QA_MATRIX
- Fallback: Reforzar neck tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1165 — subtext_state_qa_matrix
- Definición: Campo operativo para subtext state dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar subtext state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar subtext state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUBTEXT_STATE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUBTEXT_STATE_QA_MATRIX
- Fallback: Reforzar subtext state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1166 — emotion_transition_rule_qa_matrix
- Definición: Campo operativo para emotion transition rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion transition rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion transition rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_TRANSITION_RULE_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_TRANSITION_RULE_QA_MATRI
- Fallback: Reforzar emotion transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1167 — camera_reaction_pattern_qa_matrix
- Definición: Campo operativo para camera reaction pattern dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera reaction pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera reaction pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_REACTION_PATTERN_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_REACTION_PATTERN_QA_MATRI
- Fallback: Reforzar camera reaction pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1168 — emotion_to_pose_map_qa_matrix
- Definición: Campo operativo para emotion to pose map dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion to pose map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion to pose map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_TO_POSE_MAP_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_TO_POSE_MAP_QA_MATRIX
- Fallback: Reforzar emotion to pose map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1169 — walking_rhythm_qa_matrix
- Definición: Campo operativo para walking rhythm dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking rhythm como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking rhythm como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_RHYTHM_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_RHYTHM_QA_MATRIX
- Fallback: Reforzar walking rhythm con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1170 — walking_weight_qa_matrix
- Definición: Campo operativo para walking weight dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_WEIGHT_QA_MATRIX
- Fallback: Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1171 — hip_movement_qa_matrix
- Definición: Campo operativo para hip movement dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hip movement como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hip movement como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HIP_MOVEMENT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HIP_MOVEMENT_QA_MATRIX
- Fallback: Reforzar hip movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1172 — shoulder_countermotion_qa_matrix
- Definición: Campo operativo para shoulder countermotion dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder countermotion como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder countermotion como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_COUNTERMOTION_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_COUNTERMOTION_QA_MATRIX
- Fallback: Reforzar shoulder countermotion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1173 — arm_swing_qa_matrix
- Definición: Campo operativo para arm swing dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar arm swing como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar arm swing como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARM_SWING_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARM_SWING_QA_MATRIX
- Fallback: Reforzar arm swing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1174 — hand_gesture_library_qa_matrix
- Definición: Campo operativo para hand gesture library dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand gesture library como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand gesture library como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_GESTURE_LIBRARY_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_GESTURE_LIBRARY_QA_MATRIX
- Fallback: Reforzar hand gesture library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1175 — breathing_visibility_qa_matrix
- Definición: Campo operativo para breathing visibility dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar breathing visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar breathing visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BREATHING_VISIBILITY_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BREATHING_VISIBILITY_QA_MATRIX
- Fallback: Reforzar breathing visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1176 — pose_energy_qa_matrix
- Definición: Campo operativo para pose energy dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose energy como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose energy como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_ENERGY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_ENERGY_QA_MATRIX
- Fallback: Reforzar pose energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1177 — pose_range_qa_matrix
- Definición: Campo operativo para pose range dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_RANGE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_RANGE_QA_MATRIX
- Fallback: Reforzar pose range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1178 — dance_signature_qa_matrix
- Definición: Campo operativo para dance signature dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dance signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dance signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DANCE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DANCE_SIGNATURE_QA_MATRIX
- Fallback: Reforzar dance signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1179 — runway_presence_qa_matrix
- Definición: Campo operativo para runway presence dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar runway presence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar runway presence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RUNWAY_PRESENCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RUNWAY_PRESENCE_QA_MATRIX
- Fallback: Reforzar runway presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1180 — camera_presence_qa_matrix
- Definición: Campo operativo para camera presence dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera presence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera presence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_PRESENCE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_PRESENCE_QA_MATRIX
- Fallback: Reforzar camera presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1181 — micro_action_library_qa_matrix
- Definición: Campo operativo para micro action library dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar micro action library como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar micro action library como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICRO_ACTION_LIBRARY_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICRO_ACTION_LIBRARY_QA_MATRIX
- Fallback: Reforzar micro action library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1182 — video_continuity_lock_qa_matrix
- Definición: Campo operativo para video continuity lock dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video continuity lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video continuity lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_CONTINUITY_LOCK_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_CONTINUITY_LOCK_QA_MATRIX
- Fallback: Reforzar video continuity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1183 — frame_to_frame_identity_qa_matrix
- Definición: Campo operativo para frame to frame identity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar frame to frame identity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar frame to frame identity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FRAME_TO_FRAME_IDENTITY_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FRAME_TO_FRAME_IDENTITY_QA_MATRI
- Fallback: Reforzar frame to frame identity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1184 — shot_transition_rule_qa_matrix
- Definición: Campo operativo para shot transition rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shot transition rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shot transition rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOT_TRANSITION_RULE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOT_TRANSITION_RULE_QA_MATRIX
- Fallback: Reforzar shot transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1185 — motion_blur_rule_qa_matrix
- Definición: Campo operativo para motion blur rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motion blur rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motion blur rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTION_BLUR_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTION_BLUR_RULE_QA_MATRIX
- Fallback: Reforzar motion blur rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1186 — hair_motion_continuity_qa_matrix
- Definición: Campo operativo para hair motion continuity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair motion continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair motion continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_MOTION_CONTINUITY_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_MOTION_CONTINUITY_QA_MATRIX
- Fallback: Reforzar hair motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1187 — wardrobe_motion_continuity_qa_matrix
- Definición: Campo operativo para wardrobe motion continuity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe motion continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe motion continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_MOTION_CONTINUITY_Q_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_MOTION_CONTINUITY_QA_MA
- Fallback: Reforzar wardrobe motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1188 — voice_body_sync_qa_matrix
- Definición: Campo operativo para voice body sync dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice body sync como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice body sync como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_BODY_SYNC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_BODY_SYNC_QA_MATRIX
- Fallback: Reforzar voice body sync con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1189 — acting_intention_per_shot_qa_matrix
- Definición: Campo operativo para acting intention per shot dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar acting intention per shot como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar acting intention per shot como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACTING_INTENTION_PER_SHOT_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACTING_INTENTION_PER_SHOT_QA_MAT
- Fallback: Reforzar acting intention per shot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1190 — clip_complexity_limit_qa_matrix
- Definición: Campo operativo para clip complexity limit dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clip complexity limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clip complexity limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLIP_COMPLEXITY_LIMIT_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLIP_COMPLEXITY_LIMIT_QA_MATRIX
- Fallback: Reforzar clip complexity limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1191 — video_prompt_timeline_qa_matrix
- Definición: Campo operativo para video prompt timeline dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video prompt timeline como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video prompt timeline como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_PROMPT_TIMELINE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_PROMPT_TIMELINE_QA_MATRIX
- Fallback: Reforzar video prompt timeline con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1192 — rigid_pose_blocker_qa_matrix
- Definición: Campo operativo para rigid pose blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rigid pose blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rigid pose blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RIGID_POSE_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RIGID_POSE_BLOCKER_QA_MATRIX
- Fallback: Reforzar rigid pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1193 — fake_expression_blocker_qa_matrix
- Definición: Campo operativo para fake expression blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fake expression blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fake expression blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAKE_EXPRESSION_BLOCKER_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAKE_EXPRESSION_BLOCKER_QA_MATRI
- Fallback: Reforzar fake expression blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1194 — morphing_blocker_qa_matrix
- Definición: Campo operativo para morphing blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar morphing blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar morphing blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MORPHING_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MORPHING_BLOCKER_QA_MATRIX
- Fallback: Reforzar morphing blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1195 — video_identity_jump_blocker_qa_matrix
- Definición: Campo operativo para video identity jump blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video identity jump blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video identity jump blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_IDENTITY_JUMP_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_IDENTITY_JUMP_BLOCKER_QA_M
- Fallback: Reforzar video identity jump blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1196 — hands_warp_video_blocker_qa_matrix
- Definición: Campo operativo para hands warp video blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands warp video blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands warp video blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_WARP_VIDEO_BLOCKER_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_WARP_VIDEO_BLOCKER_QA_MATR
- Fallback: Reforzar hands warp video blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1197 — emotion_mismatch_rule_qa_matrix
- Definición: Campo operativo para emotion mismatch rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion mismatch rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion mismatch rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_MISMATCH_RULE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_MISMATCH_RULE_QA_MATRIX
- Fallback: Reforzar emotion mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1198 — motion_repair_rule_qa_matrix
- Definición: Campo operativo para motion repair rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motion repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motion repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTION_REPAIR_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTION_REPAIR_RULE_QA_MATRIX
- Fallback: Reforzar motion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1199 — video_regression_test_qa_matrix
- Definición: Campo operativo para video regression test dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video regression test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video regression test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_REGRESSION_TEST_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_REGRESSION_TEST_QA_MATRIX
- Fallback: Reforzar video regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1606 — facs_base_vendor_repair
- Definición: Campo operativo para facs base dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar facs base como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar facs base como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FACS_BASE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FACS_BASE_VENDOR_REPAIR
- Fallback: Reforzar facs base con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1607 — smile_types_vendor_repair
- Definición: Campo operativo para smile types dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar smile types como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar smile types como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SMILE_TYPES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SMILE_TYPES_VENDOR_REPAIR
- Fallback: Reforzar smile types con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1608 — microgesture_set_vendor_repair
- Definición: Campo operativo para microgesture set dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar microgesture set como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar microgesture set como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICROGESTURE_SET_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICROGESTURE_SET_VENDOR_REPAIR
- Fallback: Reforzar microgesture set con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1609 — eye_emotion_map_vendor_repair
- Definición: Campo operativo para eye emotion map dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar eye emotion map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar eye emotion map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EYE_EMOTION_MAP_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EYE_EMOTION_MAP_VENDOR_REPAIR
- Fallback: Reforzar eye emotion map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1610 — brow_micro_movement_vendor_repair
- Definición: Campo operativo para brow micro movement dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brow micro movement como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brow micro movement como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BROW_MICRO_MOVEMENT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BROW_MICRO_MOVEMENT_VENDOR_REPAI
- Fallback: Reforzar brow micro movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1611 — jaw_tension_vendor_repair
- Definición: Campo operativo para jaw tension dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jaw tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jaw tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JAW_TENSION_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JAW_TENSION_VENDOR_REPAIR
- Fallback: Reforzar jaw tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1612 — mouth_corner_behavior_vendor_repair
- Definición: Campo operativo para mouth corner behavior dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar mouth corner behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar mouth corner behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOUTH_CORNER_BEHAVIOR_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOUTH_CORNER_BEHAVIOR_VENDOR_REP
- Fallback: Reforzar mouth corner behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1613 — neck_tension_vendor_repair
- Definición: Campo operativo para neck tension dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar neck tension como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar neck tension como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NECK_TENSION_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NECK_TENSION_VENDOR_REPAIR
- Fallback: Reforzar neck tension con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1614 — subtext_state_vendor_repair
- Definición: Campo operativo para subtext state dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar subtext state como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar subtext state como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUBTEXT_STATE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUBTEXT_STATE_VENDOR_REPAIR
- Fallback: Reforzar subtext state con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1615 — emotion_transition_rule_vendor_repair
- Definición: Campo operativo para emotion transition rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion transition rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion transition rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_TRANSITION_RULE_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_TRANSITION_RULE_VENDOR_R
- Fallback: Reforzar emotion transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1616 — camera_reaction_pattern_vendor_repair
- Definición: Campo operativo para camera reaction pattern dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera reaction pattern como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera reaction pattern como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_REACTION_PATTERN_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_REACTION_PATTERN_VENDOR_R
- Fallback: Reforzar camera reaction pattern con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1617 — emotion_to_pose_map_vendor_repair
- Definición: Campo operativo para emotion to pose map dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion to pose map como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion to pose map como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_TO_POSE_MAP_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_TO_POSE_MAP_VENDOR_REPAI
- Fallback: Reforzar emotion to pose map con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1618 — walking_rhythm_vendor_repair
- Definición: Campo operativo para walking rhythm dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking rhythm como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking rhythm como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_RHYTHM_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_RHYTHM_VENDOR_REPAIR
- Fallback: Reforzar walking rhythm con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1619 — walking_weight_vendor_repair
- Definición: Campo operativo para walking weight dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar walking weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar walking weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WALKING_WEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WALKING_WEIGHT_VENDOR_REPAIR
- Fallback: Reforzar walking weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1620 — hip_movement_vendor_repair
- Definición: Campo operativo para hip movement dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hip movement como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hip movement como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HIP_MOVEMENT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HIP_MOVEMENT_VENDOR_REPAIR
- Fallback: Reforzar hip movement con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1621 — shoulder_countermotion_vendor_repair
- Definición: Campo operativo para shoulder countermotion dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shoulder countermotion como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shoulder countermotion como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOULDER_COUNTERMOTION_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOULDER_COUNTERMOTION_VENDOR_RE
- Fallback: Reforzar shoulder countermotion con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1622 — arm_swing_vendor_repair
- Definición: Campo operativo para arm swing dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar arm swing como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar arm swing como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ARM_SWING_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ARM_SWING_VENDOR_REPAIR
- Fallback: Reforzar arm swing con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1623 — hand_gesture_library_vendor_repair
- Definición: Campo operativo para hand gesture library dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand gesture library como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand gesture library como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_GESTURE_LIBRARY_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_GESTURE_LIBRARY_VENDOR_REPA
- Fallback: Reforzar hand gesture library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1624 — breathing_visibility_vendor_repair
- Definición: Campo operativo para breathing visibility dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar breathing visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar breathing visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BREATHING_VISIBILITY_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BREATHING_VISIBILITY_VENDOR_REPA
- Fallback: Reforzar breathing visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1625 — pose_energy_vendor_repair
- Definición: Campo operativo para pose energy dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose energy como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose energy como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_ENERGY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_ENERGY_VENDOR_REPAIR
- Fallback: Reforzar pose energy con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1626 — pose_range_vendor_repair
- Definición: Campo operativo para pose range dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose range como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose range como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_RANGE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_RANGE_VENDOR_REPAIR
- Fallback: Reforzar pose range con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1627 — dance_signature_vendor_repair
- Definición: Campo operativo para dance signature dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar dance signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar dance signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DANCE_SIGNATURE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DANCE_SIGNATURE_VENDOR_REPAIR
- Fallback: Reforzar dance signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1628 — runway_presence_vendor_repair
- Definición: Campo operativo para runway presence dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar runway presence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar runway presence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RUNWAY_PRESENCE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RUNWAY_PRESENCE_VENDOR_REPAIR
- Fallback: Reforzar runway presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1629 — camera_presence_vendor_repair
- Definición: Campo operativo para camera presence dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera presence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera presence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_PRESENCE_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_PRESENCE_VENDOR_REPAIR
- Fallback: Reforzar camera presence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1630 — micro_action_library_vendor_repair
- Definición: Campo operativo para micro action library dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar micro action library como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar micro action library como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MICRO_ACTION_LIBRARY_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MICRO_ACTION_LIBRARY_VENDOR_REPA
- Fallback: Reforzar micro action library con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1631 — video_continuity_lock_vendor_repair
- Definición: Campo operativo para video continuity lock dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video continuity lock como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video continuity lock como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_CONTINUITY_LOCK_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_CONTINUITY_LOCK_VENDOR_REP
- Fallback: Reforzar video continuity lock con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1632 — frame_to_frame_identity_vendor_repair
- Definición: Campo operativo para frame to frame identity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar frame to frame identity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar frame to frame identity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FRAME_TO_FRAME_IDENTITY_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FRAME_TO_FRAME_IDENTITY_VENDOR_R
- Fallback: Reforzar frame to frame identity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1633 — shot_transition_rule_vendor_repair
- Definición: Campo operativo para shot transition rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar shot transition rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar shot transition rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SHOT_TRANSITION_RULE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SHOT_TRANSITION_RULE_VENDOR_REPA
- Fallback: Reforzar shot transition rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1634 — motion_blur_rule_vendor_repair
- Definición: Campo operativo para motion blur rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motion blur rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motion blur rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTION_BLUR_RULE_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTION_BLUR_RULE_VENDOR_REPAIR
- Fallback: Reforzar motion blur rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1635 — hair_motion_continuity_vendor_repair
- Definición: Campo operativo para hair motion continuity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hair motion continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hair motion continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAIR_MOTION_CONTINUITY_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAIR_MOTION_CONTINUITY_VENDOR_RE
- Fallback: Reforzar hair motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1636 — wardrobe_motion_continuity_vendor_repair
- Definición: Campo operativo para wardrobe motion continuity dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe motion continuity como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe motion continuity como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_MOTION_CONTINUITY_V_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_MOTION_CONTINUITY_VENDO
- Fallback: Reforzar wardrobe motion continuity con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VOICE_1637 — voice_body_sync_vendor_repair
- Definición: Campo operativo para voice body sync dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar voice body sync como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar voice body sync como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VOICE_BODY_SYNC_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VOICE_BODY_SYNC_VENDOR_REPAIR
- Fallback: Reforzar voice body sync con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1638 — acting_intention_per_shot_vendor_repair
- Definición: Campo operativo para acting intention per shot dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar acting intention per shot como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar acting intention per shot como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACTING_INTENTION_PER_SHOT_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACTING_INTENTION_PER_SHOT_VENDOR
- Fallback: Reforzar acting intention per shot con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1639 — clip_complexity_limit_vendor_repair
- Definición: Campo operativo para clip complexity limit dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar clip complexity limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar clip complexity limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CLIP_COMPLEXITY_LIMIT_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CLIP_COMPLEXITY_LIMIT_VENDOR_REP
- Fallback: Reforzar clip complexity limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1640 — video_prompt_timeline_vendor_repair
- Definición: Campo operativo para video prompt timeline dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video prompt timeline como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video prompt timeline como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_PROMPT_TIMELINE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_PROMPT_TIMELINE_VENDOR_REP
- Fallback: Reforzar video prompt timeline con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1641 — rigid_pose_blocker_vendor_repair
- Definición: Campo operativo para rigid pose blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar rigid pose blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar rigid pose blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_RIGID_POSE_BLOCKER_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_RIGID_POSE_BLOCKER_VENDOR_REPAIR
- Fallback: Reforzar rigid pose blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1642 — fake_expression_blocker_vendor_repair
- Definición: Campo operativo para fake expression blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fake expression blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fake expression blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FAKE_EXPRESSION_BLOCKER_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FAKE_EXPRESSION_BLOCKER_VENDOR_R
- Fallback: Reforzar fake expression blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1643 — morphing_blocker_vendor_repair
- Definición: Campo operativo para morphing blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar morphing blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar morphing blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MORPHING_BLOCKER_VENDOR_REPA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MORPHING_BLOCKER_VENDOR_REPAIR
- Fallback: Reforzar morphing blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1644 — video_identity_jump_blocker_vendor_repair
- Definición: Campo operativo para video identity jump blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video identity jump blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video identity jump blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_IDENTITY_JUMP_BLOCKER__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_IDENTITY_JUMP_BLOCKER_VEND
- Fallback: Reforzar video identity jump blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1645 — hands_warp_video_blocker_vendor_repair
- Definición: Campo operativo para hands warp video blocker dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hands warp video blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hands warp video blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HANDS_WARP_VIDEO_BLOCKER_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HANDS_WARP_VIDEO_BLOCKER_VENDOR_
- Fallback: Reforzar hands warp video blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1646 — emotion_mismatch_rule_vendor_repair
- Definición: Campo operativo para emotion mismatch rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar emotion mismatch rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar emotion mismatch rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_EMOTION_MISMATCH_RULE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_EMOTION_MISMATCH_RULE_VENDOR_REP
- Fallback: Reforzar emotion mismatch rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1647 — motion_repair_rule_vendor_repair
- Definición: Campo operativo para motion repair rule dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar motion repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar motion repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MOTION_REPAIR_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MOTION_REPAIR_RULE_VENDOR_REPAIR
- Fallback: Reforzar motion repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1648 — video_regression_test_vendor_repair
- Definición: Campo operativo para video regression test dentro de Acting, FACS, microgestos, pose, caminada y continuidad de video. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar video regression test como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar video regression test como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_VIDEO_REGRESSION_TEST_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_VIDEO_REGRESSION_TEST_VENDOR_REP
- Fallback: Reforzar video regression test con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
