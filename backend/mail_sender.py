import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(url, SERVICE, diff, NAME):
    port = 465
    smtp_server = "smtp.gmail.com"

    sender = 'amatacz.dev@gmail.com'
    password = 'czhduadjgpbhaxbm'

    receiver = "a.matacz@o2.pl"

    subject = "[NIE PRZEGAP] Obserwowany przez Ciebie produkt jest teraz w niższej cenie!"

    email_text = open('backend/email.html', 'r').read()

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.attach(MIMEText(email_text, "html"))
    text = msg.as_string()
    ssl_connection = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=ssl_connection) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, text)
