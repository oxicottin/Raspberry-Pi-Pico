# VCNL4010 Proximity/Light sensor

![466-02](https://user-images.githubusercontent.com/34151610/144733273-9b4982b6-24f1-4870-81c8-06c1938a60ae.jpg)

## Purchase:
https://www.adafruit.com/product/466
https://www.arrow.com/en/products/466/adafruit-industries

## Description
The VCNL4010 sensor is a nice way to add a small-distance proximity sensor to your microcontroller project. For longer distances (in the range of cm, you can use a SHARP IR distance sensor, but those are only good if the object is over 10 cm away. The VCNL4010 is designed for much shorter distances, no more than 200mm (about 7.5") and under our experimentation we found it worked best at distances of about 10-150mm. It would be good for say detecting when a hand moved nearby, or before a robot smacks into a wall. The sensor also has an ambient light sensor built in.

This sensor is easy to use with any microcontroller that has i2c capability. It is 5 volt compliant so you can use it with 3.3V or 5V logic with no risk of damage. There is an onboard 3.3V ultra low dropout regulator so you can power it with 3.3 to 5.0V. However, if you can give it 5.0V that is ideal since the VIN voltage powers the IR LED and the higher the voltage you can give it, the more powerful it is.
