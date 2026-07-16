# SUNO FINAL TEST — PROJECT_FIXTURE_VALIDATION_001

## MUSIC IDENTITY
Synthetic character music validation, not celebrity imitation. Genre and vocal mode must trace to Profile360 music fields.

## PARAMETERS
music_identity_signature: declared. genre_primary: project-defined. genre_secondary: controlled fusion only. BPM: 82-108 for validation. vocal_mode: spoken-sung hybrid. spoken_vs_sung_ratio: 60/40. hook_style: concise. verse_density: medium. production_texture: cinematic/modern. language_variant: Latam Spanish unless otherwise declared.

## SONG STRUCTURE
[Intro] atmosphere. [Verse 1] identity-safe narration. [Pre-Chorus] emotional lift. [Chorus/Hook] short memorable phrase. [Verse 2] project-safe context. [Bridge] reflective turn. [Final Hook] controlled repeat. [Outro] clean ending.

## NEGATIVE MUSIC TAGS
no generic pop, no childish voice, no celebrity imitation, no wrong accent, no unrelated lyrics, no invented biography, no excessive autotune unless requested.

## EXPECTED OUTPUT
Music prompt/lyrics fixture or formal mock with QA evidence and sidecar trace.

## FALLBACK FIXES
If generic, tighten genre+BPM+instrument palette. If too sung, increase spoken_vs_sung_ratio. If wrong accent, lock language_variant/accent_policy.

## REQUIRED FIELD IDS
P360_MUSIC_0239, P360_MUSIC_0241, P360_MUSIC_0245, P360_MUSIC_0249

## REQUIRED ADAPTER
suno_music_adapter

## GOLDEN TEST
GT_SUNO_LYRIC_PERSONALITY
## RETEST PROTOCOL
If output is generic, wrong-accent, too childish, unrelated to canon or over-autotuned, retest with tightened BPM, genre_primary, instrument palette, spoken_vs_sung_ratio and negative_music_tags. Record fallback and retest hash.

## PRODUCTION REJECTION CONDITIONS
Reject if lyrics invent biography, imitate a celebrity, drift language variant, or cannot be traced to field_ids and source_ids.
