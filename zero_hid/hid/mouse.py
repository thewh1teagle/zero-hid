from . import write as hid_write


def relative_mouse_event(
    dev, buttons, x, y, vertical_wheel_delta, horizontal_wheel_delta, absolute=False
):
    buf = [
        buttons,
        x & 0xFF,
        y & 0xFF,
        vertical_wheel_delta & 0xFF,
        horizontal_wheel_delta & 0xFF,
    ]
    hid_write.write_to_hid_interface(dev, buf)


def absolute_mouse_event(
    dev, buttons, x, y, vertical_wheel_delta, horizontal_wheel_delta
):
    buf = [
        buttons,
        x & 0xFF,
        (x >> 8) & 0xFF,  # Extract the upper byte of x
        y & 0xFF,
        (y >> 8) & 0xFF,  # Extract the upper byte of y
        vertical_wheel_delta & 0xFF,
        horizontal_wheel_delta & 0xFF,
    ]
    hid_write.write_to_hid_interface(dev, buf)
