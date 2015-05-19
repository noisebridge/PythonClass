'''doctest looks for lines beginning with 
the interpreter prompt, >>>, to find the beginning of a test case
'''
#python -m doctest -v example7-doctest.py

def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b