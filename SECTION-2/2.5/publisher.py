<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:da710da6e3fcb5b0bffc44984fac0d973bb84690c081905202be1a9ac9948754
size 1888
=======
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

# Execute this loop forever until terminated by the user or
# the raspberry pi fails
while True:
    try:
        # Read the humidity and temperature values using the sensor and pass
        # them to current_humidity & current_temperature
        current_humidity, current_temperature = DHT.read_retry(sensor, pin)

        # If there is no change in temperature as well as humidity, ignore
        # sending the payload & wait for 1 second
        if current_temperature == temperature and \
                current_temperature == humidity:
            time.sleep(1)
            continue

        # Pass the read values into their corresponding variables
        temperature = current_temperature
        humidity = current_humidity

        # Define the structure of payload
        payload = '{{ "data":"PayloadData", "Timestamp":{}, \
"Temperature":{:3.2f}, \
"Humidity":{:3.2f} }}'.format(int(time.time()), temperature, humidity)

        # Publish the payload to the cloud
        publisher.publish(topic_path, data=payload.encode('utf-8'))

        print("Publishing the payload : " + payload)

        # Wait for 3 seconds before executing the loop again
        time.sleep(3)

    # In case of keyboard interruption or system crash, raise these exceptions
    except (KeyboardInterrupt, SystemExit):
        raise
>>>>>>> 1208bfe06536730cf9b4d3020469041d29f05060
