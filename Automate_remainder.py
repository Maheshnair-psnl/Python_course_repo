import smtplib
from datetime import date

def send_email(receiver_email, subject, message):
    sender_email = 'maheshwork2811@gmail.com' #email id
    password = '*******' #password

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        email_body = f'Subject: {subject}\n\n{message}'

        server.sendmail(sender_email, receiver_email, email_body)
        print('Email sent successfully!')
    except Exception as error:
        print(f'An error occurred while sending the email: {error}')
    finally:
        server.quit()

def automate_reminder():
    today = date.today()
    if today.weekend() == 5:  # email reminder on required date
        receiver_email = 'maheshwork2811@gmail.com'
        subject = 'Reminder: Pending courses'
        message = 'Don\'t forget to complete your pending course by today!'
        send_email(receiver_email, subject, message)

# Run the automation script
automate_reminder()
