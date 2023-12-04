from zero_hid import Mouse
from time import sleep

with Mouse(absolute=True) as m:
    m.move(1000, 1000)
    sleep(0.2)
    m.move(5000, 5000)