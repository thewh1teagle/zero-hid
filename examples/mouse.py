from zero_hid import Mouse

with Mouse() as m:
    for i in range(5):
        m.move(5,5)