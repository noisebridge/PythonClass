Functions, Generators and Ducks

0. #### What is a function? Yes, really. (5 minutes)    
    a. agreeing on our terms and concepts    
    b. types, data, and customizing    
    c. builtin functions, a [more interactive resource](http://joequery.me/code/python-builtin-functions/) than the docs    
    d. 

1. #### Today's deep dive: from functions to generators (25 mins)

    ```python

    #1
    def calculate_15perc_tax(bill):
    '''return the amount of money to pay in tax in US dollars
    '''
    return bill * .15



    #2
    item_prices = [6.95, 19.45, 4.0, 4.0, 13.95]
    def calc_20perc_tax_allitems(items):
        tax_items_ls = []
        for i in items:
            ...
        return 

    #3
    
    #list comprehensions and generator expressions, oh my!
    
    ```
    hint: if you find yourself writing way too much code, have a gander at the [builtin functions](https://docs.python.org/2/library/functions.html#built-in-funcs)     
    1.     
        a. Take the #1 example function and modify to ensure that it works with numeric types     
        b. Modify to return an english message to the customer that they need to graciously pay at least the returned amount        
        c. How have we used duck typing?    
    2.    
        a. Take the #2 example and return a list of values that correspond to 20% of the original values           
        b. Only calculate 20% for items larger than $10, for the rest return $0    
    3.    
        a. convert the final statement (2a) into list comprehensions and generator expressions     
        b. where the introduction to those concepts live [in the docs](https://docs.python.org/2/howto/functional.html)    


2. #### Definitions and Terminology (15 minutes)   
    1. Mathematical 
        a. In mathematics, a function is a relation between a set of inputs and a set of permissible outputs with the property that each input is related to exactly one output - [wiki](http://en.wikipedia.org/wiki/Function_%28mathematics%29)
        b. The output of a function f corresponding to an input x is denoted by f(x) (read "f of x")         

    2. In More Practical Programming Terms    
        a. A function is a block of code to be entered into, executed, and usually will give a return value    
        b. [In the docs](https://docs.python.org/2/reference/simple_stmts.html#the-return-statement)    

    3. Natural Language - eg: English    
        a. Functions are verbs that act on a noun     
        b. Usually a verb needs to function on particular a type of noun    
        c. [evacuate:](http://www.merriam-webster.com/dictionary/evacuate) to remove (someone) from a dangerous place    
        d. "The building was evacuated." not "There was a fire so the people evacuated."     
        e. let's define our own evacuate function in our own module    
        f. begs the question of more specific OOP tools     

    4. Function Signatures    
        a. [Definition in Computer Science](https://en.wikipedia.org/wiki/Type_signature)    
        b. Let's look at the signature of a couple [built in functions](https://docs.python.org/2/library/functions.html#built-in-functions)     
            1. next(iterator[, default])    
            2. print(*objects, sep=' ', end='\n', file=sys.stdout)    

3. #### Enough Thoery, a little more code! (20 mins)    
    a. examples/gen_countdown.py    
    b. examples/gen_lines_of_file.py    
    c. detour into iterators v. iterables    

4. #### Generators and the yield statement (20 mins)    
    a. [The docs have some great language](https://docs.python.org/2/howto/functional.html#generators)     
    b. detour into scoping and namespaces in python - in_class/customer_bills.py

5. #### Optional Exercises in Refactoring (20 mins)    
    a. Let's refactor the code in in_class/color_choice_refactor.py   
    b. or look at the code in in_class/parse_text_trade.py   

6. #### Extra: Functions are self-contained blocks of code (10 mins)    
    a. This means that they can be nicely tested!    
        1. Let's test the first example we wrote with the unittest framework    
        2. See: [example4-setup.py](example4-setup.py)     

7. #### Lab: Working with data inputs of variable sizes - Text Processing    
    1. parsing files and doing intelligent NLP    
    2. pymotw - there's a [text processing](http://pymotw.com/2/articles/text_processing.html) section!       
    3. [Peter Norvig on text processing](http://nbviewer.ipython.org/url/norvig.com/ipython/How%20to%20Do%20Things%20with%20Words.ipynb) ipynb    
    4. search nltk or text processing in python      
