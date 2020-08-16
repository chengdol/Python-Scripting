#!/usr/bin/python3

# Program to find prime numbers.
# Intended for demonstrating signals

from time import sleep
from signal import *

def isprime(n):
    sleep(0.1)
    x = 2
    while (x * x ) <= n:
        if not n % x:
            return False
        x += 1
    return True

# SIGHUP turns debug printing on and off
## pkill -HUP 5_signal-primes-v5.py
debug = False   
def sighup_handler(signum, frame):
    global debug    # Otherwise would be assumed local
    debug = not debug

signal(SIGHUP, sighup_handler)

# SIGUSR1 reports current status
## pkill -USR1 5_signal-primes-v5.py
def report_status(signum, frame):
    global primes_list
    print("found %d primes so far" % len(primes_list))

signal(SIGUSR1, report_status)

# Some other signals are ignored
signal(SIGINT, SIG_IGN)
signal(SIGQUIT, SIG_IGN)
signal(SIGTERM, SIG_IGN)

n = 1
primes_list = []

while True:
    if isprime(n):
        if debug:
            print("%d is prime" % n)
        primes_list.append(n)
    n += 1
        
