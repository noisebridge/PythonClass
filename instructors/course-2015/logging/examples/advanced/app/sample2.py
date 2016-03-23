
import logging

def main():

    sample_log = logging.getLogger('ex2.'+__name__)
    return_val = "main func return val"

    sample_log.debug('example main function')
    sample_log.debug('return: %s' % return_val)

    return return_val

