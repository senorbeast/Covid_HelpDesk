from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('addpost', views.add_need, name='addpost'),
    path('addhelp', views.add_source, name='addhelp'),
    path('fbform', views.fbform, name='fbform'),
    path('about', views.about, name='about'),
    path('ajax/load-cities/', views.load_cities,
         name='ajax_load_cities'),  # AJAX
    path('newpostCards', views.newPostCards,
         name='newpostCards'),  # AJAX
]
