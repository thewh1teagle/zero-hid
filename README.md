
<img width=550 src="https://github.com/thewh1teagle/zero-hid/assets/61390950/13608efd-15c1-4fdd-86b5-e411e15fa638">

HID python library for emulating mouse and keyboard on PI.


## Setup

1. Install apt dependencies

```bash
sudo apt-get update
sudo apt-get install -y git python3-pip
```  


2. install [usb gadget module](https://github.com/thewh1teagle/zero-hid/tree/main/usb_gadget#usb-gadget-module-configuration-for-zero-hid)  
3. Install `zero-hid` with `pip`
```bash
pip3 install zero-hid
```

## Usage
Note: You should connect the data usb port (left one) to the raspberry, and NOT the power port  
  
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
- Easy to setup
- Comprehensive Testing

## Examples
see [examples](examples)

## Tests
| Raspberry Pi Model | Raspbian Version | Kernel Version |
|---------------------|-------------------|----------------|
| Raspberry Pi 4      | Raspbian 12       | 6.1            |
| Raspberry Pi Zero   | Raspbian 5.10     | -              |

## Gotaches

Error when installing with pip
```shell
error: externally-managed-environment
```
See [how-solve-error-externally-managed-environment-when-installing-pip3](https://www.jeffgeerling.com/blog/2023/how-solve-error-externally-managed-environment-when-installing-pip3)

Or simply create virtual environment
```shell
sudo apt-get update
sudo apt install -y python3-venv
python3 -m venv ~/venv
source ~/venv/bin/activate
pip3 install zero-hid
```
