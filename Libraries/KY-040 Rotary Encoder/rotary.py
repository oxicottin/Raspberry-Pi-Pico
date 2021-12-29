from machine import Pin

dt_direction_pin = Pin(13, Pin.IN, Pin.PULL_UP)
clk_step_pin  = Pin(12, Pin.IN, Pin.PULL_UP)

previous_value = True
counter = 0
###############################################################################
def cw_direction():
    global counter
    counter -= 1
    print ("turned left: {}".format(counter))
  
def ccw_direction():
    global counter
    counter += 1
    print ("turned right: {}".format(counter))    
###############################################################################
    
while True:
    if previous_value != clk_step_pin.value():
        if clk_step_pin.value() == False:
            if dt_direction_pin.value() == False:
                cw_direction()
            else:
                ccw_direction()
        previous_value = clk_step_pin.value()   
    