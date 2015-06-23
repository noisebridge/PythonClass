#### Python Object Oriented Programming       


A wonderful way to encapsulate our data and actions!    

0. #### Installation and Class Prep: all in the std lib!     
    1. Class Prep Resources:     
        1. [Python docs](https://docs.python.org/2/) are the place for this! The tutorial, the [language reference](https://docs.python.org/2/reference/index.html) and even the [HOWTOs](https://docs.python.org/2/howto/index.html)    
        2. A great look at 'double underscore' aka 'dunder' or 'magic methods' see Rafe Kettler's [magic methods blogpost](http://rafekettler.com/magicmethods.html)     
        3. Also in the 'language reference' section of the docs [Objects, values and types](https://docs.python.org/2/reference/datamodel.html#objects-values-and-types)      


1. #### Today's deep dive: Let's get to modeling real world objects - 20 minutes    

    ```python
    class Customer(object): 
        '''customer class, of which you are an instance of in many entities' application code
        '''

        #data attributes for each instance are initialized in the __init__ method
        def __init__(self, money_in_account, favorite_item='cotton-candy'): #this is the initializer, (not the constructor!)
            self.money_in_account = money_in_account
            self.favorite_item = favorite_item
            self.items_bought = []

        def add_bought_item(self, bought_item):
            self.items_bought.append( bought_item )

        def __repr__(self):  #just __str__ in python 3
            return "Customer with {0} money\nitems bought: {1}\nfavorite item {2}" \
                    .format(
                        self.money_in_account, 
                        self.items_bought, 
                        self.favorite_item)
            
    cust = Customer(100)
    print cust

    cust.add_bought_item('popcorn')
    print cust
    ```
    
    1. This is a user defined object  - 3 minutes    
        1. let's examine all of its attributes using dir()    
        2. where is this user defined class getting its other attributes from?    
        3. how can we expand this object and make it interact with other objects?    
    
2. #### What to know about python objects by example     
    1. Terms, Concepts and denotative definitions - 25 minutes    
        0. constructor - creation of a new instance of specified object type    
            a. see examples/inherit_from_string.py     
        1. initializer - the '__init__' factory, populate that instance with methods and attributes    
        2. attributes - data attributes and method attributes    
        3. self reference - the 'self' is to tell the interpreter which class name an attribute is a member of    
        4. dunder methods - written in C, can be over ridden or defined by user, duck typing     
        5. operator - the term and operator overloading when defining classes     
        6. type and class - relationships objects have to each other, visual    

3. #### We've been using objects all along     
    1. Reimplementing type int as an Integer class - 10 minutes     
        1. what kinds of attributes would an integer need?    
        2. examples/reimplement_integer.py    
        3. everything is a type and a class

    2. Scope of LEGB - 10 minutes     
        1. what is scope and how is it 'dangerous?'    
        2. examples/legb.py     
        

4. #### Expanding first example: making objects interact    
    1.  Making a product object - 20 minutes    
    

5. #### Lab Primer      
    1. Card Game    
    2. what objects would we need for all card games?    
    3. what objects and designs would we need for your specific favorite card game    
    4. try it out on your own    



