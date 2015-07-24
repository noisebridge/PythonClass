"""
Checks each line of a file for valid emails.

Use Django's email validator regex.

Store the result in one of 2 files:
    1. valid emails.
    2. invalid emails.


NOTE: This project still fails on a case when the email has a trailing string. This is because the re.match() method only matches the beginning of the string. We should match the whole string.
"""
import re


rough_email_validator = r'([^@|\s]+@[^@]+\.[^@|\s]+)'

email_validator_re = re.compile(rough_email_validator)

def build_emails_from_sample_file(filename):
    """
    """

    with open(filename, 'r') as f:
        l = list()
        for line in f:
            l.append(line.rstrip())

    if len(l) < 1:
        raise Exception, "The file had no data."

    return l


def write_list_to_file(mylist, output_filename):
    """
    """

    import json # move this to the top

    with open(output_filename, 'w') as f:
        json.dump(mylist, f)


if __name__ == '__main__':
    """ Run tests for our module.
    """

    SAMPLE_SOURCE_FILE = "source.txt"

    VALID_OUTPUT_FILE = "valid.txt"
    INVALID_OUTPUT_FILE = "invalid.txt"
    
    VALID_EMAILS = list()
    INVALID_EMAILS = list()

    for email in build_emails_from_sample_file(SAMPLE_SOURCE_FILE):
        
        if email_validator_re.match(email):
            print "Valid email: {}".format(email)
            VALID_EMAILS.append(email)
        else:
            print "Not a valid email: {}".format(email)
            INVALID_EMAILS.append(email)
    
    write_list_to_file(VALID_EMAILS, VALID_OUTPUT_FILE)
    write_list_to_file(INVALID_EMAILS, INVALID_OUTPUT_FILE)

