from machine import Pin

###############################################################################
#Define Pins

dt_direction_pin = Pin(13, Pin.IN, Pin.PULL_UP)
clk_step_pin  = Pin(12, Pin.IN, Pin.PULL_UP)
###############################################################################
# Constants

previous_value = True
counter = 0
###############################################################################
   
while True:
        if previous_value != clk_step_pin.value():
            if clk_step_pin.value() == False:
                if dt_direction_pin.value() == False:
                    counter -= 1
                    print("CW")
                    if counter >= -1:
                        print ("-Level: {}".format(counter))
                    elif counter >= -2:    
                        print ("-Level: {}".format(counter))
                    elif counter <= -3:
                        print ("-Tilted Down: {}".format(counter))
                    elif counter >= 3:
                        print ("+Tilted Up: {}".format(counter))
                    elif counter >= 0 and counter <= 2:
                        print ("+Level: {}".format(counter))
                    previous_value = clk_step_pin.value()
            
                else:
                    counter += 1
                    print("CCW")
                    if counter >= -1:
                        print ("-Level: {}".format(counter))
                    elif counter >= -2:    
                        print ("-Level: {}".format(counter))
                    elif counter <= -3:
                        print ("-Tilted Down: {}".format(counter))
                    elif counter >= 3:
                        print ("+Tilted Up: {}".format(counter))
                    elif counter >= 0 and counter <= 2:
                        print ("+Level: {}".format(counter))   

            previous_value = clk_step_pin.value()   
    
    





