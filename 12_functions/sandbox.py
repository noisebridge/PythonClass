#stub

def func():
    pass
    print 3

print func()

print(type(func))
type(func)


"""
#function attributes, really not necessary until advanced and highly specialized use case arises
def foo():
    pass

foo.attr1 = 1
foo.attr2 = 2

print(globals())
print(locals())

print(dir())
print(dir(foo))
#If a function does not have a return keyword, it will send a None value.
#know what functionality the interactive interpreter is giving you here 
"""
def outer():
    def inner1():
        return 1
    def inner2():
        return 2
    def inner3():
        return 3
    def inner4():
        return 4
    #all_inner_ls = [inner1, inner2, inner3, inner4]
    #for i in all_inner_ls:
    #    return i 
    return inner1, inner2, inner3, inner4

print("outer")
print(outer())

def make_usable_value():
    return_value = 5
    return return_value

print(make_usable_value)
print "before"
print dir()
make_usable_value()
print "after"
print dir()

#print(return_value)
print("globals", globals())
print("locals", locals())

def lets_use_old_function_and_add_one():
    new_return_value = make_usable_value() + 1
    return new_return_value

print lets_use_old_function_and_add_one()


print "pass by reference v. pass by value?"
n = [1, 2, 3, 4, 5]

print "Original list:", n

def f(x):
    x.pop()
    x.pop()
    x.insert(0, 0)
    print "Inside f():", x    
    
f(n)    

print "After function call:", n

#What we commonly refer to as "variables" in Python are more properly called names. 
#Likewise, "assignment" is really the binding of a name to an object. 
#Each binding has a scope that defines its visibility, 
#usually the block in which the name originates.

class InanimateCarbonRod(object):
    def __init__(self, color):
        self.color = color 

    def get_color(self):
        return self.color

rod = InanimateCarbonRod("green")
print rod.get_color()


def take_and_add_hella_args(simple_arg, *args):
    mult_args = args 
    print(mult_args)
    #for i in args:
    #    simple_arg += i
    #all_args_added = simple_arg + args
    return mult_args

print take_and_add_hella_args(10, (1,2,3,4,5))

def fprintf(file, fmt, *args): 
    with open(file, 'w') as fp:
        fp.write(fmt % args)
# Use fprintf. args gets (42,"hello world", 3.45) 
fprintf("out.txt","%d %s %f", 42, "hello world", 3.45)



def gen_tokens(text):
    """ str -> gen
    call split on our text when its a string
    """
    with open(text) as fp:
        fp = fp.read()
    for word in fp.split():
        yield word
    #or (word for word in fp.split() )
    
def gen_cleaner_words(text):
    """ str -> str
    removes commonly 'attached' punctuation marks such as ',''.''*word*' etc.
    note that this function does not remove any words from iterable
    """
    for i in gen_tokens(text):
        yield i.translate(None, "!@#$%^&*().,[]+=-_`~<>?:;")
