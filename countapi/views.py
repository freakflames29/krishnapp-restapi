from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist
from .serializers import CountSerializer
from .models import Count
from rest_framework.generics import get_object_or_404
from rest_framework import filters


class CountView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields =["date"]

    def get(self, rq):
        try:
            user = rq.user
            print(user)
            count = Count.objects.filter(user=user)
            
            
            for backend in list(self.filter_backends):
                count = backend().filter_queryset(rq, count, self)
                
            count_ser = CountSerializer(count, many=True)
            return Response(count_ser.data, status=200)

        except Count.DoesNotExist as e:
            return Response({"msg": "You have not chanting data"}, status=400)

        except Exception as e:
            print(e)
            return Response({"msg": "unknown error"}, status=400)

    def post(self, rq):
        try:
            userCount = rq.user.count.get(date=rq.data['date'])
            # count = Count.objects.get(date=rq.data['date'])
            countser = CountSerializer(userCount, data=rq.data, partial=True)
        except Count.DoesNotExist as e:
            countser = CountSerializer(data=rq.data)

        if countser.is_valid():
            countser.save(user=rq.user)
            return Response(countser.data, status=200)
        else:
            return Response({"msg": "Something went wrong"}, status=400)
