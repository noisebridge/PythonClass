



class myint(int):
    """ Override multiplication from the int class
    """
    pass

    def __mul__(*args):
        return "meow"


#print 5 * 15
print myint(5) * 15 * 10
#print 15 * myint(5)

"""
print myint(5)
print dir(5)
print dir(myint(5))
# Find what attributes are new
for attribute in dir(myint(5)):
    if attribute not in dir(5):
        print attribute
"""


