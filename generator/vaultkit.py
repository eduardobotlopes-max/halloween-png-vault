# -*- coding: utf-8 -*-
"""Page furniture shared by the Halloween PNG Vault bonus PDFs."""
import os

from style import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(HERE, "..", "ENTREGAVEIS"))
BRAND = "The Halloween PNG Vault"


def background(c, colour=CREAM):
    c.setFillColor(colour)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)


def footer(c, page_no, label=BRAND):
    c.setFont("Text", 8.5)
    c.setFillColor(INK_2)
    c.drawString(M, 24, label)
    c.drawRightString(PAGE_W - M, 24, str(page_no))


def rule(c, y, x0=M, x1=PAGE_W - M, colour=LINE, lw=1):
    c.setStrokeColor(colour)
    c.setLineWidth(lw)
    c.line(x0, y, x1, y)


def header_band(c, kicker, title, colour=PURPLE, height=132):
    """Dark banner at the top of a chapter page."""
    y0 = PAGE_H - height
    c.setFillColor(colour)
    c.rect(0, y0, PAGE_W, height, stroke=0, fill=1)
    bat(c, PAGE_W - 70, PAGE_H - 44, 16, color=Color(1, 1, 1, 0.35))
    bat(c, PAGE_W - 116, PAGE_H - 70, 11, color=Color(1, 1, 1, 0.22))
    c.setFont("TextBold", 10.5)
    c.setFillColor(YELLOW)
    c.drawString(M, PAGE_H - 46, kicker.upper())
    size = fit(title, "Display", 33, PAGE_W - 2 * M - 70, 20)
    c.setFont("Display", size)
    c.setFillColor(WHITE)
    c.drawString(M, y0 + 38, title)
    return y0 - 34


def section(c, x, y, title, colour=ORANGE_DARK, size=16):
    """Small section heading with a coloured bar. Returns the next baseline."""
    c.setFillColor(colour)
    c.rect(x, y - 3, 4, size + 2, stroke=0, fill=1)
    c.setFont("Display", size)
    c.setFillColor(INK)
    c.drawString(x + 12, y, title)
    return y - size - 12


def body(c, x, y, txt, max_w, size=11, colour=INK_2, leading=None):
    return text_block(c, x, y, txt, "Text", size, max_w, colour, leading or size * 1.5)


def bullets(c, x, y, items, max_w, size=11, colour=INK_2, dot=ORANGE, gap=7):
    for it in items:
        c.setFillColor(dot)
        c.circle(x + 3.2, y + 3.4, 3.2, stroke=0, fill=1)
        yy = text_block(c, x + 14, y, it, "Text", size, max_w - 14, colour, size * 1.45)
        y = yy - gap
    return y


def card(c, x, y, w, h, fill=WHITE, border=LINE, radius=12, lw=1):
    c.setFillColor(fill)
    c.setStrokeColor(border)
    c.setLineWidth(lw)
    c.roundRect(x, y, w, h, radius, stroke=1, fill=1)


def tag(c, x, y, txt, colour=ORANGE, soft=ORANGE_SOFT, size=9):
    w = width(txt, "TextBold", size) + 16
    c.setFillColor(soft)
    c.roundRect(x, y - 4, w, size + 9, (size + 9) / 2, stroke=0, fill=1)
    c.setFont("TextBold", size)
    c.setFillColor(colour)
    c.drawString(x + 8, y + 1.5, txt)
    return x + w + 6


def cut_line(c, y, label="cut here"):
    c.saveState()
    c.setStrokeColor(INK_2)
    c.setLineWidth(0.8)
    c.setDash(5, 4)
    c.line(M * 0.6, y, PAGE_W - M * 0.6, y)
    c.restoreState()
    scissors(c, M * 0.6 + 14, y, 9)
    c.setFont("Text", 7.5)
    c.setFillColor(INK_2)
    c.drawString(M * 0.6 + 30, y - 2.5, label)


def cut_box(c, x, y, w, h, radius=0):
    c.saveState()
    c.setStrokeColor(INK_2)
    c.setLineWidth(0.8)
    c.setDash(4, 3)
    if radius:
        c.roundRect(x, y, w, h, radius, stroke=1, fill=0)
    else:
        c.rect(x, y, w, h, stroke=1, fill=0)
    c.restoreState()


def cut_circle(c, x, y, r):
    c.saveState()
    c.setStrokeColor(INK_2)
    c.setLineWidth(0.8)
    c.setDash(4, 3)
    c.circle(x, y, r, stroke=1, fill=0)
    c.restoreState()


def cover(c, kicker, title_lines, subtitle, bonus_no, accent=ORANGE):
    """Dark cover page shared by both bonus PDFs."""
    background(c, NIGHT)
    # glow
    for i, rr in enumerate((240, 190, 140, 95)):
        c.setFillColor(Color(0.42, 0.24, 0.85, 0.10 + i * 0.03))
        c.circle(PAGE_W * 0.78, PAGE_H * 0.78, rr, stroke=0, fill=1)
    for i, rr in enumerate((210, 160, 110)):
        c.setFillColor(Color(0.98, 0.45, 0.09, 0.07 + i * 0.03))
        c.circle(PAGE_W * 0.16, PAGE_H * 0.2, rr, stroke=0, fill=1)

    full_moon(c, PAGE_W - 92, PAGE_H - 96, 34)
    bat(c, 92, PAGE_H - 120, 20, color=Color(1, 1, 1, 0.5))
    bat(c, 140, PAGE_H - 158, 13, color=Color(1, 1, 1, 0.3))

    y = PAGE_H - 250
    c.setFillColor(accent)
    c.roundRect(M, y + 96, 132, 30, 15, stroke=0, fill=1)
    c.setFont("TextBold", 11)
    c.setFillColor(NIGHT)
    c.drawCentredString(M + 66, y + 105, f"BONUS #{bonus_no}")

    c.setFont("TextBold", 11)
    c.setFillColor(YELLOW)
    c.drawString(M, y + 66, kicker.upper())

    for ln in title_lines:
        size = fit(ln, "Display", 46, PAGE_W - 2 * M, 24)
        c.setFont("Display", size)
        c.setFillColor(WHITE)
        c.drawString(M, y, ln)
        y -= size + 6

    y -= 14
    text_block(c, M, y, subtitle, "Text", 13, PAGE_W - 2 * M - 60, Color(0.86, 0.82, 0.94), 20)

    pumpkin(c, PAGE_W * 0.5, 150, 54)
    ghost(c, PAGE_W * 0.5 - 132, 138, 34)
    witch_hat(c, PAGE_W * 0.5 + 138, 132, 40)

    c.setFont("Text", 9.5)
    c.setFillColor(Color(1, 1, 1, 0.55))
    c.drawCentredString(PAGE_W / 2, 52, f"{BRAND} · for personal and commercial use by the buyer")


def contents_page(c, title, rows, note=None):
    background(c)
    y = header_band(c, "What's inside", title)
    x = M
    maxw = PAGE_W - 2 * M
    for i, (name, desc, pages) in enumerate(rows, 1):
        h = 52
        card(c, x, y - h, maxw, h, WHITE, LINE)
        c.setFillColor(ORANGE_SOFT)
        c.roundRect(x + 10, y - h + 11, 30, 30, 10, stroke=0, fill=1)
        c.setFont("Display", 15)
        c.setFillColor(ORANGE_DARK)
        c.drawCentredString(x + 25, y - h + 20, str(i))
        c.setFont("Display", 13.5)
        c.setFillColor(INK)
        c.drawString(x + 52, y - 22, name)
        c.setFont("Text", 9.5)
        c.setFillColor(INK_2)
        c.drawString(x + 52, y - 36, desc)
        c.setFont("TextBold", 9.5)
        c.setFillColor(PURPLE)
        c.drawRightString(x + maxw - 14, y - 30, pages)
        y -= h + 9
    if note:
        y -= 6
        card(c, M, y - 62, maxw, 62, YELLOW_SOFT, YELLOW)
        text_block(c, M + 16, y - 20, note, "Text", 10, maxw - 32, INK, 14)
