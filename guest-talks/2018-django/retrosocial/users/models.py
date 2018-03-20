from django import forms
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class PostForm(forms.ModelForm):
    def __init__(self, data=None):
        super().__init__(data)
        self.fields['text'].widget.attrs.update({'autofocus': 'true'})

    class Meta:
        model = Post
        fields = ['text']
