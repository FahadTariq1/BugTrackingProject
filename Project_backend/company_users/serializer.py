from rest_framework import serializers
from company_users.models import CompanyUser

class SignUpSerializer(serializers.Serializer):
    name = serializers.CharField() 
    email = serializers.EmailField() 
    password = serializers.CharField() 
    type = serializers.ChoiceField(choices=CompanyUser.Choices) 
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class AllDeveloperSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField() 

