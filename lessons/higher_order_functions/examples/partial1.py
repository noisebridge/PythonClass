"""
An extremely basic implementation of a partial.

"""
import functools


def pythagorean(a, b):

    return a**2 + b**2


pythagorean_partial = functools.partial(pythagorean, 5)

print pythagorean_partial(1)
