FROM debian:latest

RUN dpkg --add-architecture armhf
RUN apt-get update
RUN apt-get install -y git build-essential \
    g++-arm-linux-gnueabihf libncurses-dev \
    lib32z1 lib32stdc++6 lib32z1 lib32z1-dev flex bison

WORKDIR /kernel
COPY kernel.sh /kernel
# ENTRYPOINT ["/bin/sh", "-c" , "/kernel/build.sh || /bin/bash"]