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