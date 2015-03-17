"""
A quick example of *args and *kwargs

This is the right way to do things.  Note that we should be
explicit where possible, but we also need ways to do things
dynamically when the need arises.

Q: How is this better than explicit arguments?
A: Our function can accept input from anywhere. If you have a
variety of different places that call this function, they don't
need to know anything about the function to put arguments in.

Explicit means not using this pattern where possible.
"""
# Remember: explicit is better than implicit
import this


def dyn_function(*spaghetti, **potato_hash):
    """ Accept spaghetti, potato_hash which correspond to a list and a dict respectively.
    """
    
    print "\n\n"
    print("{}, {}").format(type(spaghetti), type(potato_hash))
    print("{}, {}").format(spaghetti, potato_hash)


if __name__ == "__main__":

    # Create some space

    mylist = [1,2,3,4,5]
    mydict = {'cilantro':2,'tomatoes':10,'onions':1,'garlic':3}
    # So what do we expect here?  When are things unpacked?
    # How many objects are going into the function?
    # Are we using the complete functionality inside the function? (hint: no)
    dyn_function(*mylist, **mydict)

    # What about here? How many objects?
    # How does the output differ from the above function?
    dyn_function(   1, 
                    'pomodoro', 
                    cilantro=2, 
                    tomatoes=10, 
                    onions=1, 
                    garlic=3)




