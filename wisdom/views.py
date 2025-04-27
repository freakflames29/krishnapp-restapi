from django.shortcuts import render
from rest_framework import generics
from  .serializers import WisdomSerializer
from .models import Wisdom

class  WisdomListView(generics.ListCreateAPIView):
    queryset = Wisdom.objects.all()
    serializer_class = WisdomSerializer