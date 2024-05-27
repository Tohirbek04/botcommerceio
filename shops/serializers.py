from rest_framework import serializers

from categories.serializers import CategorySerializer
from shops.models import ProductModel, ProductImageModel


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = 'image', 'uuid'


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(source='productimage_set', many=True, read_only=True)

    class Meta:
        model = ProductModel
        fields = 'name', 'images','price', 'count', 'category'







