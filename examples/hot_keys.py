from zero_hid import Keyboard, KeyCodes

with Keyboard() as k:
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
