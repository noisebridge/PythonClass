

#### String Management - processing strings and extracting information

We'll be writing an algorithm tonight that describes the 'phone book' search method, a way of quickly searching a list of items for a specific item.

This is an 'algorithm' which is a long word for 'way of doing things'.

Other things that are algorithms: tying your shoes, addition, making an omelet.



1. ##### Today's deep dive: functions and scope

    ```python
    """ Lets learn a bit about functions and 'scope'
    """
    
    # you can use lowercase, but globals as all caps can help differentiate.
    THIS_IS_A_GLOBAL_VARIABLE = "is this available in the function?"

    def add_a_number(source_number, number_to_add):
        """ This function allows us to add whatever we pass it
        """
        result = source_number + number_to_add
        
        print "Viewing: {}".format(THIS_IS_A_GLOBAL_VARIABLE)

        return result

    first_number = 100
    second_number = 10
    returned_from_the_function = add_a_number(first_number, second_number)
    print "Result of {} + {}: {}".format(first_number, second_number, returned_from_the_function)
    ```

    1. What is this tricky scope concept?
        1. It determines what you can see from your location in your code. 
        2. Remember: a name/variable is just a 'name' assigned to ANY object.

    2. Some scope guidelines:
        3. Globally defined (no indentation) names can be seen from anywhere.
        4. Names defined in a function or class can not be seen except in functions or classes (or modules) that are children of that class.
        5. This means scope can be thought of like a tree with global as the roots.
        6. Pitfall: a name cannot be used before it is defined. The code runs one line at a time.



2. ##### What are we even doing? Lets set up our phone book search:
    
    1. Some things we need:
        1. Data to search through. It must be sorted. Why?
        2. A description of how our search will operate.
        3. A value to search for. Lets arbitrarily start with the 57th index value (of 100).

    2. DATA SET (REQUIREMENT 1)
        1. First we need data. Lets make a [random list](https://docs.python.org/2/library/random.html#random.sample) of 100 items between the numbers 1 to one million.
        ```python
        import random

        # if we do this we can probably all get the same list        
        random.seed(99)

        mynumbers = random.sample(1000000, 100)

        print mynumbers[0:10]
        print mynumbers.sort()[0:10]
        print mynumbers[0:10]

        our_dataset = mynumbers.sort()
        ```

    3. Description of our search algorithm (REQUIREMENT 2)
        1. What is a phone book search?
            1. Open a phonebook half way.
            2. If the first letters of the last name you are searching for is before your location, open the book up in the middle of the first half. Otherwise open to the middle of the second half.
            3. Repeat 2 until you are on the right page.
            4. When on the same page, you can repeat this with the actual values.





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
