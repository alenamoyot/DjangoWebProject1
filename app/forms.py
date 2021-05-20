"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from.models import Blog


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    tel = forms.CharField(label='Номер телефона', min_length=2, max_length=12)                          
    gender = forms.ChoiceField(label='Ваш пол',
                               choices=[('1','Мужской'), ('2','Женский')],
                               widget=forms.RadioSelect, initial=1)
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',
                                required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='Оставьте свой отзыв:',
                              widget=forms.Textarea(attrs={'rows':10, 'cols':40}))

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog #используемая модель
        fields = ('title', 'description', 'content', 'posted', 'author', 'image',)
        labels = {'title':"Заголовок",'description':"Краткое описание", 'content':"Содержание", 'posted':"Дата", 'author':"Автор", 'image':"Изображение",}