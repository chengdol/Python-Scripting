#!/usr/bin/python3

# tartest4.py
# Extract only recently modified files (using tarinfo)

import os
import tarfile
import time

os.chdir("/home/chris/extract-here")

# Compute the time one week ago (seconds since epoch)
mintime = time.time() - (7 * 24 * 3600)

with tarfile.open("/tmp/test3.tar", "r") as t:
    for info in t:
        if info.mtime > mintime and info.isfile():
            print("extracting %s" % info.name)
            t.extract(info)


