from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})


def login(request):
    return render(request, 'users/login.html', {})
