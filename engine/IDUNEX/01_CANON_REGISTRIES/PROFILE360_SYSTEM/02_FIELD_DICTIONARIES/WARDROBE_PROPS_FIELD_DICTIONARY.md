## Phase 3 file-level inheritance
inherits = GLOBAL_FIELD_DICTIONARY_RULES#GLOBAL_ALLOWED_FORBIDDEN_DEPENDS_AFFECTS
field_specific_delta_required = true

# Perfil360 Field Dictionary — Wardrobe, bodywear editorial adulto, props, materiales y física textil

**Motor:** IDUNEX_MOTOR_v1.0.0  
**Estado interno:** prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE  
**ENGINE_RELEASE_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**PACKAGE_GENERATION_DATE:** NEUTRALIZED_ACTIVE_SCOPE  
**Uso:** base central de conocimiento, generación, actualización, auditoría y reparación de proyectos IDUNEX para PROJECT_BRAND_ENTITY.  
**Regla cero:** este archivo no es resumen. Es runtime operativo. Si una instrucción, campo, test o política no puede afectar una salida real, debe convertirse en regla ejecutable o eliminarse del runtime.


| Field ID | Campo | Grupo | Lock | QA | Fallback |
|---|---|---|---|---|---|
| `P360_WARDROBE_0302` | `wardrobe_signature` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wardrobe signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0303` | `color_palette` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COLOR_PALETTE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar color palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0304` | `silhouette_preference` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SILHOUETTE_PREFERENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar silhouette preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0305` | `fabric_preferences` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_PREFERENCES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fabric preferences con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0306` | `fabric_weight` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fabric weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0307` | `fabric_texture` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_TEXTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fabric texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0308` | `fit_rules` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FIT_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar fit rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0309` | `seam_visibility` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SEAM_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar seam visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0310` | `drape_behavior` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DRAPE_BEHAVIOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar drape behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0311` | `wrinkle_logic` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRINKLE_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wrinkle logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0312` | `support_physics` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUPPORT_PHYSICS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar support physics con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0313` | `layering_logic` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LAYERING_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar layering logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0314` | `season_rule` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SEASON_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar season rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0315` | `occasion_rule` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OCCASION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar occasion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0316` | `body_shape_fit_rule` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_SHAPE_FIT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar body shape fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0317` | `wardrobe_story_logic` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_STORY_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wardrobe story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0318` | `bodywear_editorial_limits` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODYWEAR_EDITORIAL_LIMITS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar bodywear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0319` | `swimwear_editorial_limits` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SWIMWEAR_EDITORIAL_LIMITS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar swimwear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0320` | `lingerie_non_explicit_rule` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LINGERIE_NON_EXPLICIT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar lingerie non explicit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0321` | `adult_context_rule` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_CONTEXT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar adult context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0322` | `no_exploitation_rule` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_EXPLOITATION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar no exploitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0323` | `camera_angle_safety` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_ANGLE_SAFETY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar camera angle safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0324` | `pose_safety` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_SAFETY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar pose safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0325` | `styling_alternative_rule` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STYLING_ALTERNATIVE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar styling alternative rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_0326` | `commercial_safe_rewrite` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMMERCIAL_SAFE_REWRITE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar commercial safe rewrite con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0327` | `accessory_rules` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCESSORY_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar accessory rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0328` | `jewelry_limit` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JEWELRY_LIMIT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar jewelry limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0329` | `prop_material` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_MATERIAL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar prop material con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0330` | `prop_weight` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar prop weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0331` | `prop_scale` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar prop scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0332` | `hand_object_contact` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_OBJECT_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0333` | `object_shadow_rule` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_SHADOW_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar object shadow rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_0334` | `brand_logo_restrictions` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_RESTRICTIONS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar brand logo restrictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0335` | `prop_scene_coherence` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_SCENE_COHERENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar prop scene coherence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0336` | `object_continuity_video` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_CONTINUITY_VIDEO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar object continuity video con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0337` | `prop_lineage_rule` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_LINEAGE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar prop lineage rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0338` | `floating_cloth_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLOATING_CLOTH_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar floating cloth blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0339` | `texture_flat_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEXTURE_FLAT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar texture flat blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0340` | `wrong_style_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_STYLE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wrong style blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_0341` | `brand_logo_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar brand logo blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0342` | `unsupported_bodywear_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UNSUPPORTED_BODYWEAR_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar unsupported bodywear blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0343` | `prop_physics_blocker` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_PHYSICS_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar prop physics blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0344` | `wardrobe_identity_drift_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_IDENTITY_DRIFT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar wardrobe identity drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0345` | `material_repair_rule` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MATERIAL_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar. | Reforzar material repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0751` | `wardrobe_signature_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_SIGNATURE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0752` | `color_palette_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COLOR_PALETTE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar color palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0753` | `silhouette_preference_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SILHOUETTE_PREFERENCE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar silhouette preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0754` | `fabric_preferences_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_PREFERENCES_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric preferences con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0755` | `fabric_weight_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_WEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0756` | `fabric_texture_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_TEXTURE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0757` | `fit_rules_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FIT_RULES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fit rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0758` | `seam_visibility_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SEAM_VISIBILITY_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar seam visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0759` | `drape_behavior_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DRAPE_BEHAVIOR_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar drape behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0760` | `wrinkle_logic_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRINKLE_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrinkle logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0761` | `support_physics_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUPPORT_PHYSICS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar support physics con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0762` | `layering_logic_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LAYERING_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar layering logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0763` | `season_rule_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SEASON_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar season rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0764` | `occasion_rule_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OCCASION_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar occasion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0765` | `body_shape_fit_rule_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_SHAPE_FIT_RULE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body shape fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0766` | `wardrobe_story_logic_prompt_effect` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_STORY_LOGIC_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0767` | `bodywear_editorial_limits_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODYWEAR_EDITORIAL_LIMITS_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar bodywear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0768` | `swimwear_editorial_limits_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SWIMWEAR_EDITORIAL_LIMITS_PR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar swimwear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0769` | `lingerie_non_explicit_rule_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LINGERIE_NON_EXPLICIT_RULE_P_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lingerie non explicit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0770` | `adult_context_rule_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_CONTEXT_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0771` | `no_exploitation_rule_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_EXPLOITATION_RULE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no exploitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_0772` | `camera_angle_safety_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_ANGLE_SAFETY_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera angle safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_0773` | `pose_safety_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_SAFETY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0774` | `styling_alternative_rule_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STYLING_ALTERNATIVE_RULE_PRO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar styling alternative rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_0775` | `commercial_safe_rewrite_prompt_effect` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMMERCIAL_SAFE_REWRITE_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar commercial safe rewrite con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0776` | `accessory_rules_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCESSORY_RULES_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accessory rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0777` | `jewelry_limit_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JEWELRY_LIMIT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jewelry limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0778` | `prop_material_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_MATERIAL_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop material con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0779` | `prop_weight_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_WEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0780` | `prop_scale_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0781` | `hand_object_contact_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_OBJECT_CONTACT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_0782` | `object_shadow_rule_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_SHADOW_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object shadow rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_0783` | `brand_logo_restrictions_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_RESTRICTIONS_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo restrictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_0784` | `prop_scene_coherence_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_SCENE_COHERENCE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop scene coherence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_0785` | `object_continuity_video_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_CONTINUITY_VIDEO_PROM_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object continuity video con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0786` | `prop_lineage_rule_prompt_effect` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_LINEAGE_RULE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop lineage rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0787` | `floating_cloth_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLOATING_CLOTH_BLOCKER_PROMP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar floating cloth blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0788` | `texture_flat_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEXTURE_FLAT_BLOCKER_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar texture flat blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0789` | `wrong_style_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_STYLE_BLOCKER_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong style blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_0790` | `brand_logo_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_BLOCKER_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0791` | `unsupported_bodywear_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UNSUPPORTED_BODYWEAR_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar unsupported bodywear blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0792` | `prop_physics_blocker_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_PHYSICS_BLOCKER_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop physics blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0793` | `wardrobe_identity_drift_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_IDENTITY_DRIFT_RULE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe identity drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_0794` | `material_repair_rule_prompt_effect` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MATERIAL_REPAIR_RULE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar material repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1200` | `wardrobe_signature_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1201` | `color_palette_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COLOR_PALETTE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar color palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1202` | `silhouette_preference_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SILHOUETTE_PREFERENCE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar silhouette preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1203` | `fabric_preferences_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_PREFERENCES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric preferences con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1204` | `fabric_weight_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1205` | `fabric_texture_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_TEXTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1206` | `fit_rules_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FIT_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fit rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1207` | `seam_visibility_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SEAM_VISIBILITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar seam visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1208` | `drape_behavior_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DRAPE_BEHAVIOR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar drape behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1209` | `wrinkle_logic_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRINKLE_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrinkle logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1210` | `support_physics_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUPPORT_PHYSICS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar support physics con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1211` | `layering_logic_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LAYERING_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar layering logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1212` | `season_rule_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SEASON_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar season rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1213` | `occasion_rule_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OCCASION_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar occasion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1214` | `body_shape_fit_rule_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_SHAPE_FIT_RULE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body shape fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1215` | `wardrobe_story_logic_qa_matrix` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_STORY_LOGIC_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1216` | `bodywear_editorial_limits_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODYWEAR_EDITORIAL_LIMITS_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar bodywear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1217` | `swimwear_editorial_limits_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SWIMWEAR_EDITORIAL_LIMITS_QA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar swimwear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1218` | `lingerie_non_explicit_rule_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LINGERIE_NON_EXPLICIT_RULE_Q_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lingerie non explicit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1219` | `adult_context_rule_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_CONTEXT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1220` | `no_exploitation_rule_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_EXPLOITATION_RULE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no exploitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1221` | `camera_angle_safety_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_ANGLE_SAFETY_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera angle safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1222` | `pose_safety_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_SAFETY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1223` | `styling_alternative_rule_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STYLING_ALTERNATIVE_RULE_QA__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar styling alternative rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_1224` | `commercial_safe_rewrite_qa_matrix` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMMERCIAL_SAFE_REWRITE_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar commercial safe rewrite con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1225` | `accessory_rules_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCESSORY_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accessory rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1226` | `jewelry_limit_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JEWELRY_LIMIT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jewelry limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1227` | `prop_material_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_MATERIAL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop material con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1228` | `prop_weight_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1229` | `prop_scale_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1230` | `hand_object_contact_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_OBJECT_CONTACT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_1231` | `object_shadow_rule_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_SHADOW_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object shadow rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_1232` | `brand_logo_restrictions_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_RESTRICTIONS_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo restrictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1233` | `prop_scene_coherence_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_SCENE_COHERENCE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop scene coherence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1234` | `object_continuity_video_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_CONTINUITY_VIDEO_QA_M_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object continuity video con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1235` | `prop_lineage_rule_qa_matrix` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_LINEAGE_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop lineage rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1236` | `floating_cloth_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLOATING_CLOTH_BLOCKER_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar floating cloth blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1237` | `texture_flat_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEXTURE_FLAT_BLOCKER_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar texture flat blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1238` | `wrong_style_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_STYLE_BLOCKER_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong style blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_1239` | `brand_logo_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1240` | `unsupported_bodywear_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UNSUPPORTED_BODYWEAR_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar unsupported bodywear blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1241` | `prop_physics_blocker_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_PHYSICS_BLOCKER_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop physics blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1242` | `wardrobe_identity_drift_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_IDENTITY_DRIFT_RULE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe identity drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1243` | `material_repair_rule_qa_matrix` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MATERIAL_REPAIR_RULE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar material repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1649` | `wardrobe_signature_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_SIGNATURE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1650` | `color_palette_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COLOR_PALETTE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar color palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1651` | `silhouette_preference_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SILHOUETTE_PREFERENCE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar silhouette preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1652` | `fabric_preferences_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_PREFERENCES_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric preferences con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1653` | `fabric_weight_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_WEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1654` | `fabric_texture_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FABRIC_TEXTURE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fabric texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1655` | `fit_rules_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FIT_RULES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar fit rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1656` | `seam_visibility_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SEAM_VISIBILITY_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar seam visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1657` | `drape_behavior_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_DRAPE_BEHAVIOR_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar drape behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1658` | `wrinkle_logic_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRINKLE_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrinkle logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1659` | `support_physics_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SUPPORT_PHYSICS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar support physics con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1660` | `layering_logic_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LAYERING_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar layering logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1661` | `season_rule_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SEASON_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar season rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1662` | `occasion_rule_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OCCASION_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar occasion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1663` | `body_shape_fit_rule_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODY_SHAPE_FIT_RULE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar body shape fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1664` | `wardrobe_story_logic_vendor_repair` | wardrobe | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_STORY_LOGIC_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1665` | `bodywear_editorial_limits_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BODYWEAR_EDITORIAL_LIMITS_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar bodywear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1666` | `swimwear_editorial_limits_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_SWIMWEAR_EDITORIAL_LIMITS_VE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar swimwear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1667` | `lingerie_non_explicit_rule_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_LINGERIE_NON_EXPLICIT_RULE_V_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar lingerie non explicit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1668` | `adult_context_rule_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ADULT_CONTEXT_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar adult context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1669` | `no_exploitation_rule_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_NO_EXPLOITATION_RULE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar no exploitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_CAMERA_1670` | `camera_angle_safety_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_CAMERA_ANGLE_SAFETY_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar camera angle safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_ACTING_1671` | `pose_safety_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_POSE_SAFETY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar pose safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1672` | `styling_alternative_rule_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_STYLING_ALTERNATIVE_RULE_VEN_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar styling alternative rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_1673` | `commercial_safe_rewrite_vendor_repair` | bodywear | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_COMMERCIAL_SAFE_REWRITE_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar commercial safe rewrite con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1674` | `accessory_rules_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_ACCESSORY_RULES_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar accessory rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1675` | `jewelry_limit_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_JEWELRY_LIMIT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar jewelry limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1676` | `prop_material_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_MATERIAL_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop material con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1677` | `prop_weight_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_WEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1678` | `prop_scale_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1679` | `hand_object_contact_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_HAND_OBJECT_CONTACT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LIGHTING_1680` | `object_shadow_rule_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_SHADOW_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object shadow rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_1681` | `brand_logo_restrictions_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_RESTRICTIONS_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo restrictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_SCENE_1682` | `prop_scene_coherence_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_SCENE_COHERENCE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop scene coherence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_VIDEO_1683` | `object_continuity_video_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_OBJECT_CONTINUITY_VIDEO_VEND_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar object continuity video con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1684` | `prop_lineage_rule_vendor_repair` | props | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_LINEAGE_RULE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop lineage rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1685` | `floating_cloth_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_FLOATING_CLOTH_BLOCKER_VENDO_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar floating cloth blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1686` | `texture_flat_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_TEXTURE_FLAT_BLOCKER_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar texture flat blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1687` | `wrong_style_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WRONG_STYLE_BLOCKER_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wrong style blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_LEGAL_1688` | `brand_logo_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_BRAND_LOGO_BLOCKER_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar brand logo blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1689` | `unsupported_bodywear_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_UNSUPPORTED_BODYWEAR_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar unsupported bodywear blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1690` | `prop_physics_blocker_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_PROP_PHYSICS_BLOCKER_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar prop physics blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1691` | `wardrobe_identity_drift_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_WARDROBE_IDENTITY_DRIFT_RULE_PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar wardrobe identity drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |
| `P360_WARDROBE_1692` | `material_repair_rule_vendor_repair` | qa | HARD_LOCK if identity-critical else CONTROLLED_VARIATION | QA_MATERIAL_REPAIR_RULE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test. | Reforzar material repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión. |

## Reglas extendidas por campo

### P360_WARDROBE_0302 — wardrobe_signature
- Definición: Campo operativo para wardrobe signature dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wardrobe signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_SIGNATURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WARDROBE_SIGNATURE_DRIFT_OR_GAP
- Fallback: Reforzar wardrobe signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0303 — color_palette
- Definición: Campo operativo para color palette dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar color palette como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar color palette como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COLOR_PALETTE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_COLOR_PALETTE_DRIFT_OR_GAP
- Fallback: Reforzar color palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0304 — silhouette_preference
- Definición: Campo operativo para silhouette preference dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar silhouette preference como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar silhouette preference como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SILHOUETTE_PREFERENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SILHOUETTE_PREFERENCE_DRIFT_OR_GAP
- Fallback: Reforzar silhouette preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0305 — fabric_preferences
- Definición: Campo operativo para fabric preferences dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fabric preferences como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric preferences como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_PREFERENCES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FABRIC_PREFERENCES_DRIFT_OR_GAP
- Fallback: Reforzar fabric preferences con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0306 — fabric_weight
- Definición: Campo operativo para fabric weight dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fabric weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FABRIC_WEIGHT_DRIFT_OR_GAP
- Fallback: Reforzar fabric weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0307 — fabric_texture
- Definición: Campo operativo para fabric texture dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fabric texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_TEXTURE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FABRIC_TEXTURE_DRIFT_OR_GAP
- Fallback: Reforzar fabric texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0308 — fit_rules
- Definición: Campo operativo para fit rules dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar fit rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fit rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FIT_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FIT_RULES_DRIFT_OR_GAP
- Fallback: Reforzar fit rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0309 — seam_visibility
- Definición: Campo operativo para seam visibility dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar seam visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar seam visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SEAM_VISIBILITY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SEAM_VISIBILITY_DRIFT_OR_GAP
- Fallback: Reforzar seam visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0310 — drape_behavior
- Definición: Campo operativo para drape behavior dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar drape behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar drape behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DRAPE_BEHAVIOR_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_DRAPE_BEHAVIOR_DRIFT_OR_GAP
- Fallback: Reforzar drape behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0311 — wrinkle_logic
- Definición: Campo operativo para wrinkle logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wrinkle logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrinkle logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRINKLE_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WRINKLE_LOGIC_DRIFT_OR_GAP
- Fallback: Reforzar wrinkle logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0312 — support_physics
- Definición: Campo operativo para support physics dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar support physics como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar support physics como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUPPORT_PHYSICS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SUPPORT_PHYSICS_DRIFT_OR_GAP
- Fallback: Reforzar support physics con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0313 — layering_logic
- Definición: Campo operativo para layering logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar layering logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar layering logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LAYERING_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LAYERING_LOGIC_DRIFT_OR_GAP
- Fallback: Reforzar layering logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0314 — season_rule
- Definición: Campo operativo para season rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar season rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar season rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SEASON_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SEASON_RULE_DRIFT_OR_GAP
- Fallback: Reforzar season rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0315 — occasion_rule
- Definición: Campo operativo para occasion rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar occasion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar occasion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OCCASION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_OCCASION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar occasion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0316 — body_shape_fit_rule
- Definición: Campo operativo para body shape fit rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar body shape fit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body shape fit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_SHAPE_FIT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BODY_SHAPE_FIT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar body shape fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0317 — wardrobe_story_logic
- Definición: Campo operativo para wardrobe story logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wardrobe story logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe story logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_STORY_LOGIC_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WARDROBE_STORY_LOGIC_DRIFT_OR_GAP
- Fallback: Reforzar wardrobe story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0318 — bodywear_editorial_limits
- Definición: Campo operativo para bodywear editorial limits dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar bodywear editorial limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar bodywear editorial limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODYWEAR_EDITORIAL_LIMITS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BODYWEAR_EDITORIAL_LIMITS_DRIFT_OR_GAP
- Fallback: Reforzar bodywear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0319 — swimwear_editorial_limits
- Definición: Campo operativo para swimwear editorial limits dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar swimwear editorial limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar swimwear editorial limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SWIMWEAR_EDITORIAL_LIMITS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_SWIMWEAR_EDITORIAL_LIMITS_DRIFT_OR_GAP
- Fallback: Reforzar swimwear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0320 — lingerie_non_explicit_rule
- Definición: Campo operativo para lingerie non explicit rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar lingerie non explicit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lingerie non explicit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LINGERIE_NON_EXPLICIT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_LINGERIE_NON_EXPLICIT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar lingerie non explicit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0321 — adult_context_rule
- Definición: Campo operativo para adult context rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar adult context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_CONTEXT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ADULT_CONTEXT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar adult context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0322 — no_exploitation_rule
- Definición: Campo operativo para no exploitation rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar no exploitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no exploitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_EXPLOITATION_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_NO_EXPLOITATION_RULE_DRIFT_OR_GAP
- Fallback: Reforzar no exploitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0323 — camera_angle_safety
- Definición: Campo operativo para camera angle safety dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar camera angle safety como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera angle safety como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_ANGLE_SAFETY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_CAMERA_ANGLE_SAFETY_DRIFT_OR_GAP
- Fallback: Reforzar camera angle safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0324 — pose_safety
- Definición: Campo operativo para pose safety dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar pose safety como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose safety como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_SAFETY_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_POSE_SAFETY_DRIFT_OR_GAP
- Fallback: Reforzar pose safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0325 — styling_alternative_rule
- Definición: Campo operativo para styling alternative rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar styling alternative rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar styling alternative rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STYLING_ALTERNATIVE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_STYLING_ALTERNATIVE_RULE_DRIFT_OR_GAP
- Fallback: Reforzar styling alternative rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_0326 — commercial_safe_rewrite
- Definición: Campo operativo para commercial safe rewrite dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar commercial safe rewrite como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar commercial safe rewrite como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMMERCIAL_SAFE_REWRITE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_COMMERCIAL_SAFE_REWRITE_DRIFT_OR_GAP
- Fallback: Reforzar commercial safe rewrite con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0327 — accessory_rules
- Definición: Campo operativo para accessory rules dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar accessory rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accessory rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCESSORY_RULES_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_ACCESSORY_RULES_DRIFT_OR_GAP
- Fallback: Reforzar accessory rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0328 — jewelry_limit
- Definición: Campo operativo para jewelry limit dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar jewelry limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jewelry limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JEWELRY_LIMIT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_JEWELRY_LIMIT_DRIFT_OR_GAP
- Fallback: Reforzar jewelry limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0329 — prop_material
- Definición: Campo operativo para prop material dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar prop material como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop material como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_MATERIAL_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROP_MATERIAL_DRIFT_OR_GAP
- Fallback: Reforzar prop material con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0330 — prop_weight
- Definición: Campo operativo para prop weight dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar prop weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_WEIGHT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROP_WEIGHT_DRIFT_OR_GAP
- Fallback: Reforzar prop weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0331 — prop_scale
- Definición: Campo operativo para prop scale dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar prop scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_SCALE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROP_SCALE_DRIFT_OR_GAP
- Fallback: Reforzar prop scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0332 — hand_object_contact
- Definición: Campo operativo para hand object contact dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar hand object contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand object contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_OBJECT_CONTACT_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_HAND_OBJECT_CONTACT_DRIFT_OR_GAP
- Fallback: Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0333 — object_shadow_rule
- Definición: Campo operativo para object shadow rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar object shadow rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object shadow rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_SHADOW_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_OBJECT_SHADOW_RULE_DRIFT_OR_GAP
- Fallback: Reforzar object shadow rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_0334 — brand_logo_restrictions
- Definición: Campo operativo para brand logo restrictions dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar brand logo restrictions como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo restrictions como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_RESTRICTIONS_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BRAND_LOGO_RESTRICTIONS_DRIFT_OR_GAP
- Fallback: Reforzar brand logo restrictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0335 — prop_scene_coherence
- Definición: Campo operativo para prop scene coherence dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar prop scene coherence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop scene coherence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_SCENE_COHERENCE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROP_SCENE_COHERENCE_DRIFT_OR_GAP
- Fallback: Reforzar prop scene coherence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0336 — object_continuity_video
- Definición: Campo operativo para object continuity video dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar object continuity video como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object continuity video como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_CONTINUITY_VIDEO_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_OBJECT_CONTINUITY_VIDEO_DRIFT_OR_GAP
- Fallback: Reforzar object continuity video con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0337 — prop_lineage_rule
- Definición: Campo operativo para prop lineage rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar prop lineage rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop lineage rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_LINEAGE_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROP_LINEAGE_RULE_DRIFT_OR_GAP
- Fallback: Reforzar prop lineage rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0338 — floating_cloth_blocker
- Definición: Campo operativo para floating cloth blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar floating cloth blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar floating cloth blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLOATING_CLOTH_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_FLOATING_CLOTH_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar floating cloth blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0339 — texture_flat_blocker
- Definición: Campo operativo para texture flat blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar texture flat blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar texture flat blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEXTURE_FLAT_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_TEXTURE_FLAT_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar texture flat blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0340 — wrong_style_blocker
- Definición: Campo operativo para wrong style blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wrong style blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong style blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_STYLE_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WRONG_STYLE_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar wrong style blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_0341 — brand_logo_blocker
- Definición: Campo operativo para brand logo blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar brand logo blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_BRAND_LOGO_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar brand logo blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0342 — unsupported_bodywear_blocker
- Definición: Campo operativo para unsupported bodywear blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar unsupported bodywear blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar unsupported bodywear blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UNSUPPORTED_BODYWEAR_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_UNSUPPORTED_BODYWEAR_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar unsupported bodywear blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0343 — prop_physics_blocker
- Definición: Campo operativo para prop physics blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar prop physics blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop physics blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_PHYSICS_BLOCKER_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_PROP_PHYSICS_BLOCKER_DRIFT_OR_GAP
- Fallback: Reforzar prop physics blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0344 — wardrobe_identity_drift_rule
- Definición: Campo operativo para wardrobe identity drift rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar wardrobe identity drift rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe identity drift rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_IDENTITY_DRIFT_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_WARDROBE_IDENTITY_DRIFT_RULE_DRIFT_OR_GAP
- Fallback: Reforzar wardrobe identity drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0345 — material_repair_rule
- Definición: Campo operativo para material repair rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar.
- Ejemplo correcto: Usar material repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar material repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MATERIAL_REPAIR_RULE_PASS requiere coherencia con Perfil360, core relevante, output y sidecar.
- Fail code: FAIL_MATERIAL_REPAIR_RULE_DRIFT_OR_GAP
- Fallback: Reforzar material repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0751 — wardrobe_signature_prompt_effect
- Definición: Campo operativo para wardrobe signature dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_SIGNATURE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_SIGNATURE_PROMPT_EFFECT
- Fallback: Reforzar wardrobe signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0752 — color_palette_prompt_effect
- Definición: Campo operativo para color palette dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar color palette como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar color palette como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COLOR_PALETTE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COLOR_PALETTE_PROMPT_EFFECT
- Fallback: Reforzar color palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0753 — silhouette_preference_prompt_effect
- Definición: Campo operativo para silhouette preference dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar silhouette preference como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar silhouette preference como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SILHOUETTE_PREFERENCE_PROMPT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SILHOUETTE_PREFERENCE_PROMPT_EFF
- Fallback: Reforzar silhouette preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0754 — fabric_preferences_prompt_effect
- Definición: Campo operativo para fabric preferences dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric preferences como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric preferences como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_PREFERENCES_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_PREFERENCES_PROMPT_EFFECT
- Fallback: Reforzar fabric preferences con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0755 — fabric_weight_prompt_effect
- Definición: Campo operativo para fabric weight dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_WEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_WEIGHT_PROMPT_EFFECT
- Fallback: Reforzar fabric weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0756 — fabric_texture_prompt_effect
- Definición: Campo operativo para fabric texture dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_TEXTURE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_TEXTURE_PROMPT_EFFECT
- Fallback: Reforzar fabric texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0757 — fit_rules_prompt_effect
- Definición: Campo operativo para fit rules dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fit rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fit rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FIT_RULES_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FIT_RULES_PROMPT_EFFECT
- Fallback: Reforzar fit rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0758 — seam_visibility_prompt_effect
- Definición: Campo operativo para seam visibility dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar seam visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar seam visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SEAM_VISIBILITY_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SEAM_VISIBILITY_PROMPT_EFFECT
- Fallback: Reforzar seam visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0759 — drape_behavior_prompt_effect
- Definición: Campo operativo para drape behavior dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar drape behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar drape behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DRAPE_BEHAVIOR_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DRAPE_BEHAVIOR_PROMPT_EFFECT
- Fallback: Reforzar drape behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0760 — wrinkle_logic_prompt_effect
- Definición: Campo operativo para wrinkle logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrinkle logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrinkle logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRINKLE_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRINKLE_LOGIC_PROMPT_EFFECT
- Fallback: Reforzar wrinkle logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0761 — support_physics_prompt_effect
- Definición: Campo operativo para support physics dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar support physics como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar support physics como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUPPORT_PHYSICS_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUPPORT_PHYSICS_PROMPT_EFFECT
- Fallback: Reforzar support physics con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0762 — layering_logic_prompt_effect
- Definición: Campo operativo para layering logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar layering logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar layering logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LAYERING_LOGIC_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LAYERING_LOGIC_PROMPT_EFFECT
- Fallback: Reforzar layering logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0763 — season_rule_prompt_effect
- Definición: Campo operativo para season rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar season rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar season rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SEASON_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SEASON_RULE_PROMPT_EFFECT
- Fallback: Reforzar season rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0764 — occasion_rule_prompt_effect
- Definición: Campo operativo para occasion rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar occasion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar occasion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OCCASION_RULE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OCCASION_RULE_PROMPT_EFFECT
- Fallback: Reforzar occasion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0765 — body_shape_fit_rule_prompt_effect
- Definición: Campo operativo para body shape fit rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body shape fit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body shape fit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_SHAPE_FIT_RULE_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_SHAPE_FIT_RULE_PROMPT_EFFEC
- Fallback: Reforzar body shape fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0766 — wardrobe_story_logic_prompt_effect
- Definición: Campo operativo para wardrobe story logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe story logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe story logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_STORY_LOGIC_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_STORY_LOGIC_PROMPT_EFFE
- Fallback: Reforzar wardrobe story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0767 — bodywear_editorial_limits_prompt_effect
- Definición: Campo operativo para bodywear editorial limits dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar bodywear editorial limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar bodywear editorial limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODYWEAR_EDITORIAL_LIMITS_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODYWEAR_EDITORIAL_LIMITS_PROMPT
- Fallback: Reforzar bodywear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0768 — swimwear_editorial_limits_prompt_effect
- Definición: Campo operativo para swimwear editorial limits dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar swimwear editorial limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar swimwear editorial limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SWIMWEAR_EDITORIAL_LIMITS_PR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SWIMWEAR_EDITORIAL_LIMITS_PROMPT
- Fallback: Reforzar swimwear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0769 — lingerie_non_explicit_rule_prompt_effect
- Definición: Campo operativo para lingerie non explicit rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lingerie non explicit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lingerie non explicit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LINGERIE_NON_EXPLICIT_RULE_P_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LINGERIE_NON_EXPLICIT_RULE_PROMP
- Fallback: Reforzar lingerie non explicit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0770 — adult_context_rule_prompt_effect
- Definición: Campo operativo para adult context rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_CONTEXT_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_CONTEXT_RULE_PROMPT_EFFECT
- Fallback: Reforzar adult context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0771 — no_exploitation_rule_prompt_effect
- Definición: Campo operativo para no exploitation rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no exploitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no exploitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_EXPLOITATION_RULE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_EXPLOITATION_RULE_PROMPT_EFFE
- Fallback: Reforzar no exploitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_0772 — camera_angle_safety_prompt_effect
- Definición: Campo operativo para camera angle safety dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera angle safety como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera angle safety como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_ANGLE_SAFETY_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_ANGLE_SAFETY_PROMPT_EFFEC
- Fallback: Reforzar camera angle safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_0773 — pose_safety_prompt_effect
- Definición: Campo operativo para pose safety dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose safety como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose safety como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_SAFETY_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_SAFETY_PROMPT_EFFECT
- Fallback: Reforzar pose safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0774 — styling_alternative_rule_prompt_effect
- Definición: Campo operativo para styling alternative rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar styling alternative rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar styling alternative rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STYLING_ALTERNATIVE_RULE_PRO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STYLING_ALTERNATIVE_RULE_PROMPT_
- Fallback: Reforzar styling alternative rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_0775 — commercial_safe_rewrite_prompt_effect
- Definición: Campo operativo para commercial safe rewrite dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar commercial safe rewrite como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar commercial safe rewrite como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMMERCIAL_SAFE_REWRITE_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMMERCIAL_SAFE_REWRITE_PROMPT_E
- Fallback: Reforzar commercial safe rewrite con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0776 — accessory_rules_prompt_effect
- Definición: Campo operativo para accessory rules dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accessory rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accessory rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCESSORY_RULES_PROMPT_EFFEC_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCESSORY_RULES_PROMPT_EFFECT
- Fallback: Reforzar accessory rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0777 — jewelry_limit_prompt_effect
- Definición: Campo operativo para jewelry limit dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jewelry limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jewelry limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JEWELRY_LIMIT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JEWELRY_LIMIT_PROMPT_EFFECT
- Fallback: Reforzar jewelry limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0778 — prop_material_prompt_effect
- Definición: Campo operativo para prop material dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop material como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop material como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_MATERIAL_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_MATERIAL_PROMPT_EFFECT
- Fallback: Reforzar prop material con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0779 — prop_weight_prompt_effect
- Definición: Campo operativo para prop weight dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_WEIGHT_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_WEIGHT_PROMPT_EFFECT
- Fallback: Reforzar prop weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0780 — prop_scale_prompt_effect
- Definición: Campo operativo para prop scale dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_SCALE_PROMPT_EFFECT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_SCALE_PROMPT_EFFECT
- Fallback: Reforzar prop scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0781 — hand_object_contact_prompt_effect
- Definición: Campo operativo para hand object contact dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand object contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand object contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_OBJECT_CONTACT_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_OBJECT_CONTACT_PROMPT_EFFEC
- Fallback: Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_0782 — object_shadow_rule_prompt_effect
- Definición: Campo operativo para object shadow rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object shadow rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object shadow rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_SHADOW_RULE_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_SHADOW_RULE_PROMPT_EFFECT
- Fallback: Reforzar object shadow rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_0783 — brand_logo_restrictions_prompt_effect
- Definición: Campo operativo para brand logo restrictions dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo restrictions como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo restrictions como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_RESTRICTIONS_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_RESTRICTIONS_PROMPT_E
- Fallback: Reforzar brand logo restrictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_0784 — prop_scene_coherence_prompt_effect
- Definición: Campo operativo para prop scene coherence dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop scene coherence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop scene coherence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_SCENE_COHERENCE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_SCENE_COHERENCE_PROMPT_EFFE
- Fallback: Reforzar prop scene coherence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_0785 — object_continuity_video_prompt_effect
- Definición: Campo operativo para object continuity video dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object continuity video como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object continuity video como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_CONTINUITY_VIDEO_PROM_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_CONTINUITY_VIDEO_PROMPT_E
- Fallback: Reforzar object continuity video con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0786 — prop_lineage_rule_prompt_effect
- Definición: Campo operativo para prop lineage rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop lineage rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop lineage rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_LINEAGE_RULE_PROMPT_EFF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_LINEAGE_RULE_PROMPT_EFFECT
- Fallback: Reforzar prop lineage rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0787 — floating_cloth_blocker_prompt_effect
- Definición: Campo operativo para floating cloth blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar floating cloth blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar floating cloth blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLOATING_CLOTH_BLOCKER_PROMP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLOATING_CLOTH_BLOCKER_PROMPT_EF
- Fallback: Reforzar floating cloth blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0788 — texture_flat_blocker_prompt_effect
- Definición: Campo operativo para texture flat blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar texture flat blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar texture flat blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEXTURE_FLAT_BLOCKER_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEXTURE_FLAT_BLOCKER_PROMPT_EFFE
- Fallback: Reforzar texture flat blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0789 — wrong_style_blocker_prompt_effect
- Definición: Campo operativo para wrong style blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong style blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong style blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_STYLE_BLOCKER_PROMPT_E_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_STYLE_BLOCKER_PROMPT_EFFEC
- Fallback: Reforzar wrong style blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_0790 — brand_logo_blocker_prompt_effect
- Definición: Campo operativo para brand logo blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_BLOCKER_PROMPT_EF_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_BLOCKER_PROMPT_EFFECT
- Fallback: Reforzar brand logo blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0791 — unsupported_bodywear_blocker_prompt_effect
- Definición: Campo operativo para unsupported bodywear blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar unsupported bodywear blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar unsupported bodywear blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UNSUPPORTED_BODYWEAR_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UNSUPPORTED_BODYWEAR_BLOCKER_PRO
- Fallback: Reforzar unsupported bodywear blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0792 — prop_physics_blocker_prompt_effect
- Definición: Campo operativo para prop physics blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop physics blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop physics blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_PHYSICS_BLOCKER_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_PHYSICS_BLOCKER_PROMPT_EFFE
- Fallback: Reforzar prop physics blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0793 — wardrobe_identity_drift_rule_prompt_effect
- Definición: Campo operativo para wardrobe identity drift rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe identity drift rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe identity drift rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_IDENTITY_DRIFT_RULE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_IDENTITY_DRIFT_RULE_PRO
- Fallback: Reforzar wardrobe identity drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_0794 — material_repair_rule_prompt_effect
- Definición: Campo operativo para material repair rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante prompt_effect: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar material repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar material repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MATERIAL_REPAIR_RULE_PROMPT__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MATERIAL_REPAIR_RULE_PROMPT_EFFE
- Fallback: Reforzar material repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1200 — wardrobe_signature_qa_matrix
- Definición: Campo operativo para wardrobe signature dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_SIGNATURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_SIGNATURE_QA_MATRIX
- Fallback: Reforzar wardrobe signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1201 — color_palette_qa_matrix
- Definición: Campo operativo para color palette dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar color palette como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar color palette como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COLOR_PALETTE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COLOR_PALETTE_QA_MATRIX
- Fallback: Reforzar color palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1202 — silhouette_preference_qa_matrix
- Definición: Campo operativo para silhouette preference dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar silhouette preference como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar silhouette preference como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SILHOUETTE_PREFERENCE_QA_MAT_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SILHOUETTE_PREFERENCE_QA_MATRIX
- Fallback: Reforzar silhouette preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1203 — fabric_preferences_qa_matrix
- Definición: Campo operativo para fabric preferences dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric preferences como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric preferences como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_PREFERENCES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_PREFERENCES_QA_MATRIX
- Fallback: Reforzar fabric preferences con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1204 — fabric_weight_qa_matrix
- Definición: Campo operativo para fabric weight dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_WEIGHT_QA_MATRIX
- Fallback: Reforzar fabric weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1205 — fabric_texture_qa_matrix
- Definición: Campo operativo para fabric texture dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_TEXTURE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_TEXTURE_QA_MATRIX
- Fallback: Reforzar fabric texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1206 — fit_rules_qa_matrix
- Definición: Campo operativo para fit rules dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fit rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fit rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FIT_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FIT_RULES_QA_MATRIX
- Fallback: Reforzar fit rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1207 — seam_visibility_qa_matrix
- Definición: Campo operativo para seam visibility dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar seam visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar seam visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SEAM_VISIBILITY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SEAM_VISIBILITY_QA_MATRIX
- Fallback: Reforzar seam visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1208 — drape_behavior_qa_matrix
- Definición: Campo operativo para drape behavior dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar drape behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar drape behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DRAPE_BEHAVIOR_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DRAPE_BEHAVIOR_QA_MATRIX
- Fallback: Reforzar drape behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1209 — wrinkle_logic_qa_matrix
- Definición: Campo operativo para wrinkle logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrinkle logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrinkle logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRINKLE_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRINKLE_LOGIC_QA_MATRIX
- Fallback: Reforzar wrinkle logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1210 — support_physics_qa_matrix
- Definición: Campo operativo para support physics dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar support physics como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar support physics como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUPPORT_PHYSICS_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUPPORT_PHYSICS_QA_MATRIX
- Fallback: Reforzar support physics con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1211 — layering_logic_qa_matrix
- Definición: Campo operativo para layering logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar layering logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar layering logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LAYERING_LOGIC_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LAYERING_LOGIC_QA_MATRIX
- Fallback: Reforzar layering logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1212 — season_rule_qa_matrix
- Definición: Campo operativo para season rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar season rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar season rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SEASON_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SEASON_RULE_QA_MATRIX
- Fallback: Reforzar season rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1213 — occasion_rule_qa_matrix
- Definición: Campo operativo para occasion rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar occasion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar occasion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OCCASION_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OCCASION_RULE_QA_MATRIX
- Fallback: Reforzar occasion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1214 — body_shape_fit_rule_qa_matrix
- Definición: Campo operativo para body shape fit rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body shape fit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body shape fit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_SHAPE_FIT_RULE_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_SHAPE_FIT_RULE_QA_MATRIX
- Fallback: Reforzar body shape fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1215 — wardrobe_story_logic_qa_matrix
- Definición: Campo operativo para wardrobe story logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe story logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe story logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_STORY_LOGIC_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_STORY_LOGIC_QA_MATRIX
- Fallback: Reforzar wardrobe story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1216 — bodywear_editorial_limits_qa_matrix
- Definición: Campo operativo para bodywear editorial limits dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar bodywear editorial limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar bodywear editorial limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODYWEAR_EDITORIAL_LIMITS_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODYWEAR_EDITORIAL_LIMITS_QA_MAT
- Fallback: Reforzar bodywear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1217 — swimwear_editorial_limits_qa_matrix
- Definición: Campo operativo para swimwear editorial limits dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar swimwear editorial limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar swimwear editorial limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SWIMWEAR_EDITORIAL_LIMITS_QA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SWIMWEAR_EDITORIAL_LIMITS_QA_MAT
- Fallback: Reforzar swimwear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1218 — lingerie_non_explicit_rule_qa_matrix
- Definición: Campo operativo para lingerie non explicit rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lingerie non explicit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lingerie non explicit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LINGERIE_NON_EXPLICIT_RULE_Q_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LINGERIE_NON_EXPLICIT_RULE_QA_MA
- Fallback: Reforzar lingerie non explicit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1219 — adult_context_rule_qa_matrix
- Definición: Campo operativo para adult context rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_CONTEXT_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_CONTEXT_RULE_QA_MATRIX
- Fallback: Reforzar adult context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1220 — no_exploitation_rule_qa_matrix
- Definición: Campo operativo para no exploitation rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no exploitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no exploitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_EXPLOITATION_RULE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_EXPLOITATION_RULE_QA_MATRIX
- Fallback: Reforzar no exploitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1221 — camera_angle_safety_qa_matrix
- Definición: Campo operativo para camera angle safety dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera angle safety como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera angle safety como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_ANGLE_SAFETY_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_ANGLE_SAFETY_QA_MATRIX
- Fallback: Reforzar camera angle safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1222 — pose_safety_qa_matrix
- Definición: Campo operativo para pose safety dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose safety como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose safety como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_SAFETY_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_SAFETY_QA_MATRIX
- Fallback: Reforzar pose safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1223 — styling_alternative_rule_qa_matrix
- Definición: Campo operativo para styling alternative rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar styling alternative rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar styling alternative rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STYLING_ALTERNATIVE_RULE_QA__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STYLING_ALTERNATIVE_RULE_QA_MATR
- Fallback: Reforzar styling alternative rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_1224 — commercial_safe_rewrite_qa_matrix
- Definición: Campo operativo para commercial safe rewrite dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar commercial safe rewrite como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar commercial safe rewrite como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMMERCIAL_SAFE_REWRITE_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMMERCIAL_SAFE_REWRITE_QA_MATRI
- Fallback: Reforzar commercial safe rewrite con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1225 — accessory_rules_qa_matrix
- Definición: Campo operativo para accessory rules dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accessory rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accessory rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCESSORY_RULES_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCESSORY_RULES_QA_MATRIX
- Fallback: Reforzar accessory rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1226 — jewelry_limit_qa_matrix
- Definición: Campo operativo para jewelry limit dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jewelry limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jewelry limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JEWELRY_LIMIT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JEWELRY_LIMIT_QA_MATRIX
- Fallback: Reforzar jewelry limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1227 — prop_material_qa_matrix
- Definición: Campo operativo para prop material dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop material como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop material como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_MATERIAL_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_MATERIAL_QA_MATRIX
- Fallback: Reforzar prop material con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1228 — prop_weight_qa_matrix
- Definición: Campo operativo para prop weight dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_WEIGHT_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_WEIGHT_QA_MATRIX
- Fallback: Reforzar prop weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1229 — prop_scale_qa_matrix
- Definición: Campo operativo para prop scale dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_SCALE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_SCALE_QA_MATRIX
- Fallback: Reforzar prop scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1230 — hand_object_contact_qa_matrix
- Definición: Campo operativo para hand object contact dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand object contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand object contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_OBJECT_CONTACT_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_OBJECT_CONTACT_QA_MATRIX
- Fallback: Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_1231 — object_shadow_rule_qa_matrix
- Definición: Campo operativo para object shadow rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object shadow rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object shadow rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_SHADOW_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_SHADOW_RULE_QA_MATRIX
- Fallback: Reforzar object shadow rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_1232 — brand_logo_restrictions_qa_matrix
- Definición: Campo operativo para brand logo restrictions dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo restrictions como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo restrictions como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_RESTRICTIONS_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_RESTRICTIONS_QA_MATRI
- Fallback: Reforzar brand logo restrictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1233 — prop_scene_coherence_qa_matrix
- Definición: Campo operativo para prop scene coherence dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop scene coherence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop scene coherence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_SCENE_COHERENCE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_SCENE_COHERENCE_QA_MATRIX
- Fallback: Reforzar prop scene coherence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1234 — object_continuity_video_qa_matrix
- Definición: Campo operativo para object continuity video dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object continuity video como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object continuity video como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_CONTINUITY_VIDEO_QA_M_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_CONTINUITY_VIDEO_QA_MATRI
- Fallback: Reforzar object continuity video con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1235 — prop_lineage_rule_qa_matrix
- Definición: Campo operativo para prop lineage rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop lineage rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop lineage rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_LINEAGE_RULE_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_LINEAGE_RULE_QA_MATRIX
- Fallback: Reforzar prop lineage rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1236 — floating_cloth_blocker_qa_matrix
- Definición: Campo operativo para floating cloth blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar floating cloth blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar floating cloth blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLOATING_CLOTH_BLOCKER_QA_MA_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLOATING_CLOTH_BLOCKER_QA_MATRIX
- Fallback: Reforzar floating cloth blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1237 — texture_flat_blocker_qa_matrix
- Definición: Campo operativo para texture flat blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar texture flat blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar texture flat blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEXTURE_FLAT_BLOCKER_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEXTURE_FLAT_BLOCKER_QA_MATRIX
- Fallback: Reforzar texture flat blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1238 — wrong_style_blocker_qa_matrix
- Definición: Campo operativo para wrong style blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong style blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong style blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_STYLE_BLOCKER_QA_MATRI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_STYLE_BLOCKER_QA_MATRIX
- Fallback: Reforzar wrong style blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_1239 — brand_logo_blocker_qa_matrix
- Definición: Campo operativo para brand logo blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_BLOCKER_QA_MATRIX_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_BLOCKER_QA_MATRIX
- Fallback: Reforzar brand logo blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1240 — unsupported_bodywear_blocker_qa_matrix
- Definición: Campo operativo para unsupported bodywear blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar unsupported bodywear blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar unsupported bodywear blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UNSUPPORTED_BODYWEAR_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UNSUPPORTED_BODYWEAR_BLOCKER_QA_
- Fallback: Reforzar unsupported bodywear blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1241 — prop_physics_blocker_qa_matrix
- Definición: Campo operativo para prop physics blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop physics blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop physics blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_PHYSICS_BLOCKER_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_PHYSICS_BLOCKER_QA_MATRIX
- Fallback: Reforzar prop physics blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1242 — wardrobe_identity_drift_rule_qa_matrix
- Definición: Campo operativo para wardrobe identity drift rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe identity drift rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe identity drift rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_IDENTITY_DRIFT_RULE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_IDENTITY_DRIFT_RULE_QA_
- Fallback: Reforzar wardrobe identity drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1243 — material_repair_rule_qa_matrix
- Definición: Campo operativo para material repair rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante qa_matrix: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar material repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar material repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MATERIAL_REPAIR_RULE_QA_MATR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MATERIAL_REPAIR_RULE_QA_MATRIX
- Fallback: Reforzar material repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1649 — wardrobe_signature_vendor_repair
- Definición: Campo operativo para wardrobe signature dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe signature como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe signature como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_SIGNATURE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_SIGNATURE_VENDOR_REPAIR
- Fallback: Reforzar wardrobe signature con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1650 — color_palette_vendor_repair
- Definición: Campo operativo para color palette dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar color palette como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar color palette como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COLOR_PALETTE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COLOR_PALETTE_VENDOR_REPAIR
- Fallback: Reforzar color palette con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1651 — silhouette_preference_vendor_repair
- Definición: Campo operativo para silhouette preference dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar silhouette preference como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar silhouette preference como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SILHOUETTE_PREFERENCE_VENDOR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SILHOUETTE_PREFERENCE_VENDOR_REP
- Fallback: Reforzar silhouette preference con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1652 — fabric_preferences_vendor_repair
- Definición: Campo operativo para fabric preferences dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric preferences como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric preferences como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_PREFERENCES_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_PREFERENCES_VENDOR_REPAIR
- Fallback: Reforzar fabric preferences con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1653 — fabric_weight_vendor_repair
- Definición: Campo operativo para fabric weight dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_WEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_WEIGHT_VENDOR_REPAIR
- Fallback: Reforzar fabric weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1654 — fabric_texture_vendor_repair
- Definición: Campo operativo para fabric texture dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fabric texture como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fabric texture como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FABRIC_TEXTURE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FABRIC_TEXTURE_VENDOR_REPAIR
- Fallback: Reforzar fabric texture con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1655 — fit_rules_vendor_repair
- Definición: Campo operativo para fit rules dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar fit rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar fit rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FIT_RULES_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FIT_RULES_VENDOR_REPAIR
- Fallback: Reforzar fit rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1656 — seam_visibility_vendor_repair
- Definición: Campo operativo para seam visibility dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar seam visibility como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar seam visibility como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SEAM_VISIBILITY_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SEAM_VISIBILITY_VENDOR_REPAIR
- Fallback: Reforzar seam visibility con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1657 — drape_behavior_vendor_repair
- Definición: Campo operativo para drape behavior dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar drape behavior como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar drape behavior como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_DRAPE_BEHAVIOR_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_DRAPE_BEHAVIOR_VENDOR_REPAIR
- Fallback: Reforzar drape behavior con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1658 — wrinkle_logic_vendor_repair
- Definición: Campo operativo para wrinkle logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrinkle logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrinkle logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRINKLE_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRINKLE_LOGIC_VENDOR_REPAIR
- Fallback: Reforzar wrinkle logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1659 — support_physics_vendor_repair
- Definición: Campo operativo para support physics dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar support physics como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar support physics como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SUPPORT_PHYSICS_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SUPPORT_PHYSICS_VENDOR_REPAIR
- Fallback: Reforzar support physics con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1660 — layering_logic_vendor_repair
- Definición: Campo operativo para layering logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar layering logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar layering logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LAYERING_LOGIC_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LAYERING_LOGIC_VENDOR_REPAIR
- Fallback: Reforzar layering logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1661 — season_rule_vendor_repair
- Definición: Campo operativo para season rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar season rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar season rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SEASON_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SEASON_RULE_VENDOR_REPAIR
- Fallback: Reforzar season rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1662 — occasion_rule_vendor_repair
- Definición: Campo operativo para occasion rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar occasion rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar occasion rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OCCASION_RULE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OCCASION_RULE_VENDOR_REPAIR
- Fallback: Reforzar occasion rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1663 — body_shape_fit_rule_vendor_repair
- Definición: Campo operativo para body shape fit rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar body shape fit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar body shape fit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODY_SHAPE_FIT_RULE_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODY_SHAPE_FIT_RULE_VENDOR_REPAI
- Fallback: Reforzar body shape fit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1664 — wardrobe_story_logic_vendor_repair
- Definición: Campo operativo para wardrobe story logic dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe story logic como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe story logic como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_STORY_LOGIC_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_STORY_LOGIC_VENDOR_REPA
- Fallback: Reforzar wardrobe story logic con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1665 — bodywear_editorial_limits_vendor_repair
- Definición: Campo operativo para bodywear editorial limits dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar bodywear editorial limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar bodywear editorial limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BODYWEAR_EDITORIAL_LIMITS_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BODYWEAR_EDITORIAL_LIMITS_VENDOR
- Fallback: Reforzar bodywear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1666 — swimwear_editorial_limits_vendor_repair
- Definición: Campo operativo para swimwear editorial limits dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar swimwear editorial limits como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar swimwear editorial limits como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_SWIMWEAR_EDITORIAL_LIMITS_VE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_SWIMWEAR_EDITORIAL_LIMITS_VENDOR
- Fallback: Reforzar swimwear editorial limits con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1667 — lingerie_non_explicit_rule_vendor_repair
- Definición: Campo operativo para lingerie non explicit rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar lingerie non explicit rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar lingerie non explicit rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_LINGERIE_NON_EXPLICIT_RULE_V_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_LINGERIE_NON_EXPLICIT_RULE_VENDO
- Fallback: Reforzar lingerie non explicit rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1668 — adult_context_rule_vendor_repair
- Definición: Campo operativo para adult context rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar adult context rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar adult context rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ADULT_CONTEXT_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ADULT_CONTEXT_RULE_VENDOR_REPAIR
- Fallback: Reforzar adult context rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1669 — no_exploitation_rule_vendor_repair
- Definición: Campo operativo para no exploitation rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar no exploitation rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar no exploitation rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_NO_EXPLOITATION_RULE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_NO_EXPLOITATION_RULE_VENDOR_REPA
- Fallback: Reforzar no exploitation rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_CAMERA_1670 — camera_angle_safety_vendor_repair
- Definición: Campo operativo para camera angle safety dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar camera angle safety como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar camera angle safety como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_CAMERA_ANGLE_SAFETY_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_CAMERA_ANGLE_SAFETY_VENDOR_REPAI
- Fallback: Reforzar camera angle safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_ACTING_1671 — pose_safety_vendor_repair
- Definición: Campo operativo para pose safety dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar pose safety como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar pose safety como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_POSE_SAFETY_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_POSE_SAFETY_VENDOR_REPAIR
- Fallback: Reforzar pose safety con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1672 — styling_alternative_rule_vendor_repair
- Definición: Campo operativo para styling alternative rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar styling alternative rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar styling alternative rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_STYLING_ALTERNATIVE_RULE_VEN_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_STYLING_ALTERNATIVE_RULE_VENDOR_
- Fallback: Reforzar styling alternative rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_1673 — commercial_safe_rewrite_vendor_repair
- Definición: Campo operativo para commercial safe rewrite dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar commercial safe rewrite como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar commercial safe rewrite como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_COMMERCIAL_SAFE_REWRITE_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_COMMERCIAL_SAFE_REWRITE_VENDOR_R
- Fallback: Reforzar commercial safe rewrite con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1674 — accessory_rules_vendor_repair
- Definición: Campo operativo para accessory rules dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar accessory rules como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar accessory rules como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_ACCESSORY_RULES_VENDOR_REPAI_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_ACCESSORY_RULES_VENDOR_REPAIR
- Fallback: Reforzar accessory rules con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1675 — jewelry_limit_vendor_repair
- Definición: Campo operativo para jewelry limit dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar jewelry limit como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar jewelry limit como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_JEWELRY_LIMIT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_JEWELRY_LIMIT_VENDOR_REPAIR
- Fallback: Reforzar jewelry limit con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1676 — prop_material_vendor_repair
- Definición: Campo operativo para prop material dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop material como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop material como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_MATERIAL_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_MATERIAL_VENDOR_REPAIR
- Fallback: Reforzar prop material con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1677 — prop_weight_vendor_repair
- Definición: Campo operativo para prop weight dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop weight como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop weight como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_WEIGHT_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_WEIGHT_VENDOR_REPAIR
- Fallback: Reforzar prop weight con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1678 — prop_scale_vendor_repair
- Definición: Campo operativo para prop scale dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop scale como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop scale como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_SCALE_VENDOR_REPAIR_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_SCALE_VENDOR_REPAIR
- Fallback: Reforzar prop scale con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1679 — hand_object_contact_vendor_repair
- Definición: Campo operativo para hand object contact dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar hand object contact como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar hand object contact como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_HAND_OBJECT_CONTACT_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_HAND_OBJECT_CONTACT_VENDOR_REPAI
- Fallback: Reforzar hand object contact con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LIGHTING_1680 — object_shadow_rule_vendor_repair
- Definición: Campo operativo para object shadow rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object shadow rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object shadow rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_SHADOW_RULE_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_SHADOW_RULE_VENDOR_REPAIR
- Fallback: Reforzar object shadow rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_1681 — brand_logo_restrictions_vendor_repair
- Definición: Campo operativo para brand logo restrictions dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo restrictions como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo restrictions como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_RESTRICTIONS_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_RESTRICTIONS_VENDOR_R
- Fallback: Reforzar brand logo restrictions con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_SCENE_1682 — prop_scene_coherence_vendor_repair
- Definición: Campo operativo para prop scene coherence dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop scene coherence como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop scene coherence como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_SCENE_COHERENCE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_SCENE_COHERENCE_VENDOR_REPA
- Fallback: Reforzar prop scene coherence con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_VIDEO_1683 — object_continuity_video_vendor_repair
- Definición: Campo operativo para object continuity video dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar object continuity video como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar object continuity video como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_OBJECT_CONTINUITY_VIDEO_VEND_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_OBJECT_CONTINUITY_VIDEO_VENDOR_R
- Fallback: Reforzar object continuity video con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1684 — prop_lineage_rule_vendor_repair
- Definición: Campo operativo para prop lineage rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop lineage rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop lineage rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_LINEAGE_RULE_VENDOR_REP_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_LINEAGE_RULE_VENDOR_REPAIR
- Fallback: Reforzar prop lineage rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1685 — floating_cloth_blocker_vendor_repair
- Definición: Campo operativo para floating cloth blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar floating cloth blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar floating cloth blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_FLOATING_CLOTH_BLOCKER_VENDO_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_FLOATING_CLOTH_BLOCKER_VENDOR_RE
- Fallback: Reforzar floating cloth blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1686 — texture_flat_blocker_vendor_repair
- Definición: Campo operativo para texture flat blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar texture flat blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar texture flat blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_TEXTURE_FLAT_BLOCKER_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_TEXTURE_FLAT_BLOCKER_VENDOR_REPA
- Fallback: Reforzar texture flat blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1687 — wrong_style_blocker_vendor_repair
- Definición: Campo operativo para wrong style blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wrong style blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wrong style blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WRONG_STYLE_BLOCKER_VENDOR_R_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WRONG_STYLE_BLOCKER_VENDOR_REPAI
- Fallback: Reforzar wrong style blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_LEGAL_1688 — brand_logo_blocker_vendor_repair
- Definición: Campo operativo para brand logo blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar brand logo blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar brand logo blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_BRAND_LOGO_BLOCKER_VENDOR_RE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_BRAND_LOGO_BLOCKER_VENDOR_REPAIR
- Fallback: Reforzar brand logo blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1689 — unsupported_bodywear_blocker_vendor_repair
- Definición: Campo operativo para unsupported bodywear blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar unsupported bodywear blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar unsupported bodywear blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_UNSUPPORTED_BODYWEAR_BLOCKER_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_UNSUPPORTED_BODYWEAR_BLOCKER_VEN
- Fallback: Reforzar unsupported bodywear blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1690 — prop_physics_blocker_vendor_repair
- Definición: Campo operativo para prop physics blocker dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar prop physics blocker como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar prop physics blocker como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_PROP_PHYSICS_BLOCKER_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_PROP_PHYSICS_BLOCKER_VENDOR_REPA
- Fallback: Reforzar prop physics blocker con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1691 — wardrobe_identity_drift_rule_vendor_repair
- Definición: Campo operativo para wardrobe identity drift rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar wardrobe identity drift rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar wardrobe identity drift rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_WARDROBE_IDENTITY_DRIFT_RULE_PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_WARDROBE_IDENTITY_DRIFT_RULE_VEN
- Fallback: Reforzar wardrobe identity drift rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.

### P360_WARDROBE_1692 — material_repair_rule_vendor_repair
- Definición: Campo operativo para material repair rule dentro de Wardrobe, bodywear editorial adulto, props, materiales y física textil. Debe transformar investigación y canon en decisiones concretas de prompt, cámara, luz, voz, movimiento, wardrobe, escena, QA y sidecar. Variante vendor_repair: especifica cómo se aplica en compilación, auditoría y reparación sin dejar decisión abierta.
- Ejemplo correcto: Usar material repair rule como restricción positiva y QA: declarar rasgo, conectar con escena, validar salida y registrar sidecar.
- Ejemplo incorrecto: Mencionar material repair rule como adorno sin control, o reemplazarlo por rasgo genérico por estética.
- QA: QA_MATERIAL_REPAIR_RULE_VENDOR__PASS exige evidencia explícita en prompt/sidecar/test.
- Fail code: FAIL_MATERIAL_REPAIR_RULE_VENDOR_REPA
- Fallback: Reforzar material repair rule con descriptor concreto, negative/avoid, regla de cámara/luz/movimiento y test de regresión.
