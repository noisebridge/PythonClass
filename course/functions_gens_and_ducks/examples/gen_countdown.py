def countdown_from_n(n):
    print "Counting down!" 
    while n > 0:
        yield n # Generate a value (n) n -= 1
        n -= 1

countdown = countdown_from_n(5)

first_gen_var = countdown.next() 
print first_gen_var
print countdown.next()
print countdown.next()
print countdown.next()
print countdown.next()


countdown_from_ten = countdown_from_n(10)

#print len( list(countdown_from_ten) ) 
#print countdown_from_ten.next() 

xvar = xrange(3, 79, 3)

print xvar 

#call next() is python 2 or __next__() in Python 3

