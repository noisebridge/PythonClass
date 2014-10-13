
An Introduction to Keywords and Control Flow



1. What are keywords?

    1. [Keywords](http://en.wikipedia.org/wiki/Reserved_word) are "reserved" by Python for a special use.
        - Python keywords are found in the keyword module (>>>print keyword.kwlist):
        - How important is control flow to Python? Pretty important! My breakdown (take w/ grain of salt):
```Python
$ python kw-control.py
There are three categories of keywords:
Control Flow keywords: ['while', 'if', 'elif', 'raise', 'for', 'break', 'continue', 'else', 'pass', 'try', 'except', 'finally', 'with', 'as']
Comparison Keywords ['and', 'in', 'is', 'not', 'or']
Specialized Keywords: ['del', 'assert', 'class', 'def', 'return', 'yield', 'lambda', 'exec', 'import', 'from', 'global', 'print']

Inside Specialized Keywords:
Global level: ['del', 'global']
User Feedback: ['assert', 'print']
Classes: ['class']
Functions ['def', 'return', 'yield', 'lambda']
Module level: ['import', 'from', 'exec']
```
        - The code for this is in the folder for this lesson. Source is keyword module.



