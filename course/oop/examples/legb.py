#print dir(__builtins__)

#print zip

class Zip(object):
    open = True

    def zip(self):
        if self.open == True:
            self.open = False
        else:
            self.open = True 
        return open


zip = Zip()

print zip



#zip.zip() 

#print zip.open