from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

mongo = PyMongo()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../../frontend/build', static_url_path='/')
    app.config.from_object(config_class)

    CORS(app, supports_credentials=True)
    mongo.init_app(app)
    jwt.init_app(app)

    from app.routes import auth, calculator
    app.register_blueprint(auth.bp)
    app.register_blueprint(calculator.bp)

    return app