"""
This example intentionally doesn't work.

Go through this code and predict what will happen, then run
the code.

The below function fixes i in the parent scope, which means
that the function 'f' 'gets updates' as i progresses through
the loop.

Clearly we need to somehow fix i to be contained in the local
scope for 'f'.

Original code at: http://eev.ee/blog/2011/04/24/gotcha-python-scoping-closures/
"""


if __name__ == "__main__":
    """
    Only read the code the first time through.

    Then read the comments after you see the results.
    """

    # We'll append a bunch of functions into this list.
    myfunctions = list()


    for i in range(4):
        """
        We'll use the namespace f repeatedly in this scope, but 
        the functions will actually be bound as indexed items in 
        our list. The 'f' name will be fresh in each loop.
        """

        def f():
            """
            Each time we build this function, we are fixing the
            value i into the function from the parent scope.

            Here we try and fail to fix a new value of i into the
            function f each time through the loop. Why does it fail?
            
            Note: in Python, child scopes have access to all parent
            scopes up to the global scope, so be wary of this and
            use it to your advantage where possible.
            """
            print i

        myfunctions.append(f)
    i=7

    for my_function in myfunctions:
        my_function()

