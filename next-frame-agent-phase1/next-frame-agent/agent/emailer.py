import os, smtplib, ssl
from email.message import EmailMessage

def send_email(subject: str, body: str) -> None:
    """Send a plain email through Gmail using an app password (free)."""
    addr = os.environ["EMAIL_ADDRESS"]
    pwd = os.environ["EMAIL_APP_PASSWORD"]
    msg = EmailMessage()
    msg["From"] = addr
    msg["To"] = addr
    msg["Subject"] = subject
    msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as s:
        s.login(addr, pwd)
        s.send_message(msg)
