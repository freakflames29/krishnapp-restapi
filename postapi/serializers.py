from rest_framework.serializers import ModelSerializer
from .models import Post
from authapi.serializers import UserSerializer

class PostSerializer(ModelSerializer):

    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["id","title","desc","image","user"]
