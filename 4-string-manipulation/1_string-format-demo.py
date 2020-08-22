#!/usr/bin/python3

# Demonstration of formatted strings

age = 34
name = "Mary"

# Using the % operator and % format codes
print("%s is %d" % (name, age))

# Using the string format() method
print("{0} is {1}".format(name, age))

# If args are printed in order you don't need the 0 and 1
print("{} is {}".format(name, age))

# You can print the arguments in a different order
print("{1} is {0}'s age".format(name, age))

# Example of accessing the attributes of an object
import os
file = "/etc"
info = os.stat(file)
print("file {0} uid {1.st_uid}, size {1.st_size}".format(file, info))

# Example of specifying field width and precision
# Print table of powers of two and their square roots

import math
x = 1
for i in range(10):
    x = x * 2
    y = math.sqrt(x)
    print("{0:4}{1:10}{2:10.3f}".format(i, x, y))
    # print("%4d%10d%10.3f" % (i, x, y))

# Example of building the format string dynamically
# import sys
width1 = 4
width2 = 10
width3 = 10
# Or we might pick up the widths from the command line:
# width1 = int(sys.argv[1])
# width2 = int(sys.argv[2])
# width3 = int(sys.argv[3])

# Build a format string (two curly brackets get you one curly bracket)
formatter = "{{0:{0}}}{{1:{1}}}{{2:{2}.3f}}".format(width1, width2, width3)
print(formatter)	# Debug
print(formatter.format(i, x, y))	# Use the formatter we built

# There is a more direct way:
print("{0:{width1}}{1:{width2}}{2:{width3}.3f}".format(i, x, y,
                                            width1=4,width2=10, width3=10))

# String concatenation
a = "hello"
b = "world"
c = a + " " + b
print(c)

# String multipication
print(3*"Yes! ")

# Simple use of "in" operator:

print("34" in "123456789")
print("43" in "123456789")
print("43" not in "2123456789")
      
# More realilstic example of the "in" operator
for line in open("/etc/passwd"):
    if "chris" in line:
        print(line)

