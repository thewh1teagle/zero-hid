import tempfile
from zero_hid import Mouse


def test_left_click():
    with tempfile.NamedTemporaryFile() as f:
        m = Mouse(f.name)
        m.left_click()
        m.close()
        f.seek(0)
        assert b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00' == f.read()


def test_move():
    with tempfile.NamedTemporaryFile() as f:
            m = Mouse(f.name)
            m.move_relative(100, 100)
            m.close()
            f.seek(0)
            assert b'\x00dd\x00\x00' == f.read()
