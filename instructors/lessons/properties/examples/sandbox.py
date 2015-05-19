import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "a circle with radius {}".format(self.radius)
    # Some additional properties of Circles 
    @property #not an attribute to be modified but to be calculated itself
    #an attribute is to be calculated not to be modified 
    def area(self):
        return math.pi * self.radius ** 2

    def b_area(self):
        return math.pi * self.radius ** 2 

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(10)

print c 
print c.area
print c.b_area()

class Foo(object):
    def __init__(self,name):
        self.__name = name 

    def __repr__(self):
        return self.__name 

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if not isinstance(value,str): 
            raise TypeError("Must be string")
            self.__name = value 

    @name.deleter
    def name(self):
        raise TypeError("can't delete name")

f = Foo('okay now')

print f
#f.name('hello')  NOPE!
f = "hello"
print f

#A descriptor is simply an object that represents the value of an attribute
#it customizes one or more of the special methods 
#   __get__(), __set__(), and __delete__()

class TypedProperty(object):
    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        self.default = default if default else type()

    def __get__(self, instance, cls):
        return getattr(instance,self.name,self.default)

    def __set__(self, instance, value): #known as caching
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type) 
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

class Use(object):
    name = TypedProperty("name", str) 
    num = TypedProperty("num", int, 42)


#Metaclasses
#The problem is inheriting and distinguishing things from there
import time
class Date(object):

    def __init__(self, year, month, day):
        self.year = year 
        self.month = month 
        self.day = day 

    def __repr__(self):
        return "the date of {0}/{1}/{2}".format(self.month, self.day, self.year)

    def now(self):
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday) 

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400) 
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod 
    def clm_now(cls):
        t = time.localtime()
        print "cls method"
        # Create an object of the appropriate type 
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


d = Date(1967, 4, 9)

print d
print d.tomorrow()
print d.now()
print d.clm_now()
print d.tomorrow()

class Foo(object):

    def __init__(self, baz, bar, bow):
        self.baz = baz 
        self.bar = bar 
        self.bow = bow

    def __repr__(self):
        return "the attributes of {0}/{1}/{2}".format(self.baz, self.bar, self.bow)

f = Foo('baz', 'bar', 'bow')
