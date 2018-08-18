from flask import Flask
import flask_cors
import flask_jwt_extended
import os

FLASK_NAME = os.environ.get("FLASK_NAME")
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


def create_app():
    app = Flask(FLASK_NAME, static_folder="../client/dist",
                template_folder="../client")
    app.secret_key = FLASK_SECRET_KEY

    # JWT
    jwt = flask_jwt_extended.JWTManager(app)

    return app


app = create_app()
