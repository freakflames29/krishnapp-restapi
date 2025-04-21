from django.urls import path
from . import views

urlpatterns = [
    path("all/",views.AllPostView.as_view()),
    path("<int:pk>/",views.SinglePostView.as_view()),
    path("create/",views.CreatePostView.as_view()),
    path("",views.UserPostView.as_view()),
]

# posts/ ==> users post
# posts/all ==> lists all post
# posts/<id> ==> lists specific posts
# posts/create/ ==> create post
