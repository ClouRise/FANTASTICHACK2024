from django.urls import path
from .views import kanban_board, create_card, edit_card, delete_card, export_cards_to_excel

urlpatterns = [
    path('', kanban_board, name='kanban_board'),
    path('create/', create_card, name='create_card'),
    path('edit/<int:pk>/', edit_card, name='edit_card'),
    path('delete/<int:pk>/', delete_card, name='delete_card'),
    path('export/', export_cards_to_excel, name='export_cards_to_excel'),
]
