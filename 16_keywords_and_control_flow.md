
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

14 Control Flow keywords: ['if', 'elif', 'else', 'while', 'for', 'pass', 'break', 'continue', 'raise', 'try', 'except', 'finally', 'with', 'as']

5 Comparison Keywords: ['and', 'in', 'is', 'not', 'or']

12 Specialized Keywords: ['del', 'assert', 'class', 'def', 'return', 'yield', 'lambda', 'exec', 'import', 'from', 'global', 'print']

Inside Specialized Keywords:
Namespace: ['del', 'global', 'exec']
Import: ['import', 'from']
User Feedback: ['assert', 'print']
Classes: ['class']
Functions ['def', 'return', 'yield', 'lambda']
```

3. This gives us a really top-down view of keywords in Python.
    1. One really obvious result: control flow + comparison = 19/31 keywords.
    2. In other words, over half the keywords are dedicated to control flow, and the other half are very sparse and independent of each other.
    3. Control flow must be REALLY SUPER IMPORTANT to have this large a share of the parser.    
    4. FYI: Python Builtin Environment ~~ dir(__builtins__) + [tokens](https://docs.python.org/2/reference/lexical_analysis.html#)
    5. Lets go through the examples in the folder for control (while/for/if etc.)
