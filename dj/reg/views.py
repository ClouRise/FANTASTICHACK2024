from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу логина после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'reg/register.html', {'form': form})
