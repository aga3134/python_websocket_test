from flask import Flask
from flask_sockets import Sockets
from flask import render_template

app = Flask(__name__)
sockets = Sockets(app)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        print(message)
        ws.send(message)

if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()