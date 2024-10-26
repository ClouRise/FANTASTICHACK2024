from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm, LoginForm
from .models import User

# Вьюха регистрации
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'reg/register.html', {'form': form})

# Вьюха авторизации
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                return redirect('http://127.0.0.1:8000')  # Переадресация на приложение 'main'
            else:
                form.add_error(None, 'Неверный логин или пароль.')
    else:
        form = LoginForm()
    return render(request, 'reg/login.html', {'form': form})
