# -*- coding: utf-8 -*-
"""BONUS #4 · Spooky Party Printables Pack (A4, print at home)."""
import os
import random

from reportlab.pdfgen import canvas

from style import *
from vaultkit import *

OUT = os.path.join(OUT_DIR, "BONUS-4-Spooky-Party-Printables.pdf")
TITLE = "Spooky Party Printables Pack"

BINGO_WORDS = [
    "Pumpkin", "Ghost", "Black cat", "Witch hat", "Bat", "Spider", "Cobweb", "Skeleton",
    "Candle", "Full moon", "Broomstick", "Cauldron", "Sweets", "Toffee apple", "Owl",
    "Haunted house", "Mummy", "Vampire", "Skull", "Spooky sign", "Fairy lights", "Scarecrow",
    "Face paint", "Costume", "Treat bag", "Jack-o'-lantern", "Green slime", "Werewolf",
    "Cupcake", "Torch",
]

HUNT = [
    "Something orange", "A carved pumpkin", "A cobweb (real or fake)", "Someone in a hat",
    "A black cat (toy counts)", "Something that glows", "A spooky sound", "Three sweets in one bag",
    "A bat shape", "Something sticky", "A friend dressed in white", "A candle or fairy light",
    "Something that makes you jump", "A door with decorations", "Anything purple",
    "A skeleton (any size)",
]

FOOD_LABELS = [
    ("Witches' Brew", "Punch"), ("Monster Munch", "Crisps"), ("Bat Wings", "Chicken"),
    ("Mummy Fingers", "Sausage rolls"), ("Frog Spawn", "Jelly"), ("Graveyard Dust", "Popcorn"),
    ("Spider Eggs", "Grapes"), ("Wizard's Worms", "Sweets"),
]

TAGS = ["Happy Halloween!", "Trick or Treat", "Thanks for coming!", "Boo!"]


# ---------------------------------------------------------------- pages
def page_howto(c):
    background(c)
    y = header_band(c, "Read this first", "How to print")
    x, w = M, PAGE_W - 2 * M
    y = section(c, x, y, "Three rules for a good print")
    y = bullets(c, x, y, [
        "Print at <b>100% / Actual size</b>. Turn OFF \"fit to page\" so the cut lines stay accurate."
        .replace("<b>", "").replace("</b>", ""),
        "A4 paper. For invitations, toppers and tags use 160-250 gsm card. Plain paper is fine for the games.",
        "Colour, best quality. If your ink is low, the pages still read well in greyscale.",
    ], w)
    y -= 6
    y = section(c, x, y, "What you need")
    y = bullets(c, x, y, [
        "Scissors (a craft knife for the middle of the door signs, if you have one).",
        "String or ribbon for the bunting, and a hole punch or the tip of the scissors.",
        "Cocktail sticks for the cupcake toppers, and sticky tape.",
    ], w, dot=PURPLE)
    y -= 6
    card(c, x, y - 92, w, 92, GREEN_SOFT, GREEN)
    yy = text_block(c, x + 18, y - 24, "Short on time?", "Display", 15, w - 36, INK, 18)
    text_block(c, x + 18, yy - 2,
               "Print pages 3, 9 and 13 only. An invitation, a sheet of cupcake toppers and a door sign "
               "already make the party look planned. Everything else is a bonus.",
               "Text", 10.5, w - 36, INK_2, 14.5)
    y -= 112
    y = section(c, x, y, "Cutting the shapes")
    body(c, x, y, "Every piece has a dashed line. Cut just inside it and the line disappears. "
                  "For the circles, cut in one slow turn of the paper rather than moving the scissors.", w)
    footer(c, 2)


def invitation(c, x, y, w, h, style_a=True):
    card(c, x, y, w, h, WHITE, LINE, 14, 1)
    # top band
    c.saveState()
    p = c.beginPath()
    p.roundRect(x, y, w, h, 14)
    c.clipPath(p, stroke=0, fill=0)
    c.setFillColor(NIGHT if style_a else PURPLE)
    c.rect(x, y + h - 112, w, 112, stroke=0, fill=1)
    full_moon(c, x + w - 56, y + h - 52, 22)
    bat(c, x + 52, y + h - 46, 13, color=Color(1, 1, 1, .55))
    bat(c, x + 84, y + h - 70, 9, color=Color(1, 1, 1, .32))
    c.restoreState()

    c.setFont("TextBold", 10)
    c.setFillColor(YELLOW)
    c.drawCentredString(x + w / 2, y + h - 40, "YOU'RE INVITED TO")
    c.setFont("Display", 27)
    c.setFillColor(WHITE)
    c.drawCentredString(x + w / 2, y + h - 74, "A SPOOKY PARTY" if style_a else "A HALLOWEEN PARTY")
    c.setFont("Text", 9.5)
    c.setFillColor(Color(1, 1, 1, .8))
    c.drawCentredString(x + w / 2, y + h - 95, "Costumes encouraged · Sweets guaranteed")

    if style_a:
        pumpkin(c, x + 52, y + 36, 21)
        ghost(c, x + w - 52, y + 38, 17)
    else:
        witch_hat(c, x + 50, y + 28, 21)
        cauldron(c, x + w - 54, y + 28, 20)

    fy = y + h - 146
    for label in ("For", "Date", "Time", "Place", "RSVP"):
        c.setFont("TextBold", 10)
        c.setFillColor(ORANGE_DARK if style_a else PURPLE)
        c.drawString(x + 30, fy, label.upper())
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.line(x + 78, fy - 3, x + w - 30, fy - 3)
        fy -= 27
    star(c, x + w / 2, y + 30, 6)


def page_invitations(c, page_no, style_a=True):
    background(c)
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M, PAGE_H - 34, ("INVITATIONS · DESIGN A" if style_a else "INVITATIONS · DESIGN B") +
                 "  ·  print on 160-250 gsm card")
    w, h = PAGE_W - 2 * M, 330
    invitation(c, M, PAGE_H - 60 - h, w, h, style_a)
    cut_line(c, PAGE_H - 60 - h - 26)
    invitation(c, M, PAGE_H - 60 - h - 52 - h, w, h, style_a)
    footer(c, page_no)


def pennant(c, x, y, w, h, char=None, icon_name=None, colour=ORANGE):
    """Triangular bunting flag with two punch marks."""
    p = c.beginPath()
    p.moveTo(x, y + h)
    p.lineTo(x + w, y + h)
    p.lineTo(x + w / 2, y)
    p.close()
    c.saveState()
    c.setFillColor(colour)
    c.drawPath(p, stroke=0, fill=1)
    c.restoreState()
    # cut outline
    c.saveState()
    c.setStrokeColor(INK_2)
    c.setLineWidth(0.8)
    c.setDash(4, 3)
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()
    # punch holes
    for dx in (w * 0.18, w * 0.82):
        c.setFillColor(CREAM)
        c.setStrokeColor(INK_2)
        c.setLineWidth(0.7)
        c.circle(x + dx, y + h - 18, 6, stroke=1, fill=1)
    if char:
        size = 74 if char != "!" else 78
        c.setFont("Display", size)
        c.setFillColor(WHITE)
        c.drawCentredString(x + w / 2, y + h * 0.42, char)
    elif icon_name == "pumpkin":
        pumpkin(c, x + w / 2, y + h * 0.56, 34)
    elif icon_name == "ghost":
        ghost(c, x + w / 2, y + h * 0.58, 26)
    elif icon_name == "bat":
        bat(c, x + w / 2, y + h * 0.6, 30, color=NIGHT)


def page_bunting(c, page_no, items):
    background(c)
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M, PAGE_H - 34, "BUNTING · cut out, punch the holes, thread string through")
    w, h = 240, 300
    gap_x = (PAGE_W - 2 * M - 2 * w)
    positions = [(M, PAGE_H - 70 - h), (M + w + gap_x, PAGE_H - 70 - h),
                 (M, PAGE_H - 90 - 2 * h), (M + w + gap_x, PAGE_H - 90 - 2 * h)]
    for (px, py), it in zip(positions, items):
        char, icon_name, colour = it
        pennant(c, px, py, w, h, char, icon_name, colour)
    footer(c, page_no)


def page_toppers(c, page_no, seed):
    background(c)
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M, PAGE_H - 34, "CUPCAKE TOPPERS · cut two circles, tape a cocktail stick between them")
    rnd = random.Random(seed)
    r = 68
    cols, rows = 3, 4
    x0 = (PAGE_W - (cols * 2 * r + (cols - 1) * 22)) / 2 + r
    y0 = PAGE_H - 92 - r
    kinds = ["pumpkin", "ghost", "bat", "boo", "witch_hat", "spider",
             "trick", "cauldron", "pumpkin", "ghost", "treat", "bat"]
    rnd.shuffle(kinds)
    palette = [ORANGE, PURPLE, NIGHT, GREEN, ORANGE_DARK, PURPLE]
    for i in range(cols * rows):
        cx = x0 + (i % cols) * (2 * r + 22)
        cy = y0 - (i // cols) * (2 * r + 20)
        col = palette[i % len(palette)]
        c.setFillColor(col)
        c.circle(cx, cy, r - 6, stroke=0, fill=1)
        c.setFillColor(CREAM)
        c.circle(cx, cy, r - 13, stroke=0, fill=1)
        k = kinds[i]
        if k == "pumpkin":
            pumpkin(c, cx, cy, 30)
        elif k == "ghost":
            ghost(c, cx, cy - 2, 24)
        elif k == "bat":
            bat(c, cx, cy, 30, color=NIGHT)
        elif k == "witch_hat":
            witch_hat(c, cx, cy - 6, 32)
        elif k == "spider":
            spider(c, cx, cy, 20, thread=False)
        elif k == "cauldron":
            cauldron(c, cx, cy - 8, 24)
        else:
            label = {"boo": "BOO!", "trick": "TRICK", "treat": "TREAT"}[k]
            size = fit(label, "Display", 30, 2 * (r - 18))
            c.setFont("Display", size)
            c.setFillColor(col)
            c.drawCentredString(cx, cy - size * 0.32, label)
        cut_circle(c, cx, cy, r)
    footer(c, page_no)


def _label_half(c, w, h, name, what, colour):
    """One face of a folded tent card, drawn from (0, 0) to (w, h)."""
    c.setFillColor(colour)
    c.rect(0, 0, w, 5, stroke=0, fill=1)
    size = fit(name, "Display", 28, w - 150)
    c.setFont("Display", size)
    c.setFillColor(INK)
    c.drawCentredString(w / 2, h * 0.5, name)
    c.setFont("Text", 11)
    c.setFillColor(INK_2)
    c.drawCentredString(w / 2, h * 0.28, what)
    if colour == ORANGE:
        pumpkin(c, 54, h * 0.55, 19)
        bat(c, w - 54, h * 0.56, 19, color=NIGHT)
    else:
        ghost(c, 54, h * 0.55, 16)
        witch_hat(c, w - 54, h * 0.48, 20)


def page_food_labels(c, page_no):
    background(c)
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M, PAGE_H - 34, "FOOD LABELS · cut out, fold along the middle so the card stands up")
    w = PAGE_W - 2 * M
    h = 168
    half = h / 2
    y = PAGE_H - 62 - h
    for i, (name, what) in enumerate(FOOD_LABELS[:4]):
        colour = ORANGE if i % 2 == 0 else PURPLE
        cut_box(c, M, y, w, h)
        # bottom face, upright
        c.saveState(); c.translate(M, y); _label_half(c, w, half, name, what, colour); c.restoreState()
        # top face, upside down so it reads once the card is folded
        c.saveState(); c.translate(M + w, y + h); c.rotate(180)
        _label_half(c, w, half, name, what, colour); c.restoreState()
        # fold line
        c.saveState()
        c.setStrokeColor(LINE); c.setLineWidth(0.8); c.setDash(2, 3)
        c.line(M, y + half, M + w, y + half)
        c.restoreState()
        c.setFont("Text", 7)
        c.setFillColor(INK_2)
        c.drawRightString(M - 4, y + half - 2.5, "fold")
        y -= h + 14
    footer(c, page_no)


def page_tags(c, page_no):
    background(c)
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M, PAGE_H - 34, "TREAT BAG TAGS · punch the hole and tie to the bag")
    w, h = (PAGE_W - 2 * M - 20) / 2, 150
    y = PAGE_H - 66 - h
    i = 0
    while y > 80:
        for col in range(2):
            x = M + col * (w + 20)
            txt = TAGS[i % len(TAGS)]
            colour = [ORANGE, PURPLE, NIGHT, GREEN][i % 4]
            cut_box(c, x, y, w, h, radius=12)
            c.setFillColor(colour)
            c.roundRect(x + 6, y + 6, w - 12, h - 12, 9, stroke=0, fill=1)
            c.setFillColor(CREAM)
            c.circle(x + w / 2, y + h - 22, 7, stroke=0, fill=1)
            size = fit(txt, "Display", 24, w - 50)
            c.setFont("Display", size)
            c.setFillColor(WHITE)
            c.drawCentredString(x + w / 2, y + h * 0.42, txt)
            if i % 4 == 0:
                pumpkin(c, x + w / 2, y + 44, 23)
            elif i % 4 == 1:
                ghost(c, x + w / 2, y + 44, 19)
            elif i % 4 == 2:
                ghost(c, x + w / 2, y + 44, 19)
            else:
                bat(c, x + w / 2, y + 46, 26, color=WHITE)
            i += 1
        y -= h + 16
    footer(c, page_no)


def page_door_sign(c, page_no, line1, line2, colour, art):
    background(c, NIGHT if art == "dare" else CREAM)
    w = PAGE_W - 2 * M
    x = M
    if art == "dare":
        for i, rr in enumerate((260, 200, 150)):
            c.setFillColor(Color(0.42, 0.24, 0.85, 0.10 + i * 0.04))
            c.circle(PAGE_W / 2, PAGE_H * 0.62, rr, stroke=0, fill=1)
        castle(c, PAGE_W / 2, 150, 92, color=Color(0, 0, 0, 0.55))
        full_moon(c, PAGE_W / 2 + 130, PAGE_H - 190, 40)
        for bx, by, bs in ((120, PAGE_H - 210, 22), (180, PAGE_H - 260, 15), (PAGE_W - 150, 300, 18)):
            bat(c, bx, by, bs, color=Color(1, 1, 1, .45))
        c.setFont("Display", 64)
        c.setFillColor(ORANGE)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 330, line1)
        c.setFont("Display", 64)
        c.setFillColor(WHITE)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 400, line2)
        c.setFont("TextBold", 13)
        c.setFillColor(YELLOW)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 440, "· NO TURNING BACK ·")
    else:
        c.setFillColor(colour)
        c.roundRect(x, 150, w, PAGE_H - 300, 22, stroke=0, fill=1)
        c.setFillColor(CREAM)
        c.roundRect(x + 14, 164, w - 28, PAGE_H - 328, 16, stroke=0, fill=1)
        pumpkin(c, PAGE_W / 2, PAGE_H - 250, 58)
        c.setFont("Display", 46)
        c.setFillColor(colour)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 360, line1)
        c.setFont("Display", 46)
        c.setFillColor(INK)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 412, line2)
        c.setFont("Text", 13)
        c.setFillColor(INK_2)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 444, "Knock, say the magic words, take one sweet")
        ghost(c, PAGE_W / 2 - 110, 250, 30)
        witch_hat(c, PAGE_W / 2 + 110, 244, 38)
        star(c, PAGE_W / 2, 220, 9)
    c.setFillColor(Color(1, 1, 1, .5) if art == "dare" else INK_2)
    c.setFont("Text", 8.5)
    c.drawCentredString(PAGE_W / 2, 96, "Trim the border and tape to the door · The Halloween PNG Vault")
    footer(c, page_no) if art != "dare" else None


def bingo_card(c, x, y, w, h, words, title):
    card(c, x, y, w, h, WHITE, INK_2, 14, 1.2)
    c.setFillColor(PURPLE)
    p = c.beginPath()
    p.roundRect(x, y + h - 62, w, 62, 14)
    c.saveState()
    c.clipPath(p, stroke=0, fill=0)
    c.setFillColor(PURPLE)
    c.rect(x, y + h - 62, w, 62, stroke=0, fill=1)
    c.restoreState()
    c.setFont("Display", 26)
    c.setFillColor(WHITE)
    c.drawCentredString(x + w / 2, y + h - 44, "HALLOWEEN BINGO")
    c.setFont("Text", 9)
    c.setFillColor(YELLOW)
    c.drawCentredString(x + w / 2, y + h - 57, title)

    grid = w - 36
    cell = grid / 5
    gx = x + 18
    gy = y + 30
    for r in range(5):
        for col in range(5):
            cx, cy = gx + col * cell, gy + (4 - r) * cell
            free = (r == 2 and col == 2)
            c.setStrokeColor(LINE)
            c.setLineWidth(1)
            c.setFillColor(ORANGE_SOFT if free else WHITE)
            c.rect(cx, cy, cell, cell, stroke=1, fill=1)
            if free:
                pumpkin(c, cx + cell / 2, cy + cell * 0.58, cell * 0.24)
                c.setFont("TextBold", 7.5)
                c.setFillColor(ORANGE_DARK)
                c.drawCentredString(cx + cell / 2, cy + cell * 0.16, "FREE")
                continue
            word = words[r * 5 + col if not (r > 2 or (r == 2 and col > 2)) else r * 5 + col - 1]
            size = 8
            lines = wrap(word, "Text", size, cell - 8)
            ty = cy + cell / 2 + (len(lines) - 1) * 5
            for ln in lines:
                c.setFont("Text", size)
                c.setFillColor(INK)
                c.drawCentredString(cx + cell / 2, ty, ln)
                ty -= 10
    c.setFont("Text", 8)
    c.setFillColor(INK_2)
    c.drawCentredString(x + w / 2, y + 12, "Cross one off each time you spot it. Five in a row wins.")


def page_bingo(c, page_no, seed):
    background(c)
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M, PAGE_H - 34, "HALLOWEEN BINGO · every card is different · one card per player")
    rnd = random.Random(seed)
    words = rnd.sample(BINGO_WORDS, 24)
    w = PAGE_W - 2 * M
    h = 74 + (w - 36) + 34          # header + square grid + strap line
    bingo_card(c, M, PAGE_H - 64 - h, w, h, words, f"Card {seed}")
    card(c, M, PAGE_H - 64 - h - 86, w, 72, ORANGE_SOFT, ORANGE)
    yy = text_block(c, M + 18, PAGE_H - 64 - h - 30, "How to play", "Display", 14, w - 36, INK, 17)
    text_block(c, M + 18, yy - 2,
               "Give each player a different card. Cross off a square every time you spot that thing "
               "at the party. Five in a row - across, down or diagonally - wins a sweet.",
               "Text", 10, w - 36, INK_2, 14)
    footer(c, page_no)


def page_hunt(c, page_no):
    background(c)
    y = header_band(c, "Game", "Spooky Scavenger Hunt", PURPLE, 118)
    x, w = M, PAGE_W - 2 * M
    body(c, x, y, "Give one sheet per child. Tick a box each time you spot something. "
                  "First to finish a whole column wins a sweet.", w, 11)
    y -= 46
    cols = 2
    cw = (w - 20) / cols
    for i, item in enumerate(HUNT):
        cx = x + (i % cols) * (cw + 20)
        cy = y - (i // cols) * 44
        card(c, cx, cy - 34, cw, 34, WHITE, LINE, 10)
        c.setStrokeColor(ORANGE)
        c.setLineWidth(1.4)
        c.rect(cx + 12, cy - 25, 17, 17, stroke=1, fill=0)
        c.setFont("Text", 10.5)
        c.setFillColor(INK)
        c.drawString(cx + 38, cy - 20, item)
    y -= (len(HUNT) // cols) * 44 + 16
    card(c, x, y - 58, w, 58, PURPLE_SOFT, PURPLE)
    c.setFont("Display", 14)
    c.setFillColor(PURPLE)
    c.drawString(x + 16, y - 26, "Hunter's name:")
    c.setStrokeColor(PURPLE)
    c.line(x + 140, y - 30, x + w - 16, y - 30)
    footer(c, page_no)


def page_sweets(c, page_no):
    background(c)
    y = header_band(c, "Game", "Guess How Many Sweets", ORANGE_DARK, 118)
    x, w = M, PAGE_W - 2 * M
    body(c, x, y, "Fill a jar with sweets and count them (write the number down and hide it). "
                  "Everyone writes a guess. Closest guess wins the jar.", w, 11)
    y -= 56
    card(c, x, y - 120, w, 120, WHITE, LINE)
    cauldron(c, x + 86, y - 74, 44)
    c.setFont("Display", 22)
    c.setFillColor(INK)
    c.drawString(x + 170, y - 44, "Jar filled with:")
    c.setStrokeColor(LINE)
    c.line(x + 170, y - 62, x + w - 30, y - 62)
    c.setFont("Text", 10)
    c.setFillColor(INK_2)
    c.drawString(x + 170, y - 84, "Real number (keep this secret!):")
    c.setStrokeColor(LINE)
    c.line(x + 170, y - 100, x + w - 30, y - 100)
    y -= 146
    c.setFont("TextBold", 10)
    c.setFillColor(INK_2)
    c.drawString(x, y, "ENTRY SLIPS · cut along the dashed lines")
    y -= 14
    sh = 74
    while y - sh > 70:
        cut_box(c, x, y - sh, w, sh)
        c.setFont("Display", 15)
        c.setFillColor(ORANGE_DARK)
        c.drawString(x + 16, y - 28, "My guess:")
        c.setStrokeColor(LINE)
        c.line(x + 110, y - 32, x + 240, y - 32)
        c.setFont("Text", 10.5)
        c.setFillColor(INK_2)
        c.drawString(x + 262, y - 28, "Name:")
        c.setStrokeColor(LINE)
        c.line(x + 306, y - 32, x + w - 16, y - 32)
        pumpkin(c, x + w - 44, y - 56, 13)
        c.setFont("Text", 8.5)
        c.setFillColor(INK_2)
        c.drawString(x + 16, y - 56, "Closest guess without going over wins the jar.")
        y -= sh + 10
    footer(c, page_no)


def page_thanks(c, page_no):
    background(c)
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M, PAGE_H - 34, "THANK YOU TAGS · for party bags on the way out")
    w, h = (PAGE_W - 2 * M - 18) / 2, 128
    y = PAGE_H - 62 - h
    msgs = [("Thanks for", "haunting with us!"), ("You were", "spook-tacular!"),
            ("Thanks for", "coming!"), ("Sweet dreams,", "little monster")]
    i = 0
    while y > 70:
        for col in range(2):
            x = M + col * (w + 18)
            l1, l2 = msgs[i % len(msgs)]
            cut_box(c, x, y, w, h, radius=10)
            c.setStrokeColor(ORANGE if i % 2 == 0 else PURPLE)
            c.setLineWidth(2)
            c.roundRect(x + 8, y + 8, w - 16, h - 16, 8, stroke=1, fill=0)
            c.setFont("Text", 12)
            c.setFillColor(INK_2)
            c.drawCentredString(x + w / 2, y + h - 44, l1)
            size = fit(l2, "Display", 21, w - 44)
            c.setFont("Display", size)
            c.setFillColor(ORANGE_DARK if i % 2 == 0 else PURPLE)
            c.drawCentredString(x + w / 2, y + h - 74, l2)
            ghost(c, x + w / 2, y + 34, 16) if i % 2 == 0 else pumpkin(c, x + w / 2, y + 34, 18)
            i += 1
        y -= h + 14
    footer(c, page_no)


def page_licence(c, page_no):
    background(c, NIGHT)
    c.setFont("Display", 30)
    c.setFillColor(WHITE)
    c.drawString(M, PAGE_H - 120, "Enjoy the party")
    c.setFont("Text", 12)
    y = text_block(c, M, PAGE_H - 160,
                   "Print these pages as many times as you like, for your own family, your class or your "
                   "customers' parties. They are yours to use.",
                   "Text", 12, PAGE_W - 2 * M - 40, Color(0.86, 0.82, 0.94), 18)
    y -= 24
    c.setFont("Display", 16)
    c.setFillColor(ORANGE)
    c.drawString(M, y, "The one rule")
    y -= 24
    text_block(c, M, y,
               "Please don't resell or share the PDF itself, or upload it anywhere. The printed pieces are "
               "yours; the file stays with you.",
               "Text", 11.5, PAGE_W - 2 * M - 40, Color(0.86, 0.82, 0.94), 17)
    pumpkin(c, PAGE_W / 2, 210, 54)
    ghost(c, PAGE_W / 2 - 124, 196, 30)
    bat(c, PAGE_W / 2 + 130, 226, 26, color=Color(1, 1, 1, .6))
    c.setFont("Text", 9.5)
    c.setFillColor(Color(1, 1, 1, .55))
    c.drawCentredString(PAGE_W / 2, 110, BRAND)


# ---------------------------------------------------------------- build
def build():
    register_fonts()
    os.makedirs(OUT_DIR, exist_ok=True)
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle("Spooky Party Printables Pack · The Halloween PNG Vault")
    c.setAuthor(BRAND)

    cover(c, "Print at home · A4", ["Spooky Party", "Printables Pack"],
          "Invitations, bunting, cupcake toppers, food labels, door signs, treat tags and three "
          "games for the kids. Print as many times as you like.", 4)
    c.showPage()

    contents_page(c, "Everything in this pack", [
        ("How to print", "Paper, size and cutting in 30 seconds", "p. 2"),
        ("Invitations", "Two designs, two per page", "p. 3-4"),
        ("Bunting", "HAPPY HALLOWEEN + pumpkin flags", "p. 5-8"),
        ("Cupcake toppers", "24 toppers, two sheets", "p. 9-10"),
        ("Food labels", "Standing tent cards for the table", "p. 11"),
        ("Treat bag tags", "Tie one to every party bag", "p. 12"),
        ("Door signs", "Welcome sign and Enter If You Dare", "p. 13-14"),
        ("Games", "Four bingo cards, scavenger hunt, guess the sweets", "p. 15-20"),
        ("Thank you tags", "For the goodbye bags", "p. 21"),
    ], note="Tip: print only the pages you need. Each section starts on its own page, so nothing "
            "is wasted if you skip the games or the bunting.")
    c.showPage()

    page_howto(c); c.showPage()
    page_invitations(c, 3, True); c.showPage()
    page_invitations(c, 4, False); c.showPage()

    letters = list("HAPPY") + [None] + list("HALLOWEEN") + [None]
    icons = {5: "pumpkin", 15: "ghost"}
    colours = [ORANGE, PURPLE, NIGHT, GREEN, ORANGE_DARK]
    flags = []
    for i, ch in enumerate(letters):
        flags.append((ch, icons.get(i), colours[i % len(colours)]))
    for pg in range(4):
        page_bunting(c, 5 + pg, flags[pg * 4:pg * 4 + 4])
        c.showPage()

    page_toppers(c, 9, 11); c.showPage()
    page_toppers(c, 10, 77); c.showPage()
    page_food_labels(c, 11); c.showPage()
    page_tags(c, 12); c.showPage()
    page_door_sign(c, 13, "TRICK OR", "TREATERS WELCOME", ORANGE, "welcome"); c.showPage()
    page_door_sign(c, 14, "ENTER", "IF YOU DARE", NIGHT, "dare"); c.showPage()
    for i, seed in enumerate((1, 2, 3, 4)):
        page_bingo(c, 15 + i, seed); c.showPage()
    page_hunt(c, 19); c.showPage()
    page_sweets(c, 20); c.showPage()
    page_thanks(c, 21); c.showPage()
    page_licence(c, 22)
    c.save()
    print("built:", OUT)


if __name__ == "__main__":
    build()
