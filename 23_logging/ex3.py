

import logging
import logging.handlers

logger = logging.getLogger('root_lv')

log_lv = logging.INFO

logger.setLevel(log_lv)

formatter = logging.Formatter('%(asctime)s\t\t%(name)s\t\t%(levelname)s\t\t%(module)s:%(lineno)d\t\t%(message)s')

my_filter = logging.Filter("root_lv.generic_function")

logger.addFilter(my_filter)

logger_handler = logging.FileHandler('example.log')

logger_handler.setFormatter(formatter)

logger.addHandler(logger_handler)



# Now lets add some log events.
logger.debug("This is a test log.")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")


def generic_function():
    """
    """
    logger = logging.getLogger('root_lv.generic_function')
    for i in range(0,5):
        logger.debug("This is a current value of i: %s" % i)

    return

generic_function()

