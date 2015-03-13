#OOP, Classes and Class interaction  

######spike: what OOP isn't   
let’s open up our good friend [repl.it](http://repl.it/) and [Scheme](https://classes.soe.ucsc.edu/cmps112/Spring03/languages/scheme/SchemeTutorialA.html) some non-OOP
    starting with a couple built-in functions   
    (print "Hello, " (read) "!")
    now let's define some of our variabls   
    (define pi 3.14)
    (define square (lambda (x)  (* x x)))

    (define my_list (list 1 2 3 5))

    (define length
           (lambda (l)
                   (if (null? l)
                          0
                          (+ 1 (length (cdr l))))))     

1. What is OOP? and how does Python implement this paradigm?       
-OOP is when objects have their own data and their own methods that act on the data   
-The Python language is written in C and the built-in objects including the built-in functions that act on objects  
-One could make a pit stop in the docs for a glance at the [python data model](https://docs.python.org/2/reference/datamodel.html)  
-These built-in functions are ultimately called by a '__method__' that is to say a "double underscore" method or "dunder" and then executed in the corresponding C code     
-In order to understand this more need to write our own objects      

    Define Terms:
    -attribute: data an object contains     
    -method: function an object contains    
    -property: attributes and methods an object contains    

######exercise 1: syntax and user defined methods by defining a single Playing Card     
Keep in mind the design rule of YAGNI: "ya ain’t gonna need it"

    Class BlahClass(object):
    '''docstring describing class'''
    #class methods would go here

    def __init__(self, anyarg, moreargs): #the initializer for object instance
        '''where we define instance attributes''' 
        self.anyarg = anyarg
        self.moreargs = moreargs

    def instance_method(self):
        return "arbitrary example code " + self.anyarg  

######exercise 2: adding 'magic' methods aka 'dunder' methods  
Now let's take a look at how to make our object more useful to us with [magic methods](http://rafekettler.com/magicmethods.html)    
    __new__, __del__, __str__, __unicode__, __repr__, __manymanymore__  

__init__ is an initializer, by the time we hit this we have already contracted the object, thus the object already exists.

the goal of self is to create that unique instance, the goal of __init__ is to populate that instance with methods and attributes

Note: python OOP implementation exposes instance attibutes, eg: you can get and set easily!
    instance_attr.now_equals(this)  
Why? 
because its Great!
"python is language for consenting adults"

######exercise 3: make a PokerCard class with the functionality of a high or low Ace composition v. inheritance    
See examples/inheritance-v-composition.py

keep in mind that classes are effectively modules in and of themselves  
they are also APIs in and of themselves     
   


