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
