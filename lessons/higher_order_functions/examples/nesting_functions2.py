"""
Lets see how the Python bytecode compiler deals with nested scope.
"""


def outer():
    """ Lets see what z is in each scope.

    What do we expect to have printed when we print cat?
    """

    z = 9

    def inner():

        x = 5
        q = z + x

        # Run this with z commented first. Then uncomment z.
        # IMPORTANT: Predict what will happen!
        #z = 5

        return q, z

    return inner(), z


if __name__ == "__main__":
    """
    Don't dwell on this during class:
    =================================
    Python 3 has a new keyword called nonlocal used like this:
        nonlocal z
    This will expose the parent scope of z to the local scope, skirting
    the 'assignment before reference' issue and allowing the parent 
    scope to be changed within the local scope. This may or may not be
    your intended behavior. 

    You may not want the parent scope to change within the local 
    scope. But when you do, you don't need to do any weird contortions 
    to accomplish it (e.g. return the new value of z from the inner 
    scope and assign it back to the parent scope for z.
    """

    print outer()
