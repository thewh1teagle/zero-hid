from zero_hid import Keyboard, KeyCodes
from zero_hid.hid import keycodes
from time import sleep

k = Keyboard()
k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
k.type('cmd')
k.press([], KeyCodes.KEY_ENTER)
for i in range(1, 10):
    k.type(f'color {i}')
    k.press([], KeyCodes.KEY_ENTER)
k.type('cls & pause & exit')
k.press([], KeyCodes.KEY_ENTER)