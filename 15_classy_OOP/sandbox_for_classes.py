#stub

class Pillow(object):
    """This is a comfy pillow"""

    def __init__(self, upholstery='linen', stuffing_type='cotton', stuffing_capacity=100, size=None):
        self.upholstery = upholstery
        self.stuffing_type = stuffing_type
        self.stuffing_capacity = stuffing_capacity
        self.size = (9,24)
        self.active = True

    def get_area(self):
        return self.size[0] * self.size[1]

    def hit_someone(self, hit_object=10):
        """self.int -> self.int 
        lose stuffing capacity points equal to size of hit object"""

        self.stuffing_capacity -= hit_object

        if self.stuffing_capacity <= 0:
            self.active = True


    def __str__(self):
        #note that reversing two methods would recurse
        return "this is an override: {}".format(self.__repr__())

