
### Functions Omnibus

A bag of tricks regarding namespace/scope, code blocks, argument un/packing, lambdas (anonymous function), closures, and maybe more.

Today is going to get a little theoretical and you'll find interesting applications for these rules that supplement your other work.



1. ##### Today's deep dive: [Clarifying Scope](https://www.python.org/dev/peps/pep-0227/).

    1. Nesting Functions - How does Python resolve names?
        1. LEGB?  Local, Enclosing, Global, Built-in. Lets use an example:
            ```
            """ Lets see what z is in each scope.

            What will we see for each value of z?
            """

            # 
            z = 15

            def cat():
                """ The cat function is written in main.
                """
                #if you use z in cat, you cannot call it before using it...
                #print("z in cat BEFORE ASSIGNMENT {}".format(z))
                z = 10
                print("z in cat AFTER ASSIGNMENT {}".format(z))

                def cat_helper():
                    """ The cat_helper function is inside of cat only.
                    """
                    #if you use z in cat_helper, you cannot call it before using it...
                    #print("z in cat_helper BEFORE ASSIGNMENT {}".format(z))
                    z = 5
                    print("z in cat_helper AFTER ASSIGNMENT {}".format(z))
                    
                    return
                
                # this is inside of cat
                cat_helper()
                return

            # now we are back in main
            print("z in main {}".format(z))
            
            # lets run cat()... it will run meow() from inside cat()
            cat()
            ```

2. Using `(*args, **kwargs)`:
    1. No discussion topic - see args_kwargs examples.


3. Functions are objects.
    1. What does this really mean? It means we can give them names and pass them around.
        ```
        def addx(b, x):
            """ takes b,x and returns b + x
            """
            return b + x

        def multx(b, x):
            """ takes b,x and returns b * x
            """
            return b * x

        # we can assign the function to a new name, it has 2 names now.
        my_addx = addx

        my_b = 1
        my_x = 2

        print(my_addx(my_b, my_x))
        ```
    2. Ok.. that's nice. Lets do more. Lets put our functions in a list.
        ```
        # continue the last code section
        my_functions = [addx, multx]

        print(my_functions[0](1, 2))
        print(my_functions[1](1, 2))
        ```
    3. Ok lets get weird. These anonymous functions don't have names.
        ```
        # open up a python terminal:
        addx = lambda b, x: b + x
        
        my_functions = [addx, lambda b, x: b * x]

        # lets multiply without the word multx
        print(my_functions[1](b,x))

        ```

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
    1. A [partial](https://docs.python.org/2/library/functools.html#functools.partial) is part of a callable object (generally a function) with a fixed keyword argument or positional argument. This reduces the number of arguments that need to be provided to the function, essentially 'fixing' one argument.
    2. Review the partial example.
    3. Functools also has an update_wrapper function for making a decorator's wrapper look like the wrapped object. Invoked using the @wraps decorator on the function wrapper. 
    4. Review the wraps example.
    5. [the functools.total_ordering decorator](https://docs.python.org/2/library/functools.html#functools.total_ordering) will autogenerate rich comparisons if you specify a single one.  
    6. Finally, reduce is located here in Python 3.



Preparing for this lesson:

This won't guarantee you will be ready for the lesson, but it will serve as a good warm up.

1. Read [Python Scopes and Namespaces](https://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces) 
2. Optional: [Pep 227 - Statically Nested Scopes](http://legacy.python.org/dev/peps/pep-0227/)
3. If you know nothing else, know that python resolves scopes in LEGB order: local, enclosing, global, built-in.
4. [Closure and Decorator Blog Post by Simeon Franklin](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/) of SF Python.
