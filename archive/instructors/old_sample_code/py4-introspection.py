"""
These will need to be run in a clean virtulenv to give an understanding of a clean install of python.... is this enough?

From: http://stackoverflow.com/questions/1006169/how-do-i-look-inside-a-python-object

type()
dir()
id()
getattr()
hasattr()
globals()
locals()
callable()

"""
import sys
import pkgutil

# List of built in modules, awesome.
print
print "sys.builtin_module_names:"
print sys.builtin_module_names
print

print "pkgutil.iter_modules:"
print( pkgutil.iter_modules)
print

print "dir(__builtins__)"
print dir(__builtins__)
print

#This seems quite complete, not sure where it pulls from though!
#help('modules')
