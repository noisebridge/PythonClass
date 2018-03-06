from django import forms
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.CASCADE
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
