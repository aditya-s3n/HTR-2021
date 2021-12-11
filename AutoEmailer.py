import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def emailApplicant(receiverEmail, applicantName):
    subject = "Accepted applicant"
    #insert variable to identify applicant #
    body = applicantName + " we would like to inform you that you have been accepted for an interview."
    sender_email = "theannoyedalt@gmail.com"
    receiver_email = receiverEmail
    password = "1486jasmine"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "EmailContents.txt"  # In same directory as script
    with open(filename, "w") as file:
        file.write(body)
        
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encodes file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Adds attachment to message and converts message to string
    message.attach(part)
    text = message.as_string()

    # Logs in and sends mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    #wipes doc when done
    with open("EmailContent.txt", "w") as file:
        file.write("0")