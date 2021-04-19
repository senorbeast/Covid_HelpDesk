from django.http import Http404
from django.shortcuts import render

from .models import Needy
# Create your views here.


def index(request):
    return render(request, 'index.html')


def posts(request):
    posts = Needy.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def add_post(request):
    return render(request, 'contact.html')
