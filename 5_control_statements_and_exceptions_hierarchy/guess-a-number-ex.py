"""
This is an example of the control structures.
"""


result = ""
our_number = 21


def test_number(answer):

    answer = int(answer)

    if answer == our_number:
        return "got it right"
    elif answer > our_number:
        return "nope, lower"
    else:
        return "nope, higher"


while result != "got it right":
    result = test_number(raw_input("Choose a number:"))
    print result

