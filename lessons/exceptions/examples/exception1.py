"""
Course: Exceptions
Topic:  try... except
Summary: Lets catch a simple problem.

Takeaways: If we have an issue, the application can handle the issue and keep going. Voila!

"""

if __name__ == '__main__':
    """ Catch an IOerror, which includes any time the file doesn't exist.

    """

    # This file doesn't exist, oops!
    filename = "does_not_exist.txt"

    try:
        f = open(filename, 'r')
        f.read()

    except IOError as e:
        print "Error!", e # we will look at this next example, ignore it for now


    # Demonstrate that the application continues
    print "..."
    print "Continue on with the application..."

