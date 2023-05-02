"""
This is an example of the control structures.
"""


if __name__ == "__main__":

    result = ""
    our_number = 21

    while result != "got it right":

        answer = raw_input("Choose a number:")
        answer = int(answer)

        if answer == our_number:
            result= "got it right"
        elif answer > our_number:
            result= "nope, lower"
        else:
            result= "nope, higher"
        
        print result

