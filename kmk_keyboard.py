import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

# Encoder Setup
encoders = EncoderHandler()
keyboard.modules.append(encoders)

encoders.pins = [
    (board.GP2, board.GP3),  # Encoder 1
    (board.GP4, board.GP5),  # Encoder 2
    (board.GP6, board.GP7),  # Encoder 3
]

encoders.map = [
    ((KC.MPRV, KC.MNXT), KC.MPLY),  # Encoder 1: Prev/Next, press = Play/Pause
    ((KC.VOLD, KC.VOLU), KC.MUTE), # Encoder 2: Volume down/up, press = Mute
    ((KC.NO, KC.NO), KC.NO),       # Encoder 3: Unused
]

# Matrix setup (example GP pins)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.row_pins = (board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16)
keyboard.diode_orientation = DiodeOrientation.COL2ROW  # Mostly column-side

# This is a placeholder layout; we’ll replace it with your exact 62-key UK ISO layout
keyboard.keymap = [
    [
        KC.ESC,  KC.N1,    KC.N2,    KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,
        KC.N0,   KC.MINS,  KC.EQL,  KC.BSPC, KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,
        KC.Y,    KC.U,     KC.I,    KC.O,   KC.P,    KC.LBRC, KC.RBRC, KC.ENT,  KC.LSFT, KC.A,
        KC.S,    KC.D,     KC.F,    KC.G,   KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.NUHS, KC.LSFT,  KC.Z,    KC.X,   KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM,
        KC.DOT,  KC.SLSH,  KC.RSFT, KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.MO(1),
    ]
]

if __name__ == '__main__':
    keyboard.go()
