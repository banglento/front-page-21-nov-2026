# Front Page — 21 November 2026

An entry for the make.fun competition **news-image-20261121** ("Sum up
21 November's world news in one image", $100 prize pool, top 50 paid):
one image that sums up the world news of Saturday 21 November 2026.

The image is a newspaper front page. The date sits in a black bar under
the masthead, the day's biggest story leads, four more stories fill a
two-by-two grid, and an "In Brief" column carries four shorter items —
ten stories in all, across the Middle East, Europe, the Americas and
Asia-Pacific, spanning conflict, markets, climate, justice, science,
trade and sport.

## Stories covered

- **Lead — Bahrain:** Iran's Revolutionary Guards said they struck two
  US military positions in Bahrain; Bahrain said the attack hit a
  civilian industrial site and started a fire, reported no injuries,
  and said its air defences intercepted other attacks. The US denied
  Iran's claim that it hit an F-16. (Al Jazeera, Euronews)
- **Ukraine:** A Russian ballistic missile hit the centre of Kryvyi
  Rih, President Zelensky's hometown, killing two people and wounding
  dozens. (Al Jazeera, France 24)
- **Markets:** An AI and chip stock sell-off pushed the S&P 500 and
  the Dow into correction; the Nasdaq erased its 2026 gains. (UPI,
  The Guardian, BBC News)
- **Climate:** The COP31 UN climate summit in Antalya, Turkey, ran
  past its deadline with no deal, split over fossil fuels. (BBC News,
  France 24, PBS NewsHour)
- **Mexico:** Special forces captured Fausto Isidro Meza Flores,
  "Chapo Isidro", who was on the FBI's ten most-wanted list; the
  violence that followed killed at least 11 people. (BBC News,
  CBS News)
- **World Court:** France said it will seek a UN Security Council
  meeting after Myanmar rejected the International Court of Justice
  ruling that held it responsible for genocide against the Rohingya.
  (PBS NewsHour, The Guardian, The Hindu)

In Brief: BepiColombo (ESA/JAXA) entered orbit around Mercury after an
eight-year journey; researchers reported that Wolbachia-carrying
mosquitoes cut dengue cases among children in Brazil; the EU and
Indonesia signed a trade deal removing 98.5% of tariffs on EU goods;
James Harden scored 51 points, passing Kobe Bryant on the all-time
list of 50-point games.

Full source list: see [SOURCES.md](SOURCES.md).

## How it was made

The poster was drawn programmatically — no AI image generation, so no
word can come out garbled. `draw.py` (Python 3 + Pillow, system serif
and sans fonts) lays out the masthead, date bar, headlines, summaries
and a simple drawn graphic (a missile arc over the Bahrain coast), and
renders `entry.png` at 1024×1024. Re-running `python3 draw.py`
reproduces the same PNG.

`main.ts` (Node 22, standard library only) is the competition
program: it checks the image is within the 1 MiB gate limit and copies
`entry.png` to the output directory (`MAKEFUN_OUTPUT_DIR`, default
`/output`) as `entry.png`, byte for byte, so both grading runs produce
an identical file.

## License

MIT — see [LICENSE](LICENSE).
