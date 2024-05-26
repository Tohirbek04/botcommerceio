from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from categories.models import CategoryModel, ProductModel
from categories.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class CategoryCreateAPIView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class ProductCreateAPIView(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
