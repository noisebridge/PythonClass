
#GUI programming.  Connect a callback function with a lambda...
for value in ["one","two","three"]:
    b = tk.Button(label=value, command=lambda arg=value: my_callback(arg))
    b.pack()

#or: There are a few cases where lambda is useful, for example it's often convenient when connecting up signals in PyQt applications, like this:

w = PyQt4.QtGui.QLineEdit()
w.textChanged.connect(lambda event: dothing())
#Just calling w.textChanged.connect(dothing) would call the dothing method 
#with an extra event argument and cause an error.. 
#Using the lambda means we can tidily drop the argument without having to define a wrapping function


#lets say you have a function that needs to be called for any value in a switch statement...
#how about using this instead?
#see: https://developer.mozilla.org/en-US/docs/Mozilla/Localization/Localization_and_Plurals
plural_rules = [
    lambda n: 'all',
    lambda n: 'singular' if n == 1 else 'plural',
    lambda n: 'singular' if 0 <= n <= 1 else 'plural',
    ...
]
# Call plural rule #1 with argument 4 to find out which sentence form to use.
plural_rule[1](4) # returns 'plural'


# Closures can be written with lambdas, since it's not a named function definition.=
# These are useful in other languages
# http://en.wikipedia.org/wiki/Closure_(computer_programming)
#nested lambdas...
def compose(f, g) :
    def result(x) :
        return f(g(x))
    #end result
    return result
#end compose
and here’s an example use:

>>> h = compose(lambda x : x + 2, lambda x : x * x)
>>> h(3)
11

# functional calls that can be changed on the fly..
i = lambda x: print 'log', (x)
d = lambda x: print 'debug', (x)
s = i
s("World")
s = d
s('world')
