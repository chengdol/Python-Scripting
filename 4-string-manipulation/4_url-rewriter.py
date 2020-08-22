#!/usr/bin/python3

# This example is about re-writing URLs. It assumes we are moving a series
# of web sites from the domain oldplace.com to the domain newplace.org and
# need to update a document containing a list of URLs.

import re

# This is the string containing the URLs we want to process.
# In reality we would more likely read this from a file.

urls = \
'''The report is <a href = https://docs.oldplace.com/chris/report> here </a>
Access your mailbox <a href = http://mail.oldplace.com/mailbox?id=5432"> here </a>
The full events list is at http://events.oldplace.com/index.html'''

regex = r"(https?)://(\w+)\.oldplace\.com/(\S+)"
newurls = re.sub(regex, r"\1://\2.newplace.org/\3", urls)
print(re.findall(regex, urls))   #  Debug only
print(newurls)
