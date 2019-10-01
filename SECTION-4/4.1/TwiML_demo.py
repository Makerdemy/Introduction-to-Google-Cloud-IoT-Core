from twilio.twiml.voice_response import VoiceResponse, Say

response = VoiceResponse()
response.say('Ahoy, world!', voice='alice', language='en-US')

print(response)