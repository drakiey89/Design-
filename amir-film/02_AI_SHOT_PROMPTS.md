# 02 — Shot-by-Shot AI Generation Prompts

These prompts work in Seedance 2.5, Kling 3.0, Veo, Runway Gen-4 and NVIDIA Cosmos (via NIM).
- Generate at 16:9 in 1080p, or the model's highest setting; upscale to 2160p afterwards (Topaz).
- Generate at 24 or 25 fps and conform to 25 fps in the edit.
- Generate 5 s or 10 s clips and trim to the storyboard length.

## A. Locks — paste into every prompt

**EXTERIOR LOCK**
> Use the reference image as the exact building. Preserve the tower-on-podium massing, the
> monumental pointed Islamic arch spine running the full tower height, the geometric
> mashrabiya crown, the deeply recessed vertical windows between sculptural fins, the stepped
> podium with landscaped roof terraces, the palm-lined arrival court with fountain, and the
> separate emergency bay with ambulance access. Surfaces are warm ivory board-formed concrete
> with brushed bronze and dark-teal glazing. Do not add wings, storeys or new buildings. No
> morphing, no warping, no flicker. Photorealistic, correct vertical geometry, physically
> plausible smooth camera, natural motion blur.

**INTERIOR LOCK (style bible)**
> Contemporary Islamic tropical-brutalist hospital interior: warm ivory board-formed concrete
> walls, honed natural stone floors, warm timber ceiling baffles and wall panels, brushed bronze
> trims, dark-teal accents, geometric mashrabiya screens casting patterned daylight,
> hospital-grade finishes (seamless vinyl in clinical rooms, hand-wash stations, rounded corners).
> Real daylight plus warm 3000 K practicals. Malaysian patients, families and staff of mixed
> ages and ethnicities; some women in hijab, some clinicians in scrubs or white coats. Natural,
> anatomically correct people moving at realistic speed. No readable text except simple
> wayfinding.

**NEGATIVE (all shots)**
> morphing architecture, extra floors, melting or garbled text, warped Arabic script, flicker,
> jitter, fisheye, drone spin, speed ramp, extra fingers, distorted faces, mannequins, sci-fi
> holograms, blood, surgery in progress, alarms, crying, oversaturation, CGI plastic look,
> watermark

**Workflow for interiors** (there are no source images yet):
1. Generate one keyframe still per shot with a photoreal image model, using the INTERIOR LOCK.
2. Pick the stills together so they read as one building.
3. Animate each approved still with image-to-video.

Never use text-to-video for the final interior shots. Results drift between shots.

---

## B. Shot prompts

### Scene 1 — The Vision
**1.1 · 4 s · image-to-video, start frame = reference render (outpainted to a wide aerial view)**
> Aerial establishing shot of Penang at sunrise, Bayan Lepas district, the Penang Strait
> glimmering in soft haze, low-rise urban fabric and tropical trees. The AMIR hospital tower
> stands as a distinct silhouette in the middle distance. Slow constant forward glide at high
> altitude, 35mm lens, no rotation. Soft pink-gold dawn light. [EXTERIOR LOCK]

**1.2 · 6 s · image-to-video, start frame = reference render**
> Continuous aerial approach to the AMIR Renal & Transplant Center: the drone descends gently
> and pushes in, revealing the full tower, the stepped podium with landscaped roof terraces, the
> palm-lined arrival court and fountain. Sunrise light grazes the board-formed concrete fins.
> The movement eases to a slow finish. 35mm. [EXTERIOR LOCK]

### Scene 2 — The Architectural Landmark
**2.1 · 4.5 s · i2v, reference render**
> Aerial three-quarter view of the tower and podium at golden hour. Slow orbit of no more than
> 15 degrees with a gentle descent. Warm light rakes across the deep window reveals and
> mashrabiya crown, and long shadows fall over the roof gardens. 35mm. [EXTERIOR LOCK]

**2.2 · 4 s · i2v, reference render (cropped to the arch)**
> Low-angle frontal view from the arrival court looking up at the monumental pointed Islamic
> arch spine rising the full height of the tower. Vertical pedestal rise, tilt-shift with
> perfectly parallel verticals. Close detail of the board-formed concrete grain, form-tie holes,
> bronze mullions and teal glass. Golden-hour light. [EXTERIOR LOCK]

**2.3 · 3.5 s · i2v, reference render (cropped to the entrance)**
> Eye-level lateral tracking shot along the arrival court: a Malaysian family, an elderly man
> with a walking cane and a nurse in teal scrubs walk calmly towards the arched glass entrance,
> past palms and the fountain. Natural walking motion, 24mm, 1.5 m height. [EXTERIOR LOCK]

### Scene 3 — Welcome and Arrival
**3.1 · 4 s · i2v, entrance crop**
> Steadicam at walking pace moves under the deep entrance canopy towards tall glazed doors,
> which slide open smoothly. Warm interior light glows beyond. 24mm, eye level, no head bob.
> [EXTERIOR LOCK]

**3.2 · 4.5 s · i2v, interior keyframe K-3.2**
> Double-height hospital lobby: stone floor, timber ceiling baffles, a tall mashrabiya screen
> wall casting geometric sunlight patterns, a reception and registration desk with two staff,
> comfortable seating with families waiting, a wheelchair user being greeted by a staff member.
> Slow continuous dolly forward with slight lateral drift, 18mm, verticals true. [INTERIOR LOCK]

**3.3 · 3.5 s · i2v, reference render (emergency bay crop)**
> A separate covered emergency arrival bay to the side of the main entrance, an ambulance parked
> under the canopy, clear signage reading "EMERGENCY", a calm paramedic and nurse, and the main
> visitor drop-off visible but separate in the background. Locked-off camera with a gentle
> push, 35mm. [EXTERIOR LOCK] (Replace the sign text in compositing if it warps.)

### Scene 4 — Specialist Renal Care
**4.1 · 4.5 s · i2v, keyframe K-4.1**
> Specialist consultation room: a nephrologist in a white coat explains results on a wall
> monitor showing a generic kidney illustration to a middle-aged Malay patient and his wife.
> Warm, attentive body language. Daylight through a mashrabiya screen. Slow push-in, 50mm,
> shallow depth of field. [INTERIOR LOCK]

**4.2 · 4.5 s · i2v, keyframe K-4.2**
> Renal outpatient corridor: wide and calm, with daylight at the far end, timber handrails,
> discreet wayfinding reading "Renal Clinic" and "Dialysis", and staff walking unhurriedly.
> Lateral track parallel to the wall, 24mm, verticals true. [INTERIOR LOCK]

**4.3 · 5 s · i2v, keyframe K-4.3**
> Modern haemodialysis unit: a row of reclining treatment chairs with dialysis machines beside
> each, large windows with tropical greenery outside, a nurse in teal scrubs checking a
> patient's line and sharing a smile, another patient reading. Calm and clean. Slow lateral
> track, 35mm. [INTERIOR LOCK]

### Scene 5 — Clinical Excellence
**5.1 · 3.5 s · keyframe K-5.1**
> Diagnostic imaging suite: a CT scanner in a calm room with a timber feature wall and a
> radiographer at the shielded control window. The camera pushes slowly through an open doorway
> from the control room. 24mm. [INTERIOR LOCK]

**5.2 · 4.5 s · keyframe K-5.2**
> Modern operating theatre: a surgical team in gowns and masks preparing, a laminar-flow
> ceiling, surgical lights and booms, clean steel and teal surfaces, no visible surgery. Slow
> crane down from a high corner, 24mm. [INTERIOR LOCK]

**5.3 · 3.5 s · keyframe K-5.3**
> Critical care unit: a glass-fronted ICU bay with a monitored bed, soft daylight, and a nurse
> at a central station with clear line of sight to the bays. Quiet and orderly. Gentle lateral
> track, 35mm. [INTERIOR LOCK]

**5.4 · 2.5 s · keyframe K-5.4**
> Clean-zone clinical corridor leading to specialist procedure suites: pressure-controlled
> doors, hand-hygiene stations, soft cool lighting balanced with warm timber. Locked-off camera
> with a slight push, 35mm. [INTERIOR LOCK]

### Scene 6 — Recovery and Human Experience
**6.1 · 4.5 s · keyframe K-6.1**
> Single-bed inpatient room in morning light: the patient sits up comfortably, an adult daughter
> in hijab beside them, a timber headwall, a large window with a view over Penang towards the
> strait. Slow push towards the window, 35mm. [INTERIOR LOCK]

**6.2 · 3 s · keyframe K-6.2**
> Ward nurse station: warm lighting and timber counter, two nurses reviewing a tablet together,
> calm. Lateral track, 35mm. [INTERIOR LOCK]

**6.3 · 4.5 s · keyframe K-6.3**
> Family lounge: families resting, tea service, tropical indoor planting, mashrabiya shadows on
> the floor, and a discreet sign to the surau. Slow lateral drift, 24mm. [INTERIOR LOCK]

### Scene 7 — Healing Landscape
**7.1 · 4.5 s · i2v, reference render (terrace crop) or keyframe K-7.1**
> Podium roof garden terrace: shaded timber benches beneath a concrete pergola, frangipani,
> palms and ferns, an elderly woman in a wheelchair with her carer in dappled late-afternoon
> light, and the tower rising behind. Slow lateral track, 24mm. [EXTERIOR LOCK]

**7.2 · 5.5 s · i2v, reference render**
> From the terrace edge the camera rises smoothly and pulls back to reveal the complete tower,
> podium and landscaped 2.5-acre site at late golden hour. No rotation. 35mm aerial.
> [EXTERIOR LOCK]

### Scene 8 — The Final Pitch
**8.1 · 6 s · i2v, reference render relit to blue hour**
> Blue hour after sunset: the AMIR tower glows warmly from within, the pointed-arch spine is
> softly illuminated, the façade fins are gently uplit, and soft vehicle light trails pass the
> drop-off. Gentle pull-back that eases to a complete stop; hold still. 35mm. [EXTERIOR LOCK]
> Leave clean negative space in the lower third for the end titles.

---

## C. Generation settings (starting points)
| Setting | Value |
|---|---|
| Aspect / resolution | 16:9, 1080p native, upscale to 2160p |
| Duration | 5 s (trim) or 10 s for shots of 5 s or more |
| Motion strength | Low to medium (architectural). Raise only for walking people. |
| Seed | Lock the seed per scene once a good look is found |
| Takes | 3 per shot. Pick by QC (`07`), not by "wow" factor. |
| Signage / Arabic | Leave blank or simple in generation; composite the vector logo afterwards |
