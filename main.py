from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('my_broadcast_event', namespace='/test')
def send_content(sent_data):
    content = sent_data['data']
    emit('my_content', {'data': content}, broadcast=True)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    socketio.run(app)
