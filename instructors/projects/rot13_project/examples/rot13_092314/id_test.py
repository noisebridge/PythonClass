




def cat_tester(cat):

    print "inside function, before assignment:", id(cat)
    print cat
    cat += " twice"
    print "inside function, after assignment", id(cat)
    print cat

    return cat

if __name__ == "__main__":

    cat = "meow"

    print cat

    print "outside function, before assignment:", id(cat)
    cat = cat_tester(cat)
    print "outside function, after assignment:", id(cat)

    print cat
    cat = cat_tester(cat)
