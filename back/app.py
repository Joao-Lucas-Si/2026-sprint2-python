from flask_socketio import SocketIO  # pyright: ignore[reportMissingModuleSource]

from flask import Flask

app = Flask(__name__)

socketio = SocketIO(app)