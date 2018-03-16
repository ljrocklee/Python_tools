# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

me = "LinuxAppStatusCheck@homecredit.cn"
you = "jack.lee@homecreditcfc.cn"
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open("attachment/testtext.txt", 'rb')
# Create a text/plain message
msg = MIMEText(fp.read().decode('utf-8'))
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % "testtext.txt"
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('10.25.4.4')
s.sendmail(me, you, msg.as_string())
s.quit()