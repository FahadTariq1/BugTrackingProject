from projects.views import ProjectDetails,ProjectCreation
from django.urls import path

urlpatterns=[
    path('all/', ProjectDetails.as_view(),name = "all"),
    path('create/', ProjectCreation.as_view(),name = "create"),
]