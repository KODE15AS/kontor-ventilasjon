#!/usr/bin/env python3
"""Genererer kontor-mal.svg fra DXF-originalen.

Ren geometri-mal i KODE15-profil, uten tekst — brukes som underlag for
sonemerker og etiketter i KODE-klima.

Bruk:  python3 dxf-til-svg.py   (krever ezdxf: pip install ezdxf)
"""
import re
from pathlib import Path

import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.svg import SVGBackend
from ezdxf.addons.drawing.layout import Page
from ezdxf.addons.drawing.config import (
    Configuration, ColorPolicy, BackgroundPolicy,
)

HER = Path(__file__).resolve().parent
KILDE = HER.parent.parent / "dok" / "2026-09-30-kontor-layout.dxf"
MAAL = HER.parent / "kontor-mal.svg"

# Kun geometrilagene — dimensjoner, tekst, senter-/hjelpe-/skjulte linjer
# og lysplan holdes utenfor malen.
BEHOLD = {"0", "1-YTTERGEOMETRI"}

# KODE15-profil (norm «web-profil»)
STREK = "#233038"   # --k15-skifer
BAKGRUNN = "#F7F4EF"  # --k15-bg

VISNING_BREDDE = 1030  # px; høyde følger av tegningens proporsjoner
STREKTYKKELSE = 950    # i viewBox-enheter (~1 px ved 1030 px bredde)

doc = ezdxf.readfile(KILDE)
msp = doc.modelspace()
for e in list(msp):
    if e.dxf.layer not in BEHOLD:
        msp.delete_entity(e)

cfg = Configuration(
    color_policy=ColorPolicy.CUSTOM,
    custom_fg_color=STREK,
    background_policy=BackgroundPolicy.CUSTOM,
    custom_bg_color=BAKGRUNN,
)
ctx = RenderContext(doc)
backend = SVGBackend()
Frontend(ctx, backend, config=cfg).draw_layout(msp)
svg = backend.get_string(Page(0, 0))

# ezdxf setter fysisk størrelse i mm (1:1 = ~37 m bred!) og hårfin strek;
# sett fornuftig visningsstørrelse og synlig strektykkelse.
m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
vb_b, vb_h = float(m.group(1)), float(m.group(2))
hoyde = round(VISNING_BREDDE * vb_h / vb_b)
svg = re.sub(r'width="[\d.]+mm" height="[\d.]+mm"',
             f'width="{VISNING_BREDDE}" height="{hoyde}"', svg)
svg = re.sub(r'stroke-width: [\d.]+;',
             f'stroke-width: {STREKTYKKELSE};', svg)

MAAL.write_text(svg, encoding="utf-8")
print(f"skrev {MAAL} ({VISNING_BREDDE}x{hoyde} px)")
