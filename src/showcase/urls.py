
from django.contrib import admin
from django.urls import path,include

from .views import index, details

app_name = 'showcase'

urlpatterns = [
    path('', index),
    path('details', details),
]