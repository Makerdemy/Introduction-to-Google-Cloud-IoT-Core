# Import necessary Modules
import os
from google.cloud import pubsub_v1
import Adafruit_DHT as DHT
import time

# Create an object for publishing
publisher = pubsub_v1.PublisherClient()

# Define topic path
topic_path = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('PROJECT_ID'), topic=os.getenv('TOPIC_NAME'))

# Initialise sensor type and pin number in BCM model
sensor = DHT.DHT11
pin = 4

# Initialise temperature and humidity values with 0.0
temperature = 0.0
humidity = 0.0

# Execute this loop for 30 minutes, until terminated by the user or
# the raspberry pi fails
for _ in range(30):
    try:
        # Read the humidity and temperature values using the sensor and pass
        # them to current_humidity & current_temperature
        humidity, temperature = DHT.read_retry(sensor, pin)

        # Define the structure of payload
        payload = '{{ "data":"PayloadData", "Timestamp":{}, \
"Temperature":{:3.2f}, \
"Humidity":{:3.2f} }}'.format(int(time.time()), temperature, humidity)

        # Publish the payload to the cloud
        publisher.publish(topic_path, data=payload.encode('utf-8'))

        print("Publishing the payload : " + payload)

        # Wait for 60 seconds before executing the loop again
        time.sleep(60)

    # In case of keyboard interruption or system crash, raise these exceptions
    except (KeyboardInterrupt, SystemExit):
        raise
