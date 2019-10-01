import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail():
    message = Mail(
        from_email=os.environ['FROM_EMAIL'],
        to_emails=os.environ['TO_EMAIL'],
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code) 
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

send_mail()