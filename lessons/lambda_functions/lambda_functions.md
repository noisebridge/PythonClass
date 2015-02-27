## Lambda Functions

There are no setup steps since Python 2.7 supports lambdas with the built-in keyword `lambda`.  

### 1. Overview
[Lamdas](https://docs.python.org/2/reference/expressions.html#lambda) are anonymous functions.  They are anonymous since the function doesn't define a name for itself and doesn't use a return statement.  There's actually not much to it.  The useful thing about lamda functions is that they're represented as an object with type 'function'.

This provides the supporting features of a [functional programming language](http://en.wikipedia.org/wiki/Functional_programming).  It has roots in functional programming languages like Lisp and is supported in many popular languages such as Javascript, C++11, C#, Objective-C, Java, closure, etc.

### 2. Why use lambdas?
Well, actually you really don't *need* to in Python. There's an on going debate with people who love and hate it (even a request to remove it from python3 when it was coming out!)  However it may be a natural fit for certain tasks and might be something you would enjoy adding to your toolbox.  It may also be a good skill to translate to other programming languages.

Useful tasks include:
- Simple manipulations of lists and dictionaries.  Lambdas work will with built-in functions:
    1. [filter](https://docs.python.org/2/library/functions.html#filter) for searching lists
    2. [map](https://docs.python.org/2/library/functions.html#map) for converting lists
    3. [reduce](https://docs.python.org/2/library/functions.html#reduce) results in a single output value by summing over each elements in the list
- Callback functions or delayed evaluation, for event driven programming

Some benefits include:
- *Can be* easy to read for simple algorithms
- No inherent state data held in a function.  You can then be sure the lambda function is de-coupled and will always behave the same way when called. (maybe?)
- Used as a 'macro' to hold lists of known parameters.  This could clean up code.
- The joy of learning a new skill with a funny name!

### 3. Why to avoid lambdas?
In most cases lambdas functions can be represented with defined functions or [list comprehension](https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions).  For complicated code it's generally clearer to write out longer procedural code.   Always think of the next poor person who has to read your code!

Lambdas likely won't improve your program's performance.

### 4. More Real World Use Cases

NOTE: See ex3.py

Basic data manipulation we've been doing in class can be done in a different way.  For example, querrying or manipulating a JSON document (dictionary structures).  

Interesting mathmetics, such as procedurally generating prime numbers or other sequences.  

Replacing large code blocks of `if` statements to instead use lambda functions.  These are building blocks for some OO design patterns. For example see [Strategy Design](http://sourcemaking.com/design_patterns/strategy)

Event driven programming makes use of callbacks (ie. delayed execution) Lambdas support passing parameters to these callbacks.

Other ideas?