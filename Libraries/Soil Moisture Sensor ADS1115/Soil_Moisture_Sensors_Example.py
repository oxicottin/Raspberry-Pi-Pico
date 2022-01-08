# 8 Capacitive Soil Moisture Sensors

import machine
from machine import I2C
from ads1x15 import ADS1115
import utime

# ------------------------------------------------------------------------
# Define GPIO Pins

i2c2 = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

# ------------------------------------------------------------------------
"""
# Scan i2c-Bus for connected devices

print('Scanning i2c bus')
devices = i2c2.scan()

if len(devices) == 0:
 print("No i2c device !")
else:
 print('i2c devices found:',len(devices))
 
for device in devices:
 print("Decimal address: ",device," | Hexa address: ",hex(device))
"""
# ------------------------------------------------------------------------
# Define Variables

adc0 = ADS1115(i2c2, 0x48, 1)  # Gain = 1 
adc1 = ADS1115(i2c2, 0x49, 1)  # Gain = 1
# adc2 = ADS1115(i2c2, 0x4A, 1)  # Gain = 1 
# adc3 = ADS1115(i2c2, 0x4B, 1)  # Gain = 1 

wet = 11140  # Reading when sensor is wet
dry = 21844  # Reading when sensor is dry

# ------------------------------------------------------------------------
#  Define Functions

# Calculate the percentage between the wet/dry values
def percentage_value(value, in_min, out_max, out_min):
        percentage_value = (value - in_min) / (out_max - out_min) * 100
        return (str(round(percentage_value))) + "%"
    
# ------------------------------------------------------------------------
while True:   
    """
# https://www.calculatorsoup.com/calculators/statistics/average.php
    print(adc0.read())  # Run to get wet/dry variable numbers
    utime.sleep(0.25)
    """
    
    adc0_result_A0 = percentage_value(adc0.read(0, 0), dry, wet, dry)
#     adc0_result_A0 = percentage_value(adc0.read(0, 0), dry, wet, dry)
#     adc0_result_A1 = percentage_value(adc0.read(0, 1), dry, wet, dry)
#     adc0_result_A2 = percentage_value(adc0.read(0, 2), dry, wet, dry)
#     adc0_result_A3 = percentage_value(adc0.read(0, 3), dry, wet, dry)
#     
#     adc1_result_A0 = percentage_value(adc1.read(0, 0), dry, wet, dry)
#     adc1_result_A1 = percentage_value(adc1.read(0, 1), dry, wet, dry)
#     adc1_result_A2 = percentage_value(adc1.read(0, 2), dry, wet, dry)
#     adc1_result_A3 = percentage_value(adc1.read(0, 3), dry, wet, dry)
 
 
    print("adc0:",adc0_result_A0)
    utime.sleep(0.25)


