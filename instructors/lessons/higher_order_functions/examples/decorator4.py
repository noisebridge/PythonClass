"""
lets pass an argument to a decorator which calls a decorator
containing a wrapper... things are getting out of hand...
"""

# Lets count how often the decorator is used.
# This needs to be a mutable object in Python 2.
# Why? Because we don't have the nonlocal keyword.
# Otherwise if we try to change it, it will be referenced before assignment.
i = [0]


def incrementor(i):
    print i[0]
    def mydecorator(func):
        """ A decorator that simply passes through a function.
        """
        # We see this when the decorator itself is invoked.
        print "Decorator is go!"
        def function_wrapper(*args, **kwargs):
            """
            We'll need to run the function in the wrapper in order
            to extend the functionality and/or modify the output.
            """
            if i[0] < 5:
                # This wrapping happens before the decorated function is run...
                # We get these increments as the wrappers are executed.
                i[0] += 1
                print i
                # Lets intercept the return if there are too many values.
                # I have been explicit in this compound if statement, but 
                # remember an empty dict/list is false, so there's a better way.
                if len(args) > 1 or len(kwargs.keys()) > 0:
                    return func(args[0])
                elif len(args) == 0:
                    return func('')
                else:
                    return func(*args, **kwargs)
            else:
                def passfunc(func):
                    def useless():
                        pass
                    return useless
                return passfunc

        return function_wrapper
    return mydecorator

# Using the decorator a bunch. Why not?
@incrementor(i)
@incrementor(i)
@incrementor(i)
@incrementor(i)
@incrementor(i)
def sample(myinput):
    print "instantiating sample function"
    return myinput

# This would all break if it wasn't wrapped/decorated!
print sample('too', 'many', 'arguments')
print sample('we got data through!', 'tell NASA!')
print sample()

print i[0]
