from flask import Flask
from flask_socketio import SocketIO,send,emit

list_task = []
data_id = 0
# create flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!Key'

#Creating the socket object
socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on('message')
def handleMessage(task):
    list_task.append(task)
    print(list_task)
    data_id = len(list_task)
    print(f'Task no:{data_id} {task}')
    #broadcasting the meesage to all connected users
    send(task,broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
