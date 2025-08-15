// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
/* Base (Layer 0)
 * ,-----------------------------------------.      ,-----------------------------------------.
 * |Raise |   1  |   2  |   3  |   4  |   5  |      |   6  |   7  |   8  |   9  |   0  | F11  |
 * |------+------+------+------+------+------|      |------+------+------+------+------+------|
 * | Tab  |   Q  |   W  |   E  |   R  |   T  |      |   Y  |   U  |   I  |   O  |   P  |  =   |
 * |------+------+------+------+------+------|      |------+------+------+------+------+------|
 * | Ctrl |   A  |   S  |   D  |   F  |   G  |      |   H  |   J  |   K  |   L  |   ;  |  "   |
 * |------+------+------+------+------+------|      |------+------+------+------+------+------|
 * |  `   |   Z  |   X  |   C  |   V  |   B  |      |   N  |   M  |   ,  |   .  |   /  |  -   |
 * |------+------+------+------+------+------|      |------+------+------+------+------+------|
 * |      |      |      |      | Esc  |Enter |      |Space | Bksp |   [  |   ]  |   \  | Win  |
 * `-----------------------------------------'      `-----------------------------------------'
 */
[0] = LAYOUT(
  TO(1),   KC_1,    KC_2,    KC_3,    KC_4,   KC_5,    KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_F11,
  MT(KC_LALT, KC_TAB),    // Tab tap, Alt hold
           KC_Q,    KC_W,    KC_E,    KC_R,   KC_T,    KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_EQL,
  C(KC_B), // Ctrl+B tap, Ctrl hold
           KC_A,    KC_S,    KC_D,    KC_F,   KC_G,    KC_H,    KC_J,    KC_K,    KC_L,    KC_SCLN, KC_QUOT,
  KC_GRV,  KC_Z,    KC_X,    KC_C,    KC_V,   KC_B,    KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_MINS,
  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    LT(1, KC_ESC),          // Escape tap, Layer 1 hold
    MT(MOD_LSFT, KC_ENT),   // Enter tap, Shift hold
    MT(MOD_RALT, KC_SPC),   // Space tap, AltGr hold
    MT(MOD_LCTL, KC_BSPC),  // Backspace tap, Ctrl hold
                                                                         KC_LBRC, KC_RBRC, KC_BSLS, KC_LGUI
),

/* Raised (Layer 1)
 * ,-----------------------------------------.      ,-----------------------------------------.
 * |      |      |      |      |      |      |      |      |      |      |      |      |      |
 * |------+------+------+------+------+------|      |------+------+------+------+------+------|
 * |      |   Q  |   W  |   E  |   R  |   T  |      |   Y  |   U  |   I  |   O  |C-S-V |  =   |
 * |------+------+------+------+------+------|      |------+------+------+------+------+------|
 * | Ctrl |   A  |   S  |   D  |   F  |   G  |      | Left | Down |  Up  |Right |   ;  |  "   |
 * |------+------+------+------+------+------|      |------+------+------+------+------+------|
 * |  `   |   Z  |   X  |   C  |   V  |   B  |      |   N  |   M  |   (  |   )  |   /  |  -   |
 * |------+------+------+------+------+------|      |------+------+------+------+------+------|
 * |Lower |      |      |      |      | S-CR |      |      |      |   (  |   )  |   \  | Win  |
 * `-----------------------------------------'      `-----------------------------------------'
 */
[1] = LAYOUT(
  XXXXXXX, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
  _______, KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    KC_Y,    KC_U,    KC_I,    KC_O,    C(S(KC_V)),
                                                                                                     KC_EQL,
  KC_LCTL, KC_A,    KC_S,    KC_D,    KC_F,    KC_G,    KC_LEFT, KC_DOWN, KC_UP,   KC_RGHT, KC_SCLN, KC_QUOT,
  KC_GRV,  KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    KC_N,    KC_M,    S(KC_9), S(KC_0), KC_SLSH, KC_MINS,
  TO(0),   XXXXXXX, XXXXXXX, XXXXXXX, _______, S(KC_ENTER),
                                                        _______, _______, S(KC_9), S(KC_0), KC_BSLS, KC_LGUI
)

};
