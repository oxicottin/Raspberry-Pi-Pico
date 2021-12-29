# 3 Capacitive Soil Moisture Sensors

from machine import ADC
import utime

##############################################################################
# Define GPIO Pins

adc0 = machine.ADC(machine.Pin(26))
# adc1 = machine.ADC(machine.Pin(27))
# adc2 = machine.ADC(machine.Pin(28))
##############################################################################
# Define Variables

wet = 28882
dry = 56263
##############################################################################
#  Define Functions

def percentage_value(value, in_min, out_max, out_min):
        percentage_value = (value - in_min) / (out_max - out_min) * 100
        return (str(round(percentage_value))) + "%"
##############################################################################
while True:
    
# https://www.calculatorsoup.com/calculators/statistics/average.php
#    print(adc0.read_u16())  # Run to get wet and dry definition numbers

    print(percentage_value(adc0.read_u16(), dry, wet, dry))
    utime.sleep(0.5)

    
