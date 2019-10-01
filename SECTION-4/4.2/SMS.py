from twilio.rest import Client
import os

def send_SMS():
    # Your Account SID from twilio.com/console
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # Your Auth Token from twilio.com/console
    auth_token  = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=os.environ['TWILIO_TO'], 
        from_=os.environ['TWILIO_FROM'],
        body="Hello! This is Twilio, ready to assist you in enabling notifications")

    print(message.sid)

send_SMS()
