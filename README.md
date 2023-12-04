<img src="https://user-images.githubusercontent.com/61390950/141596451-c3f69064-7152-4d07-80b0-141b60265c02.png" style="width: 500px; height: 300px; border-radius: 100px">

HID python library for emulating mouse and keyboard on PI.


## Setup

1. Install apt dependencies

```bash
sudo apt-get update
sudo apt-get install -y git python3-full
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

Or simply execute
```shell
sudo rm -rf /usr/lib/python3.11/EXTERNALLY-MANAGED
```
