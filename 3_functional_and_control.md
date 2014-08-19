
1. If you’ve done excel then you have done functional programming
-finding ‘perfect primes’ in excel, numbers, libreoffice

2. Where and how functional programming is incorporated into python, a mostly imperative language
https://docs.python.org/2/howto/functional.html
-forces you to break down problem into small chunks
-easier to debug
etc.


The principle of referential transparency (RT) is this:
An expression e is referentially transparent if for all programs p every occurrence of e in p can be replaced with the result of evaluating e, without affecting the observable result of p

We'll use this statement to test whether our following code is functional or imperative.

Note about "true" functional languages and their use of strong typing and recursion.

quickly compare to imperative programming paradigm (r object in requests library example) and how this relates to OOP.
what does a purely functional language look like?

--retrieve dataset 
build upon previous lesson using requests library and request data from reddit API
--quickly parse dataset into basic list


3. iterators and generators: using examples of cleaning and manipulating raw text data into consummable information for end user.

a yield statement can halt at an iteration whereas a return statement 

Two common operations on an iterator’s output are 
    1) performing some operation for every element
    2) selecting a subset of elements that meet some condition. 

subroutines are another word for function.
Subroutines are entered at one point and exited at another point (the top of the function, and a return statement), but coroutines can be entered, exited, and resumed at many different points (the yield statements). 

#neato tidbit
The dict() constructor can accept an iterator that returns a finite stream of (key, value) tuples: 
>>> L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
>>> dict(iter(L)){'Italy': 'Rome', 'US': 'Washington DC', 'France': 'Paris'} 

list comps and gen expressions borrowed directly from Haskell

On executing the yield expression, the generator outputs the value of i, similar to a return statement. The big difference between yield and a return statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved. On the next call to the generator’s .next() method, the function will resume executing. 

If a generator function calls return or reaches the end its definition, a StopIteration exception is raised.
Once a generator has been exhausted, calling next() on it will result in an error, so you can only consume all the values of a generator once.
 
include control 
try:

except:

finally: 