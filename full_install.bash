#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit 1
fi

apt-get update && apt-get upgrade -y
apt-get install git python3-pip
cd /tmp
git clone https://github.com/thewh1teagle/zero-hid.git
cd /tmp/zero-hid/usb_gadget
chmod +x install.sh && ./install.sh
cd .. && pip3 install .
cd ~ && rm -rf /tmp/zero_hid

echo "Done install."
echo "You should reboot now."
read -p "Do you want to reboot? (y/n)" -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    /sbin/reboot
fi
