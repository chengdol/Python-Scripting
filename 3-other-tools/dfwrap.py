#!/usr/bin/env python3
# dfwrap.py
# running an external command from Python
# stdout is captured and looped over line by line
# proc.out is a BufferedReader and we can loop over
# the lines as we would for an open file

import subprocess

threshold = 80    # default threshold (%)
partition = "/"   # default partition

proc = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
for line in proc.stdout:
    # split into space-separated fields
    splitline = line.decode().split()
    # The %full figure is in field 4, the mount point in field 5
    print(splitline[1] + " and " + splitline[5])
    if splitline[5] == partition:
        # this is the partition we want to check
        print("partition " + partition + " is " + splitline[4][:-1])
        if int(splitline[4][:-1]) > threshold:
            print("WARNING!")
            

   
