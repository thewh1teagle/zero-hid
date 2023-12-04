from zero_hid import Mouse

m = Mouse()
for i in range(5):
    m.move(5,5)
m.close()