from django.db import models
# Create your models here.

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

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, verbose_name='Статус')
        
    class Meta:
        verbose_name = 'Единица'
        verbose_name_plural = 'Единицы'

    def __str__(self):
        return self.product__name


class ProductImage(models.Model):
    product_img = models.ForeignKey(Product, default=None, on_delete=models.CASCADE,related_name='images')
    images = models.FileField(upload_to = 'images/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return self.product_img.name
