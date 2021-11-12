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
    apt-get update && apt-get install python3-pip -y
    cd /tmp
    rm -rf /tmp/zero-hid
    mkdir /tmp/zero-hid
    curl -L https://github.com/thewh1teagle/zero-hid/tarball/main | tar xz --strip-components=1 -C zero-hid
    cd /tmp/zero-hid/usb_gadget
    chmod +x install.sh && ./install.sh
    cd .. && pip3 install .
    cd ~ && rm -rf /tmp/zero_hid

    /usr/bin/init-usb-gadget 2>/dev/null

    echo "Done install."
    echo "You should reboot now."
}


uninstall() {
    mkdir zero_hid
    curl -L https://github.com/thewh1teagle/zero-hid/tarball/main | tar xz --strip-components=1 -C zero-hid
    pushd "zero_hid/usb_gadget"
    chmod +x ./remove-usb-gadget && ./remove-usb-gadget
    popd
    rm -rf /usr/bin/init-usb-gadget zero_hid

    sed -i '/dtoverlay=dwc2/d' /boot/config.txt
    sed -i '/dwc2/d' /etc/modules
    sed -i '/libcomposite/d' /etc/modules
    sed -i '/init-usb-gadget/d' /etc/rc.local

    echo "Uninstall done"
    echo "it's recommended to reboot"
    
}



check_root
if [ -f /usr/bin/init-usb-gadget ]; then
    echo "Looks like zero-hid already installed"
    while true; do
        read -p "Do you want to uninstall it? (Y/n) " yn </dev/tty
        case $yn in
            [Yy]* ) uninstall && ask_reboot; break;;
            [Nn]* ) exit 0;;
            * ) echo "Please answer yes or no.";;
        esac
    done
else
    echo "Installing zero-hid..."
    install && echo "Installed."
    ask_reboot
fi
