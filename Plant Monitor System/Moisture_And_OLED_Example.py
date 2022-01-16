import machine
import time
import uasyncio
from machine import I2C
from ads1x15 import ADS1115
from sh1106 import SH1106_I2C
from dht22 import DHT22

# ------------------------------------------------------------------------
# Define/Initialize GPIO Pins

i2c2 = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
dht22 = DHT22(machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP))
btn_show_display = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(25, machine.Pin.OUT)

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

# -----------------------------------ADC Converter

wet = 11140  # Wet Baseline Reading 
dry = 21500  # Dry Baseline Reading 

adc0 = ADS1115(i2c2, 0x48, 1)  # Pins, 1st ADC Address, Gain = 1
# adc1 = ADS1115(i2c2, 0x49, 1)  # Pins, 2nd ADC Address, Gain = 1
# adc2 = ADS1115(i2c2, 0x4A, 1)  # Pins, 3rd ADC Address, Gain = 1 
# adc3 = ADS1115(i2c2, 0x4B, 1)  # Pins, 4th ADC Address, Gain = 1

# -----------------------------------OLED Display

oled_width = 128 # Width of OLED screen
oled_height = 64 # Height of OLED screen

oled = SH1106_I2C(oled_width, oled_height, i2c2)

screen1_row2 = "Pot 2: TEST" 
screen1_row3 = "Pot 3: TEST"
screen1_row4 = "Pot 4: TEST"

# -----------------------------------Date/Time

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
eut = time.time() # Epoch Unix Timestamp
        
if len(str(abs(time.localtime()[4]))) == 1:
    curr_min = ("0" + str(abs(time.localtime()[4])))
else:
    curr_min = str(abs(time.localtime()[4]))
if len(str(abs(time.localtime()[3]))) == 1:
    curr_hr = ("0" + str(abs(time.localtime()[3])))
else:
    curr_hr = str(abs(time.localtime()[3]))
if len(str(abs(time.localtime()[2]))) == 1:
    date_day = ("0" + str(abs(time.localtime()[2])))
else:
    curr_day = str(abs(time.localtime()[2]))
    
    # Result Date/Time
    curr_date = (months[abs(time.localtime()[1])] + "-" + curr_day + "-" + str(abs(time.localtime()[0]) % 100) + " " + curr_hr + ":" + curr_min)
    
# -----------------------------------Temperature & Humidity Sensor

T, H = dht22.read() # Gets Temp & Hum from dht22.py library
temp_f = T * (9/5) + 32.0 # Converts the (T) temperature to Fahrenheit degrees

# -----------------------------------ADC Converter
  
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

# -----------------------------------OLED Display

    # %m.kf Converts a value of type float (or double) to m decimal positions with k digits after the period.
OLED_screen1 = [[0, 8, (curr_date)], [0, 24 , "Temp: %3.0fF" %temp_f], [0, 40, "Humidity: %3.0f%%" %H]]
OLED_screen2 = [[0, 2 , "Pot 1: " + str(adc0_result_A0)], [0, 18, screen1_row2], [0, 34, screen1_row3], [0, 50, screen1_row4]]

# -----------------------------------uasyncio Coroutine

# Coroutine: blink on a timer
async def blink(delay):
    while True:
        led.toggle() # Toggle onboard LED on/off
        await uasyncio.sleep(delay)

# Coroutine: only return on button press
async def wait_button():
    btn_prev = btn_show_display.value()
    while (btn_show_display.value() == 1) or (btn_show_display.value() == btn_prev):
        btn_prev = btn_show_display.value()
        await uasyncio.sleep(0.04)
        
# Coroutine: entry point for asyncio program
async def main():
    
    # Start coroutine as a task and immediately return
    uasyncio.create_task(blink(0.2))
    
# ------------------------------------------------------------------------
# Main Loop

    while True:
        # Calculate time between button presses
        await wait_button()

        for i in range(2):
        # Scroll in, stop, scroll out (vertical)
            scroll_in_screen_v(OLED_screen1)
            time.sleep(5) # Sleep for 5 seconds
            scroll_out_screen_v(2)

            scroll_in_screen_v(OLED_screen2)
            time.sleep(5) # Sleep for 5 seconds
            scroll_out_screen_v(2)

# Start event loop and run entry point coroutine
uasyncio.run(main())












#Attach interrupt to btn_show_display            
# btn_show_display.irq(trigger=machine.Pin.IRQ_RISING, handler=show_display)

# -----------------------------------
   
#   
# # https://www.calculatorsoup.com/calculators/statistics/average.php
#     print(adc0.read())  # Run to get wet/dry variable numbers
#     time.sleep(0.25)



