#!/usr/bin/bash

cmd="/kernel/kernel.sh || /bin/bash"
docker run --rm -it build /bin/bash -c "$cmd"