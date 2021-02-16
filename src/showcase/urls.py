
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings
from .views import index, details

app_name = 'showcase'

urlpatterns = [
    path('', index),
    path('details/<str:product_id>/', details,name='details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)