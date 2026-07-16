# AUDIO_SFX_FOLEY_CONTRACT — IDUNEX MOTOR v1.0.0

## Purpose
Define audio/SFX/Foley output as a first-class IDUNEX modality, traced to Profile360, scene physics, QA and sidecar. No audio output can be delivered without QA, fallback and hash lineage.

## Matrices
| Layer | Required decisions | QA evidence | Fallback |
|---|---|---|---|
| Ambiente | city/interior/exterior/stage/weather/time | ambience_profile | reduce to one base bed + one location cue |
| Room tone | noise floor, air, HVAC, crowd bed | room_tone_dbfs | capture/describe 10s neutral tone |
| Pasos | surface, footwear, tempo, distance | footsteps_surface_map | simplify to one surface + tempo grid |
| Ropa/tela | fabric friction, movement, layers | textile_foley_map | isolate fabric, remove impossible rustle |
| Respiración | intensity, distance, emotion | breath_profile | lower breath, lock emotion cue |
| Objetos | weight, material, contact | object_foley_contact | align object sound to visual contact |
| Ciudad | PROJECT_DECLARED_CITY/urban/interior bleed | city_noise_bed | EQ clutter, keep locality cue |
| Escenario | stage, backstage, PA, crowd | stage_space_map | reduce to dry stem + controlled reverb |
| Reverb | room size, decay, pre-delay | reverb_profile | shorten decay, match scene size |
| Paneo | left/right movement and depth | pan_automation | center critical dialogue |
| Mezcla | dialogue/music/SFX balance | mix_notes | duck music under voice |
| LUFS | target integrated loudness | lufs_target | normalize to platform target |
| Master | limiter, true peak, export format | master_chain | lower limiter gain, avoid pumping |

## Negative audio artifacts
Avoid clipping, pumping, metallic reverb, phasing, over-compression, harsh sibilance, muddy low end, inconsistent room tone, off-screen Foley mismatch, AI warble, abrupt cuts and noise bursts.

## QA de sonido
PASS requires ambience, room tone, Foley contact, reverb, pan, LUFS, master, negative artifacts check, fail_code, fallback_fix and sidecar evidence.

## Sidecar de audio
Required fields: audio_scene_id, ambience_profile, room_tone_dbfs, footsteps_surface_map, textile_foley_map, breath_profile, object_foley_contact, reverb_profile, pan_automation, lufs_target, master_chain, audio_fail_codes, fallback_history, audio_hash.
