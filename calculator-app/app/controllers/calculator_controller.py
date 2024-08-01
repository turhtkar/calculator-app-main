from flask import jsonify
from app import mongo

def perform_calculation(data):
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')
    
    result = None
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({"error": "Cannot divide by zero"}), 400
    
    calc_id = mongo.db.calculations.insert_one({
        'num1': num1,
        'num2': num2,
        'operation': operation,
        'result': result
    }).inserted_id
    
    return jsonify({'result': result, 'id': str(calc_id)})