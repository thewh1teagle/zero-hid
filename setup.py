from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()
# with open('requirements.txt', 'r') as f:
#     requirements = f.read().splitlines()
setup(
    name="zero-hid",  # How you named your package folder
    packages=['zero_hid', 'zero_hid.hid'],  # Chose the same as "name"
    include_package_data=True,
    version="v0.1.6",  # Start with a small number and increase it with every change you make
    license="LGPL",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Library for emulate mouse and keyboard on raspberry pi zero",  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="thewh1teagle",  # Type in your name
    author_email="example@gmail.com",  # Type in your E-Mail
    url="https://github.com/thewh1teagle/zero_hid",  # Provide either the link to your github or to your website
    download_url="",
    keywords=[
        "rpi",
        "raspberry",
        "hid",
    ],  # Keywords that define your package best
    # install_requires=requirements,  # I get to this in a second
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    
)
print("********************* NOTE *********************")
print("To make this library work, you MUST enable usb gadget module in your raspberry pi")
print("Please refer to https://github.com/thewh1teagle/zero-hid#setup---tested-on-raspbian-lite-510")
