from flask import Flask
# from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from base.config import Config
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from base.main.routes import main
    app.register_blueprint(main)
    return app
