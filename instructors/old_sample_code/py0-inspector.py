"""

Python encourages us to explore what the language can do, and we would be well served by first building a
tool that will allow us to do that exploration.

This tool compares the dir() and getattr() built-in python functions to the getmembers() function in the inspect module.

The result we get for this list is that these things provide the same information, but do they get it in the same way?

Now lets use the inspect.getsource(inspect.getmembers) function to check out the source of the inspect.getmembers() function. What do we find?
AMAZING! It uses the python built-in functions dir() and getattr()!



"""

# We will use the inspect module from the standard library to inspect everything.
import inspect

# Prettyprint is convenient for printing different data structures when dissecting something.
import pprint

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def function_test():
    pass


inspected_alphabet = inspect.getmembers(alphabet)

all_members = dir(alphabet)
all_member_results = []
for each in all_members:
    #    all_members.append( each[0] ) # Take each inspected attribute into a list.
    all_member_results.append( getattr(alphabet, each) ) # Try a getattr() on each inspected attribute.

inspect_getmembers_manual = zip( all_members, all_member_results ) # Zip all the elements into a their getattr()

# We can use a roundabout method to see that inspect.getmembers returns the same thing as getattr()
print
if ( inspected_alphabet == inspect_getmembers_manual ):
    print "True - inspect.getmembers() returns the same result as dir(object) and then a getattr() for each object attribute."
else:
    print "False - inspect.getmembers() does some voodoo or this test is no good!"

print
#prettyprint your manually built inspect inspect.getmembers
pprint.pprint( inspect_getmembers_manual )

print
# Prettyprint the inspect.getmembers result
pprint.pprint( inspected_alphabet )

print
# What do we find?  The inspect.getsource actually uses dir() and getattr() on that dir!
print( "Documentation:", inspect.getdoc( inspect.getmembers ))
print
print inspect.getsource( inspect.getmembers )
