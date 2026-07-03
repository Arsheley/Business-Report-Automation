import smtplib
from email.message import EmailMessage


def send_email(sender_email,
               app_password,
               receiver_email):

    message = EmailMessage()

    message["Subject"] = "Business Sales Report"
    message["From"] = sender_email
    message["To"] = receiver_email

    message.set_content(
        "Hello,\n\n"
        "Please find the attached Business Sales Report.\n\n"
        "This email was generated automatically using Python.\n"
    )

    with open("Business_Report.pdf", "rb") as pdf:

        message.add_attachment(
            pdf.read(),
            maintype="application",
            subtype="pdf",
            filename="Business_Report.pdf"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(sender_email, app_password)

        smtp.send_message(message)

    print("Email sent successfully!")