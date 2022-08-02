import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465
smtp_server = "smtp.gmail.com"
sender = "aleksandra.matacz93@gmail.com"
receiver = "a.matacz@o2.pl"
password = "vteocpsfszrydrgr"
subject = "Test e-mail"
email_text = "<i>EmailEmailEmail</i>"

file = "password.txt"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject

msg.attach(MIMEText(email_text, "html"))

with open(file, "rb") as f:
    attachment = MIMEBase("application", "octet-string")
    attachment.set_payload(f.read())

encoders.encode_base64(attachment)

attachment.add_header(
    "Content-Disposition",
    f"attachment: filename={file}"
)

msg.attach(attachment)
text = msg.as_string()

ssl_connection = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=ssl_connection) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, text)
