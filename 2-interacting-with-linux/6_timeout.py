#!/usr/bin/python3

# Timeout using SIGALRM

import sys
from signal import *

def timeout_handler(signum, frame):
    raise IOError("User not responding")

# Read string from stdin, with timeout
def get_name():
    signal(SIGALRM, timeout_handler)
    ## from signal module
    alarm(5)        # Request SIGALRM in 5 seconds
    n = sys.stdin.readline()
    alarm(0)        # Cancel alarm
    return n

print("enter your name: ", end = '')
sys.stdout.flush()  # Needed because string has no newline
try:
    name = get_name()
except IOError:
    print("You did not reply, I will call you 'Sleepy'")
    name = "Sleepy"

print("hello " + name)
