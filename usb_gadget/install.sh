#!/bin/bash

echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt # upstream driver which can do the OTG host/gadget flip dictated by OTG_SENSE.
echo "dwc2" | sudo tee -a /etc/modules # loat at boot
echo "libcomposite" | sudo tee -a /etc/modules
cp init-usb-gadget /usr/bin/ # USB gadget configFS
chmod +x /usr/bin/init-usb-gadget
sed '/^exit 0/i /usr/bin/init-usb-gadget' /etc/rc.local # libcomposite configuration