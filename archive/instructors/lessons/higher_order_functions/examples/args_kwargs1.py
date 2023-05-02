"""
First lets look at how * and ** unpack a list or a dictionary.

Inside the 2 Python grammar this is called 'arglist'
https://docs.python.org/2/reference/grammar.html

This should help explain how * and ** are unpacked in place but
doesn't help us much, since our internal function is still static.

Let's quickly move on.


DONT DWELL ON THIS DURING A LESSON:
===================================
Familiar with default values in a variable? Those are different,
and to see why you need to read the full Python 2 grammar.
Here's the grammar.  Search for varargslist.

If you need default values and args/kwargs you might reconsider
such a complex function. Here's a stack overflow:
http://stackoverflow.com/questions/9872824/calling-a-python-function-with-args-kwargs-and-optional-default-arguments

"""
# Side Note: The Zen of Python
# Remember: explicit is better than implicit
import this


def normal_function(    one, two, three, four, five, 
                        cilantro=None,
                        garlic=None):
    """ Accept args, kwargs which correspond to a list and a dict respectively.
    """
    
    # Magically we have names from our unpacked dict and list.
    # The arguments were unpacked long before passing them to this function.
    # Then they were assigned IN the function definition.
    print one, two, three, four, five
    print cilantro, garlic


if __name__ == "__main__":

    # Create some space
    print "\n\n"

    mylist = [1,2,3,4,5]
    mydict = {'cilantro':2,'garlic':3}

    normal_function(*mylist, **mydict)


