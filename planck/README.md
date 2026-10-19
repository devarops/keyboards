# Planck rev6 Drop

Ortholinear 4x12 board from Drop, configured with the QMK Configurator and built with the
QMK command line.

- Board: `planck/rev6_drop`, layout `LAYOUT_ortho_4x12`.
- Layout: `planck.json`, a Configurator export with three layers: letters, then numbers with
  symbols and arrows, then function keys with a numpad and backlight controls.

## Change the layout

1. Open [config.qmk.fm](https://config.qmk.fm) and choose the Planck rev6 Drop.
2. Import `planck.json`.
3. Make the change in the Configurator.
4. Download the keymap file from the site.
5. Compile and flash it:

   ```bash
   qmk compile -c keymap.json
   qmk flash -c keymap.json
   ```

6. Press the keyboard's reset button.

This file records the keymap; the board keeps the compiled firmware. Copy the download back
into this folder so the two stay the same.
