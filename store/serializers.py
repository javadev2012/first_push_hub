from .models import ProductApi
from rest_framework import serializers

class ProductApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductApi
        fields='__all__'
