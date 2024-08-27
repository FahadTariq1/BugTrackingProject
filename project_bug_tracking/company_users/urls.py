from django.urls import path
from company_users.views import Signup
from company_users.views import Login
from company_users.views import AllDeveloper

urlpatterns = [
    path("sign-up/", Signup.as_view(), name='sign-up'),
    path("login/", Login.as_view(), name='login'),
    path("all-developers/", AllDeveloper.as_view(), name='all-developers')
]
