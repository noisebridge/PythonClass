class Integer(object):
    '''basic and subjective implementation of a user defined Integer type
    '''

    def __init__(self, value=None):
        self.value = value

    def add_value(self, value):
        self.value = value

    def convert_val_to_str(self):
        self.value = self.__str__()

    def conv_val_to_str(self):
        self.value = str(self.value)

    def conv_to_str(self):
        return str(self.value)

print bin(593)
