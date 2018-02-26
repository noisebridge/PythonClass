from django.shortcuts import render


def home(request):
    return render(request, 'users/index.html', {})


def login(request):
    return render(request, 'users/login.html', {})
