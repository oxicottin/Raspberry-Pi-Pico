# Random Nerd Tutorials


## Complete project details at: 
https://RandomNerdTutorials.com/micropython-ssd1306-oled-scroll-shapes-esp32-esp8266/

SH1106 OLED Library
The library to write to the OLED display isn’t part of the standard MicroPython library by default. So, you need to upload the library to your  board.

MicroPython OLED Scroll Functions
The sh1106.py library comes with a scroll(x, y) function. It scroll x number of pixels to the right and y number of pixels down.

Scroll OLED Screen Horizontally
Sometimes you want to display different screens on the OLED display. For example, the first screen shows sensor readings, and the second screen shows GPIO states.

Scroll in horizontally
The following function scroll_in_screen(screen) scrolls the content of an entire screen (right to left).
```
def scroll_in_screen(screen):
  for i in range (0, oled_width+1, 4):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)
```

This function accepts as argument a list of lists. For example:

screen1 = [[0, 0 , screen1_row1], [0, 16, screen1_row2], [0, 32, screen1_row3]]
Each list of the list contains the x coordinate, the y coordinate and the message [x, y, message].

As an example, we’ll display three rows on the first screen with the following messages.
```
screen1_row1 = "Screen 1, row 1"
screen1_row2 = "Screen 1, row 2"
screen1_row3 = "Screen 1, row 3"
```
Then, to make your screen scrolling from left to right, you just need to call the scroll_in_screen() function and pass as argument the list of lists:

scroll_in_screen(screen1)


## Scroll out horizontally
To make the screen scroll out, you can use the scroll_out_screen(speed) function that scrolls the entire screen out of the OLED. It accepts as argument a number that controls the scrolling speed. The speed must be a divisor of 128 (oled_width)
```
def scroll_out_screen(speed):
  for i in range ((oled_width+1)/speed):
    for j in range (oled_height):
      oled.pixel(i, j, 0)
    oled.scroll(speed,0)
    oled.show()
```


Now, you can use both functions to scroll between screens. For example:
```
scroll_in_screen(screen1)
scroll_out_screen(4)
scroll_in_screen(screen2)
scroll_out_screen(4)
```
## Continuous horizontal scroll
If you want to scroll the screen in and out continuously, you can use the scroll_screen_in_out(screen) function instead.
```
def scroll_screen_in_out(screen):
  for i in range (0, (oled_width+1)*2, 1):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)
```      
You can use this function to scroll between screens, or to scroll the same screen over and over again.
```
scroll_screen_in_out(screen1)
scroll_screen_in_out(screen2)
scroll_screen_in_out(screen3)
```

## Scroll OLED Screen Vertically
We also created similar functions to scroll the screen vertically.

Scroll in vertically
The scroll_in_screen_v(screen) scrolls in the content of the entire screen.
```
def scroll_in_screen_v(screen):
  for i in range (0, (oled_height+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)
```


## Scroll out vertically
You can use the scroll_out_screen_v(speed) function to scroll out the screen vertically. Similarly to the horizontal function, it accepts as argument, the scrolling speed that must be a number divisor of 64 (oled_height).
```
def scroll_out_screen_v(speed):
  for i in range ((oled_height+1)/speed):
    for j in range (oled_width):
      oled.pixel(j, i, 0)
    oled.scroll(0,speed)
    oled.show()
```


## Continuous vertical scroll
If you want to scroll the screen in and out vertically continuously, you can use the scroll_in_out_screen_v(screen) function.
```
def scroll_screen_in_out_v(screen):
  for i in range (0, (oled_height*2+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)
```


## Scroll OLED Screen MicroPython Script
The following script applies all the functions we’ve described previously. You can upload the following code to your board to see all the scrolling effects.

```
from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

screen1_row1 = "Screen 1, row 1"
screen1_row2 = "Screen 1, row 2"
screen1_row3 = "Screen 1, row 3"

screen2_row1 = "Screen 2, row 1"
screen2_row2 = "Screen 2, row 2"

screen3_row1 = "Screen 3, row 1"

screen1 = [[0, 0 , screen1_row1], [0, 16, screen1_row2], [0, 32, screen1_row3]]
screen2 = [[0, 0 , screen2_row1], [0, 16, screen2_row2]]
screen3 = [[0, 40 , screen3_row1]]

# Scroll in screen horizontally from left to right
def scroll_in_screen(screen):
  for i in range (0, oled_width+1, 4):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

# Scroll out screen horizontally from left to right
def scroll_out_screen(speed):
  for i in range ((oled_width+1)/speed):
    for j in range (oled_height):
      oled.pixel(i, j, 0)
    oled.scroll(speed,0)
    oled.show()

# Continuous horizontal scroll
def scroll_screen_in_out(screen):
  for i in range (0, (oled_width+1)*2, 1):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

# Scroll in screen vertically
def scroll_in_screen_v(screen):
  for i in range (0, (oled_height+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)

# Scroll out screen vertically
def scroll_out_screen_v(speed):
  for i in range ((oled_height+1)/speed):
    for j in range (oled_width):
      oled.pixel(j, i, 0)
    oled.scroll(0,speed)
    oled.show()

# Continous vertical scroll
def scroll_screen_in_out_v(screen):
  for i in range (0, (oled_height*2+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)

while True:

  # Scroll in, stop, scroll out (horizontal)
  scroll_in_screen(screen1)
  sleep(2)
  scroll_out_screen(4)

  scroll_in_screen(screen2)
  sleep(2)
  scroll_out_screen(4)

  scroll_in_screen(screen3)
  sleep(2)
  scroll_out_screen(4)

  # Continuous horizontal scroll
  scroll_screen_in_out(screen1)
  scroll_screen_in_out(screen2)
  scroll_screen_in_out(screen3)

  # Scroll in, stop, scroll out (vertical)
  scroll_in_screen_v(screen1)
  sleep(2)
  scroll_out_screen_v(4)

  scroll_in_screen_v(screen2)
  sleep(2)
  scroll_out_screen_v(4)

  scroll_in_screen_v(screen3)
  sleep(2)
  scroll_out_screen_v(4)

  # Continuous verticall scroll
  scroll_screen_in_out_v(screen1)
  scroll_screen_in_out_v(screen2)
  scroll_screen_in_out_v(screen3)
```

