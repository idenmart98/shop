from main.celery import app
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings

@app.task()
def add(x,y):
    print(x+y)
    return x+y

