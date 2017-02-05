# Author: Bojan G. Kalicanin
# Date: 05-Feb-2017
# Description: Send an e-mail message.

import smtplib
serv = smtplib.SMTP()
serv.connect()

msg = """\
From: dave@dabeaz.com
To: bob@yahoo.com
Subject: Get off my lawn!

Blah blah blah"""

serv.sendemail("dave@dabeaz.com", ['bob@yahoo.com'], msg)
