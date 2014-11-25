
import rot13


if __name__ == '__main__':
    """ Perform rotational encryption on an input.
    
    """

    target_file = 'mm.txt'
    state = 'r'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotation = 13
    
    rotation_dict = rot13.assign_and_return_positions(alphabet, rotation)

    # get source
    with open(target_file, state) as f:
        source = f.read()


    encoded_source = rot13.apply_substitution(rotation_dict, source)    

    print encoded_source
    print rot13.apply_substitution(rotation_dict, encoded_source)


