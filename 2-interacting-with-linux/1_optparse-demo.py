#!/usr/bin/python3

# optparse demo -- option parsing for our "df" wrapper

from optparse import OptionParser

## create the parser
parser = OptionParser()
parser.add_option("-t", "--threshold",
                  dest="threshold",
                  type="int",
                  default=90,
                  help="Set threshold (%)")

parser.add_option("-s", "--single",
                  action="store_true",
                  dest="singleshot",
                  default=False,
                  help="just check once, don't loop")

parser.add_option("-m", "--mailbox",
                  dest="mailbox",
                  help="mail report to this mailbox")

# For now, just print out our options and arguments
## options is a class object with attribte 'dest' above
## args is non-option argvs
(options, args) = parser.parse_args()

print("singleshot is %r" % options.singleshot)
print("mailbox is %s" % options.mailbox)
print("threshold is %d" % options.threshold)
print("non-option argument list is %s" % str(args))

## test
## ./1_optparse-demo.py --help
## ./1_optparse-demo.py -h
## ./1_optparse-demo.py -s
## ./1_optparse-demo.py -t 75 -m example.com
