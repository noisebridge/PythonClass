"""
Course: Exceptions
Topic:  Putting try except in the right place.
Summary:

Takeaways:

    Lets do this one together.  Take a function that fails. Lets try to coerce a string to an integer.
    Lets run the function from a try/except block and watch the exception be automatically passed into 
    the parent context before being raised. This allows us to handle exceptions at the top level of our applications.

    If you generalize this, you could imagine having a whole section code devoted to exception handling and management.
    What would it look like? Do we have time to build a model?
    

"""
import logging
import sys # we will use exc_info() function to log our exceptions

logging.basicConfig(level=logging.DEBUG)


def open_a_file(filename):
    """ Opens the file and returns what it read

    """

    with open(filename, 'r') as f:
        print f.read()

    return f.read()


if __name__ == '__main__':
    """ Catch an IOerror, which includes any time the file doesn't exist.

    """

    # Imagine this filename is put in by the user, and it doesn't exist.
    # This file does not exist.
    filename = "does_not_exist.txt"

    try:
        open_a_file(filename)
    except IOError as e:
        logging.error(e)
        logging.error(sys.exc_info())
    # Note that we don't have a finally, with... as did this for us.


    # Demonstrate that the application continues
    print "..."
    print "Continue on with the application..."

