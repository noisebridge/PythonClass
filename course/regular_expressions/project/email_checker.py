"""
Checks each line of a file for valid emails.

Use Django's email validator regex.

Store the result in one of 2 files:
    1. valid emails.
    2. invalid emails.

"""
import re


rough_email_validator = r'([^@|\s]+@[^@]+\.[^@|\s]+)'

email_validator_re = re.compile(rough_email_validator)



if __name__ == '__main__':

    initial_email = "email@email.email"
    bad_email = "me@@@test"

    if email_validator_re.match(initial_email):
        print "Valid email: {}".format(initial_email)
    else:
        print "Not a valid email: {}".format(initial_email)

    if email_validator_re.match(bad_email):
        print "Valid email: {}".format(bad_email)
    else:
        print "Not a valid email: {}".format(bad_email)


