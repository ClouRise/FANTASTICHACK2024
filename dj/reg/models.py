from django.db import models
from django.urls import reverse


class Category:
    name = models.CharField(max_length=20,
                            unique=True)
    slug = models.SlugField(max_length=20,
                            unique=True)  # для создания url, генераци ссылки

    class Meta:
        ordering = ['name']  # отображени
        indexes = [models.Index(fields=['name'])]  # поиск по полю name
        verbose_name = 'category'  # единственное число
        verbose_name_plural = 'categories'  # множественное число

    def __str__(self):  # получение имени
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE())
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='ПУТЬ К ПАПКЕ/%Y/%m/%d',
                              blank=True)  # поля необязательны к заполнению
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)  # числа с плавающей точкой
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(default=0.00, max_digits=4,
                                   decimal_places=2)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # абсолютны url
        return reverse("main:product_detail",  # отображение на отдельной странице
                       args=[self.slug])  # передаем слаг для генерации ссылки

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
