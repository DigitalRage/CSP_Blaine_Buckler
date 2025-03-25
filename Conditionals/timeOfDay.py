# Blaine Buckler, Time Of Day Python

from datetime import datetime
import pytz

utah_tz = pytz.timezone("America/Denver") # I couldn't get it accurate to our time zone so I used this index instead. 
utah_time = datetime.now(utah_tz)
print("Local time in Utah:", utah_time.strftime("%H:%M:%S"))
hour = utah_time.hour
print(hour)
if hour > 20 and (hour < 6 or hour < 24):
    print("It is bed time. ")
elif hour == 7: 
    print("Get to school! ")
elif hour < 7 and hour > 16:
    print("It is school time. ")
else: 
    print("it is after school")
