# -*- coding: utf-8 -*-
"""BONUS #5 · Halloween Seller Kit (guide + 100 listing titles and tag packs)."""
import os

from reportlab.pdfgen import canvas

from content_seller import *
from style import *
from vaultkit import *

OUT = os.path.join(OUT_DIR, "BONUS-5-Halloween-Seller-Kit.pdf")
W = PAGE_W - 2 * M


def page_plan(c, pno):
    background(c)
    y = header_band(c, "Start here", "Your first sale in 7 days")
    body(c, M, y, "You do not need a shop full of products. You need one product, photographed well, "
                  "listed properly. This is the fastest honest route from files to money.", W, 11.5)
    y -= 48
    for day, title, txt in PLAN:
        h = 62
        card(c, M, y - h, W, h)
        c.setFillColor(PURPLE_SOFT)
        c.roundRect(M + 12, y - h + 14, 58, 34, 10, stroke=0, fill=1)
        c.setFont("Display", 15)
        c.setFillColor(PURPLE)
        c.drawCentredString(M + 41, y - h + 24, day)
        c.setFont("Display", 14)
        c.setFillColor(INK)
        c.drawString(M + 84, y - 22, title)
        text_block(c, M + 84, y - 37, txt, "Text", 9.5, W - 100, INK_2, 13)
        y -= h + 8
    footer(c, pno)


def page_sells(c, pno):
    background(c)
    y = header_band(c, "Demand", "What actually sells", ORANGE_DARK)
    body(c, M, y, "Eight categories that move every October in the UK. Pick the one closest to people "
                  "you already know: your first ten sales usually come from your own circle.", W, 11.5)
    y -= 46
    # table head
    c.setFont("TextBold", 9)
    c.setFillColor(INK_2)
    c.drawString(M + 12, y, "CATEGORY")
    c.drawString(M + 176, y, "WHO BUYS")
    c.drawString(M + 290, y, "WHY IT WORKS")
    y -= 10
    rule(c, y)
    y -= 6
    for i, (cat, who, why) in enumerate(SELLS):
        h = 46
        if i % 2 == 0:
            c.setFillColor(HexColor("#F3EFE9"))
            c.rect(M, y - h + 4, W, h, stroke=0, fill=1)
        c.setFont("TextBold", 10.5)
        c.setFillColor(INK)
        text_block(c, M + 12, y - 8, cat, "TextBold", 10.5, 156, INK, 13)
        c.setFont("Text", 9.5)
        c.setFillColor(INK_2)
        text_block(c, M + 176, y - 8, who, "Text", 9.5, 108, INK_2, 12)
        text_block(c, M + 290, y - 8, why, "Text", 9.5, W - 302, INK_2, 12)
        y -= h
    footer(c, pno)


def page_methods(c, pno):
    background(c)
    y = header_band(c, "Production", "Pick how you print")
    body(c, M, y, "Four ways to turn a PNG into something you can post. Start with the cheapest that "
                  "matches the product you chose.", W, 11.5)
    y -= 44
    for name, kit, per, best, note in METHODS:
        h = 92
        card(c, M, y - h, W, h)
        c.setFillColor(ORANGE)
        c.roundRect(M, y - h, 5, h, 2.5, stroke=0, fill=1)
        c.setFont("Display", 16)
        c.setFillColor(INK)
        c.drawString(M + 18, y - 26, name)
        xx = M + 18
        for label, val in (("Kit cost", kit), ("Per item", per), ("Best for", best)):
            c.setFont("Text", 8)
            c.setFillColor(INK_2)
            c.drawString(xx, y - 44, label.upper())
            c.setFont("TextBold", 10)
            c.setFillColor(PURPLE)
            c.drawString(xx, y - 58, val)
            xx += max(width(val, "TextBold", 10), width(label, "Text", 8)) + 26
        text_block(c, M + 18, y - 74, note, "Text", 9.5, W - 36, INK_2, 12.5)
        y -= h + 10
    card(c, M, y - 58, W, 58, YELLOW_SOFT, YELLOW)
    text_block(c, M + 16, y - 22, "Costs are UK averages for autumn 2026 and change with supplier and "
                                  "quantity. Always price with your own numbers, not these.",
               "Text", 10, W - 32, INK, 14)
    footer(c, pno)


def page_pricing(c, pno):
    background(c)
    y = header_band(c, "Money", "Price it so it's worth it", GREEN)
    body(c, M, y, "The mistake that kills small shops is pricing against the cheapest listing on the page. "
                  "Work from your costs instead. Here is a real example for a printed T-shirt.", W, 11.5)
    y -= 46
    card(c, M, y - 232, W, 232)
    yy = y - 30
    for label, val in PRICING_ROWS:
        last = label == "Your profit"
        c.setFont("Display" if last else "Text", 14 if last else 11)
        c.setFillColor(INK if last else INK_2)
        c.drawString(M + 22, yy, label)
        c.setFont("Display" if last else "TextBold", 14 if last else 11)
        c.setFillColor(GREEN if last else (INK if val.startswith("£1") else INK_2))
        c.drawRightString(M + W - 22, yy, val)
        if last:
            rule(c, yy + 18, M + 22, M + W - 22, LINE)
        yy -= 28
    y -= 252
    y = section(c, M, y, "Three rules")
    y = bullets(c, M, y, [
        "Aim for at least £6-8 profit on a T-shirt. Below that, one refund wipes out three sales.",
        "Price postage into the item and offer \"free postage\". Buyers compare the total, not the parts.",
        "Check three similar UK listings before you publish. If you are the cheapest, you priced wrong.",
    ], W, dot=GREEN)
    footer(c, pno)


def page_places(c, pno):
    background(c)
    y = header_band(c, "Channels", "Where to sell it", PURPLE)
    body(c, M, y, "You do not need all of these. Pick one that already has buyers and one that is free.", W, 11.5)
    y -= 44
    for name, txt in PLACES:
        h = 66
        card(c, M, y - h, W, h)
        c.setFont("Display", 15)
        c.setFillColor(PURPLE)
        c.drawString(M + 18, y - 24, name)
        text_block(c, M + 18, y - 40, txt, "Text", 9.5, W - 36, INK_2, 13)
        y -= h + 9
    y -= 4
    card(c, M, y - 74, W, 74, PURPLE_SOFT, PURPLE)
    yy = text_block(c, M + 18, y - 24, "The rule that keeps your shop open", "Display", 14, W - 36, INK, 17)
    text_block(c, M + 18, yy - 2,
               "Never list designs with film, TV, game or brand characters, and never write \"Disney "
               "style\" or a brand name in a title or tag. Those listings get removed and repeat "
               "offences close shops. Original artwork only.",
               "Text", 10, W - 36, INK_2, 14)
    footer(c, pno)


def page_photos(c, pno):
    background(c)
    y = header_band(c, "Photos", "Five photos that sell", ORANGE_DARK)
    body(c, M, y, "Photos decide the sale before anyone reads your description. Take these five, in "
                  "daylight, near a window, with no flash.", W, 11.5)
    y -= 44
    for i, txt in enumerate(PHOTOS, 1):
        h = 56
        card(c, M, y - h, W, h)
        c.setFillColor(ORANGE_SOFT)
        c.circle(M + 34, y - 28, 17, stroke=0, fill=1)
        c.setFont("Display", 16)
        c.setFillColor(ORANGE_DARK)
        c.drawCentredString(M + 34, y - 33, str(i))
        text_block(c, M + 62, y - 24, txt, "Text", 10.5, W - 80, INK_2, 14)
        y -= h + 9
    y -= 6
    y = section(c, M, y, "No sample yet?")
    body(c, M, y, "Use the mockups from Bonus #1: drop your design into one and you have a listing photo "
                  "in two minutes. Take real photos as soon as your first item is made - real beats "
                  "mockup every time.", W, 10.5)
    footer(c, pno)


def page_listing(c, pno):
    background(c)
    y = header_band(c, "Listings", "Title, tags, description")
    y = section(c, M, y, "The four-part title")
    for n, part, example in TITLE_FORMULA:
        h = 42
        card(c, M, y - h, W, h)
        c.setFont("Display", 14)
        c.setFillColor(ORANGE)
        c.drawString(M + 16, y - 26, n)
        c.setFont("TextBold", 10.5)
        c.setFillColor(INK)
        c.drawString(M + 38, y - 26, part)
        c.setFont("Text", 10)
        c.setFillColor(PURPLE)
        c.drawRightString(M + W - 16, y - 26, example)
        y -= h + 7
    y -= 4
    card(c, M, y - 46, W, 46, ORANGE_SOFT, ORANGE)
    text_block(c, M + 16, y - 20,
               "Cute Ghost Halloween T-Shirt, Spooky Season Tee, Halloween Gift for Her, UK Seller",
               "TextBold", 10.5, W - 32, ORANGE_DARK, 14)
    y -= 66
    y = section(c, M, y, "Tag rules")
    y = bullets(c, M, y, TAG_RULES, W, 10.5, dot=PURPLE)
    footer(c, pno)


def page_description(c, pno):
    background(c)
    y = header_band(c, "Listings", "Description template", GREEN)
    body(c, M, y, "Copy this, replace everything in brackets. Buyers scan: short blocks, capital "
                  "headings, no wall of text.", W, 11)
    y -= 40
    lines = DESCRIPTION_TEMPLATE.split("\n")
    h = len(lines) * 14 + 32
    card(c, M, y - h, W, h, WHITE, LINE)
    yy = y - 26
    for ln in lines:
        if ln.isupper() and ln.strip():
            c.setFont("TextBold", 10)
            c.setFillColor(ORANGE_DARK)
        elif ln.startswith("["):
            c.setFont("Text", 9.5)
            c.setFillColor(PURPLE)
        else:
            c.setFont("Text", 10)
            c.setFillColor(INK_2)
        c.drawString(M + 18, yy, ln)
        yy -= 14
    y -= h + 22
    y = section(c, M, y, "One line that prevents most messages")
    body(c, M, y, "\"Order by 26 October for delivery before Halloween.\" Put it in every listing from "
                  "1 October and update it as the date gets closer.", W, 10.5)
    footer(c, pno)


def page_titles(c, pno, heading, items, start_index):
    background(c)
    y = header_band(c, "100 ready-to-paste titles", heading, NIGHT, 110)
    c.setFont("Text", 9.5)
    c.setFillColor(INK_2)
    c.drawString(M, y + 4, "Swap the product, colour or occasion words for your own. Keep titles under 140 characters.")
    y -= 22
    for i, t in enumerate(items, start_index):
        lines = wrap(t, "Text", 10, W - 46)
        h = 14 * len(lines) + 16
        if (i - start_index) % 2 == 0:
            c.setFillColor(HexColor("#F3EFE9"))
            c.rect(M, y - h + 4, W, h, stroke=0, fill=1)
        c.setFont("TextBold", 9.5)
        c.setFillColor(ORANGE_DARK)
        c.drawString(M + 10, y - 9, f"{i:03d}")
        yy = y - 9
        for ln in lines:
            c.setFont("Text", 10)
            c.setFillColor(INK)
            c.drawString(M + 44, yy, ln)
            yy -= 14
        y -= h
    footer(c, pno)


def page_tags(c, pno, packs, first):
    background(c)
    y = header_band(c, "Tag packs", "13 tags, ready to paste", PURPLE, 110)
    if first:
        c.setFont("Text", 9.5)
        c.setFillColor(INK_2)
        c.drawString(M, y + 4, "Each pack is a full set of 13 tags, all within the 20-character limit.")
        y -= 20
    for name, tags in packs:
        rows = []
        cur = []
        cur_w = 0
        for t in tags:
            tw = width(t, "TextBold", 9) + 22
            if cur_w + tw > W - 24 and cur:
                rows.append(cur)
                cur, cur_w = [], 0
            cur.append(t)
            cur_w += tw
        rows.append(cur)
        h = 34 + len(rows) * 22
        card(c, M, y - h, W, h)
        c.setFont("Display", 13)
        c.setFillColor(PURPLE)
        c.drawString(M + 14, y - 22, name)
        yy = y - 42
        for row in rows:
            xx = M + 14
            for t in row:
                xx = tag(c, xx, yy, t, PURPLE, PURPLE_SOFT, 9)
            yy -= 22
        y -= h + 10
    footer(c, pno)


def page_messages(c, pno):
    background(c)
    y = header_band(c, "Customer care", "Messages you can copy", GREEN)
    body(c, M, y, "Four messages cover almost every order. Honest, short, no emojis needed.", W, 11)
    y -= 40
    for when, msg in MESSAGES:
        lines = wrap(msg, "Text", 10, W - 40)
        h = 34 + len(lines) * 14 + 12
        card(c, M, y - h, W, h)
        c.setFont("TextBold", 10)
        c.setFillColor(GREEN)
        c.drawString(M + 18, y - 22, when.upper())
        yy = y - 42
        for ln in lines:
            c.setFont("Text", 10)
            c.setFillColor(INK_2)
            c.drawString(M + 18, yy, ln)
            yy -= 14
        y -= h + 10
    card(c, M, y - 56, W, 56, YELLOW_SOFT, YELLOW)
    text_block(c, M + 16, y - 22,
               "Ask for honest reviews only, and never offer anything in exchange for one. In the UK, "
               "paid or incentivised reviews are illegal.",
               "Text", 10, W - 32, INK, 14)
    footer(c, pno)


def page_checklist(c, pno):
    background(c)
    y = header_band(c, "Before you publish", "Launch checklist", ORANGE_DARK)
    y -= 6
    for item in CHECKLIST:
        c.setStrokeColor(ORANGE)
        c.setLineWidth(1.4)
        c.rect(M + 2, y - 13, 15, 15, stroke=1, fill=0)
        c.setFont("Text", 11)
        c.setFillColor(INK)
        c.drawString(M + 28, y - 10, item)
        y -= 24
    y -= 22
    y = section(c, M, y, "The Halloween calendar")
    for when, what in CALENDAR:
        h = 36
        card(c, M, y - h, W, h)
        c.setFont("TextBold", 10)
        c.setFillColor(PURPLE)
        c.drawString(M + 16, y - 22, when)
        c.setFont("Text", 10)
        c.setFillColor(INK_2)
        c.drawString(M + 132, y - 22, what)
        y -= h + 5
    footer(c, pno)


def page_licence(c, pno):
    background(c, NIGHT)
    c.setFont("Display", 30)
    c.setFillColor(WHITE)
    c.drawString(M, PAGE_H - 120, "Now go and sell one")
    y = text_block(c, M, PAGE_H - 162,
                   "One design, one product, one listing. Do that this week and the rest of the Vault "
                   "stops being a folder of files and starts being a shop.",
                   "Text", 12, W - 40, Color(0.86, 0.82, 0.94), 18)
    y -= 26
    c.setFont("Display", 16)
    c.setFillColor(ORANGE)
    c.drawString(M, y, "Your licence, in plain words")
    y -= 26
    y = text_block(c, M, y,
                   "Sell as many physical products as you like with the designs: shirts, mugs, tumblers, "
                   "stickers, décor, printed party items. No unit limit.",
                   "Text", 11.5, W - 40, Color(0.86, 0.82, 0.94), 17)
    y -= 10
    text_block(c, M, y,
               "Don't resell or share the files themselves, and don't sell them as clipart, digital "
               "downloads or design bundles.",
               "Text", 11.5, W - 40, Color(0.86, 0.82, 0.94), 17)
    pumpkin(c, PAGE_W / 2, 200, 50)
    ghost(c, PAGE_W / 2 - 120, 188, 28)
    bat(c, PAGE_W / 2 + 126, 214, 30, color=Color(1, 1, 1, .8))
    c.setFont("Text", 9.5)
    c.setFillColor(Color(1, 1, 1, .55))
    c.drawCentredString(PAGE_W / 2, 104, BRAND)


def build():
    register_fonts()
    os.makedirs(OUT_DIR, exist_ok=True)
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle("Halloween Seller Kit · The Halloween PNG Vault")
    c.setAuthor(BRAND)

    cover(c, "Turn the Vault into sales", ["Halloween", "Seller Kit"],
          "A 7-day plan, UK pricing, listing formulas, 100 ready-to-paste titles and 12 tag packs. "
          "Written for people selling their first Halloween product.", 5, ORANGE)
    c.showPage()

    contents_page(c, "Inside the kit", [
        ("Your first sale in 7 days", "One task a day, start to published listing", "p. 3"),
        ("What actually sells", "Eight categories that move every October", "p. 4"),
        ("Pick how you print", "DTF, sublimation, vinyl or print on demand", "p. 5"),
        ("Price it so it's worth it", "A worked example with UK costs", "p. 6"),
        ("Where to sell it", "Five channels and who each one suits", "p. 7"),
        ("Five photos that sell", "The shots buyers look for", "p. 8"),
        ("Title, tags, description", "The formula and the template", "p. 9-10"),
        ("100 listing titles", "Ready to paste, by product type", "p. 11-16"),
        ("12 tag packs", "13 tags each, within the character limit", "p. 17-19"),
        ("Messages & checklist", "Customer replies, launch list, calendar", "p. 20-21"),
    ], note="Everything here assumes original artwork. Never list designs based on films, TV shows, "
            "games or brands - that is the fastest way to lose a shop.")
    c.showPage()

    page_plan(c, 3); c.showPage()
    page_sells(c, 4); c.showPage()
    page_methods(c, 5); c.showPage()
    page_pricing(c, 6); c.showPage()
    page_places(c, 7); c.showPage()
    page_photos(c, 8); c.showPage()
    page_listing(c, 9); c.showPage()
    page_description(c, 10); c.showPage()

    pno = 11
    idx = 1
    for heading, items in TITLES.items():
        chunk = 20
        for i in range(0, len(items), chunk):
            page_titles(c, pno, heading, items[i:i + chunk], idx + i)
            c.showPage()
            pno += 1
        idx += len(items)

    for i in range(0, len(TAG_PACKS), 4):
        page_tags(c, pno, TAG_PACKS[i:i + 4], i == 0)
        c.showPage()
        pno += 1
    page_messages(c, pno); c.showPage(); pno += 1
    page_checklist(c, pno); c.showPage(); pno += 1
    page_licence(c, pno)
    c.save()
    print("built:", OUT)


if __name__ == "__main__":
    build()
