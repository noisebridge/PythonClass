### Python Profiling with Pyflame ###

#### Background ####
_Profiling_ involves measuring the performance of a
program while it runs.  It's a recommended first step
whenever you have some code which needs optimization.

Other forms of profiling - such as Memory Profiling - are
also possible, but we'll largely be considering CPU
profiling today, using a tool called Pyflame.


#### Pyflame ####
Pyflame is an open-source profiling tool developed by Uber.
It's a sampling profiler - it regularly 'inspects' the
program's state, and records the stack of Python functions
at that point in time.  Each entry in the stack will have
a filename, and file line number, and usually a function
name.

To help imagine the sample data Pyflame collects, here's
the familiar textual representation of a stacktrace:

```
  Example Stacktrace
  ---
  File "./test.py", line 57, in <module>
      bar()
  File "./test.py", line 55, in bar
      return foo()
  File "./test.py", line 50, in foo
      something_invalid()
```

We can attach Pyflame to programs that are already
running, and tune how frequently it will collect samples.

Higher sampling rates will be more accurate but do
introduce some additional CPU overhead.  By default Pyflame
samples a program 1000 times per second.


#### When to profile ####
