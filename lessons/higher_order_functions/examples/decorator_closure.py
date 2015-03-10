"""
A decorator is used to add a feature to a function.

1. The decorator should? return a function.
2. The returned function can be the original function something else.

So what does a decorator have to do with a closure?

Original Code: http://pymbook.readthedocs.org/en/latest/igd.html
"""



def mydecorator(func):
    def wrapper(*args, **kwargs):
        print 'before call'
        # run the function passed to the decorator
        result = func(*args, **kwargs)
        print 'after call'
        return result
    return wrapper


@mydecorator
def sample():
    return 'sample'

print sample()
