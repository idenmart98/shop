from django.db import models
from authe.models import Customer, ConfirmCode
# Create your models here.

ON_WAY = 'on_way'
DONE = 'done'
CANCELED = 'canceled'

BUSKET_STATUS = (
        (ON_WAY, u"в пути"),
        (DONE, u"оформлено"),
        (CANCELED, u"отменено"),
    )


SOLD = 'sold'
IN_STOCK = 'in_stock'

ITEM_STATUS = (
        (SOLD, u"продано"),
        (IN_STOCK, u"в наличии"),
    )


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя')
    
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

class Busket(models.Model):
    status = models.CharField(max_length=200, choices=BUSKET_STATUS, verbose_name='Статус')
    user = models.ForeignKey(Customer, default=None, on_delete=models.CASCADE, related_name='buskets')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class Item(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name='items')
    status = models.CharField(max_length=200, choices=ITEM_STATUS, verbose_name='Статус')
    busket = models.ForeignKey(Busket, default=None, on_delete=models.CASCADE, related_name='items')

    class Meta:
        verbose_name = 'Единица'
        verbose_name_plural = 'Единицы'

    def __str__(self):
        return self.product.name


class ProductImage(models.Model):
    product_img = models.ForeignKey(Product, default=None, on_delete=models.CASCADE,related_name='images')
    images = models.FileField(upload_to = 'images/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return self.product_img.name
    