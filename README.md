<img src="https://user-images.githubusercontent.com/61390950/141596451-c3f69064-7152-4d07-80b0-141b60265c02.png" style="width: 500px; height: 300px; border-radius: 100px">


HID library for emulate mouse and keyboard on PI zero.

## Setup - Tested on [Raspbian](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit) lite 5.10
#### Single command installation
```bash
curl -LSs "https://git.io/JXpdg" | sudo bash
```

<details>
  <summary>Manual installation</summary>
  
install packages
```bash
sudo apt-get update && sudo apt-get install git python3-pip -y
```
clone the repo and install usb gadget module
```bash
git clone https://github.com/thewh1teagle/zero-hid
cd zero_hid/usb_gadget
chmod +x install.sh && sudo ./install.sh
```
install zero_hid to python
```bash
cd zero_hid/
pip3 install .
```

</details>

## Usage
Control mouse
```python
from zero_hid import Mouse
m = Mouse()
for i in range(5):
    m.move_relative(10, 10)
```
Control keyboard
```python
from zero_hid import Keyboard

k = Keyboard()
k.type('Hello world!')
```
