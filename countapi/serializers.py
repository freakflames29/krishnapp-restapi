from rest_framework.serializers import  ModelSerializer
from .models import  Count

class CountSerializer(ModelSerializer):
    class Meta:
        model = Count
        fields =["id","count","date","time"]

