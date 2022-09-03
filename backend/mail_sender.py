import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pricetracker.pricetracker.settings


def send_email(url, SERVICE, diff, NAME):
    port = 465
    smtp_server = "smtp.gmail.com"

    sender = settings.EMAIL_HOST
    password = pricetracker.settings.EMAIL_PASSWORD

    receiver = "a.matacz@o2.pl"

    subject = "[NIE PRZEGAP] Obserwowany przez Ciebie produkt jest teraz w niższej cenie!"
    email_text = f"""
    Cześć,<br>
    {NAME} jest tańszy o {diff} złotych!<br>
    Sprawdź akutalną ofertę na {SERVICE}! <br><br> 
    <a href={url}>Link do oferty</a>""".format(NAME=NAME, diff=diff, SERVICE=SERVICE, url=url)

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
