from django.shortcuts import render

from .models import Post

def post_list(request):
    data_post = Post.objects.all()
    context = {'data_post': data_post}
    return render(request, 'gr_list/main.html', context)
