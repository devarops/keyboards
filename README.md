# Keyboards

Layouts for every keyboard I type on, kept in one place so a new machine can reproduce them.

## What it does

Remembers how each keyboard is mapped. Custom layouts otherwise live only inside a board's
memory or an old computer, and a new machine starts from the default layout. Keeping the files
here means a board can be rebuilt, or moved, without rediscovering the mapping by hand.

## The keyboards

| Board | Folder | What is stored |
| --- | --- | --- |
| Planck (rev6 Drop) | `planck/` | layout for the QMK configurator |
| Nyquist Rev. 3 | `nyquist/` | layout saved from VIA |
| perf60 (handwired) | `perf60/` | keyboard definition and keymap |
| Laptop keyboard, via kanata | `kanata/` | software remap, no hardware |

## How to use it

1. Find your board in the table above.
2. Open the configurator that matches it: the layout files are loaded, not compiled by hand.
3. Make the change there.
4. Save the layout back into the board's folder, so this copy stays current.

Board-specific steps are in each folder's own README.

## Before you start

- The keyboard itself, over USB, with a cable you know carries data.
- A Chromium browser (Chrome or Edge) for a board configured with VIA.
- QMK installed, with a `qmk_firmware` checkout, for the Planck and the perf60.

## Run the project

For a VIA board, open [usevia.app](https://usevia.app), authorise the keyboard, and load its
layout file.

For the others, compile and flash the keymap, then press the keyboard's reset button:

```bash
qmk compile -c keymap.json
qmk flash -c keymap.json
```

If the browser cannot see the keyboard, the operating system is withholding access to the
device. `nyquist/README.md` records the change that fixed it on this machine.
