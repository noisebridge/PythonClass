# Python and the Terminal

## Terminal Emulator vs. Console
See [one](https://superuser.com/questions/144666/what-is-the-difference-between-shell-console-and-terminal)
of these [two](https://askubuntu.com/questions/506510/what-is-the-difference-between-terminal-console-shell-and-command-line)
great Q&A discussions on the matter.

## Escape Sequences
Historically, terminals would communicate over 8-bit serial lines.
While most codepoints were reserved for characters,
some were used as [control characters](https://en.wikipedia.org/wiki/Control_character).
Below, we'll talk specifically about `0x0A`, `0x0D`, and `0x1B`,
which are known as line feed (LF), character return (CR), and escape (ESC), respectively.
(10, 13, and 27 in ASCII.)

There were only so many characters available for this purpose,
but ESC was used to expand this by adding [escape sequences](https://en.wikipedia.org/wiki/Escape_sequence).
In short, an ESC would be sent to indicate that the following bytes were part
of an escape sequence.
Introducing more bytes meant more control operations could be specified.

(TODO Add a bit more on this.)

## Parsing Arguments to CLI Applications
The Python standard library includes [argparse](https://docs.python.org/3/library/argparse.html),
as well as a [tutorial](https://docs.python.org/3/howto/argparse.html#id1)
on the module.

Armin Ronacher gave us [Click](http://click.pocoo.org/5/),
which makes it easy to create this kind of application.
Click provides a clean decorator API,
and it's designed to allow for different Click applications to be nested.
That is, a Click application can load another Click application,
with the latter's commands appearing as subcommands of the former.

## Terminal Drawing With Control Characters
You're probably familiar with the role of the line feed character `\n`.
As data, it usually serves to delimit the lines of text files.
However, as a control character,
it also influences how text is printed to the screen.

There's a related character, `\r`, called carriage return,
which moves the cursor to the beginning of the line.
This behavior mimics the behavior of typewriters,
and *it allows us to redraw the line currently being printed.*

Note that, in order to prevent the cursor to the next line
when calling `print()`, we can call `print("foo bar", endwith='')`.

```python
from time import sleep

def scroll(s, n):
    print(s, end='')
    for i in range(1,n+1):
        sleep(1)
        print('\r', end='')
        print(i*' ' + s, end='')

    print()

scroll('a', 10)
```

For a slightly more involved example, see `evil_bar.py` for a silly loading bar
that randomly reports its progress.
For useful libraries you might want to use, see
[tqdm](https://github.com/tqdm/tqdm) for progress bars
and
[halo](https://github.com/ManrajGrover/halo) for loading spinners.
