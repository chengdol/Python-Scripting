#!/usr/bin/python3

# Demonstrate piping into and out of a child process

## this example will not get deadlock because 'sort' will execute after
## it get all the number input. But other linux command may hang because of
## the pipeline get fulled 

from subprocess import Popen, PIPE
import random

## subporcess.PIPE, capture stdin and stdout
sorter = Popen(["sort", "-nr"], stdin=PIPE, stdout=PIPE)

# Write 10 random integers to the sorter's input
for i in range(10):
    sorter.stdin.write(("%d\n" % random.randrange(100)).encode())
    
# Without the close() below, this will hang because
# the sorter will never see EOF on its standard input
sorter.stdin.close()

# Read and print the output from sort
for line in sorter.stdout:
    print(line.decode(), end='')
