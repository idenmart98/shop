from django.shortcuts import render

from .forms import RegisterForm, LoginForm
from .models import MainUserManager, Customer, ConfirmCode
from .utils import send_register_mail

# Create your views here.

def base(request):
    return render(request, 'base.html')

def register(request):
    form = RegisterForm

    if request.method == 'POST':
        save_form = RegisterForm(request.POST)

        if Customer.objects.filter(email = request.POST['email'], verified=False):
            customer = Customer.objects.get(email=request.POST['email'])
            customer.codes.all().delete()
            code = ConfirmCode.objects.create(customer = customer)
            send_register_mail(f'Чтобы подтвердить почту, перейдите по ссылке http://127.0.0.1:8000/authe/register/confirm/{code.code}/', code.customer.email)
            return render(request, 'register.html', {'form': form, 'message': 'Проверьте вашу почту'})

        if save_form.is_valid():
            customer = Customer.objects.create(
                email = request.POST['email'],
                username = request.POST['username'],
                password = request.POST['password'],
                phone = request.POST['phone'])
            code = ConfirmCode.objects.create(customer = customer)
            send_register_mail(f'Чтобы подтвердить почту, перейдите по ссылке http://127.0.0.1:8000/authe/register/confirm/{code.code}/', code.customer.email)
            return render(request, 'reply.html', {'message': 'Проверьте вашу почту'})

        return render(request, 'register.html', {'form': form, 'error': 'Неправильный никнейм или пароль'})

    return render(request, 'register.html', {'form': form})


def login(request):
    if request:
        if request.method == 'POST':
            print(Customer.objects.filter(username = request.POST['username'], password = request.POST['password']))
            return render(request, 'reply.html', {'message': 'Вы вошли в аккаунт', 'success': True})
    return render(request, 'login.html', {'form': LoginForm()})

def confirm(request, code):
    if ConfirmCode.objects.filter(code=code):
        code = ConfirmCode.objects.get(code=code)
        if not code.confirm:
            code.confrim = True
            code.save()
            code.customer.verified = True
            code.customer.save()
            return render(request, 'reply.html', {'message': 'Ваша почта подтверждена', 'success': True})
        return render(request, 'reply.html', {'message': 'Ваша почта уже подтверждена', 'success': True})
    return render(request, 'reply.html', {'message': 'Ваш код устарел, либо неправильный', 'success': True})