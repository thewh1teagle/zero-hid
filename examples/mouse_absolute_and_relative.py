from zero_hid import Mouse
from time import sleep

# Absolute mouse used for positioning. relative mouse used for clicking.
with Mouse(absolute=False) as rel_mouse, Mouse(absolute=True) as abs_mouse:
    abs_mouse.move(5000, 5000)
    sleep(1)
    rel_mouse.right_click()
    sleep(1)
    abs_mouse.move(3000, 3000)
    sleep(1)
    rel_mouse.left_click()
