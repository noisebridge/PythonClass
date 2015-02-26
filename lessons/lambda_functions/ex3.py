# Computing a prime number. How does this work?
primes = range(2, 50)
for i in range(2, 8):
    primes = filter(lambda x: x == i or x % i, primes)

print 'Primes:', primes


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


# functional calls that can be changed on the fly. See OO 'strategy' pattern.
# For example, lets re-define the logging class. Note that sys.stdout.write
# evaluates as an expression, whereas 'print' is a statement.
import sys
log_info = lambda x: sys.stdout.write('log: ' + str(x) + '\n')
log_debug = lambda x: sys.stdout.write('debug: ' + str(x) + '\n')
s = log_debug
s("World")
s = log_info
s('world')

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

"""
# GUI programming.  Connect a callback function using a lambda...
# Connecting up signals in PyQt applications, like this:
w = PyQt4.QtGui.QLineEdit()
w.textChanged.connect(lambda event: dothing())

#Just calling w.textChanged.connect(dothing) would call the dothing method
#with an extra event argument and cause an error..

#Using the lambda means we can tidily drop the argument without having to
#define a wrapping function

"""
