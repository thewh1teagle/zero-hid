
<img width=550 src="https://github.com/thewh1teagle/zero-hid/assets/61390950/13608efd-15c1-4fdd-86b5-e411e15fa638">

HID python library for emulating mouse and keyboard on PI.


## Setup

1. Install apt dependencies

```console
sudo apt-get update
sudo apt-get install -y git python3-pip python3-venv
```  

2. install [usb gadget module](https://github.com/thewh1teagle/zero-hid/tree/main/usb_gadget#usb-gadget-module-configuration-for-zero-hid)

3. Create virtual environment

```console
python3 -m venv ~/venv
source ~/venv/bin/activate
```

4. Install `zero-hid` with `pip`
```console
pip3 install zero-hid
```
5. Reboot *if not already!*

## Usage
Note: You should connect the data usb port (left one) to the raspberry, and **NOT** the power port  
  
- Control mouse
```python
from zero_hid import Mouse
m = Mouse()
for i in range(5):
    m.move(10, 10)
```
- Control keyboard
```python
from zero_hid import Keyboard

k = Keyboard()
k.type('Hello world!')
```

## Features
- Relative / Absolute mouse movements
- Left / Right / Middle click
- Scrolling
- Typing
- Hot keys
- Drag and Drop
- LEDs status
- Easy to setup
- Comprehensive Testing

## Examples
see [examples](examples)

## Tests

| Raspberry Pi Model | Raspbian Version      | Kernel Version | Date of Testing |
|--------------------|-----------------------|----------------|-----------------|
| Raspberry Pi 4     | Raspbian 12 (bookworm)| 6.6.31         | 04/08/2024      |
| Raspberry Pi 4     | Raspbian 12           | 6.1            | 01/01/2023      |
| Raspberry Pi Zero  | Raspbian 5.10         | -              | 01/01/2023      |

## Gotachas

---
Absolute mouse used only for positining. use relative mouse for clicking etc. see examples.