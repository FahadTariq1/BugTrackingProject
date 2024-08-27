import jwt
import datetime
from .models import CompanyUser
from django.conf import settings
import secrets
import os 
from zoneinfo import ZoneInfo

def generate_secret_key():
    return secrets.token_urlsafe(50)  
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', generate_secret_key())

class Authentication:
    def authenticate(self, email=None, password=None):
        try:
            user = CompanyUser.objects.get(user_email=email)
        except CompanyUser.DoesNotExist:
            return None
        else:
            if user.password == password: 
                return user
        return None

    def generate_token(self, user):
        payload = {
            'user_email': user.email,
            'user_type':user.type,
            'user_id': user.id
        }
        
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
        return token

    def decode_token(self, token):
        try:
            print('this is the token',token)
            decoded_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            return decoded_payload
        except jwt.ExpiredSignatureError:
            return None  
        except jwt.InvalidTokenError as exc:
            print(exc)
            return None 
        

auth = Authentication()