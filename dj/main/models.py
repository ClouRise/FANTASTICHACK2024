from django.db import models

class Card(models.Model):
    STATUS_CHOICES = [
        ('backlog', 'Бэклог'),
        ('in_progress', 'В процессе'),
        ('done', 'Выполнено'),
    ]

    title = models.CharField(max_length=255)
    assignee = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='backlog')

    def __str__(self):
        return self.title
