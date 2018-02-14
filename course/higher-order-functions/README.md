# Reading:

https://github.com/rmsadik/x/blob/master/CleanCode/Clean%20Code.pdf
Clean code:

 - page 31-37 (up to switch statement)
 - 39-47 (starting from Use Descriptive Names, to Error.java)
 - 49 (just Conclusion)

It's written for java but most of the principles apply to python, and is the best treatment of the subject I've seen.

*I'm recommending this reading because I think it's very valuable*
*Do this before or after class*


# Class

## in the beginning there was *GOTO*
 - and it made spaghetti code
 - no way to tell which variables it was affecting
 - start/ends are really unclear
 - code was really confusing


## then there was light: the 'function'
 - definite parameters 
 - defined name
 - definite result
 - definite entry/exit points
 - they have their own local scope 
 - the notion of 'side effects' (acting >>> scope)
 These are all different from GOTO and they contribute to the beauty of functions, that they're modular, composable units of execution. 


## Theory of functions/ The Aesthetic of functions (Summary of the reading)
 - A function should do ONE THING
 - The function should have a legible name (usually a verb, sometimes a question for bools)
 - the function should be a single level of abstraction - the one level beneath the name
 - A function should be short
 - A function should be EVEN SHORTER
 - A function should be designed to be read by a human
 - minimum number of arguments
 - avoid having unexpected side effects



## Functions in python:
  Functions in Python are the primary tool to control code execution (classes control data representation)

  Example Function:
        
        def add(a, b):
            return a + b
        
        def swap(x, y):
            tmp = array[x]
            array[x] = array[y]
            array[y] = tmp

  def declares a new function. after the def block is executed, there will be a new python object in scope that has the name of the function. That's a python object that you can manipulate, pass to other functions, etc.

  function name should be a verb or a question, and should explain exactly what the function does so you won't be surprised.  

  arguments - have as few as possible, each one adds combinatorial complexity
   - positional arguments
   - keyword arguments
   - *args
   - **kwargs  

  function should *do one thing*

  fun facts ab>>>:
    can call other functions, can even define other functions within.  
    you can define classes inside functions
    3 ways to Return, Yield and Raise.  


##  Deeper dive:
### Lambda:
        lambda x: x*2
### Functions as arguments:
    def do_operation(a, b, operation):
        return operation(a,b)
    do_operation(5, 10, add)


  Map:

  map takes a function and a list, applies the function to every item in the list, and returns the results
  
  def map(func, sequence):
      result = []
      for item in sequence:
          result.append(func(item))
      return result

  let's write Filter!

  filter takes a function and a list, applies the function to every item in the list, and returns the items for which the function returned true. 

    is_even = lambda x: x% 2 == 0
    filter(is_even, range(1,10))
    >>>  [2, 4, 6, 8]
  (Students should now write filter)

### Functions as return values:
        def add_maker(x):
            def add(y):
                return x + y

    You can do this same effect with functools.partial

    Now you can pass an add function to map!

### Functools
  functools has plenty of useful tools for working with functions.
  
  functools.partial let's us do partial application of function argments, so we don't have to give all the arguments at one time

    import functools
    functools.partial(add, 5)
    partial_add = functools.partial(add, 10)
    partial_add(5)
    >>> 15

### Scope: How do variables that aren't arguments work?
  know that python resolves scopes in LEGB order: 
   - local,
   - enclosing, 
   - global,
   - built-in.

    x=5
    def foo(y):
        print locals()
        return x + y
    foo(10)

  #### Enclosing Scope? What's that?
  Here's an example of a "closure" - a function that encloses another function and can have variables in the 'enclosing' scope.


    def counter():
        all_numbers = []
        def add_one_more(x):
            all_numbers.append(x)
            return sum(all_numbers)
        return add_one_more
     
    this_count = counter()

    this_count(1)
    >>> 1

    this_count(1)
    >>> 2

    this_count(9)
    >>> 11

    this_count(3)
    >>> 14

    this_count(12)
    >>> 26

    this_count(-26)
    >>> 0


### Decorators
  a decorator is any function that takes a function as an argument, and returns a function.

  Let's look at a decorator that uses a *closure* to keep persistant state.

    def remember(func):
        all_results_ever = []
        def run_func(*a, **kw):
            all_results_ever.append(func(*a, **kw))
            return all_results_ever
        return run_func
    double = lambda x: x *2
    double(5)
    remember_doubles = remember(double)
    remember_doubles(4)
    >>> [8]

    remember_doubles(3)
    >>> [8, 6]

    remember_doubles(1)
    >>> [8, 6, 2]

    remember_doubles(6)
    >>> [8, 6, 2, 12]

    @remember
    def quadruple(x):
        return x * 4
    quadruple(6)
    >>> [24]
    quadruple(9)
    >>> [24, 36]


    *understand everything above here before reading memoize*
  ----------------------------------------------------------------------


    def memoize(func):
        all_results_ever = {}
        def run_func(*a, **kw):
            function_args = (a, tuple(kw.items()))
            if function_args in all_results_ever:
                return all_results_ever[function_args]
                      else:
                result = func(*a, **kw)
                all_results_ever[function_args] = result
                return result
    return run_func

    @memoize
    def double_and_print(x):
         print "I AM ACTUALLY RUNNING"
         return x * 2
    
    double_and_print(5)
    >>> I AM ACTUALLY RUNNING
    >>> 5
    double_and_print(5)
    >>> 5



### Generators
    def fib():
        fibs = [1,1]
        yield 1
        yield 1
        while True:
            next_fib = fibs[-2] + fibs[-1]
            fibs.append(next_fib)
            yield next_fib
    fib()
    >>> <generator object fib at 0x107539050>
    myfib = fib()
    next(myfib)
    >>> 1
    next(myfib)
    >>> 1
    next(myfib)
    >>> 2
    next(myfib)
    >>> 3
    next(myfib)
    >>> 5
    

### Discussion Question: Functional Style
    - what does it mean to write in a functional style, or use a functional programming language?

