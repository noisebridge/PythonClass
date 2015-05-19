"""
This needs to be nicer. It would be smart to use the doctest
module to build this into an explorable framework for learning
how compound conditionals are tested in python.

This is applicable to euler problem 1.


This mini lesson also is very relevant to the concept of truth tables.


The english language uses exclusive or, also known as 'xor'.

Programming uses inclusive or, which is known merely as 'or'.


Students: Please note how these compound comparisons are reduced to simply True or False.
The if statement merely evaluates one of two statements after reducing the statement:

if True:
    print "True"
if False:
    print "This never gets reached."
"""


if 3 == 3:
    print "True"

if 3 == 4:
    print "False"

if True == True:
    print "True"

if True:
    print "True":

if False == False:
    print "True"

if False:
    print "False"

if False and True:
    print "False"

if True and True:
    print "True"

if False and False:
    print "False"

if True or True:
    print "True"

if False or False:
    print "False"

if True or False:
    print "True"
if False or True:
    print "True"
