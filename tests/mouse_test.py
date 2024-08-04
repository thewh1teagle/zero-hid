import tempfile
from zero_hid import Mouse
from common import random_file


def test_left_click():
    with open(random_file(), "ab+") as f:
        m = Mouse(f)
        m.left_click()
        f.seek(0)
        data = f.read()
        f.close()
    assert b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00" == data


def test_move():
    with open(random_file(), "ab+") as f:
        m = Mouse(f)
        m.move(100, 100)
        f.seek(0)
        data = f.read()
        f.close()
    assert b"\x00dd\x00\x00" == data
