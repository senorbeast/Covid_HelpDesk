from django.http import Http404
from django.shortcuts import render, redirect

from .models import Needy, City, Res_type, State, Resource
from .forms import FeebackForm, HelpForm, NeedForm, Post_filt, Res_filt
from django.contrib import messages


from .forms import UserRegisterForm

#from .forms import RequestForm
# Create your views here.

# Resource -- HelpForm  -- add source-- helpingH
# Needy-- NeedForm --add need -- request


def index(request):
    return render(request, 'main.html')

# Needy posts


def posts(request):
    posts = Needy.objects.all()
    pf_new = Post_filt()
    if request.method == "POST":
        pf = Post_filt(request.POST)
        return render(request, 'posts.html', {'posts': posts, 'pf': pf})
    return render(request, 'posts.html', {'posts': posts, 'pf': pf_new})


def newPostCards(request):  # For filtering with AJAX
    state_id = request.GET.get('state_id')
    city_id = request.GET.get('city_id')
    resource_name_id = request.GET.get('resource_name_id')
    show_all_id = request.GET.get('show_all_id')
    needies = Needy.objects.all()
    if int(state_id) != 0:
        needies = needies.filter(state_id=state_id)
    if int(city_id) != 0:
        needies = needies.filter(city_id=city_id)
    if int(resource_name_id) != 0:
        needies = needies.filter(resource_name_id=resource_name_id)
    return render(request, 'posts_cards.html', {'posts': needies})

# Resources  posts


def resources(request):
    posts = Resource.objects.all().order_by('-verified')
    pf_new = Res_filt()
    if request.method == "POST":
        pf = Res_filt(request.POST)
        return render(request, 'resources.html', {'posts': posts, 'pf': pf})
    return render(request, 'resources.html', {'posts': posts, 'pf': pf_new})


def newResCards(request):  # For filtering with AJAX
    state_id = request.GET.get('state_id')
    city_id = request.GET.get('city_id')
    resource_name_id = request.GET.get('resource_name_id')
    show_all_id = request.GET.get('show_all_id')
    res = Resource.objects.all().order_by('-verified')
    if int(state_id) != 0:
        res = res.filter(state_id=state_id)
    if int(city_id) != 0:
        res = res.filter(city_id=city_id)
    if int(resource_name_id) != 0:
        res = res.filter(resource_name_id=resource_name_id)
    return render(request, 'resource_cards.html', {'posts': res})


# ! Reloading after submiting adds duplicates in DB

# Helping hand, adds a resource

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

# Request form, adds Needy


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

# Feedback


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


def disclaimer(request):
    return render(request, 'disclaimer.html')


def privacy(request):
    return render(request, 'privacy.html')

# For loading filtered cities with AJAX


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.all()
    if int(state_id) != 0:
        cities = cities.filter(state_id=state_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def editResource(request, pk):
    if request.method == "POST":
        res = Resource.objects.get(id=pk)
        hh = HelpForm(request.POST, instance=res)
        if hh.is_valid():
            hh.save()
            hhm = HelpForm()
            return render(request, 'editResource.html', {'hhm': hhm, 'msg': 'Help added!'})
        else:
            hhm = HelpForm()
            return render(request, 'editResource.html', {'hhm': hh, 'msg': 'Check for Errors!!!'})
    else:
        res = Resource.objects.get(id=pk)
        hhm = HelpForm(instance=res)
        name = res.contact_name
        email = res.email_id
        web_site = res.web_site
        phone = res.phone
        verified = res.verified
        description = res.description

        context = {
            'name': name,
            'hhm': hhm,
            'email': email,
            'web_site': web_site,
            'phone': phone,
            'description': description,
            'verified': verified,
        }

        return render(request, 'editResource.html', context)


def deleteResource(request, pk):
    res = Resource.objects.get(id=pk)
    res.delete()
    return redirect('resources')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "Acccount created successfully! You may login now.")

            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
