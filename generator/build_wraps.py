# -*- coding: utf-8 -*-
"""BONUS #3 · 60 seamless 20oz skinny tumbler wraps (2790 x 2460 px, 300 DPI).

Patterns are built from the same original shapes as the SVG cut files, tiled with
wrap-around so the left and right edges meet with no visible seam.
"""
import glob
import math
import os
import random
import shutil

import pymupdf
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.normpath(os.path.join(HERE, "..", "ENTREGAVEIS", "BONUS-2-SVG-Cut-Files"))
OUT = os.path.normpath(os.path.join(HERE, "..", "ENTREGAVEIS", "BONUS-3-Tumbler-Wraps"))

W, H = 2790, 2460          # 9.3in x 8.2in at 300 DPI
DPI = (300, 300)

PALETTES = {
    "classic": ("#1E1033", "#F97316", "#FBBF24", "#FFF4EB"),
    "midnight": ("#0A0A0A", "#8B5CF6", "#84CC16", "#F5F3FF"),
    "cream": ("#FBF8F4", "#1E1033", "#F97316", "#6D28D9"),
    "coquette": ("#FFE4EF", "#C0267A", "#1E1033", "#FFFFFF"),
    "retro": ("#F6E2C3", "#C2410C", "#166534", "#1E1033"),
    "neon": ("#12002E", "#FF3D8B", "#39FF14", "#FFE600"),
    "slime": ("#0F1B05", "#84CC16", "#FBBF24", "#FFFFFF"),
    "orange": ("#F97316", "#1E1033", "#FFF4EB", "#FBBF24"),
    "purple": ("#5B21B6", "#FBBF24", "#FFFFFF", "#F97316"),
    "mono": ("#FFFFFF", "#0A0A0A", "#525252", "#A3A3A3"),
}

MOTIF_SETS = {
    "ghosts": ["04-Ghosts", "12-Moons-and-Stars"],
    "pumpkins": ["02-Pumpkins", "03-Plain-Pumpkins"],
    "bats": ["01-Bats", "12-Moons-and-Stars"],
    "witchy": ["08-Witch-Hats", "10-Cauldrons", "11-Potion-Bottles"],
    "spooky": ["13-Skulls", "14-Bones", "15-Tombstones"],
    "cats": ["05-Black-Cats", "06-Spiders"],
    "mixed": ["01-Bats", "02-Pumpkins", "04-Ghosts", "08-Witch-Hats", "12-Moons-and-Stars"],
    "graveyard": ["15-Tombstones", "16-Haunted-Houses", "01-Bats"],
    "sweets": ["17-Sweets", "12-Moons-and-Stars"],
}

BACKGROUNDS = ("solid", "stripes", "checks", "dots", "waves", "grid")


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def load_masks(folders, rnd, count=8, size=520):
    """Rasterise a few SVGs from each folder into alpha masks."""
    masks = []
    for folder in folders:
        files = sorted(glob.glob(os.path.join(SVG_DIR, folder, "*.svg")))
        if not files:
            continue
        for fp in rnd.sample(files, min(count, len(files))):
            doc = pymupdf.open(fp)
            pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(size / 1000, size / 1000), alpha=True)
            img = Image.frombytes("RGBA", (pix.width, pix.height), pix.samples)
            alpha = img.split()[3]
            bbox = alpha.getbbox()
            masks.append(alpha.crop(bbox) if bbox else alpha)
            doc.close()
    return masks


def background(img, style, pal, rnd):
    d = ImageDraw.Draw(img)
    bg, c1, c2, c3 = [hex_rgb(c) for c in pal]
    d.rectangle([0, 0, W, H], fill=bg)
    if style == "stripes":
        sw = rnd.choice((90, 130, 180))
        horizontal = rnd.random() < 0.5
        n = (H if horizontal else W) // sw + 2
        for i in range(n):
            if i % 2:
                continue
            if horizontal:
                d.rectangle([0, i * sw, W, i * sw + sw], fill=c1)
            else:
                d.rectangle([i * sw, 0, i * sw + sw, H], fill=c1)
    elif style == "checks":
        sw = rnd.choice((150, 210, 280))
        for row in range(H // sw + 2):
            for col in range(W // sw + 2):
                if (row + col) % 2 == 0:
                    d.rectangle([col * sw, row * sw, col * sw + sw, row * sw + sw], fill=c1)
    elif style == "dots":
        step = rnd.choice((180, 240, 300))
        r = step * rnd.uniform(0.10, 0.18)
        for row in range(H // step + 2):
            for col in range(W // step + 2):
                cx = col * step + (step / 2 if row % 2 else 0)
                cy = row * step
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c1)
    elif style == "waves":
        amp = rnd.uniform(50, 110)
        step = rnd.choice((160, 220))
        t = step * 0.35
        for i in range(H // step + 3):
            y0 = i * step
            cycles = rnd.choice((4, 6, 8))
            pts = [(x, y0 + amp * math.sin(x / W * math.pi * cycles)) for x in range(0, W + 8, 8)]
            d.line(pts, fill=c1, width=int(t), joint="curve")
    elif style == "grid":
        step = rnd.choice((200, 260))
        t = rnd.choice((10, 16))
        for x in range(0, W + step, step):
            d.rectangle([x, 0, x + t, H], fill=c1)
        for y in range(0, H + step, step):
            d.rectangle([0, y, W, y + t], fill=c1)
    return img


def paste_wrapped(img, motif, x, y):
    """Paste with horizontal wrap-around so the seam matches."""
    img.paste(motif, (int(x), int(y)), motif)
    if x < 0:
        img.paste(motif, (int(x + W), int(y)), motif)
    elif x + motif.width > W:
        img.paste(motif, (int(x - W), int(y)), motif)


def coloured(mask, colour, size):
    m = mask.resize((size, int(size * mask.height / mask.width)), Image.LANCZOS)
    layer = Image.new("RGBA", m.size, hex_rgb(colour) + (255,))
    layer.putalpha(m)
    return layer


def make_wrap(path, style, pal_name, motif_key, rnd):
    pal = PALETTES[pal_name]
    img = Image.new("RGBA", (W, H), hex_rgb(pal[0]) + (255,))
    background(img, style, pal, rnd)
    masks = load_masks(MOTIF_SETS[motif_key], rnd, count=4)
    if not masks:
        raise RuntimeError("no motifs found - run build_svg.py first")
    ink = [pal[1], pal[2], pal[3]]

    cols = rnd.choice((5, 6, 7))
    rows = rnd.choice((5, 6))
    cell_w = W / cols
    cell_h = H / rows
    base = int(cell_w * rnd.uniform(0.52, 0.68))
    for r in range(rows + 1):
        for c in range(cols):
            mask = rnd.choice(masks)
            size = int(base * rnd.uniform(0.82, 1.15))
            colour = ink[(r + c) % len(ink)] if rnd.random() < 0.75 else rnd.choice(ink)
            motif = coloured(mask, colour, size)
            if rnd.random() < 0.5:
                motif = motif.rotate(rnd.uniform(-18, 18), expand=True, resample=Image.BICUBIC)
            x = c * cell_w + (cell_w / 2 if r % 2 else 0) - motif.width / 2
            y = r * cell_h - motif.height / 2 + rnd.uniform(-cell_h * 0.08, cell_h * 0.08)
            paste_wrapped(img, motif, x % W if x >= 0 else x, y)
    img.convert("RGB").save(path, "PNG", dpi=DPI, optimize=True)


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    rnd = random.Random(2026)
    combos = []
    pal_names = list(PALETTES)
    motif_keys = list(MOTIF_SETS)
    i = 0
    while len(combos) < 60:
        combos.append((BACKGROUNDS[i % len(BACKGROUNDS)],
                       pal_names[i % len(pal_names)],
                       motif_keys[i % len(motif_keys)]))
        i += 1
    for n, (style, pal, motif) in enumerate(combos, 1):
        name = f"tumbler_wrap_{n:02d}_{motif}_{pal}_{style}.png"
        make_wrap(os.path.join(OUT, name), style, pal, motif, rnd)
        if n % 10 == 0:
            print("  ", n, "wraps")

    with open(os.path.join(OUT, "READ-ME-FIRST.txt"), "w", encoding="utf-8") as f:
        f.write(
            "60 SEAMLESS TUMBLER WRAPS - The Halloween PNG Vault\n"
            "===================================================\n\n"
            "SIZE\n"
            "2790 x 2460 px at 300 DPI (9.3in x 8.2in), the standard 20oz skinny tumbler wrap.\n"
            "The left and right edges line up, so the pattern continues around the cup.\n\n"
            "HOW TO USE\n"
            "1. Open the PNG in your design software (or send it straight to your printer).\n"
            "2. Print with sublimation ink on sublimation paper, mirrored.\n"
            "3. Wrap the print around a white polyester-coated 20oz tumbler, tape it, and press.\n"
            "   Convection oven or tumbler press: follow your press's own time and temperature.\n\n"
            "TIP\n"
            "Leave 2-3 mm of overlap where the ends meet. Trim the top and bottom to your\n"
            "tumbler if it is a different height - the pattern repeats, so nothing important\n"
            "is lost at the edges.\n\n"
            "LICENCE\n"
            "Sell as many finished tumblers as you like. Do not resell or share the files.\n"
        )
    print("wraps:", len(combos))


if __name__ == "__main__":
    build()
