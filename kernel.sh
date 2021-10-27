#!/bin/bash

git clone --branch rpi-5.10.y --single-branch --depth 1 https://github.com/raspberrypi/linux
cd linux
KERNEL=kernel
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcmrpi_defconfig
# For Pi 2, Pi 3, Pi 3+, or Compute Module 3:
# KERNEL=kernel7
# make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2709_defconfig
make ARCH=arm menuconfig
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs


mkdir ../modules
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=../modules modules_install
mv arch/arm/boot/zImage arch/arm/boot/kernel.img