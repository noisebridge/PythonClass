import time


def foo():
    time.sleep(1)
    baz(1)


def bar():
    time.sleep(1)
    baz(5)


def baz(sleeptime):
    time.sleep(sleeptime)

foo()
bar()
