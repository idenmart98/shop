from django.contrib import admin
from .models import Category,Item,Product,ProductImage,Storage,StorageProduct
from .forms import ProductForm
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    model = Storage

@admin.register(StorageProduct)
class StorageProductAdmin(admin.ModelAdmin):
    model = StorageProduct



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ("name", "price","price_sell","category","description")
    inlines = [ProductImageAdmin]

    form = ProductForm
    
    fieldsets = (
        (None, {
            'fields': ("name", "price","price_sell","category","description", 'items_count',),
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
