# VL53L0xV2 Time of Flight for MicroPython

![Capture](https://user-images.githubusercontent.com/34151610/144732354-e2a8dc49-3b44-40a9-8efb-bd95bab4da57.JPG)

## AMAZON LINK:
https://www.amazon.com/dp/B07XXTMRR2?psc=1&ref=ppx_yo2_dt_b_product_details

## PRODUCT INFO

This library will help you get up and running with the cheap VL53L0X Time of Flight Sensor, in MicroPython, specifically the Raspberry Pi Pico verison.

This code is heavily based on the code by uceeatz: <https://github.com/uceeatz> with just some tweaks to make it work with the limitations of the Raspberry Pi Pico version of MicroPython.

Things to know - in my testing the sensors was out by about 50mm, so I've just minused that from the result.

I've simplified the reading of results from the sensor, just use:

``` python
distance = tof.ping()
```
to return values in millimeters.

The tof_test demo will continuously print out readings from the sensor, but be sure to replace the pin numbers with those you have used, along with the I2C bus number.

---

Happy Laser-based Measuring!

Kevin McAleer, 
March 2021

## Connecting the Pico

This should be connected to one of the I2C busses. If the board you are using comes with an XSHUT pin,
this should be connected (or pulled up) to the positive rail.
