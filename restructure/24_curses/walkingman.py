"""
We can make some slight modifications to example two and get an @ symbol walking around.

Now this could be the basis for a game.

Extensions:
    Let certain coordinates trigger actions.
"""

import curses
import curses.textpad
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN


def potato(bananawindow):
    """ Curses is controlled from here.
        This might be called 'the loop' in a game.
    """

    coords = [10, 10]
    curses.curs_set(0)

    def background(winheight, winwidth):
        """ Writes the default background each screen rewrite.

        """
        
        bananawindow.border()
        bananawindow.bkgdset('+')

        coordheight_str = str(coords[0])
        coordwidth_str = str(coords[1])
        bananawindow.addstr(winheight-2, winwidth-10, coordheight_str)
        bananawindow.addstr(winheight-2, winwidth-10+len(coordheight_str), ","+coordwidth_str)

    winheight, winwidth = bananawindow.getmaxyx()
    background(winheight, winwidth)
    keypress = int()
    # Allow a clean exit with ctrl+d
    while curses.keyname(keypress) != '^D':
        keypress = bananawindow.getch()
        # Add the background.
        if keypress == KEY_DOWN and coords[0] < winheight-2:
            coords[0] += 1
        if keypress == KEY_UP and coords[0] > 1:
            coords[0] -= 1
        if keypress == KEY_RIGHT and coords[1] < winwidth-2:
            coords[1] += 1
        if keypress == KEY_LEFT and coords[1] > 1:
            coords[1] -= 1
        bananawindow.erase()
        winheight, winwidth = bananawindow.getmaxyx()
        background(winheight, winwidth)
        bananawindow.addch(coords[0], coords[1],'@')


if __name__ == "__main__":
    """
    The documentation for curses.wrapper(<func>) is here:  
        https://docs.python.org/2/library/curses.html#curses.wrapper

        # Before calling main, curses.wrapper(main): 
            turns on cbreak mode, 
            turns off echo, 
            enables the terminal keypad, and 
            initializes colors if the terminal has color support. 
        # On exit (whether normally or by exception) it:
            restores cooked mode, 
            turns on echo, and 
            disables the terminal keypad.
    
    The wrapper function is passing a window into main. Main is defined above
    as taking one argument.  That argument is the window. We could also name
    it banana.

    """
    # curses.wrapper(main) # a more serious name for the main function
    curses.wrapper(potato) # but call the function whatever you want, i called it potato


