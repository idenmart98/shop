from django.contrib import admin
from .models import Category,Item,Product,ProductImage
# Register your models here.

admin.site.register(Category)

admin.site.register(Item)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Новости"""
    list_display = ("name", "price","price_sell","category","description")
    inlines = [ProductImageAdmin]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass



