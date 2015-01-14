

def inspect_diff(object_1, object_2):
    """ Use inspect to differentiate python built-in types.

    """


    print str(object_1) + ":"
    for value in dir(object_1):
        if value not in dir(object_2):
            print value

    print

    print str(object_2) + ":"
    for value in dir(object_2):
        if value not in dir(object_1):
            print value


