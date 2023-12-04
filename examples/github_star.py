from zero_hid import Mouse, Keyboard, KeyCodes
from time import sleep


with Keyboard() as k, Mouse() as m:
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
    sleep(3)
    k.type('https://github.com/thewh1teagle/zero-hid')
    sleep(2)
    k.press([], KeyCodes.KEY_ENTER)
    sleep(3)
    for i in range(20):
        m.move(127, -127)
    for i in range(2):
        m.move(-100, 0)        
    m.move(0, 120)
    sleep(3)
    m.left_click()
