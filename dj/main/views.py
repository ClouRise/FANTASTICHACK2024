from django.shortcuts import render, get_object_or_404, redirect
from .models import Card
from .forms import CardForm

def kanban_board(request):
    backlog = Card.objects.filter(status='backlog')
    in_progress = Card.objects.filter(status='in_progress')
    done = Card.objects.filter(status='done')

    return render(request, 'main/kanban_board.html', {
        'backlog': backlog,
        'in_progress': in_progress,
        'done': done,
    })

def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kanban_board')
    else:
        form = CardForm()
    return render(request, 'main/card_form.html', {'form': form})

# Редактирование карточки

def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)  # Получаем карточку по ID
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('kanban_board')
    else:
        form = CardForm(instance=card)
    return render(request, 'main/card_form.html', {'form': form})

# Удаление карточки
def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)  # Получаем карточку по ID
    if request.method == 'POST':
        card.delete()
        return redirect('kanban_board')
    return render(request, 'main/card_confirm_delete.html', {'card': card})