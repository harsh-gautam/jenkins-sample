#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header    import Header

smtp_host = 'smtp.yandex.com'
login, password = ("********@yandex.com", "********")
recipients_emails = ["hgautam208@gmail.com"]

msg = MIMEText('Message', 'plain', 'utf-8')
msg['Subject'] = Header('Subject', 'utf-8')
msg['From'] = login
msg['To'] = ", ".join(recipients_emails)

s = smtplib.SMTP(smtp_host, 587, timeout=10)
s.set_debuglevel(1)
try:
    s.starttls()
    s.login(login, password)
    s.sendmail(msg['From'], recipients_emails, msg.as_string())
finally:
    s.quit()
