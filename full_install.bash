#!/bin/bash

clone_repo() {
    echo "Cloning zero-hid..."
    mkdir zero-hid
    curl -L --progress-bar https://github.com/thewh1teagle/zero-hid/tarball/main | tar xz --strip-components=1 -C zero-hid
}

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
    # [ -z "$(find -H /var/lib/apt/lists -maxdepth 0 -mtime -7)" ] && sudo apt-get update # is apt updated last week?
    # [ ! -f /usr/bin/pip3 ] && apt-get install python3-pip -y
    cd /tmp
    rm -rf zero-hid
    clone_repo
    cd /tmp/zero-hid/usb_gadget
    chmod +x install.sh && ./install.sh
    # cd .. && pip3 install .
    dist_packages=$(python3 -c 'import site; print(site.getsitepackages()[0])')
    cd .. && cp -rf "zero_hid" "$dist_packages/"
    cd ~ && rm -rf /tmp/zero_hid

    /usr/bin/init_usb_gadget 2>/dev/null
}


uninstall() {
    cd /tmp
    rm -rf zero-hid
    clone_repo
    pushd "zero-hid/usb_gadget"
    chmod +x ./remove_usb_gadget && ./remove_usb_gadget
    popd
    rm -rf /usr/bin/init_usb_gadget zero_hid

    dist_packages=$(python3 -c 'import site; print(site.getsitepackages()[0])')
    rm -rf "$dist_packages/zero_hid"

    sed -i '/dtoverlay=dwc2/d' /boot/config.txt
    sed -i '/dwc2/d' /etc/modules
    sed -i '/libcomposite/d' /etc/modules
    sed -i '/init_usb_gadget/d' /etc/rc.local


    cd ~ && rm -rf /tmp/zero_hid
}



check_root
if [ -f /usr/bin/init_usb_gadget ]; then
    echo "Looks like zero-hid already installed"
    while true; do
        read -p "Do you want to uninstall it? (Y/n) " yn </dev/tty
        case $yn in
            [Yy]* ) 
                uninstall
                echo "Uninstall done"
                echo "it's recommended to reboot"
                ask_reboot
                break;;
            [Nn]* ) 
                exit 0;;
            * ) 
                echo "Please answer yes or no.";;
        esac
    done
else
    echo "Installing zero-hid..."
    install
    echo "Done install."
    echo "You should reboot now."
    ask_reboot
fi
