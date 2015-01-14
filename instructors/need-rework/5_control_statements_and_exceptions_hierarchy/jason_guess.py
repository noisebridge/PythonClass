def guess_number():
    answer=None
    our_number=21

    while answer != our_number:
        answer=int(raw_input('guess me'))
        if answer == our_number:
            print "correct"
            return
        elif answer > our_number:
            print "no, higher"
        else:
            print "no, lower"

    return our_number

if __name__ == '__main__':
       guess_number()
