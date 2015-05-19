
"""
Introduction to lamba syntax and simple use cases.  Open up an interpreter
and play around.  This is forming the building blocks to do some useful things
later on.
"""


def increment_func(x):
    return x + 1

increment_lambda = lambda x: x + 1

val = 40
print 'increment_func(val)=', increment_func(val)
print 'increment_lambda(val)=', increment_lambda(val)

print 'Type of ', increment_func, ' is', type(increment_func)
print 'Type of ', increment_lambda, ' is', type(increment_lambda)


# directly calling a lambda function. Probably no reason ever to do this
val = (lambda x: x ** 2 + 1)(3)
print 'goofy example:', val

# ----------------------------------------------------------
# As a function pointer
# given a radius, what are some basic calculations?
circumference = lambda x: x * 2 * 3.14159
area = lambda x: 3.1415 * x ** 2
volume = lambda x: 4 / 3 * 3.1415 * x ** 3
operation = circumference

print 'operation(2.0)=', operation(2.0)

# Note that our lambda function is an object.  Therefore
# it can be passed as an argument
def perform_operation(func, value):
    return func(value)

print 'perform_operation(...)=', perform_operation(area, 1.0)

# ----------------------------------------------------------
# Multiple arguments to lambda function
scaler = lambda x, y: x * y
values = range(10)
scale = 2
scaled_values = [scaler(i, scale) for i in values]
print 'scaled_values = ', scaled_values

# ----------------------------------------------------------
# Nested lambdas
add_two = lambda n: n + 2
multiply_add_two = lambda n: add_two(n * 2)  # Call lambda in lambda.

print(multiply_add_two(3))
print(multiply_add_two(5))
