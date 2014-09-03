l1 = range(0,100, 5)
l2 = range(0,660, 33)

paired_tup = zip(l1, l2)
print(paired_tup)

paired_dict = dict(paired_tup)
print(paired_dict)

numbered = dict(enumerate(paired_tup))
print(numbered)

sorted(numbered, reverse=True)

print type(numbered)

#add ten to each item in list
#for i in d:
#    d[i] += 10

#not sure what this does quite yet 

#packing tuples
greetings = 'hello', 'hi', 'hoohoo', 'hallo-o'
print(greetings)

h1 = greetings[0]
h2 = greetings[1]
h3 = greetings[2]
h4 = greetings[3]

print("unpack")
h1,h2,h3,h4 = greetings
print(greetings)

print("unpack")
greetings = h1,h2,h3,h4
print(greetings)


print(greetings[0])

for i in enumerate(greetings):
    print i

u = 'goodbye', 'bye', 'bubye', 'byebye-now'  
print(u)
