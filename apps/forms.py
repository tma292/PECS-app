from django import forms
from django.contrib.auth.models import User
from . import models
import random
import string


class ImageForm(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset=models.Category.objects.all(), empty_label="Choose the category")
    class Meta:
        model = models.Image
        fields = ['label', 'image', 'public', 'audio', 'category']


class FolderForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name']

class AddForm(forms.Form):
    image_id = forms.IntegerField()
    board = forms.ModelChoiceField(queryset=models.Board.objects.all(), empty_label="Choose the Board")
    tab = forms.ModelChoiceField(queryset=models.Tab.objects.all(), empty_label="Choose the Tab")
