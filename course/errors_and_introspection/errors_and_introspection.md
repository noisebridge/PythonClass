

#### Errors and Introspection

Tonight will cover a lot of topics. We'll start by messing with the dir() and help() commands. Then we'll view the standard library errors, catch a few in our control flow with try/except. Next we'll play briefly with inspect, timeit, and finally trace errors with pdb.


0. #### Installation and Class Prep 
    1. Installation Instructions:
        1. You only need the Python Standard Library
    2. Class Prep Resources:
        1. Optional: Review the lesson materials below.


1. #### Today's deep dive: Lets look at the guts of a list and a dict.

    ```python
    in_a_list = dir(list())
    in_a_dict = dir(dict())

    only_in_a_list = []
    for attribute in in_a_list:
        if attribute not in in_a_dict:
            only_in_a_list.append(attribute)
            
    only_in_a_dict = []
    for attribute in in_a_dict:
        if attribute not in in_a_list:
            only_in_a_dict.append(attribute)

    print 
    print "Things in a list but not a dict: {}".format(only_in_a_list)
    print
    print "Things in a dict but not a list: {}".format(only_in_a_dict)
    print
    
    ```

    1. First lets look at the contents of dir(list()) and dir(dict()) - 3 minutes
        1. Note that there are a lot of similar things, and a number of dissimilar things
        2. Example 1: dicts have keys but obviously lists have no use for taht
        3. Example 2: lists have __<slice>__ builtins for slicing. Dicts don't but why? (hint: are they ordered?)


2. #### So we just covered a bit about dir, but what is dir?
    1. Lets learn about the help() method - 15 minutes
        1. Obvious thing to do:  >>> help(dir)
        2. Help often provides really terse information.
        3. If you call help on your own function, you'll get a nicely formatted output of the function's docstring and accepted arguments.
        4. [help() details](https://docs.python.org/2/library/functions.html#help)

3. #### Next up: [timeit](https://docs.python.org/2/library/timeit.html)
    1. Ok, so you want to know how long your code takes... - XX minutes
        1. First off, `import timeit`
        2. Lets take a look at the sample code in `timeit.py`


4. ####  PDB / stack trace - part of the [debugging suite](https://docs.python.org/2/library/debug.html)
    1. From the [pdb docs](https://docs.python.org/2/library/pdb.html): When invoked as a script, pdb will automatically enter post-mortem debugging if the program being debugged exits abnormally. After post-mortem debugging (or after normal exit of the program), pdb will restart the program. Automatic restarting preserves pdb’s state (such as breakpoints) and in most cases is more useful than quitting the debugger upon program’s exit.
        1. Lets not get too far into defining what it is, lets just try it out.
        2. There are two main ways to use pdb below.
    2. Method One: `python -m pdb success.py`
        1. Used when you want to step through your whole script/app.
        2. Lets use the command step to go through success.py with pdb.
        3. Now lets do this same thing with `fail.py` and compare.
    3. Method Two: `import pdb; pdb.set_trace()`
        1. This puts an arbitrary stack trace in your actual script.
        2. But wait, what's a '[stack trace](https://en.wikipedia.org/wiki/Stack_trace)'?
        3. Wikipedia is way more info than we wanted! A stack trace is what you see when you have an exception. It's a list of all the layers of code where the exception appeared.
    4. Once you enter pdb, you can use [these commands](https://docs.python.org/2/library/pdb.html#debugger-commands) at the (pdb) prompt.
        1. Abbreviations for these commands are listed in parentheses.
        2. Entering a blank line repeats the last command entered.
        3. We can focus on three commands now, (l)ist, (n)ext, (c)ontinue
            1. list - print the command where you are in the application but only once...
            2. next - execute the next line
            3. continue - run lines until 'something happens' which triggers pdb


5. #### Lab Primer - not used TAR 061515
    1. What to cover in a lab session
    2. What can we do with concepts learned? - XX minutes   
    3. What are some real world applications?    
    4. How to prep until then


6. #### Extended Resources - not used TAR 061515
    1.
