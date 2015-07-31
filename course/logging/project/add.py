"""
A simple set of math methods that we can build our
logging infrastructure on top of.



"""
import logging, logging.config
import json

ADD_LOGGER_NAME = 'add_logger'
LOGCONFIG_FILENAME = 'logconfig.json'


add_logger = logging.getLogger(ADD_LOGGER_NAME)

with open(LOGCONFIG_FILENAME, 'r') as fp:
    logconfig = json.load(fp)

logging.config.dictConfig(logconfig)


def add_some_numbers(a, b):
    """ Adds the passed parameters and returns the result.

    """

    return a + b*2


if __name__ == "__main__":
    """ Rudimentary tests, nothing should be returned. 

    In the event of a test failure, we get an AssertionError.
    """

    try:
        result = add_some_numbers(4,5)
        expected_result = 9
        assert result == expected_result
        add_logger.info("PASS: Add succeeded, {} == {}".format(result, expected_result))
    except AssertionError:
        add_logger.info("FAIL: Add failed, {} != {}".format(result, expected_result))
                
    try:
        result = add_some_numbers(5,5)
        expected_result = 9
        assert not (result == expected_result)
        add_logger.info("PASS: Add failed, {} != {}".format(result, expected_result))
    except AssertionError:
        add_logger.info("FAIL: Add succeeded, {} == {}".format(result, expected_result))






