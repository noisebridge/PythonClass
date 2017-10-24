Reading:
    https://github.com/rmsadik/x/blob/master/CleanCode/Clean%20Code.pdf
    Clean code page 31-37 (up to switch statement)
    39-47 (starting from Use Descriptive Names, to Error.java)
    49 (just Conclusion)
    It's written for java but most of the principles apply to python, and is the best treatment of the subject I've seen



in the beginning:
    there was goto and it made spaghetti code
        - no way to tell which variables it was affecting
        - start/ends are really unclear
        - code was really confusing


then there was light:
    the 'function'
        - defined parameters
        - defined result
        - defined name
        - the notion of 'side effects'



Theory of functions/ The Aesthetic of functions (Summary of the reading)
    A function should do ONE THING
    The function should have a legible name (usually a verb, sometimes a question for bools)
    the function should be a single level of abstraction - the one level beneath the name
    A function should be short
    A function should be EVEN SHORTER
    A function should be designed to be read by a human
    minimum number of arguments
    avoid having unexpected side effects



Functions in python:
    - Functions in python are the primary tool python gives to control code execution (classes control data representation)

```
    def swap(x, y):
        tmp = array[x]
        array[x] = array[y]
        array[y] = tmp
```
    def declares a new function. after the def block is executed, there will be a new python object in scope that has the name of the function. That's a python object that you can manipulate, pass to other functions, etc.

    function name should be a verb or a question, and should explain exactly what the function does so you won't be surprised.

    arguments - have as few as possible, each one adds combinatorial complexity
        positional arguments
        keyword arguments
        *args
        **kwargs

    function should do one thing, can call other functions, can even define other functions within.

    return OR raise exception.

    Should you do side effects ? (unexpected changes to other systems)



    Deeper dive:
        - Scope: How do variables that aren't arguments work?
            know that python resolves scopes in LEGB order: local, enclosing, global, built-in.
        - Functions as arguments:
        Map:

        def map(func, sequence):
            result = []
            for item in sequence:
                result.append(func(item))
            return result

        let's write Filter!

        You can write nice code by composing functions like this, this is called a 'functional' style, as opposed to an imperitive style.

        - Lambda:
            lambda x: x*2
        - Decorators
            @memoize / @cached
        - Functools
            -partial
