####Meaningful Unittesting and TDD

1. Why Even Write Tests (My code works fine)    

2. Review of how to use assert and unittest framework    
    a. example (polygons, angles, words)
    b. what is nose and how to use    
        -Nose’s tagline is "nose extends unittest to make testing easier"
        -what is the nose api?  
    c. special methods that we get 'for free'    -from nose.tools import assert_equals
    d. should we test individual classes and methods?      

3. Checking in on terminology
    a. test fixture, test case, test runner, test suite     
    b.  

3. Writing Meaningful Tests    
    a. edge cases    

4. TDD: getting started with tdd using doctest and unittest
    a. 

5. why to make setUp and tearDowns
   -temp file
   -temp directory
   -database connection
   -db transaction
   -open socket connection
   -a signal generator putting out a test signal

-package level fixtures
-module level fixtures
-class level fixtures
-class method level fixtures
-function level fixtures: 'oddball of the bunch' in nose done with the @with_setup decorator, which is included from nose.tools

@with_setup(setup_function,teardown_function)
def test_a():
    pass



