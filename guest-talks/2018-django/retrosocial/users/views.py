from django.contrib.auth.models import User
from django.shortcuts import render

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
