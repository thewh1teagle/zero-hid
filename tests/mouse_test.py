from zero_hid import Mouse
from common import read_bytes, temp_path


def test_left_click():
    with temp_path() as p:
        m = Mouse(p)
        m.left_click()
        data = read_bytes(p)
    assert b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00" == data


def test_move():
    with temp_path() as p:
        m = Mouse(p)
        m.move(100, 100)
        data = read_bytes(p)
    assert b"\x00dd\x00\x00" == data
