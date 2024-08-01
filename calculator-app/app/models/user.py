from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        mongo.db.User.insert_one({
            'username': self.username,
            'password_hash': self.password_hash
        })

    @staticmethod
    def find_by_username(username):
        user_data = mongo.db.User.find_one({'username': username})
        if user_data:
            user = User(username, '')
            user.password_hash = user_data['password_hash']
            return user
        return None