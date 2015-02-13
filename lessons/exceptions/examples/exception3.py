"""
Course: Exceptions
Topic:  with... as
Summary: Use 'try... except', the familiar 'open' built-in function, and 'with... as' to demonstrate capturing an exception.
Takeaways: The purpose of  'with... as' is to perform certain actions if the action fails early.  In this case, 'open'
has a context manager which closes the file before returning the exception. We still need to capture the exception.

"""
import logging
import sys # we will use exc_info() function to log our exceptions

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    """ Catch an IOerror, which includes any time the file doesn't exist.

    """

    # Imagine this filename is put in by the user, and it doesn't exist.
    # This file does not exist.
    filename = "does_not_exist.txt"

    try:
        with open(filename, 'r') as f:
            print f.read()
    except IOError as e:
        logging.error(e)
        logging.error(sys.exc_info())
    # Note that we don't have a finally, with... as did this for us.


    # Demonstrate that the application continues
    print "..."
    print "Continue on with the application..."

