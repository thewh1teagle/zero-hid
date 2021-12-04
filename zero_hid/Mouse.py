from .hid.mouse import send_mouse_event
from typing import SupportsInt


class RelativeMoveRangeError(Exception):
    pass


class Mouse:
    def __init__(self, dev_path='/dev/hidg1') -> None:
        self.dev = open(dev_path, 'ab+')
    
    def left_click(self):
        send_mouse_event(self.dev, 0x1, 0, 0, 0, 0)
        send_mouse_event(self.dev, 0x0, 0, 0, 0, 0)
    
    def right_click(self):
        send_mouse_event(self.dev, 0x1, 0, 0, 0, 0)
        send_mouse_event(self.dev, 0x2, 0, 0, 0, 0)
    
    def move_relative(self, x, y):
        """
        move the mouse in relative mode
        x,y should be in range of -127 to 127
        """
        if not -127 <= x <= 127: 
            raise RelativeMoveRangeError(f"Value of x: {x} out of range (-127 - 127)")
        if not -127 <= y <= 127:
            RelativeMoveRangeError(f"Value of x: {y} out of range (-127 - 127)")
        send_mouse_event(self.dev, 0x0, x, y, 0, 0)
        
        
        
    def __enter__(self):
        return self


    def _clean_resources(self):
        print(f'closing handle {self.dev}')
        self.dev.close()    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._clean_resources()
        
        
    
    def close(self):
        self._clean_resources()