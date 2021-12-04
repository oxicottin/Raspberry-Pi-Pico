# import time
from machine import Pin, I2C
from vl53l0x import VL53L0X

# sda = Pin(16)
# scl = Pin(17)
# id = 0
#
sda = Pin(14)
scl = Pin(15)
id = 1
print("setting up i2c", id)

i2c = I2C(id=id, sda=sda, scl=scl)

print(repr(i2c.scan()))
if 0x29 not in i2c.scan():
    print("Failed to find device")
    raise RuntimeError()

# print("creating vl53lox object")
# Create a VL53L0X object
tof = VL53L0X(i2c)

# Pre: 12 to 18 (initialized to 14 by default)
# Final: 8 to 14 (initialized to 10 by default)

# the measuring_timing_budget is a value in ms, the longer the budget, the more accurate the reading.
budget = tof.measurement_timing_budget_us
print("Budget was:", budget)
tof.set_measurement_timing_budget(40000)

# Sets the VCSEL (vertical cavity surface emitting laser) pulse period for the
# given period type (VL53L0X::VcselPeriodPreRange or VL53L0X::VcselPeriodFinalRange) 
# to the given value (in PCLKs). Longer periods increase the potential range of the sensor. 
# Valid values are (even numbers only):

# tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)

# tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

while True:
# Start ranging
    print(tof.ping()-50, "mm")