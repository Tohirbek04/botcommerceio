from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shops import views

router = DefaultRouter()
router.register('product', views.ProductmodelViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
]

