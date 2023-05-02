"""

Now lets inspect the attributes that we got from inspection!

The test_not_base_reqs works to isolate functions that don't require themselves.

An example of this is the __call__ function for a function. 
But this recursively checks itself and goes to infinite depth. Is call really not a member of itself?

This behavior has stumped me for now. Why isn't __call__ noticing that __call__ has a __call__ attribute?

"""

import inspect
import pprint


def function_test():
    pass

def test_not_base_reqs(obj, depth):
    '''
    Test to see if the attributes of obj contain only 'attributes that require themselves'.
    '''
    not_base_req = []
    
    print
    print obj
    print "ATTRIBUTES:", dir(obj)
    print

    for each in dir(obj):
        if str(each) not in dir(each):
            print "-"*depth + "Attribute: " + each
            if depth > 10:
                print "Depth > 10"
                depth -= 1
                return
            test_not_base_reqs(getattr(obj,each), depth+1)

    depth -= 1
    return

    


f = function_test # now f is defined as function_test. function_test can be called as f()

c = []

test_not_base_reqs(c, 0)

