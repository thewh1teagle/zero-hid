from zero_hid import Mouse



m = Mouse()
for i in range(5):
    m.move_relative(5,5)
m.close()