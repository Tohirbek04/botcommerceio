from django.shortcuts import render
from rest_framework import viewsets

from categories.serializers import ProductSerializer
from shops.models import ProductModel


# Create your views here.


class ProductmodelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
