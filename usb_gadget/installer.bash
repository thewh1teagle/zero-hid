#!/bin/bash

check_root() {
    ROOTUID="0"
    if [ "$(id -u)" -ne "$ROOTUID" ] ; then
        echo "This script must be executed with root privileges."
        exit 1
    fi
}


ask_reboot() {
    while true; do
        read -p "Do you want to reboot? (Y/n) " yn </dev/tty
        case $yn in
            [Yy]* ) /sbin/reboot; break;;
            [Nn]* ) exit 0;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}


install() {
    echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt # upstream driver which can do the OTG host/gadget flip dictated by OTG_SENSE.
    echo "dwc2" | sudo tee -a /etc/modules # loat at boot
    echo "libcomposite" | sudo tee -a /etc/modules
    cp init_usb_gadget /usr/bin/ # USB gadget configFS
    chmod +x /usr/bin/init_usb_gadget
    sed -i '/^exit 0/i /usr/bin/init_usb_gadget' /etc/rc.local # libcomposite configuration
    /usr/bin/init_usb_gadget 2>/dev/null
}


uninstall () {
    chmod +x ./remove_usb_gadget && ./remove_usb_gadget
    rm -rf /usr/bin/init_usb_gadget
    sed -i '/dtoverlay=dwc2/d' /boot/config.txt
    sed -i '/dwc2/d' /etc/modules
    sed -i '/libcomposite/d' /etc/modules
    sed -i '/init_usb_gadget/d' /etc/rc.local
    ask_reboot
}

check_root
if [ -f "/usr/bin/init_usb_gadget" ]; then
    echo "Looks like usb gadget already instaled"
    read -p "Do you want to uninstall it? (Y/n) " yn </dev/tty
    case $yn in
        [Yy]* )
            uninstall
            echo "Done uninstalling usb gadget. you should reboot now."    
            ask_reboot; break;;
        [Nn]* ) exit 0;;
        * ) echo "Please answer yes or no.";;
    esac
else
    install
    echo "Installed usb gadget, You should reboot now"
    ask_reboot
fi