import smtplib
from email.mime.text import MIMEText

subject = "Spotify Update"
body = "This is the body of the text message"
sender = "charlie.oestreicher@gmail.com"
recipients = ["charles.oestreicher@duke.edu"]
password = "ynzxdyiuxgzaxffe"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


# send_email(subject, body, sender, recipients, password)
