import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

def send_email(subject, body, to_email):
    # Set up the email parameters
    sender_email = 'your_email@gmail.com'  # Your email address
    password = 'your_password'  # Your email password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, to_email, msg.as_string())
    server.quit()

def generate_daily_report():
    # Generate your daily report content here
    report_date = datetime.date.today()
    report_content = f"Daily Report for {report_date}:\n\n1. Item 1\n2. Item 2\n3. Item 3"

    return report_content

def main():
    # Set up email recipients
    recipients = ['recipient1@example.com', 'recipient2@example.com']

    # Generate daily report
    report_subject = 'Daily Report'
    report_body = generate_daily_report()

    # Send email to each recipient
    for recipient in recipients:
        send_email(report_subject, report_body, recipient)

if __name__ == "__main__":
    main()
