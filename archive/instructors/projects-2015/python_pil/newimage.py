"""
Create a new image.

"""

from PIL import Image

buff = ""

newimage = Image.new("RGBA",(100, 100), None)

newimage = newimage.point(lambda i: i + 257 )

newimage.show()

# PIL.Image.eval(image, *args) may allow us to achieve our goal
