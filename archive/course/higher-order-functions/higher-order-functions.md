
### Higher Order Functions

#### Ten Thousand Foot View

A function that acts on or `returns` another function.


#### 5 Minute Deep Dive - [Functools](https://docs.python.org/2/library/functools.html)

```python
import functools

def multip(*args):
    """ return the accumulated total of all arguments multiplied together
    """
    accumulated_total = 1
    for i in args:
        accumulated_total *= i

    return accumulated_total

my_values = range(1,4)

print("values:", my_values)

print("original:", multip(*my_values))

# lets make a partial from the original function and functools.partial
multip2 = functools.partial(multip, 2)
print("x2:", multip2(*my_values))

multip3 = functools.partial(multip, 3)
print("x3:", multip3(*my_values))

multip4 = functools.partial(multip, 4)
print("x4:", multip4(*my_values))

multip222 = functools.partial(multip, 2, 2, 2)
print("x2x2x2", multip222(*my_values))

mymultiplier = multip
print(mymultiplier(10,20))

my_function_list = list()
my_function_list.append(multip)
my_function_list.append(multip2)
my_function_list.append(multip3)
my_function_list.append(multip222)

for i in my_function_list:
    print(i(1,2,3,4))

for i in range(100):
    my_functions.append(functools.partial(multip, i))

for i in my_functions:
    print(i(1,2,3))

```

#### Unpacking the Deep Dive

List sections here as we flesh them out

1. What is a [partial](https://docs.python.org/2/library/functools.html#functools.partial)
    - [partial parameters](https://docs.python.org/2/library/functools.html#partial-objects)?
    
    - talked about first class objects
        - called a function from its index on a list

    - talk about scope

#### Function Scope, Global Scope, LEGB

    - LEGB = Local, Enclosing, Global, Builtins




