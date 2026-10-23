#!/usr/bin/env python3
"""Build the AMIR 90-second animatic (1080p, 25 fps) from timeline.json.

Usage: python3 make_animatic.py [--vo path/to/voiceover.wav]

Outputs (in this folder):
  AMIR_animatic_clean_1080p.mp4      no subtitles (presentation version)
  AMIR_animatic_subtitled_1080p.mp4  SRT burned in (review version)
  amir_film.edl                      CMX3600 EDL with GEN_x.x placeholders

The animatic uses only the supplied exterior render. Interior scenes are labelled
slates until the generated shots exist. It is a timing/structure preview, not the film.
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
W, H = 1920, 1080
TEAL, IVORY, GOLD = (15, 76, 74), (244, 237, 225), (176, 141, 87)
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_IT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
XFADE = 0.5  # seconds of cross-dissolve either side of a scene boundary

tl = json.loads((HERE / "timeline.json").read_text())
FPS, DUR = tl["fps"], tl["duration_s"]
NFRAMES = int(round(FPS * DUR))


def font(path, size):
    return ImageFont.truetype(path, size)


def build_canvas():
    """1500x844 plate: sharp building half of the board centred on a blurred extension."""
    src = Image.open(ROOT / "assets" / "A01_exterior_render_board.jpg").convert("RGB")
    # x 620-1262 excludes the board's text panel (left) and phase/bed graphics (right)
    right = src.crop((620, 0, 1262, 844))
    bg = right.resize((1500, 844), Image.BICUBIC).filter(ImageFilter.GaussianBlur(28))
    bg = ImageEnhance.Brightness(bg).enhance(0.85)
    mask = Image.new("L", right.size, 255)
    edge = ImageDraw.Draw(mask)
    for i in range(40):  # feather the left/right seams
        a = int(255 * i / 40)
        edge.line([(i, 0), (i, 843)], fill=a)
        edge.line([(right.width - 1 - i, 0), (right.width - 1 - i, 843)], fill=a)
    bg.paste(right, ((1500 - right.width) // 2, 0), mask)
    return bg


CANVAS = build_canvas()
SLATE_BG = ImageEnhance.Brightness(
    Image.blend(CANVAS.filter(ImageFilter.GaussianBlur(18)), Image.new("RGB", CANVAS.size, TEAL), 0.6)
).enhance(0.55)


def ease(p):
    p = min(max(p, 0.0), 1.0)
    return p * p * (3 - 2 * p)


def window(img, cx, cy, w):
    h = w * 9 / 16
    cx = min(max(cx, w / 2), img.width - w / 2)
    cy = min(max(cy, h / 2), img.height - h / 2)
    box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    return img.transform((W, H), Image.EXTENT, box, Image.BICUBIC)


def bluehour(frame):
    f = ImageEnhance.Brightness(frame).enhance(0.62)
    f = Image.blend(f, Image.new("RGB", f.size, (25, 45, 95)), 0.28)
    return ImageEnhance.Contrast(f).enhance(1.08)


def tracked(draw, xy, text, fnt, fill, tracking=0, anchor_center=False):
    widths = [draw.textlength(c, font=fnt) for c in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x, y = xy
    if anchor_center:
        x -= total / 2
    for c, cw in zip(text, widths):
        draw.text((x, y), c, font=fnt, fill=fill)
        x += cw + tracking
    return total


def text_layer(items):
    """items: list of (text, font, fill, (x, y), tracking, centered). Returns RGBA layer with soft shadow."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d, ds = ImageDraw.Draw(layer), ImageDraw.Draw(shadow)
    for text, fnt, fill, (x, y), tr, c in items:
        tracked(ds, (x + 2, y + 3), text, fnt, (0, 0, 0, 120), tr, c)
        tracked(d, (x, y), text, fnt, fill, tr, c)
    shadow = shadow.filter(ImageFilter.GaussianBlur(6))
    return Image.alpha_composite(shadow, layer)


# --- pre-rendered overlays -------------------------------------------------
OVERLAYS = []  # (t_in, t_out, layer)
GRADIENT = Image.new("RGBA", (W, H), (0, 0, 0, 0))
_g = ImageDraw.Draw(GRADIENT)
for _y in range(H // 2, H):  # soft bottom darkening so titles stay legible
    _g.line([(0, _y), (W, _y)], fill=(0, 0, 0, int(120 * ((_y - H / 2) / (H / 2)) ** 1.5)))


def add(t_in, t_out, layer):
    OVERLAYS.append((t_in, t_out, layer))


for sc in tl["scenes"]:
    if sc.get("title"):
        if sc.get("title_style") == "serif":
            lay = text_layer([(sc["title"], font(SERIF, 64), IVORY + (255,), (W / 2, 760), 6, True)])
        else:
            lay = text_layer([(sc["title"], font(SANS, 30), IVORY + (255,), (130, 880), 7, False)])
        add(sc["title_in"], sc["title_out"], lay)
    if sc["animatic"]["type"] == "slate":
        a = sc["animatic"]
        items = [(f"SCENE {sc['n']} — {sc['name']}", font(SANS, 34), GOLD + (255,), (W / 2, 250), 6, True),
                 ("Concept shots to be generated — see 02_AI_SHOT_PROMPTS.md", font(SANS, 24),
                  IVORY + (190,), (W / 2, 310), 1, True)]
        for i, line in enumerate(a["lines"]):
            items.append((line, font(SANS, 30), IVORY + (235,), (W / 2, 420 + i * 58), 1, True))
        add(sc["in"], sc["out"], text_layer(items))

disc = tl["disclosure"]
add(1.0, 9.0, text_layer([(disc, font(SANS, 17), IVORY + (170,), (W - 40 - 790, 32), 0, False)]))
add(86.0, 90.5, text_layer([(disc, font(SANS, 16), IVORY + (150,), (W / 2, H - 42), 0, True)]))
ec = tl["end_card"]["lines"]
add(85.0, 90.5, text_layer([(ec[0], font(SERIF, 72), IVORY + (255,), (W / 2, 430), 6, True)]))
add(85.5, 90.5, text_layer([(ec[1], font(SERIF_IT, 38), GOLD + (255,), (W / 2, 545), 1, True)]))
add(86.0, 90.5, text_layer([(ec[2], font(SANS, 24), IVORY + (220,), (W / 2, 615), 5, True)]))
rule = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(rule).line([(W / 2 - 160, 525), (W / 2 + 160, 525)], fill=GOLD + (230,), width=2)
add(85.3, 90.5, rule)
add(0, 90.5, text_layer([("ANIMATIC PREVIEW — NOT FINAL FILM", font(SANS, 16), IVORY + (140,), (40, 32), 3, False)]))


def overlay_alpha(t, t_in, t_out, fade=0.6):
    if t < t_in or t > t_out:
        return 0.0
    return min(1.0, (t - t_in) / fade, (t_out - t) / fade if t_out < DUR else 1.0)


# --- scene rendering --------------------------------------------------------
def render_scene(sc, t):
    a = sc["animatic"]
    span = sc["out"] - sc["in"]
    if a["type"] == "plate":
        end = a.get("hold_from", sc["out"])
        p = ease((t - sc["in"]) / (end - sc["in"]))
        f, to = a["from"], a["to"]
        cx, cy, w = (f[i] + (to[i] - f[i]) * p for i in range(3))
        frame = window(CANVAS, cx, cy, w)
        if a.get("grade") == "bluehour":
            frame = Image.blend(frame, bluehour(frame), ease((t - sc["in"]) / 1.5))
        return frame
    p = (t - sc["in"]) / span  # slate: slow drift over the blurred plate
    return window(SLATE_BG, 700 + 100 * p, 422, 1300)


def scene_at(t):
    for i, sc in enumerate(tl["scenes"]):
        if sc["in"] <= t < sc["out"] or i == len(tl["scenes"]) - 1:
            return i


def frame_at(n):
    t = n / FPS
    scenes = tl["scenes"]
    i = scene_at(t)
    frame = render_scene(scenes[i], t)
    # cross-dissolve around boundaries
    if i > 0 and t - scenes[i]["in"] < XFADE:
        prev = render_scene(scenes[i - 1], t)
        frame = Image.blend(prev, frame, 0.5 + (t - scenes[i]["in"]) / (2 * XFADE))
    elif i < len(scenes) - 1 and scenes[i]["out"] - t < XFADE:
        nxt = render_scene(scenes[i + 1], t)
        frame = Image.blend(frame, nxt, 0.5 - (scenes[i]["out"] - t) / (2 * XFADE))
    if t < 1.0:
        frame = Image.blend(Image.new("RGB", frame.size), frame, ease(t / 1.0))
    if t >= 85.0:  # dim the plate under the end card
        frame = ImageEnhance.Brightness(frame).enhance(1 - 0.35 * ease((t - 85.0) / 1.0))
    out = Image.alpha_composite(frame.convert("RGBA"), GRADIENT)
    for t_in, t_out, lay in OVERLAYS:
        al = overlay_alpha(t, t_in, t_out)
        if al > 0:
            if al < 1:
                r, g, b, A = lay.split()
                lay = Image.merge("RGBA", (r, g, b, A.point(lambda v: int(v * al))))
            out = Image.alpha_composite(out, lay)
    return out.convert("RGB")


def write_edl():
    def tc(s):
        f = int(round(s * FPS))
        return f"{f // (FPS * 3600):02d}:{f // (FPS * 60) % 60:02d}:{f // FPS % 60:02d}:{f % FPS:02d}"
    lines = ["TITLE: AMIR_CONCEPT_FILM_90S", "FCM: NON-DROP FRAME", ""]
    n = 1
    for sc in tl["scenes"]:
        for sh in sc["shots"]:
            d = sh["out"] - sh["in"]
            lines.append(f"{n:03d}  {sh['src'].replace('.', '_'):<8} V     C        "
                         f"{tc(0)} {tc(d)} {tc(sh['in'])} {tc(sh['out'])}")
            lines.append(f"* FROM CLIP NAME: {sh['src']}.mov   SCENE {sc['n']} {sc['name']}")
            n += 1
    (HERE / "amir_film.edl").write_text("\n".join(lines) + "\n")


def main():
    vo = sys.argv[sys.argv.index("--vo") + 1] if "--vo" in sys.argv else None
    write_edl()
    clean = HERE / "AMIR_animatic_clean_1080p.mp4"
    audio = (["-i", vo] if vo else ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"])
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", *audio, "-map", "0:v", "-map", "1:a",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "320k", "-af", "apad", "-t", f"{DUR}", "-movflags", "+faststart", str(clean)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for n in range(NFRAMES):
        proc.stdin.write(frame_at(n).tobytes())
        if n % 250 == 0:
            print(f"frame {n}/{NFRAMES}", flush=True)
    proc.stdin.close()
    if proc.wait():
        sys.exit("ffmpeg failed")
    srt = ROOT / "subtitles" / "AMIR_film_EN.srt"
    style = "FontName=DejaVu Sans,FontSize=13,PrimaryColour=&H00E1EDF4,OutlineColour=&H80000000,BorderStyle=1,Outline=1,Shadow=0,MarginV=22"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(clean), "-vf",
                    f"subtitles={srt}:force_style='{style}'", "-c:v", "libx264", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart",
                    str(HERE / "AMIR_animatic_subtitled_1080p.mp4")], check=True)
    print("done")


if __name__ == "__main__":
    main()
