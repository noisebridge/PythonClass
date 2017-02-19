# Flask Websockets

Standard Flask request-response interaction:

1. Client sends request
2. Server reads request
3. Server sends response
4. Server & client close their ends of the connection

(The client and server can negotiate a connection which is kept open, but nothing happens until the client makes another request. If something is novel on the server side, the client won't know until it makes another request)

Websocket interaction:

1. Client sends websocket handshake request
2. Server upgrades connection to websocket
3. ANYTHING GOES (full duplex)

# Echo example

```python
@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message)
```

```sh
pip install -r requirements.txt
python2 server.py &

pip install websocket-client
python client.py
$ wsdump.py ws://localhost:5000/echo
Press Ctrl+C to quit
> rere
< rere
```

# Chat example

```python
clients = []


@sockets.route('/chatroom')
def chatroom(ws):
    clients.append(ws)

    while not ws.closed:
        try:
            message = ws.receive()

            for client in clients:
                client.send(message)
        except:
            break

    clients.remove(ws)
```

```
python2 server.py
# Now go to localhost:5000 in the browser
```

# How to deploy using heroku

See https://github.com/heroku-examples/python-websockets-chat.
