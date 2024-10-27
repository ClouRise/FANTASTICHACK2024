from django.db.models import Q  # Импортируйте Q для создания запросов
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Card
from .forms import CardForm

def kanban_board(request):
    # Получаем карточки по статусу
    backlog = Card.objects.filter(status='backlog')
    in_progress = Card.objects.filter(status='in_progress')
    done = Card.objects.filter(status='done')

    # Обработка поиска
    search_query = request.GET.get('search', '')
    if search_query:
        cards = Card.objects.filter(
            Q(title__icontains=search_query) | 
            Q(assignee__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    else:
        cards = Card.objects.all()

    # Если это POST-запрос, то обрабатываем сохранение изменений карточки
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        card = get_object_or_404(Card, pk=card_id)
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('kanban_board')

    return render(request, 'main/kanban_board.html', {
        'backlog': backlog,
        'in_progress': in_progress,
        'done': done,
        'cards': cards,
        'search_query': search_query,
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

def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('kanban_board')
    else:
        form = CardForm(instance=card)
    return render(request, 'main/kanban_board.html', {'form': form})

def delete_card(request, pk):

    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('kanban_board')

def export_cards_to_excel(request):

    cards = Card.objects.all().values('title', 'assignee', 'description', 'status')

    df = pd.DataFrame(cards)

    df.columns = ['Название', 'Исполнитель', 'Описание', 'Статус']

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    response['Content-Disposition'] = 'attachment; filename="карточки.xlsx"'

    df.to_excel(response, index=False)

    return response
