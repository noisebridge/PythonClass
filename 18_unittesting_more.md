####Meaningful Unittesting and TDD

1. Why Even Write Tests (My code works fine)    
    [docs!](https://docs.python.org/2.7/library/unittest.html)    


2. Review of how to use assert and unittest framework    
    a. boilerplate examples, [pymotw](http://pymotw.com/2/unittest/)      
    b. checking in on terminology: test fixture, test case, test runner, test suite    
    c. special methods that we get 'for free'    -from nose.tools import assert_equals
    d. should we test individual classes and methods?             

3. Writing Meaningful Tests    
    a. edge cases    
    b. what a unit test really means    
    c. bit of philosophy / story of objects    


4. TDD: getting started with tdd using unittest    
    - what can we write?     

5. why would one make setUp and tearDowns    
   -temp file    
   -temp directory    
   -database connection    
   -db transaction    
   -open socket connection    
   -a signal generator putting out a test signal    

6. other frameworks for TiP    
    a. [great write up from HHG to Python](http://docs.python-guide.org/en/latest/writing/tests/)    
    b. what is nose and how to use     
        -Nose’s tagline is "nose extends unittest to make testing easier"    
        -what is the nose api?    
    c. py.test    

(unnecessary stuff to del)
-package level fixtures
-module level fixtures
-class level fixtures
-class method level fixtures
-function level fixtures: 'oddball of the bunch' in nose done with the @with_setup decorator, which is included from nose.tools
production, refactoring, documentation, reassurance, psych help, rolling on considering edge cases.
