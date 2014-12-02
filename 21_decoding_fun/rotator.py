
import rot13


if __name__ == '__main__':
    """ Perform rotational encryption on an input.
    
    """

    source_file = 'cc.txt'
    state = 'r'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotation = 13

    output_file = 'ccenc.txt'
    output_mode = 'w'
    
    rotation_dict = rot13.assign_and_return_positions(alphabet, rotation)

    # get source
    with open(source_file, state) as f:
        source = f.read()

    print rotation_dict

    encoded_source = rot13.apply_substitution(rotation_dict, source)

    print encoded_source

    with open(output_file, output_mode) as f:
        f.write(encoded_source)

