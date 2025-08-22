from itertools import product
from tokenize import PlainToken
from wsgiref.util import request_uri
from xmlrpc.client import Boolean

from django.shortcuts import render
from rest_framework import generics,status
from .models import ProductApi
from .serializers import ProductApiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
            'Mana hammasi==>':serializer_data
        }
        return Response(info)
# class ProductApiDeleteApiView(generics.DestroyAPIView):
#     queryset = ProductApi.objects.all()
#     serializer_class = ProductApiSerializer
# class ProductApiDeleteApiView(APIView):
#     def delete(self,request,pk):
#         try:
#             productApi=ProductApi.objects.get(id=pk)
#             productApi.delete()
#             return Response({'status':"O'chirib tashlandi!"})
#         except:
#             return Response({'status':'Bu id li kitob mavjud emas!'})
class ProductApiDeleteApiView(APIView):
    def delete(self,request,pk):
            productApi=get_object_or_404(ProductApi,pk=pk)
            productApi.delete()
            return Response({'status':"O'chirib tashlandi!"})


# class ProductApiUpdateApiView(generics.UpdateAPIView):
#     queryset = ProductApi.objects.all()
#     serializer_class = ProductApiSerializer
class ProductApiUpdateApiView(APIView):
    def put(self,request,pk):
            productApi=get_object_or_404(ProductApi,pk=pk)
            serializer=ProductApiSerializer(productApi,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            productApi= ProductApi.objects.get(id=pk)
            serializer=ProductApiSerializer(productApi,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'status':"Bad request"},status=status.HTTP_400_BAD_REQUEST)
class ProductApiCreateApiView(generics.CreateAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer
# class ProductApiCreateApiView(APIView):
#     def post(self,request):
#         datam=request.date
#         serializer=ProductApiSerializer(data=datam)
#         if serializer.is_valid():
#             serializer.save()
#             info={
#                 'status':'may users',
#                 'Users':datam
#             }
#             return Response(info)

# class ProductApiMixedApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ProductApi.objects.all()
#     serializer_class = ProductApiSerializer
class ProductApiMixedApiView(APIView):
    def get(self,request,pk):
        productApi=get_object_or_404(ProductApi,pk=pk)
        serializer=ProductApiSerializer(productApi).data
        info={
            'status':'Query worked successfully',
            'result':serializer
        }
        return Response(info)
    def put(self,request,pk):
        productApi=get_object_or_404(ProductApi,pk=pk)
        serializer=ProductApiSerializer(productApi,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status: Your serializer has got a problem'})
    def patch(self,request,pk):
        productApi=get_object_or_404(ProductApi,pk=pk)
        serializer=ProductApiSerializer(productApi,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status: Your serializer has got a problem'})
    def delete(self,request,pk):
            productApi=get_object_or_404(ProductApi,pk=pk)
            productApi.delete()
            return Response({'status':"O'chirib tashlandi!"})