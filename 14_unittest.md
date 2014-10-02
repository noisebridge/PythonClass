    
    
1. Unit Testing - What is it?    

    1. Wikipedia - [Unit Testing](http://en.wikipedia.org/wiki/Unit_testing)    
    2. Python unittest builtin module - no setup required, just 'import unittest'    
    3. The paradigm: red, green, refactor.    
        - red - make a test, but don't write the code. The test obviously fails.    
        - green - write the minimum code to pass the test. Verify the test passes.    
        - refactor - clean up the code. Follow: [PEP8](http://legacy.python.org/dev/peps/pep-0008/#maximum-line-length), [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself), [rule of three](http://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)), etc.    
    4. How do we build a good test? That is too large a topic for today, but here are some ideas:    
        -  break your code into testable subproblems.    
        -  too simple is bad, avoid testing builtins and standard library functions.    
        -  build the test before any code is written, this is "Test DRIVEN Development"    
        -  This is just one way to code. You should know how to write a test, though.    
    
    
2. Lets build a tiny little unit testing framework.    
    1. Build a simple test, e.g. 1+1==2    
        -  The test isn't the focus yet.    
    2. Build some more tests (2 more today)    
        -  Two more tests in the same category.    
        -  Simple math is best, we just want to get enough tests to see implementation patterns.    
    3. Now lets generalize. 4 things change in each test.    
        -  test name - although you could have different text for fail/success    
        -  assert statement simply takes True/False (or a list of True/False) - we use only == to keep things simple    
        -  left side of assert statement    
        -  right side of assert statement    
    4. Parts of our testing framework:    
        -  test fixture - setup needed to build and breakdown a test - variables, databases, tcp connections, etc.    
        -  test case - a single subproblem, can include multiple asserts, and therefore multiple pass/fail responses.    
        -  test suite - an aggregation of test cases, iterates over each test case.    
        -  test runner - the framework over which tests are run, as easy as a for loop and print statement to display results.    
    
    
3. Now that we understand the parts we need, let's use a more robust and WELL TESTED framework.    
    1. Python 'unittest' builtin module.    
        -  This framework uses classes.    
        -  Don't get lost in the weeds on the classes.
        -  The module provides a special suite of [Asserts](https://docs.python.org/2.7/library/unittest.html#assert-methods). They are very readable.    
    2. unittest howto - the example 1 from the python documentation is copied into this repository:    
        -  unittest.TestCase is the parent class for our class. Inherit from this.    
        -  setUp() function contains the components your unit test needs to access.    
        -  tearDown() takes anything down like tcp connections, database connections, etc.    
        -  Individual tests are methods of unittest.TestCase. Begin with test_ and name them well.    
        -  invoke unittest.main(), as in the example.     
            1. There is a complex breakdown of this in the documentation.    
            2. It is interesting but very detailed. Eventually you may use it.    
    3. Now lets integrate our unit tests from our framework into Python's standard framework.    
        -  We do this to translate all the insights we got from building our framework into the unittest framework.    
        -  This will solidify learning because your brain hasn't accessed that info for around 40-100 minutes.    
    
    
    
