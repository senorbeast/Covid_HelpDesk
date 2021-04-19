from django.http import Http404
from django.shortcuts import render

from .models import Needy
#from .forms import RequestForm
# Create your views here.
from django.utils import timezone


def index(request):
    return render(request, 'index.html')


def posts(request):
    posts = Needy.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def add_post(request):
    # if request.method == 'POST':
    #     #form = RequestForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         pub_date = timezone.now()
    #         req = form.cleaned_data['req']
    #         state_choice = form.cleaned_data['state_choice']
    #         query = Needy(name=name, pub_date=pub_date,
    #                       req=req, state_choice=state_choice)
    #         query.save()
    return render(request, 'contact.html')
