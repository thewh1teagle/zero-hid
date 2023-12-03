import tempfile
from zero_hid import Mouse


def test_left_click():
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmpdir:
        m = Mouse(f'{tmpdir}/test')
        m.left_click()
        m.close()
        f.seek(0)
        assert b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00' == f.read()


def test_move():
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmpdir:
            m = Mouse(f'{tmpdir}/test')
            m.move_relative(100, 100)
            m.close()
            f.seek(0)
            assert b'\x00dd\x00\x00' == f.read()
