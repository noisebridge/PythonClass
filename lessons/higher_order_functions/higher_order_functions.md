
### Higher Order Functions

Exploring dynamic argument and keyword quantities, nested functions, higher order functions, closures, and decorators.

If you get behind in this lesson, just keep typing/copying/running code. The topic is hard at first, so if it feels hard, things are going as planned.

1. Nesting Functions - How does Python resolve names?    
    a. LEGB?  Local, Enclosing, Global, Built-in.    
    b. In other words, if Python finds a variable name in a function, then it will stop looking even if the function is in the global scope.    
    c. See nesting_functions examples.    


2. Using `(*args, **kwargs)`:    
    a. No discussion topic - see args_kwargs examples.    


3. How to get a nested function to close. Also known as a closure.    
    a. **A what?** A [closure](http://en.wikipedia.org/wiki/Closure_(computer_programming)) - Simple definition: A function that binds a set of 'private' variables.    
    b. **How does this help me write useful code?**     
        i. Control flow.     
        ii. Private functions for specific environments.     
        iii. Passing variables to a function based on the context of the function.        
    c. **Why not just put the environment in the global scope?** You could.     
        i. Security,     
        ii. compartmentalization,     
        iii. memory efficiency, code reusability.      
        iv. Closures are a sophisticated, optional tool.    


4. Decorators     
    i. lorem ipsum    


5. Functools - What's a partial?    
    i. lorem ipsum    



Preparing for this lesson:

1. Read [Python Scopes and Namespaces](https://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces)     
2. Optional: [Pep 227 - Statically Nested Scopes](http://legacy.python.org/dev/peps/pep-0227/)    
3. If you know nothing else, know that python resolves scopes in LEGB order: local, enclosing, global, built-in.    
