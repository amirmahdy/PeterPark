from flask import Flask
import flask_sqlalchemy
import app.config as config
from flask_migrate import Migrate

db = flask_sqlalchemy.SQLAlchemy()
migrate = Migrate()


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)
    
    return flask_app
