
Keywords, Structured Programming, and Control Flow


1. [Structured Programming](http://en.wikipedia.org/wiki/Structured_programming)
    
    1. Two base paradigms for programming - [non-structured programming](http://en.wikipedia.org/wiki/Non-structured_programming) and [structured programming](http://en.wikipedia.org/wiki/Structured_programming).
        - Most modern languages are structured.
        - Some non-structured examples I googled: COBOL, Assembly, MUMPS, Basic.
        - Wikipedia claim: Biggest difference is that structured languages disallow the 'goto' statement, which 'jumps' to another place in the code.
        - Structured language introduces keywords like if/then/else(conditional branch) or for/while/with(also conditional branch!).
        - We can see then that Python is a 'structured language'.
        - [Control flow](http://en.wikipedia.org/wiki/Control_flow#Control_structures_in_practice) governs how a language flows through its individual structures.



2. So what are keywords?

    1. [Keywords](http://en.wikipedia.org/wiki/Reserved_word) are "reserved" by Python for a special use.
        - Python keywords are found in the keyword module (>>>print keyword.kwlist):
        - How important is control flow to Python? Pretty important! My breakdown (take w/ grain of salt):
        - (The code for this is in the folder for this lesson. Source is keyword module.)
```Python
$ python kw-control.py 
There are 31 keywords: ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

Lets break them into 3 categories:
Control Flow keywords: ['if', 'elif', 'else', 'while', 'for', 'pass', 'break', 'continue', 'raise', 'try', 'except', 'finally', 'with', 'as']
Comparison Keywords ['and', 'in', 'is', 'not', 'or']
Specialized Keywords: ['del', 'assert', 'class', 'def', 'return', 'yield', 'lambda', 'exec', 'import', 'from', 'global', 'print']

Inside Specialized Keywords:
Namespace: ['del', 'global', 'exec']
Import: ['import', 'from']
User Feedback: ['assert', 'print']
Classes: ['class']
Functions ['def', 'return', 'yield', 'lambda']
```

3. So now we know all the keywords, lets make up some examples for the future. Here are some idefor our examples:

    (lets use our alphabet list from the README.md example along with some list methods)

    1. if/elif/else (pass)
    2. for / (continue) / (break)
    3. while / (break) / (finally)
    4. try / except (raise) / (finally)
    5. with / as

