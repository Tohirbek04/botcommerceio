from django.urls import path, include

from categories.views import ProductCreateAPIView, ProductViewSet, CategoryCreateAPIView, CategoryViewSet

urlpatterns = [
    path('view/category/', CategoryViewSet.as_view()),
    path('category/', CategoryCreateAPIView.as_view()),
    path('view/product/', ProductViewSet.as_view()),
    path('product/', ProductCreateAPIView.as_view()),
]
