"""
This isn't a script, here's the first way to run pdb:

    $ python -m pdb myscript.py

From our PDB docs:
    When invoked as a script, pdb will automatically enter post-mortem debugging if the program being debugged exits abnormally. After post-mortem debugging (or after normal exit of the program), pdb will restart the program. Automatic restarting preserves pdb’s state (such as breakpoints) and in most cases is more useful than quitting the debugger upon program’s exit.

Once you enter pdb this way, you can use these commands at the (pdb) prompt:
    https://docs.python.org/2/library/pdb.html#debugger-commands
    Abbreviations for these commands are listed in parentheses.
    Entering a blank line repeats the last command entered.

========================================

So lets start with a working application, success.py:

    $ python -m pdb success.py

Run this inline stack trace module, try out these commands:

    help
    help where
    where
    step
    [hit enter to repeat step many times]

You should recognize that your application is looping and failing.

========================================

Next lets look at a failing application, fail.py:

    $ python -m pdb fail.py

Lets just use step for now:

    step
    [hit enter to repeat step many times]

========================================

Ok, so how do we use this in our application if we want to inspect an area that isn't necessarily throwing an error?

    Add this LOC (line of code) to your script:
    >>> import pdb; pdb.set_trace()

We can focus on three commands now, (l)ist, (n)ext, (c)ontinue
    list - print the command where you are in the application but only once...
    next - execute the next line
    continue - run lines until 'something happens' which triggers pdb





"""

