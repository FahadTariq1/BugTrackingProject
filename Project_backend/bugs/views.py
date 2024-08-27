from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from company_users.authentication import auth
from rest_framework import status
from projects.decorators import validated_user
from projects.decorators import check_user_access
from django.utils.decorators import method_decorator 
from bugs.models import Bug
from bugs.serializer import BugsSearchByProjectSerializer
from bugs.serializer import BugsCreationSerializer
from bugs.serializer import BugsUpdateSerializer
from rest_framework.exceptions import NotFound


class BugSearch(APIView):
    @method_decorator(validated_user, name="dispatch")
    def get(self, request):
        print(f"Query Parameters: {request.query_params}")
        assignedproject_id = request.query_params.get('assignedproject_id')
        search_bug = request.query_params.get('search_bug', '')

        if not assignedproject_id:
            return Response({"error": "assignedproject_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        bugs_query = Bug.objects.filter(assignedproject_id=assignedproject_id)
        if search_bug:
            bugs_query = bugs_query.filter(description__icontains=search_bug)  
        if not bugs_query.exists():
            return Response({"error": "No bugs found for the given parameters"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BugsSearchByProjectSerializer(bugs_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BugCreation(APIView):
    @method_decorator(check_user_access, name="dispatch")
    def post(self, request):
        serializer = Bug(data=request.data)
        print(request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            bugs = Bug.objects.create(**validated_data)
            return Response(BugsCreationSerializer(bugs).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BugUpdate(APIView):
    @method_decorator(check_user_access, name="dispatch")
    def patch(self, request, bug_id):
        try:
            bug = Bug.objects.get(id=bug_id)  
        except Bug.DoesNotExist:  
            raise NotFound(detail="Bug not found")

        serializer = BugsUpdateSerializer(bug, data=request.data, partial=True)
        if serializer.is_valid():
            if serializer.validated_data.get('bug_type') == "deleted":
                bug.delete()
                return Response({"message": "Bug deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            else:
                for key, value in serializer.validated_data.items():
                    setattr(bug, key, value)
                bug.save()
                return Response(BugsUpdateSerializer(bug).data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
