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
            myimage.show()
            myimage.save(outfile)
        except IOError:
            print("cannot convert", infile)
