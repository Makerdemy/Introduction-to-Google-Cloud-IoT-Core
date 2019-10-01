<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:ea5e0f8723ef5f2a29b67bb297f7db853675d4ca69df78e75bad8b92eb54cac6
size 746
=======
#import Adafruit library and the time library
import Adafruit_DHT as DHT
import time

#Declare the sensor type and the pin of raspberry pi to which sensor is connected to 
sensor = DHT.DHT11
pin = 4

#Use read_retry method to get temperature and humidity values
humidity, temperature = DHT.read_retry(sensor, pin)

#Always printing the temperature and humidity values with exception handling
while True:
    try:
        if temperature is not None and humidity is not None:
            print('Temperature = {0:0.1f}*C and Humidity = {1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get the sensor reading. Please try again!')
        time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
            raise
>>>>>>> 1208bfe06536730cf9b4d3020469041d29f05060
