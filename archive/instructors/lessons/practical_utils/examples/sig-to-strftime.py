#note most of this file is an example from pymotw
import datetime

print help(datetime.datetime)

d = datetime.datetime(1999, 12, 30, 14,33)
print d

s = d.strftime(format)

print s


today = datetime.datetime.today()
print 'ISO     :', today

format = "%a %b %d %H:%M:%S %Y"

s = today.strftime(format)
print 'strftime:', s

d = datetime.datetime.strptime(s, format)
print 'strptime:', d.strftime(format)