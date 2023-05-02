def push_and_print(q):
    while True:
        x = (yield)
        if x == '':
            return
        print('push_and_print: {}'.format(x))
        q.append(x)

q = []
p = push_and_print(q)
try:
    # p has to be primed in order to advance to the first `yield`
    p.send(None)
    print(q)    # []
    p.send('a') # 'a'
    print(q)    # ['a']
    p.send('b') # 'b'
    print(q)    # ['a', 'b']
    p.next()    # Equivalent to p.send(None). Prints None.
    print(q)    # ['a', 'b', None]
    p.send('')  # Raises StopIteration, like a generator. This needs to be caught.
except StopIteration:
    print('Done')
