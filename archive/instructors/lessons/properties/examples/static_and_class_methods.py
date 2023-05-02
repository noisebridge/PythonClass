import time

class Date(object):
    def __init__(self, year, month, day):
        self.year = year 
        self.month = month 
        self.day = day
    
    @staticmethod 
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday) 

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400) 
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    '''@classmethod 
    def cls_now(cls):
        t = time.localtime()
        # Create an object of the appropriate type 
        return cls(t.tm_year, t.tm_month, t.tm_mday)'''

# Example of creating some dates
a = Date(1967, 4, 9)
b = Date.now() # Calls static method now()
c = Date.tomorrow() # Calls static method tomorrow()
#d = Date.cls_now()
print a.__dict__
print b
print c

class Times(object): 
    factor = 1

    @classmethod 
    def mul(cls,x):
        return cls.factor * x

class TwoTimes(Times): 
    factor = 2

x = TwoTimes.mul(4) # Calls Times.mul(TwoTimes, 4) -> 8

print x


class EuroDate(Date):
    # Modify string conversion to use European dates 
    def __str__(self):
        return "%02d/%02d/%4d" % (self.day, self.month, self.year)