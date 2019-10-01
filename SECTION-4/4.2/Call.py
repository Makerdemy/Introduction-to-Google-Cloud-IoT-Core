# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

def place_call():
    # Your Account Sid and Auth Token from twilio.com/console

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    client.calls.create(
                            url = '<Use your TwiML Bin URL>', 
                            to = os.environ['TWILIO_TO'],
                            from_ = os.environ['TWILIO_FROM']
                        )

place_call()
