'''LEGB: Locals, Enclosing, Global, Builtins 
'''

attr1 = 'dull'
print "locals are {}".format(locals())
print '\n'

class Product(object):

    

    def __init__(self):

        self.attr1 = 'sharp'

    def meth(self):
        def func():
            return 555
        return func()



print attr1

prod = Product()

print prod.attr1