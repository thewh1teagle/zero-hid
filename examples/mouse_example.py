from zero_hid import Mouse

with Mouse() as m:
    for i in range(5):
        m.move_relative(5,5)