'''example from http://www.devshed.com/c/a/Python/Object-Orientation-in-Python/'''

class ParentClass(object):
    testVariableA = 'This is a test variable. Pay no attention to it.'
    testVariableB = 'This is also a test variable. Or is it? We may never know.'
    def __init__ ( self, testArgument ):
       self.testVariableC = testArgument
    def testMethod ( self ):
       return False
 
class ChildClass ( ParentClass ):
    testVariableB = 'I am a very rebellious variable. Yes I am.'
    def testMethod ( self ):
       return True

parentObject = ParentClass ( "I am an insignificant test argument." )
print parentObject.testVariableA # This is a test variable. Pay no attention to it.
print parentObject.testVariableB # This is a test variable. Or is it? We may never know.
print parentObject.testVariableC # I am an insignificant test argument
print parentObject.testMethod() # False
 
childObject = ChildClass ( "This is a subclass of ParentClass." )
print childObject.testVariableA # This is a test variable. Pay no attention to it.
print childObject.testVariableB # I am a very rebellious variable. Yes I am.
print childObject.testVariableC # This is a subclass of Parent Class.
print childObject.testMethod() # True