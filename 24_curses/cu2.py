
import curses
import curses.textpad


def potato(bananawindow):
    """ Curses is controlled from here.
        This might be called 'the loop' in a game.
    """

    def background():
        """ Writes the default background each screen rewrite.

        """
        bananawindow.border()
        bananawindow.bkgdset('+')

        winheight, winwidth = bananawindow.getmaxyx()
        winheight_str = str(winheight)
        winwidth_str = str(winwidth)
        bananawindow.addstr(winheight-2, winwidth-10, winheight_str)
        bananawindow.addstr(winheight-2, winwidth-10+len(winheight_str), ","+winwidth_str)

    background()
    keypress = int()
    # 113 is the lowercase 'q' key.
    while curses.keyname(keypress) != '^D':
        keypress = bananawindow.getch()
        bananawindow.erase()
        background()
        # Lets actually add the character to the screen now.
        bananawindow.addch(1,10,keypress)
        bananawindow.addstr(2,10,curses.unctrl(keypress))
        bananawindow.addstr(3,10,curses.keyname(keypress))


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


