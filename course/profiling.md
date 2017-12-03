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
It can be attached to existing processes, or used to
examine the performance of a new process.

Pyflame is a sampling profiler - instead of recording
every single function call, it rapidly 'inspects' the
state of a program, and records the current Python stack
during each snapshot.

We can attach Pyflame to programs that are already
running, and we can control the sampling rate it uses.
In general, higher sampling rates will be more accurate
but also introduce some level of performance overhead.
By default Pyflame will inspect a program 1000 times
per second.


#### When to profile ####
