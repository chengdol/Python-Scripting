#!/usr/bin/python3

# Simple tar program
# tartest1.py

import tarfile
import sys

# If no command line args, archive the current directory
if len(sys.argv) < 2:
    list = ["."]
else:
    list = sys.argv[1:] # Skip the program name argv[0]

# Open a (new) tar archive for uncompressed writing
# tarfile support context manager protocol, can use with-block
with tarfile.open("/tmp/test1.tar", "w") as t:
    for file in list:
        t.add(file)

# No need to call close(), the context manager will do that




