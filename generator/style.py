# -*- coding: utf-8 -*-
"""Shared visual system: page size, palette, fonts, text helpers and vector art."""
import math
import os

from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

PAGE_W, PAGE_H = A4            # 595 x 842 pt, UK standard
M = 40                         # page margin

NIGHT   = HexColor("#1E1033")
NIGHT_2 = HexColor("#2C1A4A")
PURPLE  = HexColor("#6D28D9")
PURPLE_SOFT = HexColor("#EFE7FF")
ORANGE  = HexColor("#F97316")
ORANGE_DARK = HexColor("#C2410C")
ORANGE_SOFT = HexColor("#FFEBD9")
YELLOW  = HexColor("#FBBF24")
YELLOW_SOFT = HexColor("#FFF4D1")
GREEN   = HexColor("#16A34A")
GREEN_SOFT = HexColor("#DCF5E4")
CREAM   = HexColor("#FBF8F4")
INK     = HexColor("#1A1325")
INK_2   = HexColor("#4A4257")
LINE    = HexColor("#E6DDF0")
WHITE   = HexColor("#FFFFFF")
GHOST   = HexColor("#F7F5FF")

# category -> (main colour, soft colour, icon)
TEAL = HexColor("#0F766E")
TEAL_SOFT = HexColor("#D5F2EE")
PINK = HexColor("#C0267A")
PINK_SOFT = HexColor("#FCE3F0")

CATEGORIES = {
    "Party Games":           (ORANGE, ORANGE_SOFT, "pumpkin"),
    "Treasure Hunts":        (TEAL, TEAL_SOFT, "chest"),
    "Challenges":            (PURPLE, PURPLE_SOFT, "spider"),
    "Mystery Boxes":         (ORANGE_DARK, ORANGE_SOFT, "cauldron"),
    "Spooky Night Fun":      (NIGHT_2, PURPLE_SOFT, "bat"),
    "Easy Crafts":           (PINK, PINK_SOFT, "hat"),
    "Quiet-Time Printables": (GREEN, GREEN_SOFT, "ghost"),
}

_FDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
_REG = False


def register_fonts():
    """OFL fonts: Baloo 2 for titles, Nunito for text."""
    global _REG
    if _REG:
        return
    pdfmetrics.registerFont(TTFont("Display", os.path.join(_FDIR, "Baloo2-XBold.ttf")))
    pdfmetrics.registerFont(TTFont("Text", os.path.join(_FDIR, "Nunito-Reg.ttf")))
    pdfmetrics.registerFont(TTFont("TextBold", os.path.join(_FDIR, "Nunito-Bold.ttf")))
    _REG = True


# ---------------------------------------------------------------- text
def width(txt, font, size):
    return pdfmetrics.stringWidth(txt, font, size)


def fit(txt, font, size_max, max_w, size_min=10):
    s = size_max
    while s > size_min and width(txt, font, s) > max_w:
        s -= 0.5
    return s


def wrap(txt, font, size, max_w):
    words, lines, cur = txt.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if width(t, font, size) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(c, x, y, txt, font, size, max_w, color=INK, leading=None):
    """Draw wrapped text from the top (y = first baseline). Returns y after the block."""
    leading = leading or size * 1.32
    c.setFont(font, size)
    c.setFillColor(color)
    for ln in wrap(txt, font, size, max_w):
        c.drawString(x, y, ln)
        y -= leading
    return y


def centred(c, x, y, txt, font, size, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawCentredString(x, y, txt)


def outlined(c, x, y, txt, font, size, fill, stroke, sw=3, centre=True):
    """Title lettering with a thick outline (drawn as stroke then fill)."""
    c.saveState()
    c.setLineJoin(1)
    c.setLineWidth(sw * 2)
    xx = x - width(txt, font, size) / 2 if centre else x
    c.setStrokeColor(stroke)
    t = c.beginText(xx, y)
    t.setFont(font, size)
    t.setTextRenderMode(1)          # stroke only: the outline
    t.textOut(txt)
    c.drawText(t)
    c.setFillColor(fill)
    t = c.beginText(xx, y)          # text render mode persists in PDF, so reset it explicitly
    t.setFont(font, size)
    t._code.append("0 Tr")          # reportlab skips setTextRenderMode(0) when it thinks it is already 0
    t.textOut(txt)
    c.drawText(t)
    c.restoreState()


# ---------------------------------------------------------------- vector art
def star(c, x, y, r, color=YELLOW, points=5):
    p = c.beginPath()
    for i in range(points * 2):
        a = math.pi / 2 + i * math.pi / points
        rr = r if i % 2 == 0 else r * 0.45
        px, py = x + rr * math.cos(a), y + rr * math.sin(a)
        (p.moveTo if i == 0 else p.lineTo)(px, py)
    p.close()
    c.setFillColor(color)
    c.drawPath(p, stroke=0, fill=1)


def sparkles(c, pts, color=YELLOW):
    for (x, y, r) in pts:
        star(c, x, y, r, color)


def pumpkin(c, x, y, r, face=True, line=None, fill=ORANGE, lw=2.2):
    """Pumpkin centred on (x, y) with half-width r. line=colour draws outline art."""
    c.saveState()
    h = r * 0.82
    if line:
        c.setStrokeColor(line); c.setLineWidth(lw); c.setFillColor(WHITE)
    else:
        c.setFillColor(fill)
    # three overlapping lobes
    for dx, w in ((-0.42, 0.62), (0.42, 0.62), (0, 0.66)):
        c.ellipse(x + dx * r - w * r, y - h, x + dx * r + w * r, y + h,
                  stroke=1 if line else 0, fill=1)
    if not line:
        c.setStrokeColor(ORANGE_DARK); c.setLineWidth(max(1, r * 0.04))
        for dx in (-0.36, 0.36):
            c.bezier(x + dx * r, y + h * 0.9, x + dx * r * 1.35, y + h * 0.3,
                     x + dx * r * 1.35, y - h * 0.3, x + dx * r, y - h * 0.9)
    # stem
    c.setFillColor(GREEN if not line else WHITE)
    p = c.beginPath()
    p.moveTo(x - r * 0.1, y + h * 0.85); p.lineTo(x - r * 0.06, y + h * 1.25)
    p.lineTo(x + r * 0.16, y + h * 1.32); p.lineTo(x + r * 0.12, y + h * 0.85); p.close()
    c.drawPath(p, stroke=1 if line else 0, fill=1)
    if face:
        c.setFillColor(NIGHT if not line else WHITE)
        for sx in (-1, 1):
            p = c.beginPath()
            p.moveTo(x + sx * r * 0.42, y + h * 0.05); p.lineTo(x + sx * r * 0.18, y + h * 0.05)
            p.lineTo(x + sx * r * 0.3, y + h * 0.42); p.close()
            c.drawPath(p, stroke=1 if line else 0, fill=1)
        p = c.beginPath()
        p.moveTo(x - r * 0.5, y - h * 0.22)
        p.curveTo(x - r * 0.3, y - h * 0.7, x + r * 0.3, y - h * 0.7, x + r * 0.5, y - h * 0.22)
        p.lineTo(x + r * 0.26, y - h * 0.34); p.lineTo(x + r * 0.14, y - h * 0.2)
        p.lineTo(x, y - h * 0.34); p.lineTo(x - r * 0.14, y - h * 0.2)
        p.lineTo(x - r * 0.26, y - h * 0.34); p.close()
        c.drawPath(p, stroke=1 if line else 0, fill=1)
    c.restoreState()


def ghost(c, x, y, s, line=None, fill=GHOST, lw=2.2):
    """Friendly ghost, (x, y) = centre, s = half-width."""
    c.saveState()
    p = c.beginPath()
    top = y + s * 1.1
    p.moveTo(x - s, y - s * 0.9)
    p.lineTo(x - s, y + s * 0.1)
    p.curveTo(x - s, top + s * 0.25, x + s, top + s * 0.25, x + s, y + s * 0.1)
    p.lineTo(x + s, y - s * 0.9)
    n = 4
    for i in range(n):
        x0 = x + s - i * (2 * s / n)
        x1 = x0 - 2 * s / n
        p.curveTo(x0 - s * 0.12, y - s * 1.2, x1 + s * 0.12, y - s * 1.2, x1, y - s * 0.9)
    p.close()
    if line:
        c.setStrokeColor(line); c.setLineWidth(lw); c.setFillColor(WHITE)
        c.drawPath(p, stroke=1, fill=1)
    else:
        c.setFillColor(fill); c.setStrokeColor(LINE); c.setLineWidth(1)
        c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(NIGHT if not line else WHITE)
    if line:
        c.setStrokeColor(line)
    for sx in (-1, 1):
        c.ellipse(x + sx * s * 0.38 - s * 0.14, y + s * 0.2, x + sx * s * 0.38 + s * 0.14,
                  y + s * 0.55, stroke=1 if line else 0, fill=1)
    c.ellipse(x - s * 0.16, y - s * 0.35, x + s * 0.16, y + s * 0.02, stroke=1 if line else 0, fill=1)
    if not line:
        c.setFillColor(HexColor("#FFB4C8"))
        for sx in (-1, 1):
            c.circle(x + sx * s * 0.66, y + s * 0.02, s * 0.1, stroke=0, fill=1)
    c.restoreState()


def bat(c, x, y, s, color=NIGHT, line=None, lw=2.2):
    """Bat with spread wings, (x, y) = body centre, s = half wingspan."""
    c.saveState()
    p = c.beginPath()
    p.moveTo(x, y + s * 0.18)
    p.curveTo(x + s * 0.25, y + s * 0.35, x + s * 0.6, y + s * 0.45, x + s, y + s * 0.3)
    p.curveTo(x + s * 0.85, y + s * 0.1, x + s * 0.85, y - s * 0.05, x + s * 0.8, y - s * 0.15)
    p.curveTo(x + s * 0.7, y - s * 0.05, x + s * 0.6, y - s * 0.08, x + s * 0.55, y - s * 0.2)
    p.curveTo(x + s * 0.45, y - s * 0.1, x + s * 0.35, y - s * 0.12, x + s * 0.3, y - s * 0.25)
    p.curveTo(x + s * 0.2, y - s * 0.12, x + s * 0.1, y - s * 0.15, x, y - s * 0.28)
    p.curveTo(x - s * 0.1, y - s * 0.15, x - s * 0.2, y - s * 0.12, x - s * 0.3, y - s * 0.25)
    p.curveTo(x - s * 0.35, y - s * 0.12, x - s * 0.45, y - s * 0.1, x - s * 0.55, y - s * 0.2)
    p.curveTo(x - s * 0.6, y - s * 0.08, x - s * 0.7, y - s * 0.05, x - s * 0.8, y - s * 0.15)
    p.curveTo(x - s * 0.85, y - s * 0.05, x - s * 0.85, y + s * 0.1, x - s, y + s * 0.3)
    p.curveTo(x - s * 0.6, y + s * 0.45, x - s * 0.25, y + s * 0.35, x, y + s * 0.18)
    p.close()
    if line:
        c.setStrokeColor(line); c.setLineWidth(lw); c.setFillColor(WHITE)
        c.drawPath(p, stroke=1, fill=1)
    else:
        c.setFillColor(color); c.drawPath(p, stroke=0, fill=1)
    # head + ears
    c.setFillColor(color if not line else WHITE)
    if line:
        c.setStrokeColor(line)
    q = c.beginPath()
    q.moveTo(x - s * 0.14, y + s * 0.12); q.lineTo(x - s * 0.16, y + s * 0.42)
    q.lineTo(x - s * 0.05, y + s * 0.3); q.lineTo(x + s * 0.05, y + s * 0.3)
    q.lineTo(x + s * 0.16, y + s * 0.42); q.lineTo(x + s * 0.14, y + s * 0.12); q.close()
    c.drawPath(q, stroke=1 if line else 0, fill=1)
    c.circle(x, y + s * 0.08, s * 0.17, stroke=1 if line else 0, fill=1)
    c.setFillColor(YELLOW if not line else (line or NIGHT))
    for sx in (-1, 1):
        c.circle(x + sx * s * 0.065, y + s * 0.12, s * 0.035, stroke=0, fill=1)
    c.restoreState()


def spider(c, x, y, s, color=NIGHT, thread=True):
    c.saveState()
    if thread:
        c.setStrokeColor(color); c.setLineWidth(max(0.8, s * 0.06))
        c.line(x, y + s * 0.5, x, y + s * 3)
    c.setStrokeColor(color); c.setLineWidth(max(1, s * 0.1))
    for side in (-1, 1):
        for i, a in enumerate((25, 5, -15, -35)):
            ang = math.radians(a)
            kx = x + side * s * 0.6 * math.cos(ang)
            ky = y + s * 0.6 * math.sin(ang) + s * 0.25
            ex = x + side * s * 1.05 * math.cos(ang)
            ey = y + s * 0.2 * math.sin(ang) - s * 0.35
            p = c.beginPath(); p.moveTo(x, y); p.lineTo(kx, ky); p.lineTo(ex, ey)
            c.drawPath(p, stroke=1, fill=0)
    c.setFillColor(color)
    c.circle(x, y, s * 0.45, stroke=0, fill=1)
    c.setFillColor(WHITE)
    for sx in (-1, 1):
        c.circle(x + sx * s * 0.17, y + s * 0.08, s * 0.13, stroke=0, fill=1)
    c.setFillColor(NIGHT)
    for sx in (-1, 1):
        c.circle(x + sx * s * 0.15, y + s * 0.06, s * 0.06, stroke=0, fill=1)
    c.restoreState()


def cauldron(c, x, y, s):
    c.saveState()
    c.setFillColor(HexColor("#7CE35A"))
    for dx, dy, r in ((-0.3, 0.55, 0.22), (0.05, 0.7, 0.18), (0.35, 0.58, 0.15), (0.2, 0.95, 0.1)):
        c.circle(x + dx * s, y + dy * s, r * s, stroke=0, fill=1)
    c.setFillColor(NIGHT)
    c.ellipse(x - s, y - s * 0.7, x + s, y + s * 0.5, stroke=0, fill=1)
    c.roundRect(x - s * 1.1, y + s * 0.32, s * 2.2, s * 0.26, s * 0.13, stroke=0, fill=1)
    c.setFillColor(HexColor("#4ADE80"))
    c.ellipse(x - s * 0.9, y + s * 0.4, x + s * 0.9, y + s * 0.58, stroke=0, fill=1)
    c.setFillColor(NIGHT)
    for sx in (-1, 1):
        c.rect(x + sx * s * 0.55 - s * 0.1, y - s * 0.9, s * 0.2, s * 0.3, stroke=0, fill=1)
    c.restoreState()


def witch_hat(c, x, y, s):
    c.saveState()
    c.setFillColor(NIGHT)
    c.ellipse(x - s * 1.1, y - s * 0.22, x + s * 1.1, y + s * 0.22, stroke=0, fill=1)
    p = c.beginPath()
    p.moveTo(x - s * 0.6, y); p.curveTo(x - s * 0.3, y + s * 0.8, x - s * 0.1, y + s * 1.2, x + s * 0.45, y + s * 1.55)
    p.curveTo(x + s * 0.2, y + s * 1.1, x + s * 0.4, y + s * 0.6, x + s * 0.6, y); p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(PURPLE)
    c.rect(x - s * 0.58, y + s * 0.04, s * 1.16, s * 0.24, stroke=0, fill=1)
    c.setFillColor(YELLOW)
    c.rect(x - s * 0.12, y + s * 0.04, s * 0.24, s * 0.24, stroke=0, fill=1)
    c.setFillColor(PURPLE)
    c.rect(x - s * 0.06, y + s * 0.09, s * 0.12, s * 0.14, stroke=0, fill=1)
    c.restoreState()


def moon(c, x, y, r, color=YELLOW, bg=NIGHT):
    c.setFillColor(color)
    c.circle(x, y, r, stroke=0, fill=1)
    c.setFillColor(bg)
    c.circle(x + r * 0.45, y + r * 0.3, r * 0.85, stroke=0, fill=1)


def full_moon(c, x, y, r):
    c.setFillColor(HexColor("#FDBA74"))
    c.circle(x, y, r * 1.12, stroke=0, fill=1)
    c.setFillColor(HexColor("#FB923C"))
    c.circle(x, y, r, stroke=0, fill=1)
    c.setFillColor(HexColor("#F97316"))
    for dx, dy, rr in ((-0.35, 0.2, 0.14), (0.3, -0.25, 0.1), (0.1, 0.4, 0.07)):
        c.circle(x + dx * r, y + dy * r, rr * r, stroke=0, fill=1)


def castle(c, x, y, s, color=NIGHT):
    """Haunted castle silhouette standing on (x, y)."""
    c.saveState()
    c.setFillColor(color)
    c.rect(x - s * 0.8, y, s * 1.6, s * 0.9, stroke=0, fill=1)
    for tx, tw, th in ((-0.9, 0.34, 1.5), (0.56, 0.34, 1.35), (-0.18, 0.36, 1.9)):
        c.rect(x + tx * s, y, tw * s, th * s, stroke=0, fill=1)
        p = c.beginPath()
        p.moveTo(x + tx * s - s * 0.05, y + th * s)
        p.lineTo(x + (tx + tw / 2) * s, y + (th + 0.5) * s)
        p.lineTo(x + (tx + tw) * s + s * 0.05, y + th * s); p.close()
        c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(YELLOW)
    for wx, wy in ((-0.78, 1.05), (0.68, 0.95), (-0.05, 1.4), (-0.05, 0.9), (-0.45, 0.45), (0.3, 0.45)):
        c.roundRect(x + wx * s, y + wy * s, s * 0.1, s * 0.16, s * 0.05, stroke=0, fill=1)
    c.restoreState()


def chest(c, x, y, s):
    """Treasure chest centred on (x, y)."""
    c.saveState()
    brown, dark = HexColor("#9A5B2C"), HexColor("#6B3A17")
    c.setFillColor(YELLOW)
    for dx, dy in ((-0.45, 0.55), (0.1, 0.7), (0.5, 0.5)):
        c.circle(x + dx * s, y + dy * s, s * 0.2, stroke=0, fill=1)
    c.setFillColor(brown); c.roundRect(x - s, y - s * 0.75, s * 2, s * 1.05, s * 0.12, stroke=0, fill=1)
    c.setFillColor(dark); c.roundRect(x - s * 1.05, y + s * 0.2, s * 2.1, s * 0.3, s * 0.1, stroke=0, fill=1)
    c.setFillColor(YELLOW)
    for dx in (-0.7, 0.7):
        c.rect(x + dx * s - s * 0.08, y - s * 0.75, s * 0.16, s * 1.25, stroke=0, fill=1)
    c.roundRect(x - s * 0.18, y - s * 0.1, s * 0.36, s * 0.42, s * 0.06, stroke=0, fill=1)
    c.setFillColor(dark); c.circle(x, y + s * 0.1, s * 0.07, stroke=0, fill=1)
    c.restoreState()


def icon(c, name, x, y, s):
    if name == "pumpkin":
        pumpkin(c, x, y - s * 0.1, s)
    elif name == "bat":
        bat(c, x, y, s * 1.2)
    elif name == "ghost":
        ghost(c, x, y, s * 0.8)
    elif name == "spider":
        spider(c, x, y, s * 0.8, thread=False)
    elif name == "cauldron":
        cauldron(c, x, y - s * 0.1, s * 0.8)
    elif name == "hat":
        witch_hat(c, x, y - s * 0.6, s * 0.8)
    elif name == "chest":
        chest(c, x, y - s * 0.05, s * 0.75)


def clock_icon(c, x, y, r, color):
    c.saveState()
    c.setStrokeColor(color); c.setLineWidth(1.6); c.setFillColor(WHITE)
    c.circle(x, y, r, stroke=1, fill=1)
    c.line(x, y, x, y + r * 0.6); c.line(x, y, x + r * 0.45, y)
    c.restoreState()


def people_icon(c, x, y, r, color):
    c.saveState()
    c.setFillColor(color)
    for dx, sc in ((-0.45, 0.8), (0.45, 0.8), (0, 1.0)):
        c.circle(x + dx * r, y + r * 0.35 * sc, r * 0.28 * sc, stroke=0, fill=1)
        c.wedge(x + dx * r - r * 0.5 * sc, y - r * 0.75 * sc, x + dx * r + r * 0.5 * sc,
                y + r * 0.2 * sc, 0, 180, stroke=0, fill=1)
    c.restoreState()


def dashed_rect(c, x, y, w, h, color, r=10, dash=(5, 4), lw=1.5):
    c.saveState()
    c.setStrokeColor(color); c.setLineWidth(lw); c.setDash(*dash)
    c.roundRect(x, y, w, h, r, stroke=1, fill=0)
    c.restoreState()


def scissors(c, x, y, s, color=INK_2):
    c.saveState()
    c.setStrokeColor(color); c.setLineWidth(1.3); c.setFillColor(WHITE)
    c.circle(x - s * 0.6, y + s * 0.3, s * 0.28, stroke=1, fill=1)
    c.circle(x - s * 0.6, y - s * 0.3, s * 0.28, stroke=1, fill=1)
    c.line(x - s * 0.38, y + s * 0.18, x + s * 0.7, y - s * 0.25)
    c.line(x - s * 0.38, y - s * 0.18, x + s * 0.7, y + s * 0.25)
    c.restoreState()
