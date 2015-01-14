ipython notebook gist url: http://nbviewer.ipython.org/gist/teddymcw/000dcebdb4f44c7283ef


Objectives:
-Formally introduce functional programming paradigm in python, compare to imperative, and make it easy
-Execute some "valuable" text processing
-Have some fun with words


1. If you’ve done excel then you have done functional programming. Formal definitions (20 min)
-basic functions in excel, numbers, libreoffice

-plug in a couple of sets (or lists) into excel and apply a few functions
-test against below definitions

Referential Transparency: What can you see in the data/objects being processed?

The principle of referential transparency (RT) is this:
An expression e is referentially transparent if for all programs p every occurrence of e in p can be replaced with the result of evaluating e, without affecting the observable result of p

We'll use this statement to test whether our following code is functional or imperative.

Plug in excel example.

2. Where and how functional programming is incorporated into python, a mostly imperative language (10 min)

-discuss pros and cons, why and when?

-official resource: https://docs.python.org/2/howto/functional.html

Why even use a functional style of programming when imperative is just fine!?
-forces you to break down problem into small chunks
-easier to debug
etc.

-can you apply these rules to English grammar?

3. iterators and generators: using basic examples (20 min)

intro to list comps, iterator terminology and generators using examples

iterables v. iterators:
eg: can be iterated v. the iterator itself.
keep in mind that the iterator variable is also different than the value the iterator is pointing to

Two common operations on an iterator’s output are 
    1) performing some operation for every element
    2) selecting a subset of elements that meet some condition


list comps and gen expressions borrowed directly from Haskell

list comprehensions:
list comps are "syntactic sugar" in that they don't add any functionality but they make expressions easier to write and in this case to read and comprehend 

generators:   definite added functionality
a yield statement can halt at an iteration whereas a return statement returns an entire object
a generator is an iterable that is a stream in memory, it can only be iterated through once

subroutines: another word for function. Subroutines are entered at one point and exited at another point (the top of the function, and a return statement)

coroutines: a type of subroutine BUT can be entered, exited, and resumed at many different points (the yield statements). Generators can be referred to as coroutines in the python domain.

note that it is rare to find the case where using a generator is not better than using a list. In fact in python 3 many functions that did produce lists were replaced by their generator equivalent such as range and xrange or filter and ifilter. 


4. basic appiclation: compare cleaning text methods on larger text corpuses converted into iterables for processing (10 min)

-introduce text to work with
-discuss methodology and necesary steps for valuable analysis

5. deeper dive application: cleaning and manipulating raw text data into consummable information for end user (40 min)

-thinking about what we want to extract
-how should we design are functions
-write
-apply / play!

6. fun with itertools (10 min)

-applying a few functions that would produce some type of analysis or humor
-tour the itertools library and discuss purpose

7. further: (infinity)

-lambda functions

-include control statements to take care of the StopIteration exception when a generator has exhausted its possible iterators.
 
try:

except:

finally:

-what other metrics or analysis can we provide combining what we have written thus far and what we are aware of just in the stdlib available to us?
-how would we spur cretivity when feeling stuck? 
