Functions, Generators and Ducks

0. #### What is a function? Yes, really.    
    a. agreeing on our terms and concepts    
    b. types, data, and customizing    
    c. builtin functions, a [more interactive resource](http://joequery.me/code/python-builtin-functions/) than the docs    
    d. 

1. #### Today's deep dive: from functions to generators (15 mins)

    ```python
    num = 10
    print id(num)

    def square_x(x): #arguments are aka parameters
        x ** x

    print num  
    print id(num)
    ```

    1. Play with id() of variables and what a function can return - 3 minutes    
    2. Write iterations of this functions to return different values with no side effects    


2. #### Definitions and Terminology (35 minutes)   
    1. Mathematical 
        1. In mathematics, a function is a relation between a set of inputs and a set of permissible outputs with the property that each input is related to exactly one output
        2. The output of a function f corresponding to an input x is denoted by f(x) (read "f of x")    
        3. To illustrate these let's jump into some built-in functions [example0.py](example0.py)
    2. In More Practical Programming Terms    
        1. A function is a block of code to be entered into, executed and usually give a return value    
        2. [In the docs](https://docs.python.org/2/reference/simple_stmts.html#the-return-statement)    
        3. Plug in your code from warm-up or from [example1.py](example1.py) to [online python tutor](http://pythontutor.com/visualize.html#mode=edit)    
 
    3. Natural Language - eg: English    
        1. Functions are verbs that act on a noun     
        2. Usually a verb needs to function on particular a type of noun    
        3. [evacuate:](http://www.merriam-webster.com/dictionary/evacuate) to remove (someone) from a dangerous place    
        4. "The building was evacuated." not "There was a fire so the people evacuated."  

    4. Function Signatures    
        1. [Definition in Computer Science](https://en.wikipedia.org/wiki/Type_signature)    
        2. Let's look at the signature of the ubiquotous [python builtin open()](https://docs.python.org/2/library/functions.html#open)    

3. #### Functions are self-contained blocks of code (10 mins)    
    1. This means that they can be nicely tested!    
        1. Let's test the first example we wrote with the unittest framework    
        2. See: [example4-setup.py](example4-setup.py)  

4. #### Generators and the yield statement (20 mins)    
    1. [LearnPython resource](http://www.learnpython.org/en/Generators)  

5. #### Exercise Reading and Refactoring (20 mins)    
    1. Refactor the code in [example2.py](example2.py)    

6. #### Resources Used    
    1. [joequery blog on built-in examples](http://joequery.me/code/python-builtin-functions/#enumerate)    

