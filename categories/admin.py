from django.contrib import admin

from categories.models import CategoryModel, ProductModel, ProductsImages


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductModel)
class CategoryAdmin(admin.ModelAdmin):
    pass
