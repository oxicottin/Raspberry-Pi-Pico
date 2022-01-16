import machine, time
from machine import I2C
from ads1x15 import ADS1115

i2c2 = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

wet = 11140  # Wet Baseline Reading 
dry = 21827  # Dry Baseline Reading 

adc0 = ADS1115(i2c2, 0x48, 1)  # Pins, 1st ADC Address, Gain = 1
# adc1 = ADS1115(i2c2, 0x49, 1)  # Pins, 2nd ADC Address, Gain = 1
# adc2 = ADS1115(i2c2, 0x4A, 1)  # Pins, 3rd ADC Address, Gain = 1 
# adc3 = ADS1115(i2c2, 0x4B, 1)  # Pins, 4th ADC Address, Gain = 1

# First Analog-to-Digital ADC PGA Converter ADS1115--------------
#     adc0_result_A0 = percentage_value(adc0.read(0, 0), dry, wet, dry)
#     adc0_result_A1 = percentage_value(adc0.read(0, 1), dry, wet, dry)
#     adc0_result_A2 = percentage_value(adc0.read(0, 2), dry, wet, dry)
#     adc0_result_A3 = percentage_value(adc0.read(0, 3), dry, wet, dry)
# 
# Second Analog-to-Digital ADC PGA Converter ADS1115-------------
#     adc1_result_A0 = percentage_value(adc1.read(0, 0), dry, wet, dry)
#     adc1_result_A1 = percentage_value(adc1.read(0, 1), dry, wet, dry)
#     adc1_result_A2 = percentage_value(adc1.read(0, 2), dry, wet, dry)
#     adc1_result_A3 = percentage_value(adc1.read(0, 3), dry, wet, dry)


for i in range (100):
# https://www.calculatorsoup.com/calculators/statistics/average.php
    print(adc0.read())  # Run to get wet/dry variable numbers
    time.sleep(0.25)