from flask import Flask, render_template
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'

    from .server import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app