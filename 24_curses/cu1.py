
import curses
import curses.textpad


def potato(bananascreen):
    """ Curses is controlled from here.
        This might be called 'the loop' in a game.
    """

    curses.textpad.rectangle(bananascreen,0,0,10,10)

    keypress = int()
    # 113 is the lowercase 'q' key.
    while keypress != 113:
        keypress = bananascreen.getch()
        print curses.unctrl(keypress), keypress


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


