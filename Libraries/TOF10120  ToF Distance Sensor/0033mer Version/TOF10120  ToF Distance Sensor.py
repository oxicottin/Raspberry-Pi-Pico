
# TOF Pi Pico code
# Micropython

from machine import Pin, I2C
from time import sleep

i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=100000)

led1 = Pin(18,Pin.OUT)
led2 = Pin(19,Pin.OUT)
led3 = Pin(20,Pin.OUT)
led4 = Pin(21,Pin.OUT)
beeper = Pin(22,Pin.OUT)
       
addr = i2c.scan()[0]
data = bytearray(2)

while True:
    
    i2c.readfrom_mem_into(addr, 0, data)
    distance = data[0] << 8 | data[1]
    print(distance)
    
    if   distance > 200:
        led1(0)
        led2(0)
        led3(0)
        led4(0)
        beeper(0)
    elif distance <= 180 and distance >= 140:
        led1(1)
        led2(0)
        led3(0)
        led4(0)
        beeper(0)
    elif distance <= 139 and distance >= 100:
        led1(1)
        led2(1)
        led3(0)
        led4(0)
        beeper(0)
    elif distance <= 99 and distance >= 60:
        led1(1)
        led2(1)
        led3(1)
        led4(0)
        beeper(0)
    elif distance <= 59 and distance >= 30:
        led1(1)
        led2(1)
        led3(1)
        led4(1)
        beeper(0)
    elif distance < 15:
        led1(1)
        led2(1)
        led3(1)
        led4(1)
        beeper(1)  
    sleep(.1)

    