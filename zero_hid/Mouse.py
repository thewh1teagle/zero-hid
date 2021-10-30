from .hid.mouse import send_mouse_event

class Mouse:
    def __init__(self, dev='/dev/hidg1') -> None:
        self.dev = dev
    
    def left_click(self):
        send_mouse_event(self.dev, 0x1, 0, 0, 0, 0)
        send_mouse_event(self.dev, 0x0, 0, 0, 0, 0)
    
    def right_click(self):
        send_mouse_event(self.dev, 0x1, 0, 0, 0, 0)
        send_mouse_event(self.dev, 0x2, 0, 0, 0, 0)
    
    def move_relative(self, x, y):
        assert -127 <= x <= 127
        assert -127 <= y <= 127
        send_mouse_event(self.dev, 0x0, x, y, 0, 0)
    