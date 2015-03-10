"""
An extremely basic implementation of a partial.

"""
import functools


def pythagorean(a, b):

    return a**2 + b**2

pythagorean_partial = functools.partial(pythagorean, 5)

print pythagorean_partial.func
print pythagorean_partial.args
print pythagorean_partial.keywords

print pythagorean_partial(3)
#print pythagorean_partial(b=3) # This also works...



def pythagorean2(a=1, b=1):

    return a**2 + b**2

pythagorean_partial2 = functools.partial(pythagorean2, a=5)


print pythagorean_partial2.func
print pythagorean_partial2.args
print pythagorean_partial2.keywords

# Must supply keywords here, dicts are unordered.
print pythagorean_partial2(b=2)

