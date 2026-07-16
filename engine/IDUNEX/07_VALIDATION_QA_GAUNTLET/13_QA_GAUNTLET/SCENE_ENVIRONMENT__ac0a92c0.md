# QA MODULE — SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10

source_id: `SRC_049_SCENE_ENVIRONMENT_SPATIAL_PHYSICS_ENGINE_FULL10`  
alias: `ENV_PHYSICS_FULL10`  
research_document: `investigacion_forense_scene_environment_spatial_physics_engine_20260616_053247.pdf`  
research_document_sha256: `443ec6a66404a4e70b9ac3d52f7a58da27a57fd10f9e13efba5693f52b3fa451`  
coverage_score: 9  
global_go: false

## Purpose

This module applies forensic scene physics and mise-en-scene checks to IDUNEX image/video prompt packs and sidecars. It does not alter identity canon. It validates environment plausibility, spatial geometry, contact, gravity, occlusion, scale, lighting, reflection, props and continuity.

## PASS/FAIL checklist

| Aspect | PASS | FAIL | Fail code | Fallback |
|---|---|---|---|---|
| Gravity & weight | all objects/subjects have support or intentional suspension | floating object or unsupported subject | ENV-GRAV | add support/contact/shadow language and retest |
| Contact & collision | hands/feet/body contact props and floor correctly | interpenetration or clipping | ENV-COLL | change pose/camera, inpaint or regenerate |
| Scale & proportion | human/object proportions plausible | giant/miniature object or subject | ENV-SCALE | specify relative size and perspective |
| Perspective & depth | coherent vanishing points and floor/wall/depth | impossible geometry or flat/melted space | ENV-PERSP | enforce camera/lens/depth plan |
| Occlusion & layers | foreground occludes background correctly | wrong layer ordering | ENV-OCCL | depth-map guidance or layer repair |
| Lighting & shadows | light direction and contact shadows match | missing or wrong shadow | ENV-LIGHT | specify key/fill/rim/practical lights |
| Reflections | mirrors/water/metal/glass reflect coherent content | empty or wrong reflection | ENV-REFL | explicit reflection prompt or correction |
| Props & decor | props anchored and scene-coherent | floating/melted/cluttered props | ENV-PROP | reduce props and anchor to surfaces |
| Continuity | stable scene across frames | flicker/drift/teleporting | ENV-CONT | seed/continuity_id/frame reference |
| Culture/location | authentic without stereotypes | incongruent PROJECT_DECLARED_LOCALITY/location cues | ENV-BACK | simplify and use context-specific details |

## Sidecar required fields

`scene_type`, `lighting_setup`, `phys_checklist`, `style_ref`, `locale`, `continuity_id`, `fail_codes`, `fallbacks_applied`, `source_ids_used`, `field_ids_used`, `qa_retest_ids`.

## GO policy

`prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; project_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`, `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`, `coverage_score=9`. Coverage 10 requires real output sidecar evidence and hash-verified QA.
