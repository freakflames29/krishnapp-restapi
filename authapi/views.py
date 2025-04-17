from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db import IntegrityError, Error


from .serializers import UserSerializer


class UserView(APIView):
    def post(self, rq):
        try:
            username = rq.data['username']
            email = rq.data['email']
            password = rq.data['password']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            token = Token.objects.create(user=user)

            resData = {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "token": token.key

            }
            return Response(resData, status=201)


        except IntegrityError as e:
            return Response({"error": "Username already exists"}, status=401)


        except Exception as e:
            print("Error is ", e)
            return Response({"error": "Username, password , email required"}, status=400)


class LoginView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, rq):
        user = rq.user
        userser = UserSerializer(user)

        return Response(userser.data, status=200)

