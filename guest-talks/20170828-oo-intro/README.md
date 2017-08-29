# Intro to OOP and Data Structures in Python
This talk will introduce basic object-oriented programming concepts in Python.
Attention will be given to how Python's class system can be used to make custom
data structures that behave nicely with built-in functions.

The Python documentation on this is thorough and mature.
Instead of attempting to give a comprehensive introduction,
this lesson is intended to provide just enough coverage
to get students comfortable with the main ideas behind OOP in Python
within an hour.

Expected outcomes for students:
- Understand basic concepts behind OO in general
- Develop an intuition for the implementation of built-in methods
- Have an easier time reading library code

## Tests
The exercises for this lesson are provided as a small test suite.
To perform the tests, just execute `python -m unittest test_square_grid`
from this directory.

To complete the exercise, edit the class in `square_grid.py`
until all tests pass.

## Classes and Objects
The vocabulary used to describe Object-Oriented Programming (OOP)
varies a bit, but **class** and **object** are used consistently.
The goal of OOP is to attach data to functions that are intended
to operate on that data.

This is accomplished by grouping the needed data,
which we call **attributes**,
with functions that we call **methods**.
Lets look at an example.

We might want to ensure that functions for inserting
into a sorted list might only act on sorted lists.
Instead of writing

```python
sorted_list = [1,3,5,7]
sorted_list = insert_into_sorted_list(sorted_list, 4)
```

we can instead create a class...

```python
class SortedList(list):
    def __init__(self, from_list=None):
        if from_list is not None:
            # Code here ...
        else:
            # etc ...

    def insert(self, x):
        """Override insert to respect ordering."""
        # Code here ...
``` 

...which allows us to write code like this...

```python
l = SortedList([1,3,5,7])
l.insert(4)
l
# => [1,3,4,5,7]
l.insert(1)
# => [1,1,3,4,5,7]
```

In the second block, we created a class with `class SortedList(list):`.
This list also **inherits** all the methods from the `list` class,
which is its **parent class**.
One of these methods is `insert`.
However, we don't want `insert` to work the same way,
as it normally requires an `index` argument - `some_list.insert(2, x)`.
Hence, we **override** the `insert` method to accept a different signature
(without an index)
and to operate with different logic
(choose insertion index based on ordering instead.)

In the third block, we create an **instance**, `l`, of the class.
This instance is an **object**.
There can be many instances of a class, each of which is a distinct object.

**In the talk, we follow up directly with
[the Python documentation](https://docs.python.org/2/tutorial/classes.html#class-objects)
for some concrete examples.**

## Special / Magic / Dunder Methods
In Python, built-in functions like `str` and `len` work by accessing
special methods of the objects passed to them.
These methods are named after the built-in functions themselves,
but bracketed by double-underscores, e.g. `__str__`.
The **d**ouble-**under**score naming convention lead to these being referred to
as **dunder methods**.

Some of these method names are slightly less obvious.
For instance, suppose we wanted to implement addition for two-dimensional vectors.

```python
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        x = self.x + vec.x
        y = self.y + vec.y
        return Vector(x,y)
```

The above allows us to do:
```python
a = Vector(1,2)
b = Vector(3,4)
a.add(b)
# => Vector(4,6)
```

...but wouldn't it be nice to be able to write `a + b` instead of `a.add(b)`?
Good news - we can!

```python
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vec):
        x = self.x + vec.x
        y = self.y + vec.y
        return Vector(x,y)
```
