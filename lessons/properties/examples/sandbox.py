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

class Foo(object):
    name = TypedProperty("name", str) 
    num = TypedProperty("num", int, 42)


#Metaclasses
#The problem is inheriting and distinguishing things from there


