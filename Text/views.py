from django.shortcuts import render
from .serializers import UserRegisterSerializer,TextSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from . import models
# Create your views here.

class register(APIView):
    
    def post(self,request,format=None):
        serializer=UserRegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token=Token.objects.get_or_create(user=account)
            data['token']=token.key
            return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
        else:
            data=serializer.errors
            return Response({"status": "error", "data": data}, status=status.HTTP_400_BAD_REQUEST)
             
class textsubmit(APIView):
    def post(self, request):
        serializer1 = TextSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response({"status": "success", "data": serializer1.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer1.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class TextView(APIView):
    def get_detals():
        queryset = models.Text.objects.all()
        if queryset.is_valid():
            queryset.save()
            return Response({"status": "success", "data": queryset.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": queryset.errors}, status=status.HTTP_400_BAD_REQUEST)