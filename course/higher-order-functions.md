
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

# lets make some specific functions based on our original function
multip2 = functools.partial(multip, 2)
multip3 = functools.partial(multip, 3)
multip4 = functools.partial(multip, 4)
multip5 = functools.partial(multip, 5)

my_values = range(1,4)

print my_values

print("original", multip(*my_values))
print("x2", multip2(*my_values))
print("x3", multip3(*my_values))
print("x4", multip4(*my_values))
print("x5", multip5(*my_values))
```

#### Unpacking the Deep Dive

List sections here as we flesh them out

1. What is a [partial](https://docs.python.org/2/library/functools.html#functools.partial)
    - [partial parameters](https://docs.python.org/2/library/functools.html#partial-objects)?
    






