from flask import Flask
from flask_migrate import Migrate
from .model import configure

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/FLASK-API-BACKEND.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure(app) # passing config informations of database to app in Flask

    Migrate(app, app.db)
    return app