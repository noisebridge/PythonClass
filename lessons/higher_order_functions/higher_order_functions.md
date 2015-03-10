
### Higher Order Functions

Exploring dynamic argument and keyword quantities, nested functions, higher order functions, closures, and decorators.

If you get behind during this lesson, just keep typing/copying/running code. The topic is hard at first, so if it feels hard, things are going as planned.

1. Nesting Functions - How does Python resolve names?
    1. LEGB?  Local, Enclosing, Global, Built-in
    2. In other words, if Python finds a variable name in a function, then it will stop looking even if the function is in the global scope
    3. See nesting_functions examples


2. Using `(*args, **kwargs)`:
    1. No discussion topic - see args_kwargs examples.


3. How to get a nested function to close. Also known as a closure.
    1. **A what?** A [closure](http://en.wikipedia.org/wiki/Closure_(computer_programming)) - Simple definition: A function that binds a set of 'private' variables.
    2. **How does this help me write useful code?** 
        1. Control flow
        2. Private functions for specific environments
        3. Passing variables to a function based on the context of the function
    3. **Why not just put the environment in the global scope?** You could. 
        1. Security 
        2. compartmentalization
        3. memory efficiency, code reusability
        4. Closures are a sophisticated, optional tool


4. Decorators - Forget everything about the @ symbol for now.
    1. A decorator is a callable object that wraps around another callable object. Often a function that wraps around a function.
    2. The decorator must return a callable object, usually a function.
    3. A decorator is used to add functionality to the original function. Also called enhancement.
    4. If you have used chaining in other functions, it is a very similar idea. Chains of functions run on each others output from the inside out. Decorators are also wrapped and executed from the inside out.
    5. Example time. Head over to decorator1.py and continue through all the decorator examples.


5. Functools - What's a partial?
    1. lorem ipsum



Preparing for this lesson:

1. Read [Python Scopes and Namespaces](https://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces) 
2. Optional: [Pep 227 - Statically Nested Scopes](http://legacy.python.org/dev/peps/pep-0227/)
3. If you know nothing else, know that python resolves scopes in LEGB order: local, enclosing, global, built-in.
4. [Closure and Decorator Blog Post by Simeon Franklin](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/) of SF Python.
