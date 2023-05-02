# Threading And Concurrent Programming in Python
This talk will discuss implementing
[concurrent programs](https://en.wikipedia.org/wiki/Concurrent_computing)
using the Python standard library, the role of the Global Interpreter Lock (GIL), and the difference between concurrency and parallelism.
If time allows, conventional strategies for circumventing the limitations
imposed by a GIL will be discussed.

**Update: it's a bit misleading that the title leads off with "threading."
The talk is more generally focused on concurrent programming.**

In this talk:
- Concurrency at a high level
- Coroutines in Python, as a means of introducing synchronization
- Threads in Python, with a look at sharing state instead of communicating
- Introduce the GIL, and identify it as a mutex

Not really in this talk: PyPy, `gevent`, `concurrent.futures`, `asyncio`, `multiprocessing`, IronPython/Jython, etc.

## PyClass News
Next Monday (the 25th,) PyClass will restart with a new cycle!

## Motivating Example
Suppose we need to explain in great detail the process of
swapping the engines of two cars.
We could write one long algorithm involving both cars.
Alternatively, we could write a short algorithm that involves pausing whenever
the engine has been removed.
The algorithm relinquishes the engine to the calling process
and waits until a different engine is provided to it,
at which point it installs the new engine.

Functions that involve such an exchange of control are called **coroutines**.

Now, we can:
- Write one coroutine and use it twice - once each for two cars of the same model.
- Write a coroutine for each model, and allow them to communicate with each other.

Food for thought:
- Does this design require more than one mechanic?
- Can this design be executed faster if more than one mechanic is available?

We've overlooked some things.
- With only one mechanic, the process itself is managing execution.
- How might the exchange of the engines be implemented? Do we have a solution that we can readily implement in a program? Do starting states exist in which our "program" can't complete?

## What is concurrency?
Suppose we have two or more tasks to execute.

If we only start when no other task is ongoing,
then we are executing them **sequentially**.
Otherwise, we are carrying them out **concurrently**.

**Parallel algorithms** distribute computations over
multiple devices or multiple processors,
whereas **serial** algorithms assume that
all computations must take place on a single processor.

Question: can we write a concurrent program that executes
in serial instead of in parallel?

So, we can think about several models now:
- Serial & sequential
- Serial & concurrent
- Parallel & concurrent
- "Embarrassingly" parallel (below)

## Sharing resources
If a parallel computation requires no shared resources or coordination
between processes,
then the problem being solved is said to be **embarrassingly parallel**.
However, this is not the case for most problems of interest.
For instance,
many processes may need access to a shared resource,
or one process may not be able to proceed until another has completed a certain task.
In fact, synchronizing communication and/or access to resources
is the [main challenge](https://en.wikipedia.org/wiki/Concurrency_control)
in designing concurrent programs.

Let's have a look at the
[Dining Philosophers Problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem).

## Coroutines
A simple means of synchronization is for a process to pause itself
and relinquish control to its calling process.

Python 3 has added several important features (like `async` and `await`)
to coroutines in recent years.
However, we're going to focus on the more primitive coroutine feature
that Python has had for a long time - the `yield` keyword.
(See also `sched_yield()` from the POSIX standard.)

### Simple examples
Here, we're using `yield` as an expression instead of as a statement.
If you've used generators before,
you've used `yield` to pass values back to the caller.
Here, we receive them instead.

```python
def push_and_print(q):
    while True:
        x = (yield)
        if x == '':
            return
        print(x)
        q.append(x)

q = []
p = push_and_print(q)
try:
    # p has to be primed in order to advance to the first `yield`
    p.send(None)
    l #=> []
    p.send('a') # prints 'a'
    l #=> ['a']
    p.send('b') # prints 'b'
    l #=> ['a', 'b']
    p.next() # Equivalent to p.send(None). Prints None.
    l #=> ['a', 'b', None]
    p.send('') #=> Raises StopIteration, like a generator. This needs to be caught.
except StopIteration:
    print('Done')
```

It happens that we can send and receive in one call.

```python
def echo():
    x = None
    while True:
        x = yield x

e = echo()
e.next()
e.send('Hello!')
```

```python
def repeat_last(initial=None):
    msg, old, new = None, None, initial
    while True:
        msg = yield old
        old, new = new, msg
        print('Old: {} New: {}'.format(new, old))

r = repeat_last('z')
msgs = [None, 'a', 'b', 'c']
print('(Priming)')
for msg in msgs:
    print('Sending: {}'.format(msg))
    res = r.send(msg)
    print('Received: {}'.format(res))

print('Sending: None')
r.next()
print('Sending: None')
r.next()
```

For more on coroutines, see David Beazley's talk,
[A Curious Course on Coroutines](http://www.dabeaz.com/coroutines/Coroutines.pdf).

## Threads

### Sharing State
However, sharing state is often viewed as an antipattern when it is unnecessary.
In fact, part of the Rob Pike's philosophy in designing Go
is that concurrent processes should **share state by communicating**,
as opposed to **communicating by sharing state**.

**Note: if you're coming from another language,
Python 2's `mutex` doesn't work the way you think it does.
It's meant for single-threaded contexts,
(CITATION NEEDED)
and is deprecated for a reason.
Use the synchronization objects from `threading`.)**

### Global Interpreter Lock
While Jython and IronPython actually do allow proper OS level threading
and PyPy provides green threads,
CPython (the reference implementation that you probably use)
does not allow for "proper" threading.
This is a constraint imposed by the use a **global interpreter lock**, or **GIL**.

It happens that the GIL is itself a mutex that prevents
a given Python process from controlling more than one native thread at once.

Here's a nice,
[in-depth discussion](https://code.tutsplus.com/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612)
that also has a nice table.

## Asyncio
If you're familiar with JavaScript,
you're probably familiar with its use of an event loop.
An **event loop** is a design pattern that enables the programmer to say,
"Do `f`. When `f` is complete, pass the output of `f` to the function `g`."
Here, `g` is a **callback**.
This can be accomplished by dedicating the main thread to the event loop,
as long as we restrict each such `f` to be a computation outsourced
to a different process or piece of hardware.
For instance, our program might need wait on the operating system
to provide a reply to an HTTP request made over a network.

In Python 3.4, coroutines have been improved to provide a similar model in the
[asyncio](https://docs.python.org/3/library/asyncio.html)
module of the standard library.
If you enjoyed the material in this talk,
then I highly encourage you to check out `asyncio`.
You might also like Go or Erlang, depending on your tastes.
