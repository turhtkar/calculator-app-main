from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import register_user, login_user

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.get_json()
    return register_user(data)

@bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.get_json()
    return login_user(data)