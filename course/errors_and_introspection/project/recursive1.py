"""
"""


def add_one(x):
    """
    """
    _xi = x
    print " "*x + "Going deeper, x={}".format(x)
    if x < 10:
        # import pdb; pdb.set_trace()
        x = add_one(x + 1)
    # base case
    else: # equivalent to x >= 50
        print "The bottom!"

    print " "*_xi + "Getting shallower, original x={}".format(_xi)
    return x
    

x = 1
print add_one(x)

    
