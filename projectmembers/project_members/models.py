from django.db import models
from django.urls import reverse


class Card(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    content = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    # cats = models.ForeignKey('Category', on_delete=models.DO_NOTHING, default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})

    class Meta:
        verbose_name = 'Card'
