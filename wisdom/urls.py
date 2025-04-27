from django.urls import path
from . import views
urlpatterns = [
    path("",views.WisdomListView.as_view())
]
