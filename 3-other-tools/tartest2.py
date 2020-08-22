#!/usr/bin/python3

# Simple tar program, plus exception handling
# tartest2.py

import tarfile
import sys

if len(sys.argv) < 2:
    list = ["."]
else:
    list = sys.argv[1:]

with tarfile.open("/tmp/test2.tar", "w") as t:
    for file in list:
        try:
            t.add(file)
        except PermissionError as e:
            print("Sorry we had a problem: %s" % e)



