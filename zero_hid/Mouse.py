from . import defaults
from .hid.mouse import relative_mouse_event, absolute_mouse_event
from typing import SupportsInt

class RelativeMoveRangeError(Exception):
    pass


class Mouse:
    def __init__(self, dev = defaults.RELATIVE_MOUSE_PATH, absolute = False) -> None:
        self.move = self.__move_absolute if absolute else self.__move_relative # dynamic move method
        self.__send_mouse_event = absolute_mouse_event if absolute else relative_mouse_event # dynamic mouse event method
        if not hasattr(dev, 'write'): # check if file like object
            self.dev = open(dev, 'ab+')
        else:
            self.dev = dev

    
    def left_click(self):
        self.__send_mouse_event(self.dev, 0x1, 0, 0, 0, 0)
        self.__send_mouse_event(self.dev, 0x0, 0, 0, 0, 0)
    
    def right_click(self):
        self.__send_mouse_event(self.dev, 0x2, 0, 0, 0, 0)
        self.__send_mouse_event(self.dev, 0x0, 0, 0, 0, 0)

    def __move_relative(self, x, y):
        """
        move the mouse in relative mode
        x,y should be in range of -127 to 127
        """
        if not -127 <= x <= 127: 
            raise RelativeMoveRangeError(f"Value of x: {x} out of range (-127 - 127)")
        if not -127 <= y <= 127:
            RelativeMoveRangeError(f"Value of y: {y} out of range (-127 - 127)")
        self.__send_mouse_event(self.dev, 0x0, x, y, 0, 0)
        
    def __move_absolute(self, x, y):
        if not 0 <= x <= 65535: 
            raise RelativeMoveRangeError(f"Value of x: {x} out of range (0 - 65535)")
        if not 0 <= y <= 65535:
            RelativeMoveRangeError(f"Value of y: {y} out of range (0 - 65535)")
        self.__send_mouse_event(self.dev, 0x0, x, y, 0, 0)
        
        
    def __enter__(self):
        return self


    def _clean_resources(self):
        self.dev.close()    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._clean_resources()
        
        
    
    def close(self):
        self._clean_resources()