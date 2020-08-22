#!/usr/bin/python3

# Just a logging demo, doesn't do anything useful

import logging
from systemd.journal import JournalHandler

# Logging to a file
# root logger configure
logging.basicConfig(filename="example.log", level=logging.WARN,
                    format="%(levelname)s %(asctime)s %(message)s")

# root logger log
logging.warning("this is a formatted warning")

# Logging to the sytemd journal
jlogger  = logging.getLogger("journal-logger")
jhandler = JournalHandler()
jformatter = logging.Formatter(fmt="%(levelname)s %(message)s")
jhandler.setFormatter(jformatter)
jlogger.addHandler(jhandler)

# This message will propagate to the root logger as well
jlogger.warning("This is a warning sent to the journal")

# Prevent the message propagating to the root logger
jlogger.propagate = False
## journalctl | tail
jlogger.warning("Warning ONLY to journal")

# Within an exception handler you can print a stack trace:
def bad_idea():
    try:
        c = 1 / 0	# Easy way to force an exception
    except:
        logging.error("Failed to divide", exc_info=True)

bad_idea()

