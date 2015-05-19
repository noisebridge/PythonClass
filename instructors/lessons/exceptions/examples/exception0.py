"""
Course: Exceptions
Topic: View an exception 
Summary: What happens if there is an exception? What do we see?

Takeaways: raising an exception -> happens automatically if not handled.

"""

if __name__ == '__main__':
    """ Catch an IOerror, which includes any time the file doesn't exist.

    """

    # This file doesn't exist, oops!
    filename = "does_not_exist.txt"

    f = open(filename, 'r')
    f.read()

    except IOError as e:
        print( "Error!", e) # we will look at this next example, ignore it for now

    # Demonstrate that the application continues
    print("...")
    print("Continue on with the application...")

