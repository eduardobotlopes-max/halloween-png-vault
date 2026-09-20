# -*- coding: utf-8 -*-
"""BONUS #2 · 500 original SVG cut files for Cricut / Silhouette.

Shapes are built as real polygons, then unioned and subtracted with shapely, so a
pumpkin's face is a genuine hole in the silhouette and the machine cuts it properly.
Everything is generated parametrically: no traced artwork, all original.
"""
import math
import os
import random
import shutil

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from shapely import affinity
from shapely.geometry import MultiPolygon, Polygon
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "ENTREGAVEIS", "BONUS-2-SVG-Cut-Files"))
FONT = os.path.join(HERE, "fonts", "Baloo2-XBold.ttf")


# ---------------------------------------------------------------- geometry helpers
def ell(cx, cy, rx, ry, rot=0.0, n=72):
    pts = [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n))
           for i in range(n)]
    p = Polygon(pts)
    return affinity.rotate(p, math.degrees(rot), origin=(cx, cy)) if rot else p


def pg(points):
    return Polygon(points)


def rrect(x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    pts = []
    for (cx, cy, a0) in ((x + w - r, y + h - r, 0), (x + r, y + h - r, 90),
                         (x + r, y + r, 180), (x + w - r, y + r, 270)):
        for i in range(17):
            a = math.radians(a0 + i * 90 / 16)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return Polygon(pts)


def star_poly(cx, cy, r, points=5, inner=0.45, rot=-math.pi / 2):
    pts = []
    for i in range(points * 2):
        a = rot + i * math.pi / points
        rr = r if i % 2 == 0 else r * inner
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return Polygon(pts)


def bez(p0, p1, p2, p3, n=24):
    out = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        out.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return out


def thick_line(p0, p1, t):
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    ln = math.hypot(dx, dy) or 1
    nx, ny = -dy / ln * t / 2, dx / ln * t / 2
    return pg([(p0[0] + nx, p0[1] + ny), (p1[0] + nx, p1[1] + ny),
               (p1[0] - nx, p1[1] - ny), (p0[0] - nx, p0[1] - ny)])


def thick_path(pts, t):
    return unary_union([thick_line(pts[i], pts[i + 1], t) for i in range(len(pts) - 1)] +
                       [ell(x, y, t / 2, t / 2, n=16) for x, y in pts])


# ---------------------------------------------------------------- svg out
def to_svg(geom, path, title):
    geoms = geom.geoms if isinstance(geom, MultiPolygon) else [geom]
    d = []
    for poly in geoms:
        if poly.is_empty:
            continue
        poly = poly.simplify(0.6, preserve_topology=True)
        for ring in [poly.exterior] + list(poly.interiors):
            coords = list(ring.coords)
            d.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in coords) + "Z")
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" '
           f'height="1000"><title>{title}</title>'
           f'<path fill="#000000" fill-rule="evenodd" d="{"".join(d)}"/></svg>')
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)


def _clean(geoms):
    """buffer(0) fixes the self-intersections that hand-built polygons pick up."""
    out = []
    for g in geoms:
        if g is None or g.is_empty:
            continue
        if not g.is_valid:
            g = g.buffer(0)
        if not g.is_empty:
            out.append(g)
    return out


def compose(solids, holes=()):
    g = unary_union(_clean(solids))
    h = _clean(holes)
    if h:
        g = g.difference(unary_union(h))
    return g


# ---------------------------------------------------------------- shapes
def bat(rnd):
    span = rnd.uniform(390, 460)
    lift = rnd.uniform(0.6, 1.3)
    scallops = rnd.choice((3, 4))
    br = rnd.uniform(56, 76)
    cy = 520
    pts = [(500, cy - br * 0.2)]
    for side in (1, -1):
        seq = []
        seq += bez((500, cy - br * 0.2),
                   (500 + side * span * 0.25, cy - span * 0.22 * lift),
                   (500 + side * span * 0.60, cy - span * 0.32 * lift),
                   (500 + side * span, cy - span * 0.30 * lift))
        seq += bez((500 + side * span, cy - span * 0.30 * lift),
                   (500 + side * span * 0.86, cy + span * 0.02),
                   (500 + side * span * 0.90, cy + span * 0.10),
                   (500 + side * span * 0.80, cy + span * 0.22))
        for i in range(scallops):
            x0 = 500 + side * span * (0.80 - i * (0.80 / scallops))
            x1 = 500 + side * span * (0.80 - (i + 1) * (0.80 / scallops))
            seq += bez((x0, cy + span * 0.20),
                       (x0 - side * span * 0.06, cy + span * 0.36),
                       (x1 + side * span * 0.06, cy + span * 0.36),
                       (x1, cy + span * 0.20))
        if side == 1:
            seq.append((500, cy + span * 0.30))
            pts += seq
        else:
            pts += list(reversed(seq))
    wings = pg(pts).buffer(0)
    ears = pg([(500 - br * 0.72, cy - br * 0.4), (500 - br * 0.85, cy - br * 1.75),
               (500 - br * 0.18, cy - br * 1.05), (500 + br * 0.18, cy - br * 1.05),
               (500 + br * 0.85, cy - br * 1.75), (500 + br * 0.72, cy - br * 0.4)])
    head = ell(500, cy - br * 0.5, br * 0.78, br * 0.68)
    eyes = [ell(500 + sx * br * 0.3, cy - br * 0.55, br * 0.13, br * 0.16) for sx in (-1, 1)]
    return compose([wings, ears, head], eyes if rnd.random() < 0.55 else ())


def pumpkin(rnd, face=True):
    r = rnd.uniform(320, 370)
    h = r * rnd.uniform(0.80, 0.94)
    cy = 560
    body = unary_union([ell(500, cy, r * 0.70, h),
                        ell(500 - r * 0.40, cy, r * 0.60, h * 0.93),
                        ell(500 + r * 0.40, cy, r * 0.60, h * 0.93)])
    stem = pg([(500 - r * 0.11, cy - h * 0.88), (500 - r * 0.09, cy - h * 1.28),
               (500 + r * 0.16, cy - h * 1.36), (500 + r * 0.13, cy - h * 0.88)])
    leaf = None
    if rnd.random() < 0.4:
        leaf = ell(500 + r * 0.34, cy - h * 1.06, r * 0.22, r * 0.10, rot=-0.5)
    solids = [body, stem] + ([leaf] if leaf else [])
    if not face:
        return compose(solids)
    style = rnd.choice(("triangle", "round", "square", "cat", "diamond"))
    holes = []
    ey, ex, es = cy - h * 0.20, r * 0.30, r * 0.17
    for sx in (-1, 1):
        cxx = 500 + sx * ex
        if style == "triangle":
            holes.append(pg([(cxx - es, ey - es * 0.25), (cxx + es, ey - es * 0.25), (cxx, ey + es * 1.15)]))
        elif style == "round":
            holes.append(ell(cxx, ey + es * 0.3, es * 0.78, es * 0.78))
        elif style == "square":
            holes.append(rrect(cxx - es * 0.75, ey - es * 0.3, es * 1.5, es * 1.5, es * 0.22))
        elif style == "cat":
            holes.append(pg([(cxx - es, ey + es), (cxx + es, ey + es), (cxx, ey - es * 0.7)]))
        else:
            holes.append(pg([(cxx - es * 0.85, ey + es * 0.4), (cxx, ey - es * 0.85),
                             (cxx + es * 0.85, ey + es * 0.4), (cxx, ey + es * 1.35)]))
    holes.append(pg([(500 - r * 0.10, cy + h * 0.12), (500 + r * 0.10, cy + h * 0.12), (500, cy - h * 0.06)]))
    teeth = rnd.choice((2, 3, 4))
    mw, my = r * 0.48, cy + h * 0.30
    step = (2 * mw) / (teeth * 2)
    mouth = [(500 - mw, my)]
    for i in range(teeth * 2):
        x = 500 - mw + step * (i + 1)
        mouth.append((x, my + h * 0.20 if i % 2 == 0 else my))
    mouth += [(500 + mw, my + h * 0.30), (500, my + h * 0.42), (500 - mw, my + h * 0.30)]
    holes.append(pg(mouth))
    return compose(solids, holes)


def ghost(rnd):
    w = rnd.uniform(270, 320)
    top, bottom = 250, rnd.uniform(750, 800)
    waves = rnd.choice((3, 4, 5))
    pts = [(500 - w, bottom), (500 - w, top + w * 0.5)]
    pts += bez((500 - w, top + w * 0.5), (500 - w, top - w * 0.40),
               (500 + w, top - w * 0.40), (500 + w, top + w * 0.5))
    pts.append((500 + w, bottom))
    step = 2 * w / waves
    for i in range(waves):
        x0 = 500 + w - i * step
        x1 = x0 - step
        dip = bottom + (95 if i % 2 == 0 else 72)
        pts += bez((x0, bottom), (x0 - step * 0.18, dip), (x1 + step * 0.18, dip), (x1, bottom))
    body = pg(pts).buffer(0)
    solids = [body]
    if rnd.random() < 0.35:                      # little arms
        for sx in (-1, 1):
            solids.append(ell(500 + sx * w * 1.02, top + w * 1.25, w * 0.22, w * 0.16))
    ey = top + w * 0.78
    er = w * rnd.uniform(0.13, 0.18)
    holes = [ell(500 + sx * w * 0.38, ey, er, er * rnd.uniform(1.0, 1.3)) for sx in (-1, 1)]
    holes.append(ell(500, ey + w * 0.44, w * 0.15, w * 0.21))
    if rnd.random() < 0.4:                       # blush
        holes += [ell(500 + sx * w * 0.66, ey + w * 0.30, w * 0.09, w * 0.06) for sx in (-1, 1)]
    return compose(solids, holes)


def cat(rnd):
    hr = rnd.uniform(185, 225)
    cy = 400
    head = ell(500, cy, hr, hr * 0.94)
    ears = [pg([(500 - hr * 0.95, cy - hr * 0.42), (500 - hr * 0.86, cy - hr * 1.5),
                (500 - hr * 0.08, cy - hr * 0.78)]),
            pg([(500 + hr * 0.95, cy - hr * 0.42), (500 + hr * 0.86, cy - hr * 1.5),
                (500 + hr * 0.08, cy - hr * 0.78)])]
    bh = rnd.uniform(320, 390)
    body = pg([(500 - hr * 0.74, cy + hr * 0.4), (500 + hr * 0.74, cy + hr * 0.4),
               (500 + hr * 1.05, cy + hr * 0.4 + bh), (500 - hr * 1.05, cy + hr * 0.4 + bh)])
    d = rnd.choice((-1, 1))
    bx, by = 500 + d * hr * 1.0, cy + hr * 0.4 + bh
    tail = thick_path(bez((bx, by), (bx + d * 230, by - 40), (bx + d * 250, by - 300),
                          (bx + d * 120, by - 330)), 60)
    holes = []
    if rnd.random() < 0.6:
        holes = [ell(500 + sx * hr * 0.38, cy - hr * 0.08, hr * 0.16, hr * 0.22) for sx in (-1, 1)]
    return compose([head, body, tail] + ears, holes)


def spider(rnd):
    br = rnd.uniform(145, 185)
    cy = 520
    solids = [ell(500, cy + br * 0.35, br, br * 0.85), ell(500, cy - br * 0.78, br * 0.58, br * 0.52)]
    for side in (-1, 1):
        for i, ang in enumerate((30, 10, -10, -30)):
            a = math.radians(ang)
            x0, y0 = 500 + side * br * 0.5, cy + br * 0.05 + i * br * 0.18
            knee = (x0 + side * br * 1.3 * math.cos(a), y0 - br * 1.0 * math.sin(a) - br * 0.15)
            end = (x0 + side * br * 1.95 * math.cos(a), y0 + br * 0.85)
            solids.append(thick_path(bez((x0, y0), knee, knee, end), br * 0.13))
    holes = [ell(500 + sx * br * 0.22, cy - br * 0.82, br * 0.12, br * 0.14) for sx in (-1, 1)]
    return compose(solids, holes)


def web(rnd):
    spokes = rnd.choice((7, 8, 9))
    rings = rnd.choice((3, 4))
    corner = rnd.random() < 0.5
    cx, cy = (40, 40) if corner else (500, 500)
    rmax = 900 if corner else 430
    t = 16
    span = math.pi / 2 if corner else 2 * math.pi
    a0 = 0 if corner else 0
    solids = []
    for i in range(spokes + 1):
        a = a0 + span * i / spokes
        solids.append(thick_line((cx, cy), (cx + rmax * math.cos(a), cy + rmax * math.sin(a)), t))
    for k in range(1, rings + 1):
        rr = rmax * k / (rings + 0.45)
        pts = []
        steps = spokes * 6
        for i in range(steps + 1):
            a = a0 + span * i / steps
            seg = (i / 6) % 1.0
            sag = rr * 0.05 * math.sin(math.pi * seg)
            pts.append((cx + (rr - sag) * math.cos(a), cy + (rr - sag) * math.sin(a)))
        solids.append(thick_path(pts, t))
    return compose(solids)


def witch_hat(rnd):
    w = rnd.uniform(290, 350)
    cy = 640
    lean = rnd.uniform(-0.3, 0.3)
    brim = ell(500, cy, w, w * 0.24)
    tip = (500 + lean * w + w * 0.24, cy - w * 1.5)
    left = bez((500 - w * 0.46, cy), (500 - w * 0.34, cy - w * 0.72), (500 + lean * w - w * 0.14, cy - w * 1.14), tip)
    right = bez(tip, (500 + lean * w * 0.5 + w * 0.10, cy - w * 0.98), (500 + w * 0.28, cy - w * 0.56),
                (500 + w * 0.46, cy))
    cone = pg(left + right)
    band = rrect(500 - w * 0.6, cy - w * 0.34, w * 1.2, w * 0.2, w * 0.04).intersection(cone.buffer(0))
    buckle = rrect(500 - w * 0.09, cy - w * 0.36, w * 0.18, w * 0.24, w * 0.03)
    holes = [band.difference(buckle)] if rnd.random() < 0.6 else ()
    return compose([brim, cone], holes)


def broom(rnd):
    ang = math.radians(rnd.uniform(-30, 30))
    length = rnd.uniform(620, 740)
    dx, dy = math.sin(ang), -math.cos(ang)
    hx, hy = 500 - dx * length * 0.45, 500 - dy * length * 0.45
    tx, ty = 500 + dx * length * 0.5, 500 + dy * length * 0.5
    solids = [thick_line((hx, hy), (tx, ty), 42)]
    bw = rnd.uniform(115, 160)
    n = rnd.choice((5, 6, 7))
    for i in range(n):
        f = (i / (n - 1) - 0.5) * 2
        ex = tx + dx * 190 + f * bw * 1.35
        ey = ty + dy * 190 + abs(f) * 26
        solids.append(pg([(tx - dy * 22 + f * bw * 0.4, ty + dx * 22 + f * 8),
                          (ex - 30, ey), (ex + 30, ey),
                          (tx + dy * 22 + f * bw * 0.4, ty - dx * 22 + f * 8)]))
    solids.append(thick_line((tx - dx * 10, ty - dy * 10), (tx + dx * 62, ty + dy * 62), 96))
    return compose(solids)


def cauldron(rnd):
    r = rnd.uniform(270, 320)
    cy = 560
    solids = [ell(500, cy, r, r * 0.84),
              rrect(500 - r * 1.14, cy - r * 0.88, r * 2.28, r * 0.22, r * 0.11),
              pg([(500 - r * 0.62, cy + r * 0.55), (500 - r * 0.36, cy + r * 0.55),
                  (500 - r * 0.42, cy + r * 1.02), (500 - r * 0.72, cy + r * 1.02)]),
              pg([(500 + r * 0.62, cy + r * 0.55), (500 + r * 0.36, cy + r * 0.55),
                  (500 + r * 0.42, cy + r * 1.02), (500 + r * 0.72, cy + r * 1.02)])]
    for _ in range(rnd.choice((2, 3))):
        solids.append(ell(500 + rnd.uniform(-r * 0.5, r * 0.5), cy - r * 0.95 - rnd.uniform(40, 160),
                          rnd.uniform(24, 46), rnd.uniform(24, 46)))
    return compose(solids)


def potion(rnd):
    w = rnd.uniform(170, 225)
    cy = 600
    shape = rnd.choice(("round", "cone", "square"))
    if shape == "round":
        bottle = ell(500, cy, w, w * 1.05)
    elif shape == "cone":
        bottle = pg([(500 - w * 0.3, cy - w), (500 + w * 0.3, cy - w), (500 + w, cy + w), (500 - w, cy + w)])
    else:
        bottle = rrect(500 - w * 0.8, cy - w, w * 1.6, w * 2, w * 0.2)
    neck = rrect(500 - w * 0.26, cy - w * 1.55, w * 0.52, w * 0.65, w * 0.08)
    cork = rrect(500 - w * 0.35, cy - w * 1.88, w * 0.7, w * 0.4, w * 0.1)
    holes = []
    mark = rnd.choice(("star", "skull", "none", "bolt"))
    if mark == "star":
        holes.append(star_poly(500, cy + w * 0.05, w * 0.45, 5, 0.42))
    elif mark == "skull":
        holes.append(ell(500, cy, w * 0.34, w * 0.38))
    elif mark == "bolt":
        holes.append(pg([(500 - w * 0.12, cy - w * 0.45), (500 + w * 0.3, cy - w * 0.45),
                         (500 + w * 0.05, cy + w * 0.02), (500 + w * 0.28, cy + w * 0.02),
                         (500 - w * 0.18, cy + w * 0.6), (500 - w * 0.02, cy + w * 0.06),
                         (500 - w * 0.26, cy + w * 0.06)]))
    return compose([bottle, neck, cork], holes)


def moon_star(rnd):
    kind = rnd.choice(("crescent", "moon_face", "stars", "star", "moon_stars"))
    if kind == "crescent":
        r = rnd.uniform(300, 360)
        return compose([ell(500, 500, r, r)], [ell(500 + r * rnd.uniform(0.34, 0.5), 500 - r * 0.18, r * 0.9, r * 0.9)])
    if kind == "moon_face":
        r = rnd.uniform(300, 350)
        g = compose([ell(500, 500, r, r)], [ell(500 + r * 0.44, 500 - r * 0.14, r * 0.88, r * 0.88)])
        return compose([g], [ell(500 - r * 0.2, 500 - r * 0.18, r * 0.09, r * 0.13)])
    if kind == "star":
        return compose([star_poly(500, 500, rnd.uniform(330, 400), rnd.choice((4, 5, 6, 8)),
                                  rnd.uniform(0.36, 0.5))])
    if kind == "moon_stars":
        r = rnd.uniform(240, 290)
        g = compose([ell(420, 480, r, r)], [ell(420 + r * 0.42, 480 - r * 0.16, r * 0.88, r * 0.88)])
        extra = [star_poly(rnd.uniform(620, 860), rnd.uniform(220, 780), rnd.uniform(50, 110), 5, 0.42)
                 for _ in range(3)]
        return compose([g] + extra)
    return compose([star_poly(rnd.uniform(180, 820), rnd.uniform(180, 820), rnd.uniform(55, 130),
                              rnd.choice((4, 5)), 0.42) for _ in range(rnd.choice((5, 7, 9)))])


def skull(rnd):
    r = rnd.uniform(240, 290)
    cy = 460
    solids = [ell(500, cy, r, r * 1.05), rrect(500 - r * 0.56, cy + r * 0.66, r * 1.12, r * 0.66, r * 0.24)]
    holes = []
    ew = r * rnd.uniform(0.27, 0.34)
    for sx in (-1, 1):
        holes.append(ell(500 + sx * r * 0.42, cy - r * 0.1, ew, ew * 1.12))
    holes.append(pg([(500 - r * 0.13, cy + r * 0.44), (500 + r * 0.13, cy + r * 0.44), (500, cy + r * 0.14)]))
    n = rnd.choice((3, 4))
    for i in range(n):
        x = 500 - r * 0.34 + i * (r * 0.68 / max(1, n - 1))
        holes.append(rrect(x - r * 0.045, cy + r * 0.76, r * 0.09, r * 0.34, r * 0.02))
    if rnd.random() < 0.3:
        holes.append(star_poly(500 + r * 0.62, cy - r * 0.62, r * 0.18, 5, 0.42))
    return compose(solids, holes)


def bone(rnd):
    ln = rnd.uniform(500, 640)
    t = rnd.uniform(66, 92)
    ang = math.radians(rnd.uniform(-40, 40))
    dx, dy = math.cos(ang), math.sin(ang)
    p0 = (500 - dx * ln / 2, 500 - dy * ln / 2)
    p1 = (500 + dx * ln / 2, 500 + dy * ln / 2)
    solids = [thick_line(p0, p1, t)]
    for (px, py), s in ((p0, 1), (p1, -1)):
        for side in (-1, 1):
            solids.append(ell(px + s * dx * t * 0.1 + side * dy * t * 0.58,
                              py + s * dy * t * 0.1 - side * dx * t * 0.58, t * 0.64, t * 0.64))
    return compose(solids)


def tombstone(rnd):
    w = rnd.uniform(280, 340)
    h = rnd.uniform(460, 560)
    cy = 600
    top = rnd.choice(("round", "flat", "cross"))
    if top == "round":
        pts = [(500 - w, cy + h / 2), (500 - w, cy - h / 2 + w)]
        pts += bez((500 - w, cy - h / 2 + w), (500 - w, cy - h / 2 - w * 0.35),
                   (500 + w, cy - h / 2 - w * 0.35), (500 + w, cy - h / 2 + w))
        pts.append((500 + w, cy + h / 2))
        stone = pg(pts)
    elif top == "flat":
        stone = rrect(500 - w, cy - h / 2, w * 2, h, w * 0.14)
    else:
        stone = pg([(500 - w * 0.34, cy + h / 2), (500 - w * 0.34, cy - h * 0.14),
                    (500 - w, cy - h * 0.14), (500 - w, cy - h * 0.44),
                    (500 - w * 0.34, cy - h * 0.44), (500 - w * 0.34, cy - h / 2 - w * 0.25),
                    (500 + w * 0.34, cy - h / 2 - w * 0.25), (500 + w * 0.34, cy - h * 0.44),
                    (500 + w, cy - h * 0.44), (500 + w, cy - h * 0.14),
                    (500 + w * 0.34, cy - h * 0.14), (500 + w * 0.34, cy + h / 2)])
    ground = ell(500, cy + h / 2, w * 1.55, w * 0.24)
    holes = []
    if top != "cross" and rnd.random() < 0.6:
        holes.append(pg([(500 - w * 0.12, cy - h * 0.08), (500 + w * 0.12, cy - h * 0.08),
                         (500 + w * 0.12, cy + h * 0.22), (500 - w * 0.12, cy + h * 0.22)]))
        holes.append(pg([(500 - w * 0.34, cy - h * 0.02), (500 + w * 0.34, cy - h * 0.02),
                         (500 + w * 0.34, cy + h * 0.06), (500 - w * 0.34, cy + h * 0.06)]))
    return compose([stone, ground], holes)


def house(rnd):
    w = rnd.uniform(320, 390)
    base_y = 780
    bh = rnd.uniform(270, 330)
    solids = [pg([(500 - w, base_y), (500 - w, base_y - bh), (500 + w, base_y - bh), (500 + w, base_y)]),
              pg([(500 - w * 1.16, base_y - bh), (500, base_y - bh - rnd.uniform(150, 220)),
                  (500 + w * 1.16, base_y - bh)])]
    n = rnd.choice((2, 3))
    for i in range(n):
        tw = w * 0.2
        tx = 500 - w * 0.66 + (i * (w * 1.32 / (n - 1)) if n > 1 else w * 0.66)
        th = rnd.uniform(150, 250)
        solids.append(pg([(tx - tw, base_y - bh), (tx - tw, base_y - bh - th),
                          (tx, base_y - bh - th - tw * 1.2), (tx + tw, base_y - bh - th),
                          (tx + tw, base_y - bh)]))
    holes = [rrect(500 - w * 0.15, base_y - bh * 0.6, w * 0.3, bh * 0.6, w * 0.15)]
    for sx in (-1, 1):
        holes.append(pg([(500 + sx * w * 0.56 - w * 0.13, base_y - bh * 0.82),
                         (500 + sx * w * 0.56 + w * 0.13, base_y - bh * 0.82),
                         (500 + sx * w * 0.56 + w * 0.13, base_y - bh * 0.46),
                         (500 + sx * w * 0.56 - w * 0.13, base_y - bh * 0.46)]))
    return compose(solids, holes)


def candy(rnd):
    kind = rnd.choice(("corn", "wrapped", "apple", "lolly"))
    if kind == "corn":
        w = rnd.uniform(210, 270)
        body = pg([(500, 210), (500 + w, 790), (500 - w, 790)])
        holes = [pg([(500 - w * 0.62, 610), (500 + w * 0.62, 610), (500 + w * 0.68, 650), (500 - w * 0.68, 650)]),
                 pg([(500 - w * 0.3, 420), (500 + w * 0.3, 420), (500 + w * 0.36, 460), (500 - w * 0.36, 460)])]
        return compose([body], holes)
    if kind == "wrapped":
        w = rnd.uniform(195, 245)
        return compose([ell(500, 500, w, w * 0.64),
                        pg([(500 - w, 500), (500 - w - 150, 375), (500 - w - 118, 500), (500 - w - 150, 625)]),
                        pg([(500 + w, 500), (500 + w + 150, 375), (500 + w + 118, 500), (500 + w + 150, 625)])])
    if kind == "apple":
        r = rnd.uniform(230, 280)
        return compose([ell(500, 450, r, r * 1.03), rrect(500 - 22, 450 + r * 0.7, 44, 330, 18),
                        pg([(500 - 12, 450 - r), (500 - 44, 450 - r - 120), (500 + 34, 450 - r - 66)])])
    r = rnd.uniform(215, 265)
    spiral = compose([ell(500, 400, r, r)],
                     [thick_path([(500 + (r * 0.8 * i / 90) * math.cos(i / 90 * 6.0 * math.pi),
                                   400 + (r * 0.8 * i / 90) * math.sin(i / 90 * 6.0 * math.pi))
                                  for i in range(1, 91)], r * 0.12)])
    return compose([spiral, rrect(500 - 20, 400 + r * 0.55, 40, 360, 16)])


def frame(rnd):
    kind = rnd.choice(("banner", "circle", "plaque"))
    if kind == "banner":
        h = rnd.uniform(210, 270)
        return compose([pg([(90, 500 - h / 2), (910, 500 - h / 2), (910, 500 + h / 2), (90, 500 + h / 2)]),
                        pg([(90, 500 - h / 2), (20, 500 - h / 2 - 62), (20, 500 + h / 2 + 62), (90, 500 + h / 2)]),
                        pg([(910, 500 - h / 2), (980, 500 - h / 2 - 62), (980, 500 + h / 2 + 62), (910, 500 + h / 2)])])
    if kind == "circle":
        r = rnd.uniform(350, 410)
        t = rnd.uniform(28, 48)
        ring = compose([ell(500, 500, r, r)], [ell(500, 500, r - t, r - t)])
        pts = rnd.choice((6, 8, 10))
        extra = [star_poly(500 + (r + t) * math.cos(2 * math.pi * i / pts),
                           500 + (r + t) * math.sin(2 * math.pi * i / pts), t * 1.3, 5, 0.42)
                 for i in range(pts)]
        return compose([ring] + extra)
    w, h, t = rnd.uniform(370, 420), rnd.uniform(250, 310), 30
    return compose([rrect(500 - w, 500 - h, w * 2, h * 2, 42)],
                   [rrect(500 - w + t, 500 - h + t, (w - t) * 2, (h - t) * 2, 30)])


# ---------------------------------------------------------------- lettering
QUOTES = [
    "BOO", "BOO!", "EEK", "SPOOKY", "SPOOKY SEASON", "STAY SPOOKY", "TRICK OR TREAT",
    "HAPPY HALLOWEEN", "WITCH PLEASE", "CREEP IT REAL", "BOO CREW", "HEY BOO",
    "LITTLE MONSTER", "TOO CUTE TO SPOOK", "GHOUL GANG", "FEELIN SPOOKY",
    "PUMPKIN PATCH", "HOCUS FOCUS", "BASIC WITCH", "SWEET OR SPOOKY", "BAT VIBES",
    "SPOOK CENTRAL", "CANDY CORN CREW", "GHOSTED", "RESTING WITCH FACE", "SPOOKTACULAR",
    "MY BROOM BROKE", "FANG YOU", "BITE ME", "SKELE FUN", "HAUNTED HOUSE",
    "TREAT YO SELF", "OCTOBER 31", "SPOOKY MAMA", "SPOOKY DADA", "PUMPKIN SPICE",
    "COSY SEASON", "BOO BEES", "WITCHY VIBES", "MOON CHILD", "SPOOKY VIBES ONLY",
    "GHOULS NIGHT", "TRICK OR TEACH", "NAP QUEEN", "SPOOKY LITTLE THING",
]


def text_line_paths(font, glyphs, cmap, text, tracking):
    upem = font["head"].unitsPerEm
    paths, x = [], 0.0
    for ch in text:
        name = cmap.get(ord(ch))
        if name is None:
            x += upem * 0.3
            continue
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        d = pen.getCommands()
        if d:
            paths.append((d, x))
        x += glyphs[name].width + tracking * upem
    return paths, x, upem


def quote_svg(path, font, glyphs, cmap, text, rnd):
    words = text.split()
    if len(words) >= 4:
        mid = (len(words) + 1) // 2
        lines = [" ".join(words[:mid]), " ".join(words[mid:])]
    elif len(words) in (2, 3) and rnd.random() < 0.7:
        lines = [words[0], " ".join(words[1:])] if len(words) == 3 else [words[0], words[1]]
    else:
        lines = [text]
    rendered, widest = [], 1.0
    for ln in lines:
        paths, adv, upem = text_line_paths(font, glyphs, cmap, ln, rnd.uniform(0.0, 0.05))
        rendered.append((paths, adv))
        widest = max(widest, adv)
    upem = font["head"].unitsPerEm
    line_h = upem * 1.02
    total_h = line_h * len(lines)
    scale = min(880.0 / widest, 780.0 / total_h)
    groups = []
    y0 = 500 - (total_h * scale) / 2 + line_h * 0.76 * scale
    for i, (paths, adv) in enumerate(rendered):
        x0 = 500 - (adv * scale) / 2
        yy = y0 + i * line_h * scale
        for d, gx in paths:
            groups.append(f'<g transform="translate({x0 + gx * scale:.2f},{yy:.2f}) '
                          f'scale({scale:.4f},{-scale:.4f})"><path d="{d}"/></g>')
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" '
           f'height="1000"><title>{text}</title><g fill="#000000" fill-rule="nonzero">'
           f'{"".join(groups)}</g></svg>')
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)


# ---------------------------------------------------------------- build
GROUPS = [
    ("01-Bats", bat, 32),
    ("02-Pumpkins", lambda r: pumpkin(r, True), 40),
    ("03-Plain-Pumpkins", lambda r: pumpkin(r, False), 12),
    ("04-Ghosts", ghost, 40),
    ("05-Black-Cats", cat, 26),
    ("06-Spiders", spider, 20),
    ("07-Cobwebs", web, 18),
    ("08-Witch-Hats", witch_hat, 26),
    ("09-Broomsticks", broom, 18),
    ("10-Cauldrons", cauldron, 20),
    ("11-Potion-Bottles", potion, 26),
    ("12-Moons-and-Stars", moon_star, 30),
    ("13-Skulls", skull, 26),
    ("14-Bones", bone, 16),
    ("15-Tombstones", tombstone, 22),
    ("16-Haunted-Houses", house, 22),
    ("17-Sweets", candy, 22),
    ("18-Frames-and-Banners", frame, 22),
]
QUOTE_COUNT = 82


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    total = 0
    for folder, fn, count in GROUPS:
        d = os.path.join(OUT, folder)
        os.makedirs(d)
        rnd = random.Random(sum(map(ord, folder)))
        made = 0
        while made < count:
            g = fn(rnd)
            if g.is_empty or g.area < 8000:
                continue
            made += 1
            total += 1
            name = f"{folder[3:].lower().replace('-', '_')}_{made:03d}"
            to_svg(g, os.path.join(d, name + ".svg"), name.replace("_", " "))
        print(f"  {folder}: {made}")

    d = os.path.join(OUT, "19-Words-and-Quotes")
    os.makedirs(d)
    font = TTFont(FONT)
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    rnd = random.Random(99)
    for i in range(QUOTE_COUNT):
        q = QUOTES[i % len(QUOTES)]
        slug = q.lower().replace(" ", "_").replace("!", "")
        quote_svg(os.path.join(d, f"quote_{i + 1:03d}_{slug}.svg"), font, glyphs, cmap, q, rnd)
        total += 1
    font.close()
    print(f"  19-Words-and-Quotes: {QUOTE_COUNT}")

    with open(os.path.join(OUT, "READ-ME-FIRST.txt"), "w", encoding="utf-8") as f:
        f.write(
            "500 SVG CUT FILES - The Halloween PNG Vault\n"
            "==========================================\n\n"
            "HOW TO USE\n"
            "Cricut Design Space: New Project > Upload > Upload Image > drag the .svg in.\n"
            "Silhouette Studio: File > Open, then set your cut lines.\n"
            "Canva, Illustrator, Affinity, Inkscape: open as a vector, scale with no quality loss.\n\n"
            "WHAT THEY ARE\n"
            "Single-colour silhouettes on a 1000 x 1000 canvas, sized for vinyl, HTV, cardstock\n"
            "and paper. Faces, windows and cut-outs are real holes, so they cut straight away.\n\n"
            "LICENCE\n"
            "Sell as many finished physical products as you like (shirts, signs, decals, cards).\n"
            "Do not resell or share the SVG files themselves, as they are or modified.\n\n"
            "FONT NOTICE\n"
            "The lettering files were outlined from Baloo 2, licensed under the SIL Open Font\n"
            "Licence 1.1. The outlines are artwork here, not an installable font.\n"
        )
    print("SVG files:", total)
    return total


if __name__ == "__main__":
    build()
