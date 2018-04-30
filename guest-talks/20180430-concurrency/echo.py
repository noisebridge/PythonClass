def echo():
    print('Echo start')
    x = None
    while True:
        print('Echo top: {}'.format(x))
        x = yield x
        print('Echo bottom: {}'.format(x))
    print("This won't execute")

e = echo()
e.next()
e.send('Hello!')
