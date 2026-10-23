# 06 — Asset-to-Scene Mapping

## Supplied assets (audited)
| ID | File | Source | Size | Content | Notes |
|---|---|---|---|---|---|
| A01 | `assets/A01_exterior_render_board.jpg` | User upload (supplied twice; the files are byte-identical) | 1500×844 | Exterior render on a presentation board: tower, podium, pointed-arch spine with أمير, palms, fountain, ambulance bay, signage pylon; the left third is a text panel | **Primary building identity.** Too low-resolution to be a 4K plate itself; use it as the reference or start frame. Board text (L2–5 / L6–15 / bed phases) must not appear in the film; the animatic crops it out. **The façade lettering "AMIR RENAL AND TRANSPLANT CENTER" and the emergency sign in this render are AI-garbled.** Replace them in compositing. |
| A01a | `assets/A01a_building_crop.jpg` | Derived crop | 940×529 | Upper building, arch spine, crown | Reference for 2.2 and 8.1 |
| A01b | `assets/A01b_entrance_crop.jpg` | Derived crop | 700×284 | Entrance, palms, emergency bay | Reference for 2.3, 3.1, 3.3 |
| P01 | `AMIR_Kertas_Cadangan_…pdf` (33 pp) | User upload | — | Proposal paper (BM): Lot PT 3095, a 5-storey podium plus a 10-storey tower, 200 beds in two phases, the financial structure | Used only to check facts. **No figures from it go on screen.** |
| B01 | `../amir-brutalist/` | Earlier session output | — | Brutalist reinterpretation prompt and a Gamma still | Mood reference for concrete texture only; that still is a *different* building design and must not be cut into the film |

**No supplied video files were found** in this session. If AMIR video exists, add it here and re-check continuity.

## Scene-by-scene mapping
| Shot | Primary asset | Method | Status |
|---|---|---|---|
| 1.1 | A01 (outpainted wide) | Outpaint, then i2v | To generate |
| 1.2 | A01 | i2v | To generate (animatic: 2.5D push on A01) |
| 2.1 | A01 | i2v | To generate (animatic: A01) |
| 2.2 | A01a | i2v | To generate (animatic: tilt on A01) |
| 2.3 | A01b | i2v | To generate |
| 3.1 | A01b | i2v | To generate (animatic: push on A01b) |
| 3.2 | K-3.2 (new keyframe) | t2i, then i2v | To generate |
| 3.3 | A01b (emergency bay) | i2v | To generate |
| 4.1–4.3 | K-4.1…K-4.3 | t2i, then i2v | To generate (animatic: slate) |
| 5.1–5.4 | K-5.1…K-5.4 | t2i, then i2v | To generate (animatic: slate) |
| 6.1–6.3 | K-6.1…K-6.3 | t2i, then i2v | To generate (animatic: slate) |
| 7.1 | A01 terrace / K-7.1 | i2v | To generate (animatic: lateral move on A01 podium) |
| 7.2 | A01 | i2v | To generate |
| 8.1 | A01 relit to blue hour | Relight, then i2v | To generate (animatic: A01 with a blue-hour grade) |

**Still needed from the client:** approved architectural drawings (plans, sections, elevations), the vector logo (AMIR and أمير),
any interior design concepts, and the brand fonts if they exist.
