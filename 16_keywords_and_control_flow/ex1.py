
try:
    print yourmom
except Exception as e:
    print e

# The eval() will allow us to see the compiling error.
try:
    eval(
    """
try:
    and = 5
except Exception as e:
    print e
    """ 
    )
            
    # and = 5   # Uncommenting prevents this whole script from compiling. 
except Exception as e:
    print e


print "We made it to the end!"
