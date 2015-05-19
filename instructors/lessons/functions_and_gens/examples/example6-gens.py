from string import ascii_letters as ltrs
for index, letter in enumerate(ltrs):
   print index, letter

print enumerate(ltrs)
print list(enumerate(ltrs))


def dum_func():
    pass

x = dum_func()
print id(x)
y = dum_func()
print id(y)

def gen_lines_file(text):
    with open(text, 'rb') as fp:
        for line in fp:
            yield line 

#print list(gen_lines_file("dummy_file.txt"))

genl = gen_lines_file("dummy_file.txt")
print "id genl"
print id(genl)
print list(genl)

genl = gen_lines_file("dummy_file.txt")
print id(genl)
print genl.next()

for line in genl:
    print line

print "\n\n\n"

genl = gen_lines_file("dummy_file.txt")
print id(genl)
for line in genl:
    print line    

genl = gen_lines_file("dummy_file.txt")
print genl.next()
