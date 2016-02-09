

#### String Management - processing strings and extracting information

This lesson covers some topics related to strings in Python. In particular: encoding, string management, built-in methods, iterating over strings, substring search, and immutability (concept: immutable type).


1. ##### Today's deep dive: dissecting a string (10 minutes)

    ```python
    # Do this in the console so you can see the difference!

    mystring = "hello world"

    dir(mystring)
    

    mynumber = 1001001
    my_coerced_string = str(mynumber)

    ```

    ```python
    >>> mynumber
    >>> mynumber.__repr__()
    >>> my_coerced_string
    >>> my_coerced_string.__repr__()

    >>> help(mynumber.__repr__()
    ```
    

    1. What is going on here? - 3 minutes
        1. What is the __repr__ method?


2. ##### String Encoding! ascii or utf-8?
    1. First off, what are they?
    2. ascii - this is a 1:1 encoding of bytes to characters, it can only represent the english letters and some additional stuff.
    3. unicode - this is a huge set of characters representing many languages. Not all fonts support all sections of unicode. Unicode costs between 1-4 bytes per character.
    4. So what does Python use?
        1. Python 2 uses ascii
        2. Python 3 uses unicode
        3. You can identify a unicode string because it will look like this: u'hello world'.
        4. How do you know if you are using Python 2 or 3? When you type the python command, you have to type `python3` to use Python 3 on most systems.
    5. Lets use Python 2 - Three types of string declarations:
        1. ascii = 'this is a string'
        2. unicode = u'this is a unicode string'
        3. raw = r'this needs no escapes'
    6. String escapes - a string will often need escapes.
        ```python
        >>> 'hello world'
        >>> 'hello humans\' world'
        >>> '\\'
        >>> r'\\'
        >>> '\\\\'
        ```

3. ##### Lets play with some strings.

    1. First lets look inside a string
        1. Lets use the dir built-in method.
        ```python
        >>> mystring = "this is my string"
        >>> help(dir)
        >>> dir(mystring)
        ```
        2. These things are string methods. [Lets look at some](https://docs.python.org/2/library/stdtypes.html#string-methods)
            1. lower(), capitalize(), title()
            2. find(), rfind(), count()
            3. partition(), rpartition(), split()
    

    2. Now lets slice a string.
        1. [Reference documentation](https://docs.python.org/2/reference/expressions.html#slicings)
        2. [Slice Tutorial](https://docs.python.org/2/tutorial/introduction.html#strings)

    3. Substring search:
        1. The easy way:
            1. `for mystr in bigstring: pass`

    4. Iterating over a list of strings:
        1. Again, we use the for... in pattern:
            ```python

            ```

    5. Regular Expressions.
        1. Lets see if we get to this.
            ```python

            ```
