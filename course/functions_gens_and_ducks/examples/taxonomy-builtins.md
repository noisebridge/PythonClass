##introspective
dir()
help()
id() #This is the address of the object in memory
type()
locals()
globals()
repr()

#numbers
int()
float()
long()
round(number)
complex()

#conversion only, mostly for numbers
abs(x)
bin(x)
hex(x)
oct(x)

##additional math helpers
cmp(x,y) # x and y are ints
hash()

#string convert
str()
chr(st)
unichr(i)
unicode(object='')

##string services
format(value)

#iterables
list()
dict()
set()
tuple()
frozenset()

##iteration helpers
len()
range()
xrange()
enumerate(sequence)
sorted(iterable)
reversed(sequence)
zip()
any(iterable)
all(iterable)
iter(o)
max(iterable)
min(iterable)
sum(iterable)
slice(stop)
next(iterator)

##functional - used on iterables
filter(function, iterable)
map(function, iterable)
reduce(function, iterable)

##class-based
classmethod()
staticmethod()
getattr()
delattr()
hasattr()
isinstance()
issubclass()
property()
super(type)
var()

##file handlers
open(name)
reload(file)
file(name)

##input
raw_input()
input()

##special
memoryview()
import

#type testing or inheritance
basestring()
callable(object)
object()

##probably never use
-eval
-execfile

##non-essential Built-ins
look at bottom of docs and never use