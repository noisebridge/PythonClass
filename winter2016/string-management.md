

#### String Management - processing strings and extracting information

This lesson covers some topics related to strings in Python. In particular: encoding, string management, built-in methods, iterating over strings, substring search, and immutability (concept: immutable type).


1. ##### Today's deep dive: dissecting a string (10 minutes)

    ```python
    # Do this in the console so you can see the difference!

    mystring = "hello world"

    # what are we seeing here?
    dir(mystring)

    # lets try using some methods...
    mystring.upper()
    # did that permanently change the string?
    mystring.title()
    # how about that? Why did we get the result we did?
    
    # now lets coerce something else into a string
    mynumber = 1001001
    my_coerced_string = str(mynumber)
    # number and string are similar enough that python can have regular rules to do this
    # if you wanted to follow different rules, you could write them yourself
    ```



2. ##### String Encoding! ascii or utf-8?
    1. First off, what are they?
        1. ascii - this is a 1:1 encoding of bytes to characters, it can only represent the english letters and some additional stuff.
        2. unicode - this is a huge set of characters representing many languages. Not all fonts support all sections of unicode. Unicode costs between 1-4 bytes per character.
    2. So what does Python use in the Python interpreter?
        1. Python 2 uses ascii for strings, but has unicode strings available if you choose to use them.
        2. Python 3 uses unicode by default, so you never have to think about it.
        3. You can identify a unicode string because it will look like this: u'hello world'.
        4. How do you know if you are using Python 2 or 3? When you type the python command, you have to type `python3` to use Python 3 on most systems.
    3. What about your source code file, does that have to be ascii or unicode? [Lets check PEP 263](https://www.python.org/dev/peps/pep-0263/)
        1. The Python 2 interpreter defaults to decoding a source code file (a script) as ascii.
        2. In order to use a different encoding you need to specify it:
            1. emacs-friendly: `# -*- coding: utf-8 -*-`
            2. vim-friendly:`# vim: set fileencoding=utf-8 :`
            3. Precise definition from PEP 263: encoding must match the regular expression `"coding[:=]\s*([-\w.]+)"`
            4. you could use human friendly: `# this file uses the encoding: utf-8`
        3. What about Python 3?
            1. Python 3 uses utf-8 [as the default file coding](https://docs.python.org/3.3/howto/unicode.html#the-string-type)
            2. PEP 263 still applies to Python 3.
    4. Lets use Python 2 - Three types of string declarations:
        1. ascii = 'this is a string'
        2. unicode = u'this is a unicode string'
        3. raw = r'this needs no escapes'
    5. String escapes - a string will often need escapes.
        1.  Let's play with [escape sequences!](https://docs.python.org/2/reference/lexical_analysis.html#string-literals)
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
    

    2. Now lets slice a string.
        1. [Reference documentation](https://docs.python.org/2/reference/expressions.html#slicings)
        2. [Slice Tutorial](https://docs.python.org/2/tutorial/introduction.html#strings)

    3. Substring Search - find a string that fits inside another string.
        1. How many instances of 'is' are in 'this is my string'?
        2. Lets work with some more string methods.
            1. find(), rfind(), 
            2. count()
            3. partition(), rpartition()
            4. split()

    4. Iterating over a list of strings:
        1. Again, we use the for... in pattern:

    5. Regular Expressions - a definition, you should know they exist and try them out.
        1. Regular expressions are strings that can match a set of regular strings.
            1. There's a lot to say about these
            2. Check out the Python `re` library
