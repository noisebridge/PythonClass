"""
Pil Sample
source (url): https://pillow.readthedocs.org/handbook/tutorial.html
"""

from __future__ import print_function
import os, sys
from PIL import Image


def roll(image, delta):
    """Roll an image sideways
    
    (A more detailed explanation goes here.)
    """

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: 
        print("the delta was 0!")
        return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image


for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            myimage = Image.open(infile)
            
            myimage.save(outfile)

            myrolledimage = roll(myimage, 249)
            myrolledimage.save("rolled." + outfile)

        except IOError:
            print("cannot convert", infile)


