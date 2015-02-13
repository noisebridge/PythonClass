"""
Course: Exceptions
Topic:  try... except... finally
Summary: Introduce finally. Finally allows us to 'cleanly finish' what we are doing in the try 
block, after an except block. In this example, the code is opened for write, but mistakenly read from.

Takeaways: Finally can be used to finish up what you are doing whether or not there was an exception.  
The example here is a little contrived (based on user error!) but we can imagine a case where your code
opens a file, then some other program locks it, and then your program crashes because it can't write.

Next up we'll discuss 'with... as' and get into the basics of using our first context manager (it is built-in to 'open').

"""

if __name__ == '__main__':
    """ Catch an IOerror, which includes any time the file doesn't exist.

    """

    filename = "myfile.txt"

    try:
        f = open(filename, 'w')
        f.read()

    except IOError as e:
        print "Error!", e # we will look at this next example, ignore it for now

    # This always runs after the try, even if there is an exception.
    finally:
        print "Is f closed?", f.closed
        f.close() # We need to manually close this, next we will learn a better way
        print "Is f closed?", f.closed


    # Demonstrate that the application continues
    print "..."
    print "Continue on with the application..."

