#Import smtplib for the actual sending function
import smtplib
import base64

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile = "test.txt"
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
me = "w079064@163.com"
you = "819008930@qq.com"
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
username = "w079064@163.com"
password = "wys08257307qaz"
s = smtplib.SMTP('smtp.163.com')
s.login(username, password)
s.sendmail(me, [you], msg.as_string())
s.quit()

