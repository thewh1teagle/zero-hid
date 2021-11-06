from typing import List
from .hid.keyboard import send_keystroke, release_keys
from .hid.keycodes import KeyCodes
from time import sleep

class Keyboard:
    def __init__(self, dev='/dev/hidg0') -> None:
        self.dev = dev

    def send_key(self, keycode, release = True):
        send_keystroke(self.dev, 0, keycode, release)

    def type(self, text, delay=0.001):
        for c in text:
            self.send_key(KeyCodes[c])

    def release(self):
        release_keys(self.dev)
