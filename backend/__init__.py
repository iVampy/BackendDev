"""Initialize Flask app."""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()
login_manager = LoginManager()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # flask swagger configs
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "School Portal Application API"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app

from .models import User
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))