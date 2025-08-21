from tokenize import PlainToken
from wsgiref.util import request_uri
from xmlrpc.client import Boolean

from django.shortcuts import render
from rest_framework import generics,status
from .models import ProductApi
from .serializers import ProductApiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# class ProductApiListApiView(generics.ListAPIView):
#     queryset = ProductApi.objects.all()
#     serializer_class = ProductApiSerializer
class ProductApiListApiView(APIView):
    def get(self,request):
        productApi=ProductApi.objects.all()
        serializer_data=ProductApiSerializer(productApi,many=True).data
        info={
            'status':'My users ',
            'productApi list':serializer_data
        }
        return Response(info,status=status.HTTP_200_OK)
# class ProductApiDetailApiView(generics.RetrieveAPIView):
#     queryset = ProductApi.objects.all()
#     serializer_class = ProductApiSerializer
#     lookup_field = 'id'
class ProductApiDetailApiView(APIView):
    def get(self,request,pk):
        productApi=ProductApi.objects.get(id=pk)
        serializer_data=ProductApiSerializer(productApi).data
        info={
            'status':'Product taken successfully',
            'productApi': serializer_data
        }
        return Response(info)
class ProductApiDeleteApiView(generics.DestroyAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer

class ProductApiUpdateApiView(generics.UpdateAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer

# class ProductApiCreateApiView(generics.CreateAPIView):
#     queryset = ProductApi.objects.all()
#     serializer_class = ProductApiSerializer
class ProductApiCreateApiView(APIView):
    def post(self,request):
        datam=request.date
        serializer=ProductApiSerializer(data=datam)
        if serializer.is_valid():
            serializer.save()
            info={
                'status':'may users',
                'Users':datam
            }
            return Response(info)

class ProductApiMixedApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer
