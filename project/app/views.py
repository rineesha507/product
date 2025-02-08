from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import Product, Category 
from .serializers import ProductSerializer, CategorySerializer,LoginSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)  # Allow file uploads
    permission_classes = [IsAuthenticated]



class LoginAPI(APIView):
    def post(self,request):
        data =request.data
        serializer =LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
            "status" :False,
            "data" :{}
        })
        username =serializer.data['username']
        password =serializer.data['password']

        user_obj = authenticate(username = username, password= password)

        if user_obj:
            token , _ = Token.objects.get_or_create(user=user_obj)
            return Response({
            "status" :True,
            "data" :{'token' :str(token) }
        })


        return Response({
            "status" :True,
            "data" :{},
            "message" : "Invalid credentials"
        })

