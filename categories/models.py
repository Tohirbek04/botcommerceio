from django.db.models import Model, CASCADE, ImageField, CharField, FloatField, ForeignKey, IntegerField, TextField

from root.settings import UNITS_CHOICES, STOCK_STATUS_CHOICES


class CategoryModel(Model):
    name = CharField(max_length=255)
    emoji = CharField(max_length=255)
    image = ImageField(null=True, blank=True, upload_to='categories/image/%Y/%m/%d/')
    description = TextField(null=True, blank=True)
    sort_order = IntegerField(default=0)


class ProductModel(Model):
    name = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    price = FloatField(default=0)
    units = CharField(max_length=15, choices=UNITS_CHOICES, default='Select unit')
    stock = CharField(max_length=50, choices=STOCK_STATUS_CHOICES, default='Select stock status')
    selling_price = FloatField(default=0)
    category = ForeignKey('categories.CategoryModel', on_delete=CASCADE, related_name='products')
    image = ForeignKey('categories.ProductsImages', on_delete=CASCADE, related_name='products')
    emoji = CharField(max_length=255)
    sort_order = IntegerField(default=0)


class ProductsImages(Model):
    image = ImageField(upload_to='products/image/%Y/%m/%d/')
    product = ForeignKey('categories.ProductModel', CASCADE)
