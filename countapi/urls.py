from django.urls import path
from . import views
urlpatterns = [
    path("",views.CountView.as_view())
]