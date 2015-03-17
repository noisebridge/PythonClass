"""
Again in this example follow this order:
    1. Read only the code.
    2. Run the code.
    3. Read the comments.
    4. Run the code as much as you need to grok it.


Original code at: http://eev.ee/blog/2011/04/24/gotcha-python-scoping-closures/
"""

if __name__ == "__main__":
    """
    """

    # We'll append a bunch of functions into this list.
    myfunctions = []

    # We'll use the namespace f repeatedly in this scope, but the functions
    # will actually be bound as indexed items in our list.  So the 'f' will
    # die after each loop.

    for i in range(4):

        def f_factory(i):
            """ Why does nesting functions work?

            This is called a factory. We passed i into
            the factory function, causing it to become
            a different 'internal' name, i, from the
            i in the parent scope.

            """
            def f():
                print i
            return f

        """
        Here is where we pass the value of i into f_factory
        This is the critical step which makes a new object i
        for each instance of f_factory.
        The function f is said to 'close around' the object i,
        creating a closure.
        f_factory(i) returns a function, which is appended to myfunctions.
        """
        myfunctions.append(f_factory(i))

    # Let's introspect on our functions.
    print myfunctions

    for my_function in myfunctions:
        my_function()
        #print my_function.__name__

    # One more trick, but this isn't pythonic. Just to see some () syntax.
    # Remember, () is called an argument list or arglist.

    for funct_index in range(len(myfunctions)):
        #print("Current index: %s" % funct_index)
        #myfunctions[funct_index]() # Note this instantiation of the list item.
        pass


