from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.http import request
from django.urls import reverse


class PMUser(AbstractUser):
    about = models.TextField(max_length=3000, blank=True)
    tags = models.TextField(blank=True)
    vk = models.URLField(blank=True)
    tg = models.URLField(blank=True)
    warns = models.TextField(blank=True)
    lawsuit = models.TextField(blank=True)
    banned = models.BooleanField(default=False)

    def had_tg_vk(self):
        return self.vk or self.tg

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_id': self.pk})

    def get_edit_absolute_url(self):
        return reverse('profiledit', kwargs={'profile_id': self.pk})


class Card(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    author = models.ForeignKey('PMUser', on_delete=models.CASCADE, blank=True)
    content = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def get_time(self):
        return self.time_created.strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pcard', kwargs={'pcard_id': self.pk})

    def get_edit_absolute_url(self):
        return reverse('pcardedit', kwargs={'pcard_id': self.pk})

    class Meta:
        verbose_name = 'Card'
