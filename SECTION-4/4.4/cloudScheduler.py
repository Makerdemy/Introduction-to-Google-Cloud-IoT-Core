from twilio.rest import Client
import os


def send_SMS():
    # Your Account SID from twilio.com/console
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    # Your Auth Token from twilio.com/console
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=os.environ["TWILIO_TO"],
        from_=os.environ["TWILIO_FROM"],
        body="Hello! I request you all to please do attend the meeting, " +\
        "which is scheduled in an another half-an-hour, at our meeting hall"
    )

    print(message.sid)


def cloudScheduler(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.
    """
    if "data" in event:
        send_SMS()
