from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """
    Create and configure an instance of the Flask application.
    This function initializes the Flask application, loads configuration
    settings from the specified configuration class, and returns the app instance.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.health_check import health_check_routes

    app.register_blueprint(health_check_routes)

    return app