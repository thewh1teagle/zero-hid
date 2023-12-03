from . import write as hid_write

def send_mouse_event(dev, buttons, relative_x, relative_y,
                     vertical_wheel_delta, horizontal_wheel_delta):
    buf = [
        buttons,
        relative_x & 0xff,
        (relative_x >> 8) & 0xff,  # Extract the upper byte of relative_x
        relative_y & 0xff,
        (relative_y >> 8) & 0xff,  # Extract the upper byte of relative_y
        vertical_wheel_delta & 0xff,
        horizontal_wheel_delta & 0xff
    ]
    hid_write.write_to_hid_interface(dev, buf)