from django.db import models
from django.urls import reverse


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название города')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    # После создания записи перейти на её url(CreateView)
    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})