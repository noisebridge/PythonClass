import curses

def main(stdscr):
    """ Curses is controlled from here.
        This might be called 'the loop' in a game.

        game loop: http://gameprogrammingpatterns.com/game-loop.html
    """

    curses.textpad.rectangle(stdscr,0,0,10,10)

    keypress = int()
    # 113 is the lowercase 'q' key.
    while keypress != 113:
        keypress = stdscr.getch()
        print keypress


if __name__=='__main__':
    """
    This is our most basic model.

    This presupposes you know how to read a try... finally... block.
    For now, put it in your 'to learn' notes.

    You can come back to this to see the components initialized by curses.wrapper.

    This code is pretty identical to example 1.
    Moving on!!
    """
    try:
        stdscr=curses.initscr()
        curses.noecho() ; curses.cbreak()
        stdscr.keypad(1)
        main(stdscr)                        # Enter the main loop
    finally:
        stdscr.erase()
        stdscr.refresh()
        stdscr.keypad(0)
        curses.echo() ; curses.nocbreak()
        curses.endwin()                     # Terminate curses
