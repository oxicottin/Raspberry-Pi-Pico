import machine
from dht22 import DHT22
import utime
import time

dht22 = DHT22(machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP))

# -----------------------------------Temperature & Humidity Sensor
T, H = dht22.read() # Gets Temp & Hum from dht22.py library
temp_f = T * (9/5) + 32.0 # Converts the (T) temperature to Fahrenheit degrees
# ------------------------------------------------------------------------
#  Let's Do Stuff

while True:
    
    print('Temperature: %3.1f C' %T)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %H + "\n")
    utime.sleep(5) # Wait 5 seconds