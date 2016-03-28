# coding: utf-8
from django import forms

from post.models import Post


class PostForm(forms.Form):
    title = forms.CharField(label=u'Заголовок')
    sign = forms.CharField(label=u'Подпись')
    picture = forms.ImageField(label=u'Картина')
    is_published = forms.BooleanField(label=u'Опубликовать сейчас')
    #gallery = forms.ModelForm(label=u'Привязка к галерее')

class SearchForm(forms.Form):
    query = forms.CharField(label=u'Поиск: ', max_length=100)