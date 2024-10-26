from django.urls import path
from .views import register, login_view  # Импортируем нужные функции

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),  # Путь для авторизации
]
