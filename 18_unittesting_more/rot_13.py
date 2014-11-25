# -*- coding: utf-8 -*-
"""

Goals:
    1. Somehow 'clean up' the string to deal with characters not in the radix.
        Sanitize or disregard? 
        There could be spaces or other characters that aren't a part of a-z 'radix'.
        a.  The allowed radix - http://en.wikipedia.org/wiki/Radix
    2. Take a message; return an encrypted version of the message.
    
    3. Rot N?  Decrypt message?
    4. Create tests? TDD?

We didn't define a few specifics:

    1. Where do we get our input?
        A string variable.
    2. Where do we put our output?
        We will print the output for now.
    3. We decided to disregard non alphabet characters and include them unaltered in the encrypted version of the message.

"""

"""
Idea for dealing with characters that aren't part of the radix:
    send pieces to whatever is running the encryption.
    1. isalpha function? is this good enough for a-z? in a for loop?
    2. we can use a method that lowercases the string -- 
    3. 
"""

"""
How do we do the rot13?
"""

ordered_rot13_radix = 'abcdefghijklmnopqrstuvwxyz'

def do_rot13_on_input(input_string, ordered_radix=ordered_rot13_radix):
    """ Perform a rot13 encryption on the provided message.

    """
    encrypted_message = str()

    for char in input_string:
        # Two possibilities: in radix, or NOT in radix.
        if char in ordered_radix:
            # must find index of the char in the ordered_radix
            char_index = ordered_radix.index(char)
            mod_char_index = (char_index + 13) % len(ordered_radix)
            mod_char = ordered_radix[mod_char_index]
            encrypted_message += mod_char
        else:
            encrypted_message += char

    return encrypted_message


def prepare_red_message(red_message):
    """ Prepare the red message before encrypting.

    """
    red_message = red_message.lower()

    return red_message

if __name__ == "__main__":
   
    # Test cases this covers: capital letters, punctuation (not in radix), and numbers.
    red_message = "Cats like to say meow; meet the cats under the animal tower at 2400h."

    #radix = (a..z)

    # how do we deal with wrapping on the index << problem to solve during encoding
    
    prepared_red_message = prepare_red_message(red_message)
    
    black_message = do_rot13_on_input(prepared_red_message)
    
    print red_message

    print black_message
    
    red_message_2 = do_rot13_on_input(black_message)

    print red_message_2

