from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .serializers import PostSerializer
from .models import Post

class AllPostView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CreatePostView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def post(self,rq):
        return self.create(rq)
    



class SinglePostView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# user's post view 
class UserPostView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = PostSerializer
    # queryset = request.user.posts.all()
    
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
    

            
