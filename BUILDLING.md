# Building

To build execute the following
```console
python3 -m venv venv
source venv/bin/activate
pip3 install -e .
```

To test execute the following

```console
pip3 install pytest
pytest tests/
```

To get kernel version and OS info

```console
cat /etc/os-release
uname -a
```