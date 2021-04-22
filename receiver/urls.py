from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),  # All Resources
    path('deleteResource/<int:pk>', views.deleteResource, name='deleteResource'),
    path('editResource/<int:pk>', views.editResource, name='editResource'),
    path('posts', views.posts, name='posts'),  # Needy posts
    path('addpost', views.add_need, name='addpost'),
    path('addhelp', views.add_source, name='addhelp'),  # Add new resource
    path('fbform', views.fbform, name='fbform'),
    path('about', views.about, name='about'),
    path('ajax/load-cities/', views.load_cities,
         name='ajax_load_cities'),  # For filtering cities with AJAX
    path('newpostCards', views.newPostCards,
         name='newpostCards'),  # For filtering needy post with  AJAX
    path('newresCards', views.newResCards,
         name='newresCards'),  # For filtering resources with AJAX
]
