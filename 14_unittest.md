    
    
1. Unit Testing - What is it?    
    a. Wikipedia - [Unit Testing](http://en.wikipedia.org/wiki/Unit_testing)    
    b. Python unittest builtin module - no setup required, just 'import unittest'    
    c. The paradigm: red, green, refactor.    
        i.   red - make a test, but don't write the code. The test obviously fails.    
        ii.  green - write the minimum code to pass the test. Verify the test passes.    
        iii. refactor - clean up the code. Follow: [PEP8](http://legacy.python.org/dev/peps/pep-0008/#maximum-line-length), [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself), rule of three][http://en.wikipedia.org/wiki/Rule_of_three_[computer_programming]), etc.    
    d. How do we build a good test? That isn't a topic for today, but here are some ideas:    
        i.   break your code into testable subproblems.    
        ii.  too simple is bad, avoid testing builtins and standard library functions.    
        iii. build the test before any code is written, this is "Test DRIVEN Development"    
        iv.  This is just one way to code. You should know how to write a test, though.    
    
    
2. Lets build a tiny little unit testing framework.    
    a. Build a simple test, e.g. 1+1==2    
        i. The test isn't the focus yet.    
    b. Build some more tests (2 more today)    
        i. Two more tests in the same category.    
        ii. Simple math is best, we just want to get enough tests to see implementation patterns.    
    c. Now lets generalize. 4 things change in each test.    
        i. test name - although you could have different text for fail/success    
        ii. type of assert - we use only == to keep things simple    
        iii. left side of assert statement    
        iiii. right side of assert statement    
    d. Parts of our testing framework:    
        i.   test fixture - setup needed to build and breakdown a test - variables, databases, tcp connections, etc.    
        ii.  test case - a single subproblem, can include multiple asserts, and therefore multiple pass/fail responses.    
        iii. test suite - an aggregation of test cases, iterates over each test case.    
        iv.  test runner - the framework over which tests are run, as easy as a for loop and print statement to display results.    
    
    
3. Now that we understand the parts we need, let's use a more robust and WELL TESTED framework.    
    a. Python 'unittest' builtin module.    
        i.   This framework uses classes.    
        ii.  Don't get lost in the weeds on the classes.    
    b. unittest howto - the example 1 from the python documentation is copied into this repository:    
        i.   unittest.TestCase is the parent class for our class. Inherit from this.    
        ii.  setUp() function contains the components your unit test needs to access.    
        iii. tearDown() takes anything down like tcp connections, database connections, etc.    
        iv.  Individual tests are methods of unittest.TestCase. Begin with test_ and name them well.    
        v.   invoke unittest.main(), as in the example.     
            a. There is a complex breakdown of this in the documentation.    
            b. It is interesting but very detailed. Eventually you may use it.    
    c. Now lets integrate our unit tests from our framework into Python's standard framework.    
        i.   We do this to translate all the insights we got from building our framework into the unittest framework.    
        ii.  This will solidify learning because your brain hasn't accessed that info for around 40-100 minutes.    
    
    
    
