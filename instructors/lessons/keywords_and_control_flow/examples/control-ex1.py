"""
Control Flow keywords: ['while', 'if', 'elif', 'raise', 'for', 'break', 'continue', 'else', 'pass', 'try', 'except', 'finally', 'with', 'as']
Comparison Keywords ['and', 'in', 'is', 'not', 'or']
"""

letter_frequency_dict = {}
word = "noisebridge"

for letter in word:
    times = letter_frequency_dict.get(letter, 0)
    times += 1
    letter_frequency_dict[letter] = times
print letter_frequency_dict
print letter_frequency_dict.keys()

# This is a list
unique_ltrs = letter_frequency_dict.keys()

# Also feel free to use letter_frequency_dict

"""
i = 0
while i < len(unique_ltrs):
    print i, unique_ltrs[i]
    print str(i) + unique_ltrs[i] # Also can print without a space.
    i += 1


i = 0
for spaghetti in unique_ltrs:
    print spaghetti, letter_frequency_dict[spaghetti]
    i = i + 1  # same as i += 1
    print "Lets go to loop number %s" % i


for i, spaghetti in enumerate(unique_ltrs):
    print i, spaghetti

    if spaghetti == 'n':
        print "n is the best letter!"
    elif spaghetti == 'x':
        print "YOU MISSPELLED NOISEBRIDGEQ"
    elif spaghetti == 'o':
        print "There is no o in team."
    elif spaghetti == 'o':
        print "You unlocked the extra secret level."
    elif spaghetti == 'n':
        print "You unlocked the secret level"
    else:
        print "You didn't put a special phrase in for %s" % spaghetti
print "And you are now out of letters."

for i, spaghetti in enumerate(unique_ltrs):
    if spaghetti == 'b':
        continue
    else:
        print "%sth letter: %s" % (i, spaghetti)

print
print

for i, spaghetti in enumerate(unique_ltrs):
    
    print "%sth letter: %s" % (i, spaghetti)
    
    if spaghetti == 'o':
        print "Uh oh, spaghetti==o..."
        # Breaks only the innermost for or while loop.
        break
print "That's the end of the example..."



for ltr in unique_ltrs:
    for ltr2 in unique_ltrs:
        print ltr, ltr2
        if ltr2 == "o":
            print "Uh oh, spaghetti==o"
            break

for ltr in unique_ltrs:
    for ltr2 in unique_ltrs:
        print ltr, ltr2
        if ltr == "o":
            print "Uh oh, spaghetti==o"
            break

    if ltr == "b":
        break

for i in range(10):
    for j in range(10):
        print i,j

    print "That was the %s external block." % i

"""
import sys
class rangetype(object):

    def __init__(self, rangelength):
        self.rangelength = rangelength

    def __repr__(self):
        print range(self.rangelength)

    def __enter__(self):
        """ This is passed to the with block as the variable.
        """
        return range(self.rangelength)

    def __exit__(self, *exc_args):
        """ Any true value for return ignores exceptions.
            Returning none should re-raise any exception from the block.
        """
        return

# getsocrata could use a context manager: https://docs.python.org/3.4/library/contextlib.html#replacing-any-use-of-try-finally-and-flag-variables

# The contextlib module provides some functions and a decorator that are useful when writing objects for use with the 'with' statement.
# https://docs.python.org/2/whatsnew/2.6.html#the-contextlib-module
def do_something():
    
    print type(rangetype(5))
    return rangetype(5)

with do_something() as example:
    print type(example), example


import contextlib
@contextlib.contextmanager
def do_something_else(name):
    
    # Put enter stuff here...
    print "Setup occurs on '%s'..." % name
    
    # The code block will run on this 'as <name>'
    try:
        yield name
    except AttributeError as e:
        print e
        pass
    # Put exit stuff here...
    else:
        pass

    return

test_name_container = ['dog', ['trent', 'cat'], 'meow']

# Using a context manager here would be silly in practice.
# This is because all the boilerplate is still in the control loops
# shown below.
prev_names = []
for test_name in test_name_container:
    with do_something_else(test_name) as name:
        prev_names.append(name.capitalize())
    print prev_names

    # there's a bug here, a string can be iterated on.
    # to fix the bug, break out of this with for strings
    with do_something_else(test_name) as name:
        for each in name:
            prev_names.append(each.capitalize())
    print prev_names


