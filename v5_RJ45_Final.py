import utime
import machine
from machine import Timer
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
#===========================================================================================
#LCDs 4 rows are top to bottom 0,1,2,3
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4 #LCDs number of rows
I2C_NUM_COLS = 20 #LCDs number of columns

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
#===========================================================================================
#Define RJ45 Connection buttons
btn_top_stroke = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)  # C (WHITE) to 3.3v | NO to GPIO 2 (ORANGE)
btn_bottom_stroke = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)  # C (WHITE) to 3.3v | NO to GPIO 3 (BLUE)

# DEFINE EXTRA RJ45 CONNECTIONS
# xtra_green = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)  # C (WHITE) to 3.3v | NO to GPIO 4 (GREEN)
# xtra_brown = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)  # C (WHITE) to 3.3v | NO to GPIO 5 (BROWN)
#=====================================

led_red = machine.Pin(21, machine.Pin.OUT)  # Red to GPIO 21 Black to Ground
led_green = machine.Pin(20, machine.Pin.OUT)  # Red to GPIO 20 Black to Ground
buzzer = machine.Pin(19, machine.Pin.OUT)  #Red to GPIO 19 Black to Ground

btn_cycle_steps = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)  #C to 3.3v | NO to GPIO 15
btn_rnds_reset = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)  #C to 3.3v | NO to GPIO 14
btn_rnds_down = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)  #C to 3.3v | NO to GPIO 13
btn_rnds_up = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)  #C to 3.3v | NO to GPIO 12
#===========================================================================================  
count_btn_top_stroke = 0 
count_btn_bottom_stroke = 0

rnds_clicks = 0

tim = Timer()
#===========================================================================================
def blink_buzz(timer):
    global led_red
    global buzzer
    led_red.toggle()
    buzzer.toggle()
#===========================================================================================                   
def round_counter():
    global rnds_clicks
    rnds_clicks += 1 #Add 1 for each button press
    lcd.move_to(0,3)
    lcd.putstr('Rnds: {}'.format(rnds_clicks))
    utime.sleep(0.25)  #Pause
#===========================================================================================
def count_up(pin):
    global rnds_clicks
    global count_btn_top_stroke
    global count_btn_bottom_stroke
    if btn_rnds_up.value() == 1:
        if count_btn_top_stroke >= 3:  #Only pass if its on error screen
            pass
        elif count_btn_bottom_stroke >= 3:  #Only pass if its on error screen
            pass
        else:  
            rnds_clicks += 1  #Add 1 to the rounds counter
            lcd.move_to(6,3)
            lcd.putstr('{}'.format(rnds_clicks))
            utime.sleep(0.25)  # Pause or it adds several numbers
        
#Attach interrupt to btn_rnds_up              
btn_rnds_up.irq(trigger=machine.Pin.IRQ_RISING, handler=count_up)
#===========================================================================================
def count_down(pin):
    global rnds_clicks
    global count_btn_top_stroke
    global count_btn_bottom_stroke
    if btn_rnds_down.value() == 1:
        if rnds_clicks < 1:  #Dont allow count to go below 0 into negative numbers
            print('7_rnds_clicks: {}'.format(rnds_clicks))
            pass
        elif count_btn_top_stroke >= 3:  #Only pass if its on error screen
            print('8_count_btn_top_stroke: {}'.format(count_btn_top_stroke))
            pass
        elif count_btn_bottom_stroke >= 3:  #Only pass if its on error screen
            print('9_count_btn_bottom_stroke: {}'.format(count_btn_bottom_stroke))
            pass
        else:
#Print 14 blank spaces to clear round counter
            lcd.move_to(6,3) 
            lcd.putstr("              ")
            rnds_clicks -= 1  #Decreases 1 to the rounds counter
            lcd.move_to(6,3)
            lcd.putstr('{}'.format(rnds_clicks))
            utime.sleep(0.25)
            
#Attach interrupt to btn_rnds_down              
btn_rnds_down.irq(trigger=machine.Pin.IRQ_RISING, handler=count_down)
#===========================================================================================
def count_reset(pin):
    global rnds_clicks
    global count_btn_top_stroke
    global count_btn_bottom_stroke
    if btn_rnds_reset.value() == 1:
        if count_btn_top_stroke >= 3:  #Only pass if its on error screen
            print('5_count_btn_top_stroke: {}'.format(count_btn_top_stroke))
            tim.deinit()  #Deinitialises the timer. Stops the timer, and disables the timer peripheral.
            led_red.value(1)  #Set led to off
            buzzer.value(0)  #Stop active buzzer
            pass  #Do nothing to LCD until user fixes stroke
        elif count_btn_bottom_stroke >= 3:  #Only pass if its on error screen
            print('6_count_btn_bottom_stroke: {}'.format(count_btn_bottom_stroke))
            tim.deinit()  #Deinitialises the timer. Stops the timer, and disables the timer peripheral.
            led_red.value(1)  #Set led to off
            buzzer.value(0)  #Stop active buzzer
            pass  #Do nothing to LCD until user fixes stroke
        else:
#Print 14 blank spaces to clear round counter
            lcd.move_to(6,3) 
            lcd.putstr("               ")
            rnds_clicks = 0  #Set rounds counter to 0 so when you go up it counts 1
            lcd.move_to(0,3)
            lcd.putstr('Rnds: {}'.format(rnds_clicks))
            utime.sleep(0.25)
            
#Attach interrupt to btn_rnds_reset              
btn_rnds_reset.irq(trigger=machine.Pin.IRQ_RISING, handler=count_reset)
#===========================================================================================
def cycle_steps(pin):
    global rnds_clicks
    global count_btn_top_stroke
    global count_btn_bottom_stroke

    if btn_cycle_steps.value() == 1:
        if count_btn_top_stroke >= 3:  #Only pass if its on error screen
            print('1_count_btn_top_stroke: {}'.format(count_btn_top_stroke))
            pass  #Do nothing
        elif count_btn_bottom_stroke >= 3:  #Only pass if its on error screen
            print('2_count_btn_bottom_stroke: {}'.format(count_btn_bottom_stroke))
            pass  #Do nothing
        else:
            count_btn_top_stroke += 1
            count_btn_bottom_stroke = 0
            if count_btn_top_stroke %2 == 1:
                print('3_count_btn_top_stroke: {}'.format(count_btn_top_stroke))
                led_red.value(0)  #Set led to off
                led_green.value(1)  #Set led to on
                lcd.clear() #Clear screen 
                lcd.move_to(2,1) #Moves text 2 characters from left on row 2
                lcd.putstr("PULL HANDLE DOWN")
                lcd.move_to(0,3)
                lcd.putstr('Rnds: {}'.format(rnds_clicks))
                utime.sleep(0.25)
            if btn_cycle_steps.value(): 
                count_btn_bottom_stroke += 1
                count_btn_top_stroke = 0   
            if count_btn_bottom_stroke % 2 == 1:
                print('4_count_btn_bottom_stroke: {}'.format(count_btn_bottom_stroke))
                led_red.value(0)  #Set led to off
                led_green.value(1)  #Set led to on
                lcd.clear() #Clear screen                                                                             
                lcd.move_to(3,1) #Moves text 3 characters from left on row 2
                lcd.putstr("PUSH HANDLE UP")
                lcd.move_to(0,3)
                lcd.putstr('Rnds: {}'.format(rnds_clicks))
                utime.sleep(0.25)

#Attach interrupt to btn_cycle_steps             
btn_cycle_steps.irq(trigger=machine.Pin.IRQ_RISING, handler=cycle_steps)
#===========================================================================================

lcd.clear() #Clear LCD screen
led_red.value(0)  #Turn off red LED if on
lcd.move_to(3,1) #Moves text 3 characters from left on row 2
lcd.putstr("LEE LOADMASTER")
lcd.move_to(3,2) #Moves text 3 characters from left on row 3
lcd.putstr("MONITOR SYSTEM")
utime.sleep(4) #Pause for 4 seconds for introduction

lcd.clear() #Clear screen
lcd.move_to(2,1) #Moves text 2 characters from left on row 2
lcd.putstr("PULL HANDLE DOWN")
lcd.move_to(0,3)
lcd.putstr('Rnds: {}'.format(rnds_clicks))
led_green.value(1)  #Ok to go turn on green LED
# count_btn_top_stroke += 1  #Sets count_btn_top_stroke to 1 to show it was pressed on startup
# count_btn_bottom_stroke = 0   #Sets count_btn_bottom_stroke to 0

#Added because when turned on the handle might/not be against the top of the stroke
if btn_top_stroke.value(): 
    rnds_clicks -= 1  #Decreases 1 to the rounds counter
#===========================================================================================
    
while True:
    if btn_top_stroke.value(): #Was the btn_top_stroke button pushed?
        count_btn_top_stroke += 1
        count_btn_bottom_stroke = 0   #Force the toggle (reset the other side)
        if count_btn_top_stroke %2 == 1:  #Message head to button 2 on odd
            lcd.clear() #Clear screen
            lcd.move_to(2,1) #Moves text 2 characters from left on row 2
            lcd.putstr("PULL HANDLE DOWN")
            round_counter() #Counts up rounds made when btn_top_stroke is pressed
            tim.deinit()  #Deinitialises the timer. Stops the timer, and disables the timer peripheral.
            led_green.value(1)  #Ok to go
            led_red.value(0)  #Set led to off
            buzzer.value(0)  #Stop active buzzer
        if count_btn_top_stroke %2 == 0:  #Pushed it twice kick to buzzer
            lcd.clear() #Clear LCD screen
            lcd.move_to(2,0) #Moves text 2 characters from left on row 1
            lcd.putstr("INCOMPLETE CYCLE")
            lcd.move_to(2,1) #Moves text 2 characters from left on row 2
            lcd.putstr("PULL HANDLE DOWN")
            lcd.move_to(0,3) #Moves text 0 characters from left on row 4
            lcd.putstr("(CHECK ALL STATIONS)")
            led_green.value(0)  #Turn off green LED becasue of error
            tim.init(freq=2, mode=Timer.PERIODIC, callback=blink_buzz)  #Start blinking LED continious untill reset
            count_btn_top_stroke += 1  #Set count_btn_top_stroke to 1 incase pressed again
        while btn_top_stroke.value():
            utime.sleep(0.05)
            
    if btn_bottom_stroke.value(): #Was the btn_bottom_stroke button pushed?
        count_btn_bottom_stroke += 1
        count_btn_top_stroke = 0   #Force the toggle (reset the other side)
        if count_btn_bottom_stroke % 2 == 1:  #Message head to button 1 on odd pushes
            lcd.clear() #Clear screen                                                                             
            lcd.move_to(3,1) #Moves text 3 characters from left on row 2
            lcd.putstr("PUSH HANDLE UP")
            lcd.move_to(0,3) #Moves text 0 characters from left on row 4
            lcd.putstr('Rnds: {}'.format(rnds_clicks))
            tim.deinit()  #Deinitialises the timer. Stops the timer, and disables the timer peripheral.
            led_green.value(1)  #Ok to go
            led_red.value(0)  #Set led to off
            buzzer.value(0)  #Stop active buzzer
        if count_btn_bottom_stroke %2 == 0:  #Pushed it twice kick to buzzer 
            lcd.clear() #Clear LCD screen
            lcd.move_to(2,0) #Moves text 2 characters from left on row 1
            lcd.putstr("INCOMPLETE CYCLE")
            lcd.move_to(3,1) #Moves text 3 characters from left on row 2ccc
            lcd.putstr("PUSH HANDLE UP")
            lcd.move_to(0,3) #Moves text 0 characters from left on row 4
            lcd.putstr("(CHECK ALL STATIONS)")
            led_green.value(0)  #Turn off green LED becasue of error
            tim.init(freq=2, mode=Timer.PERIODIC, callback=blink_buzz)  #Start blinking LED continious untill reset
            count_btn_bottom_stroke += 1  #Set count_btn_bottom_stroke to 1 incase pressed again
        while btn_bottom_stroke.value():
            utime.sleep(0.05)





