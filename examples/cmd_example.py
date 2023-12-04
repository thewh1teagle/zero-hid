from zero_hid import Keyboard, KeyCodes
from zero_hid.hid import keycodes
from time import sleep

with Keyboard() as k:
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
    sleep(2)
    k.type('cmd')
    sleep(2)
    k.press([], KeyCodes.KEY_ENTER)
    sleep(2)
    for i in range(1, 10):
        k.type(f'color {i}')
        k.press([], KeyCodes.KEY_ENTER)
    k.type('cls & pause & exit')
    k.press([], KeyCodes.KEY_ENTER)