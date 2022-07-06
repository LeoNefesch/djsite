from django import forms

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Researchers
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
