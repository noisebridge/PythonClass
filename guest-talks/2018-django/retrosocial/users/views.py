from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView

from users.models import Post, PostForm


def home(request):
    users = User.objects.all()
    posts = Post.objects.all()

    post_form = PostForm()

    return render(request, 'users/index.html', {
        'users': users,
        'posts': posts,
        'form': post_form
    })


class PostCreateView(CreateView):
    model = Post
    fields = ['text']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()

        return HttpResponseRedirect('/')
