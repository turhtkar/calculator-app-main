from flask import jsonify
from app.models.user import User
from flask_jwt_extended import create_access_token
from app import mongo

def register_user(data):
    username = data.get('username')
    password = data.get('password')
    
    if User.find_by_username(username):
        return jsonify({"msg": "Username already exists"}), 400
    
    user = User(username, password)
    user.save()
    
    return jsonify({"msg": "User created successfully"}), 201

def login_user(data):
    username = data.get('username')
    password = data.get('password')
    
    user = User.find_by_username(username)
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Invalid username or password"}), 401