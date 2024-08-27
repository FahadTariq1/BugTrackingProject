from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from company_users.serializer import SignUpSerializer
from company_users.serializer import LoginSerializer
from company_users.serializer import AllDeveloperSerializer
from company_users.models import CompanyUser
from django.contrib.auth.hashers import make_password,check_password
from company_users.authentication import auth
from projects.decorators import check_user_access
from django.utils.decorators import method_decorator 


class Signup(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = CompanyUser.objects.create(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                type=serializer.validated_data['type'],
            )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = CompanyUser.objects.get(email=email)
            except CompanyUser.DoesNotExist:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

            if not check_password(password, user.password):
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

            token = auth.generate_token(user)
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class AllDeveloper(APIView):
    @method_decorator(check_user_access,name="dispatch")
    def get(self, request):
        try:
            bug_developers = CompanyUser.objects.filter(type='developer')
            if not bug_developers.exists():
                return Response({'message': 'No developers available'}, status=status.HTTP_404_NOT_FOUND)

            serializer = AllDeveloperSerializer(bug_developers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': 'An unexpected error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

