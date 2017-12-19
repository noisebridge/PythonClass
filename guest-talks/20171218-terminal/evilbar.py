from random import randint, random
from time import sleep

def cr(prompt=''):
    print('\r' + prompt, end='')

def show(s, prompt=''):
    cr(prompt)
    print(s, end='')

def randbar(size):
    this_size = randint(1, size)
    bar = load_char * this_size
    rest = ' ' * (size - this_size)
    return bar + rest

def evil_bar(prompt='', size=32, load_char='X', sleep_time=1, p=0.9):
    """Display a loadbar of randomly varying length for a random time.

    The number of steps is distributed geometrically with probability of not
    loading p. Each step takes roughly sleep_time.
    """

    show(load_char, prompt)

    while True:
        sleep(sleep_time)

        if random() > p:
            cr(prompt)
            print(load_char * size)
            break

        bar = randbar(size)
        show(bar, prompt)

if __name__ == '__main__':
    evil_bar('Loading: ')
