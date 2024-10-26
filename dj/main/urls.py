from django.urls import path
from . import views

urlpatterns = [
    path('', views.kanban_board, name='kanban_board'),
    path('create/', views.create_card, name='create_card'),
    path('edit/<int:pk>/', views.edit_card, name='edit_card'),   # URL для редактирования карточки
    path('delete/<int:pk>/', views.delete_card, name='delete_card'),  # URL для удаления карточки
]
