from zero_hid import Mouse
from time import sleep

with Mouse() as m:
    m.scroll_y(50)
    sleep(1)
    m.scroll_x(50)
        