# Keyboards

Personal keyboard layouts. No build, no tests, no CI: each directory holds configuration
files that are consumed by a web configurator or by a QMK checkout.

## Layout

- `planck/planck.json` — QMK Configurator export for `planck/rev6_drop`.
- `nyquist/nyquist.layout.json` — VIA save file for the Nyquist Rev. 3 (USB `0xCB10:0x3156`),
  four layers.
- `nyquist/nyquist-layout-layer0.svg` and `nyquist-layout-layer1.svg` — drawings of the first
  two layers, embedded in that directory's README.
- `nyquist/src/render_layout.py` — renders one layer of the layout file to SVG.
- `perf60/` — a full QMK keyboard definition: `keyboard.json` (Pro Micro, COL2ROW) and
  `keymaps/default/keymap.c` with two layers. Copy it to `keyboards/handwired/perf60` in a
  `qmk_firmware` checkout.
- `kanata/kanata.kbd` — a kanata remap for a laptop keyboard, not a board.

## Verification

Nothing is compiled or tested in this repository. A JSON file is checked by parsing it:

```bash
python3 -m json.tool planck/planck.json >/dev/null
```

Keymap behaviour is verified on the hardware.

## Nyquist drawings

- The board is used rotated 180 degrees, so the stored array starts at its bottom-right key.
  Each drawing reverses the layer to show the board upright, with F11 at the top right.
- A dash is `KC_TRNS`, a transparent key that inherits the layer below; `unused` is `KC_NO`,
  which blocks. The two differ and stay distinct.
- Only the SVG is tracked; `*.png` is ignored.
- QMK spells the right arrow `KC_RGHT`; `KC_RIGHT` is not a keycode.
- The drawings come from `nyquist/src/render_layout.py`; run it with the layer number after a
  layout change, for example `python3 nyquist/src/render_layout.py 1`.

## Two workflows

VIA, for the Nyquist: no toolchain and no flashing. Open <https://usevia.app> in a Chromium
browser over USB, authorise the device, load the layout file, remap, then save the layout from
VIA back into the repository.

QMK, for the Planck and perf60: needs a `qmk_firmware` checkout and the QMK CLI. The Planck
uses `qmk compile -c keymap.json`, then `qmk flash -c keymap.json`. The perf60, once its folder
is copied into `keyboards/handwired/perf60`, uses `qmk compile -kb handwired/perf60 -km default`
and the same flags to flash. Press the reset button to flash.

## Linux: VIA cannot open the device

Symptom: VIA sees the keyboard through WebHID but reports
`NotAllowedError: Failed to open the device`, followed by
`Received invalid protocol version from device`. The second message is a consequence of the
first, not evidence of bad firmware.

Cause: the `/dev/hidraw*` nodes belong to `root` and the browser cannot open them. Check with
`ls -l /dev/hidraw*`; the board's nodes should read `root plugdev`.

Fix, scoped to the Keebio vendor and product IDs:

```bash
sudo tee /etc/udev/rules.d/92-via-keebio.rules >/dev/null <<'EOF'
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", ATTRS{idVendor}=="cb10", ATTRS{idProduct}=="3156", MODE="0660", GROUP="plugdev"
EOF
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=hidraw
```

Then replug the board. Replugging without the rule changes nothing, and restarting the
browser alone does not help. Another VIA board needs its own vendor and product IDs.

## Conventions

- Name VIA exports `<board>.layout.json` so they are not mistaken for QMK keymaps.
- The layout file records what the board holds in EEPROM; committing it is what lets another
  machine reproduce the mapping.
- Commits: a gitmoji, an imperative subject under 72 characters, a blank line, then prose
  explaining why. The default branch is `develop`.
- `README.md` is the index and stays non-technical; board-specific steps live in each
  directory's README; the engineering detail lives here.
