from django.shortcuts import render

from .serializers import TestSerializer
from .models import TestModel
from rest_framework import generics

class TestView(generics.ListCreateAPIView):
    serializer_class = TestSerializer
    queryset = TestModel.objects.all()
    
