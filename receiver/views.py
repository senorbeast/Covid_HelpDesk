from django.http import Http404
from django.shortcuts import render

from .models import Needy, Res_type, City, State
from .forms import HelpForm, NeedForm
#from .forms import RequestForm
# Create your views here.
from django.utils import timezone

# add source -- HelpForm -- helpingH
# add need -- NeedForm -- request

res_type = Res_type.objects.all()


def index(request):
    return render(request, 'main.html')


def posts(request):
    posts = Needy.objects.all()
    res_type = Res_type.objects.all()
    return render(request, 'posts.html', {'posts': posts, 'res_type': res_type})

# ! Reloading after submiting adds duplicates in DB


def add_source(request):
    sts = State.objects.all()
    cts = City.objects.all()
    res_type = Res_type.objects.all()
    # res_type = enumerate(res_type)
    if request.method == "POST":
        hh = HelpForm(request.POST)
        if hh.is_valid():
            hh.save()
            hhm = HelpForm()
            return render(request, 'helpingH.html', {'hhm': hhm, 'msg': 'Help added!', 'sts': sts, 'cts': cts, 'res_type': res_type})
        else:
            hhm = HelpForm()
            return render(request, 'helpingH.html', {'hhm': hh, 'msg': 'Check for Errors!!!',  'sts': sts, 'cts': cts, 'res_type': res_type})
    else:
        hhm = HelpForm()
        return render(request, 'helpingH.html', {'hhm': hhm,  'sts': sts, 'cts': cts,  'res_type': res_type})


def add_need(request):
    sts = State.objects.all()
    cts = City.objects.all()
    res_type = Res_type.objects.all()
    if request.method == "POST":
        nd = NeedForm(request.POST)
        if nd.is_valid():
            nd.save()
            nd_new = NeedForm()
            return render(request, 'request.html', {'hhm': nd_new, 'msg': 'Help added :)', 'sts': sts, 'cts': cts})
        else:
            nd_new = NeedForm()
            return render(request, 'request.html', {'hhm': nd, 'msg': 'Check for Errors!!!', 'sts': sts, 'cts': cts})
    else:
        nd_new = NeedForm()
        return render(request, 'request.html', {'hhm': nd_new})


def fbform(request):
    return render(request, 'fbform.html')


def about(request):
    return render(request, 'about.html')

# AJAX


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
