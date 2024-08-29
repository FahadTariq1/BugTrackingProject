from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import Project
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from projects.serializer import ProjectDetailsSerializer,ProjectCreationSerializer
from django.utils.decorators import method_decorator 
from projects.decorators import check_manager_access,validated_user


class ProjectDetails(APIView):
    @method_decorator(validated_user,name="dispatch")
    def get(self, request):

        description_search = request.GET.get('description_search', '').strip()
        page_size = int(request.GET.get('page_size', 10))
        page_number = int(request.GET.get('page', 1))
        queryset = Project.objects.all()
        if description_search:
            queryset = queryset.filter(description__icontains=description_search)
        paginator = PageNumberPagination()
        paginator.page = int(page_number)  
        paginator.page_size = page_size
        result_page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = ProjectDetailsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProjectCreation(APIView):
    @method_decorator(check_manager_access, name="dispatch")
    def post(self, request):
        serializer = ProjectCreationSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            project = Project.objects.create(**validated_data)
            return Response(ProjectCreationSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)