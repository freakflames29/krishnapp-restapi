from django.urls import path
from . import views

urlpatterns = [
    path("",views.AllPostView.as_view()),
    path("create/",views.CreatePostView.as_view()),
]
