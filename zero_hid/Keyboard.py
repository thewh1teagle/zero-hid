from .hid.keyboard import send_keystroke


class Keyboard:
    def __init__(self, dev='/dev/hidg0') -> None:
        self.dev = dev

