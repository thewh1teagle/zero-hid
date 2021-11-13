from typing import List

from .hid.keyboard import send_keystroke, release_keys
from .hid.keycodes import KeyCodes
from time import sleep
import json
import operator
from functools import reduce
import pkgutil

class Keyboard:
    US_KEYBOARD = json.loads( pkgutil.get_data(__name__, "keymaps/US.json").decode() )
    
    def __init__(self, dev='/dev/hidg0') -> None:
        self.dev = dev

    def type(self, text, delay=0):
        for c in text:
            key_map = self.US_KEYBOARD['Mapping'][c]
            key_map = key_map[0]
            mods = key_map['Modifiers']
            keys = key_map['Keys']
            mods = [KeyCodes[i] for i in mods]
            keys = [KeyCodes[i] for i in keys]
            
            if len(mods) == 1:
                mods = mods[0]
            else:
                mods = reduce(operator.and_, mods, 0)
            send_keystroke(self.dev, mods, keys[0])
            sleep(delay)

    def release(self):
        release_keys(self.dev)
