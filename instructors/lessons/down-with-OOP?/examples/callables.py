class Entity(object):
    '''Class to represent an entity. Callable to update the entity's position. Very esoteric ;)'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''Change the position of the entity.'''
        self.x, self.y = x, y

    def __str__(self):
        '''Return some info about this Entity'''
        return "coordinates: x {0}, y {1}".format(self.x, self.y)

e = Entity(24, 8, 3)

print e

e(12,2)

print e