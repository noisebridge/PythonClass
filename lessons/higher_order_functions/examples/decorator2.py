"""
So here's the special syntax for a decorator.

"""



def mydecorator(func):
    print "Decorator is go!"
    """ A decorator that simply passes through a function.
    """
    return func


# Using the decorator.
@mydecorator
def sample():
    print "instantiating sample function"
    return 'sample'

print sample()
