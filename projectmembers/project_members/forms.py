from cProfile import label

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddCardForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.author = self.user
        return super().save(*args, **kwargs)

    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'id': 'titleInput', 'class': 'form-control', 'type': 'text'}),
            'content': forms.Textarea(
                attrs={'id': 'contentTextarea', 'class': 'form-control'}),
            'is_published': forms.CheckboxInput(
                attrs={'id': 'isPublishedCheckbox', 'class': 'form-check-input', 'type': 'checkbox'}),
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 50:
                raise ValidationError('Заголовок слишком длинный')
            return title


class EditCardForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок карточки', widget=forms.TextInput(
        attrs={'id': 'nameInput', 'class': 'form-control', 'type': 'text'}))
    content = forms.CharField(label='Описание', widget=forms.Textarea(
        attrs={'id': 'aboutInput', 'class': 'form-control', 'type': 'text'}))

    class Meta:
        model = Card
        fields = ('title', 'content')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Никнейм', widget=forms.TextInput(
        attrs={'id': 'nameInput', 'class': 'form-control', 'type': 'text'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(
        attrs={'id': 'emailInput', 'class': 'form-control', 'type': 'text'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'id': 'passwordInput1', 'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={'id': 'passwordInput2', 'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = PMUser
        # model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'id': 'emailInput', 'class': 'form-control', 'type': 'text'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'id': 'passwordInput', 'class': 'form-control', 'type': 'password'}))


class EditUserForm(UserChangeForm):
    username = forms.CharField(label='Никнейм', widget=forms.TextInput(
        attrs={'id': 'nameInput', 'class': 'form-control', 'type': 'text'}))
    about = forms.CharField(label='О себе', widget=forms.Textarea(
        attrs={'id': 'aboutInput', 'class': 'form-control', 'type': 'text'}), required=False)
    tg = forms.URLField(label='Telegaram', widget=forms.URLInput(attrs={'id': 'tgInput', 'class': 'form-control'}),
                        required=False)
    vk = forms.URLField(label='Vk', widget=forms.URLInput(attrs={'id': 'vkInput', 'class': 'form-control'}),
                        required=False)

    class Meta:
        model = PMUser
        fields = ('username', 'about', 'tg')
