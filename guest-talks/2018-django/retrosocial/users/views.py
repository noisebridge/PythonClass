from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

import channels
from asgiref.sync import async_to_sync

from users.models import Post, PostForm

from .consumers import GROUP_NAME


channel_layer = channels.layers.get_channel_layer()


def notify_new_post(username, text):
    async_to_sync(channel_layer.group_send)(
        GROUP_NAME,
        {
            'type': 'update_feed',
            'text': text,
            'username': username
        }
    )


def home(request):
    if request.method == 'POST':
        post = PostForm(request.POST).save(commit=False)
        post.user = request.user
        post.save()

        notify_new_post(request.user.username, post.text)

    users = User.objects.all()
    posts = Post.objects.all()

    post_form = PostForm()

    return render(request, 'users/index.html', {
        'users': users,
        'posts': posts,
        'form': post_form
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
