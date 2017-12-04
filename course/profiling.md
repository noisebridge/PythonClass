### Python Profiling with Pyflame ###

#### Background ####
_Profiling_ involves measuring the performance of a
program while it runs.  It's a recommended first step
whenever you have some code which needs optimization.

This class covers the most common form of profiling,
which is 'execution time' profiling.  Other forms of
profiling are possible, including memory usage
profiling.


#### Pyflame ####
Pyflame is an open-source profiling tool developed by Uber.
It's a sampling profiler - it regularly 'inspects' the
running program's state, and records the stack of Python
functions at that point in time.

Unfortunately Pyflame is currently only available on Linux,
but most of the principles here also apply for other
profiling tools.


#### Refresher: Stacks #####
Each entry in a Python call stack includes a filename
and a file line number.  If the line is part of a function,
we can also retrieve the name of the function.

To help imagine the sample data Pyflame collects, here's
a textual representation of a stacktrace:

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
running without having to change any code, and we can
configure the rate at which we will 'sample' the stack.

Higher sampling rates will be more accurate but do
introduce some additional CPU overhead.  By default Pyflame
samples a program 1000 times per second.


#### Flamegraphs ####
So what do we do once we have collected all our program
samples?

We typically want to visualize the data in a way which
makes it clear 'where' the program is spending most of its'
time -- i.e. which functions we can focus on to increase
the performance of the program.

Flamegraphs are a popular tool for this purpose; included
below is an example of a flamegraph for a Python program
trace.

![example](profiling/flamegraph.png)


#### Example ####
Let's use Pyflame to examine where most of the execution
time is spent when we run an example, and then use the
results to make directed performance improvements.

```
def lowercase(string):
    return string.lower()

# Concatenate using a loop
def concat_loop(strings):
    result = ''
    for string in strings:
        result += ','
        result += lowercase(string)
    return result

# Concatenate using string.join
def concat_join(strings):
    return ','.join([lowercase(string) for string in strings])

# Read in the system dictionary and produce a
# comma-separated
# list of lowercase words
strings = open('/usr/share/dict/words').readlines()
concat_loop(strings)
concat_join(strings)
```
