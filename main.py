from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('my_broadcast_event', namespace='/test')
def send_content(sent_data):
    content = sent_data['data']
    content2 = sent_data['data2']
    emit('my_content', {'data': content, 'data2': content2}, broadcast=True)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    socketio.run(app)
