import board
import time
import random
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

korboard = KMKKeyboard()

korboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14)
korboard.row_pins = (board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20)
korboard.diode_orientation = DiodeOrientation.COL2ROW

korboard.keymap = [
    [
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.PSCR, KC.PAUS,
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.HOME,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.PGUP,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.NO,   KC.ENT,  KC.PGDN,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.NO,   KC.RSFT, KC.NO,   KC.END,
        KC.LCTL, KC.LWIN, KC.LALT, KC.NO,   KC.SPC,  KC.NO,   KC.NO,   KC.NO,   KC.RALT, KC.NO,   KC.NO,   KC.APP,  KC.RCTL, KC.DEL,  KC.INS,
    ]
]

displayio.release_displays()
screen1 = adafruit_displayio_ssd1306.SSD1306(displayio.I2CDisplay(board.I2C(scl=board.GP27, sda=board.GP26), device_address=0x3C), width=128, height=64)
screen2 = adafruit_displayio_ssd1306.SSD1306(displayio.I2CDisplay(board.I2C(scl=board.GP22, sda=board.GP21), device_address=0x3D), width=128, height=64)
leds = neopixel.NeoPixel(board.GP28, 90, auto_write=False)
ball_group = displayio.Group()
ball_bmp = displayio.Bitmap(5, 5, 2)
ball_palette = displayio.Palette(2)
ball_palette[1] = 0xFFFFFF

for x in range(5):
    for y in range(5):
        ball_bmp[x, y] = 1

ball = displayio.TileGrid(ball_bmp, pixel_shader=ball_palette)
ball_group.append(ball)
screen1.root_group = ball_group
ball_x, ball_y, ball_vx, ball_vy = 50, 20, 2, 1
kareem_group = displayio.Group()
kareem_label = label.Label(terminalio.FONT, text="Kareem", color=0xFFFFFF, scale=3)
kareem_group.append(kareem_label)
screen2.root_group = kareem_group
kareem_y, kareem_vy = 20, 1
last_update = 0
led_index = -1

while True:
    korboard.go_bare()

    ball_x += ball_vx
    ball_y += ball_vy
    if ball_x <= 0 or ball_x >= 123:
        ball_vx = -ball_vx
    if ball_y <= 0 or ball_y >= 59:
        ball_vy = -ball_vy
    ball.x = ball_x
    ball.y = ball_y
    kareem_y += kareem_vy

    if kareem_y <= 0 or kareem_y >= 44:
        kareem_vy = -kareem_vy
    kareem_label.x = 10
    kareem_label.y = kareem_y

    if time.monotonic() > last_update + 1:
        last_update = time.monotonic()
        if led_index != -1:
            leds[led_index] = (0, 0, 0)
        led_index = random.randint(0, 89)
        leds[led_index] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        leds.show()
