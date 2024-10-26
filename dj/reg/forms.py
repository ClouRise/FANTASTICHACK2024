from django import forms
from .models import User
import re

class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(
        max_length=20,
        label='Повторите пароль',
        widget=forms.PasswordInput(),
        required=True,
    )
    
    class Meta:
        model = User
        fields = ['username', 'password', 'full_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
    
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not re.match(r'^[а-яА-ЯёЁ\s\-]+$', full_name):
            raise forms.ValidationError("ФИО должно содержать только кириллицу, пробелы и дефисы.")
        if len(full_name) > 50:
            raise forms.ValidationError("ФИО не должно превышать 50 символов.")
        return full_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Этот логин уже используется.")
        if len(username) > 20:
            raise forms.ValidationError("Логин не должен превышать 20 символов.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Пароль является обязательным полем.")
        if len(password) > 20:
            raise forms.ValidationError("Пароль не должен превышать 20 символов.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают.")

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
