from django.urls import  path
from . import  views
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    path("signup/",views.UserView.as_view()),
    path("login/",views.LoginView.as_view()),
    path("token/",ObtainAuthToken.as_view()),

]
