from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['cat'].empty_label = 'Cat not allowed'

    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'id': 'titleInput', 'class': 'form-control', 'type': 'text'}),
            'content': forms.Textarea(
                attrs={'id': 'contetntTextarea', 'class': 'form-control'}),
            'is_published': forms.CheckboxInput(
                attrs={'id': 'isPublishedCheckbox', 'class': 'form-check-input', 'type': 'checkbox'}),
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 50:
                raise ValidationError('Заголовок слишком длинный')
            return title
