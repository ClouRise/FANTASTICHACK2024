from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(forms.ModelForm):
    full_name = forms.CharField(
        label='ФИО',
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ФИО'}),
    )
    
    username = forms.CharField(
        label='Логин',
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}),
    )
    
    password = forms.CharField(
        label='Пароль',
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
    )
    
    password2 = forms.CharField(
        label='Повторить пароль',
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
    )

    class Meta:
        model = User
        fields = ('username',)

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not re.match(r'^[А-Яа-яЁё\s\-]+$', full_name):
            raise ValidationError('ФИО должно содержать только кириллицу, пробелы или дефисы.')
        return full_name

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError('Пароли не совпадают.')
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Логин уже существует.')
        return username
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}),
        max_length=20,
    )
    
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
        max_length=20,
    )
