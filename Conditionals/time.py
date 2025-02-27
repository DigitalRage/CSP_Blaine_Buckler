# Blaine Buckler, wow to get bthe time of day Python

import time
# gmtime(0) is the first instance of time
# print(time.gmtime(0))

# current time in seconds since gmtime
# print(time.time())

current = time.time()

# current time as we are used to seeing it
now = time.ctime(current)
print(now)

# get just the hour
local_time = time.localtime(current)
hour = local_time.tm_hour
minute = local_time.tm_min
print(minute)
print(hour)
