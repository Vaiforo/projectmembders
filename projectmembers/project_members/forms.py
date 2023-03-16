from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Cat not allowed'

    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Заголовок слишком длинный')
        return title
