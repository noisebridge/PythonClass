"""
Create a new image.

"""

from PIL import Image
import random


def colormutator(*args):
    """
    Return a random color each time it is called
    """
    myint = random.randint(0,255)
    print myint
    return myint


buff = ""

newimage = Image.new("RGBA",(100, 100), None)

#newimage = newimage.point(lambda i: i + 255 )
newimage = Image.eval(newimage, colormutator)

newimage.show()

# PIL.Image.eval(image, *args) may allow us to achieve our goal
