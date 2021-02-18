from django import forms
from .models import Customer

class RegisterForm(forms.ModelForm):
    password = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = Customer
        fields = ('email', 'username', 'password', 'phone')

    username.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Ваш ник',
    })
    email.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Ваша почта'
    })
    password.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Ваш пароль'
    })
    phone.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Ваш номер телефона'
    })

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = ('username', 'password')
    username.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Ваш ник',
    })
    password.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Ваш пароль',
    })