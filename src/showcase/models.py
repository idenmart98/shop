from django.db import models
from authe.models import Customer


class Category(models.Model):
    title = models.CharField(max_length=200,verbose_name='Имя')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    price_sell = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    @property
    def items_count(self):

        return self.items.filter(status='in_stock').count()

        
        

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='items')
    status = models.CharField(max_length=200, verbose_name='Статус')
        
    class Meta:
        verbose_name = 'Единица'
        verbose_name_plural = 'Единицы'

        # def __str__(self):
        #     return self.product__name

class Storage(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='StorageProduct')
 
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
 
    def __str__(self):
        return self.product__name
 

 
class StorageProduct(models.Model):
    storage = models.ForeignKey(Storage,on_delete=models.CASCADE,verbose_name='Магазин')
    good = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Товар')
    amount = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Продукт магазина'
        verbose_name_plural = 'Продукты магазинов'

class ProductImage(models.Model):
    product_img = models.ForeignKey(Product, default=None, on_delete=models.CASCADE,related_name='images')
    images = models.FileField(upload_to = 'images/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return self.product_img.name

