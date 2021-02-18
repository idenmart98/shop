from django.urls import path,include

from .views import register, login, confirm, base

app_name = 'authe'

urlpatterns = [
    path('', base, name='base'),

    path('register', register, name='register'),
    path('register/confirm/<str:code>/', confirm, name='confirm'),
    path('login', login, name='login'),

    
]
