from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу логина после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'reg/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Замените 'home' на нужный URL после авторизации
    else:
        form = LoginForm()
    return render(request, 'reg/login.html', {'form': form})
