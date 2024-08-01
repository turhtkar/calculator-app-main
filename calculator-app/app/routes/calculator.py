from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.controllers.calculator_controller import perform_calculation

bp = Blueprint('calculator', __name__)

@bp.route('/calculate', methods=['POST', 'OPTIONS'])
@jwt_required()
def calculate():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.get_json()
    return perform_calculation(data)