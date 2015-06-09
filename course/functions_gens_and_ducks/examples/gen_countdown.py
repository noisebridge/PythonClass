def countdown_from_n(n):
    print "Counting down!" 
    while n > 0:
        yield n # Generate a value (n) n -= 1

countdown = countdown_from_n(5)
countdown.next() 

#call next() is python 2 or __next__() in Python 3