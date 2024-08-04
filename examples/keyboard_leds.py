from zero_hid import Keyboard

with Keyboard() as k:
    print('Press CapsLock / NumLock / ScrLock')
    while True:
        leds = k.blocking_read_led_state()
        print(leds)