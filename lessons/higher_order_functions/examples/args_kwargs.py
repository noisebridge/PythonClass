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


if __name__ == "__main__":

    # Create some space
    print "\n\n"

    dyn_function(   1, 
                    'pomodoro', 
                    cilantro=2, 
                    tomatoes=10, 
                    onions=1, 
                    garlic=3)



