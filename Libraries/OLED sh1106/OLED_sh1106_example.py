'''
Continuous vertical scroll
If you want to scroll the screen in and out vertically continuously, you
can use the scroll_in_out_screen_v(screen) function.
'''

import machine
from machine import I2C
from sh1106 import SH1106_I2C
import utime
# ------------------------------------------------------------------------
# Define GPIO pins

i2c = I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)
# ------------------------------------------------------------------------

oled_width = 128
oled_height = 64
oled = SH1106_I2C(oled_width, oled_height, i2c)
# ----------------------
screen1_row1 = "Screen 1, row 1"
screen1_row2 = "Screen 1, row 2"
screen1_row3 = "Screen 1, row 3"
# ----------------------
screen2_row1 = "Screen 2, row 1"
screen2_row2 = "Screen 2, row 2"
# ----------------------
screen1 = [[0, 0 , screen1_row1], [0, 16, screen1_row2], [0, 32, screen1_row3]]
screen2 = [[0, 0 , screen2_row1], [0, 16, screen2_row2]]

# ------------------------------------------------------------------------
#Define Functions

def scroll_screen_in_out_v(screen):
  for i in range (0, (oled_height*2+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
        oled.fill(0)
# ------------------------------------------------------------------------
while True:

# Continuous verticall scroll
    scroll_screen_in_out_v(screen1)
    scroll_screen_in_out_v(screen2)

      
      
      
      
      
      
      
# display = SH1106_I2C(128, 64, i2c)
# display.sleep(False)
# display.fill(0)
# display.text('Testing 1', 20, 0, 1)
# display.text('Testing 2', 20, 12, 1)
# display.text('Testing 3', 20, 24, 1)
# display.text('Testing 4', 20, 36, 1)
# display.text('Testing 5', 20, 48, 1)
# display.show()


# import machine
# from machine import I2C
# import utime
# from ssd1306 import SSD1306_I2C
# 
# i2c = I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)
# 
#  
# display = SSD1306_I2C(128, 64, i2c)
# # display.sleep(False)
# display.fill(0)
# display.text('Testing 1', 20, 0, 1)
# display.text('Testing 2', 20, 12, 1)
# display.text('Testing 3', 20, 24, 1)
# display.text('Testing 4', 20, 36, 1)
# display.text('Testing 5', 20, 48, 1)
# display.show()