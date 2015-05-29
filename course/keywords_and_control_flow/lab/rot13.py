# -*- coding: utf-8
"""
Goal: Encode a message using rot13.

"""

# Where is the message going to be coming from?
# Test case from wikipedia:
# http://en.wikipedia.org/wiki/ROT13
#message = "Why did the chicken cross the road?"
#wikipedia_result = "Jul qvq gur puvpxra pebff gur ebnq?"


def encode_with_rot13(message):
    """ Accepts a string. encodes it and returns the result string.
    
    (More detailed explanation to come)
    Steps:
    1. Accept the string as message.
    2a. Loop through the characters in the string.
    2b. If it is a letter 'apply the rot13 cipher' to the letter.
    2c. Else store the character without any change.
    3. Return the string.
    

    """
    def rotate_character(character, alphabet):
        """ Rotate a character on its alphabet.
        """
        rotated_index = (alphabet.index(character) + 13) % 26
        return alphabet[rotated_index]

    # We are ignoring case, we will use lowercase for all.
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    result_list = list()
    for character in message:
        if character in alphabet:
            result_list.append(rotate_character(character, alphabet))
        elif character in alphabet.upper():
            result_list.append(rotate_character(character, alphabet.upper()))
        else:
            result_list.append(character)
    result = ''.join(result_list)
    return result

message = raw_input("Enter your message:")

print(encode_with_rot13(message))


