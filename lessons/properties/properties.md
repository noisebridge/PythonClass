

#### Advanced OOP 

Building Classes using Python's more obscure but interesting and necessary features.


0. #### Installation and Class Prep
    1. Installation Instructions:
        1. None Tonight!

    2. Class Prep Resources:
        1. Python Essential Reference ch. 7 by David Beazley  
        2. Learning Python 


1. #### Deep Dive: Building Basic Date Class 

    ```python
    import time

    class Foo(object):

        def __init__(self, baz, bar, bow):
            self.baz = baz 
            self.bar = bar 
            self.bow = bow

        def __repr__(self):
            return "the attributes of {0}/{1}/{2}".format(self.baz, self.bar, self.bow)
    
    f = Foo('baz', 'bar', 'bow')

    t = time.localtime()
    dir(t)
    ```

    1. Replace With An Explanation - 3 minutes
        1. 
        2. 
        3. See: [example_file.py](example_file.py)
    2. Second Part
        1. 
        2. 
        3. See: [example_file.py](example_file.py)


2. #### Static and Class method decorators
    1. The difference and relationship of each to regular class definition - 20 minutes
        1. class methods implement alternative constructors. Gives subclasses the freedom to override methods without breaking other methods. These operate on the class itself as an object. 

        2. static methods attach functions to classes. They don’t need either ‘self’ or ‘cos’. Static methods improve discoverability and require context to be specified. These are ordinary methods that just happen to live in a namespace defined by a class. You might have different ways to create new instances.

        3. See: [static_and_class_methods.py](static_and_class_methods.py)


3. #### Properties
    1. Getter and Setter methods - 20 minutes
        1. properties lets getter and setter methods be invoked automatically by attribute access that is dot syntax. This allows python classes to freely expose their instance variables.
        2. 
        3. See: [properties.py](properties.py)

4. #### Descriptors
    1. a descriptor is anything that has at least just one of the methods __get__() __set__() or __delete__() - 20 minutes
        1. That is ```__get__() __set__() or __delete__()``` methods
        2. We can think of descriptors as properties that we can reuse
            -a Data Descriptor has both __get__() __set__()
            -a Non-Data Descriptor has only __get__()
        3. Just syntactic sugar for class and static methods, they are all descriptors underneath. "simple interface to complicated API” - Simeon Franklin
        4. See: [descriptors.py](descriptors.py)
    

4. #### Extended Resources
    1. [Simeon Franklin on descriptors](https://www.youtube.com/watch?v=ZdvpNaWwx24)
    2. [Zipline screencast on Descriptors](https://www.youtube.com/watch?v=P92z7m-kZpc)
    3. [Luciano Ramalho on descriptors](http://pyvideo.org/video/1760/encapsulation-with-descriptors)
    4. [Raymond Hettinger on building classes](https://speakerdeck.com/pyconslides/pythons-class-development-toolkit-by-raymond-hettinger?slide=39)
