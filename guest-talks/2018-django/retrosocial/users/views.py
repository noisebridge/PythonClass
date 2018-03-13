from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from users.models import Post, PostForm


def home(request):
    if request.method == 'POST':
        post = PostForm(request.POST).save(commit=False)
        post.user = request.user
        post.save()

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
