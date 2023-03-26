from django.shortcuts import render
from .serializer import *
from rest_framework.decorators import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken , AccessToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
# Create your views here.

def get_access_token(user):
    token = RefreshToken.for_user(user=user)
    access_token = str(token.access_token)
    
    return ({
        'refresh_token': token,
        'access_token' : access_token
    })


import datetime
class Login(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email = email,password = password)
        print(user)
        if user:
            token = get_access_token(user)
            access_token =token['access_token']
            refresh_token = token['refresh_token']
            data  = {"user":str(user),
                     "refresh_token":str(refresh_token),
                     'access_token':str(access_token),
                     'status':200}
            user_time = CustomUser.objects.get(email = email)
            user_time.last_login = datetime.datetime.now()
            user_time.save()
            return Response(data,status=200)
        return Response('not_valid_Data',status = status.HTTP_406_NOT_ACCEPTABLE)


class User_registrations_view(APIView):
    def post(self,request):
        try:
            data = request.data
            user = CustomUser.objects.filter(email = data['email'])
            if user:
                return Response('This email is already registered',status = status.HTTP_406_NOT_ACCEPTABLE)
            serializer = User_profile_serializer(data = data)
            if serializer.is_valid():
                serializer.save()
                user = CustomUser.objects.create(email = data['email'],password = make_password(data['password']))
                userData = get_access_token(user)
                access_token = userData['access_token']
                refresh_token = userData['refresh_token']
                userData = {'data':serializer.data,
                            'access_token':str(access_token),
                            'refresh_token':str(refresh_token),
                            'status':200}
                return Response(userData,status=status.HTTP_200_OK)
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            response_Data = str(e)
            return Response(response_Data,status=status.HTTP_400_BAD_REQUEST)
        
def register(request):
    return render(request , 'register.html')


class User_register(APIView):
    def post(self,request):
        try:
            data = request.data
            user_email = CustomUser.objects.get(email = data['email'])
            if user_email:
                serializer = User_profile_serializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    user = CustomUser.objects.create(email = data['email'],password = make_password(data['password']))
                    token = get_access_token(user)
                    access_token = token['access_token']
                    refresh_token = token['refresh_token']
                    userDataToken = {'user':str(user),
                                     'refresh_token':str(refresh_token),
                                     'access_token':str(access_token),
                                     'status':200}
                    return Response(userDataToken,status=status.HTTP_200_OK)
                print(serializer.errors)
                return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            response_data = str(e)
            print(e)
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)