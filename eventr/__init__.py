# global imports
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/hi')
    def hi():
        return 'Hi there'

    return app

