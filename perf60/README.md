# perf60

Handwired 60% board on a Pro Micro, defined entirely in this folder rather than exported from
a configurator.

- Board: `handwired/perf60` once copied into a `qmk_firmware` checkout.
- Layout: `keymaps/default/keymap.c`, with two layers: the base layer and a raised layer with
  navigation keys.
- Definition: `keyboard.json`, with the matrix pins, the Pro Micro board and the enabled
  features.

## Change the layout

1. Edit `keymaps/default/keymap.c`; each layer is drawn as a comment above its definition.
2. Copy this folder to `keyboards/handwired/perf60` in your `qmk_firmware` checkout.
3. Build and flash it:

   ```bash
   qmk compile -kb handwired/perf60 -km default
   qmk flash -kb handwired/perf60 -km default
   ```

4. Press the keyboard's reset button when the flash asks for the bootloader.

The keymap is compiled, not stored on the board as a file, so the checkout is the only source
until the firmware is flashed.
