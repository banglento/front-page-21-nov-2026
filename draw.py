#!/usr/bin/env python3
"""Draw the Front Page poster for Saturday 21 November 2026.

A newspaper front page, drawn programmatically with Pillow so every
word is rendered from real fonts (no AI image generation, no garbled
text). Output: entry.png, 1024x1024, in this script's directory.

Stories (all reported on 21 November 2026; see SOURCES.md):
  lead    Iran says it struck US bases in Bahrain; Bahrain reports
          a fire at a civilian industrial facility.
  ukraine Russian ballistic missile hits Kryvyi Rih, killing two.
  markets AI stock sell-off pushes US stocks into correction.
  climate COP31 talks in Antalya run past deadline over fossil fuels.
  mexico  Mexico captures FBI most-wanted cartel boss 'Chapo Isidro'.
  court   France seeks UN Security Council action after the World
          Court's genocide ruling on Myanmar.
  brief   BepiColombo orbits Mercury; Wolbachia mosquitoes cut
          dengue in Brazil; EU-Indonesia trade deal signed;
          James Harden scores 51 points.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (164, 22, 22)
NAVY = (16, 32, 64)
GREY = (90, 86, 78)
BODY = (40, 38, 34)
FAINT = (178, 172, 158)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, max_w, leading, fill=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def story(draw, x, y, w, label, headline, body, head_size=25, body_size=17):
    """Kicker + headline + short summary; returns the y below the story."""
    draw.text((x, y), label, font=font(SANS_B, 17), fill=RED)
    y += 24
    y = text_block(draw, x, y, headline, font(SERIF_B, head_size), w, head_size + 5)
    y += 3
    y = text_block(draw, x, y, body, font(SANS, body_size), w, body_size + 5, fill=BODY)
    return y


def draw_lead_graphic(draw, x, y, w, h):
    """Simple drawn scene: night sky, missile arc, burst over a coast."""
    draw.rectangle([x, y, x + w, y + h], fill=NAVY)
    for sx, sy in [(30, 22), (90, 48), (150, 16), (230, 36), (286, 66), (60, 84), (200, 74)]:
        draw.ellipse([x + sx - 2, y + sy - 2, x + sx + 2, y + sy + 2], fill=(220, 224, 235))
    draw.rectangle([x, y + h - 40, x + w, y + h], fill=(24, 74, 110))
    draw.polygon([(x, y + h - 40), (x + 70, y + h - 62), (x + 150, y + h - 46),
                  (x + 240, y + h - 66), (x + w, y + h - 50), (x + w, y + h - 40)],
                 fill=(10, 20, 38))
    pts = []
    for t in range(0, 101):
        fx = t / 100.0
        px = x + 24 + fx * (w - 90)
        py = y + h - 92 - (fx * (1 - fx)) * 4 * 44 + fx * 34
        pts.append((px, py))
    draw.line(pts, fill=(255, 196, 64), width=5)
    bx, by = pts[-1]
    for dx, dy in [(0, -18), (13, -13), (18, 0), (13, 13), (0, 18), (-13, 13), (-18, 0), (-13, -13)]:
        draw.line([bx, by, bx + dx, by + dy], fill=(255, 120, 40), width=5)
    draw.ellipse([bx - 8, by - 8, bx + 8, by + 8], fill=(255, 214, 90))
    draw.text((x + 14, y + h - 30), "BAHRAIN - STRAIT OF HORMUZ",
              font=font(SANS_B, 16), fill=(235, 240, 248))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36
    right = W - M

    # --- top strip + masthead --------------------------------------
    d.text((M, 12), "THE WORLD'S NEWS, SUMMED UP IN ONE IMAGE", font=font(SANS_B, 15), fill=GREY)
    tag = "ONE DAY - ONE PAGE"
    d.text((right - d.textlength(tag, font=font(SANS_B, 15)), 12), tag, font=font(SANS_B, 15), fill=GREY)
    d.line([M, 36, right, 36], fill=INK, width=3)
    mast = font(SERIF_B, 72)
    title = "FRONT PAGE"
    d.text(((W - d.textlength(title, font=mast)) / 2, 42), title, font=mast, fill=INK)
    d.line([M, 128, right, 128], fill=INK, width=2)

    # --- date bar ----------------------------------------------------
    d.rectangle([M, 138, right, 190], fill=INK)
    date_f = font(SERIF_B, 38)
    date_txt = "SATURDAY 21 NOVEMBER 2026"
    d.text(((W - d.textlength(date_txt, font=date_f)) / 2, 145), date_txt,
           font=date_f, fill=(250, 248, 240))

    # --- lead story (left) + graphic and Ukraine (right rail) --------
    lx, lw = M, 596
    y = 208
    d.text((lx, y), "LEAD STORY - MANAMA, BAHRAIN", font=font(SANS_B, 18), fill=RED)
    y += 26
    y = text_block(d, lx, y, "Iran Says It Struck US Bases in Bahrain",
                   font(SERIF_B, 41), lw, 47)
    y += 5
    y = text_block(d, lx, y,
                   "Iran's Revolutionary Guards said they hit two US military "
                   "positions in Bahrain. Bahrain said the attack struck a "
                   "civilian industrial site and started a fire, reported no "
                   "injuries, and said its air defences intercepted other "
                   "attacks. The US denied Iran's claim that it hit an F-16.",
                   font(SANS, 18), lw, 23, fill=BODY)
    lead_end = y

    gx, gw = 656, right - 656
    draw_lead_graphic(d, gx, 208, gw, 158)
    uk_end = story(d, gx, 380, gw, "UKRAINE - KRYVYI RIH",
                   "Missile Kills Two in Zelensky's Hometown",
                   "A Russian ballistic missile hit the centre of Kryvyi "
                   "Rih, wounding dozens.", head_size=22, body_size=16)
    block_end = max(lead_end, uk_end)
    d.line([M, block_end + 12, right, block_end + 12], fill=INK, width=3)

    # --- two-by-two secondary grid (left) + In Brief rail (right) ----
    gy = block_end + 28
    col_w = (596 - 24) // 2
    x1, x2 = M, M + col_w + 24
    e1 = story(d, x1, gy, col_w, "MARKETS - NEW YORK",
               "AI Sell-Off Pushes US Stocks Into Correction",
               "The S&P 500 and Dow fell into correction and the Nasdaq "
               "erased its 2026 gains as AI and chip shares slid.")
    e2 = story(d, x2, gy, col_w, "CLIMATE - ANTALYA, TURKEY",
               "COP31 Talks Run Past Deadline Over Fossil Fuels",
               "The UN climate summit ran into overtime with no deal, as "
               "nearly 200 countries split over fossil fuels.")
    row1_end = max(e1, e2)
    d.line([x2 - 12, gy, x2 - 12, row1_end], fill=FAINT, width=2)
    gy2 = row1_end + 18
    e3 = story(d, x1, gy2, col_w, "MEXICO - SINALOA",
               "Mexico Captures FBI Most-Wanted Cartel Boss",
               "Special forces seized 'Chapo Isidro' in Guasave; gunfights "
               "and blockades followed, killing at least 11.")
    e4 = story(d, x2, gy2, col_w, "WORLD COURT - THE HAGUE",
               "France Seeks UN Action on Myanmar Ruling",
               "France will seek a UN Security Council meeting after "
               "Myanmar rejected the World Court's genocide ruling.")
    row2_end = max(e3, e4)
    d.line([x2 - 12, gy2, x2 - 12, row2_end], fill=FAINT, width=2)

    # In Brief rail under Ukraine, aligned with the grid
    bx, bw2 = gx, gw
    box_top = gy
    box_bot = 968
    d.rectangle([bx, box_top, right, box_bot], outline=INK, width=3)
    d.rectangle([bx, box_top, right, box_top + 38], fill=INK)
    d.text((bx + 14, box_top + 7), "IN BRIEF", font=font(SANS_B, 21), fill=(250, 248, 240))
    briefs = [
        ("SPACE", "Europe and Japan's BepiColombo spacecraft entered orbit "
                  "around Mercury after an eight-year journey."),
        ("HEALTH - BRAZIL", "Mosquitoes carrying Wolbachia bacteria cut "
                            "dengue cases among children, researchers reported."),
        ("TRADE - BRUSSELS", "The EU and Indonesia signed a trade deal "
                             "removing 98.5% of tariffs on EU goods."),
        ("SPORT - NBA", "James Harden scored 51 points, passing Kobe Bryant "
                        "on the all-time list of 50-point games."),
    ]
    iy = box_top + 52
    for label, item in briefs:
        d.text((bx + 14, iy), label, font=font(SANS_B, 15), fill=RED)
        iy += 20
        iy = text_block(d, bx + 14, iy, item, font(SANS, 16), bw2 - 28, 20, fill=BODY)
        iy += 12
    assert iy <= box_bot, f"In Brief overflow: {iy} > {box_bot}"
    assert row2_end <= 962, f"grid overflow: {row2_end}"

    # --- footer -------------------------------------------------------
    d.line([M, 978, right, 978], fill=INK, width=2)
    foot = "Sources: Al Jazeera - BBC News - France 24 - The Guardian - UPI - CBS News - PBS. All stories reported on 21 November 2026."
    d.text((M, 986), foot, font=font(SANS, 14), fill=GREY)

    out = Path(__file__).resolve().parent / "entry.png"
    img.save(out, format="PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes); lead_end={lead_end} uk_end={uk_end} row2_end={row2_end} brief_end={iy}")


if __name__ == "__main__":
    main()
