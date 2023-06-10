from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.static_folder = 'static'

    from app.models.recipe import Recipe

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import recipes_bp
    app.register_blueprint(recipes_bp, url_prefix="/recipes")


    return app



