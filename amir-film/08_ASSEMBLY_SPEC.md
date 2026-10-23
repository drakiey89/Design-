# 08 — Editable Production Timeline and Assembly Spec

The single source of truth is `build/timeline.json`: scenes, shot in/out points, titles and VO cues.
`build/amir_film.edl` (CMX3600, 25 fps, non-drop) is derived from it. Import it into DaVinci Resolve or Premiere,
then relink each `GEN_x.x.mov` to the generated shot.

## Sequence settings
| Item | Value |
|---|---|
| Timeline | 3840×2160, 25 fps, progressive, Rec.709 / Gamma 2.4 |
| Length | 00:00:00:00 – 00:01:30:00 (2,250 frames). The last frame is 00:01:29:24. |
| Working codec | ProRes 422 HQ or DNxHR HQX for generated and upscaled shots |

## Track layout
| Track | Content |
|---|---|
| V1 | Generated shots 1.1–8.1, following the EDL |
| V2 | Composited signage and logo fixes (أمير wordmark, the "EMERGENCY" sign, façade lettering) |
| V3 | Titles T1–T7 and the end card T8a–c (see `05_TITLES.md`) |
| V4 | Disclosure D1 and D2 |
| V5 | Subtitles: **review copy only**. Disable this track for the clean master. |
| A1 | Voice-over (cues in `03`) |
| A2–A3 | Music, stereo (see `04`) |
| A4–A6 | Ambience and SFX by scene |

## Assembly steps
1. Import the EDL and relink the V1 media. Set the trims so each shot fills its slot exactly.
2. Add the transitions listed in `01_STORYBOARD.md`; the rest are straight cuts. The animatic uses a 0.5 s dissolve at every scene boundary as a placeholder.
3. Composite the brand signage over the generated plates on V2. Track and corner-pin it on moving shots.
4. Grade:
   - Golden hour from scene 1 to the end of scene 7: warm highlights, neutral mids, teal kept in the glazing.
   - Interiors: neutral daylight at 5,000–5,600 K, warm practicals.
   - Scene 8: a blue-hour shift over a 25-frame dissolve.
5. Add titles from `05_TITLES.md` on V3 and V4.
6. Mix the audio as in `04_MUSIC_AND_SOUND.md`.
7. Export the deliverables below and run `07_QC_CHECKLIST.md`.

## Deliverables
| File | Spec |
|---|---|
| `AMIR_ConceptFilm_90s_UHD_CLEAN.mp4` | 3840×2160, 25p, H.264 High L5.1 at 45 Mbps (or H.265 Main10 at 30 Mbps), AAC-LC 320 kbps 48 kHz, −16 LUFS. **No subtitles.** |
| `AMIR_ConceptFilm_90s_UHD_SUBTITLED.mp4` | As above, with subtitles burned in (for social and email review) |
| `AMIR_ConceptFilm_90s_EN.srt` | From `subtitles/AMIR_film_EN.srt` |
| `AMIR_ConceptFilm_90s_HD_CLEAN.mp4` | 1920×1080 at 16 Mbps, for email and laptops |
| `AMIR_ConceptFilm_ProRes_master.mov` | ProRes 422 HQ, for archive and venue playback |

## Reference ffmpeg commands
```bash
# Final UHD clean export from a ProRes master
ffmpeg -i master.mov -c:v libx264 -profile:v high -level 5.1 -preset slow -b:v 45M -maxrate 55M -bufsize 90M \
  -pix_fmt yuv420p -r 25 -c:a aac -b:a 320k -ar 48000 -t 90 -movflags +faststart AMIR_ConceptFilm_90s_UHD_CLEAN.mp4
# Subtitled review copy
ffmpeg -i AMIR_ConceptFilm_90s_UHD_CLEAN.mp4 -vf "subtitles=subtitles/AMIR_film_EN.srt" -c:a copy AMIR_ConceptFilm_90s_UHD_SUBTITLED.mp4
# Verify duration and frame count
ffprobe -v error -count_frames -show_entries stream=nb_read_frames,r_frame_rate -show_entries format=duration AMIR_ConceptFilm_90s_UHD_CLEAN.mp4
```

## Animatic (already rendered)
`build/make_animatic.py` rebuilds the 1080p preview from `timeline.json`. When a VO WAV exists, run:
`python3 build/make_animatic.py --vo path/to/vo.wav`. The VO must already be laid out on a 90 s timeline.
