"""Initialize Flask app."""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False, static_folder='../frontend/build', static_url_path='')
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app