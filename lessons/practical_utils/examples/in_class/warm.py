from pprint import pprint
import datetime as dt

p = pprint

#p(dir(dt))

print dir()
print "\n\n\n"
print help(dt.time)

''' 
keyword signature denoted by brackets 
eg: datetime.time([hour[, minute[, second[, microsecond[, tzinfo]]]]])
is distinguished with key=value arguments
time(hour=x, minute=y, etc...)

positional signatures denoted by commas making a regular tuple 
class datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])¶
datetime(required, required, required, hour=non-required, minute=non-required)
'''

dt_time_obj = dt.time(minute=27)
print dt_time_obj

print dir(dt_time_obj)

print (dt_time_obj.max)