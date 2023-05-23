from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.static_folder = 'static'

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
        # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("RENDER_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.recipe import Recipe

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import recipes_bp
    app.register_blueprint(recipes_bp, url_prefix="/recipes")


    return app


