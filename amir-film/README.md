# AMIR Renal & Transplant Center — 90-second Concept Film Package

**An Al Aafiyah Group Healthcare Initiative · Compassion. Precision. Care.**

This folder has everything needed to produce the 90-second architectural concept film.
It also has a rendered preview cut (an animatic) built from the one exterior render supplied.

## Status: what exists and what doesn't

| Deliverable | Status |
|---|---|
| Timecoded storyboard, camera moves and transitions | Done: `01_STORYBOARD.md` |
| Shot-by-shot AI video prompts | Done: `02_AI_SHOT_PROMPTS.md` |
| Full voice-over script and recording notes | Done: `03_VOICEOVER_SCRIPT.md` |
| Music and sound-design plan | Done: `04_MUSIC_AND_SOUND.md` |
| On-screen title list | Done: `05_TITLES.md` |
| Asset-to-scene mapping | Done: `06_ASSET_MAPPING.md` |
| Final QC checklist | Done: `07_QC_CHECKLIST.md` |
| Editable timeline / assembly spec | Done: `08_ASSEMBLY_SPEC.md`, `build/timeline.json`, `build/amir_film.edl` |
| Subtitles (separate SRT) | Done: `subtitles/AMIR_film_EN.srt`, timed to the generated VO |
| **Voice-over (AI scratch VO)** | Generated: ElevenLabs "Oliver – Warm British Narrator", eleven_v4, 67.2 s. `audio/vo_full_take1.mp3` is the raw take; `audio/vo_timeline_90s.wav` places each line at its cue, normalised to −16 LUFS. Use it for approvals; consider a human Malaysian narrator for the final. |
| **Animatic preview** (1080p, 25 fps, exactly 90.00 s, with the VO) | Rendered: `build/AMIR_animatic_clean_1080p.mp4` (no subtitles) and `build/AMIR_animatic_subtitled_1080p.mp4`. Rebuild with `build/make_animatic.py --vo audio/vo_timeline_90s.wav`. |
| Music | **Not included.** No music generator is connected; see the brief in `04`. |
| **Final 4K photoreal film** | **Not rendered.** It needs generated shots (see below) |

### Why the final film isn't rendered yet
- **Video generation:** the Higgsfield account on this session is on the free plan with 0 credits. No NVIDIA NIM connector is installed, and Canva would not connect.
- **Interiors:** there are no source images for scenes 4–6 (clinics, dialysis, theatre, ICU, wards). The animatic shows labelled slates there instead. It does not invent fake interiors.
- **Source image size:** the only render supplied is 1500×844, too small to be a credible 4K master. It is fine as the reference image and start frame for AI generation.
- **Music:** no music generator is connected. `04_MUSIC_AND_SOUND.md` gives a brief for a licensed track or a composer.

### To finish the film
1. Generate the 21 shots in `02_AI_SHOT_PROMPTS.md`. Use the exterior render as the reference or start frame. Budget for about 3 takes per shot.
2. Record or generate the voice-over from `03_VOICEOVER_SCRIPT.md`.
3. Put the shots on the timeline in place of the matching animatic segments, using `build/timeline.json` or `amir_film.edl`.
4. Grade, mix and export to the spec in `08_ASSEMBLY_SPEC.md`: 3840×2160, 25 fps, H.264/H.265, AAC, 90.00 s. Export a clean master with no subtitles plus the SRT.
5. Run `07_QC_CHECKLIST.md` before anything is shown to stakeholders.

## Points that need a decision from Al Aafiyah Group
1. **Floor stacking conflict.** The sources disagree:
   - The render board says L2–5 clinical podium, L6–15 ward tower.
   - The proposal paper says a 5-storey podium plus a 10-storey tower.
   - This brief says L2–7 parking, L8–14 clinical, L15 roof.

   The film is designed so that **no level numbers appear on screen** and the voice-over names no floors. Whichever version the approved drawings confirm, the film stays valid.
2. **Materials.** The render shows cream stone with teal glazing. The brief asks for board-formed concrete.
   - *Working decision:* keep the render's massing, pointed-arch spine, façade rhythm, signage and landscape exactly. Interpret the surfaces as **warm ivory board-formed concrete** close to the render's tone, with bronze and dark-teal detailing.
   - Confirm this before generating shots, because it affects every exterior prompt.
3. **Bed numbers, phases, cost and returns** stay out of the film on purpose, as the brief requires.
4. **The "أمير" signage** must match the approved logo artwork. AI tools warp Arabic script, so add it in compositing from the vector logo, not in generation.

## Folder map
```
amir-film/
  README.md                 ← this file
  01_STORYBOARD.md … 08_ASSEMBLY_SPEC.md
  assets/                   ← supplied render + derived crops
  subtitles/AMIR_film_EN.srt
  build/make_animatic.py    ← rebuilds the animatic (Python + ffmpeg)
  build/timeline.json       ← machine-readable assembly spec
  build/amir_film.edl       ← CMX3600 EDL for Premiere / Resolve
```

*Architectural concept visualization. Subject to detailed design and statutory approvals.*
