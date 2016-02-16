

#### The Phone Book Search Algorithm

We'll be writing an algorithm tonight that describes the 'phone book' search method, a way of quickly searching a list of items for a specific item.

This is an 'algorithm' which is a long word for 'way of doing things'.

Other things that are algorithms: tying your shoes, addition, making an omelet.



1. ##### Today's deep dive: functions and scope

    ```python
    """ Lets learn a bit about functions and 'scope'
    """
    
    # you can use lowercase, but globals as all caps can help differentiate.
    THIS_IS_A_GLOBAL_VARIABLE = "is this available in the function?"

    def add_a_number(source_number, number_to_add):
        """ This function allows us to add whatever we pass it
        """
        result = source_number + number_to_add
        
        print "Viewing: {}".format(THIS_IS_A_GLOBAL_VARIABLE)

        return result

    first_number = 100
    second_number = 10
    returned_from_the_function = add_a_number(first_number, second_number)
    print "Result of {} + {}: {}".format(first_number, second_number, returned_from_the_function)
    ```

    1. What is this tricky scope concept?
        1. It determines what you can see from your location in your code. 
        2. Remember: a name/variable is just a 'name' assigned to ANY object.

    2. Some scope guidelines:
        3. Globally defined (no indentation) names can be seen from anywhere.
        4. Names defined in a function or class can not be seen except in functions or classes (or modules) that are children of that class.
        5. This means scope can be thought of like a tree with global as the roots.
        6. Pitfall: a name cannot be used before it is defined. The code runs one line at a time.



2. ##### What are we even doing? Lets set up our phone book search:
    
    1. Some things we need:
        1. Data to search through. It must be sorted. Why?
        2. A description of how our search will operate.
        3. A value to search for. Lets arbitrarily start with the 57th index value (of 100).

    2. DATA SET (REQUIREMENT 1)
        1. First we need data. Lets make a [random list](https://docs.python.org/2/library/random.html#random.sample) of 100 items between the numbers 1 to one million.
        ```python
        """ Start a new file and put this code in it!!
        """
        import random

        # if we do this we can probably all get the same list        
        random.seed(99)

        our_dataset = random.sample(range(1000000), 100)
        
        # we are printing these to see if everyone has the same numbers! check it.
        print our_dataset[0:10]
        # this does sort the actual our_dataset list. 
        # A list is a mutable object (an object that can be mutated/changed).
        # remember our strings were immutable (cannot be mutated/changed) objects.
        # string internal functions CANNOT alter themselves.
        our_dataset.sort()
        print our_dataset[0:10]
        ```

    3. Description of our search algorithm (REQUIREMENT 2)
        1. What is a phone book search?
            1. Open a phonebook half way.
            2. If the first letters of the last name you are searching for is before your location, open the book up in the middle of the first half. Otherwise open to the middle of the second half.
            3. Repeat 2 until you are on the right page.
            4. When on the same page, you can repeat this with the actual values.

    4. The value 57th index of the dataset (REQUIREMENT 3)
        1. Append this to our code above:
        ```python
        # add this code to the last snip of code.
        our_value = our_dataset[57]
        print "The value we will search for: {}".format(our_value)
        ```

3. Now let's make the phone book search algorithm!
    1. Some more specifications:
        1. Write a function that returns the index we chose (57th index).
        2. The function should use a binary tree search and take the data set and the value we want to find as inputs.
        3. The function should return the index of the value. That's 57! (pitfall: the index starts at 0!)
        4. Test the function on other values using new test values (REQUIREMENT 3).
        5. What would a unit test for this look like?

    2. An example **Don't look at this example until after class!** This time around you can't - hah! We haven't written it yet.
        1. How can we use this same set of requirements to write other algorithms?
        2. Can we use this as a structure for unit tests?
        ```python
        """ placeholder
        """
        ```
