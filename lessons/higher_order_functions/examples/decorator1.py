"""
You might notice we haven't used any @ symbols. We'll do that next.

For now lets focus on the order of resolution of our print statements.

The additional instatiation of the decorated result is responsible
for the print order (The extra parentheses in the main area).

This would be totally fine in your code, but Python has special syntax for this.
"""



def mydecorator(func):
    print "Decorator is go!"
    """ A decorator that simply passes through a function.
    """
    return func


def sample():
    print "instantiating sample function"
    return 'sample'

if __name__ == "__main__":
    """
    Note the interesting parentheses. Doesn't look very pretty.
    And yet, this is how we instantiate a returned function.
    """

    print mydecorator(sample)()

