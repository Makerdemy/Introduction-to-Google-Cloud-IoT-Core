import base64
import json
from google.cloud import iot_v1
import os
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

count = 0


def send_SMS():
    # Your Account SID from twilio.com/console
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # Your Auth Token from twilio.com/console
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=os.environ['TWILIO_TO'],
        from_=os.environ['TWILIO_FROM'],
        body="Hello! The temperature has crossed the threshold limit")


def place_call():
    # Your Account Sid and Auth Token from twilio.com/console

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    client.calls.create(
        # Use your TwiML Bin URL
        url=os.environ['TWILIO_URL'],
        to=os.environ['TWILIO_TO'],
        from_=os.environ['TWILIO_FROM']
    )


def send_mail():
    message = Mail(
        from_email=os.environ['FROM_EMAIL'],
        to_emails=os.environ['TO_EMAIL'],
        subject='Temperature Alert!',
        html_content='<strong>I am sorry to say this, but the temperature has crossed its limit</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code) 
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


def device_config(config):
    client = iot_v1.DeviceManagerClient()
    name = client.device_path(os.environ['PROJECT_ID'],
                              os.environ['REGION'],  os.environ['REGISTRY'],
                              os.environ['DEVICE'])
    binary_data = bytes(config, 'utf-8')
    client.modify_cloud_to_device_config(name, binary_data)


def Notification(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.
    """

    print("""This Function was triggered by messageId {} \
    published at {}""".format(
        context.event_id, context.timestamp))

    if 'data' in event:
        global count
        data = event['data']
        data = base64.b64decode(data)
        data = data.decode('utf-8')
        data = json.loads(data)

        temperature = float(data['Temperature'])

        if temperature > 24.0:
            # Turning LED of ESP32 ON and displaying "Limit Crossed" text on 16*2 LCD
            device_config("ledon")
            # Now send SMS as the threshold limit is crossed
            send_SMS()
            if count < 1:
                # This is the first time temperature has exceeded beyond the threshold
                place_call()
                send_mail()
                count = count+1
        else:
            # Turning LED of ESP32 OFF and displaying "Safe limit" text on LCD
            device_config("ledoff")

    else:
        # This block gets executed when telemetry is not sent
        print("Data is not present!")
