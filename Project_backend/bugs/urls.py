from django.urls import path
from bugs.views import BugSearch
from bugs.views import BugCreation
from bugs.views import BugUpdate
urlpatterns=[
   path('search-bugs/',BugSearch.as_view(),name = "search-bugs"),
   path('create-bug/',BugCreation.as_view(),name = "create-bug"),
   path('update-bug/<int:bug_id>/', BugUpdate.as_view(), name='bug-update')
]


