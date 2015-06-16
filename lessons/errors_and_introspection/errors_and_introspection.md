

#### Errors and Introspection

Tonight will cover a lot of topics. We'll start by messing with the dir() and help() commands. Then we'll view the standard library errors, catch a few in our control flow with try/except. Next we'll play briefly with inspect, timeit, and finally trace errors with pdb.


0. #### Installation and Class Prep 
    1. Installation Instructions:
        1. You only need the Python Standard Library
    2. Class Prep Resources:
        1. []()
        1. []()
        1. []()
        1. []()


1. #### Today's deep dive: The Deep Dive Title Goes Here

    ```python
    in_a_list = dir(list())
    in_a_dict = dir(dict())

    only_in_a_list = []
    for attribute in in_a_list:
        if attribute not in in_a_dict:
            only_in_a_list.append(attribute)
            
    only_in_a_dict = []
    for attribute in in_a_dict:
        if attribute not in in_a_list:
            only_in_a_dict.append(attribute)

    print 
    print "Things in a list but not a dict: {}".format(only_in_a_list)
    print
    print "Things in a dict but not a list: {}".format(only_in_a_dict)
    print
    
    ```

    1. Replace With An Explanation - 3 minutes
        1. 
        2. 
        3. See: [example_file.py](example_file.py)
    2. Second Part
        1. 
        2. 
        3. See: [example_file.py](example_file.py)


2. #### First Point
    1. Replace with An Explanation - XX minutes
        1. 
        2. 
        3. See: [example_file.py](example_file.py)
    2. Second Part
        1. 
        2. 
        3. See: [example_file.py](example_file.py)
    3. Third Part
        1. 
        2. 
        3. See: [example_file.py](example_file.py)

3. #### Second Point
    1. Replace With An Explanation - XX minutes
        1. 
        2. 
        3. See: [example_file.py](example_file.py)
    2. Second Part
        1. 
        2. 
        3. See: [example_file.py](example_file.py)
    3. Third Part
        1. 
        2. 
        3. See: [example_file.py](example_file.py)


4. #### Lab Primer 
    1. What to cover in a lab session
    2. What can we do with concepts learned? - XX minutes   
    3. What are some real world applications?    
    4. How to prep until then


5. #### Extended Resources - any links or resources to take this concept further    
    1. [Sample Link](www.example.com)
    2. 
    3. 
