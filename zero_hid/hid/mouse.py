from . import write as hid_write

def send_mouse_event(mouse_path, buttons, relative_x, relative_y,
                     vertical_wheel_delta, horizontal_wheel_delta):

    buf = [0] * 5
    buf[0] = buttons
    buf[1] = relative_x & 0xff
    buf[2] = relative_y & 0xff
    buf[3] = vertical_wheel_delta & 0xff
    buf[4] = horizontal_wheel_delta & 0xff
    hid_write.write_to_hid_interface(mouse_path, buf)