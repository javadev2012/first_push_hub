from django.urls import path
from .views import (
    ProductApiListApiView,
    ProductApiCreateApiView,
    ProductApiDeleteApiView,
    ProductApiDetailApiView,
    ProductApiUpdateApiView,
    ProductApiMixedApiView
)

urlpatterns = [
    # Barcha productlar ro'yxati (GET)
    path('productlar/', ProductApiListApiView.as_view(), name='product-list'),

    # Yangi product qo'shish (POST)
    path('product/create/', ProductApiCreateApiView.as_view(), name='product-create'),

    # Bitta product detail (GET)
    path('product/detail/<int:pk>/', ProductApiDetailApiView.as_view(), name='product-detail'),

    # Product o'chirish (DELETE)
    path('product/delete/<int:pk>/', ProductApiDeleteApiView.as_view(), name='product-delete'),

    # Product yangilash (PUT/PATCH)
    path('product/update/<int:pk>/', ProductApiUpdateApiView.as_view(), name='product-update'),

    # Aralash update/delete/view (optional)
    # path('product/mixed /<int:pk>/', ProductApiMixedApiView.as_view(), name='product-mixed'),
    path('product/mixed/<int:pk>/', ProductApiMixedApiView.as_view(), name='product-mixed'),

]