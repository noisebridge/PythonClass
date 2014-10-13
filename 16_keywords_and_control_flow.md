
An Introduction to Keywords and Control Flow



1. What are keywords?

    1. [Keywords](http://en.wikipedia.org/wiki/Reserved_word) are "reserved" by Python for a special use.
        - I have separated Python keywords into three major categories: Control Flow, Comparison, and Specialized.
        - Specialized is further broken down into Classes, Functions, Modules, User Feedback, and Global Effects.
        - Please take these with a grain of salt! This is purely my method of reasoning.
        - Find the code I 





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
