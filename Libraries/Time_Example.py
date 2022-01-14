import time
import random

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
eut = time.time() # Epoch Unix Timestamp
        
if len(str(abs(time.localtime()[4]))) == 1:
    date_min = ("0" + str(abs(time.localtime()[4])))
else:
    date_min = str(abs(time.localtime()[4]))
if len(str(abs(time.localtime()[3]))) == 1:
    date_hr = ("0" + str(abs(time.localtime()[3])))
else:
    date_hr = str(abs(time.localtime()[3]))
if len(str(abs(time.localtime()[2]))) == 1:
    date_day = ("0" + str(abs(time.localtime()[2])))
else:
    date_day = str(abs(time.localtime()[2]))

    todays_date = (months[abs(time.localtime()[1])] + "-" + date_day + "-" + str(abs(time.localtime()[0]) % 100) + " " + date_hr + ":" + date_min)
        
        
print(todays_date)
print(eut)

file = open("data" + str(random.getrandbits(16)) + ".csv","w") # creation and opening of a CSV file in Write mode
file.write(str(todays_date)+"," + str(eut)) # Writing data in the opened file
file.close() 
