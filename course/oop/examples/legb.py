print dir(__builtins__)

class Zip(object):
    open = True

    def zip(self):
        if self.open == True:
            self.open = False
        else:
            self.open = True 
        return open


zip = Zip()

zip.zip() 

print zip.open