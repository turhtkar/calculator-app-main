from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
import certifi

mongo = PyMongo()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
    app.config.from_object(config_class)

    CORS(app, supports_credentials=True)
    
    # Update PyMongo initialization with SSL settings
    app.config['MONGO_URI'] = Config.MONGO_URI
    mongo.init_app(app, tlsCAFile=certifi.where())
    
    jwt.init_app(app)

    # Ensure the User collection exists
    with app.app_context():
        if 'User' not in mongo.db.list_collection_names():
            mongo.db.create_collection('User')

    from app.routes import auth, calculator
    app.register_blueprint(auth.bp)
    app.register_blueprint(calculator.bp)

    return app