from tokenize import PlainToken

from django.shortcuts import render
from rest_framework import generics
from .models import ProductApi
from .serializers import ProductApiSerializer

# Create your views here.

class ProductApiListApiView(generics.ListAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer

class ProductApiDetailApiView(generics.RetrieveAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer
    lookup_field = 'id'

class ProductApiDeleteApiView(generics.DestroyAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer

class ProductApiUpdateApiView(generics.UpdateAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer

class ProductApiCreateApiView(generics.CreateAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer

class ProductApiMixedApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer
