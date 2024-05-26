from rest_framework.serializers import ModelSerializer

from categories.models import CategoryModel, ProductsImages, ProductModel


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = 'id', 'name', 'image', 'emoji', 'description', 'sort_order'


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductsImages
        fields = 'id', 'image'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(source='product_image_set', many=True, read_only=True)

    class Meta:
        model = ProductModel
        fields = 'id', 'name', 'price', 'selling_price', 'units', 'stock', 'emoji', 'sort_order', 'description', 'category', 'images'
