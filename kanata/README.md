# Laptop keyboard, via kanata

Software remap for a laptop keyboard. Nothing is flashed: kanata runs on the computer and
rewrites the keys as they arrive.

- Config: `kanata.kbd`, with two layers, base and navigation.

## What the file defines

- `tab` taps Tab and holds the navigation layer.
- `caps` taps Ctrl+B and holds Ctrl.
- `'` taps the quote and holds AltGr.
- `ret` taps Enter and holds Right Meta.
- `lsft` taps Escape and holds Left Shift.
- The navigation layer keeps the modifiers and moves arrows onto the home row.

The two tap-hold timings sit at the top as `tap-repress-timeout` (100 ms) and `hold-timeout`
(900 ms); raise the second if a key switches to its held meaning too readily.
