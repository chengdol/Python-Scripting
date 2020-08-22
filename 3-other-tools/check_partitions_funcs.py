## no shebang here, will not run this script as stand alone code
# Supporting functions for df wrapper

import subprocess
import smtplib
from email.mime.text import MIMEText

def report_via_email(message, recipient):
    msg = MIMEText(message)
    msg["Subject"] = "Low Disk Space Warning"
    msg["From"] = "fred@thatplace.com"
    msg["To"] = recipient
    with smtplib.SMTP("smtp.somewhere.com") as t:
        ## fake credentials
        t.login("henryhiggins", "A5=jf57%4")
        t.sendmail("fred@thatplace.com", recipient, msg.as_string())

def report_via_stdout(message):
    print(message)

def check_once(options, partition_list):
    # Run df and collect the output
    proc = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    for line in proc.stdout:
        # split into space-separated fields
        splitline = line.decode().split()
        # The %full figure is in field 4, the mount point in field 5
        for partition in partition_list:
            if splitline[5] == partition:
                # this is a partition we want to check
                percent = int(splitline[4][:-1]) # Slice off trailing "%"
                if percent > options.threshold:
                    message = "WARNING: partition %s is %d%% full" % (partition, percent)
                    # Report message to email address if we have one,
                    # else to stdout
                    if options.mailbox:
                        try:
                            report_via_email(message, options.mailbox)
                        except Exception as e:
                            print(e)
                    else:
                        report_via_stdout(message)
