number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    # New block starts here
    print 'Congratulations, you guessed it.'
    print '(but you do not win any prizes!)'
    # New block ends here
elif guess < number:
    # Another block
    print 'No, it is a little higher than that'
    # You can do whatever you want in a block ...
else:
    print 'No, it is a little lower than that'
    # you must have guessed > number to reach here

print 'Done'
# This last statement is always executed,
# after the if statement is executed.



number = 23

def compare_num_until_correct(num):
    guess = int(raw_input('Guess what my secret integer is! '))
    if guess == number:
        # New block starts here
        print 'Congratulations, you guessed it.'
        print '(but you do not win any prizes!)'
        # New block ends here
    elif guess < number:
        # Another block
        print 'No, it is a little higher than that'
        compare_num_until_correct(num)
        # You can do whatever you want in a block ...
    else:
        print 'No, it is a little lower than that'
        compare_num_until_correct(num)
        
compare_num_until_correct(number) #base case
compare_num_until_correct(37) #new case



#We wanna get stuff done by telling the computer what to do cleanly
#Errors stop your code from running
#we all know IndentationErrors but there are many others which one can view in the Exception Hierarchy
#haven't gone over object hierarchy but this is a microcosm of object hierarchy



def bare_exceptions(num1, num2):
    try:
        print(num1 / num2)
    except:
        print("caught some error we're not printing for you! on to the next statement!")
    print("last line of this function and on to the next line of our algorithm!")   

bare_exceptions(10,5)    
#bare_exceptions(10,0)
#insert the raise keyword in this function above logically



#recreating the "with open(filename)" context manager

def open_and_close_file1(filename):
    try:
        fp = open(filename)
        print(fp.readline())
    except IOError as err:
        print(err)
    finally:
        fp.close()

open_and_close_file1('obama_09.txt') #file does exist
#open_and_close_file1('obama_07.txt') #file does not exist

#are there more exceptions to look up here?




#gratuitous example using a loop and the continue control statement
def grat_con():
    for line in open("foo.txt"): 
        stripped = line.strip() 
        if not stripped:
            continue # Skip the blank line
    close("foo.txt")

    
    
#gratuitous example of the break statement, always at least consider a break with a while
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again…")
        
        

#extremely gratuitous example of the pass statement, mostly used for "stubs"
def write_to_page():
    pass



#hella examples and patterns seen in the wild

#1 system example from https://wiki.python.org/moin/HandlingExceptions
import sys
try:
  untrusted.execute()
except: # catch *all* exceptions
  e = sys.exc_info()[0]
  write_to_page( "<p>Error: %s</p>" % e )


    
#2 rollback example pseudo code from wiki.python.org
try:
  do_some_stuff()
except:
  rollback()
  raise 
else:
  commit()

    
    
#3 parsing a config file where we need a config_dict option for each parsing
config_dict = {}

# Iterate over a list of all the options provided in a section.
try:
    for arg_key in config.options(section):
        config_dict[arg_key] = config.get(section, arg_key)
except ConfigParser.NoSectionError:
    print "Warning: No config section '" + str(section) + "' Returning an empty dictionary for this section."
    return {}

    return config_dict



#4 pseudocode using the else statement
try:
    operation_that_can_throw_ioerror()
except IOError:
    handle_the_exception_somehow()
else:
     # we don't want to catch the IOError if it's raised
    another_operation_that_can_throw_ioerror()
finally:
    something_we_always_need_to_do()
    
    
    
#5 bad logging psuedocode: often used for logging when running any application that would warrant collecting errors 
try:    
    this_part_of_my_application()
except ValueError as e:
    logger.error(e)
    
    

#6 final basic example from the docs just for pattern recognition
(x,y) = (5,0) #tuple unpacking
try:
  z = x / y
except ZeroDivisionError, e:  #DON'T USE this idiom b/c its deprecated in Py3 and "as e" is nicer!
  z = e # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
print z # output: "integer division or modulo by zero"
print "do we get here?"



#fun and possibly useful fact number 4080

#some of your favorite iterators are stopped with exceptions themselves

#__iter__() raises
#   StopIteration

#__getitem__() raises
#   IndexError



#Exception hierarchy
#https://docs.python.org/2/library/exceptions.html#exception-hierarchy


BaseException.__name__
BaseException.__subclasses__()

def classtree(cls, indent=0):
    print '.' * indent, cls.__name__
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)

classtree(BaseException)

print FloatingPointError.__mro__



#Multiple Exceptions using string services and the ever confusing codec!

def playwith_value_error(value):
    try: 
        return (unicode(value))
    except (ValueError, UnicodeError) as err:
        print(err)
    

print(playwith_value_error(3), type(playwith_value_error(3)))
print(playwith_value_error('a string?'), type(playwith_value_error('a string?')))
#what will fail?
print(playwith_value_error('\x80abc'), type(playwith_value_error('\x80abc')))




#self-defined Exceptions
class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyException(2*2)
except MyException as e:
    print('My exception occurred, value: {}'.format(e.value))
    

#self-defined Exceptions
class MySubbedException(ValueError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def word_concat(word1, word2):    
    try:
        concat = word1 + word2
    except:
        print('an exception')
    if (" ") not in concat:
        raise MySubbedException("There is no space in your concat word!")
    
    return concat
        
print(word_concat("hello", " world"))
#print(word_concat("hello", "world"))




#Quick Philosophy Notes

#Errors on functions are caused by a functions assumptions about its input are violated
#this is not just type checking! we're only going to concentrate on errors
#that are contained in the language but we could get into file errors, connection errors, disk space errors
#and can you think of others?
#exceptions allow you to move on in your code when you deem it necessary!

#won't exceptions just compound the places in your code where bugs can occur? 
#some say that exceptions are just like Pokemon
#rather the saying to remember is "catch what you can handle"
#your job to know when to except

#defensive coding: expecting the unexpected (and not always excepting it)

#break, continue are used when looping
