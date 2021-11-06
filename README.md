<img src="https://user-images.githubusercontent.com/61390950/140584361-70f33e1e-9b87-4901-9f34-1a4a2fd876fc.png" style="width: 550px; height: 300px; border-radius: 100px">

HID library for emulate mouse and keyboard on PI zero.

## Setup - Tested on [Raspbian](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit) lite 5.10
#### Single command installation
```bash
sudo sh -c "$(curl -Ss https://raw.githubusercontent.com/thewh1teagle/zero-hid/main/full_install.bash)
```

#### Manual installation
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

## Usage
```python
from zero_hid import Mouse
m = Mouse()
for i in range(5):
    m.move_relative(10, 10)
```
