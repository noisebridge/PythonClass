a = lambda x: x + 1
print 'Type of a is', type(a)


# Simple function pointers..
# given a radius, what are some basic calculations?
circumference = lambda x: x * 2 * 3.14159
area = lambda x: x ** 2 * 3.14159
volume = lambda x: x ** 3
radius = 2



# Manuipulate lists easier
lis = [{"name": "Peter"}, {"name": "Josef"}]

# (1) Using lambdas
loop_dic = lambda i: {"name": i["name"] + " Wallace" }
new_lis = [loop_dic(i) for i in lis]
print new_lis

# (2) Using list comprehension
lis = [{"name": "Peter"}, {"name": "Josef"}]
new_lis = [{"name": i["name"] + " Wallace"} for i in lis]
print new_lis


# Nested lambdas
add_two = lambda n: n + 2
multiply_add_two = lambda n: add_two(n * 2) # Call lambda in lambda.

print(multiply_add_two(3))
print(multiply_add_two(5))