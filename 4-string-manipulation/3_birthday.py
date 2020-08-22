#!/usr/bin/python3

# Parsing a date from a string (what day were you born on?)

from datetime import datetime

line = input("Enter your date of birth (DD/MM/YYYY): ")
birthday = datetime.strptime(line, "%d/%m/%Y")
print("You were born on a {0:%A}".format(birthday))

