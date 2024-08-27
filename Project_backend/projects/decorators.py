from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from company_users.authentication import auth  
from company_users.models import CompanyUser


allowed_user_types = ['qa', 'manager']  

def check_user_access(func):
    @wraps(func)
    def check_access(request, *args, **kwargs):
        auth_token = request.headers.get('Authorization', '')
        
        print("Request headers:", request.headers)
        print('Your token is', auth_token)
        
        if not auth_token:
            return Response({"error": "Authorization token is missing"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            token = auth_token.split()[1]
            decoded_token = auth.decode_token(token)
        except IndexError:
            return Response({"error": "Invalid token format"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not decoded_token:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user_email = decoded_token.get('user_email')
        user_type = decoded_token.get('user_type')
        
        try:
            user = CompanyUser.objects.get(email=user_email)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if user_type not in allowed_user_types:
            return Response({"error": "User does not have permission to access this resource"}, status=status.HTTP_403_FORBIDDEN)
        
        return func(request, *args, **kwargs)  
    return check_access


allowed_user_type = ['manager']  

def check_user_access2(func):
    @wraps(func)
    def check_access(request, *args, **kwargs):
        auth_token = request.headers.get('Authorization', '')
        
        print("Request headers:", request.headers)
        print('Your token is', auth_token)
        
        if not auth_token:
            return Response({"error": "Authorization token is missing"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            token = auth_token.split()[1]
            decoded_token = auth.decode_token(token)
        except IndexError:
            return Response({"error": "Invalid token format"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not decoded_token:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user_email = decoded_token.get('user_email')
        user_type = decoded_token.get('user_type')
        
        try:
            user = CompanyUser.objects.get(email=user_email)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if user_type not in allowed_user_type:
            return Response({"error": "User does not have permission to access this resource"}, status=status.HTTP_403_FORBIDDEN)
        
        return func(request, *args, **kwargs)  
    return check_access




def validated_user(func):
    @wraps(func)
    def validate_user(request, *args, **kwargs):
        auth_token = request.headers.get('Authorization', '')
        if not auth_token:
            return Response({"error": "Authorization token is missing"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            token = auth_token.split()[1]
            decoded_token = auth.decode_token(token)
        except IndexError:
            return Response({"error": "Invalid token format"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not decoded_token:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)
        
        email = decoded_token.get('user_email')
        try:
            user = CompanyUser.objects.get(email=email)
        except CompanyUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        request.user = user
        return func(request, *args, **kwargs)
    return validate_user

