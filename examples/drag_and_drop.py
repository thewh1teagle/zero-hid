from zero_hid import Mouse
from time import sleep

sleep(5)
with Mouse() as m:
    m.left_click(release=False)
    sleep(2)
    m.move(100, 100)
    sleep(2)
    m.release()