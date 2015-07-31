"""
A simple set of math methods that we can build our
logging infrastructure on top of.



"""
import logging, logging.config
import json

ADD_LOGGER_NAME = 'add_logger'


add_logger = logging.getLogger(ADD_LOGGER_NAME)


def add_some_numbers(a, b):
    """ Adds the passed parameters and returns the result.

    """

    return a + b


if __name__ == "__main__":
    """ Rudimentary tests, nothing should be returned. 

    In the event of a test failure, we get an AssertionError.
    """

    assert add_some_numbers(4,5) == 9
    assert not add_some_numbers(5,5) == 9

