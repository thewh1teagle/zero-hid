# usb gadget module configuration for [zero-hid](https://github.com/thewh1teagle/zero-hid)

To be able to use `zero-hid` package
it's necessary to change some configuration on the kernel.

### Install / remove the module
clone the repo if you haven't yet
```bash
git clone https://github.com/thewh1teagle/zero-hid
```

get into usb_gadget folder
```bash
cd zero-hid/usb_gadget
```
give the installer permission and execute `installer.bash`
```bash
chmod +x installer.bash && sudo ./installer.bash
```
