#!/bin/sh

ROOTUID="0"
if [ "$(id -u)" -ne "$ROOTUID" ] ; then
    echo "This script must be executed with root privileges."
    exit 1
fi

apt-get update && apt-get install python3-setuptools -y
cd /tmp
curl -L https://github.com/thewh1teagle/zero-hid/tarball/main | tar xz --strip-components=1 -C zero-hid
cd /tmp/zero-hid/usb_gadget
chmod +x install.sh && ./install.sh
cd .. && python3 setup.py install
cd ~ && rm -rf /tmp/zero_hid

echo "Done install."
echo "You should reboot now."
while true; do
    read -p "Do you want to rebooot? (Y/n) " yn
    case $yn in
        [Yy]* ) /sbin/reboot; break;;
        [Nn]* ) exit 0;;
        * ) echo "Please answer yes or no.";;
    esac
done
