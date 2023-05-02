"""
Pil Sample
source (url): https://pillow.readthedocs.org/handbook/tutorial.html
"""

from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            myimage = Image.open(infile)
            # multiply each pixel by 1.2
            myimage = myimage.point(lambda i: i * 2)
            myimage.save(outfile)
        except IOError:
            print("cannot convert", infile)
