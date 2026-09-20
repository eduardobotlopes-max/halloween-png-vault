# -*- coding: utf-8 -*-
"""Browsable PDF catalogues for the SVG cut files and the tumbler wraps."""
import glob
import io
import os

import pymupdf
from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from style import *
from vaultkit import *

SVG_DIR = os.path.normpath(os.path.join(HERE, "..", "ENTREGAVEIS", "BONUS-2-SVG-Cut-Files"))
WRAP_DIR = os.path.normpath(os.path.join(HERE, "..", "ENTREGAVEIS", "BONUS-3-Tumbler-Wraps"))
W = PAGE_W - 2 * M


def svg_thumb(path, px=180):
    doc = pymupdf.open(path)
    pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(px / 1000, px / 1000), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    doc.close()
    buf = io.BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)
    return ImageReader(buf)


def png_thumb(path, px=420):
    img = Image.open(path)
    img.thumbnail((px, px))
    buf = io.BytesIO()
    img.convert("RGB").save(buf, "PNG")
    buf.seek(0)
    return ImageReader(buf)


def grid_pages(c, items, cols, rows, thumb_fn, title, kicker, bonus_no, subtitle, label_fn,
               cell_ratio=1.0, start_page=3):
    per = cols * rows
    pno = start_page
    for i in range(0, len(items), per):
        background(c)
        c.setFont("TextBold", 9)
        c.setFillColor(INK_2)
        c.drawString(M, PAGE_H - 34, f"{title.upper()}  ·  {i + 1}-{min(i + per, len(items))} of {len(items)}")
        cw = W / cols
        ch = (PAGE_H - 120) / rows
        for j, path in enumerate(items[i:i + per]):
            col, row = j % cols, j // cols
            x = M + col * cw
            y = PAGE_H - 80 - (row + 1) * ch
            box = min(cw - 14, ch - 26)
            bw = box * cell_ratio
            c.setFillColor(WHITE)
            c.setStrokeColor(LINE)
            c.roundRect(x + (cw - bw) / 2 - 4, y + 16, bw + 8, box + 8, 8, stroke=1, fill=1)
            c.drawImage(thumb_fn(path), x + (cw - bw) / 2, y + 20, bw, box,
                        preserveAspectRatio=True, anchor="c", mask=None)
            c.setFont("Text", 6.6)
            c.setFillColor(INK_2)
            c.drawCentredString(x + cw / 2, y + 6, label_fn(path)[:34])
        footer(c, pno)
        c.showPage()
        pno += 1
    return pno


def build_svg_catalogue():
    register_fonts()
    out = os.path.join(OUT_DIR, "BONUS-2-SVG-Catalogue.pdf")
    files = []
    for folder in sorted(os.listdir(SVG_DIR)):
        d = os.path.join(SVG_DIR, folder)
        if os.path.isdir(d):
            files += sorted(glob.glob(os.path.join(d, "*.svg")))
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle("SVG Cut Files Catalogue · The Halloween PNG Vault")
    cover(c, "Browse every file", ["SVG Cut Files", "Catalogue"],
          f"All {len(files)} cut files at a glance, in the same folder order as your download. "
          "Find the one you want here, then open that file from the folder.", 2, ORANGE)
    c.showPage()

    folders = [f for f in sorted(os.listdir(SVG_DIR)) if os.path.isdir(os.path.join(SVG_DIR, f))]
    rows = []
    for f in folders:
        n = len(glob.glob(os.path.join(SVG_DIR, f, "*.svg")))
        rows.append((f[3:].replace("-", " "), f"{n} files", f))
    background(c)
    y = header_band(c, "Folders", "What's in the pack")
    for name, count, folder in rows:
        h = 30
        card(c, M, y - h, W, h)
        c.setFont("TextBold", 10.5)
        c.setFillColor(INK)
        c.drawString(M + 14, y - 20, name)
        c.setFont("Text", 9.5)
        c.setFillColor(PURPLE)
        c.drawRightString(M + W - 14, y - 20, count)
        y -= h + 5
    y -= 8
    card(c, M, y - 54, W, 54, YELLOW_SOFT, YELLOW)
    text_block(c, M + 16, y - 20, "Cut-outs (pumpkin faces, windows, buckles) are real holes in the "
                                  "file, so your machine cuts them without extra work.",
               "Text", 10, W - 32, INK, 14)
    footer(c, 2)
    c.showPage()

    grid_pages(c, files, 6, 8, svg_thumb, "SVG cut files", "Catalogue", 2, "",
               lambda p: os.path.basename(p)[:-4])
    c.save()
    print("built:", out, len(files), "files")


def build_wrap_catalogue():
    register_fonts()
    out = os.path.join(OUT_DIR, "BONUS-3-Tumbler-Wraps-Catalogue.pdf")
    files = sorted(glob.glob(os.path.join(WRAP_DIR, "*.png")))
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle("Tumbler Wraps Catalogue · The Halloween PNG Vault")
    cover(c, "Browse every wrap", ["Tumbler Wraps", "Catalogue"],
          f"All {len(files)} seamless 20oz wraps at a glance. Each one is 2790 x 2460 px at "
          "300 DPI, with edges that line up around the cup.", 3, ORANGE)
    c.showPage()

    background(c)
    y = header_band(c, "Before you print", "How to use these wraps")
    y = section(c, M, y, "Sizing")
    y = bullets(c, M, y, [
        "2790 x 2460 px at 300 DPI: the standard 20oz skinny tumbler wrap.",
        "Print at 100% and mirrored, on sublimation paper.",
        "Leave 2-3 mm overlap where the ends meet, and trim the top and bottom to your cup.",
    ], W)
    y -= 6
    y = section(c, M, y, "Colours")
    y = bullets(c, M, y, [
        "Sublimation shifts colours slightly: always run one test cup before a batch.",
        "The dark backgrounds need a full white polyester coating to stay true.",
    ], W, dot=PURPLE)
    y -= 6
    card(c, M, y - 56, W, 56, GREEN_SOFT, GREEN)
    text_block(c, M + 16, y - 22, "File names tell you the style: motif, palette and background, "
                                  "e.g. tumbler_wrap_07_ghosts_midnight_checks.",
               "Text", 10, W - 32, INK, 14)
    footer(c, 2)
    c.showPage()

    grid_pages(c, files, 3, 4, png_thumb, "Tumbler wraps", "Catalogue", 3, "",
               lambda p: os.path.basename(p)[:-4].replace("tumbler_wrap_", ""), cell_ratio=1.0)
    c.save()
    print("built:", out, len(files), "wraps")


if __name__ == "__main__":
    build_svg_catalogue()
    build_wrap_catalogue()
