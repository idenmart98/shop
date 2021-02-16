from django.contrib import admin
from django.urls import path,include

from .views import index, details

urlpatterns = [
    path('', index),
    path('details', details),
]
