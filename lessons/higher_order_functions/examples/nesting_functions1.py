"""
First lets explore nested functions. 
Nested functions have nested scopes.

PEP 227 - 'Statically Nested Scopes' - http://legacy.python.org/dev/peps/pep-0227/

Allows for closures and lambda functions.
"""


def cat():
    """ Lets see what z is in each scope.

    What do we expect to have printed when we print cat?
    """

    z = 9

    def meow():
        x = 5
        z = 5
        q = z + x

        return q, z

    return meow(), z


if __name__ == "__main__":

    print cat()
