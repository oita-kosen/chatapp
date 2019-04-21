from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'm16.cloudmqtt.com'
app.config['MQTT_BROKER_PORT'] = 20145
app.config['MQTT_USERNAME'] = 'bqntusbe'
app.config['MQTT_PASSWORD'] = 'FSeMpNi8kNhF'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

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

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('device/sensor')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    emit('my_content', {'data': data['payload'], 'data2': data['payload']}, broadcast=True, namespace='/test')

if __name__ == '__main__':
    socketio.run(app)
