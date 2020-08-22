#!/usr/bin/python3

# Build page hit histogram from apache access log

import collections

# New dictionary entries default to integer value of zero
hist = collections.defaultdict(int)

for line in open("/home/chris/python-demos/access_log"):
    # Isolate the URL (file name) from the access log entry
    url = line.split()[6].split('?')[0]
    # and count another hit for that page
    hist[url] += 1

# Loop over dictionary entries sorted by value
## sort the records by hit number
for url in sorted(hist, key=hist.get, reverse=True):
    # Stop printing when hit counts fall below zero
    if hist[url] < 50:
        break;
    print ("%-40s : %6d" % (url, hist[url]))




