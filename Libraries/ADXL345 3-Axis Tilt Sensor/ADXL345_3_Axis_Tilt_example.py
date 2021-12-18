import machine
from machine import Pin, I2C
import utime
import ustruct

# https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-i2c-example-with-micropython-and-cc/47d0c922b79342779cdbd4b37b7eb7e2

###############################################################################
# Constants

# I2C address
ADXL345_ADDR = 0x53

# Registers
REG_DEVID = 0x00
REG_POWER_CTL = 0x2D
REG_DATAX0 = 0x32

# Other constants
DEVID = 0xE5
SENSITIVITY_2G = 1.0 / 256  # (g/LSB)
EARTH_GRAVITY = 9.80665     # Earth's gravity in [m/s^2]

###############################################################################

# Initialize I2C with pins 
print("Setting Up i2c")
sda = Pin(0)
scl = Pin(1)
id = 0

# Create I2C object
i2c = I2C(id=id, sda=sda, scl=scl,freq=400000)

# Scan the bus and print out address found
devices = i2c.scan()

if devices:
    for d in devices:
        print("i2c hex:",hex(d))

print("i2c scan:",repr(i2c.scan()))
if 0x53 not in i2c.scan():
    print("Failed to find device")
    raise RuntimeError()

###############################################################################
# Functions

def reg_write(i2c, addr, reg, data):
    """
    Write bytes to the specified register.
    """
    
    # Construct message
    msg = bytearray()
    msg.append(data)
    
    # Write out message to register
    i2c.writeto_mem(addr, reg, msg)
    
def reg_read(i2c, addr, reg, nbytes=1):
    """
    Read byte(s) from specified register. If nbytes > 1, read from consecutive
    registers.
    """
    
    # Check to make sure caller is asking for 1 or more bytes
    if nbytes < 1:
        return bytearray()
    
    # Request data from specified register(s) over I2C
    data = i2c.readfrom_mem(addr, reg, nbytes)
    
    return data

###############################################################################
# Main

# Read device ID to make sure that we can communicate with the ADXL345
data = reg_read(i2c, ADXL345_ADDR, REG_DEVID)
if (data != bytearray((DEVID,))):
    print("ERROR: Could not communicate with ADXL345")
    sys.exit()
    
# Read Power Control register
data = reg_read(i2c, ADXL345_ADDR, REG_POWER_CTL)
print("Power Control Register:", data)

# Tell ADXL345 to start taking measurements by setting Measure bit to high
data = int.from_bytes(data, "big") | (1 << 3)
reg_write(i2c, ADXL345_ADDR, REG_POWER_CTL, data)

# Test: read Power Control register back to make sure Measure bit was set
data = reg_read(i2c, ADXL345_ADDR, REG_POWER_CTL)
print("Register Back Power Control:", data)

# Wait before taking measurements
utime.sleep(2.0)

###############################################################################
while True:
    
    # Read X, Y, and Z values from registers (16 bits each)
    data = reg_read(i2c, ADXL345_ADDR, REG_DATAX0, 6)

    # Convert 2 bytes (little-endian) into 16-bit integer (signed)
    acc_x = ustruct.unpack_from("<h", data, 0)[0]
    acc_y = ustruct.unpack_from("<h", data, 2)[0]
    acc_z = ustruct.unpack_from("<h", data, 4)[0]

    # Convert measurements to [m/s^2]
    acc_x = acc_x * SENSITIVITY_2G * EARTH_GRAVITY
    acc_y = acc_y * SENSITIVITY_2G * EARTH_GRAVITY
    acc_z = acc_z * SENSITIVITY_2G * EARTH_GRAVITY
##################################################
#  Print results_Old
    
#     print("X:", "{:.2f}".format(acc_x), \
#           "| Y:", "{:.2f}".format(acc_y), \
#           "| Z:", "{:.2f}".format(acc_z))
##################################################
#  Print results_New

#   {:.2f} = Specifys 2 digits of precision and f represents a floating point number
    y_tilt = ("{:.2f}".format(acc_y))  
    
    if y_tilt >= "2.00":
        print ("Tilted Up: {}".format(y_tilt))       
    elif y_tilt >= "-0.01" and y_tilt <= "-1.99":
        print ("-Level: {}".format(y_tilt))
    elif y_tilt >= "0.00" and y_tilt <= "1.99":
        print ("+Level: {}".format(y_tilt))    
    else:
        print ("Tilted Down: {}".format(y_tilt))
    utime.sleep(0.1)
    
    
    
    
    
    
