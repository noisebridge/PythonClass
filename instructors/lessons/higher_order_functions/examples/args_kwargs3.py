"""
Topic: *args, **kwargs

Contrived real world example.

The names args, kwargs are just convention.

You can replace them with spaghetti and kittens, the interpreter
won't mind one bit.
"""

def sum_ints(*args, **kwargs):
    """ This function is contrived to illustrate args in a function.
    """

    print args

    return sum(args)

if __name__ == "__main__":


    print sum_ints(1,2,3)

    print sum_ints(1,2)

    print sum_ints()
