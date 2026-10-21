from flask_socketio import SocketIO  # pyright: ignore[reportMissingModuleSource]

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

socketio = SocketIO(app)