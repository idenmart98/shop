from django.urls import path,include

from .views import register, login, confirm

app_name = 'authe'

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('register/confirm/<str:code>/', confirm, name='confirm'),
]
