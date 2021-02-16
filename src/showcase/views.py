from django.shortcuts import render
from .models import Category,Product,ProductImage
# Create your views here.

def index(request):
    product = Product.objects.all().order_by("-id")
    
    return render(request, 'index.html',{
        'product':product,
        })

def details(request,product_id):
    product = Product.objects.get(id = product_id)
    image = ProductImage.objects.filter(product=product)

    return render(request, 'index.html',{
        'product':product,
        'image': image
        })  
    