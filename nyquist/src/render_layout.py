#!/usr/bin/env python3
"""Render a Nyquist layer from nyquist.layout.json as an SVG.

Usage: python3 nyquist/src/render_layout.py [layer] [output.svg]
The layer defaults to 0; the output defaults to
nyquist/nyquist-layout-layer<layer>.svg.

The board is used rotated 180 degrees, so the stored array is reversed
here to draw the board upright.
"""

import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

NYQUIST = Path(__file__).resolve().parent.parent
LAYOUT = NYQUIST / "nyquist.layout.json"

KEY, STEP, SPLIT, PAD = 58, 64, 128, 28
TOP, BOT = 88, 44
COLS, ROWS = 12, 5
WIDTH = 2 * PAD + COLS * STEP - (STEP - KEY) + SPLIT
HEIGHT = TOP + ROWS * STEP - (STEP - KEY) + BOT

SHIFT = {
    "1": "!", "2": "@", "3": "#", "4": "$", "5": "%", "6": "^",
    "7": "&", "8": "*", "9": "(", "0": ")", "-": "_", "=": "+",
    "[": "{", "]": "}", "\\": "|", ";": ":", "'": '"', ",": "<",
    ".": ">", "/": "?", "`": "~",
}
PLAIN = {
    "KC_BSLS": "\\", "KC_RBRC": "]", "KC_LBRC": "[", "KC_MINS": "-",
    "KC_SLSH": "/", "KC_DOT": ".", "KC_COMM": ",", "KC_SCLN": ";",
    "KC_QUOT": "'", "KC_EQL": "=", "KC_GRV": "`", "KC_NO": "",
    "KC_LGUI": "Win", "KC_LALT": "Alt", "KC_LCTL": "Ctrl",
    "KC_LSFT": "Shift", "KC_ENT": "Enter", "KC_BSPC": "Bksp",
    "KC_SPC": "Space", "KC_TAB": "Tab", "KC_ESC": "Esc",
    "KC_LEFT": "\u2190", "KC_RGHT": "\u2192", "KC_UP": "\u2191", "KC_DOWN": "\u2193",
    "KC_PGUP": "PgUp", "KC_PGDN": "PgDn", "KC_HOME": "Home", "KC_END": "End",
}
MODS = {"LCTL": "Ctrl", "LSFT": "Shift", "LALT": "Alt", "RALT": "AltGr", "LGUI": "Win"}


def name(code):
    if code in PLAIN:
        return PLAIN[code]
    if code.startswith("KC_"):
        rest = code[3:]
        if rest.isdigit() or (rest.startswith("F") and rest[1:].isdigit()) or len(rest) == 1:
            return rest
        return rest.replace("_", " ").title()
    return code


def label(code):
    if code.startswith("S("):
        inner = name(code[2:-1])
        return SHIFT.get(inner, "Shift+" + inner)
    if code.startswith("C("):
        return "Ctrl+" + label(code[2:-1])
    return name(code) or "none"


def describe(code):
    if code == "KC_NO":
        return "unused", "", "blank"
    if code == "KC_TRNS":
        return "", "\u2014", "trns"
    if code.startswith("MT("):
        mods, tap = code[3:-1].split(",")
        held = [MODS.get(m.replace("MOD_", "").strip(), m) for m in mods.split("|")]
        held = [h.replace("AltGr", "Gr") for h in held]
        return "hold " + "+".join(held), name(tap), "modtap"
    if code.startswith("LT("):
        layer, tap = code[3:-1].split(",")
        return "hold L" + layer, name(tap), "modtap"
    if code.startswith("TO("):
        return "switch to", "Layer " + code[3:-1], "layer"
    if code.startswith("C(") and "," not in code:
        return "", "Ctrl+" + label(code[2:-1]), "combo"
    if code.startswith("S("):
        return "", label(code), "combo"
    return "", name(code), "plain"


def cell(index):
    half, rest = divmod(index, 30)
    row, col = divmod(rest, 6)
    return col + (6 if half else 0), row


def render(layer_index, out):
    layer = list(reversed(json.load(open(LAYOUT))["layers"][layer_index]))
    parts = []
    for index, code in enumerate(layer):
        col, row = cell(index)
        x = PAD + col * STEP + (SPLIT if col >= 6 else 0)
        y = TOP + row * STEP
        small, main, kind = describe(code)
        fill = {"modtap": "#454545", "layer": "#454545", "combo": "#454545",
                "blank": "#343434", "trns": "#343434"}.get(kind, "#3b3b3b")
        parts.append(
            f'<rect x="{x}" y="{y}" width="{KEY}" height="{KEY}" rx="7" fill="{fill}" '
            f'stroke="#2a2a2a" stroke-width="1"/>'
        )
        cx = x + KEY / 2
        if main:
            size = 17 if len(main) <= 2 else (13 if len(main) <= 6 else (11 if len(main) <= 9 else 8.5))
            colour = "#7d746c" if kind == "trns" else "#f6f2ec"
            offset = 5 if small else 6
            parts.append(
                f'<text x="{cx}" y="{y + KEY / 2 + offset}" text-anchor="middle" '
                f'font-size="{size}" fill="{colour}">{escape(main)}</text>'
            )
        if small:
            parts.append(
                f'<text x="{cx}" y="{y + 15}" text-anchor="middle" '
                f'font-size="{8 if len(small) > 11 else 8.5}" '
                f'fill="#b9b1a8">{escape(small)}</text>'
            )
        if main in SHIFT and not small:
            parts.append(
                f'<text x="{cx}" y="{y + 18}" text-anchor="middle" font-size="9" '
                f'fill="#b9b1a8">{escape(SHIFT[main])}</text>'
            )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
<rect width="{WIDTH}" height="{HEIGHT}" fill="#efe0d7"/>
<rect x="{PAD - 14}" y="{TOP - 14}" width="{WIDTH - 2 * (PAD - 14)}" height="{HEIGHT - TOP - BOT + 20}" rx="16" fill="#f4e6de" stroke="#dcc7ba"/>
<text x="{PAD}" y="32" font-family="DejaVu Sans, sans-serif" font-size="20" font-weight="bold" fill="#3b3330">Nyquist Rev. 3 \u2014 layer {layer_index}</text>
<g font-family="DejaVu Sans, sans-serif" font-weight="500">
{chr(10).join(parts)}
</g>
</svg>'''
    out.write_text(svg)
    print(f"wrote {out}")


def main():
    layer_index = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else NYQUIST / f"nyquist-layout-layer{layer_index}.svg"
    render(layer_index, out)


if __name__ == "__main__":
    main()
