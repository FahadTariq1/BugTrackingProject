from django.urls import path
from bugs.views import BugSearch,BugCreation,BugUpdate,BugDelete
urlpatterns=[
   path('search/',BugSearch.as_view(),name = "search-bugs"),
   path('create/',BugCreation.as_view(),name = "create-bug"),
   path('update/<int:bug_id>/', BugUpdate.as_view(), name='bug-update'),
   path('delete/<int:bug_id>/', BugDelete.as_view(), name='bug-delete')
]


