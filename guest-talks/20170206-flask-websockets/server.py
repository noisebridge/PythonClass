from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)




@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message)


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


@app.route('/')
def client():
    return """
    <html>
        <body>
            <form>
                <input/>
            </form>

            <script>

                var w = new WebSocket('ws://localhost:5000/chatroom')

                w.onmessage = msg => {
                    var p = document.createElement('p')
                    p.innerText = msg.data
                    document.body.append(p)
                }

                var input = document.querySelector('input')
                var form = document.querySelector('form')

                form.onsubmit = () => {
                    w.send(input.value)
                    input.value = ''
                    return false
                }
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
