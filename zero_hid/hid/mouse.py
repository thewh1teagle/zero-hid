from . import write as hid_write

def relative_mouse_event(dev, buttons, x, y,
                     vertical_wheel_delta, horizontal_wheel_delta, absolute = False):
    buf = [
        buttons,
        x & 0xff,
        y & 0xff,
        vertical_wheel_delta & 0xff,
        horizontal_wheel_delta & 0xff
    ]
    hid_write.write_to_hid_interface(dev, buf)


def absolute_mouse_event(dev, buttons, x, y,
                     vertical_wheel_delta, horizontal_wheel_delta):
    buf = [
        buttons,
        x & 0xff,
        (x >> 8) & 0xff,  # Extract the upper byte of x
        y & 0xff,
        (y >> 8) & 0xff,  # Extract the upper byte of y
        vertical_wheel_delta & 0xff,
        horizontal_wheel_delta & 0xff
    ]
    hid_write.write_to_hid_interface(dev, buf)