import uuid

from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class ShopModel(BaseModel):
    user = models.ForeignKey('users.User', models.CASCADE)


class CategoryModel(BaseModel):
    shop = models.ForeignKey('shops.ShopModel', models.CASCADE)


class ProductModel(BaseModel):
    uuid = models.UUIDField(db_default=uuid.uuid4, editable=False, unique=True)
    price = models.FloatField(db_default=0.0)
    count = models.IntegerField(db_default=0)
    image = models.ImageField(upload_to='products/%Y/%m/%d')


class ProductImageModel(BaseModel):
    uuid = models.UUIDField(db_default=uuid.uuid4, editable=False, unique=True)
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey('shops.ProductModel', on_delete=models.CASCADE)


class RDBaseModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Region(RDBaseModel):
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class District(RDBaseModel):
    region = models.ForeignKey('shops.Region', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Districts'
