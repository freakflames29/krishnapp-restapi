from rest_framework.serializers import ModelSerializer
from .models import Wisdom

class WisdomSerializer(ModelSerializer):
    class Meta:
        model = Wisdom
        fields = "__all__"
    