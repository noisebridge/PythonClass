

Course 4 - Built-in Types and String Services


Resources:


[Python Standard Library Chapter 7 - String Services](https://docs.python.org/2/library/strings.html)

1. Built-in types - [Python Standard Library Chapter 5 - Built-in Types](https://docs.python.org/2/library/stdtypes.html)    
  a. What is a type? A container for information in Python. Lets avoid a more strict definition [because the topic is very detailed](http://en.wikipedia.org/wiki/Type_system).    
  b. Principal builtin types are numerics, sequences, mappings, files, classes, instances and exceptions.    
  c. We often think of data types when we consider types. [Python Standard Lirary 8.15 - Data Types](https://docs.python.org/2/library/datatypes.html)    
  d. However, functions, iterators, sequences, file objects, modules, and pretty much everything else is a type. I don't really know where this definition ends. I know some builtin functions are in C and keywords probably aren't types.     
  e.     


2. Lets dig into some practical types - Numeric, Mapping, Iterator, Sequence, Set, File Objects    
  a. Numeric - int, float, long, complex.    
  b. Also check out [Python Standard Library Chapter 9](https://docs.python.org/2/library/numeric.html)    
  c. Mapping (container) - Only built-in mapping is the dictionary.    
  d. set/frozenset (container) - Mutable and immutable respectively. Unordered, hashable. Has some nice built-ins.    
  e. Iterator - Containers have this. __iter__() object supports the 'for' and 'in' statements. next() returns the next item from the container and raises StopIteration forever if all items are exhausted.    
  f. Note that generators are a possible implementation of iterators but not the only one.     
  g. Sequence - Also supports iteration methods. Str, unicode, list, tuple, butearray, buffer, xrange. This list is HUGE!    
    1. [String Methods](https://docs.python.org/2/library/stdtypes.html#string-methods)    
    2. [String Formatting Operations](https://docs.python.org/2/library/stdtypes.html#string-methods)    
    3. [Helpful Table of Mutable Sequence Type Operations](https://docs.python.org/2/library/stdtypes.html#mutable-sequence-types)    
    4. [Unicode object](https://docs.python.org/2/library/functions.html#unicode)    
  
  h. File Objects - [Files have a lot of methods available](https://docs.python.org/2/library/stdtypes.html#file-objects)     
  i. [Almost everything else you can imagine](https://docs.python.org/2/library/stdtypes.html#other-built-in-types)    
