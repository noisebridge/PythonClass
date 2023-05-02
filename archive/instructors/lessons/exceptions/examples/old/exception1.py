"""
Using a try/except pattern to restrict the user to certain input.

"""

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again"
        
