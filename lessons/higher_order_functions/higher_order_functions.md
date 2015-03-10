
### Higher Order Functions

Exploring dynamic argument and keyword quantities, nested functions, higher order functions, closures, and decorators.

If you get behind in this lesson, just keep typing/copying/running code. The topic is hard at first, so if it feels hard, things are going as planned.

1. Nesting Functions - How does Python resolve names?
    I. LEGB?  Local, Enclosing, Global, Built-in.    
    II. In other words, if Python finds a variable name in a function, then it will stop looking even if the function is in the global scope.    
    III. See nesting_functions examples.    


2. Using `(*args, **kwargs)`:    
    i. No discussion here. Head to the examples for args_kwargs.    


3. How to get a nested function to close. Also known as a closure.    
    i. *A what?* A [closure](http://en.wikipedia.org/wiki/Closure_(computer_programming)) - Simple definition: A function that binds a set of 'private' variables.    
    ii. *How does this help me write useful code?* Control flow. Private functions for specific environments. Passing variables to a function based on the context of the function.    
    iii. *Why not just put the environment in the global scope?* You could. Security, compartmentalization, memory efficiency, code reusability.  Closures are a sophisticated, optional tool.


4. Decorators     
    i. lorem ipsum    


5. Functools - What's a partial?    
    i. lorem ipsum    



Preparing for this lesson:

1. Read [Python Scopes and Namespaces](https://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces)     
2. Optional: [Pep 227 - Statically Nested Scopes](http://legacy.python.org/dev/peps/pep-0227/)    
3. If you know nothing else, know that python resolves scopes in LEGB order: local, enclosing, global, built-in.    
