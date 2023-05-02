import inspect
import pprint






class CatMaker( int ):
    """
    This catmaker class will change the __div__ function to the meow function.
    """


    def __div__(self, other):
        """
        Replace division with a "Meow!"
        """ 

        return "Meow"
        """
        try: 
            getattr(other, '__div__' )
            return getattr(other, '__div__')
        except:
            return "Other has no attribute '__div__'."
        """ 

def meow_tester():

    meow1 = int(5)
    meow2 = CatMaker(5)

    print
    print "These attr are in 5 but not in Catmaker(5)"
    for each in dir(meow1):
        if each not in dir(meow2):
            print each

    print
    print "These attr are in CatMaker(5) but not in 5."
    for each in dir(meow2):
        if each not in dir(meow1):
            print each

