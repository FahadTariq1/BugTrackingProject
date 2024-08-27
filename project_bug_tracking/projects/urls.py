from projects.views import ProjectDetails
from projects.views import ProjectCreation
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns=[
    path('all-projects/',ProjectDetails.as_view(),name = "all-projects"),
    path('create-project/',ProjectCreation.as_view(),name = "create-project"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)