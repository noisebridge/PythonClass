
"""
Now lets go for broke. 

This isn't our final version but it will expose you to the settings we will be configuring there.

Steps:
    1. Set up logger's 'name'.
    2. Specify a handler (FileHandler)
    3. Specify a formatter and attach it to the handler.
    4. Add the handler to the logger 'name'.
    5. Use the logger.

"""

import logging

myloglv = logging.DEBUG

mylogger = logging.getLogger('myrootlevel')
mylogger.setLevel(myloglv)

logger_handler = logging.FileHandler('example.log')

# Next lets add a filter. Review the generic function below.
myfilter = logging.Filter("root_lv.generic_function")
mylogger.addFilter(myfilter)

myformatter = logging.Formatter('%(asctime)s\t\t%(name)s\t\t%(levelname)s\t\t%(module)s:%(lineno)d\t\t%(message)s')
logger_handler.setFormatter(myformatter)

mylogger.addHandler(logger_handler)


# Now lets add some log events.
mylogger.debug("I'm a lumberjack and that's ok...")
mylogger.info("Your axe is getting dull...")
mylogger.warning("TIMBER!!!")
mylogger.error("Chainsaw out of gas.")
mylogger.critical("AAAHHHHHHHHHH!!!")


def generic_function():
    """
    This function illustrates a change in scope that we might want to log as a subspace of rootlevel
    """
    genlogger = logging.getLogger('myrootlevel.genfunc')
    for i in range(0,5):
        genlogger.debug("This is a current value of i: %s" % i)

    return

generic_function()

# The log hierarchy is tied to scope.
logger.info("This log statement is back in the parent level.")

