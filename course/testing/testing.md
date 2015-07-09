#### Testing - ensuring code is air tight and elastic!


Starting with unit test and testing philosophy


0. #### Today's deep dive: Writing a well tested function to change the last letter of a word to an upper case letter    

    ```python
    def upper_last_letter(word):
        pass
    ```

    1. Inputs this must handle - 15 minutes
        1. "hello", "roboT", "j14-2dsw5", 2044    
        
    
1. Unit Testing - What is it?    

    a. Wikipedia - [Unit Testing](http://en.wikipedia.org/wiki/Unit_testing)    
    b. Python unittest builtin module - no setup required, just 'import unittest'    
    c. The paradigm: red, green, refactor.    
        a. red - make a test, but don't write the code. The test obviously fails.    
        b. green - write the minimum code to pass the test. Verify the test passes.    
        c. refactor - clean up the code. Follow: [PEP8](http://legacy.python.org/dev/peps/pep-0008/#maximum-line-length), [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself), [rule of three](http://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)), etc.    
    d. How do we build a good test? That is too large a topic for today, but here are some ideas:    
        a.  break your code into testable subproblems.    
        b.  too simple is bad, avoid testing builtins and standard library functions.    
        c.  build the test before any code is written, this is "Test DRIVEN Development"    
        d.  This is just one way to code. You should know how to write a test, though.    
     
2. Parts of a test case: 4 things in each test.    
        a.  test name - although you could have different text for fail/success    
        b.  assert statement simply takes True/False (or a list of True/False) - we use only == to keep things simple    
        c.  left side of assert statement    
        d.  right side of assert statement    

3. Parts of our testing framework: paraphrased from documentation    
        a.  test fixture - setup needed to build and breakdown a test - variables, databases, tcp connections, etc.    
        b.  test case - a single subproblem, can include multiple asserts, and therefore multiple pass/fail responses.    
        c.  test suite - an aggregation of test cases, iterates over each test case.    
        d.  test runner - the framework over which tests are run, as easy as a for loop and print statement to display results.    
    
    
3. Understanding the components    
    1. Python [unittest](https://docs.python.org/2/library/unittest.html) builtin module.    
        a.  The module provides a special suite of [Asserts](https://docs.python.org/2.7/library/unittest.html#assert-methods). They are very readable.    
    2. unittest howto - the example 1 from the python documentation is copied into this repository:    
        a.  [unittest.TestCase](https://docs.python.org/2.7/library/unittest.html#unittest.TestCase) is the parent class for our class. Inherit from this.    
        b.  setUp() function contains the components your unit test needs to access.    
        c.  tearDown() takes anything down like tcp connections, database connections, etc.    
        d.  Individual tests are methods of unittest.TestCase, they begin with test_ and remember to name these as specifically as possible!    
      
    
    
    
