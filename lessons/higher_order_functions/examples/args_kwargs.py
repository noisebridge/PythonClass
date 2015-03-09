"""
A quick example of *args and *kwargs
"""


# Remember: explicit is better than implicit
import this

def dyn_function(*args, **kwargs):
    """ Accept args, kwargs which correspond to a list and a dict respectively.
    """
    
    print("{}, {}").format(type(args), type(kwargs))
    print("{}, {}").format(args, kwargs)


def dyn_function_with_explicits(argname, name="myname", *args, **kwargs):

    print type(argname), argname
    print type(name), name

    print("{}, {}").format(type(args), type(kwargs))
    print("{}, {}").format(args, kwargs)


if __name__ == "__main__":

    # Create some space
    print "\n\n"

    dyn_function(   1, 
                    'pomodoro', 
                    cilantro=2, 
                    tomatoes=10, 
                    onions=1, 
                    garlic=3)

    mylist = [1,2,3,4,5]
    mydict = {'cilantro':2,'tomatoes':10,'onions':1,'garlic':3}

    dyn_function_with_explicits(    'argument', 
                                    dir(),
                                    mylist,
                                    mydict)



