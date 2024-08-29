from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from projects.decorators import validated_user, check_user_access
from django.utils.decorators import method_decorator 
from bugs.models import Bug
from bugs.serializer import BugsSearchByProjectSerializer, BugsCreationSerializer, BugsUpdateSerializer
from rest_framework.exceptions import NotFound


class BugSearch(APIView):
    @method_decorator(validated_user, name="dispatch")
    def get(self, request):
        project_id = request.query_params.get('project_id')
        print('This is the project_id')
        print(project_id)
        search_bug = request.query_params.get('search_bug', '')

        if not project_id:
            return Response({"error": "project_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        bugs = Bug.objects.filter(assignedproject=project_id)
        serializer = BugsSearchByProjectSerializer(bugs, many=True)
        
        if search_bug:
            bugs = bugs.filter(description__icontains=search_bug)  
        if not bugs.exists():
            return Response({"error": "No bugs found for the given parameters"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BugCreation(APIView):
    @method_decorator(check_user_access, name="dispatch")
    def post(self, request):
        serializer = BugsCreationSerializer(data=request.data)
        if serializer.is_valid():
            bug = Bug.objects.create(**serializer.validated_data)
            return Response(BugsCreationSerializer(bug).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BugUpdate(APIView):
    @method_decorator(check_user_access, name="dispatch")
    def patch(self, request, bug_id):
        try:
            bug = Bug.objects.get(id=bug_id)  
        except Bug.DoesNotExist:  
            raise NotFound(detail="Bug not found")
        
        serializer = BugsUpdateSerializer( bug, data=request.data, partial=True)
        if serializer.is_valid():
            bug.status = serializer.validated_data.get('status')
            bug.save()
            return Response(BugsUpdateSerializer(bug).data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BugDelete(APIView):
    @method_decorator(check_user_access, name="dispatch")
    def delete(self, request, bug_id):
        try:
            bug = Bug.objects.get(id=bug_id)  
        except Bug.DoesNotExist:  
            raise NotFound(detail="Bug not found")
        bug.delete()
        return Response({"message": "Bug deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        