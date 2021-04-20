from django.http import Http404
from django.shortcuts import render

from .models import Needy, state_choices
from .forms import HelpForm, NeedForm
#from .forms import RequestForm
# Create your views here.
from django.utils import timezone

# add source -- HelpForm -- helpingH
# add need -- NeedForm -- request


def index(request):
    return render(request, 'index.html')


def posts(request):
    posts = Needy.objects.all()
    newp = []
    for post in posts:
        if post.state == "MP":
            newp.append(post)
    return render(request, 'posts.html', {'posts': newp})


def add_source(request):
    if request.method == "POST":
        hh = HelpForm(request.POST)
        if hh.is_valid():
            hh.save()
            hhm = HelpForm()
            return render(request, 'helpingH.html', {'hhm': hhm, 'msg': 'Help added!', 'state_choices': state_choices})
        else:
            hhm = HelpForm()
            return render(request, 'helpingH.html', {'hhm': hh, 'msg': 'Check for Errors!!!', 'state_choices': state_choices})
    else:
        hhm = HelpForm()
        return render(request, 'helpingH.html', {'hhm': hhm, 'state_choices': state_choices})


def add_need(request):
    if request.method == "POST":
        nd = NeedForm(request.POST)
        if nd.is_valid():
            nd.save()
            nd_new = NeedForm()
            return render(request, 'request.html', {'hhm': nd_new, 'msg': 'Help added :)', 'state_choices': state_choices})
        else:
            nd = NeedForm()
            return render(request, 'request.html', {'hhm': nd, 'msg': 'Check for Errors!!!', 'state_choices': state_choices})
    else:
        nd_new = NeedForm()
        return render(request, 'request.html', {'hhm': nd_new, 'state_choices': state_choices})


def fbform(request):
    return render(request, 'fbform.html')
