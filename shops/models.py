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
    price = models.FloatField(db_default=0.0)
    count = models.IntegerField(db_default=0)


class ProductImageModel(BaseModel):
    image = models.ImageField(upload_to='products')
