from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('deleteResource/<int:pk>', views.deleteResource, name='deleteResource'),
    path('editResource/<int:pk>', views.editResource, name='editResource'),
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
