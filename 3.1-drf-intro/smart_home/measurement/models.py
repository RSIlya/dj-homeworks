from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, unique=True, verbose_name='Описание')


class Measurement(models.Model):

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='values')
    temperature = models.FloatField(verbose_name='Измеренное значение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время измерения')
