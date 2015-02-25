### Lambda Functions

There aren't any packages or setup steps. Python 2.7 supports lambdas with the keyword `lambda`.  

## 1. Overview
[Lamdas](https://docs.python.org/2/reference/expressions.html#lambda) are anonymous functions.  Anonymous means that the function doesn't define a name for itself.  Also lambdas do not use a return statement.  They can be used as an alternative to defining a function, where a data object instead represents a function.

This provides the supporting features of a [functional programming language](http://en.wikipedia.org/wiki/Functional_programming).  It has roots in functional programming languages like Lisp and is gaining popularity with support in C++11 and other languages (TBD)

## 2. Why use lambdas?
Well, actually you really don't *need* to. It's an on going debate with people who love and hate it (even eith requests to remove it from python!)  However it may be a natural fit for certain tasks and might be something you would enjoy adding to your tool bag.  If you use closures or other event driven languages

These tasks include:
- Simple manipulations of lists and dictionaries.  Lambdas work will with built-in functions:
    1.[filter](https://docs.python.org/2/library/functions.html#filter) for searching lists
    2.[map](https://docs.python.org/2/library/functions.html#map) for converting lists
    3.[reduce](https://docs.python.org/2/library/functions.html#reduce) results in a single output value by summing over each elements in the list
- Callback functions or delayed evaluation


Some benefits include:
- *Can be* easy to read for simple algorithms
- No inherent state data held in a function.  You can then be sure the lambda function is de-coupled and will always behave the same. (maybe?)
- Used as a 'macro' to hold lists of known parameters.  This could clean up code.
- The joy of learning a new skill with a funny name!

## 3. Why to avoid lambdas?
In most cases lambdas functions can be represented with defined functions or list comprehension.  For complicated code it's clearer to write out longer procedural code.   Always think of the next poor person who has to read your code!

Lambdas likely won't improve your program's performance.

## 4. More Real World Use Cases

See ex3.py for code regarding:

Basic data manipulation we've been doing in class can be done in a different way.  For example, querrying or manipulating a JSON document (dictionary structures).  Or generating prime numbers.  

Replacing large code blocks of `if` statements to instead use lambda functions.  These are building blocks for some OO design patterns. For example see [Strategy Design](http://sourcemaking.com/design_patterns/strategy)

Event driven programming makes use of callbacks (ie. delayed execution) Lambdas support passing parameters to these callbacks.

Other ideas?