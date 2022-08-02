import smtplib
import ssl


port = 465
smtp_server = "smtp.gmail.com"
sender = "aleksandra.matacz93@gmail.com"
receiver = "a.matacz@o2.pl"
password = "vteocpsfszrydrgr"

msg = """\
Subject: Test email

Pierwszy email.
"""
ssl_connection = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=ssl_connection) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg)
