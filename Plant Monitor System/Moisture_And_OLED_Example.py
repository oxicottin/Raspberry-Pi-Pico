import machine
from machine import I2C
from ads1x15 import ADS1115
from sh1106 import SH1106_I2C
import utime

# ------------------------------------------------------------------------
# Define GPIO Pins

i2c2 = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

# ------------------------------------------------------------------------
# Scan i2c-Bus for connected devices
"""
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
#  Define Functions

# Calculate the percentage between the wet/dry values
def percentage_value(value, in_min, out_max, out_min):
        percentage_value = (value - in_min) / (out_max - out_min) * 100
        return (str(round(percentage_value))) + "%"

# Scroll in OLED screen vertically
def scroll_in_screen_v(screen):
  for i in range (0, (oled_height+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)

# Scroll out OLED screen vertically
def scroll_out_screen_v(speed):
  for i in range ((oled_height+1)/speed):
    for j in range (oled_width):
      oled.pixel(j, i, 0)
    oled.scroll(0,speed)
    oled.show()
 
# ------------------------------------------------------------------------
# Define Variables

wet = 11140  # Wet Baseline Reading 
dry = 22000  # Dry Baseline Reading 

adc0 = ADS1115(i2c2, 0x48, 1)  # Pins, 1st ADC Address, Gain = 1
# adc1 = ADS1115(i2c2, 0x49, 1)  # Pins, 2nd ADC Address, Gain = 1
# adc2 = ADS1115(i2c2, 0x4A, 1)  # Pins, 3rd ADC Address, Gain = 1 
# adc3 = ADS1115(i2c2, 0x4B, 1)  # Pins, 4th ADC Address, Gain = 1 

oled_width = 128 # Width of OLED screen
oled_height = 64 # Height of OLED screen

oled = SH1106_I2C(oled_width, oled_height, i2c2)

#screen1_row1 = "Sensor 1: " + str(adc0_result_A0) # "Screen 1, row 1"
screen1_row2 = "Screen 1, row 2" 
screen1_row3 = "Screen 1, row 3"
screen1_row4 = "Screen 1, row 4"

# ------------------------------------------------------------------------
while True:
    """
# https://www.calculatorsoup.com/calculators/statistics/average.php
    print(adc0.read())  # Run to get wet/dry variable numbers
    utime.sleep(0.25)
    """
    
# First Analog-to-Digital ADC PGA Converter ADS1115--------------
    adc0_result_A0 = percentage_value(adc0.read(0, 0), dry, wet, dry)
#     adc0_result_A1 = percentage_value(adc0.read(0, 1), dry, wet, dry)
#     adc0_result_A2 = percentage_value(adc0.read(0, 2), dry, wet, dry)
#     adc0_result_A3 = percentage_value(adc0.read(0, 3), dry, wet, dry)
# 
# Second Analog-to-Digital ADC PGA Converter ADS1115-------------
#     adc1_result_A0 = percentage_value(adc1.read(0, 0), dry, wet, dry)
#     adc1_result_A1 = percentage_value(adc1.read(0, 1), dry, wet, dry)
#     adc1_result_A2 = percentage_value(adc1.read(0, 2), dry, wet, dry)
#     adc1_result_A3 = percentage_value(adc1.read(0, 3), dry, wet, dry)

    screen1 = [[0, 0 , "Sensor 1: " + str(adc0_result_A0)], [0, 16, screen1_row2], [0, 32, screen1_row3], [0, 48, screen1_row4]]
    
# Scroll in, stop, scroll out (vertical)
    scroll_in_screen_v(screen1)
    utime.sleep(5) # Sleep for 5 seconds
    scroll_out_screen_v(2)




