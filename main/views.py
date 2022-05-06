from django.shortcuts import render
from django.contrib.auth import logout


def home(request):
    return render(request, 'main/home.html')


def logout_view(request):
    logout(request)
