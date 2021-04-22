from django.http import Http404
from django.shortcuts import render

from .models import Needy, City, Res_type, State
from .forms import FeebackForm, HelpForm, NeedForm, Post_filt
#from .forms import RequestForm
# Create your views here.

# Resource -- HelpForm  -- add source-- helpingH
# Needy-- NeedForm --add need -- request


def index(request):
    return render(request, 'main.html')


def posts(request):
    posts = Needy.objects.all()
    pf_new = Post_filt()
    if request.method == "POST":
        pf = Post_filt(request.POST)
        return render(request, 'posts.html', {'posts': posts, 'pf': pf})
    return render(request, 'posts.html', {'posts': posts, 'pf': pf_new})

# ! Reloading after submiting adds duplicates in DB


def add_source(request):
    # res_type = enumerate(res_type)
    if request.method == "POST":
        hh = HelpForm(request.POST)
        if hh.is_valid():
            hh.save()
            hhm = HelpForm()
            return render(request, 'helpingH.html', {'hhm': hhm, 'msg': 'Help added!'})
        else:
            hhm = HelpForm()
            return render(request, 'helpingH.html', {'hhm': hh, 'msg': 'Check for Errors!!!'})
    else:
        hhm = HelpForm()
        return render(request, 'helpingH.html', {'hhm': hhm})


def add_need(request):
    if request.method == "POST":
        nd = NeedForm(request.POST)
        if nd.is_valid():
            nd.save()
            nd_new = NeedForm()
            return render(request, 'request.html', {'hhm': nd_new, 'msg': 'Help added :)'})
        else:
            nd_new = NeedForm()
            return render(request, 'request.html', {'hhm': nd, 'msg': 'Check for Errors!!!'})
    else:
        nd_new = NeedForm()
        return render(request, 'request.html', {'hhm': nd_new})


def fbform(request):
    if request.method == "POST":
        fb = FeebackForm(request.POST)
        if fb.is_valid():
            fb.save()
            fd_new = FeebackForm()
            return render(request,  'fbform.html', {'hhm': fd_new, 'msg': 'Feedback added :)'})
        else:
            fd_new = FeebackForm()
            return render(request,  'fbform.html', {'hhm': fb, 'msg': 'Check for Errors!!!'})
    else:
        fd_new = FeebackForm()
        return render(request,  'fbform.html', {'hhm': fd_new})


def about(request):
    return render(request, 'about.html')


# AJAX


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def newPostCards(request):
    state_id = request.GET.get('state_id')
    needies = Needy.objects.filter(state_id=state_id).all()
    city_id = request.GET.get('city_id')
    if city_id:
        needies = Needy.objects.filter(city_id=city_id).all()
    resource_name_id = request.GET.get('resource_name_id')
    if resource_name_id:
        needies = Needy.objects.filter(resource_name_id=resource_name_id).all()
    show_all_id = request.GET.get('show_all_id')
    if show_all_id:
        needies = Needy.objects.get.all()
    return render(request, 'posts_cards.html', {'posts': needies})
