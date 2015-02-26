"""

Some ideas for more advanced concepts with lambdas.
Each of these examples are separate.  We could also
try to find a way to use lambdas to re-write code in
other lesson plans.

"""

# ----------------------------------------------------------

# Computing a prime number. How does this work?
primes = range(2, 50)
for i in range(2, 8):
    primes = filter(lambda x: x == i or x % i, primes)

print 'Primes:', primes

# ----------------------------------------------------------

# lets say you have a function that needs to be called for any value
# in a long series of 'if' statements. How about generating a lookup
# table of functions instead?
# see: https://developer.mozilla.org/en-US/docs/Mozilla/Localization/Localization_and_Plurals
plural_rules = [
    lambda n: 'all',
    lambda n: 'singular' if n == 1 else 'plural',
    lambda n: 'singular' if 0 <= n <= 1 else 'plural',
    # Option.. could we write more of the rules here?
    # Or replace a lambda expression with a function?
]
# Call plural rule #1 with argument 4 to find out which sentence form to use.
print plural_rules[1](4)  # returns 'plural'

# ----------------------------------------------------------

# functional calls that can be changed on the fly. See OO 'strategy' pattern.
# For example, lets implement a simple action in a lambda function.
roar = lambda x: x + ' roars!'
die = lambda x: x + ' dies!'
action = roar
action("monster")

action = die
action("monster")


# ----------------------------------------------------------

# GUI programming.  Connect a callback function using a lambda...
# This code is from: https://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Strategy

class Button:
    """A very basic button widget."""
    def __init__(self, submit_func, label):
        self.on_submit = submit_func   # Set the strategy function directly
        self.label = label
 
# Create two instances with different strategies
button1 = Button(sum, "Add 'em")
button2 = Button(lambda nums: " ".join(map(str, nums)), "Join 'em")
 
# Test each button
numbers = range(1, 10)   # A list of numbers 1 through 9
print button1.on_submit(numbers)  # displays "45"
print button2.on_submit(numbers)  # displays "1 2 3 4 5 6 7 8 9"


# ----------------------------------------------------------

# Closures can be written with lambdas, since it's not a named function definition.
# These are useful in other languages
# http://en.wikipedia.org/wiki/Closure_(computer_programming)
# nested lambdas...
def compose(f, g):
    def result(x):
        return f(g(x))
    # end result
    return result
# end compose

# Here's an example use:
h = compose(lambda x: x + 2, lambda x: x * x)
print h(3)

# ----------------------------------------------------------

"""
# Lets create a 'macro' that cleans up our code.
# here is some pseudo code taken from the web...
def a_func()
  ...
  if some_conditon:
     ...
     call_some_big_func(arg1, arg2, arg3, arg4...)
  else
     ...
     call_some_big_func(arg1, arg2, arg3, arg4...)

#I replace that with a temp lambda

def a_func()
  ...
  call_big_f = lambda args_that_change: call_some_big_func(arg1, arg2, arg3, args_that_change)
  if some_conditon:
     ...
     call_big_f(argX)
  else
     ...
     call_big_f(argY)
"""