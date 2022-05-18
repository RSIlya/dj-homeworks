from django.db import models


class Phone(models.Model):

    name = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.URLField(max_length=255, verbose_name='Изображение')
    price = models.PositiveIntegerField(verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(verbose_name='Поддержка lte')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
