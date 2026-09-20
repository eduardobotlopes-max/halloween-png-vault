# -*- coding: utf-8 -*-
"""BONUS #1 · Mockup Studio — the guide that ships with the 30 mockup photos."""
import os

from reportlab.pdfgen import canvas

from style import *
from vaultkit import *

OUT = os.path.join(OUT_DIR, "BONUS-1-Mockup-Studio-Guide.pdf")
W = PAGE_W - 2 * M

CONTENTS = [
    ("T-shirts · flat lay", "Black, white, cream, sand, sage and a folded black tee", "01-06"),
    ("T-shirts · worn & hung", "On a woman, on a man, on hangers, held up for the camera", "07-11"),
    ("Sweatshirts & hoodies", "Cream and black crewnecks, sand and black hoodies", "12-15"),
    ("Mugs", "Single, on a rainy window sill, held in both hands, a matching pair", "16-19"),
    ("20oz tumblers", "Single, a row of three, held in one hand", "20-22"),
    ("Bags & home", "Canvas tote flat and held, linen cushion, blank sticker sheets", "23-26"),
    ("Kids", "Baby bodysuit and a children's tee", "27-28"),
    ("Full scenes", "Three products together, and a craft desk at golden hour", "29-30"),
]

CANVA = [
    "Open Canva and start a design at 2000 x 2000 px.",
    "Upload the mockup photo and drag it onto the canvas so it fills the page.",
    "Upload your PNG design, drag it on top and scale it onto the product.",
    "With the design selected, open Edit > Adjust and drop Opacity to about 92%.",
    "Add a Multiply blend if your design sits on a dark garment, so the fabric texture shows through.",
    "Rotate the design a degree or two to match the product, then Share > Download > PNG.",
]

PHOTOPEA = [
    "Open photopea.com (free, works in the browser, no account) and open the mockup photo.",
    "File > Open & Place, and choose your PNG design.",
    "Scale and position it on the product, then press Enter.",
    "Set the design layer's blend mode to Multiply on light garments, or Screen on very dark ones.",
    "Use Edit > Free Transform > Warp to bend the design around a mug or tumbler.",
    "File > Export As > PNG or JPG at 2000 px.",
]

SIZES = [
    ("Adult T-shirt, front", "28 x 35 cm", "A4 or A3 transfer, centred 7-8 cm below the collar"),
    ("Adult T-shirt, pocket", "8 x 8 cm", "Left chest, 18-20 cm from the shoulder seam"),
    ("Kids' T-shirt", "20 x 25 cm", "Scale down with the size: 2-4 years takes 15 x 18 cm"),
    ("Sweatshirt / hoodie", "25 x 30 cm", "Sit it higher than on a tee so the front pocket stays clear"),
    ("11oz mug", "20 x 8 cm", "Wrap, leaving 2 cm clear each side of the handle"),
    ("20oz skinny tumbler", "23.6 x 20.8 cm", "Full seamless wrap, 2-3 mm overlap"),
    ("Canvas tote", "25 x 30 cm", "Centred, 10 cm below the handle stitching"),
    ("Sticker sheet", "A5 or A4", "Leave 5 mm between stickers for the cut line"),
]

RULES = [
    "One mockup style per listing. A gallery that jumps between wood, linen and studio looks chaotic.",
    "Your first photo is the flat lay. It reads best as a thumbnail on a phone.",
    "Never claim a mockup is a photo of the item you posted. Add one real photo as soon as you have made one.",
    "Keep the design inside the printable area shown in the size table, or the press will cut it off.",
    "Export at 2000 x 2000 px. Bigger is wasted; smaller looks soft on a retina screen.",
]


def page_contents(c):
    background(c)
    y = header_band(c, "Bonus #1", "What's in the pack")
    body(c, M, y, "30 blank product photos, ready for your designs. Every product is empty, well lit "
                  "and square to the camera, so a design drops straight on.", W, 11.5)
    y -= 46
    for name, desc, nums in CONTENTS:
        h = 48
        card(c, M, y - h, W, h)
        c.setFont("Display", 14)
        c.setFillColor(INK)
        c.drawString(M + 16, y - 22, name)
        c.setFont("Text", 9.5)
        c.setFillColor(INK_2)
        c.drawString(M + 16, y - 36, desc)
        c.setFont("TextBold", 10)
        c.setFillColor(ORANGE_DARK)
        c.drawRightString(M + W - 16, y - 28, nums)
        y -= h + 8
    y -= 4
    card(c, M, y - 58, W, 58, YELLOW_SOFT, YELLOW)
    text_block(c, M + 16, y - 22, "File names follow the same order: MOCK-01-tee-black-flatlay, "
                                  "MOCK-02-tee-white-flatlay, and so on.",
               "Text", 10, W - 32, INK, 14)
    footer(c, 2)


def page_steps(c, pno, title, kicker, colour, steps, note_title, note_body):
    background(c)
    y = header_band(c, kicker, title, colour)
    y -= 4
    for i, txt in enumerate(steps, 1):
        lines = wrap(txt, "Text", 10.5, W - 90)
        h = 22 + len(lines) * 15
        card(c, M, y - h, W, h)
        c.setFillColor(ORANGE_SOFT)
        c.circle(M + 32, y - h / 2, 16, stroke=0, fill=1)
        c.setFont("Display", 15)
        c.setFillColor(ORANGE_DARK)
        c.drawCentredString(M + 32, y - h / 2 - 5, str(i))
        yy = y - 20
        for ln in lines:
            c.setFont("Text", 10.5)
            c.setFillColor(INK_2)
            c.drawString(M + 60, yy, ln)
            yy -= 15
        y -= h + 8
    y -= 10
    card(c, M, y - 74, W, 74, GREEN_SOFT, GREEN)
    yy = text_block(c, M + 18, y - 24, note_title, "Display", 14, W - 36, INK, 17)
    text_block(c, M + 18, yy - 2, note_body, "Text", 10, W - 36, INK_2, 14)
    footer(c, pno)


def page_sizes(c, pno):
    background(c)
    y = header_band(c, "Placement", "Where the design goes", PURPLE)
    body(c, M, y, "Print sizes that work on UK blanks. Measure once on your own garment before a big run.",
         W, 11)
    y -= 40
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M + 12, y, "PRODUCT")
    c.drawString(M + 190, y, "PRINT SIZE")
    c.drawString(M + 300, y, "PLACEMENT")
    y -= 10
    rule(c, y)
    y -= 6
    for i, (prod, size, place) in enumerate(SIZES):
        h = 42
        if i % 2 == 0:
            c.setFillColor(HexColor("#F3EFE9"))
            c.rect(M, y - h + 4, W, h, stroke=0, fill=1)
        text_block(c, M + 12, y - 8, prod, "TextBold", 10.5, 170, INK, 13)
        c.setFont("TextBold", 10.5)
        c.setFillColor(PURPLE)
        c.drawString(M + 190, y - 8, size)
        text_block(c, M + 300, y - 8, place, "Text", 9.5, W - 312, INK_2, 12)
        y -= h
    y -= 8
    y = section(c, M, y, "Quick sanity check")
    bullets(c, M, y, [
        "Hold an A4 sheet against a T-shirt: that is roughly a 21 x 30 cm print.",
        "If the design touches a seam or the collar, it is too big.",
    ], W, 10.5, dot=PURPLE)
    footer(c, pno)


def page_rules(c, pno):
    background(c)
    y = header_band(c, "Listing photos", "Five rules", ORANGE_DARK)
    y -= 4
    for i, txt in enumerate(RULES, 1):
        lines = wrap(txt, "Text", 10.5, W - 90)
        h = 24 + len(lines) * 15
        card(c, M, y - h, W, h)
        c.setFont("Display", 20)
        c.setFillColor(ORANGE)
        c.drawString(M + 18, y - h / 2 - 7, str(i))
        yy = y - 22
        for ln in lines:
            c.setFont("Text", 10.5)
            c.setFillColor(INK_2)
            c.drawString(M + 50, yy, ln)
            yy -= 15
        y -= h + 9
    y -= 6
    card(c, M, y - 80, W, 80, PURPLE_SOFT, PURPLE)
    yy = text_block(c, M + 18, y - 24, "One honest line for your listing", "Display", 14, W - 36, INK, 17)
    text_block(c, M + 18, yy - 2,
               "\"Product photos are mockups showing the design; every item is printed to order in "
               "the UK.\" It takes ten seconds to add and stops most refund arguments before they start.",
               "Text", 10, W - 36, INK_2, 14)
    footer(c, pno)


def build():
    register_fonts()
    os.makedirs(OUT_DIR, exist_ok=True)
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle("Mockup Studio · The Halloween PNG Vault")
    c.setAuthor(BRAND)

    cover(c, "30 blank product photos", ["Mockup", "Studio"],
          "Drop any design from the Vault onto a real product photo and you have a listing image in "
          "two minutes. T-shirts, sweatshirts, mugs, tumblers, totes, cushions, kids' wear.", 1)
    c.showPage()
    page_contents(c); c.showPage()
    page_steps(c, 3, "Do it in Canva", "Free, 2 minutes", PURPLE, CANVA,
               "Save it as a template",
               "Once one mockup is set up, duplicate the Canva page and swap only the design. The next "
               "twenty listings take a minute each.")
    c.showPage()
    page_steps(c, 4, "Do it in Photopea", "Free, more control", ORANGE_DARK, PHOTOPEA,
               "Why bother with blend modes",
               "Multiply lets the cotton texture and the folds show through the print. Without it the "
               "design looks like a sticker floating on the photo, and buyers can tell.")
    c.showPage()
    page_sizes(c, 5); c.showPage()
    page_rules(c, 6); c.showPage()

    background(c, NIGHT)
    c.setFont("Display", 30)
    c.setFillColor(WHITE)
    c.drawString(M, PAGE_H - 120, "Go and list one")
    text_block(c, M, PAGE_H - 162,
               "Pick one design, one mockup and one product. A listing that exists beats five that are "
               "still in a folder.",
               "Text", 12, W - 40, Color(0.86, 0.82, 0.94), 18)
    c.setFont("Display", 16)
    c.setFillColor(ORANGE)
    c.drawString(M, PAGE_H - 250, "Your licence, in plain words")
    text_block(c, M, PAGE_H - 278,
               "Use these mockups in your own shop listings, ads and social posts, for as many products "
               "as you like. Don't resell or share the mockup files themselves, and don't sell them as "
               "a mockup pack.",
               "Text", 11.5, W - 40, Color(0.86, 0.82, 0.94), 17)
    pumpkin(c, PAGE_W / 2, 200, 50)
    ghost(c, PAGE_W / 2 - 120, 188, 28)
    bat(c, PAGE_W / 2 + 126, 214, 30, color=Color(1, 1, 1, .8))
    c.setFont("Text", 9.5)
    c.setFillColor(Color(1, 1, 1, .55))
    c.drawCentredString(PAGE_W / 2, 104, BRAND)
    c.save()
    print("built:", OUT)


if __name__ == "__main__":
    build()
