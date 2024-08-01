import os
from urllib.parse import quote_plus
import certifi

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # Update the MongoDB URI with SSL settings
    password = quote_plus("eq43opeLp8q0KEox")
    MONGO_URI = (
        f"mongodb+srv://orielsher1:{password}@fishycluster.l43rehd.mongodb.net/"
        f"fishyUsers?retryWrites=true&w=majority&tlsCAFile={certifi.where()}"
    )
    
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super-secret'
    JWT_TOKEN_LOCATION = ['headers']
    JWT_COOKIE_SECURE = False  # Set to True in production with HTTPS
    JWT_COOKIE_CSRF_PROTECT = True
