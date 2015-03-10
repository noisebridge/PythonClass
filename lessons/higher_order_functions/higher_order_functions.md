
### Higher Order Functions

Exploring dynamic argument and keyword quantities, nested functions, higher order functions, closures, and decorators.

If you get behind in this lesson, just keep typing/copying/running code. The topic is hard at first, so if it feels hard, things are going as planned.

1. Nesting Functions - How does Python resolve names?
    _1. LEGB?  Local, Enclosing, Global, Built-in
    _2. Python stops looking when it finds a variable defined. So if it exists in local and global scope, Python will use the local scope.
    _3. See nesting_functions examples


2. Using `(*args, **kwargs)`:
    1. No discussion topic - see args_kwargs examples


3. How to get a nested function to close. Also known as a closure.
    _1. **A what?** A [closure](http://en.wikipedia.org/wiki/Closure_(computer_programming)) - Simple definition: A function that binds a set of 'private' variables.
    _2. **How does this help me write useful code?** 
        __1. Control flow
        __2. Private functions for specific environments
        __3. Passing variables to a function based on the context of the function
    _3. **Why not just put the environment in the global scope?** You could. 
        __1. Security
        __2. compartmentalization
        __3. memory efficiency, code reusability
        __4. Closures are a sophisticated, optional tool


4. Decorators 
    1. [PEP318](https://www.python.org/dev/peps/pep-0318/)
    2. A decorator encloses a method or function. 
    3. [Decorator Reference Syntax](https://docs.python.org/2/reference/compound_stmts.html#function-definitions)
    4. 


5. Functools - What's a partial?
    1. lorem ipsum



Preparing for this lesson:

1. Read [Python Scopes and Namespaces](https://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces) 
2. Optional: [Pep 227 - Statically Nested Scopes](http://legacy.python.org/dev/peps/pep-0227/)
3. If you know nothing else, know that python resolves scopes in LEGB order: local, enclosing, global, built-in.
