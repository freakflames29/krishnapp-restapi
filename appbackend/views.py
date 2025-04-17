from rest_framework.views import APIView
from rest_framework.response import Response

class HealthCheck(APIView):
    def get(self,rq):
        return  Response({"msg":"All checked "},status=200)