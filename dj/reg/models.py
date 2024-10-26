from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username
