from django.urls import path
from .views import ProductApiListApiView,ProductApiCreateApiView,ProductApiDeleteApiView,ProductApiDetailApiView,ProductApiUpdateApiView,ProductApiMixedApiView

urlpatterns=[
    path('productlar/', ProductApiListApiView.as_view()),
    path('product/create/', ProductApiDetailApiView.as_view() ),
    path('product/mixedupdate/<int:pk>', ProductApiDeleteApiView.as_view()),
    path('product/detail/<int:pk>', ProductApiUpdateApiView.as_view()),
    path('product/delete/<int:pk>', ProductApiCreateApiView.as_view()),
    path('product/update/<int:pk>', ProductApiMixedApiView.as_view())
]