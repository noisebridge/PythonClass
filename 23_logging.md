

### logging: A Python Standard Library Module
The Python logging library is a complex and configurable tool for logging events in your code, it is a core Python skill.  At the most basic, is a replacement for the print statements frequently scattered through code for debugging. For short scripts where you don't want a lot of setup, use basicConfig, which only adds one line to your code.  For longer projects, you'll want to use a lot more logging infrastructure, which we will discuss in detail. Note that print statements are acceptable for standard output to the console that the user will need to use the application, and that basicConfig goes to standard error by default.


### 1. Basic setup
- We will be using Python 2.  Not 3!  Feel free to learn Python 3 logging later! Concepts translate!
- [logging is in the standard library](https://docs.python.org/2/library/logging.html), so you will need to `import logging`, but it comes installed.
- `logging.basicConfig(level='INFO')` - This is all we need (also you need to import logging)
- [What's a log level? Great question!](https://docs.python.org/2/library/logging.html#logging-levels) You can also make your own custom levels, we won't do that today.
- Now lets make a logging event: `logging.debug("let's pass the debug level a string.")`
- This is good enough to replace print statements in any tiny scripts you do.
- Now lets send this to a file! `logging.basicConfig(filename='example.log', level='INFO')`
- Increase the log level to hide our statements. Change to `logging.basicConfig(filename='example.log', level='DEBUG')`

That's a serious advantage, we just turned something that creates extra work (commenting, uncommenting, and removing print statements) to a valuable tool that should remain in the code forever, and we did it in 2 lines of code.

### 2. Advanced Logging - Lets build our own logger!
- This gives us access to much more powerful options: handler, format, filter.
- What's a handler? It's an object defining how each log event's data is handled.
- Format? Examples: date, log-level, name, filename, line number, logged message.
- Filter - We will cover how to filter by name in order to only capture one function.



