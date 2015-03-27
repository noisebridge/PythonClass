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