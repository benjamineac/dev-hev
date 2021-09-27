from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'

    from .server import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app