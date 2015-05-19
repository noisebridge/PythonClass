def countdown(n):
    print "Counting down!" 
    while n > 0:
        yield n # Generate a value (n) n -= 1

c = countdown(5)
c.next()

#call next() is python 2 or __next__() in Python 3

def gen_file_line(text):
    with open(text) as fp:
        for line in fp:
            yield line

dum_text = "dummyfile.txt"

