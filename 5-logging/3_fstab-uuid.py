#!/usr/bin/python3

# Program to replace device names in /etc/fstab

import re
from subprocess import Popen, PIPE

# The first group in this regex matches a partition name
# The second group matches the rest of the line
regex = re.compile(r"(/dev/sd[ab][1-9])(.*)")

outfile = open("fstab.out", mode="w")

for line in open("fstab.in"):
    match = re.search(regex, line)
    if match:
        print("Need to replace %s" % (match.group(1)))  # Debugging only
        # Pass the partition name to lsblk and capture the line of output
        lsblk = Popen(["lsblk", "-n", "--output", "UUID",
                       match.group(1)], stdout=PIPE)
        uuid = lsblk.stdout.readline().decode()
        # Build the replacement line (using the second match group)
        replacement = "UUID=" + uuid[:-1] + re.sub(regex, r"\2", line)
        print("replacement line is %s" % replacement)   # Debugging only
        print(replacement, end='', file=outfile) 
    else:   # Copy the line through unchanged
        print(line, end='', file=outfile)

outfile.close()

        
