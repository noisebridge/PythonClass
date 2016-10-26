"""
What the heck is inspect frames?

There wasn't a lot of documentation on frames available, except for using them to do 'frame hacks' and 'crazy monkey patch'
hacks when working with lxml. As such, I am not pursuing this.

"""
import inspect
import sys

def handle_stackframe_without_leak():

    cat = ["meow"]

    frame = sys.getframe(0)

    print frame
    try:
        print inspect.getframeinfo( frame )
        # do something with the frame
    finally:
        del frame
